#!/usr/bin/env python3
"""Gráficos SVG del informe de cliente: mapa de calor de ocasiones por franja y atractivo de segmentos.
Intensidades y puntajes = [ESTIMACIÓN] preliminar a partir de I006 (a validar con la encuesta I008)."""
import os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "02_COMPETENCIA", "graficos"))
import graficos as g  # noqa: E402
g.HERE = HERE

FR = ["6–8", "8–10", "10–12", "12–14", "14–16", "16–18", "18–20", "20–24", "0–6"]
SEG = [("Familias de barrio", [2, 3, 1, 0, 0, 1, 3, 1, 0]), ("Estudiantes universitarios", [2, 3, 2, 1, 1, 3, 2, 1, 0]),
       ("Oficinistas / centro", [3, 3, 1, 2, 1, 2, 1, 0, 0]), ("Jóvenes / centennials", [0, 1, 1, 1, 1, 3, 3, 2, 1]),
       ("Adultos mayores", [1, 3, 3, 1, 0, 1, 1, 0, 0]), ("Trabajadores por turnos", [3, 1, 0, 2, 1, 0, 0, 2, 2]),
       ("Consumidores nocturnos", [0, 0, 0, 0, 0, 0, 1, 3, 3]), ("Turistas", [0, 3, 2, 1, 1, 2, 1, 1, 0]),
       ("Empresas (catering)", [1, 3, 2, 1, 0, 1, 0, 0, 0]), ("Celíacos / saludables", [1, 2, 1, 1, 1, 2, 1, 0, 0])]
RAMP = ["#F4F4F4", "#FBD9A8", "#F5A742", "#B12028"]  # secuencial claro→oscuro (0 = sin demanda)
LAB = ["sin demanda", "baja", "media", "alta"]


def heat():
    lw, top, cw, ch = 200, 60, 58, 26
    w, h = lw + cw * len(FR) + 10, top + ch * len(SEG) + 50
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {g.FONT} role="img" aria-label="Mapa de calor de ocasiones por franja horaria">',
         f'<text x="0" y="18" font-size="15" font-weight="800" fill="{g.INK}">Cuándo compra cada segmento (intensidad estimada por franja horaria)</text>']
    for j, f in enumerate(FR):
        o.append(f'<text x="{lw + cw * j + cw / 2}" y="{top - 8}" text-anchor="middle" font-size="11" fill="{g.INK2}">{f} h</text>')
    for i, (s, vals) in enumerate(SEG):
        y = top + ch * i
        o.append(f'<text x="{lw - 8}" y="{y + 17}" text-anchor="end" font-size="12" fill="{g.INK}">{html.escape(s)}</text>')
        for j, v in enumerate(vals):
            o.append(f'<g><title>{html.escape(s)} · {FR[j]} h: {LAB[v]}</title><rect x="{lw + cw * j + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="3" fill="{RAMP[v]}"/></g>')
            if v:
                o.append(f'<text x="{lw + cw * j + cw / 2}" y="{y + 17}" text-anchor="middle" font-size="10.5" fill="{"#fff" if v == 3 else g.INK}">{LAB[v]}</text>')
    tot = [sum(v[j] for _, v in SEG) for j in range(len(FR))]
    y = top + ch * len(SEG) + 6
    o.append(f'<text x="{lw - 8}" y="{y + 14}" text-anchor="end" font-size="12" font-weight="700" fill="{g.INK}">Total (suma)</text>')
    for j, t in enumerate(tot):
        o.append(f'<text x="{lw + cw * j + cw / 2}" y="{y + 14}" text-anchor="middle" font-size="12" font-weight="800" fill="{g.INK}">{t}</text>')
    o.append(f'<text x="0" y="{h - 6}" font-size="10.5" fill="{g.INK2}">[ESTIMACIÓN] a partir de I006; se valida con encuesta (I008) y observación (I009). Domingo: pico de facturas y delivery (17 h).</text></svg>')
    g.save("ocasiones_por_franja.svg", "".join(o))


heat()
g.bar_h([("Oficinistas / centro", 25, "tamaño 3 · valor 4 · encaje 5"), ("Empresas (catering)", 25, "valor 5 · encaje 5 · tamaño 2"),
         ("Familias de barrio", 23, "tamaño 5 · replicable 5"), ("Estudiantes universitarios", 23, "tamaño 5 · valor 2"),
         ("Jóvenes / centennials", 21, "experiencia · delivery"), ("Trabajadores por turnos", 19, "insatisfechos · horario"),
         ("Turistas", 19, "ticket alto · estacional"), ("Adultos mayores", 18, "fieles · precio"),
         ("Celíacos / saludables", 18, "nicho · riesgo de contaminación"), ("Consumidores nocturnos", 16, "ocasional")],
        "atractivo_segmentos.svg", "Atractivo preliminar de segmentos (6 criterios × 1–5, máx. 30)", color=g.C_PAN,
        note="[ESTIMACIÓN] preliminar. Criterios: tamaño, valor, accesibilidad, insatisfacción, encaje con modelo de planta, replicabilidad.")
print("OK")
