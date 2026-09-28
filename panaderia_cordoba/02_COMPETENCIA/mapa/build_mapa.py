#!/usr/bin/env python3
"""Genera el mapa competitivo de Córdoba Capital (PAN-CBA).

Entradas (en ../datos/):
  geo_barrios.json          barrios con centroide aproximado, zona, población, NSE; corredores; hitos
  locales_competencia.json  un registro por local (marca, tipo, dirección, barrio, zona, …)
Salidas:
  ../MAPA_COMPETITIVO_CORDOBA.html   mapa interactivo (Leaflet embebido + plano OSM en el navegador)
  esquema_zonas.svg                  plano esquemático por zonas (para informes PDF)
  ../datos/resumen_zonas.json        conteos por zona y tipo
  ../datos/locales_competencia.csv   base en formato planilla

Requiere: shapely, scipy (sólo para generar; el HTML resultante es autónomo).
Las posiciones son APROXIMADAS: cada local se ubica en el centro de su barrio con un
desplazamiento en espiral para que no se superpongan. El plano de zonas es una
teselación (Voronoi) de los centros de barrio recortada al ejido (≈ cuadrado de 24 km).
"""
import csv
import html
import json
import math
import os
import re
import unicodedata
from collections import Counter, defaultdict
from urllib.parse import quote_plus

import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, box, mapping
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.dirname(HERE)
DATOS = os.path.join(COMP, "datos")

# Ejido de Córdoba Capital (aprox.): casi un cuadrado de ~24 km de lado
EJIDO = box(-64.316, -31.524, -64.061, -31.307)
ZONAS = {
    "Z01": "Centro", "Z02": "Nueva Córdoba", "Z03": "Güemes / Observatorio", "Z04": "Oeste",
    "Z05": "Este", "Z06": "Norte cercano", "Z07": "Noroeste", "Z08": "Norte premium / Noroeste lejano",
    "Z09": "Sur", "Z10": "Periferia",
}
ZCOLOR = {"Z01": "#F18A00", "Z02": "#E4572E", "Z03": "#B12028", "Z04": "#8E6C8A", "Z05": "#3B7EA1",
          "Z06": "#2E8B57", "Z07": "#C7A33A", "Z08": "#6A994E", "Z09": "#D1495B", "Z10": "#8D99AE"}
TIPOS = {
    "cadena_panaderia": ("Cadena de panaderías", "#B12028"),
    "panaderia_barrio": ("Panadería de barrio", "#F18A00"),
    "bakery_cafe": ("Bakery café / masa madre", "#7B2CBF"),
    "medialuneria_dulces": ("Medialunería / pastelería", "#E76F51"),
    "especialidad": ("Café de especialidad", "#2A9D8F"),
    "cafeteria_cadena": ("Cadena de café", "#264653"),
    "supermercado": ("Supermercado", "#6C757D"),
    "conveniencia": ("Tienda de conveniencia (estación)", "#3A86FF"),
    "fast_food": ("Comida rápida (desayuno)", "#8D6E63"),
    "otro": ("Otro", "#999999"),
}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def load():
    geo = json.load(open(os.path.join(DATOS, "geo_barrios.json"), encoding="utf-8"))
    locs = json.load(open(os.path.join(DATOS, "locales_competencia.json"), encoding="utf-8"))
    return geo, locs


def barrio_index(geo):
    idx = {}
    for b in geo["barrios"]:
        if b.get("lat") is None or b.get("lon") is None:
            continue
        if not EJIDO.buffer(0.02).contains(Polygon([(b["lon"], b["lat"])] * 3).centroid):
            continue
        idx[norm(b["barrio"])] = b
    return idx


