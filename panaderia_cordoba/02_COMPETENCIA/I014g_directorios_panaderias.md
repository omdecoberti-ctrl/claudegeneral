# R5 — Cosecha desde directorios (notas)

Fecha de consulta: 2026-09-28/29. Solo WebSearch (30 búsquedas usadas, cupo completo).

## Resultado
- 97 registros en `r5_directorios.json`: 60 con dirección completa, 6 con calle sin número, 31 solo nombre.
- 50 registros con zona asignada (varias zonas son **inferidas** por la avenida/numeración; en `nota` dice "inferida").
- Campos extra respecto del BRIEF: `rating_restaurantguru`, `reviews_restaurantguru`, `fuente_id`. `google_rating` solo se cargó cuando el fragmento decía "Google".
- **Meta de 120 no alcanzada**: los fragmentos de WebSearch muestran 4–10 entradas por búsqueda, no las páginas completas de listados.

## Fuentes
| ID | Fuente | Rinde |
|---|---|---|
| F1500 | lahelveticaonline.com.ar (fichas /panaderia/… "Panadería en Capital, Córdoba") | **Alto**: dirección + barrio + horario en el resumen. El mejor directorio. |
| F1501 | argentino.com.ar (fichas "teléfono - Dirección, Córdoba Capital" y listados /cordoba-capital/panaderias, /panaderias+y+panificadoras) | **Medio-alto**: dirección en el título de cada ficha; los listados solo devuelven nombres. |
| F1502 | restaurantguru.com (fichas por local) | **Medio**: dirección + puntaje RG + cantidad de reseñas; mezcla resultados de Córdoba (España). |
| F1503 | waze.com/live-map (direcciones de sucursales) | **Medio**: muy bueno para cadenas (La Celeste, Pugliese, Panicafé), dirección con número. |
| F1504 | mapcarta.com | Bajo: nombres, casi sin número. |
| F1505 | empresasdecordoba.com (/pagina/…) | **Medio-alto**: dirección + teléfono en el fragmento. |
| F1506 | yelp / wanderlog (listas "best bakeries") | Bajo: solo nombres. |
| F1507 | paginasamarillas.com.ar | Bajo: el fragmento no muestra direcciones. |
| — | cylex.com.ar, nuevaeranet, guiaoleo, tripadvisor, foursquare | Sin resultados útiles (cylex devolvió Córdoba, España; tripadvisor idem). |

## Alertas para la deduplicación
- Santa Rosa 724: "Buono Pane" (argentino) y "Panadería el Renuevo" (empresasdecordoba), misma dirección → posible cambio de nombre.
- Av. Fuerza Aérea 2966: Corradini = "Desayunos Sorpresa" (argentino); no se cargó el segundo.
- Europea, Levure, Gloria del Cerro, Nueva Delhi, Panes & Delicias aparecen en varios directorios (una sola fila, con la mejor fuente).
- "El Vergel [Gral. Paz]": dirección ambigua (calle General Paz 311 vs. barrio General Paz).
- Panadería San Alfonso (Recta Martinolli 7290): figura CERRADA permanentemente en RG.
- La Pana (Independencia 707): teléfono 03385 (otra característica) → verificar.
- Excluidos: Panadería Don Manuel (Av. Gral Paz 190, tel. 03541 = probable Villa Carlos Paz); Panadería Castillo (Don Bosco 2706, "San Vicente" — posible otra localidad); panificadoras sin nombre (Juan B. Justo 3900; Gral. Paz 1935 Alta Cba.); Mi Sueño (slug Malvinas Argentinas); resultados de Córdoba (España) y Veracruz.
- Panicafé, El Vergel, La Celeste, Pugliese, La Platense, Il Panettone se cargaron como `cadena_panaderia`.

## Qué rinde más (para futuras rondas)
1. `allowed_domains: lahelveticaonline.com.ar` + barrios en la consulta ("Panadería en Capital, Córdoba" + barrio).
2. `allowed_domains: empresasdecordoba.com` + "Panaderia teléfono Av".
3. `allowed_domains: waze.com` + nombre de cadena ("Driving directions … Córdoba").
4. `allowed_domains: argentino.com.ar` con "teléfono" + "Córdoba Capital" + nombre de avenida.
