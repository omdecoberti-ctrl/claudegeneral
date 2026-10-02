# Informe de competencia — Córdoba Capital (G3)

| Campo | Valor |
|---|---|
| Código | E-04 v3 · Consolida I013, I014 (a–h), I015 (a, b), I016 (a, b) |
| Fecha | 28/09/2026 · v2: 29/09/2026 · **v3: 02/10/2026** |
| Gate | G3 — Competencia |
| Estado | **v3: relevamiento de escritorio ampliado + zonas candidatas** (397 locales). Falta trabajo de campo (precios en góndola, cliente incógnito) y cruzarlo con la capa en vivo de OpenStreetMap |
| Mapa interactivo | [`MAPA_COMPETITIVO_CORDOBA.html`](MAPA_COMPETITIVO_CORDOBA.html): plano real de la ciudad, capas, filtros, Google Maps y panaderías de OpenStreetMap en vivo |
| Datos | `datos/locales_competencia.json` (**397 locales únicos, 194 marcas**) · `datos/locales_competencia.csv` (345 ubicados en el mapa) · `datos/precios_relevados.json` · `datos/locales_excluidos.json` |

> **Cómo leer este informe.**
> - Todo dato lleva etiqueta: [HECHO] con fuente, [ESTIMACIÓN], [INTERPRETACIÓN] o [RECOMENDACIÓN].
> - Las fuentes están en los anexos (códigos F100–F699) y en `00_MASTER/SOURCES.md`.
> - El relevamiento se hizo desde el buscador web: el entorno no permite abrir páginas completas ni Google Maps, y el cupo de búsquedas de la sesión se agotó.
> - Por eso **no es un censo completo**. Las cadenas grandes y el segmento moderno están bien cubiertos; las panaderías de barrio de la periferia, subrepresentadas. Para completarlo, el mapa trae una **capa en vivo de OpenStreetMap** que corre en el navegador de quien lo abre (ver §11).

> **Qué cambió en la v2 (29/09):** el censo pasó de **104 a 381 locales únicos** (4 excluidos por estar fuera de Córdoba Capital o cerrados; 26 duplicados fusionados):
> - **Cadenas:** sucursales de Del Pilar, Lo+Rico, Independencia, Armando y Perdú, y **9 cadenas nuevas identificadas**: El Vergel, Panicafé, Lapana, Medialunas 707, Andrea Franceschini, Catriel, Pugliese, La Platense y Santa Claus.
> - **Panaderías de barrio:** de 28 a 120.
> - **Indirectos:** 34 supermercados, 19 locales de comida rápida y 9 estaciones de servicio con tienda.
> - **Nuevos datos:** precios, redes y puntajes.

> **Qué cambió en la v3 (02/10):** foco en las **zonas candidatas Z05–Z08** y en los **competidores directos del formato** (detalle en `I014h_zonas_candidatas_y_competidores_directos.md`).
> - **+16 locales** (397 en total): Panicafé Villa Belgrano (Martinolli 6191), 3 El Vergel (Poeta Lugones, Panamericano, Spilimbergo), 6 Del Pilar (Urca, Castro Barros, Carrefour Martinolli, Gral. Paz 185, 9 de Julio 915, Vélez Sarsfield 3429), Lo+Rico Martinolli 7191, Tregua, Con Manteca, Qala Caffè, Fernández Villa Cabrera y La Milkería. Del Pilar del Cerro figura **cerrado** (excluido).
> - **Vigencia:** Panicafé, El Vergel, Fernández y La Celeste Valle Escondido (abrió ~may-2026) están activos; Cherry Season reabrió en el Cerro con casa matriz de 350 m² y tostadero.
> - **Nuevos:** fichas de Panicafé, Lapana y El Vergel, precios en apps de los 4 competidores directos y una lectura por zona candidata (§4b).
> - **Lo que dicen los clientes** (I016b, en el informe de cliente E-06): la queja n.º 1 de la categoría es la **frescura**.

<!--SVG:02_COMPETENCIA/graficos/cadenas_locales.svg-->

---

## 1. Resumen ejecutivo: 12 hallazgos

1. **La Celeste es el jugador a vencer en conveniencia.** [HECHO]
   - 16 locales propios, fundada en 1952, 10 de ellos abiertos las 24 h todo el año.
   - Muy concentrada en Nueva Córdoba (10 de 16 locales).
   - Producto ícono: el sándwich de miga. Está en Rappi, PedidosYa y en un canal propio (pedix).
   - Tiene 94 mil seguidores en Instagram.
2. **Su debilidad es la experiencia desigual entre locales.** [HECHO]
   - En Restaurantguru, Belgrano 439 tiene 4,4 con 2.376 reseñas; Obispo Trejo, 2,9, y Buenos Aires 1064, 2,6.
   - Quejas repetidas: calidad irregular, demoras, mala atención y precio.
   - Casi no tiene lugar para sentarse.
   - No tiene locales en el oeste, el este, el norte cercano, el noroeste ni la periferia.
3. **Del Pilar ya opera en Córdoba el modelo que evaluamos.** [HECHO]
   - 35 a 45 locales según la fuente (8 propios, el resto franquicias; incluye alrededores). Relevamos **13 con dirección en Córdoba Capital**.
   - Precios de piso masivo: medialuna de manteca $290 y 12 medialunas + criollo $5.600 (Rappi, sin fecha).
   - Planta de ultracongelado propia (−40 °C) que abastece locales, empresas y supermercados.
   - Es el competidor más parecido a una "panadería de un fabricante de congelados".
