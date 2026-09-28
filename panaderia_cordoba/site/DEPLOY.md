# Sitio web del proyecto: publicación en Vercel y acceso por socio

**En línea desde el 28/09/2026: https://panaderia-cordoba.vercel.app**

El sitio se genera solo a partir de los `.md` del repositorio (`build.py`).
Cada vez que se sube un cambio a GitHub, Vercel lo vuelve a generar y publicar. No hay que hacer nada a mano.

**Acceso:** cada socio entra con **su usuario y contraseña**. El control lo hace `middleware.js`, que corre en Vercel antes de mostrar cualquier página, PDF o archivo. Sin credenciales válidas no se ve nada. Al entrar, el sitio reconoce al socio, lo saluda y le ofrece su panel personal. El enlace "salir", arriba a la derecha, cierra la sesión.

## Configurar el proyecto de Vercel (una sola vez, ~5 minutos)
En el proyecto ya creado en Vercel:

1. **Settings → Git → Connected Git Repository:** conectar `omdecoberti-ctrl/claudegeneral`, si todavía no está conectado.
2. **Settings → Build and Deployment:**
   | Campo | Valor |
   |---|---|
   | Framework Preset | **Other** |
   | Root Directory | **vacío** (raíz del repo). La raíz tiene `vercel.json` + `middleware.js`, que apuntan a esta carpeta. También funciona con `panaderia_cordoba/site`. |
   | Build / Output / Install Command | dejar en automático: los toma de `vercel.json` |
3. **Settings → Environments → Production → Branch Tracking:** `main`, que es la rama de producción del proyecto.
4. **Deployments → Redeploy** (o subir cualquier cambio). A los 1–2 minutos el sitio queda en `https://<proyecto>.vercel.app`.
5. **Probar:** tiene que pedir usuario y contraseña. Probar también con una contraseña incorrecta, que tiene que rechazar.

> **Importante:** en **Settings → Deployment Protection**, si está activada "Vercel Authentication", también pedirá login de Vercel. Para los socios conviene **desactivarla** y dejar solo el acceso propio del sitio.

## Usuarios y contraseñas
- Los usuarios están definidos en `config.json` (campo `usuario`): `oscar`, `fabiola`, `laura`, `mariaisabel`.
- Las contraseñas **no están en el repositorio**. Solo está su hash salado, en `auth_users.js`.
- **Cambiar una contraseña:** `python crear_usuarios.py laura`. Muestra la nueva contraseña y actualiza el hash; después, commit + push. La IA puede hacerlo a pedido.
- **Agregar un socio o usuario:** sumarlo en `config.json` → `socios` y correr `python crear_usuarios.py <usuario>`.
- **Opcional:** en lugar del archivo, se puede cargar la variable de entorno `SITE_USERS` en Vercel, con el mismo formato JSON que `auth_users.js`.

## Qué incluye el sitio
- **Inicio / tablero:** días a la apertura, decisiones esperando a los socios, tareas, preguntas, riesgos, hitos y STATUS.
- **Panel por socio:** tareas asignadas y compartidas, decisiones pendientes, preguntas y riesgos donde figura su nombre.
- **Registros navegables** con filtro por texto y por estado. Todos los códigos (D001, PD029, Q046…) son enlaces.
- **Buscador global**, áreas del proyecto, entregables PDF/HTML y el botón "Ver / editar en GitHub".

## Plan de Vercel
- El acceso por usuario funciona en cualquier plan: no usa la "Deployment Protection" paga de Vercel.
- Los términos del plan **Hobby (gratis)** lo limitan a uso **no comercial**. Para un proyecto de empresa corresponde el plan **Pro**, que se paga por miembro del equipo de Vercel.
- Los socios no necesitan cuenta de Vercel: solo entran con su usuario del sitio.

## Mantenimiento
- **Hitos y fechas de corte:** `config.json` → `hitos`.
- **Paneles:** se arman con la columna "Responsable" de las tablas. Para que una tarea aparezca en el panel de alguien, su nombre tiene que figurar ahí.
- **Probar en local:** `cd panaderia_cordoba/site && python3 build.py && python3 -m http.server -d dist`. En local no pide contraseña: el acceso solo corre en Vercel.
