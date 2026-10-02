# I005b — Costos y cliente, v2 (P3: completa huecos de I005 e I006)

**Proyecto:** PAN-CBA (panadería-café en Córdoba Capital) · **Fecha de corte:** 2026-10-02 · **Rol:** economía del proyecto
**Método:** 30 búsquedas web (WebSearch; WebFetch bloqueado). Los datos salen de los fragmentos que devuelve el buscador. No se abrieron los PDF completos, así que varios valores quedan para verificar en la fuente primaria (se marcan con ⚠).
**Etiquetas:** [HECHO] dato con fuente · [ESTIMACIÓN] cálculo propio a partir de hechos · [SUPUESTO] parámetro sin fuente · [INTERPRETACIÓN] lectura del analista.
**Tipo de cambio de referencia:** MEP $1.553 (F905 de I005).

> **Qué cierra este informe:** pendientes 2, 3, 4, 5, 6 y 8 de I005 §7 y la brecha 2 de I006 §9 (ocupados por rama). **Siguen abiertos:** alquileres por zona, habilitaciones y reseñas de clientes.

---

## Resumen ejecutivo (números clave)

| Tema | Número clave | Etiqueta |
|---|---|---|
| UTHGRA (CCT 389/04), básicos jul–sep-2026 (categoría base) | N2 mozo de mostrador $1.047.930 · N3 cafetero (el "barista" del convenio) $1.099.139 · N5 cajero $1.210.980 · N6 mozo/barman/encargado $1.292.026, más sumas no remunerativas de $72–88 mil | [HECHO] F1900–F1903 |
| Costo empleador por puesto UTHGRA | entre ≈ $1,49 M (N2) y ≈ $1,84 M (N6) por mes | [ESTIMACIÓN] |
| Panaderos Córdoba Capital (Sociedad Obreros Panaderos) | Hay escala 2026 publicada, pero **no se pudieron leer los montos** (sigue s/d). Como referencia de otro convenio panadero: "Oficial Maestro" $1.667.783 (ago-26) y $1.699.471 (sep-26) | [HECHO, otro CCT] F1904–F1906 |
| Mercado Pago Point | débito **3,25% + IVA** al instante (2,99% a 2 días); crédito **6,29% / 5,39% / 4,39% + IVA** (al instante / 5 días / 10 días) | [HECHO] F1907 |
| Mercado Pago QR | dinero en cuenta **0,8%**; débito por QR 1,35% al instante / 0,85% a 2 días | [HECHO] F1908–F1910 |
| Posnet tradicional | Getnet 2,29% débito / 3,79% crédito (72 h); Payway 2,39% / 3,89% (5–7 días) | [HECHO] F1911 |
| Costo de cobro ponderado | ≈ **2,6% + IVA ≈ 3,1% de la venta** con todo acreditado al instante; ≈ 2,3% si se optimizan los plazos | [ESTIMACIÓN] |
| Café en grano | **$34.960/kg + IVA** (saco de 46 kg) · ≈ $38.560/kg (caja de 6 kg) · $28.600–41.000/kg (bolsa de 1 kg) | [HECHO] F1912 |
| Costo de café por taza | ≈ **$250–380 el espresso simple** (7–9 g) → 8–12% de un precio de carta de $3.200–3.800 | [ESTIMACIÓN] |
| Azúcar | $30.165 la bolsa de 50 kg (≈ $603/kg), 2-sep-2026 ⚠ | [HECHO] F1915 |
| Leche entera en sachet | $2.049–2.725 por litro (góndola online) | [HECHO] F1916 |
| Ecogas, Servicio General P (comercios) | cargo fijo **$94.724/mes** + **$341,25/m³** (de 0 a 1.000 m³), desde 1-ago-2026 ⚠ | [HECHO] F1919 |
| EPEC, Tarifa N°2 (comercios hasta 40 kW) | Ene-2026 vs dic-2025: **+3,7% a +6,6%**. El precio por kWh quedó sin confirmar | [HECHO parcial] F1917–F1918 |
| ENGHo 2017/18 | Alimentos y bebidas no alcohólicas: **22,7%** del gasto (país) y 23,1% (Pampeana) · **pan: 6,1% del gasto en alimentos** (país) y **6,0%** (Pampeana) · restaurantes y comidas fuera del hogar: **6,2%** del gasto total (país); "restaurantes y hoteles" en la Pampeana: 6,3% | [HECHO] F1920–F1923 |
| Gran Córdoba, EPH II-T 2026 | **736 mil ocupados** (−11 mil i.a.), desocupación **10,5%** (87 mil personas), **71,8% asalariados** | [HECHO] F1924–F1926 |
| Ticket de cafetería en Córdoba | espresso $3.200 · cappuccino $4.500 · combo infusión + 2 medialunas **$7.500** (cafetería premiada) · Havanna sep-26: espresso $3.800, café con leche $5.400–6.200 | [HECHO] F1928–F1929 |
| Ticket de desayuno/merienda que proponemos para el modelo | **$7.500–11.000 por persona** (reemplaza el SUPUESTO de $7.000 de I005) | [ESTIMACIÓN] |
| Fin de semana / "domingo de facturas" | Antes de la crisis: 20–30 docenas por día de lunes a viernes contra **~100 docenas** el fin de semana (× 3–5). La venta de facturas cayó **85%** contra 2023 | [HECHO, testimonios del sector] F1932–F1934 |
| Ticket de delivery | **s/d.** Los $3.000–3.900 "por pedido" que circulan son **lo que cobra el repartidor**, no el ticket del cliente | [HECHO, con aclaración] F1936–F1938 |