4. **El mapa de cadenas es más denso de lo que parecía.** Hay **16 cadenas locales** de panadería o medialunería con 3 o más locales: El Vergel (11), Medialunas 707 (11), Andrea Franceschini (11), Panicafé (9), Lapana (8), Pugliese (4), Catriel (4), La Platense (3), Santa Claus (3), más las ya conocidas. Además:
   - Lo+Rico: ~30 locales (22 de panadería y 8 de empanadas).
   - Panadería Independencia: 12–15 locales, franquicia sin regalías.
   - Armando Medialunas: de 8 a una meta de 13 locales.
   - [INTERPRETACIÓN] Con precio medio o bajo, el masivo es un océano rojo.
5. **El segmento moderno tiene audiencia de culto pero poca escala:**
   - Culpa de los Dos: 155 mil seguidores con unos 6 locales.
   - Cherry Season: 94 mil seguidores con 2–3 locales.
   - Superanfibio: 27 mil seguidores.
   - [INTERPRETACIÓN] La audiencia digital crece con el producto emblema y la experiencia, no con la cantidad de locales.
6. **Las cadenas de café porteñas no prosperan en la calle en Córdoba.** Café Martínez cerró la mayoría de sus locales y relanza con un inversor local. Havanna y Starbucks viven en shoppings, con apertura a las 10. [HECHO]
7. **La franja de 6:30 a 8 h está casi libre en el segmento de calidad.** Los cafés de especialidad abren a las 8 o más tarde y las cadenas de shopping, a las 10. Solo La Celeste (24 h) y las panaderías clásicas atienden esa franja. [HECHO + INTERPRETACIÓN]
8. **Escalera de precios del combo café + 2 medialunas:** Mostaza ~$3.600 → Café Martínez $6.900 → Havanna ~$7.000 → Starbucks $9.700. [HECHO, fechas dispares] Entre $4.500 y $5.500 hay un hueco sin una propuesta de calidad clara. [INTERPRETACIÓN]
9. **Hay un hueco de posicionamiento:** ninguna cadena local ocupa el cuadrante de precio medio (5–6) con experiencia media-alta (6–7). Las cadenas de panadería están en precio medio con experiencia baja; la experiencia alta es cara y no escala. [INTERPRETACIÓN]
10. **Geografía:**
    - Nueva Córdoba, el Centro y Güemes concentran la oferta moderna y las cadenas; están saturados.
    - El oeste (Alberdi, Alto Alberdi: un directorio cuenta 21 panaderías solo en Alto Alberdi) y la periferia son territorio de panadería clásica de barrio.
    - Argüello, Recta Martinoli y Valle Escondido (Z08) combinan poder adquisitivo con oferta clásica y pocas propuestas modernas.
    - [HECHO + INTERPRETACIÓN]
11. **"Del día anterior a mitad de precio" es práctica generalizada** en Córdoba. Nadie tiene un programa de fidelización propio visible; la fidelización la ponen terceros (bancos, ServiClub de YPF, apps). [HECHO + INTERPRETACIÓN]
12. **Sin TACC, saludable y catering para empresas están poco comunicados.** Solo Del Pilar comunica canal para empresas y galletas sin TACC; Lüben (General Paz) es una panadería 100% sin gluten. Es un espacio afín a lo que ya hace Canalsenses. [HECHO + INTERPRETACIÓN]

---

## 2. Mapa de la competencia

**Mapa interactivo:** abrir [`MAPA_COMPETITIVO_CORDOBA.html`](MAPA_COMPETITIVO_CORDOBA.html). En el sitio está en *Otros → Mapa competitivo*.
- Plano real de Córdoba (CARTO u OpenStreetMap).
- 10 zonas coloreadas, corredores comerciales e hitos.
- Filtros por tipo, zona y horario 24 h, y búsqueda.
- Cada local tiene un botón **"Ver en Google Maps"**.
- **Capa en vivo de OpenStreetMap:** todas las panaderías, pastelerías y cafés registrados, con ubicación exacta, asignados a su zona y exportables a Excel.

**Plano esquemático por zonas** (posiciones aproximadas por barrio):

<!--SVG:02_COMPETENCIA/mapa/esquema_zonas.svg-->

**Zoom al centro** (Centro, Nueva Córdoba, Güemes):

<!--SVG:02_COMPETENCIA/mapa/esquema_centro.svg-->

**Cómo se armaron las zonas:** las zonas Z01–Z10 son la segmentación de trabajo del proyecto. El plano las construye a partir del centro aproximado de 61 barrios (teselación de Voronoi recortada al ejido municipal, que es casi un cuadrado de ~24 km). Es un **esquema**, no un límite catastral: sirve para comparar zonas, no para medir distancias.

---

## 3. Segmentación del mercado competitivo

No todos compiten igual. Cada tipo de jugador se pelea por ocasiones distintas:

