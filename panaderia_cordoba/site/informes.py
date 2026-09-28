#!/usr/bin/env python3
"""Genera versiones HTML + PDF (identidad Canalsenses) de los informes para socios.
Uso: python informes.py ruta/relativa/INFORME.md [...]   (rutas relativas a panaderia_cordoba/)
Requiere Chromium (Playwright) para el PDF: CHROME=/ruta/al/chrome.
"""
import os, re, subprocess, sys, html
import build  # reutiliza render_md (SVG embebidos, tablas, badges)

CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
CSS = """
:root{--brand:#F18A00;--brand2:#B12028;--tx:#404040;--tx2:#7a7a7a;--line:#E6E6E6;--soft:#FFF4E5}
*{box-sizing:border-box}body{margin:0;background:#fff;color:var(--tx);font-family:'Montserrat','Segoe UI',Helvetica,Arial,sans-serif;font-size:12.5px;line-height:1.5}
.wrap{max-width:1000px;margin:0 auto;padding:0 18px 30px}
header{border-bottom:3px solid var(--brand);padding:14px 0 10px;display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap}
.logo{font-weight:800;color:var(--brand);font-size:19px}.logo small{display:block;font-size:9.5px;color:var(--tx2);font-weight:600;letter-spacing:1.4px}
.meta{font-size:10.5px;color:var(--tx2);text-align:right}
h1{color:var(--brand);font-size:24px;margin:18px 0 8px}h2{color:var(--brand);font-size:17px;border-left:4px solid var(--brand);padding-left:8px;margin:24px 0 8px;break-after:avoid}
h3{color:var(--brand2);font-size:14px;margin:16px 0 6px;break-after:avoid}
.tw{overflow-x:auto;margin:8px 0 12px}table{border-collapse:collapse;width:100%;font-size:11px}
th{background:var(--brand);color:#fff;text-align:left;padding:5px 7px}td{border-bottom:1px solid var(--line);padding:4px 7px;vertical-align:top}
tr:nth-child(even) td{background:#FFFBF5}tr{break-inside:avoid}
blockquote{margin:8px 0;padding:6px 12px;border-left:4px solid var(--brand);background:var(--soft)}
code{background:#f3f3f3;padding:0 3px;border-radius:3px;font-size:10.5px}
.st{display:inline-block;font-size:10px;font-weight:700;border-radius:4px;padding:0 6px}.st.ok{background:#E8F5E9;color:#2E7D32}.st.pend{background:#FFF1DC;color:#A85800}.st.crit{background:#FBEDEE;color:#B12028}.st.mute{background:#F0F0F0;color:#666}
.fig{margin:10px 0;break-inside:avoid}.fig svg{max-width:100%;height:auto;display:block}
a{color:var(--brand2)}footer{margin-top:24px;border-top:1px solid var(--line);padding-top:6px;font-size:9.5px;color:var(--tx2);display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
@media print{@page{size:A4;margin:11mm}.wrap{max-width:none;padding:0}body{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""


def one(rel):
    src = os.path.join(build.ROOT, rel)
    text = open(src, encoding="utf-8").read()
    title = build.title_of(text, os.path.basename(rel))
    body = build.render_md(text, rel)
    code = re.search(r"\| Código \| ([^|]+)\|", text)
    code = code.group(1).strip() if code else ""
    out = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head><body><div class="wrap">
<header><div class="logo">CANALSENSES<small>ULTRACONGELADOS CANALSENSES S.R.L. · PROYECTO PANADERÍA PAN-CBA</small></div>
<div class="meta">{html.escape(code)}<br>Generado el {build.NOW:%d/%m/%Y} · Confidencial</div></header>
{body}
<footer><span>Ultracongelados Canalsenses S.R.L. · Proyecto PAN-CBA · Fuente: panaderia_cordoba/{html.escape(rel)}</span><span>Etiquetas: [HECHO] [ESTIMACIÓN] [INTERPRETACIÓN] [RECOMENDACIÓN]</span></footer>
</div></body></html>"""
    base = src[:-3]
    open(base + ".html", "w", encoding="utf-8").write(out)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={base}.pdf", "file://" + base + ".html"], capture_output=True, timeout=180)
    print("OK", base + ".html", "+ .pdf" if os.path.exists(base + ".pdf") else "(sin PDF)")


if __name__ == "__main__":
    for r in sys.argv[1:]:
        one(r)