---

## A. Costos

### A1. Escalas salariales 2026

#### A1.1 UTHGRA – FEHGRA (CCT 389/04), básicos de jul–sep-2026, categoría base del establecimiento

| Nivel / puesto (CCT 389/04) | Equivalente en PAN-CBA | Básico | Suma no remunerativa | Costo empleador mensualizado* | USD (MEP) | Etiqueta | Fuente |
|---|---|---|---|---|---|---|---|
| N1 (bachero, maestranza) | bacha / limpieza | $990.555 | s/d | ≈ $1.341.000 | ≈ 864 | [HECHO] básico (I005) / [ESTIMACIÓN] | F919–F920 (I005) |
| N2 (mozo de mostrador) | vendedor/a de mostrador en el salón | $1.047.930 | $72.000 | ≈ $1.491.000 | ≈ 960 | [HECHO] / [ESTIMACIÓN] | F1901 |
| N3 (**cafetero** ≈ barista) | barista | $1.099.139 | $75.000 | ≈ $1.563.000 | ≈ 1.006 | [HECHO] / [ESTIMACIÓN] | F1903 |
| N5 (cajero) | cajero/a | $1.210.980 | $83.000 | ≈ $1.723.000 | ≈ 1.109 | [HECHO] / [ESTIMACIÓN] | F1901 |
| N6 (mozo, cocinero, barman, capataz o encargado) | mozo/a de salón, encargado/a de turno | $1.292.026 | $88.000 | ≈ $1.838.000 | ≈ 1.184 | [HECHO] / [ESTIMACIÓN] | F1901, F1903 |
| N7 (supervisión) | — | solo existe en establecimientos de categoría superior | — | — | — | [HECHO] | F1903 |

\* Costo empleador = básico × 1,25 (cargas sociales) × 13/12 (aguinaldo) + suma no remunerativa. Es la misma convención que usa I005. No incluye antigüedad, presentismo, vacaciones ni adicionales del convenio. [ESTIMACIÓN]

- [HECHO] Los básicos de junio se mantienen en julio, agosto y septiembre de 2026. La negociación se reabre a fin de año (F1900, F1902).
- [HECHO] La escala combina la categoría del establecimiento (estrellas, tenedores o copas) con el nivel profesional (F1902). ⚠ Hay que verificar la categoría que corresponde a PAN-CBA.

#### A1.2 Panaderos

| Ítem | Dato | Etiqueta | Fuente |
|---|---|---|---|
| Sociedad Obreros Panaderos de Córdoba Capital y su Zona de Actuación | Publica escalas 2026 para "Córdoba Capital", "Interior A", "Interior B" y "Río Cuarto". **No se pudieron leer los montos por categoría** (maestro, ayudante, vendedora) | [HECHO] existencia / montos **s/d** | F1904, F1905 |
| Acuerdo homologado (Sociedad Obreros Panaderos de Córdoba Capital – Centro Industriales Panaderos y Afines de Córdoba) | Acuerdo y escalas homologados por la Disposición 1946/2025 (acuerdo del 21-ago-2025). Confirma que **hay un convenio local** distinto del FAUPPA–FAIPA | [HECHO] | F1905 |
| Referencia de otro convenio panadero (CCT 231/94, SOPSTE) | "Oficial Maestro" $1.667.783 (ago-2026) y $1.699.471 (sep-2026), con revisión salarial del 28-sep-2026 que fija tramos hasta dic-2026 | [HECHO] no es Córdoba | F1906 |
| FAUPPA–FAIPA, junio 2026 (ya en I005) | Maestro $1.285.276 · medio oficial/cajero $1.265.873 | [HECHO] | F917 (I005) |

- [ESTIMACIÓN] Si el maestro panadero cordobés estuviera en la banda de $1,29–1,70 M de básico (entre el piso FAUPPA y la referencia de CCT 231/94), su costo empleador mensualizado iría de **$1,74 M a $2,30 M**. Hasta conseguir la planilla local, usar **$2,0 M** como valor central [SUPUESTO].
- [INTERPRETACIÓN] El gremio local de panaderos de Córdoba existe y tiene escala propia. El encuadre del personal de producción (panaderos) y de venta de mostrador de pan va casi seguro por ese convenio, y el de salón y barra por UTHGRA. **Acción:** descargar la planilla en socobpancba.ar (F1904) o pedirla al Centro de Industriales Panaderos.

### A2. Medios de pago: comisiones y plazos (2026)

