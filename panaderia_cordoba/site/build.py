#!/usr/bin/env python3
"""Genera el sitio web del proyecto PAN-CBA a partir de los .md del repositorio.

Uso:  python build.py            → genera ./dist
El sitio es estático: se puede publicar en Cloudflare Pages, Vercel o cualquier hosting.
"""
import html
import json
import os
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone, date

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "_vendor"))  # markdown incluido en el repo
import markdown  # noqa: E402

SITE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SITE)
DIST = os.path.join(SITE, "dist")
CFG = json.load(open(os.path.join(SITE, "config.json"), encoding="utf-8"))
AR = timezone(timedelta(hours=-3))
NOW = datetime.now(AR)

SKIP_DIRS = {"site", ".git", "node_modules"}
REG = {  # prefijo de código → página que lo define
    "PD": "00_MASTER/DECISIONS.md", "D": "00_MASTER/DECISIONS.md",
    "A": "00_MASTER/ASSUMPTIONS.md", "Q": "00_MASTER/OPEN_QUESTIONS.md",
    "R": "00_MASTER/RISKS.md", "T": "00_MASTER/TASKS.md",
    "I": "00_MASTER/RESEARCH_BACKLOG.md", "E": "00_MASTER/RESEARCH_BACKLOG.md",
    "F": "00_MASTER/SOURCES.md", "G": "00_MASTER/ROADMAP.md", "L": "00_MASTER/LEARNINGS.md",
}
CODE_RE = re.compile(r"\b(PD\d{3}|[DAQRTIEFL]\d{3}|G\d{1,2})\b")

NAV = [
    ("Tablero", ["00_MASTER/STATUS.md", "00_MASTER/PROJECT_MASTER.md", "00_MASTER/ROADMAP.md"]),
    ("Registros", ["00_MASTER/DECISIONS.md", "00_MASTER/ASSUMPTIONS.md", "00_MASTER/OPEN_QUESTIONS.md",
                   "00_MASTER/RISKS.md", "00_MASTER/TASKS.md", "00_MASTER/TAREAS/README.md", "00_MASTER/RESEARCH_BACKLOG.md",
                   "00_MASTER/SOURCES.md", "00_MASTER/LEARNINGS.md"]),
    ("Análisis especiales", ["03_CLIENTE/ARQUETIPOS_CLIENTES.md", "04_CONCEPTO/ANALISIS_CORNER_SHOP_IN_SHOP.md",
                             "04_CONCEPTO/ANALISIS_DELIVERY_PEDIDOSYA_DARK_KITCHEN.md", "09_OPERACIONES/I011_modelos_productivos.md",
                             "02_COMPETENCIA/I016c_resenas_cadenas_medialunas_cafe.md"]),
    ("Gestión", ["00_MASTER/METHODOLOGY.md", "00_MASTER/PARTNER_INPUTS.md", "@MEMOS", "@GATE_REVIEWS",
                 "@MINUTAS", "00_MASTER/CHANGELOG.md", "00_MASTER/SESSION_LOG.md", "00_MASTER/GLOSSARY.md",
                 "CLAUDE.md"]),
]
NAV_LABEL = {
    "00_MASTER/STATUS.md": "Estado (STATUS)", "00_MASTER/PROJECT_MASTER.md": "Mapa del proyecto",
    "00_MASTER/ROADMAP.md": "Roadmap por Gates", "00_MASTER/DECISIONS.md": "Decisiones (D / PD)",
    "00_MASTER/ASSUMPTIONS.md": "Hipótesis (A)", "00_MASTER/OPEN_QUESTIONS.md": "Preguntas (Q)",
    "00_MASTER/RISKS.md": "Riesgos (R)", "00_MASTER/TASKS.md": "Tareas (T)", "00_MASTER/TAREAS/README.md": "Fichas de tareas",
    "00_MASTER/RESEARCH_BACKLOG.md": "Investigaciones (I / E)", "00_MASTER/SOURCES.md": "Fuentes (F)",
    "00_MASTER/LEARNINGS.md": "Aprendizajes (L)", "00_MASTER/METHODOLOGY.md": "Metodología",
    "00_MASTER/PARTNER_INPUTS.md": "Información de socios", "00_MASTER/CHANGELOG.md": "Historial de cambios",
    "00_MASTER/SESSION_LOG.md": "Bitácora de sesiones", "00_MASTER/GLOSSARY.md": "Glosario",
    "CLAUDE.md": "Protocolo de la IA",
    "03_CLIENTE/ARQUETIPOS_CLIENTES.md": "10 arquetipos de cliente", "04_CONCEPTO/ANALISIS_CORNER_SHOP_IN_SHOP.md": "Corner / shop in shop",
    "04_CONCEPTO/ANALISIS_DELIVERY_PEDIDOSYA_DARK_KITCHEN.md": "PedidosYa y dark kitchen", "09_OPERACIONES/I011_modelos_productivos.md": "Modelos productivos (I011)",
    "02_COMPETENCIA/I016c_resenas_cadenas_medialunas_cafe.md": "Reseñas de panaderías",
}
STATE_CLASS = [
    (r"^(FINALIZADA|VALIDADA|CERRADA|RESPONDIDA|CERRADO)", "ok"),
    (r"^(BLOQUEADA|REFUTADA|\*?\*?Lista para decidir|MATERIALIZADO)", "crit"),
    (r"^(PENDIENTE|EN PROCESO|EN VALIDACIÓN|EN INVESTIGACIÓN|ABIERTA|ABIERTO|MITIGANDO|PARCIAL|Esperando|Parcial|Lista)", "pend"),
    (r"^(BACKLOG|NO VALIDADA|Futuro|REEMPLAZADA|DESCARTADA)", "mute"),
]


