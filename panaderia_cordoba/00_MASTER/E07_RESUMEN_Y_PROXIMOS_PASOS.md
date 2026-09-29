# Resumen del proyecto: qué hicimos, qué aprendimos y qué sigue

| Campo | Valor |
|---|---|
| Código | E-07 · Resumen ejecutivo al 29/09/2026 |
| Gate actual | G0 casi cerrado · G1–G3 con investigación de escritorio v2 · falta trabajo de campo |
| Apertura objetivo | 01–08/03/2027 (D004) · **quedan ~22 semanas** |
| Sitio | https://panaderia-cordoba.vercel.app |

---

## 1. En una frase
En 5 días pasamos de cero a:
- un proyecto organizado, con 8 decisiones aprobadas y un plan a marzo;
- un sitio con panel por socio;
- los primeros informes de mercado, cliente y competencia, con mapa y __NLOC__ competidores relevados.

**Lo que falta para elegir el concepto el 13/11:** escuchar al cliente (trabajo de campo), probar el producto (degustación a ciegas) y tomar tres decisiones pendientes.

---

## 2. Qué hicimos

| Bloque | Qué se hizo | Dónde está |
|---|---|---|
| **Organización (G0)** | Estructura 00–19 · metodología (gates, decisiones, etiquetas de evidencia) · roadmap G0–G15 · registros de decisiones (D), hipótesis (A), preguntas (Q), riesgos (R), tareas (T) y fuentes (F) | `00_MASTER/` |
| **Decisiones aprobadas** | D001 metodología · D002 subsidiaria de UC, decisiones por mayoría, encargado contratado · D003 USD 100k + 20k de reserva · D004 apertura en marzo 2027 · D005 investigación · D006 revisión semanal y entregables en PDF/HTML · D007–D008 sitio en Vercel con usuario por socio | `DECISIONS.md` |
| **Plan a marzo** | Roadmap semana a semana con 3 fechas de corte: 13/11 concepto · 15/12 local firmado · 14/02 obra terminada | E-01 · `15_APERTURA/` |
| **Sitio web** | Tablero general, panel por socio, registros con filtros, códigos enlazados, buscador, entregables, mapa | panaderia-cordoba.vercel.app |
| **Mercado (G1)** | Tamaño (TAM ~USD 333 M), demografía, consumo, crisis del rubro, 10 tendencias, referentes, macro y costos | E-05 · `01_MERCADO/` |
| **Cliente (G2)** | 10 segmentos con puntaje, ocasiones por franja horaria, necesidades del cliente (jobs-to-be-done), perfiles tipo; guía de entrevistas, encuesta, protocolo de cliente incógnito, degustación E002 | E-06 · `03_CLIENTE/` |
| **Competencia (G3)** | __NLOC__ locales en __NMARCAS__ marcas · mapa interactivo con zonas, Google Maps y datos de OpenStreetMap en vivo · La Celeste sucursal por sucursal · redes, precios, posicionamiento · 7 espacios en blanco | E-04 · `02_COMPETENCIA/` |
| **Franquicias** | Modelos en Argentina (el fabricante gana con el producto, no con la regalía), marco legal, referentes | I018 |
| **Canalsenses** | Relevamiento público: planta en Canals, 200–250 t/mes, ~35 variedades, 40% de capacidad ociosa | I010 |

---

## 3. Qué aprendimos (lo que más pesa para decidir)

1. **El pan tradicional está en crisis** (ventas −30/40% en Córdoba en 2025). Competir con pan común por precio es mal negocio. El valor está en los productos de margen, en el desayuno y la merienda, en el café y en la conveniencia.
2. **La Celeste es el rival en conveniencia:** 16 locales, 10 abiertos 24 h, 94 mil seguidores. Su experiencia es desigual (reseñas de 2,6 a 4,4) y no tiene locales en 5 zonas.
3. **Del Pilar ya aplica nuestro modelo:** 45 locales, planta de ultracongelado, franquicias. No alcanza con producir en planta: hace falta un concepto distinto.
4. **Hueco de posicionamiento:** precio medio + experiencia media-alta + desayuno temprano (6:30–9 h). En la escalera de precios del combo, el espacio libre está entre $4.500 y $5.500.
5. **Zonas candidatas:** Z08 Argüello/Villa Belgrano, Z05 General Paz, Z06 Alta Córdoba y Z07 Cerro/Villa Cabrera. Nueva Córdoba está saturada.
6. **El cliente:** desayuna en casa (86%), recortó salidas (76%), compra de a unidad y "del día anterior", valora la frescura (71%) y paga con QR (84%).
7. **Riesgo de percepción:** al 72% le importa que sea "hecho a mano", pero al 41% le suma que esté "horneado en el local". Hay que probarlo con la degustación a ciegas antes de decidir.
8. **Logística:** con entregas desde Canals cada 15 días, el local necesita mucho stock congelado. Hay que resolver entrega semanal o un depósito en Córdoba.
9. **Franquicia:** el modelo natural para UC es ganar con el producto, no con la regalía. La ley parece exigir historia operativa del local antes de franquiciar (a confirmar por Laura), lo que empuja las franquicias a 2028.
10. **Contexto:** inflación bajando (1,8% mensual en Córdoba), dólar oficial ≈ MEP, demanda débil (pobreza 31%). Conviene planificar en USD.