| Medio | Al instante | Plazo más largo | Etiqueta | Fuente |
|---|---|---|---|---|
| MP Point, débito | **3,25% + IVA** | 2,99% + IVA a 2 días | [HECHO] (may-2026) | F1907 |
| MP Point, crédito en un pago | **6,29% + IVA** | 5,39% a 5 días · **4,39% + IVA a 10 días** | [HECHO] (may-2026) | F1907 |
| MP QR, dinero en cuenta | **0,8%** | — | [HECHO] | F1908, F1909 |
| MP QR, débito | 1,33–1,40% | 0,84–0,88% a 2 días | [HECHO] | F1908, F1910 |
| MODO QR | 0,8% con acreditación inmediata | — | [HECHO] | F1908 |
| Getnet | débito 2,29% · crédito 3,79% | acreditación en 72 h | [HECHO] | F1911 |
| Payway | débito 2,39% · crédito 3,89% | acreditación en 5–7 días | [HECHO] | F1911 |
| Transferencia del saldo de MP a un banco | sin costo | — | [HECHO] | F1908 |

⚠ **Fuentes en conflicto:** otra versión de la página de costos de MP que devolvió el buscador indica, para Point, débito 2,99% al instante y 2,75% a 2 días, y crédito 5,99% / 5,19% / 4,19%, "IVA incluido" (F1910). La diferencia está en si el IVA va incluido o se suma. Para el modelo usamos la versión más cara (F1907, "+ IVA") por prudencia. Además se suman retenciones de IIBB y SIRCREB según el padrón provincial (s/d).

**Costo de cobro ponderado** [ESTIMACIÓN; la mezcla de medios es SUPUESTO: 40% QR o transferencia, 30% débito, 20% crédito, 10% efectivo]

| Escenario | Cálculo | Comisión sin IVA | Con IVA 21% |
|---|---|---|---|
| Todo al instante con MP | 0,4×0,8 + 0,3×3,25 + 0,2×6,29 | 2,55% | **≈ 3,1% de la venta** |
| Plazos optimizados con MP (débito a 2 días, crédito a 10 días) | 0,4×0,8 + 0,3×2,99 + 0,2×4,39 | 2,10% | ≈ 2,5% |
| Posnet tradicional (Getnet) + QR | 0,4×0,8 + 0,3×2,29 + 0,2×3,79 | 1,77% | ≈ 2,1% |

[INTERPRETACIÓN] Empujar el pago por QR (es el más barato, 0,8%) y tener un posnet bancario para tarjetas baja el costo financiero de cobro unos **0,5–1 pp de la venta**. Sobre una facturación de $40 M/mes [SUPUESTO], son $200–400 mil por mes.

### A3. Café en grano y costo por taza

| Presentación | Precio | $/kg | Etiqueta | Fuente |
|---|---|---|---|---|
| Saco de grano tostado de 46 kg | $1.608.160 + IVA | **$34.960 + IVA (≈ $42.300 con IVA)** | [HECHO] / $/kg [ESTIMACIÓN] | F1912 |
| Caja de 6 kg (café de oficina mayorista, 5 Hispanos) | $231.334 | ≈ $38.556 | [HECHO] | F1912 |
| Bolsa de 1 kg en góndola online (Fundador, Luggiani, Montibello, Bonafide Espresso) | $28.600 a $41.000 | $28.600–41.000 | [HECHO] | F1912 |
| Lavazza Crema e Aroma, 1 kg | $53.000 | $53.000 | [HECHO] | F1912 |
| Café molido económico | $21.800–25.000/kg | — | [HECHO] | F1913 |

**Costo por taza** [ESTIMACIÓN; la dosis es SUPUESTO técnico: espresso simple de 7–9 g, doble de 14–18 g; leche de 150 ml por cortado o café con leche]

| Bebida | Café | Leche (a $2.100/l, F1916) | Costo directo | Precio de referencia | Costo / precio |
|---|---|---|---|---|---|
| Espresso simple (grano a $35–42 mil/kg) | $245–380 | — | **$250–380** | $3.200 (Córdoba, F1928) – $3.800 (Havanna, F1929) | **8–12%** |
| Café con leche o cappuccino (doble) | $490–760 | $315 | **$800–1.075** (sin vaso ni azúcar) | $4.500 (Córdoba) – $5.400–6.400 (Havanna) | **15–20%** |

- [HECHO] Consumo per cápita estimado en Argentina: ~208 tazas por año, equivalente a ~1 kg de café (F1913).
- [INTERPRETACIÓN] El café sigue siendo el producto de mayor margen de la carta. Lo que pesa en el costo es la leche (y la vajilla descartable en take away), no el grano.

### A4. Manteca, leche y azúcar

| Insumo | Precio | Fecha | Etiqueta | Fuente |
|---|---|---|---|---|
| Azúcar común tipo A, bolsa de 50 kg | **$30.165** (≈ $603/kg) | 2-sep-2026 | [HECHO] ⚠ El fragmento no deja claro si es precio de ingenio o mayorista, ni si incluye IVA | F1915 |
| Leche entera en sachet de 1 l (góndola online) | Carrefour $2.049 · El Granero $2.130 · SuperMami $2.725 | s/f (consulta 2026-10-02) | [HECHO] minorista | F1916 |
| Leche en sachet de 1 l, mayorista | existe oferta mayorista de La Serenísima (vertientemye.com), monto s/d | — | s/d | F1916 |
| Leche, contexto del sector | Producción +2,2% i.a. en ago-2026 y +4,5% acumulado ene–ago. El precio al productor, en términos reales, quedó en el mínimo de una década para un mes de agosto | sep-2026 | [HECHO] | F1914 |
| Manteca (sin dato nuevo) | ≈ $10.340/kg (Teodoro, caja de 5 kg, lista mayorista) | 1-jun-2026 | [HECHO] (I005) | F927 (I005) |

