#!/usr/bin/env python3
"""Gráficos SVG del análisis competitivo (PAN-CBA). Salida: esta carpeta.
Paleta categórica validada (dataviz validate_palette, modo claro): #B12028 · #F18A00 · #1F6FD0.
Cada marca lleva <title> (tooltip nativo) y rótulo visible con el valor.
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(os.path.dirname(HERE), "datos")
INK, INK2, GRID = "#404040", "#7a7a7a", "#E6E6E6"
C_PAN, C_CAFE, C_OTRO = "#B12028", "#F18A00", "#1F6FD0"
FONT = "font-family=\"Montserrat,Segoe UI,Arial,sans-serif\""


def esc(s):
    return html.escape(str(s))


def save(name, svg):
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(svg)


def bar_h(rows, fname, title, unit="", fmt=lambda v: f"{v}", color=C_PAN, w=760, band=None, note=""):
    """rows: [(label, value, sublabel)] barras horizontales de un solo color."""
    lw, top, rh = 230, 46, 30
    h = top + rh * len(rows) + 46
    vmax = max(r[1] for r in rows) * 1.12
    if band:
        vmax = max(vmax, band[1] * 1.1)
    X = lambda v: lw + (w - lw - 70) * v / vmax
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT} role="img" aria-label="{esc(title)}">',
         f'<text x="0" y="18" font-size="15" font-weight="800" fill="{INK}">{esc(title)}</text>']
    for t in range(0, 5):
        v = vmax * t / 4
        o.append(f'<line x1="{X(v):.1f}" y1="{top - 6}" x2="{X(v):.1f}" y2="{top + rh * len(rows)}" stroke="{GRID}"/>')
    if band:
        o.append(f'<rect x="{X(band[0]):.1f}" y="{top - 8}" width="{X(band[1]) - X(band[0]):.1f}" height="{rh * len(rows) + 8}" fill="#1F6FD0" fill-opacity=".10" stroke="#1F6FD0" stroke-dasharray="4 3"/>'
                 f'<text x="{(X(band[0]) + X(band[1])) / 2:.1f}" y="{top - 12}" text-anchor="middle" font-size="11" font-weight="700" fill="#1F6FD0">{esc(band[2])}</text>')
    for i, (lab, v, sub) in enumerate(rows):
        y = top + i * rh
        o.append(f'<text x="{lw - 10}" y="{y + 13}" text-anchor="end" font-size="12.5" fill="{INK}">{esc(lab)}</text>')
        if sub:
            o.append(f'<text x="{lw - 10}" y="{y + 25}" text-anchor="end" font-size="10" fill="{INK2}">{esc(sub)}</text>')
        x0, x1 = X(0), X(v)
        o.append(f'<g><title>{esc(lab)}: {esc(fmt(v))}{esc(unit)}</title><rect x="{x0}" y="{y + 4}" width="{max(2, x1 - x0):.1f}" height="16" rx="4" fill="{color}"/></g>'
                 f'<text x="{x1 + 6:.1f}" y="{y + 16}" font-size="12" font-weight="700" fill="{INK}">{esc(fmt(v))}{esc(unit)}</text>')
    if note:
        o.append(f'<text x="0" y="{h - 10}" font-size="10.5" fill="{INK2}">{esc(note)}</text>')
    o.append("</svg>")
    save(fname, "".join(o))


def bar_range(rows, fname, title, unit="", fmt=lambda v: f"{v}", color=C_PAN, w=760, band=None, note=""):
    """rows: [(label, lo, hi, sublabel)] barras de rango (mín–máx)."""
    lw, top, rh = 250, 50, 30
    h = top + rh * len(rows) + 46
    vmax = max(r[2] for r in rows) * 1.15
    if band:
        vmax = max(vmax, band[1] * 1.1)
    X = lambda v: lw + (w - lw - 80) * v / vmax
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT} role="img" aria-label="{esc(title)}">',
         f'<text x="0" y="18" font-size="15" font-weight="800" fill="{INK}">{esc(title)}</text>']
    step = 10 if vmax > 30 else 5
    for v in range(0, int(vmax) + 1, step):
        o.append(f'<line x1="{X(v):.1f}" y1="{top - 6}" x2="{X(v):.1f}" y2="{top + rh * len(rows)}" stroke="{GRID}"/>'
                 f'<text x="{X(v):.1f}" y="{top + rh * len(rows) + 14}" text-anchor="middle" font-size="10" fill="{INK2}">{esc(fmt(v))}</text>')
    if band:
        o.append(f'<rect x="{X(band[0]):.1f}" y="{top - 8}" width="{X(band[1]) - X(band[0]):.1f}" height="{rh * len(rows) + 8}" fill="#1F6FD0" fill-opacity=".10" stroke="#1F6FD0" stroke-dasharray="4 3"/>'
                 f'<text x="{(X(band[0]) + X(band[1])) / 2:.1f}" y="{top - 14}" text-anchor="middle" font-size="11" font-weight="700" fill="#1F6FD0">{esc(band[2])}</text>')
    for i, (lab, lo, hi, sub) in enumerate(rows):
        y = top + i * rh
        o.append(f'<text x="{lw - 10}" y="{y + 13}" text-anchor="end" font-size="12.5" fill="{INK}">{esc(lab)}</text>')
        if sub:
            o.append(f'<text x="{lw - 10}" y="{y + 25}" text-anchor="end" font-size="10" fill="{INK2}">{esc(sub)}</text>')
        x0, x1 = X(lo), X(hi)
        o.append(f'<g><title>{esc(lab)}: {esc(fmt(lo))}–{esc(fmt(hi))}{esc(unit)}</title><rect x="{x0:.1f}" y="{y + 4}" width="{max(3, x1 - x0):.1f}" height="16" rx="4" fill="{color}"/></g>'
                 f'<text x="{x1 + 6:.1f}" y="{y + 16}" font-size="12" font-weight="700" fill="{INK}">{esc(fmt(lo))}–{esc(fmt(hi))}{esc(unit)}</text>')
    if note:
        o.append(f'<text x="0" y="{h - 8}" font-size="10.5" fill="{INK2}">{esc(note)}</text>')
    o.append("</svg>")
    save(fname, "".join(o))


def zonas():
    res = json.load(open(os.path.join(DATOS, "resumen_zonas.json"), encoding="utf-8"))
    grupos = {"Panaderías": (["cadena_panaderia", "panaderia_barrio", "bakery_cafe"], C_PAN),
              "Café, medialunas y pastelería": (["especialidad", "cafeteria_cadena", "medialuneria_dulces"], C_CAFE),
              "Otros formatos": (["fast_food", "conveniencia", "supermercado", "otro"], C_OTRO)}
    w, lw, top, rh = 760, 250, 58, 30
    rows = list(res.items())
    h = top + rh * len(rows) + 40
    vmax = max(v["total"] for _, v in rows) * 1.15 or 1
    X = lambda v: (w - lw - 60) * v / vmax
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT} role="img" aria-label="Locales relevados por zona y tipo">',
         f'<text x="0" y="18" font-size="15" font-weight="800" fill="{INK}">Locales relevados por zona y tipo</text>']
    lx = 0
    for g, (_, col) in grupos.items():
        o.append(f'<rect x="{lx}" y="30" width="12" height="12" rx="3" fill="{col}"/><text x="{lx + 17}" y="40" font-size="11.5" fill="{INK}">{esc(g)}</text>')
        lx += 30 + 7 * len(g)
    for i, (z, v) in enumerate(rows):
        y = top + i * rh
        o.append(f'<text x="{lw - 10}" y="{y + 15}" text-anchor="end" font-size="12" fill="{INK}">{z} · {esc(v["zona"])}</text>')
        x = lw
        for g, (ks, col) in grupos.items():
            n = sum(v["por_tipo"].get(k, 0) for k in ks)
            if n:
                ww = X(n)
                o.append(f'<g><title>{z} {esc(v["zona"])} — {esc(g)}: {n}</title><rect x="{x:.1f}" y="{y + 4}" width="{max(ww - 2, 1):.1f}" height="16" rx="3" fill="{col}"/></g>')
                x += ww
        o.append(f'<text x="{x + 6:.1f}" y="{y + 16}" font-size="12" font-weight="700" fill="{INK}">{v["total"]}</text>')
    o.append(f'<text x="0" y="{h - 8}" font-size="10.5" fill="{INK2}">Relevamiento de escritorio (28/09/2026), no censo: las panaderías de barrio y la periferia están subrepresentadas. Ver mapa en vivo (OSM).</text>')
    o.append("</svg>")
    save("zonas_por_tipo.svg", "".join(o))


def posicionamiento(ykey="experiencia_1a10", ylab="Experiencia (1–10)", fname="posicionamiento_precio_experiencia.svg",
                    title="Mapa de posicionamiento: precio × experiencia", hueco=(5, 6.5, 6, 7.5, "Hueco: precio medio + experiencia media-alta")):
    d = [x for x in json.load(open(os.path.join(DATOS, "posicionamiento_marcas.json"), encoding="utf-8")) if x.get("precio_1a10") and x.get(ykey)]
    w, h, m = 760, 560, 62
    X = lambda v: m + (w - m - 30) * (v - 0.5) / 10
    Y = lambda v: h - m - (h - m - 40) * (v - 0.5) / 10
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {FONT} role="img" aria-label="{esc(title)}">',
         f'<text x="0" y="18" font-size="15" font-weight="800" fill="{INK}">{esc(title)}</text>']
    for t in range(1, 11):
        o.append(f'<line x1="{X(t):.0f}" y1="{Y(0.5):.0f}" x2="{X(t):.0f}" y2="{Y(10.5):.0f}" stroke="{GRID}"/><line x1="{X(0.5):.0f}" y1="{Y(t):.0f}" x2="{X(10.5):.0f}" y2="{Y(t):.0f}" stroke="{GRID}"/>'
                 f'<text x="{X(t):.0f}" y="{Y(0.5) + 16:.0f}" text-anchor="middle" font-size="10.5" fill="{INK2}">{t}</text><text x="{X(0.5) - 8:.0f}" y="{Y(t) + 4:.0f}" text-anchor="end" font-size="10.5" fill="{INK2}">{t}</text>')
    o.append(f'<text x="{(X(0.5) + X(10.5)) / 2:.0f}" y="{h - 14}" text-anchor="middle" font-size="12" fill="{INK}">Precio percibido (1 = barato · 10 = caro)</text>'
             f'<text transform="translate(16,{(Y(0.5) + Y(10.5)) / 2:.0f}) rotate(-90)" text-anchor="middle" font-size="12" fill="{INK}">{esc(ylab)}</text>')
    if hueco:
        x0, x1, y0, y1, lab = hueco
        o.append(f'<rect x="{X(x0):.0f}" y="{Y(y1):.0f}" width="{X(x1) - X(x0):.0f}" height="{Y(y0) - Y(y1):.0f}" fill="{C_OTRO}" fill-opacity=".10" stroke="{C_OTRO}" stroke-dasharray="5 4"/>'
                 f'<text x="{X(x0) + 4:.0f}" y="{Y(y1) - 6:.0f}" font-size="11" font-weight="700" fill="{C_OTRO}">{esc(lab)}</text>')
    short = lambda n: n.replace("Panadería ", "").replace(" Córdoba", "").replace(" Medialunas", "")
    groups = {}
    for x in d:
        groups.setdefault((x["precio_1a10"], x[ykey]), []).append(x)
    for (px, py), xs in groups.items():
        cx, cy = X(px), Y(py)
        right_busy = any(k != (px, py) and k[1] == py and 0 < k[0] - px <= 1.6 for k in groups)
        anchor, dx = ("end", -11) if right_busy else ("start", 11)
        tip = "; ".join(f"{x['marca']} (foco: {x.get('foco', '')})" for x in xs)
        o.append(f'<g><title>{esc(tip)} — precio {px}, {esc(ylab)} {py}</title><circle cx="{cx:.0f}" cy="{cy:.0f}" r="7" fill="{C_PAN}" stroke="#fff" stroke-width="2"/></g>')
        for j, x in enumerate(xs):
            yy = cy + 4 + (j - (len(xs) - 1) / 2) * 13
            o.append(f'<text x="{cx + dx:.0f}" y="{yy:.0f}" text-anchor="{anchor}" font-size="11.5" fill="{INK}" stroke="#fff" stroke-width="3" paint-order="stroke">{esc(short(x["marca"]))}</text>')
    o.append(f'<text x="{w - 6}" y="{h - 30}" text-anchor="end" font-size="10" fill="{INK2}">Puntajes 1–10 = [INTERPRETACIÓN] del analista a partir de precios, reseñas y comunicación (I015–I016).</text>')
    o.append("</svg>")
    save(fname, "".join(o))


def main():
    zonas()
    posicionamiento()
    posicionamiento("conveniencia_1a10", "Conveniencia (horario, cobertura, apps)", "posicionamiento_precio_conveniencia.svg",
                    "Mapa de posicionamiento: precio × conveniencia", None)
    bar_h([("Mostaza", 3600, "fecha s/d"), ("Café Martínez", 6900, "sep-2026 (nacional)"), ("Havanna", 7000, "~2025, no confirmado"),
           ("YPF Full (CABA)", 7700, "ago-2026, no verificado"), ("Especialidad Córdoba", 8200, "estimado: espresso + 2 medialunas, oct-2025"),
           ("Panicafé (Rappi)", 6850, "café con leche + 2, oct-2026"), ("Lapana (PedidosYa)", 7700, "café con leche + 2 mafaldas, oct-2026"),
           ("Starbucks", 9700, "may-2025")], "escalera_combo_desayuno.svg",
          "Escalera de precios: café + 2 medialunas (ARS)", fmt=lambda v: f"${v:,.0f}".replace(",", "."), color=C_PAN,
          band=(4500, 5500, "Hueco de precio tentativo"),
          note="Precios de fuentes y fechas distintas; comparar como orden de magnitud. Fuente: I015 (c4) e I014h (apps, oct-2026).")
    bar_h([("Café Martínez (nacional)", 178000, "cuenta oficial del país"), ("Culpa de los Dos", 155000, "3–6 locales"), ("La Celeste", 94000, "16 locales"),
           ("Cherry Season", 94000, "3 locales"), ("Lo+Rico", 37000, "~30 locales"), ("Perdú", 35000, "7 locales"), ("Superanfibio", 27000, "1–3 locales"),
           ("Ethiopia Café", 23000, "1 local"), ("La Capke Go!", 21000, "1–2 locales"), ("Del Pilar", 20000, "35–45 locales"), ("Kråke Café", 11000, "1 local"),
           ("Independencia", 5866, "12 locales"), ("Medialunas 707 (NC)", 4023, "7 locales")], "instagram_seguidores.svg",
          "Seguidores en Instagram por marca", fmt=lambda v: f"{v / 1000:.0f} mil" if v >= 10000 else f"{v:,}".replace(",", "."), color=C_CAFE,
          note="Fragmentos de buscador, sep-2026. La audiencia no crece con la cantidad de locales: crece con el producto de culto y la experiencia.")
    bar_h([("Belgrano 439", 4.4, "2.376 reseñas"), ("Ituzaingó", 4.3, "536"), ("M. T. de Alvear 227", 4.3, "514"), ("Obispo Oro 384", 4.2, "652"),
           ("Av. Colón 375", 3.6, "446"), ("Obispo Trejo 1029", 2.9, "1.292"), ("Buenos Aires 1064", 2.6, "486")], "la_celeste_resenas.svg",
          "La Celeste: puntaje por sucursal (Restaurantguru, 1–5)", fmt=lambda v: f"{v:.1f}".replace(".", ","), color=C_PAN,
          note="Misma marca, experiencia muy distinta según el local: el principal punto débil de la red.")
    bar_h([("La Celeste", 15, "declarado 16"), ("Del Pilar", 19, "declarado 35–45 (incluye alrededores)"), ("El Vergel", 14, "s/d"),
           ("Medialunas 707", 11, "s/d"), ("Andrea Franceschini", 11, "7 oficiales + dudosos"), ("Independencia", 9, "declarado 12–15"),
           ("Armando", 9, "declarado 8 → meta 13"), ("Lo+Rico", 10, "declarado 20–26 panaderías"), ("Panicafé", 8, "s/d"), ("Lapana", 8, "s/d"),
           ("Perdú", 7, "s/d"), ("Catriel", 4, "declarado 4"), ("Pugliese", 4, "s/d"), ("Culpa de los Dos", 3, "declarado 5–6")],
          "cadenas_locales.svg", "Cadenas locales: sucursales relevadas con dirección en Córdoba Capital",
          color=C_PAN, note="Relevamiento de escritorio al 02/10/2026 (I014 v2 + I014h). 'Declarado' = lo que informa la marca o la prensa.")
    bar_range([("Centro peatonal", 35, 42, "1 aviso"), ("Valle Escondido (Z08)", 18, 22, "3 avisos"), ("Nueva Córdoba (Z02)", 15, 24, "8 avisos"),
               ("Centro fuera de peatonal", 11, 21, "4 avisos"), ("Argüello / V. Belgrano (Z08)", 8.5, 19, "3 avisos"), ("Güemes (Z03)", 9, 20, "1 aviso: poco confiable"),
               ("Manantiales (Z09)", 8, 18, "4 avisos"), ("Alberdi / Colón (Z04)", 6, 16, "4 avisos"), ("Villa Cabrera / Urca (Z07)", 5, 13, "8 avisos"),
               ("Cerro / Rafael Núñez (Z07)", 9, 12, "4 avisos"), ("Alta Córdoba (Z06)", 7, 11, "1 aviso: poco confiable"), ("Jardín / O'Higgins (Z09)", 7, 11, "4 avisos"),
               ("General Paz (Z05)", 5.5, 10, "2 avisos: poco confiable")],
              "zonas_candidatas_alquiler.svg", "Alquiler de locales a la calle por zona (USD/m² por mes, oct-2026)",
              fmt=lambda v: f"{v:.0f}" if v == int(v) else f"{v:.1f}".replace(".", ","), color=C_CAFE,
              band=(25, 35, "Tope compatible para 100–120 m² (10–12% de ventas)"),
              note="Sin expensas ni IVA; TC $1.545. Avisos de portales vistos por buscador (I029, F1800–F1844). Verificar en el aviso antes de negociar.")
    bar_h([("El Vergel (Pablo Cabrera 2885)", 4.9, "2.014 reseñas · RG"), ("Armando Medialunas (Duarte Quirós)", 4.6, "451 · RG"),
           ("Panicafé Gral. Paz", 4.5, "4.058 · agregador 9/10"), ("Medialunas 707", 4.4, "1.010 · agregador 8,8/10"),
           ("La Celeste (mejor local)", 4.4, "Belgrano 439 · 2.376"), ("Pugliese (Río Bamba)", 4.2, "1.050 · RG"),
           ("Panicafé Cerro", 4.2, "+16.000 · agregador 8,4/10"), ("Del Pilar", 3.9, "414 · agregador 7,8/10"),
           ("Independencia", 3.8, "110 · RG"), ("Moreno", 3.7, "873 · RG"), ("Medialunas Calentitas (promedio)", 3.6, "6 locales: 3,1–4,0"),
           ("Perdú", 3.4, "544 · RG"), ("Lapana (Tripadvisor)", 3.4, "65"), ("La Platense", 3.4, "282 · RG"),
           ("Lo+Rico", 3.1, "agregador 6,2/10"), ("La Celeste (peor local)", 2.6, "Buenos Aires 1064 · 486")],
          "resenas_cadenas.svg", "Puntaje de reseñas: panaderías de medialunas, facturas y café (escala 1–5)",
          fmt=lambda v: f"{v:.1f}".replace(".", ","), color=C_PAN,
          note="RG = Restaurant Guru (agrega Google y otros). Escalas /10 divididas por 2. Fragmentos de buscador, oct-2026 (I016b, I016c, I014h).")
    print("OK gráficos")


if __name__ == "__main__":
    main()
