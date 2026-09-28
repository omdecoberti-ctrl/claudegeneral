# Sitio web del proyecto: publicación y acceso por socio

El sitio se genera solo a partir de los `.md` del repositorio (`build.py`).
Cada vez que se sube un cambio a GitHub, el hosting lo vuelve a generar y publicar.
No hace falta tocar nada a mano.

## Qué incluye
- **Inicio / tablero:** días a la apertura, decisiones esperando a los socios, tareas, preguntas, riesgos, hitos y STATUS.
- **Mi panel (uno por socio):** tareas asignadas, tareas compartidas, decisiones pendientes, preguntas y riesgos donde figura su nombre.
- **Registros navegables:** decisiones, hipótesis, preguntas, riesgos, tareas, investigaciones y fuentes.
  - Cada tabla larga tiene filtro de texto y filtro por estado.
  - Todos los códigos (D001, PD029, Q046, R019…) son enlaces a su registro.
- **Buscador global**, secciones por área, entregables PDF/HTML descargables y botón "Ver / editar en GitHub".

---

## Opción recomendada: Cloudflare Pages + Cloudflare Access (usuario por socio, gratis hasta 50 usuarios)

### Paso 1 — Publicar el sitio (Cloudflare Pages)
1. Crear una cuenta en https://dash.cloudflare.com (con el mail de Oscar o el de la empresa).
2. Ir a **Workers & Pages → Create → Pages → Connect to Git** y autorizar GitHub.
3. Elegir el repositorio `omdecoberti-ctrl/claudegeneral`.
4. Configurar:
   | Campo | Valor |
   |---|---|
   | Production branch | `claude/stoic-hawking-6pkd67` (o `main` si más adelante se unifica) |
   | Framework preset | None |
   | Root directory | `panaderia_cordoba/site` |
   | Build command | `pip install -r requirements.txt && python build.py` |
   | Build output directory | `dist` |
   | Variable de entorno (opcional) | `PYTHON_VERSION` = `3.11` |
5. Hacer clic en **Save and Deploy**. Queda publicado en `https://<nombre-proyecto>.pages.dev`.

### Paso 2 — Restringir el acceso a los 4 socios (Cloudflare Access / Zero Trust)
1. En el panel de Cloudflare ir a **Zero Trust**.
   - Elegir el plan **Free**, que cubre hasta 50 usuarios.
   - Cloudflare puede pedir una tarjeta aunque el plan sea gratuito.
2. Ir a **Access → Applications → Add an application → Self-hosted**.
   - Application domain: `<nombre-proyecto>.pages.dev`.
   - Agregar también `*.<nombre-proyecto>.pages.dev`, para proteger las versiones de prueba.
   - Session duration: por ejemplo 1 mes, para no tener que ingresar el código seguido.
3. Crear una política: **Action = Allow**, **Include → Emails** con los mails de Oscar, Fabiola, Laura y María Isabel.
4. Método de ingreso: **One-time PIN**. Cada socio pone su mail y recibe un código.
   - Si usan Google, también se puede sumar "Login with Google".
5. Probar entrando en una ventana de incógnito: tiene que pedir el mail.

> Los nombres exactos de los menús de Cloudflare pueden cambiar. Si algo no coincide, buscar "Access application" en la ayuda de Cloudflare.

### Paso 3 — Asociar cada mail con su panel
Completar el campo `email` de cada socio en `site/config.json` (o pasarle los mails a la IA).
Con eso, al entrar, el sitio saluda a cada uno y le muestra el acceso directo a **su** panel.

---

## Alternativa: Vercel
1. En https://vercel.com, hacer **Add New → Project** e importar el repositorio.
2. Configurar:
   - Root Directory: `panaderia_cordoba/site`
   - Build Command: `pip install -r requirements.txt && python3 build.py`
   - Output Directory: `dist`
3. Para restringir el acceso hace falta el **plan Pro**:
   - Para password protection o para usuarios del equipo.
   - Además, el plan gratuito de Vercel es para uso no comercial.
   - El saludo personalizado por socio **no funciona en Vercel**, porque depende de Cloudflare Access. Los paneles por socio igual quedan accesibles desde el menú.

---

## Mantenimiento
- **Hitos y fechas de corte:** se editan en `site/config.json` → `hitos`.
- **Socios, mails y palabras clave** para armar los paneles: `site/config.json` → `socios`.
- **Probar en local:** `cd panaderia_cordoba/site && pip install -r requirements.txt && python build.py`, y después abrir `dist/` con un servidor (`python -m http.server -d dist`).
- **Paneles:** se arman leyendo la columna "Responsable" de las tablas. Para que una tarea aparezca en el panel de alguien, su nombre tiene que figurar en esa columna.