[ESTIMACIÓN] Para el modelo: leche mayorista ≈ **$1.700–1.900/l** (góndola −15/−20%) [SUPUESTO de descuento mayorista]; manteca ≈ **$11.000–11.500/kg** en oct-2026 (el dato de junio indexado por un IPC de ~1,8% mensual, F901); azúcar ≈ **$650–700/kg** con flete e IVA.

### A5. Tarifas de luz (EPEC) y gas (Ecogas) para un comercio chico

| Servicio | Dato | Etiqueta | Fuente |
|---|---|---|---|
| EPEC, Tarifa N°2 "General y de Servicios" | Comercios, industrias y servicios con potencia autorizada de **hasta 40 kW**: es la tarifa que aplica a PAN-CBA | [HECHO] | F1917 |
| EPEC, Tarifa 2 en ene-2026 | +6,58% y +3,72% contra dic-2025, según la resolución aplicada (seguimiento de AGUEERA) | [HECHO] | F1918 |
| EPEC, quitas de subsidio | Para comercios, el aumento final en factura llegó a **101%** (nota histórica, fecha s/d) | [HECHO, fecha dudosa] | F1917 |
| EPEC, $/kWh de Tarifa 2 | El fragmento devolvió "$75,96 pico / $73,48 valle / $8,99 resto" para 300–750 kWh. Son valores **inconsistentes** (el resto no puede ser 8 veces más barato que el valle). **No usar** | s/d | F1917 |
| Ecogas Centro, Servicio General P (comercios) | **Cargo fijo $94.723,95/mes**. Cargo variable **$341,25/m³** (0–1.000 m³), $336,44 (1.001–9.000 m³) y $331,04 (más de 9.000 m³). Vigente desde 1-ago-2026 | [HECHO] ⚠ Falta verificar en el PDF a qué subcategoría SGP corresponde y si el $/m³ incluye el precio del gas | F1919 |
| Ecogas, ajustes 2026 (ya en I005) | ene +2,5% · abr +0,6% · sep +1,4% (nacional) | [HECHO] | F923–F924 (I005) |

**Factura mensual tipo** [ESTIMACIÓN; los consumos son SUPUESTO técnico]
- Gas, con horno rotativo + cocina: 500–800 m³/mes → $94.724 + (500–800 × $341,25) = **$265.000–368.000** antes de impuestos. Con impuestos y tasas (+25–30%, SUPUESTO): **≈ $330.000–480.000 por mes**.
- Luz: con consumos de 2.500–4.000 kWh/mes (cámaras, heladeras, máquina de café, iluminación), el $/kWh queda **s/d**. Hasta tener el cuadro ERSeP verificado, recomendamos tomar **$180–220/kWh todo incluido** [SUPUESTO], es decir **$450.000–880.000 por mes**. ⚠ Prioridad para la próxima pasada: leer el PDF de EPEC de sep/oct-2026 (F923 de I005).

---

## B. Tamaño de mercado: ENGHo 2017/18

| Indicador | Total país | Región Pampeana | Etiqueta | Fuente |
|---|---|---|---|---|
| Alimentos y bebidas no alcohólicas / gasto de consumo total | **22,7%** | **23,1%** (otra fuente cita 22,8%) | [HECHO] | F1920, F1921, F1922 |
| Pan / gasto en alimentos | **6,1%** (era 10,7% en 1996/97) | **6,0%** | [HECHO] | F1922 |
| Cereales / gasto en alimentos | — | 0,9% | [HECHO] | F1922 |
| Legumbres, cereales, papa, pan y pastas / gasto en alimentos | 12,9% (era 19,4% en 1996/97) | — | [HECHO] | F1922 |
| Restaurantes y comidas fuera del hogar / gasto de consumo total | **6,2%** | "Restaurantes y hoteles": 6,3% | [HECHO] | F1920, F1923 |
| Comidas fuera del hogar | se incorporan como rubro propio en 2017/18 (la ENGHo 1996/97 no las relevaba) | — | [HECHO] | F1922 |
| Gasto de consumo mensual por hogar, en pesos de 2017/18 | **s/d** (está en el informe de INDEC, F1920, no se extrajo) | s/d | — | F1920 |

**Cómo se aplica (para reemplazar el TAM de I005 §4)** [ESTIMACIÓN; la población y el gasto por hogar son SUPUESTOS]

Fórmulas:
- Gasto anual en pan = Hogares × Gasto de consumo mensual por hogar × 23,1% × 6,0% × 12
- Gasto anual fuera del hogar = Hogares × Gasto de consumo mensual por hogar × 6,2% × 12