# ───────────────────────── utilidades ─────────────────────────
def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def url_of(rel_md):
    return "/" + rel_md[:-3] + ".html"


def strip_md(s):
    s = re.sub(r"\*\*|__|`", "", s)
    return s.strip()


def md_files():
    out = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith("."))
        for f in sorted(files):
            if f.endswith(".md"):
                out.append(rel(os.path.join(d, f)))
    return out


def asset_files():
    out = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith("."))
        for f in sorted(files):
            if f.lower().endswith((".pdf", ".html", ".xlsx", ".png", ".jpg", ".docx", ".pptx", ".csv", ".svg", ".json")) and not f.startswith("plantilla_"):
                out.append(rel(os.path.join(d, f)))
    return out


def title_of(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return strip_md(m.group(1)) if m else fallback


def parse_tables(text):
    """Devuelve lista de tablas markdown como listas de dicts (claves = encabezados)."""
    tables, lines, i = [], text.splitlines(), 0
    while i < len(lines) - 1:
        if lines[i].startswith("|") and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            hdr = [strip_md(c) for c in lines[i].strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                rows.append(dict(zip(hdr, cells + [""] * (len(hdr) - len(cells)))))
                j += 1
            tables.append(rows)
            i = j
        else:
            i += 1
    return tables


def read(rel_md):
    p = os.path.join(ROOT, rel_md)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def inline_md(s):
    return markdown.markdown(s).removeprefix("<p>").removesuffix("</p>")


# ───────────────────────── render markdown ─────────────────────────
BASENAME = {}


def embed_svgs(text):
    """<!--SVG:ruta--> → SVG en línea (ruta relativa a panaderia_cordoba/)."""
    def rep(m):
        p = os.path.join(ROOT, m.group(1).strip())
        if not os.path.exists(p):
            return f"*(gráfico no encontrado: {m.group(1)})*"
        svg = open(p, encoding="utf-8").read()
        return f'\n<figure class="fig">{svg}</figure>\n'
    return re.sub(r"<!--SVG:([^>]+?)-->", rep, text)


def render_md(text, rel_md):
    text = embed_svgs(text)
    body = markdown.markdown(text, extensions=["tables", "sane_lists", "fenced_code", "md_in_html"])
    # ids en encabezados que empiezan con un código (### D001 — …, ## G0 — …)
    def hid(m):
        tag, inner = m.group(1), m.group(2)
        c = CODE_RE.match(re.sub(r"<[^>]+>", "", inner).strip())
        return f'<{tag} id="{c.group(1)}">{inner}</{tag}>' if c else m.group(0)
    body = re.sub(r"<(h[1-4])>(.*?)</\1>", hid, body)
    # ids en filas cuya primera celda es un código
    def rid(m):
        c = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        return f'<tr id="{c}"><td>{m.group(2)}</td>' if re.fullmatch(CODE_RE.pattern, c) else m.group(0)
    body = re.sub(r"<tr>(\s*)<td>(.*?)</td>", lambda m: rid(m), body)
    # tablas con scroll
    body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    # badges de estado
    def badge(m):
        txt = m.group(1)
        plain = re.sub(r"<[^>]+>", "", txt).strip()
        for pat, cls in STATE_CLASS:
            if re.match(pat, plain):
                return f'<td><span class="st {cls}">{txt}</span></td>'
        return m.group(0)
    body = re.sub(r"<td>([^<]{0,90}(?:<strong>[^<]{0,60}</strong>[^<]{0,60})?)</td>", badge, body)
    # rutas en <code> → enlaces a páginas del sitio
    def codelink(m):
        path = m.group(1).strip()
        cand = None
        for c in (path, os.path.normpath(os.path.join(os.path.dirname(rel_md), path)).replace(os.sep, "/"),
                  "00_MASTER/" + path):
            if c.endswith(".md") and os.path.exists(os.path.join(ROOT, c)):
                cand = c
                break
        if not cand and path.endswith(".md") and os.path.basename(path) in BASENAME:
            cand = BASENAME[os.path.basename(path)]
        return f'<a href="{url_of(cand)}"><code>{path}</code></a>' if cand else m.group(0)
    body = re.sub(r"<code>([^<]+?\.md)</code>", codelink, body)
    def hreffix(m):
        href = m.group(1)
        if re.match(r"^(https?:|/|#|mailto:)", href):
            return m.group(0)
        path = os.path.normpath(os.path.join(os.path.dirname(rel_md), href)).replace(os.sep, "/")
        if path.endswith(".md") and os.path.exists(os.path.join(ROOT, path)):
            return f'href="{url_of(path)}"'
        if os.path.exists(os.path.join(ROOT, path)):
            return f'href="/archivos/{path}" target="_blank"'
        return m.group(0)
    body = re.sub(r'href="([^"]+)"', hreffix, body)
    return body


def autolink(body, ids, self_url):
    """Enlaza códigos (D001, PD029, Q046…) a su registro, fuera de <a>, <code> y <pre>."""
    out, depth = [], 0
    for tok in re.split(r"(<[^>]+>)", body):
        if tok.startswith("<"):
            t = tok.lower()
            if re.match(r"<(a|code|pre)[\s>]", t):
                depth += 1
            elif re.match(r"</(a|code|pre)>", t):
                depth = max(0, depth - 1)
            out.append(tok)
        elif depth == 0 and tok:
            def rep(m):
                code = m.group(1)
                pref = "PD" if code.startswith("PD") else code[0]
                if pref == "T" and os.path.exists(os.path.join(ROOT, "00_MASTER", "TAREAS", code + ".md")):
                    page = f"/00_MASTER/TAREAS/{code}.html"
                    return code if page == self_url else f'<a class="code" href="{page}" title="Ver ficha de la tarea">{code}</a>'
                page = url_of(REG[pref])
                if code not in ids.get(page, set()):
                    return code
                href = (f"#{code}" if page == self_url else f"{page}#{code}")
                return f'<a class="code" href="{href}">{code}</a>'
            out.append(CODE_RE.sub(rep, tok))
        else:
            out.append(tok)
    return "".join(out)


# ───────────────────────── layout ─────────────────────────
CSS = r"""
:root{--brand:#F18A00;--brand2:#B12028;--tx:#404040;--tx2:#7a7a7a;--bg:#fff;--soft:#FFF4E5;--line:#E8E8E8;--side:#FAFAFA;
--ok:#2E7D32;--okbg:#E8F5E9;--pend:#A85800;--pendbg:#FFF1DC;--crit:#B12028;--critbg:#FBEDEE;--mute:#666;--mutebg:#F0F0F0}
*{box-sizing:border-box}html{scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--tx);font-family:'Montserrat','Segoe UI',Helvetica,Arial,sans-serif;font-size:14px;line-height:1.55}
a{color:var(--brand2)}a:hover{color:var(--brand)}
.top{position:sticky;top:0;z-index:20;background:#fff;border-bottom:3px solid var(--brand);display:flex;align-items:center;gap:14px;padding:10px 16px}
.logo{font-weight:800;color:var(--brand);font-size:17px;text-decoration:none;white-space:nowrap}.logo small{display:block;font-size:9px;color:var(--tx2);font-weight:500;letter-spacing:1.3px}
.menu{display:none;background:none;border:1px solid var(--line);border-radius:6px;padding:6px 10px;font-size:16px;cursor:pointer}
.search{flex:1;max-width:460px;margin-left:auto;position:relative}
.search input{width:100%;padding:8px 12px;border:1px solid var(--line);border-radius:8px;font:inherit;font-size:13px}
.results{position:absolute;top:40px;left:0;right:0;background:#fff;border:1px solid var(--line);border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.1);max-height:60vh;overflow:auto;display:none}
.results a{display:block;padding:8px 12px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--tx)}.results a:hover{background:var(--soft)}.results small{color:var(--tx2);display:block}
.who{font-size:12px;color:var(--tx2);white-space:nowrap}
.layout{display:grid;grid-template-columns:270px minmax(0,1fr);min-height:calc(100vh - 60px)}
nav.side{background:var(--side);border-right:1px solid var(--line);padding:14px 10px 40px;overflow:auto;position:sticky;top:60px;height:calc(100vh - 60px)}
nav.side h4{font-size:10.5px;letter-spacing:1.2px;text-transform:uppercase;color:var(--tx2);margin:16px 8px 4px}
nav.side a{display:block;padding:5px 8px;border-radius:6px;text-decoration:none;color:var(--tx);font-size:13px}
nav.side a:hover{background:var(--soft)}nav.side a.on{background:var(--brand);color:#fff;font-weight:700}
nav.side a.sub{padding-left:20px;font-size:12px;color:var(--tx2)}
main{padding:22px 32px 60px;max-width:1150px;min-width:0}
h1{color:var(--brand);font-weight:800;font-size:26px;margin:4px 0 12px}
h2{color:var(--brand);font-size:19px;border-left:4px solid var(--brand);padding-left:8px;margin:30px 0 10px}
h3{color:var(--brand2);font-size:15px;margin:22px 0 6px}
.tw{overflow-x:auto;margin:10px 0 16px;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th{background:var(--brand);color:#fff;text-align:left;padding:7px 9px;font-weight:700;position:sticky;top:0}
td{border-bottom:1px solid var(--line);padding:6px 9px;vertical-align:top}
tr:nth-child(even) td{background:#FFFBF5}tr:target td{background:#FFE7C2 !important}
h3:target,h2:target{background:#FFE7C2}
code{background:#f3f3f3;padding:1px 4px;border-radius:4px;font-size:12px}
pre{background:#f6f6f6;padding:12px;border-radius:8px;overflow:auto}
blockquote{margin:10px 0;padding:8px 14px;border-left:4px solid var(--brand);background:var(--soft);border-radius:0 8px 8px 0}
a.code{font-weight:700;text-decoration:none;border-bottom:1px dotted var(--brand2);white-space:nowrap}
.st{display:inline-block;font-size:11px;font-weight:700;border-radius:4px;padding:1px 7px}
.st.ok{background:var(--okbg);color:var(--ok)}.st.pend{background:var(--pendbg);color:var(--pend)}.st.crit{background:var(--critbg);color:var(--crit)}.st.mute{background:var(--mutebg);color:var(--mute)}
.pagebar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:6px;font-size:12px;color:var(--tx2)}
.btn{display:inline-block;padding:6px 12px;border-radius:6px;border:1px solid var(--brand);color:var(--brand2);text-decoration:none;font-weight:700;font-size:12px;background:#fff}
.btn.fill{background:var(--brand);color:#fff}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 -4px}.filters input,.filters select{padding:6px 10px;border:1px solid var(--line);border-radius:6px;font:inherit;font-size:12.5px}
.filters .count{font-size:12px;color:var(--tx2);align-self:center}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin:14px 0}
.kpi{border:1px solid var(--line);border-top:3px solid var(--brand);border-radius:8px;padding:10px 12px;text-decoration:none;color:var(--tx);display:block}
.kpi b{display:block;font-size:26px;font-weight:800}.kpi span{font-size:11.5px;color:var(--tx2)}a.kpi:hover{background:var(--soft)}
.kpi.alert{border-top-color:var(--brand2)}.kpi.alert b{color:var(--brand2)}
.hitos{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:8px}
.hito{border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:12.5px}.hito b{color:var(--brand)}
.hito.corte{border-color:var(--brand2);background:var(--critbg)}.hito.corte b{color:var(--brand2)}.hito.past{opacity:.5}
.hito.next{outline:3px solid var(--brand)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}
.card{border:1px solid var(--line);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--tx);display:block}.card:hover{border-color:var(--brand);background:var(--soft)}
.card b{color:var(--brand);font-size:15px}.card small{display:block;color:var(--tx2)}.card .n{font-size:22px;font-weight:800;color:var(--brand2)}
.hello{display:none;background:var(--brand);color:#fff;border-radius:10px;padding:12px 16px;margin:0 0 14px}.hello a{color:#fff;font-weight:800}
.note{font-size:12px;color:var(--tx2)}
.fig{margin:14px 0;overflow-x:auto}.fig svg{max-width:100%;height:auto;display:block}
.box{border:1px solid var(--brand);background:var(--soft);border-radius:10px;padding:10px 16px;margin:12px 0}
footer{margin-top:40px;padding-top:10px;border-top:1px solid var(--line);font-size:11px;color:var(--tx2)}
@media(max-width:860px){.top{flex-wrap:wrap}.search{order:3;flex-basis:100%}.logo small{display:none}.layout{grid-template-columns:minmax(0,1fr)}nav.side{display:none;position:fixed;top:58px;left:0;right:0;bottom:0;height:auto;z-index:30}
nav.side.open{display:block}.menu{display:block}main{padding:16px}.who{display:none}.search{max-width:none}}
@media print{.top,nav.side,.filters,.pagebar{display:none}.layout{display:block}main{max-width:none}}
"""

JS = r"""
const SOCIOS = __SOCIOS__;
document.querySelector('.menu')?.addEventListener('click',()=>document.querySelector('nav.side').classList.toggle('open'));
// búsqueda global
let IDX=null;const q=document.getElementById('q'),res=document.getElementById('res');
q?.addEventListener('input',async()=>{if(!IDX){IDX=await (await fetch('/search.json')).json()}
 const v=q.value.trim().toLowerCase();if(v.length<2){res.style.display='none';return}
 const terms=v.split(/\s+/);const hits=IDX.filter(p=>terms.every(t=>p.x.includes(t)||p.t.toLowerCase().includes(t))).slice(0,15);
 res.innerHTML=hits.map(p=>{const i=p.x.indexOf(terms[0]);const s=i>=0?p.x.substring(Math.max(0,i-50),i+90):'';return `<a href="${p.u}">${p.t}<small>…${s.replace(/</g,'&lt;')}…</small></a>`}).join('')||'<a>Sin resultados</a>';
 res.style.display='block'});
document.addEventListener('click',e=>{if(res&&!e.target.closest('.search'))res.style.display='none'});
// filtros en tablas largas
document.querySelectorAll('main .tw table').forEach(tb=>{const rows=[...tb.querySelectorAll('tbody tr')];if(rows.length<6)return;
 const hs=[...tb.querySelectorAll('th')].map(h=>h.textContent.trim());const ei=hs.findIndex(h=>/^Estado/i.test(h));
 const bar=document.createElement('div');bar.className='filters';
 bar.innerHTML=`<input type="search" placeholder="Filtrar ${rows.length} filas…">`+(ei>=0?`<select><option value="">Todos los estados</option>${[...new Set(rows.map(r=>r.cells[ei]?.textContent.trim().split(/[ (→;—]/)[0]).filter(Boolean))].sort().map(s=>`<option>${s}</option>`).join('')}</select>`:'')+`<span class="count"></span>`;
 tb.parentElement.before(bar);const inp=bar.querySelector('input'),sel=bar.querySelector('select'),cnt=bar.querySelector('.count');
 const f=()=>{const v=inp.value.toLowerCase(),s=sel?.value||'';let n=0;rows.forEach(r=>{const ok=r.textContent.toLowerCase().includes(v)&&(!s||(r.cells[ei]?.textContent.trim().startsWith(s)));r.style.display=ok?'':'none';n+=ok});cnt.textContent=(v||s)?`${n} de ${rows.length}`:''};
 inp.addEventListener('input',f);sel?.addEventListener('change',f)});
// identidad → saludo y acceso al panel personal (cookie del acceso de Vercel o Cloudflare Access)
function hola(s){const w=document.getElementById('who');if(w)w.innerHTML=`${s.nombre} · <a href="/salir">salir</a>`;const h=document.getElementById('hello');
 if(h){h.innerHTML=`Hola, ${s.nombre.split(' ')[0]} · <a href="/socios/${s.id}.html">Ver mis pendientes →</a>`;h.style.display='block'}}
const ck=(document.cookie.match(/(?:^|; )socio=([^;]+)/)||[])[1];const sc=ck&&SOCIOS.find(x=>x.id===ck);
if(sc){hola(sc)}else(async()=>{try{const r=await fetch('/cdn-cgi/access/get-identity',{credentials:'include'});if(!r.ok)return;const j=await r.json();
 const s=SOCIOS.find(x=>x.email&&j.email&&x.email.toLowerCase()===j.email.toLowerCase());const w=document.getElementById('who');
 if(w)w.textContent=s?s.nombre:(j.email||'');const h=document.getElementById('hello');
 if(s&&h){h.innerHTML=`Hola, ${s.nombre.split(' ')[0]} · <a href="/socios/${s.id}.html">Ver mis pendientes →</a>`;h.style.display='block'}}catch(e){}})();
"""


def nav_html(cur, pages):
    def link(u, label, cls=""):
        on = " on" if u == cur else ""
        return f'<a class="{cls}{on}" href="{u}">{html.escape(label)}</a>'
    h = [link("/index.html", "Inicio"), "<h4>Mi panel</h4>"]
    for s in CFG["socios"]:
        h.append(link(f"/socios/{s['id']}.html", s["nombre"]))
    for sec, items in NAV:
        h.append(f"<h4>{sec}</h4>")
        for it in items:
            if it.startswith("@"):
                folder = "00_MASTER/" + it[1:] + "/"
                subs = [p for p in pages if p.startswith(folder)]
                if subs:
                    h.append(f'<a href="{url_of(subs[0])}">{it[1:].title().replace("_", " ")}</a>')
                    h += [link(url_of(p), pages[p]["title"][:42], "sub") for p in subs]
            elif it in pages:
                h.append(link(url_of(it), NAV_LABEL.get(it, pages[it]["title"])))
    h.append("<h4>Áreas</h4>")
    for d in sorted({p.split("/")[0] for p in pages if re.match(r"^\d\d_", p) and not p.startswith("00_")}):
        readme = f"{d}/README.md"
        if readme in pages:
            t = pages[readme]["title"]
            h.append(link(url_of(readme), d[:2] + " · " + (t.split("—", 1)[1].strip() if "—" in t else d[3:])))
            if cur.startswith("/" + d + "/"):
                h += [link(url_of(p), pages[p]["title"][:42], "sub") for p in pages if p.startswith(d + "/") and p != readme]
    h.append("<h4>Otros</h4>")
    h.append(link("/archivos/02_COMPETENCIA/MAPA_COMPETITIVO_CORDOBA.html", "🗺 Mapa competitivo"))
    h.append(link("/entregables.html", "Entregables (PDF / HTML)"))
    h.append(link(url_of("00_MASTER/PLANTILLAS/README.md"), "Plantillas"))
    return "\n".join(h)


def page(title, body, cur, pages, extra_bar=""):
    socios_js = json.dumps([{k: s[k] for k in ("id", "nombre", "email")} for s in CFG["socios"]], ensure_ascii=False)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{html.escape(title)} · {CFG['codigo']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css"></head><body>
<div class="top"><button class="menu" aria-label="Menú">☰</button>
<a class="logo" href="/index.html">CANALSENSES<small>{html.escape(CFG['proyecto'].upper())} · {CFG['codigo']}</small></a>
<div class="search"><input id="q" type="search" placeholder="Buscar en todo el proyecto (ej. Del Pilar, PD029, alquiler)…" autocomplete="off"><div class="results" id="res"></div></div>
<span class="who" id="who"></span></div>
<div class="layout"><nav class="side">{nav_html(cur, pages)}</nav>
<main><div class="hello" id="hello"></div>{extra_bar}{body}
<footer>{html.escape(CFG['empresa'])} · {CFG['codigo']} · Sitio generado automáticamente desde el repositorio el {NOW:%d/%m/%Y %H:%M} (hora Argentina). Confidencial.</footer>
</main></div><script>{JS.replace('__SOCIOS__', socios_js)}</script></body></html>"""


# ───────────────────────── dashboard y paneles ─────────────────────────
def registers():
    dec = read("00_MASTER/DECISIONS.md")
    tasks = [r for t in parse_tables(read("00_MASTER/TASKS.md")) for r in t if re.match(r"^T\d{3}$", r.get("Código", ""))]
    seen, tasks_u = set(), []
    for r in tasks:
        if r["Código"] not in seen:
            seen.add(r["Código"]); tasks_u.append(r)
    pds = [r for t in parse_tables(dec) for r in t if re.match(r"^PD\d{3}$", r.get("Código", ""))]
    qs = [r for t in parse_tables(read("00_MASTER/OPEN_QUESTIONS.md")) for r in t if re.match(r"^Q\d{3}$", r.get("Código", ""))]
    risks = [r for t in parse_tables(read("00_MASTER/RISKS.md")) for r in t if re.match(r"^R\d{3}$", r.get("Código", "")) and r.get("Sev.")]
    inv = [r for t in parse_tables(read("00_MASTER/RESEARCH_BACKLOG.md")) for r in t if re.match(r"^I\d{3}$", r.get("Código", ""))]
    hyp = [r for t in parse_tables(read("00_MASTER/ASSUMPTIONS.md")) for r in t if re.match(r"^A\d{3}$", r.get("Código", ""))]
    dcount = len(re.findall(r"^### D\d{3}", dec, re.M))
    return dict(tasks=tasks_u, pds=pds, qs=qs, risks=risks, inv=inv, hyp=hyp, dcount=dcount)


def is_open_task(r):
    return strip_md(r.get("Estado", "")).startswith(("PENDIENTE", "EN PROCESO", "BLOQUEADA"))


def is_open_pd(r):
    return not strip_md(r.get("Estado", "")).startswith(("CERRADA", "Futuro"))


def is_open_q(r):
    return not strip_md(r.get("Estado", "")).startswith(("RESPONDIDA", "DESCARTADA"))


def state_badge(txt):
    plain = re.sub(r"<[^>]+>", "", txt).strip()
    for pat, cls in STATE_CLASS:
        if re.match(pat, plain):
            return f'<span class="st {cls}">{txt}</span>'
    return txt


def mini_table(rows, cols, empty="Nada pendiente 🎉"):
    if not rows:
        return f'<p class="note">{empty}</p>'
    h = "<div class='tw'><table><thead><tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr></thead><tbody>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{state_badge(inline_md(r.get(c, ''))) if c == 'Estado' else inline_md(r.get(c, ''))}</td>" for c in cols) + "</tr>"
    return h + "</tbody></table></div>"


def hitos_html():
    today = NOW.date()
    nxt = next((h for h in CFG["hitos"] if date.fromisoformat(h["fecha"]) >= today), None)
    out = []
    for h in CFG["hitos"]:
        d = date.fromisoformat(h["fecha"])
        cls = "hito" + (" corte" if h["corte"] else "") + (" past" if d < today else "") + (" next" if h is nxt else "")
        dias = (d - today).days
        rest = f"faltan {dias} días" if dias > 0 else ("hoy" if dias == 0 else "cumplido")
        out.append(f'<div class="{cls}"><b>{d:%d/%m/%Y}</b><br>{html.escape(h["nombre"])}<br><span class="note">{rest}</span></div>')
    return '<div class="hitos">' + "".join(out) + "</div>"


def dashboard(R, status_body):
    ap = date.fromisoformat(CFG["hitos"][-1]["fecha"])
    dias = (ap - NOW.date()).days
    open_t = [r for r in R["tasks"] if is_open_task(r)]
    open_pd = [r for r in R["pds"] if is_open_pd(r)]
    urgent_pd = [r for r in open_pd if "Lista para decidir" in r.get("Estado", "") or "PARCIAL" in r.get("Estado", "")]
    open_q = [r for r in R["qs"] if is_open_q(r)]
    hi_r = sorted([r for r in R["risks"] if r["Sev."].strip().isdigit() and int(r["Sev."]) >= 6], key=lambda r: -int(r["Sev."]))
    inv_done = [r for r in R["inv"] if "FINALIZADA" in r.get("Estado", "")]
    k = f"""<div class="kpis">
<a class="kpi alert" href="#hitos"><b>{dias}</b><span>días a la apertura ({ap:%d/%m/%Y})</span></a>
<a class="kpi" href="{url_of('00_MASTER/DECISIONS.md')}"><b>{R['dcount']}</b><span>decisiones aprobadas</span></a>
<a class="kpi alert" href="{url_of('00_MASTER/DECISIONS.md')}#pendientes"><b>{len(urgent_pd)}</b><span>decisiones esperando a los socios</span></a>
<a class="kpi" href="{url_of('00_MASTER/TASKS.md')}"><b>{len(open_t)}</b><span>tareas activas</span></a>
<a class="kpi" href="{url_of('00_MASTER/OPEN_QUESTIONS.md')}"><b>{len(open_q)}</b><span>preguntas abiertas</span></a>
<a class="kpi" href="{url_of('00_MASTER/RISKS.md')}"><b>{len(hi_r)}</b><span>riesgos de severidad ≥ 6</span></a>
<a class="kpi" href="{url_of('00_MASTER/RESEARCH_BACKLOG.md')}"><b>{len(inv_done)}/{len(R['inv'])}</b><span>investigaciones finalizadas</span></a>
<a class="kpi" href="{url_of('00_MASTER/ASSUMPTIONS.md')}"><b>{len(R['hyp'])}</b><span>hipótesis (validadas: {sum('VALIDADA' == strip_md(r.get('Estado','')) for r in R['hyp'])})</span></a>
</div>"""
    cards = []
    for s in CFG["socios"]:
        n = len(person_items(s, R)["mine"])
        cards.append(f'<a class="card" href="/socios/{s["id"]}.html"><b>{html.escape(s["nombre"])}</b><small>{html.escape(s["rol"])}</small><span class="n">{n}</span> <small style="display:inline">tareas asignadas</small></a>')
    body = f"""<h1>{html.escape(CFG['proyecto'])}</h1>
<p class="note">Tablero general del proyecto. Todo se actualiza automáticamente con cada cambio en el repositorio.</p>{k}
<h2>Decisiones esperando a los socios</h2>{mini_table(urgent_pd, ['Código', 'Decisión requerida', 'Estado', 'Insumos necesarios'])}
<h2 id="hitos">Hitos y fechas de corte</h2>{hitos_html()}
<h2>Paneles de los socios</h2><div class="cards">{''.join(cards)}</div>
<h2>Riesgos principales</h2>{mini_table(hi_r, ['Código', 'Riesgo', 'Sev.', 'Responsable', 'Estado'])}
<h2>Estado del proyecto (STATUS)</h2><div class="box">{status_body}</div>"""
    return body


def person_items(s, R):
    name_keys = [k for k in s["claves"] if k not in ("Socios", "hermanos")]
    shared_keys = [k for k in s["claves"] if k in ("Socios", "hermanos")]
    def has(txt, keys):
        return any(re.search(rf"\b{re.escape(k)}\b", txt, re.I) for k in keys)
    mine = [r for r in R["tasks"] if is_open_task(r) and has(r.get("Responsable", ""), name_keys)]
    shared = [r for r in R["tasks"] if is_open_task(r) and r not in mine and has(r.get("Responsable", ""), shared_keys)]
    qs = [r for r in R["qs"] if is_open_q(r) and has(" ".join(r.values()), name_keys)]
    risks = [r for r in R["risks"] if has(r.get("Responsable", ""), name_keys)]
    return dict(mine=mine, shared=shared, qs=qs, risks=risks)


def person_page(s, R):
    it = person_items(s, R)
    open_pd = [r for r in R["pds"] if is_open_pd(r) and ("Lista para decidir" in r.get("Estado", "") or "PARCIAL" in r.get("Estado", ""))]
    return f"""<h1>Panel de {html.escape(s['nombre'])}</h1>
<p class="note">{html.escape(s['rol'])} · Se arma solo a partir de los registros del proyecto (tareas, preguntas, riesgos y decisiones donde figura su nombre).</p>
<div class="kpis"><div class="kpi alert"><b>{len(it['mine'])}</b><span>tareas asignadas</span></div>
<div class="kpi"><b>{len(it['shared'])}</b><span>tareas compartidas (socios / hermanos)</span></div>
<div class="kpi alert"><b>{len(open_pd)}</b><span>decisiones esperando a los socios</span></div>
<div class="kpi"><b>{len(it['qs'])}</b><span>preguntas donde se lo menciona</span></div></div>
<h2>Mis tareas</h2>{mini_table(it['mine'], ['Código', 'Tarea', 'Gate', 'Prioridad', 'Estado', 'Resultado esperado'])}
<h2>Decisiones que tenemos que tomar como socios</h2>{mini_table(open_pd, ['Código', 'Decisión requerida', 'Estado', 'Insumos necesarios'])}
<h2>Tareas compartidas</h2>{mini_table(it['shared'], ['Código', 'Tarea', 'Responsable', 'Prioridad', 'Estado'])}
<h2>Preguntas abiertas que me involucran</h2>{mini_table(it['qs'], ['Código', 'Pregunta', 'Prioridad', 'Estado'])}
<h2>Riesgos a mi cargo</h2>{mini_table(it['risks'], ['Código', 'Riesgo', 'Sev.', 'Estado'], 'Ningún riesgo asignado.')}
<h2>Próximos hitos</h2>{hitos_html()}"""


# ───────────────────────── build ─────────────────────────
def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    files = md_files()
    for f in files:
        BASENAME.setdefault(os.path.basename(f), f)
    assets = asset_files()
    pages = {}
    for f in files:
        txt = read(f)
        pages[f] = {"title": title_of(txt, os.path.basename(f)[:-3]), "text": txt, "body": render_md(txt, f)}
    # ids por página (para enlazar sólo códigos existentes)
    ids = {url_of(f): set(re.findall(r'id="([^"]+)"', p["body"])) for f, p in pages.items()}
    index = []
    R = registers()

    def write(url, content):
        path = os.path.join(DIST, url.lstrip("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(content)

    for f, p in pages.items():
        u = url_of(f)
        body = p["body"]
        if f == "00_MASTER/DECISIONS.md":
            body = body.replace("<h2>Decisiones pendientes (PD)</h2>", '<h2 id="pendientes">Decisiones pendientes (PD)</h2>')
        folder = os.path.dirname(f)
        if f.endswith("README.md") and folder:
            docs = [x for x in pages if os.path.dirname(x) == folder and x != f]
            fl = [a for a in assets if os.path.dirname(a) == folder]
            if docs or fl:
                body += "<h2>Documentos en esta carpeta</h2><ul>" + "".join(
                    f'<li><a href="{url_of(x)}">{html.escape(pages[x]["title"])}</a></li>' for x in docs) + "".join(
                    f'<li><a href="/archivos/{a}">{html.escape(os.path.basename(a))}</a></li>' for a in fl) + "</ul>"
        stem = os.path.join(folder, os.path.basename(f)[:-3]) if folder else os.path.basename(f)[:-3]
        dl = "".join(f'<a class="btn fill" href="/archivos/{stem}.{ext}">Descargar {ext.upper()}</a>'
                     for ext in ("pdf", "html") if f"{stem}.{ext}" in assets)
        bar = (f'<div class="pagebar">{dl}<a class="btn" href="{CFG["repo_url"]}/blob/{CFG["repo_branch"]}/{CFG["repo_path"]}/{f}" '
               f'target="_blank" rel="noopener">Ver / editar en GitHub</a><span>{html.escape(f)}</span></div>')
        write(u, page(p["title"], autolink(body, ids, u), u, pages, bar))
        index.append({"t": p["title"], "u": u, "x": re.sub(r"\s+", " ", strip_md(p["text"])).lower()[:20000]})

    status_body = autolink(pages["00_MASTER/STATUS.md"]["body"].split("</table></div>", 1)[-1], ids, "/index.html")
    write("/index.html", page("Inicio", autolink(dashboard(R, status_body), ids, "/index.html"), "/index.html", pages))
    for s in CFG["socios"]:
        u = f"/socios/{s['id']}.html"
        write(u, page(f"Panel de {s['nombre']}", autolink(person_page(s, R), ids, u), u, pages))

    # entregables y archivos
    for a in assets:
        dst = os.path.join(DIST, "archivos", a)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(ROOT, a), dst)
    rows = "".join(f'<tr><td>{html.escape(os.path.dirname(a))}</td><td><a href="/archivos/{a}" target="_blank">{html.escape(os.path.basename(a))}</a></td></tr>'
                   for a in assets)
    write("/entregables.html", page("Entregables", f"<h1>Entregables y archivos</h1><p class='note'>PDF y HTML emitidos para los socios. Se abren en una pestaña nueva.</p><div class='tw'><table><thead><tr><th>Carpeta</th><th>Archivo</th></tr></thead><tbody>{rows}</tbody></table></div>", "/entregables.html", pages))

    open(os.path.join(DIST, "style.css"), "w").write(CSS)
    json.dump(index, open(os.path.join(DIST, "search.json"), "w", encoding="utf-8"), ensure_ascii=False)
    open(os.path.join(DIST, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(DIST, "_headers"), "w").write("/*\n  X-Robots-Tag: noindex, nofollow\n  X-Frame-Options: DENY\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    print(f"OK: {len(pages)} páginas, {len(assets)} archivos, {len(CFG['socios'])} paneles → {DIST}")


if __name__ == "__main__":
    main()