| Tipo | Qué es | Ocasiones que captura | Ejemplos en Córdoba | Relevados |
|---|---|---|---|---|
| **Cadena de panaderías** | 3 o más locales, marca de panadería | Compra para el hogar, desayuno para llevar, sándwiches, noche (24 h) | La Celeste, Del Pilar, El Vergel, Panicafé, Independencia, Lo+Rico, Perdú, Pugliese, Catriel, La Platense, Santa Claus | **92** |
| **Panadería de barrio** | Independiente, 1–2 locales | Compra diaria de pan y facturas, cercanía, domingo | Don Mignon, Delizzie, El Roble, Vicente, Panes y Costumbres, El Trigal, Futura, Perikos, La Blanca, Marcel… | **120** |
| **Bakery café / masa madre** | Panadería con café y salón, estética moderna | Desayuno y merienda con salón, brunch, pan premium | Lapana (8), Superanfibio, Fernández, La Capke, Brunchería, De a Deveras, Mocafe, Urban Bakery | **25** |
| **Medialunería / pastelería** | Foco en medialunas, facturas de autor y tortas | Merienda, "darse un gusto", regalo, delivery | Medialunas 707 (11), Andrea Franceschini (11), Armando (9), Culpa de los Dos, Frocca, Sharon, Essenza | **45** |
| **Café de especialidad** | Café de calidad más pastelería | Café de calidad, trabajo o estudio, cita | Cherry Season, Kråke, Ethiopia, Caffè del Popolo, Lattertulia, La Vereda de Achával, Le Dureau | 10 |
| **Cadena de café** | Marca nacional o internacional | Café de marca, shopping, aeropuerto | Havanna, Starbucks, Café Martínez, Bonafide, Tostado, Juan Valdez | 22 |
| **Comida rápida** | Desayuno económico | Desayuno barato, 24 h | Mostaza (8; Nueva Córdoba abre a las 6), McDonald's/McCafé (11 de 19) | **19** |
| **Conveniencia (estaciones)** | YPF Full, Shell Select, Axion Spot, Puma | Café al paso, ruta, noche | YPF Full 24 h (La Voz del Interior 6350, Las Malvinas 2595, Duarte Quirós 3607) | **9** (universo parcial) |
| **Supermercados** | Panadería propia y horneado en tienda | Compra de reposición, precio | Carrefour, Disco, Super MaMi, Libertad/La Anónima, Cordiez, Vea, Changomás, Makro | **34** (panadería propia verificada en Libertad, MaMi y Disco) |

[INTERPRETACIÓN] Para PAN-CBA, los competidores **directos** son las cadenas de panadería y las bakery-café. Los **indirectos por ocasión** son la especialidad, las cadenas de café, la comida rápida y la conveniencia en el desayuno para llevar. Los **sustitutos** son el supermercado y el desayuno en casa: el 86% desayuna en su casa (I006).

---

## 4. Análisis por zona

<!--SVG:02_COMPETENCIA/graficos/zonas_por_tipo.svg-->

> **Conteo v3 por zona** (locales relevados / panaderías): Z01 51/32 · Z02 48/27 · Z03 18/13 · Z04 31/19 · Z05 38/25 · Z06 37/21 · Z07 35/19 · Z08 30/15 · Z09 43/28 · Z10 14/4. Otros 52 registros no tienen barrio ni zona y no se pueden ubicar en el mapa.
>
> **Ajuste de lectura v2 [INTERPRETACIÓN]:** las zonas "sin La Celeste" no están vacías.
> - En Z05 (General Paz) y Z07 (Cerro) ya hay formatos panadería + café: **Panicafé** y **Lapana**.
> - En Z06 y Z04 está **El Vergel**, con muy buenas reseñas.
> - La oportunidad en esas zonas depende de ganarles en experiencia, café y consistencia, no de la falta de oferta.

| Zona | Perfil competitivo | Jugadores principales relevados | Lectura para PAN-CBA [INTERPRETACIÓN] |
|---|---|---|---|
| **Z01 Centro** | Cadenas de café y La Celeste; muchas oficinas y flujo peatonal diurno | La Celeste, Havanna, Starbucks, Café Martínez, Bonafide, Le Dureau | Alto flujo y alta competencia. Oportunidad en desayuno temprano y almuerzo rápido para oficinistas. Alquiler alto; muchas galerías vacías (40–50%). |
| **Z02 Nueva Córdoba** | **La zona más saturada**: 10 La Celeste, especialidad, medialunerías, cadenas | La Celeste (10), Cherry Season, Caffè del Popolo, Lattertulia, Perdú, Medialunas 707, Mostaza 24 h, Starbucks | Mercado estudiantil enorme (UNC), pero La Celeste domina la conveniencia 24 h. Entrar solo con un diferencial claro. |
| **Z03 Güemes / Observatorio** | Polo de merienda "instagrameable" (Belgrano y Achával Rodríguez) | Culpa de los Dos, Kråke, Ethiopia, Brunchería, La Capke, Armando | Público joven, dispuesto a pagar por experiencia. Hay pastelería de autor; falta panadería de calidad para llevar. |
| **Z04 Oeste (Alberdi, Alto Alberdi)** | Panadería clásica de barrio muy densa (21 en Alto Alberdi) | Don Mignon, Delizzie, Emilia, Delicias Artesanales; De a Deveras; Havanna y Starbucks (Nuevocentro) | Mucha competencia de precio bajo. Poco atractivo para un formato premium; posible para uno eficiente de precio medio. |
| **Z05 Este (General Paz, San Vicente)** | Polo gastronómico moderno más nichos | Lapana, Lüben (sin TACC), Questo Pane, Panz | Barrio con identidad foodie y **sin La Celeste**. Candidata a evaluar. |
| **Z06 Norte cercano (Alta Córdoba, Cofico, Lugones)** | Clásicas, pastelería de autor y shoppings | Panadero, Frocca, Artesanos del Sabor, Perdú, Medialunas 707; Havanna y Starbucks (Dinosaurio y Córdoba Shopping) | Gran población residencial (Alta Córdoba ~34.600 hab.) y **sin La Celeste**. Candidata a evaluar. |
| **Z07 Noroeste (Cerro, Urca, Villa Cabrera)** | Pastelería de alto ticket sobre Rafael Núñez | Cherry Season, Sharon, Europea, Gloria del Cerro, Superanfibio, Fernández | NSE alto y competencia premium. Hueco posible en panadería de calidad a precio medio y en conveniencia. |
| **Z08 Norte premium (Argüello, Villa Belgrano, Valle Escondido)** | Clásicas de buen nivel más La Celeste (Gauss y Valle Escondido 24 h) | El Roble, Vicente, Delizie D'Italia, Panes y Costumbres, Essenza, Culpa de los Dos | Zona en crecimiento con poder adquisitivo. Pocos formatos modernos de panadería con café. **Candidata fuerte.** |
| **Z09 Sur (Jardín, Manantiales, O'Higgins)** | Poco relevado; La Celeste (O'Higgins y Corro) e Independencia | Mocafe, La Celeste, Independencia | Manantiales crece fuerte (más de 25 mil habitantes, con proyección de 120 mil). Hay que relevar con OSM y en campo. |
| **Z10 Periferia** | Clásicas de precio bajo; cafés del aeropuerto | El Trigal, Los Boulevares, Vucetich; Juan Valdez y Tostado (aeropuerto) | Sensibilidad al precio alta. Baja prioridad para el local 1. |