def zone_polygons(geo):
    pts, zs = [], []
    for b in geo["barrios"]:
        if b.get("lat") is None or b.get("zona") not in ZONAS:
            continue
        pts.append((b["lon"], b["lat"]))
        zs.append(b["zona"])
    arr = np.array(pts)
    far = [(-65, -30), (-63, -30), (-65, -33), (-63, -33)]
    vor = Voronoi(np.vstack([arr, far]))
    cells = defaultdict(list)
    for i, z in enumerate(zs):
        reg = vor.regions[vor.point_region[i]]
        if -1 in reg or not reg:
            continue
        poly = Polygon([vor.vertices[v] for v in reg]).intersection(EJIDO)
        if not poly.is_empty:
            cells[z].append(poly)
    return {z: unary_union(p) for z, p in cells.items()}


def place(locs, bidx, geo):
    """Asigna lat/lon aproximados (centro del barrio + espiral)."""
    zone_centers = defaultdict(list)
    for b in geo["barrios"]:
        if b.get("lat") is not None and b.get("zona") in ZONAS:
            zone_centers[b["zona"]].append((b["lat"], b["lon"]))
    counter = Counter()
    placed = []
    for r in locs:
        lat, lon, prec = r.get("lat"), r.get("lon"), "exacta"
        if lat is None or lon is None:
            b = bidx.get(norm(r.get("barrio")))
            if not b:
                # coincidencia parcial de nombre de barrio
                nb = norm(r.get("barrio"))
                b = next((v for k, v in bidx.items() if nb and (nb in k or k in nb)), None)
            if b:
                lat, lon, prec, key = b["lat"], b["lon"], "barrio", norm(b["barrio"])
                if not r.get("zona"):
                    r["zona"] = b.get("zona")
            elif r.get("zona") in zone_centers:
                c = zone_centers[r["zona"]]
                lat, lon, prec, key = sum(x[0] for x in c) / len(c), sum(x[1] for x in c) / len(c), "zona", r["zona"]
            else:
                continue
            i = counter[key]
            counter[key] += 1
            ang, rad = i * 2.39996, 0.0011 * math.sqrt(i + 0.5)
            lat, lon = lat + rad * math.sin(ang), lon + rad * math.cos(ang) * 1.17
        r2 = dict(r)
        r2.update(_lat=round(lat, 6), _lon=round(lon, 6), _precision=prec)
        placed.append(r2)
    return placed


def gmaps(r):
    q = f"{r.get('marca', '')} {r.get('direccion') or r.get('barrio') or ''} Córdoba Argentina"
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)