---

## 4. Decisiones que tienen que tomar los socios

| Código | Decisión | Recomendación | Cuándo |
|---|---|---|---|
| **PD029** | Plan acelerado a marzo con 3 fechas de corte | Aprobar (opción A) | **Ya** |
| **PD031** | Quién hace el trabajo de campo y con qué presupuesto | Mixto (estudiantes + hermanos), USD 3–5 mil | **Ya** |
| **PD002** | Completar gobernanza: ¿la mayoría es por persona o por capital? ¿Quién es el interlocutor? | Interlocutor: Oscar. Responsables: Oscar operaciones · Fabiola finanzas · Laura legal | **Ya** |
| PD030 | Expansión 2027 | 2ª unidad propia en el 2.º semestre de 2027; franquicias en 2028 | Puede esperar |
| PD027 | Forma jurídica de la subsidiaria y precios de transferencia con UC | Fabiola + Laura proponen | Octubre |
| PD032 | Convivencia de la marca propia con los clientes mayoristas de UC | Necesita la respuesta a Q068 | Noviembre |
| PD008 | Criterios para evaluar conceptos (antes de ver los conceptos) | La IA los propone en octubre | 23/10 |

---

## 5. Qué tiene que hacer cada uno

| Quién | Qué | Código | Para cuándo |
|---|---|---|---|
| **Todos** | Leer E-04, E-05 y E-06; decidir PD029, PD031 y PD002 | T022, T023 | 05/10 |
| **Todos** | Entrar al sitio con su usuario | T028 | Esta semana |
| **Oscar** | Catálogo UC con precios de transferencia · contactos de 3–5 clientes que hornean en su local · ¿Del Pilar, Lo+Rico o La Celeste le compran a UC? · ¿los panes crudos fermentan en el local? · ¿se puede entregar semanal en Córdoba? | T024 · Q068 · Q053 · Q054 | 05/10 |
| **Laura** | Plazos reales de habilitación municipal y bromatológica (**es lo que puede atrasar la apertura**) · requisitos legales para franquiciar | T020 · Q064 | 16/10 |
| **Fabiola** | Estructura de la subsidiaria y criterio de precios de transferencia | PD027 | 23/10 |
| **Socios / campo** | Exportar los datos de OpenStreetMap desde el mapa · entrevistas, encuesta, cliente incógnito · degustación a ciegas E002 | T030 · T017 · T033 | 12/10 → 06/11 |

## 6. Qué hago yo (IA) en las próximas 2 semanas
1. Integrar el CSV de OpenStreetMap y los datos de campo a medida que lleguen: densidad real de competidores por zona y barrio.
2. Relevar normativa y plazos de habilitación (I035), junto con Laura.
3. Comparar modelos productivos: horneado en local vs. producción central vs. híbrido, con costos y superficie (I011).
4. Proponer criterios de evaluación (PD008) y preparar 4–6 conceptos (G4).
5. Metodología y puntaje de ubicaciones (G8), con prioridad en las zonas Z05–Z08.
6. Pre-modelo económico por concepto (I019).

---

## 7. Qué repasar o validar (lo que todavía no es firme)

| Tema | Por qué hay que repasarlo | Cómo |
|---|---|---|
| Datos de mercado y competencia | Salen de resúmenes de buscador, no de las fuentes completas | Verificar en origen (T032) y con campo |
| Censo de panaderías de barrio | Aunque se amplió, un buscador no ve todo | Exportar OSM (T030) + recorrida en las zonas candidatas |
| Tamaño de mercado | Es una estimación con supuestos | Recalcular con la encuesta de gasto de los hogares (ENGHo) y los resultados de la encuesta |
| Aceptación del producto de planta | Evidencia mixta | Degustación a ciegas E002 |
| Ticket y frecuencia | Estimados | Encuesta I008 + cliente incógnito |
| Logística desde Canals | Puede cambiar el m² y el costo del local | Respuesta de Oscar (Q054) |
| Plazos de habilitación | Ruta crítica del plan a marzo | T020 |
| Conflicto de canal con clientes de UC | Puede condicionar zona, marca y producto | Q068 + PD032 |

---

## 8. Calendario inmediato

| Fecha | Hito |
|---|---|
| 05/10 | Revisión semanal 1: decisiones PD029, PD031, PD002 + información de Oscar |
| 09/10 | Gate Review G0 |
| 12/10 → 06/11 | Trabajo de campo + degustación E002 |
| 23/10 | Criterios de evaluación de conceptos (PD008) |
| 30/10 | Gate Review G1–G3 |
| 02/11 → 13/11 | Conceptos + test de concepto → **CORTE 1: concepto elegido (13/11)** |
| Noviembre–diciembre | Producto, precios y números por unidad · búsqueda de local → **CORTE 2: local firmado (15/12)** |
