#!/usr/bin/env python3
"""Gráficos SVG del informe de mercado (reutiliza el estilo de 02_COMPETENCIA/graficos)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "02_COMPETENCIA", "graficos"))
import graficos as g  # noqa: E402
g.HERE = HERE

g.bar_h([("Horneado a demanda + pronóstico", 25, "impacto 5 × aplicabilidad 5"), ("Precio de entrada y porciones chicas", 25, "5 × 5"),
         ("QR y billeteras como fidelización", 20, "4 × 5"), ("Café de calidad estandarizado", 20, "5 × 4"),
         ("Delivery de medialunas (domingo)", 16, "4 × 4"), ("Masa madre y relato natural", 16, "4 × 4"),
         ("Producto emblema (hero)", 16, "4 × 4"), ("Cheaf / anti-desperdicio", 15, "3 × 5"),
         ("Suscripción de café", 12, "4 × 3"), ("Saludable y sin TACC envasado", 9, "3 × 3")],
        "tendencias_priorizadas.svg", "Tendencias priorizadas para PAN-CBA (impacto × aplicabilidad, máx. 25)",
        color=g.C_PAN, note="Puntajes = [INTERPRETACIÓN] a partir de I003/I004 (fuentes F800–F860).")
g.bar_h([("Panificados artesanales (TAM-a)", 227, "≈ $352.800 M/año"), ("Desayuno/merienda fuera del hogar (TAM-b)", 105, "≈ $163.800 M/año"),
         ("SAM: zonas ingreso medio-alto × segmento premium", 25, "≈ $38.700 M/año"), ("SOM: 1 local (250 tickets/día)", 0.377, "≈ $585 M/año")],
        "tam_sam_som.svg", "Tamaño de mercado estimado — Córdoba Capital (USD millones/año)", unit=" M",
        fmt=lambda v: f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".") if v < 10 else f"{v:,.0f}".replace(",", "."),
        color=g.C_CAFE, note="[ESTIMACIÓN] paramétrica sobre supuestos a validar (I005 §4). TC $1.545/USD (sep-2026).")
print("OK")