| Parámetro | Valor | Etiqueta |
|---|---|---|
| Hogares en Córdoba Capital | 540.000 | [SUPUESTO] (≈ 1,5 M hab. / 2,8 personas por hogar; validar con el Censo 2022) |
| Gasto de consumo por hogar, oct-2026 | $1.500.000/mes | [SUPUESTO] (validar llevando el valor de la ENGHo con el IPC Córdoba) |
| **Gasto en pan, Córdoba Capital** | 540.000 × 1,5 M × 0,231 × 0,060 × 12 ≈ **$135.000 M/año (≈ USD 87 M)** | [ESTIMACIÓN] |
| **Gasto en comidas fuera del hogar** | 540.000 × 1,5 M × 0,062 × 12 ≈ **$603.000 M/año (≈ USD 388 M)** | [ESTIMACIÓN] |

[INTERPRETACIÓN] Las participaciones de la ENGHo 2017/18 sobreestiman el pan en 2026: el sector declara caídas de 55–65% en volumen (F926 de I005, F1932). Conviene aplicar un **ajuste de −20 a −30%** al rubro pan [SUPUESTO] y, en cambio, dejar las comidas fuera del hogar cerca de su participación, porque el café y el delivery de café crecen (F1939).

---

## C. Cliente

### C1. Ocupados en el Gran Córdoba (EPH, II trimestre 2026)

| Indicador | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Ocupados | **736.000** (747.000 en II-T 2025: −11.000) | [HECHO] | F1924 |
| Desocupación | **10,5%**, 87.000 personas (segunda tasa más alta del país) | [HECHO] | F1925, F1926 |
| Asalariados / ocupados | **71,8%** (≈ 528.000) | [HECHO] / cantidad [ESTIMACIÓN] | F1926 |
| Ocupados que buscan otro empleo | 22,8% | [HECHO] | F1926 |
| Desocupación por rama de la última ocupación | comercio y construcción aportan 1 pp cada uno; industria y servicio doméstico, 0,8 pp cada uno | [HECHO] | F1924 |
| Mínimo previo | 8,8% en I-T 2026 | [HECHO] | F1927 |

**Ocupados por rama en el Gran Córdoba.** ⚠ Los fragmentos se contradicen y la confianza es baja:

| Rama | Versión A (EPH 2025, F1940) | Versión B (EPH II-T 2026, F1941) | Ocupados con la versión A × 736 mil [ESTIMACIÓN] |
|---|---|---|---|
| Comercio | 19,5% | 8,7% | ≈ 143.500 |
| Servicios financieros, inmobiliarios y empresariales (≈ oficinas) | 11,0% | s/d | ≈ 81.000 |
| Enseñanza | 8,1% | 3,4% | ≈ 59.600 |
| Transporte | 8,2% | s/d | ≈ 60.400 |
| Construcción | 8,7% | s/d | ≈ 64.000 |
| Administración pública | 6,9% | s/d | ≈ 50.800 |
| Hoteles y restaurantes | 5,7% | s/d | ≈ 42.000 |
| Servicios sociales y de salud | s/d | 2,9% | ≈ 50.000 [SUPUESTO: 6,8%, estructura típica urbana] |

[INTERPRETACIÓN] La versión A es coherente con la estructura de un aglomerado urbano (comercio cerca del 20%). La versión B probablemente mide otra cosa, por ejemplo un porcentaje de la población total o una contribución a una tasa, y **no debe usarse** como participación en el empleo. Con la versión A: **oficinas y servicios a empresas + administración pública ≈ 130 mil**, comercio ≈ 145 mil, educación ≈ 60 mil y salud ≈ 50 mil [ESTIMACIÓN]. Esos son los segmentos "desayuno al paso" y "turno" de I006. Hay que verificarlo con los microdatos de la EPH (aglomerado 13), tomando la variable PP04B_COD.

### C2. Ticket de delivery en Córdoba

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Lo que cobra el repartidor de PedidosYa por pedido | $3.659 (feb-2026) → **$3.924** (mar-2026) | [HECHO]. **No es el ticket del cliente** | F1936 |
| Ingreso medio por entrega, todas las apps (Fundación Encuentro) | $3.165,2 (mar-2026); referencia sin propinas $3.032,9 | [HECHO], ingreso del repartidor | F1937, F1938 |
| PedidosYa en Córdoba | Córdoba es una de las ciudades con más volumen; más de 15% de suba de pedidos en más de 20 localidades de la provincia | [HECHO] | F1939 |
| Delivery de café en PedidosYa | **+33% i.a. en 2026** | [HECHO] (título de la nota) | F1939 |
| **Ticket promedio del cliente en Córdoba** | **s/d** | — | — |

[ESTIMACIÓN] Como proxy para el modelo: ticket de delivery de desayuno o merienda para 2 personas = 2 bebidas + 4–6 piezas ≈ **$14.000–20.000**, con la carta de C4 y un recargo de app de 15–25% [SUPUESTO, ver I005 §2.4].

### C3. "Domingo de facturas" y picos de compra

| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Producción de facturas antes de la crisis | 20–30 docenas por día de lunes a viernes contra **100 docenas** el fin de semana | [HECHO, testimonio del sector] | F1932 |
| Otro panadero (2026) | 5 docenas por día de semana contra **15–20 docenas** el fin de semana | [HECHO, testimonio] | F1934 |
| Caída de ventas contra 2023 | pan −55%, **facturas y tortas −85%**; "vender una docena es una excepción" | [HECHO, dato gremial, mar-2026] | F1932, F1933 |
| Nueva Córdoba | facturas o medialunas frescas a $750 c/u; al día siguiente, bolsas de 4–6 unidades a mitad de precio | [HECHO] abr-2025 | F1935 |
| Frecuencia (Puratos, más de 400 casos) | **77%** consume facturas o pastelería al menos una vez por semana | [HECHO] | F1934 |
| Horarios de fin de semana | panaderías que abren sáb y dom de 8 a 21:30, otras solo el domingo de 8 a 13 | [HECHO, ejemplos] | F1934 |

[INTERPRETACIÓN] El fin de semana multiplica por **3 a 5** la venta de facturas de un día hábil, y el domingo a la mañana (8–13 h) concentra el pico. Para el modelo proponemos: domingo = 2,5× un día hábil en facturas y 1,3× en pan; pico diario de 7:30–9:30 (de paso, al trabajo) y de 17–19:30 (merienda) [SUPUESTO, validar con conteo en M1]. Además, el formato "bolsa del día anterior" se volvió una práctica estándar en Córdoba y conviene incluirla en el plan de mermas.

### C4. Ticket en cafeterías de Córdoba (2026)

| Ítem | Precio | Etiqueta | Fuente |
|---|---|---|---|
| Ristretto, espresso o cortado (cafetería de especialidad premiada, Córdoba) | $3.200 | [HECHO] (nota s/f, consultada 2026-10-02) | F1928 |
| Cappuccino (misma cafetería) | $4.500 | [HECHO] | F1928 |
| Medialuna de manteca (misma cafetería) | $2.500 | [HECHO] | F1928 |
| Combo "Clásico Medialunas" (infusión + 2 medialunas) | **$7.500** | [HECHO] | F1928 |
| Havanna (cadena nacional), sep-2026 | espresso de pocillo $3.800 · jarrito $4.300 · taza o 9 oz $5.400 · café con leche o latte $5.400–6.200 · cappuccino $5.500–6.400 | [HECHO] | F1929 |
| YPF Full, café mediano o jarrito | $5.200 | [HECHO] | F1929 |
| Ticket de cafetería de especialidad (Argentina, genérico) | $8.000–15.000 | [HECHO, sin desagregar por ciudad] | F1930 |

[ESTIMACIÓN] **Ticket por persona en PAN-CBA:** desayuno o merienda simple (combo) **$7.500–9.000**; con tostado o pastelería premium **$10.000–13.000**; ponderado **≈ $9.000–10.000**. Esto reemplaza el SUPUESTO de $7.000 de I005 §4.1. Con ese cambio, el SAM de cafetería sube un 30–40%.

---

## Pendientes que siguen abiertos

1. **Montos de la escala de la Sociedad Obreros Panaderos de Córdoba Capital** (F1904). Hay que bajar el PDF.
2. **$/kWh de EPEC Tarifa 2** y verificación de la subcategoría SGP de Ecogas (F1919), en el PDF.
3. Gasto de consumo por hogar de la ENGHo, en pesos, para la Pampeana y Córdoba (cuadros de F1920).
4. Ticket de delivery del cliente (no del repartidor). Buscar informes de PedidosYa o Rappi "Radiografía del delivery".
5. Distribución por rama en el Gran Córdoba con los microdatos de la EPH (aglomerado 13).
6. Precio mayorista de leche (sachet) y de manteca en Córdoba, oct-2026 (cotizar con distribuidores como en M1).
7. Siguen de I005: alquileres por zona y habilitaciones. Sigue de I006: reseñas de clientes.

---

## Fuentes (F1900–F1999)

Fecha de consulta de todas: 2026-10-02. Entre paréntesis, la fecha del dato cuando se conoce.