**Nota:** los conteos reflejan cuánto se pudo relevar en cada zona, no la densidad real. La capa en vivo de OpenStreetMap del mapa agrega, por zona, la cantidad de panaderías registradas con ubicación exacta.

---

## 4b. Zonas candidatas Z05–Z08: competencia directa y alquiler (v3)

**Competidores directos del formato "panadería + café a precio medio"** (fichas completas en I014h):

| | Panicafé | Lapana | El Vergel |
|---|---|---|---|
| Locales en Capital | 8 relevados (Z01, Z02, Z05, Z07, Z08, Z09), con expansión por franquicias | 8 | 14 relevados, sin cuenta central de redes |
| Propuesta | Masa madre, heladería, comida todo el día | Combos de desayuno, locales de paso | Medialunas de manteca y criollos, con café |
| Reseñas | 8,4/10 con más de 16.000 reseñas (Cerro) · 9/10 con 4.058 (Gral. Paz), índices de agregadores | 3,4/5 en Tripadvisor (65 opiniones) | 4,2–4,9/5 en Restaurantguru |
| Qué critican | Salón saturado en hora pico, baños | Atención muy irregular | s/d |
| Café + medialunas (apps, oct-2026) | Café con leche + 2: **$6.850** | Café con leche + 2 mafaldas: **$7.700** | Café + 1: **$5.000–5.750** |
| Docena de medialunas (apps) | **$25.400** | s/d (suelta $1.600) | ≈ $17.200–20.000 (½ docena $8.600–10.000) |

Como referencia, La Celeste vende la docena a $10.620–15.600 en apps. **Panicafé cobra entre 1,6 y 2,4 veces más que La Celeste y aun así llena el salón**: hay disposición a pagar por la experiencia. [HECHO + INTERPRETACIÓN]

<!--SVG:02_COMPETENCIA/graficos/zonas_candidatas_alquiler.svg-->

| Zona | Competencia directa del formato | Alquiler a la calle, USD/m² (I029) | Lectura [INTERPRETACIÓN] |
|---|---|---|---|
| **Z05 General Paz / Juniors / San Vicente** | **Alta en el núcleo Esquiú / 25 de Mayo**: Panicafé, Lapana, Perdú, Bäckerhaus, Tregua, El Vergel, Armando. Juniors y San Vicente casi sin cadenas bakery-café (falta de datos, no prueba de vacío) | 5,5–10 (poco confiable: 2 avisos) | Evitar el núcleo de Gral. Paz. **Juniors / San Vicente**: opción a validar en campo |
| **Z06 Alta Córdoba / Cofico / Gral. Bustos** | **Media-baja.** El Vergel domina; no hay Panicafé ni Lapana; Con Manteca muestra demanda de especialidad en Cofico | 7–11 (1 aviso) | **La menos disputada.** Población residencial grande; alquiler holgado (3–6% de las ventas) |
| **Z07 Cerro / Villa Cabrera / Urca** | **Alta sobre Rafael Núñez** (Panicafé casa madre, Cherry Season, Superanfibio, Qala, Fernández). Villa Cabrera, intermedia | Cerro 9–12 · Villa Cabrera / Urca 5–13 | Rafael Núñez es un frente premium saturado. **Villa Cabrera (Caraffa)**: segunda opción |
| **Z08 Argüello / V. Belgrano / Valle Escondido** | **Creciente:** Panicafé (Martinolli 6191), La Celeste Valle Escondido (may-2026), La Milkería, Lo+Rico ×2, Del Pilar en Carrefour | Argüello 8,5–19 · Valle Escondido 18–22 | La demanda está validada, pero **la ventana se achica**. Solo con un local puntual muy bueno |

**Orden preliminar para la metodología de ubicación (G8) [RECOMENDACIÓN, a validar en campo]:**
1. Z06 Cofico / Alta Córdoba / Gral. Bustos.
2. Z07 Villa Cabrera (Caraffa).
3. Z05 Juniors / San Vicente.
4. Z08, solo con una oportunidad puntual.

Esto **reemplaza** la "candidata fuerte Z08" de la v2: en 2025–2026 llegaron tres competidores directos a esa zona.