def write_csv(locs):
    cols = ["marca", "tipo", "direccion", "barrio", "zona", "horario", "abre_24h", "delivery",
            "google_rating", "google_reviews", "fuente", "nota", "_precision"]
    with open(os.path.join(DATOS, "locales_competencia.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in locs:
            w.writerow([", ".join(r[c]) if isinstance(r.get(c), list) else r.get(c, "") for c in cols])


def summary(locs, geo):
    pop = defaultdict(int)
    for b in geo["barrios"]:
        if b.get("poblacion") and b.get("zona") in ZONAS:
            pop[b["zona"]] += int(b["poblacion"])
    res = {}
    for z, name in ZONAS.items():
        zl = [r for r in locs if r.get("zona") == z]
        c = Counter(r.get("tipo", "otro") for r in zl)
        res[z] = {"zona": name, "total": len(zl), "por_tipo": dict(c),
                  "panaderias": c.get("cadena_panaderia", 0) + c.get("panaderia_barrio", 0) + c.get("bakery_cafe", 0),
                  "poblacion_barrios_relevados": pop.get(z) or None}
    json.dump(res, open(os.path.join(DATOS, "resumen_zonas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return res


# ───────────── SVG esquemático ─────────────
def svg_map(zpolys, locs, geo, res, w=1000, h=1000, bounds=None, fname="esquema_zonas.svg", skip_labels=(), titulo=""):
    minx, miny, maxx, maxy = bounds or EJIDO.bounds
    frame = box(minx, miny, maxx, maxy)
    zpolys = {z: p.intersection(frame) for z, p in zpolys.items() if not p.intersection(frame).is_empty}
    locs = [r for r in locs if minx <= r["_lon"] <= maxx and miny <= r["_lat"] <= maxy]
    kx = math.cos(math.radians(31.41))
    sx = w / ((maxx - minx) * kx)
    sy = h / (maxy - miny)
    s = min(sx, sy)

    def P(lon, lat):
        return ((lon - minx) * kx * s, (maxy - lat) * s)

    def path(poly):
        polys = [poly] if poly.geom_type == "Polygon" else list(poly.geoms)
        d = ""
        for p in polys:
            d += "M" + " L".join(f"{P(x, y)[0]:.1f},{P(x, y)[1]:.1f}" for x, y in p.exterior.coords) + " Z "
        return d
    W, H = (maxx - minx) * kx * s, (maxy - miny) * s
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H + 60:.0f}" font-family="Montserrat,Segoe UI,Arial" role="img" aria-label="Plano esquemático de Córdoba Capital por zonas">',
           f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="#FBFBFB" stroke="#999" stroke-dasharray="6 4"/>']
    for z, poly in zpolys.items():
        out.append(f'<path d="{path(poly)}" fill="{ZCOLOR[z]}" fill-opacity="0.13" stroke="{ZCOLOR[z]}" stroke-width="1.5"/>')
    for c in geo.get("corredores", []):
        try:
            (a, b), (c2, d) = c["desde"], c["hasta"]
            x1, y1 = P(b, a)
            x2, y2 = P(d, c2)
            out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#555" stroke-width="2" stroke-opacity=".45"/>')
        except Exception:
            pass
    for r in sorted(locs, key=lambda r: r.get("tipo") == "panaderia_barrio", reverse=True):
        x, y = P(r["_lon"], r["_lat"])
        col = TIPOS.get(r.get("tipo"), TIPOS["otro"])[1]
        rad = 5.5 if r.get("tipo") == "cadena_panaderia" else 3.6
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{col}" fill-opacity=".85" stroke="#fff" stroke-width=".8"/>')
    for z, poly in zpolys.items():
        if z in skip_labels:
            continue
        c = poly.representative_point()
        x, y = P(c.x, c.y)
        n = res.get(z, {}).get("total", 0)
        out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-size="15" font-weight="800" fill="{ZCOLOR[z]}" stroke="#fff" stroke-width="4" paint-order="stroke">{z} · {html.escape(ZONAS[z])}</text>'
                   f'<text x="{x:.0f}" y="{y + 17:.0f}" text-anchor="middle" font-size="12.5" fill="#404040" stroke="#fff" stroke-width="3" paint-order="stroke">{n} locales relevados</text>')
    for hto in geo.get("hitos", []):
        if hto.get("lat") is None or not (minx <= hto["lon"] <= maxx and miny <= hto["lat"] <= maxy):
            continue
        x, y = P(hto["lon"], hto["lat"])
        out.append(f'<rect x="{x - 3.5:.1f}" y="{y - 3.5:.1f}" width="7" height="7" fill="#222"/><text x="{x + 6:.0f}" y="{y + 4:.0f}" font-size="10.5" fill="#222" stroke="#fff" stroke-width="2.5" paint-order="stroke">{html.escape(hto["nombre"])}</text>')
    # leyenda
    lx, ly = 10, H + 18
    for k in ["cadena_panaderia", "panaderia_barrio", "bakery_cafe", "medialuneria_dulces", "especialidad", "cafeteria_cadena", "conveniencia", "supermercado", "fast_food"]:
        lab, col = TIPOS[k]
        out.append(f'<circle cx="{lx + 5}" cy="{ly}" r="5" fill="{col}"/><text x="{lx + 14}" y="{ly + 4}" font-size="11.5" fill="#404040">{html.escape(lab)}</text>')
        lx += 14 + 7.2 * len(lab) + 18
        if lx > W - 180:
            lx, ly = 10, ly + 20
    out.append(f'<text x="{W - 8:.0f}" y="{H - 8:.0f}" text-anchor="end" font-size="10.5" fill="#808080">Esquema no a escala exacta · posiciones aproximadas por barrio{" · límite = ejido (≈24×24 km)" if not bounds else ""}</text>')
    if titulo:
        out.append(f'<text x="12" y="24" font-size="16" font-weight="800" fill="#F18A00" stroke="#fff" stroke-width="4" paint-order="stroke">{html.escape(titulo)}</text>')
    out.append("</svg>")
    svg = "".join(out)
    open(os.path.join(HERE, fname), "w", encoding="utf-8").write(svg)
    return svg


# ───────────── HTML interactivo ─────────────
def html_map(zpolys, locs, geo, res):
    vend = os.path.join(HERE, "vendor")
    lcss = open(os.path.join(vend, "leaflet.css"), encoding="utf-8").read()
    ljs = open(os.path.join(vend, "leaflet.js"), encoding="utf-8").read()
    feats = []
    for r in locs:
        feats.append({"m": r.get("marca"), "t": r.get("tipo", "otro"), "d": r.get("direccion") or "", "b": r.get("barrio") or "",
                      "z": r.get("zona") or "", "h": r.get("horario") or "", "h24": r.get("abre_24h"),
                      "dl": ", ".join(r["delivery"]) if isinstance(r.get("delivery"), list) else (r.get("delivery") or ""),
                      "gr": r.get("google_rating"), "gn": r.get("google_reviews"), "f": r.get("fuente") or "",
                      "n": r.get("nota") or "", "la": r["_lat"], "lo": r["_lon"], "p": r["_precision"], "g": gmaps(r)})
    zgeo = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "properties": {"z": z, "nombre": ZONAS[z], "color": ZCOLOR[z], **res.get(z, {})}, "geometry": mapping(p)}
        for z, p in zpolys.items()]}
    data = json.dumps({"locales": feats, "zonas": zgeo, "tipos": TIPOS, "zonasNombres": ZONAS,
                       "corredores": geo.get("corredores", []), "hitos": geo.get("hitos", []),
                       "barrios": [b for b in geo["barrios"] if b.get("lat") is not None]}, ensure_ascii=False)
    tpl = open(os.path.join(HERE, "plantilla_mapa.html"), encoding="utf-8").read()
    out = tpl.replace("/*LEAFLET_CSS*/", lcss).replace("/*LEAFLET_JS*/", ljs).replace("/*DATA*/", data)
    open(os.path.join(COMP, "MAPA_COMPETITIVO_CORDOBA.html"), "w", encoding="utf-8").write(out)


def main():
    geo, locs = load()
    bidx = barrio_index(geo)
    # deduplicar por marca + dirección
    seen, uniq = set(), []
    for r in locs:
        k = (norm(r.get("marca")), norm(r.get("direccion")) or norm(r.get("barrio")))
        if k in seen and k[1]:
            continue
        seen.add(k)
        uniq.append(r)
    placed = place(uniq, bidx, geo)
    zpolys = zone_polygons(geo)
    write_csv(placed)
    res = summary(placed, geo)
    svg_map(zpolys, placed, geo, res, skip_labels=("Z01", "Z02", "Z03"))
    svg_map(zpolys, placed, geo, res, bounds=(-64.215, -31.445, -64.160, -31.400), fname="esquema_centro.svg",
            )
    html_map(zpolys, placed, geo, res)
    sin = len(uniq) - len(placed)
    print(f"OK: {len(placed)} locales en el mapa ({sin} sin ubicar), {len(zpolys)} zonas")
    for z, v in res.items():
        print(f"  {z} {v['zona']:<32} {v['total']:>4}  {v['por_tipo']}")


if __name__ == "__main__":
    main()