- F1900 — Calcular Sueldo, UTHGRA: aumento para gastronómicos hasta septiembre 2026 (jul-2026): https://calcularsueldo.com.ar/paritarias/15542/uthgra-aumento-para-gastronomicos-hasta-septiembre-2026.html
- F1901 — Yo-Facturo, escala salarial gastronómicos UTHGRA 2026 (categorías y montos): https://yo-facturo.com/blog/escala-salarial-gastronomicos-uthgra-2026/
- F1902 — Estudio Vilaplana, escala salarial gastronómicos 2026-2027 + acuerdo UTHGRA–FEHGRA: https://estudiovilaplana.com.ar/sueldos-gastronomicos/
- F1903 — IGI-LA, ¿cuánto gana un barista en Argentina? (2026; cafetero N3, cajero N5, encargado N6): https://www.igi-la.com/blog/cuanto-gana-barista-argentina/ ; ver también https://hruseful.com/convenios-colectivos-de-trabajo/cct-389-04-gastronomicos-y-hoteleros-uthgra/
- F1904 — Sociedad Obreros Panaderos de Córdoba, escalas salariales (Capital, Interior A/B, Río Cuarto 2026): https://socobpancba.ar/sistema/escalas_salariales/
- F1905 — Boletín Oficial / Argentina.gob.ar, Disposición 1946/2025 (homologación del acuerdo entre la Sociedad Obreros Panaderos de Córdoba Capital y el Centro Industriales Panaderos y Afines): https://www.argentina.gob.ar/normativa/nacional/norma-419440
- F1906 — SOPSTE, escalas salariales CCT 231/94 2026 (Oficial Maestro ago/sep-2026): https://sopste.org.ar/legales/escalas-salariales-cct-231-94-2026/
- F1907 — Guía de Bancos, comisiones de Mercado Pago 2026 por país (Argentina, may-2026): https://www.guiadebancos.com/ar/blog/comisiones-mercado-pago-latam-2026
- F1908 — Jonatan Almeira, cómo cobrar con QR en Argentina 2026 y comisiones de Mercado Pago: https://www.jonatanalmeira.com/como-cobrar-con-qr-argentina/ ; https://www.jonatanalmeira.com/comisiones-de-mercado-pago-en-argentina-cuanto-cobra-realmente/
- F1909 — Yo-Facturo, comisiones del QR de Mercado Pago (2026): https://yo-facturo.com/blog/qr-mercado-pago-comisiones-cobrar/
- F1910 — Mercado Pago Argentina, lectores Point y cobro con QR (páginas oficiales): https://www.mercadopago.com.ar/herramientas-para-vender/lectores-point ; https://www.mercadopago.com.ar/herramientas-para-vender/cobrar-con-qr
- F1911 — Compara Pasarelas, comisiones de Getnet y Payway 2026: https://www.comparapasarelas.com/getnet-comisiones ; https://www.comparapasarelas.com/
- F1912 — Mercado Libre, listados de café en grano por mayor y café tostado (precios 2026): https://listado.mercadolibre.com.ar/cafe-en-grano-por-mayor ; https://listado.mercadolibre.com.ar/cafe-tostado
- F1913 — iProfesional, Día Internacional del Café: precios y tazas por año (2026; el título de la página no coincide con la URL, ⚠): https://www.iprofesional.com/politica/465530-milei-inversiones-francia-beneficios-millonarios-aprovechar-rigi-argentina
- F1914 — InfoAlimentación, la producción de leche creció 2,2% en agosto de 2026 (OCLA): https://infoalimentacion.com.ar/2026/09/16/produccion-leche-agosto-2026-industria-precio-tambo/
- F1915 — IPAAT, valores de mercado (azúcar común tipo A, bolsa de 50 kg, 2-sep-2026; atribución ⚠): https://www.ipaat.gov.ar/valores-de-mercado
- F1916 — Carrefour / SuperMami / El Granero / Vertiente, leche La Serenísima en sachet de 1 l: https://www.carrefour.com.ar/la-serenisima ; https://www.supermami.com.ar/super/producto/leche-la-serenisima-fresca-entera-clasica-3-grasa-sachet-x-1-lt/_/A-3262766-3262766-s ; https://www.elgranerodigital.com.ar/productos/leche-clasica-3-x-1-l-la-serenisima-sachet/ ; https://vertientemye.com/producto/leche-sachet-la-serenisima-1l/
- F1917 — EPEC, Tarifa N°2 General y de Servicios / Electroinstalador, "sin subsidios, la luz de EPEC llega con 100% de aumento a comercios": https://web.epec.com.ar/docs/cuadro-tarifario/tarifa_n2RG53_16.pdf ; https://www.electroinstalador.com/epec/sin-subsidios-la-luz-epec-llega-100-aumento-comercios-n4550
- F1918 — AGUEERA, seguimiento tarifario enero 2026: https://www.agueera.com.ar/wp-content/uploads/2026/02/01-Seguimiento-tarifario-ene-26.pdf
- F1919 — Ecogas, cuadro tarifario Distribuidora Centro (vigente desde 1-ago-2026): https://ecogas.com.ar/assets/hogares-comercios/Tarifas/PDF/Cuadros-tarifarios/centro-ecogas.pdf
- F1920 — INDEC, ENGHo 2017-2018, informe de gastos: https://www.indec.gob.ar/ftp/cuadros/sociedad/engho_2017_2018_informe_gastos.pdf
- F1921 — Ámbito, INDEC: las familias destinan el 22,8% a alimentos (2019): https://www.ambito.com/indec-las-familias-destinan-el-228-sus-ingresos-alimentos-y-145-servicios-publicos-n5051330
- F1922 — Memoria Académica FaHCE-UNLP, "Continuidades y cambios en los gastos destinados a…" (ENGHo 1996/97 a 2017/18): https://www.memoria.fahce.unlp.edu.ar/trab_eventos/ev.15528/ev.15528.pdf
- F1923 — INDEC, ENGHo 2017-2018, resultados preliminares (región Pampeana): https://www.indec.gob.ar/ftp/cuadros/sociedad/engho_2017_2018_resultados_preliminares.pdf
- F1924 — Perfil Córdoba, Córdoba sumó 14 mil desocupados y el desempleo escaló al 10,5% (sep-2026): https://www.perfil.com/noticias/cordoba/cordoba-sumo-14-mil-desocupados-en-un-ano-y-la-tasa-de-desempleo-escalo-al-105-segun-el-indec.phtml
- F1925 — El Doce, la desocupación subió al 10,5% en Gran Córdoba (2026-09-17): https://eldoce.tv/politica/2026/09/17/la-desocupacion-subio-al-105-en-gran-cordoba-y-alcanzo-a-87-mil-personas-en-el-segundo-trimestre-de-2026/
- F1926 — En Redacción, Córdoba: la desocupación trepó al 10,5% y el 22,8% de los ocupados busca otro trabajo / INDEC EPH II-T 2026: https://enredaccion.com.ar/cordoba-la-desocupacion-trepo-al-105-y-el-228-de-los-ocupados-busca-otro-trabajo/ ; https://www.indec.gob.ar/uploads/informesdeprensa/mercado_trabajo_eph_2trim26433FCBC5A8.pdf
- F1927 — Perfil Córdoba, 8,8% de desocupación en el I-T 2026: https://www.perfil.com/noticias/cordoba/el-gran-cordoba-supera-la-media-nacional-88-de-desocupacion-en-el-primer-trimestre-de-2026.phtml
- F1928 — Vía País, una de las mejores cafeterías del mundo está en Córdoba: cuánto sale una merienda: https://viapais.com.ar/cordoba/una-de-las-mejores-cafeterias-del-mundo-esta-en-cordoba-cuanto-sale-una-merienda/
- F1929 — iProfesional, precios de café en Havanna e YPF Full (sep-2026), misma nota que F1913: https://www.iprofesional.com/politica/465530-milei-inversiones-francia-beneficios-millonarios-aprovechar-rigi-argentina
- F1930 — Restaurant Argentina, guía para abrir un restaurante en Argentina 2026 (ticket de cafetería de especialidad): https://restaurantargentina.com/como-abrir-restaurante/
- F1931 — (reservada)
- F1932 — BAE Negocios, panaderías en crisis: el pan cayó 55% y las facturas y tortas 85% (mar-2026): https://www.baenegocios.com/negocios/panaderias-en-crisis-la-venta-de-pan-cayo-55-y-la-de-facturas-y-tortas-bajo-85/ ; https://www.enbocadetodoshd.com.ar/nacionales/2026/3/26/panaderias-en-crisis-la-venta-de-pan-cayo-55-la-de-facturas-tortas-bajo-85-110754.html
- F1933 — Perfil, cerraron 14 mil panaderías y la venta de facturas cayó 85%: https://www.perfil.com/noticias/economia/en-los-ultimos-20-meses-cerraron-14-mil-panaderias-y-la-venta-de-facturas-cayo-un-85.phtml
- F1934 — Testimonios y horarios de fin de semana / Puratos (77% consume facturas semanalmente), según fragmentos del buscador: https://lahelveticaonline.com.ar/panaderia/carro-de-facturas/ ; https://lahelveticaonline.com.ar/panaderia/azahares-panes-dulces/ (⚠ atribución de cada cifra a confirmar)
- F1935 — El Doce, facturas y criollos del día anterior en Córdoba (2025-04-04): https://eldoce.tv/actualidad/2025/04/04/una-opcion-en-la-crisis-cuanto-salen-las-facturas-y-criollos-del-dia-anterior-en-cordoba/
- F1936 — iProfesional, cuánto deja cada entrega de PedidosYa (2026): https://www.iprofesional.com/management/462798-cuanto-gana-un-repartidor-de-pedidosya-en-argentina-y-de-que-depende-su-ingreso
- F1937 — Los Andes, cuánto se gana haciendo delivery en marzo 2026: https://www.losandes.com.ar/economia/cuanto-se-gana-haciendo-delivery-marzo-2026-rappi-vs-pedidos-ya-cuanto-deja-dia-n5981701
- F1938 — Infobae, cuántos pedidos debe hacer un repartidor para cubrir la canasta (2026-07-29): https://www.infobae.com/economia/2026/07/29/cuantos-pedidos-debe-hacer-un-repartidor-de-delivery-para-cubrir-la-canasta-basica-y-no-ser-pobre/
- F1939 — Revista Mercado, PedidosYa: el café por delivery subió 33% / Perfil Córdoba, PedidosYa en más de 20 localidades: https://mercado.com.ar/tendencias/pedidosya-el-consumo-de-cafe-por-delivery-subio-33-interanual-en-2026 ; https://www.perfil.com/noticias/cordoba/pedidosya-consolida-su-crecimiento-en-cordoba-con-mas-de-20-localidades-activas.phtml
- F1940 — INDEC, Mercado de trabajo EPH II-T 2025 (fragmento con la distribución por rama atribuida al Gran Córdoba, ⚠): https://www.indec.gob.ar/uploads/informesdeprensa/mercado_trabajo_eph_2trim25C42A813B2A.pdf
- F1941 — INDEC, Mercado de trabajo EPH II-T 2026 (fragmento con comercio 8,7%, enseñanza 3,4% y salud 2,9%, ⚠): https://www.indec.gob.ar/uploads/informesdeprensa/mercado_trabajo_eph_2trim26433FCBC5A8.pdf