**Doble perspectiva:** para el local 1 conviene la zona con menos competencia directa y un alquiler holgado. Para la red, Z06 y Z07 tienen corredores replicables (Fragueiro, Pablo Cabrera, Caraffa), y Z08 sigue siendo un destino natural de la 2.ª o 3.ª unidad.

---

## 5. Cadenas de panadería (competidores directos)

### 5.1 La Celeste: el gran jugador

| Dimensión | Dato |
|---|---|
| Historia | Fundada en 1952, más de 70 años. Locales propios; no franquicia. [HECHO] |
| Red | 16 sucursales: Z02 Nueva Córdoba 10 · Z01 1 · Z03 1 · Z08 2 (Gauss y Valle Escondido) · Z09 2 (O'Higgins y Corro). [HECHO] |
| Horario | **10 locales 24 h los 365 días**: Belgrano 439, Chacabuco 317, Colón 375, Gauss 5877, Obispo Oro 384, O'Higgins 5671, Rondeau 28, Obispo Salguero 512, Obispo Trejo 1029 y Gandhi 831. El resto abre de 6:10 a 22:20. [HECHO] |
| Oferta estrella | Sándwiches de miga (lo más elogiado), torta mil hojas, chipá, facturas de crema, medialunas, focaccia; helado desde 2024. [HECHO] |
| Canales | Mostrador para llevar (casi sin salón); Rappi (4,5–4,6), PedidosYa, pedix.app; estacionamiento en O'Higgins. [HECHO] |
| Comunicación | Instagram con 94 mil seguidores. Foco en tradición ("Panadería 1952"), 24 h, sorteos con influencers gastronómicos. [HECHO] |
| Modelo operativo aparente | Procesos de producción estandarizados; red densa. Probable producción centralizada (no verificado). [INTERPRETACIÓN] |
| Expansión | Planea abrir en zonas donde no está. La última apertura fue Valle Escondido 24 h. [HECHO] |

<!--SVG:02_COMPETENCIA/graficos/la_celeste_resenas.svg-->

**Fortalezas:**
- Marca histórica.
- La red 24 h es única en la ciudad.
- Domina Nueva Córdoba.
- Tiene un producto ícono (el sándwich de miga).
- Presencia en todas las apps.

**Debilidades:**
- La calidad de la experiencia varía mucho entre locales (de 2,6 a 4,4).
- Casi no tiene salón ni café para tomar en el lugar.
- Recibe críticas por precio y atención.
- No está en cinco zonas enteras.

**[INTERPRETACIÓN] Qué implica para PAN-CBA:**
- No conviene competirle de frente en Nueva Córdoba ni en 24 h.
- Sus flancos son la **experiencia consistente**, el **café y salón**, y las **zonas donde no está** (Z05, Z06, Z07, Z08 fuera de Gauss).
- Si PAN-CBA abre en una zona sin La Celeste, hay que esperar que La Celeste reaccione abriendo cerca: su plan es expandirse.

### 5.2 Del Pilar: el espejo de nuestro modelo

- **Red:** 45 locales (8 propios y 37 franquicias) en Córdoba y alrededores: Río Ceballos, Unquillo, Mendiolaza, Villa Allende y próximamente La Calera. [HECHO]
- **Planta propia de ultracongelado:** congela a −40 °C, conserva a −20 °C y transporta a −18 °C. [HECHO]
- **Tres frentes:** locales, empresas (catering para fábricas) y supermercados. [HECHO]
- **Formatos y comunicación:** módulo "Del Pilar Coffee". Comunica tradición: "más de 150 años". Instagram con 20 mil seguidores. [HECHO]
- **[INTERPRETACIÓN]** Demuestra que el modelo "planta de ultracongelado + franquicia + B2B" funciona en Córdoba a escala. Su punto débil es la experiencia, que depende de cada franquiciado, y la percepción de "pan industrial". PAN-CBA no puede ser "otro Del Pilar": necesita una propuesta más clara de experiencia y marca.
- **Pendiente:** direcciones de los 45 locales, precios y condiciones de franquicia (Q068).

### 5.3 Lo+Rico, Independencia, Armando y otras

| Marca | Locales | Modelo | Foco | Lectura [INTERPRETACIÓN] |
|---|---|---|---|---|
| **Lo+Rico** | ~30 (22 de panadería y 8 de empanadas), desde 2018 | Franquicia; expansión al interior | Medialunas, capilaridad, delivery; TikTok; 37 mil seguidores | Precio bajo o medio y volumen. Se diversifica hacia empanadas. |
| **Panadería Independencia** | 12–15 | Franquicia **sin regalías**, contratos de 3 años, exclusividad territorial | "La más antigua de Córdoba" (1863); 5,9 mil seguidores | La franquicia más barata para el franquiciado; poca presencia digital. |
| **Armando Medialunas** | de 8 a una meta de 13 | Expansión rápida | Especialista en medialunas | Formato chico y replicable. Referencia de formato. |
| **Perdú** | 5 o más (General Paz, Alta Córdoba, Alberdi, Nueva Córdoba) | s/d | "Calidad desde 1997"; 35 mil seguidores; rolls de canela, masa madre | Cadena local de rango medio. |
| **La Vene** (Mendoza) | 3 abiertos en 2018–19; meta de 20 | Franquicia con formatos "Pick & Go" y "Brunch & Coffee" | s/d | Sin evidencia de que siga abierta. Caso de aprendizaje: expansión que no se sostuvo. |
| **El Vergel** | 11 relevados | s/d | Panadería-confitería. Pablo Cabrera 2885 tiene 4,9 con 2.014 reseñas (Restaurant Guru) | Cadena local fuerte en el norte y oeste; referencia de calidad percibida |
| **Panicafé** | 9 (+1 en Villa Allende) | s/d | Panadería con café (General Paz, Cerro, Jardín) | Formato panadería + café ya presente en barrios: competidor directo del "tercer formato" |
| **Lapana** | 8 | s/d | Bakery moderna (General Paz y otros) | Referencia de formato moderno replicado |
| **Medialunas 707** | 11 | s/d | Medialunería; 4 mil seguidores por cuenta de sucursal | Formato chico especializado |
| **Andrea Franceschini** | 7 oficiales + 4 dudosos | s/d | Pastelería y tortas | Ocasión regalo y evento |
| **Pugliese, Catriel, La Platense, Santa Claus** | 3–4 cada una | s/d | Panaderías tradicionales con sucursales | Cadenas de barrio medianas |
| Descartadas | Pan de Oro (no está en Córdoba Capital) · La Reina Empanadas (11) y Panino (23) no son panaderías | — | — | — |

---

## 6. Segmento moderno: bakery, medialunería y especialidad

- **Culpa de los Dos:** pasó de marca de Instagram a unos 6 locales (incluye Villa General Belgrano). Tiene 155 mil seguidores, la audiencia más grande de Córdoba en el rubro. Producto de culto (alfajores, medialunas, mafaldas) y filas en la puerta. [HECHO]
- **Cherry Season** (ex ES Tostadores): tueste propio, puesto 63 entre las mejores cafeterías de Sudamérica, 94 mil seguidores. Tiene 3 locales y aperturas anunciadas (Nueva Córdoba y Estrada/Buenos Aires). Reels con presentadora propia. [HECHO]
- **Superanfibio:** café de especialidad y medialuna de masa madre. Tiene 3 locales (incluido Manantiales) y 27 mil seguidores; abre de 9 a 19. [HECHO]
- **Polo de Güemes:** Culpa de los Dos, Kråke, Ethiopia y Brunchería están en ~100 m (Belgrano y Achával Rodríguez). [HECHO]
- **[INTERPRETACIÓN]** Este segmento crea tendencia y comunidad, pero depende del fundador y del producto artesanal: le cuesta escalar. PAN-CBA puede tomar su **lenguaje** (producto emblema, estética, contenido) y sumarle lo que les falta: escala, horario temprano, consistencia y precio medio.

---

## 7. Cadenas de café, comida rápida y conveniencia

| Marca | Locales en Córdoba | Dato clave |
|---|---|---|
| Starbucks | 6 (Colón 608 en la calle; el resto en shoppings) | Combo más caro: $9.700 (may-2025) |
| Havanna | 5–6, más el local "Haireado" de 230 m² en Nuevocentro (inversión USD 120 mil) | Abre a las 10 en los shoppings |
| Café Martínez | 3; relanzamiento con inversor local (plan de 5 + 2) | Cerró la mayoría de sus locales en su primera etapa |
| Bonafide | 5–10 | El formato más parecido a un "café al paso" en el Centro |
| Tostado, Juan Valdez | Aeropuerto; Juan Valdez estudia un local en la ciudad | Llegada de marcas de afuera |
| Mostaza | 9 locales; "Open 24" en Plaza España (350 m²) | Techo bajo de precio: 2 medialunas + café ~$3.600 |
| McDonald's / McCafé | Más de 20 locales | Café + medialuna ~$4.000 |
| YPF Full | 3 relevadas con tienda 24 h | 29,3 M de medialunas vendidas en el país (ene–jul 2025); combo ~$7.700 en CABA; ServiClub |
| Supermercados | 34 relevados | Carrefour tiene 4 hiper y 19 Express en Capital; panadería propia verificada en Libertad/La Anónima, Super MaMi y Disco |

---

## 8. Panaderías de barrio

- **Oeste (Alberdi / Alto Alberdi):** es la zona de panadería clásica más densa. Un directorio cuenta 21 panaderías solo en Alto Alberdi. Abren de 7 a 21 o 22 todos los días. [HECHO]
- **Argüello y Recta Martinoli (Z08):** clásicas de buen nivel que abren desde las 6 (El Roble, Vicente, Delizie D'Italia, Panes y Costumbres). [HECHO]
- **Nichos emergentes:** panadería 100% sin gluten (Lüben), fábricas de pan que venden al público (Panz) y masa madre. [HECHO]
- **Premios:** en el 1.er Campeonato Nacional del Criollito (FITHEP 2025) el podio fue cordobés; el 3.er puesto fue Artesanos del Sabor. [HECHO]
- **Contexto:** CIPAC reporta caídas de ventas de 30–40% en 2025 y unos 20 cierres en la ciudad. [HECHO]
- **v2:** 120 panaderías de barrio relevadas. Donde más hay es en el Sur (Z09: Jardín, Santa Isabel, Las Flores, Villa El Libertador), el Este (Z05: General Paz, Juniors, Talleres, Yofre), el Norte cercano (Z06: Alta Córdoba, General Bustos) y el Oeste (Z04). [HECHO]
- **Calidad del dato:** muchas fichas de directorios son de 2016–2018, así que algunos locales pueden haber cerrado. Además se detectó un listado que mezclaba panaderías de Santa Fe. [HECHO]
- **Cantidad total:** no hay un dato oficial público de cuántas panaderías hay habilitadas en la ciudad.
- **[INTERPRETACIÓN]** La panadería de barrio compite por **cercanía y precio**. Está debilitada por la crisis y rara vez tiene marca, delivery o experiencia. Un formato estandarizado puede ganarle en consistencia, surtido, horario y comunicación, pero no en precio. Varias podrían ser **franquiciadas o clientes** de PAN-CBA en el futuro.

---

## 9. Redes sociales y comunicación

<!--SVG:02_COMPETENCIA/graficos/instagram_seguidores.svg-->

| Marca | Foco de comunicación | Formato que funciona |
|---|---|---|
| La Celeste | Tradición 1952, 24 h, sándwiches de miga | Sorteos con influencers |
| Del Pilar | Tradición "150 años", franquicias, empresas y supermercados | Institucional |
| Lo+Rico | Medialunas, capilaridad, delivery | TikTok y submarca de empanadas (19 mil) |
| Independencia | "La más antigua" (1863) | Institucional, baja actividad |
| Culpa de los Dos | Producto de culto, escasez y filas | Contenido de producto, comunidad |
| Cherry Season | Tueste propio, brunch, cara humana | Reels con presentadora |
| Superanfibio | Especialidad, minimalismo, merienda | Estética |
| Havanna / Café Martínez / Starbucks | Combos, promociones bancarias, app | Promociones |

**Puntajes (Restaurant Guru, v2):** Cherry Season 4,8 en Tripadvisor (#5 de 655) · El Vergel Pablo Cabrera 4,9 (2.014 reseñas) · Independencia Urca 4,1 · Perdú 3,4 (544 reseñas) · Lo+Rico 6,2/10 · La Celeste de 2,6 a 4,4 según el local.

**[INTERPRETACIÓN]**
- Las cadenas de panadería comunican **tradición**; las modernas comunican **producto y experiencia**.
- Nadie comunica bien **calidad consistente, rapidez y precio justo**, ni **frescura verificable** ("horneado acá, cada hora").
- No se vio ningún club de fidelización propio.

---

## 10. Precios y posicionamiento

**Precios relevados en v2** (Rappi/PedidosYa y prensa, fechas dispares; confirmar en el local):
- **Del Pilar:** medialuna de manteca $290; 12 medialunas + criollo $5.600. Es el piso masivo, ~$470 por unidad.
- **Lo+Rico:** combo de medialunas con criollo $9.880.
- **Armando:** docena premium rellena $23.328 (~$1.944 por unidad).
- **Bonafide Córdoba:** café 12 oz + 1 medialuna $3.308; café con leche + alfajor $2.400.
- **Especialidad en Córdoba:** espresso $3.200 y medialuna $2.500 (oct-2025).
- **Facturas en Alta Gracia:** docena del día $7.200; 10 del día anterior $3.600 (abril 2025).

- **v3 (apps, oct-2026):** Panicafé café con leche + 2 medialunas $6.850 y docena $25.400 · Lapana café con leche + 2 mafaldas $7.700 · El Vergel café + 1 medialuna $5.000–5.750 · La Celeste docena $10.620–15.600 y medialuna $1.300 · Havanna espresso $3.800 (sep-2026).

**Índice propuesto "café con leche + 2 medialunas"** (a relevar el primer lunes de cada mes): panadería masiva ~$2.600–3.100 · comida rápida $3.600 · cadena de cafetería ~$4.100–4.300 · YPF Full ~$7.700 · especialidad $8.200 o más.

**Referencia del Centro de Panaderos (abril 2026):** pan francés $3.500/kg, mignon $4.000/kg, criollos $8.000/kg, facturas desde $1.000 por unidad. La medialuna en carta de cafetería cuesta $1.400–1.600 (agosto 2026). [HECHO]

<!--SVG:02_COMPETENCIA/graficos/escalera_combo_desayuno.svg-->

<!--SVG:02_COMPETENCIA/graficos/posicionamiento_precio_experiencia.svg-->

<!--SVG:02_COMPETENCIA/graficos/posicionamiento_precio_conveniencia.svg-->

**Lectura [INTERPRETACIÓN]:**
- **Conveniencia saturada** en precio medio y bajo: YPF Full, La Celeste, Del Pilar, Lo+Rico, Mostaza.
- **Experiencia alta, pero cara y de baja escala:** Cherry Season, Superanfibio, Starbucks.
- **Hueco:** precio medio (5–6) con experiencia media-alta (6–7) y conveniencia alta (horario temprano, rapidez, apps). En Córdoba no hay una cadena que combine las tres.

---

## 11. Espacios en blanco (hipótesis a validar)

| # | Espacio | Evidencia | Perspectiva 1: local 1 | Perspectiva 2: red / franquicia | Cómo validarlo |
|---|---|---|---|---|---|
| EB1 | **"Tercer formato":** pan y facturas de calidad para llevar, más buen café, precio medio y experiencia consistente | Hueco en el mapa de posicionamiento; La Celeste es desigual; lo moderno es caro y no escala. **v2:** Panicafé (9) y Lapana (8) ya lo intentan en barrios; hay que visitarlos antes de decidir | Diferencia sin guerra de precios | Muy estandarizable si el producto viene de la planta de UC | E001 test de concepto, E003 pop-up |
| EB2 | **Desayuno temprano de calidad (6:30–9 h)** fuera de los shoppings | Especialidad y cadenas abren a las 8–10 | Captura oficinistas, estudiantes y tráfico al trabajo | Replicable en corredores | Conteos de gente en la calle 6:30–9 h (I028) |
| EB3 | **Zonas sin La Celeste con buen poder adquisitivo:** Z05 General Paz, Z06 Alta Córdoba, Z07 Cerro / Villa Cabrera, Z08 Argüello y Villa Belgrano, Z09 Manantiales | Mapa de cobertura (§4, §5.1) | Menos competencia directa 24 h | Plan de expansión por zonas | Puntaje de ubicaciones (G8) + OSM + campo |
| EB4 | **Frescura verificable y relato honesto del congelado** ("fermentación lenta en planta, horneado acá cada hora") | 41% valora "horneado en el local" (I002); A006 | Resuelve el riesgo de percepción | Estándar de marca | E002 degustación ciega |
| EB5 | **Fidelización propia simple** (QR o billetera, suscripción de café) | Nadie tiene club propio visible | Frecuencia | Base de datos de clientes para la red | Piloto |
| EB6 | **Empresas y catering de desayuno para oficinas**, más sin TACC envasado | Solo Del Pilar lo comunica | Ingreso extra en horas valle | Aprovecha la planta de UC | Entrevistas a empresas (A015) |
| EB7 | **Producto emblema cordobés** (criollo, chipá o medialuna de autor) viral y estandarizado en planta | Culpa de los Dos y Armando muestran el poder del producto de culto | Tráfico y contenido | Replicable (receta de planta) | Degustación + redes |

---

## 12. Reacciones esperables de la competencia

- **La Celeste:** podría abrir cerca (planea expandirse), sumar café o salón, o mejorar su servicio.
- **Del Pilar y Lo+Rico:** podrían bajar precios, ofrecer promociones, o acelerar franquicias en la misma zona.
- **Panaderías de barrio:** podrían dar descuentos de "día anterior" o competir por fidelidad del vecino.
- **Canalsenses:** la marca propia podría molestar a clientes mayoristas en Córdoba (R019), en particular si Del Pilar, Lo+Rico o La Celeste compran a UC (Q068).

---

## 13. Implicancias, preguntas y próximos pasos

**Implicancias [RECOMENDACIÓN]:**
1. Llevar a la etapa de conceptos (G4) el "tercer formato" (EB1) como concepto candidato principal, **junto con al menos 3 alternativas**, para no sesgar la decisión.
2. Excluir Nueva Córdoba como primera opción de ubicación, salvo que aparezca un diferencial muy fuerte. **v3:** priorizar Z06, Z07 (Villa Cabrera) y Z05 (Juniors / San Vicente); Z08 solo con una oportunidad puntual (§4b).
3. Tomar a Del Pilar como caso de estudio del modelo: franquicias, planta y operación de sus locales.
4. Diseñar la comunicación desde el día 1 sobre producto emblema, frescura visible y consistencia.

**Próximos pasos:**
- **Cruzar el censo v3 (397) con la capa OpenStreetMap del mapa**, que trae ubicaciones exactas y locales que el buscador no ve. Un socio abre el mapa, hace clic en "Exportar datos OSM", baja el CSV y me lo pasa (o lo sube al repositorio). Con eso actualizo densidades por zona y por barrio.
- **Hecho en v3:** sucursales de Del Pilar y Lo+Rico en zonas candidatas, vigencia de locales clave, fichas de Panicafé, Lapana y El Vergel, y precios en apps.
- **Sigue pendiente (solo se resuelve en campo o con la página oficial):** listado completo de Del Pilar (declara 35–45), vigencia de Delizie, El Roble y Vicente, y precios en mostrador.
- **Trabajo de campo (PD031):**
  - índice de precios "café con leche + 2 medialunas" y docena de facturas en 20 locales;
  - cliente incógnito en La Celeste, Del Pilar, Lo+Rico, Culpa de los Dos y Cherry Season;
  - conteos de gente de 6:30 a 9 h en 3 corredores candidatos.
- **Oscar:** ¿cuáles de estos competidores son clientes de UC? (Q068)

## Anexos (detalle y fuentes)
- `I014_cadenas_panaderia_cordoba.md`: perfiles de La Celeste, Del Pilar, Lo+Rico e Independencia (F300–F344).
- `I014b_cafeterias_bakery_especialidad.md`: bakery, especialidad y cadenas de café (F401–F449).
- `I014c_panaderias_de_barrio.md`: censo de barrio por zona (F500–F511).
- `I015_I016_redes_precios_posicionamiento.md`: redes, precios y posicionamiento (F600–F668).
- `I014h_zonas_candidatas_y_competidores_directos.md`: zonas Z05–Z08, Panicafé, Lapana, El Vergel, vigencia y precios en apps (F2200–F2238).
- `../03_CLIENTE/I016b_quejas_y_elogios_clientes.md`: qué critica y qué elogia el cliente (F2320–F2339).
- `../08_UBICACIONES/I029_alquileres_comerciales_por_zona.md`: alquileres por zona (F1800–F1844).
- `I014d_cadenas_sucursales_v2.md` (F1100–F1167) · `I014e_panaderias_de_barrio_v2.md` (F1200–F1320) · `I014f_competidores_indirectos.md` (F1400–F1443) · `I014g_directorios_panaderias.md` (F1500–F1507) · `I015b_precios_redes_v2.md` (F1600–F1633): ampliación v2.
- `datos/locales_excluidos.json`: registros descartados y motivo.
- `I013_censo_competitivo_cordoba.md` e `I018_franquicias_panaderia_cafe.md`: primera pasada y franquicias.
