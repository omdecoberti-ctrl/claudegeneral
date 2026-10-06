# Calculadora de punto de equilibrio y precios

| Campo | Valor |
|---|---|
| Código | E-11 · Herramienta del modelo financiero (G6–G7) |
| Fecha | 06/10/2026 |
| Estado | **v1.** Costos = lista de precios de Ultracongelados Canalsenses sin IVA (54 productos, enviada por Oscar el 06/10). PVP, mix y costos operativos = **supuestos de partida editables** |
| Abrir | **[🧮 Abrir la calculadora](/archivos/07_MODELO_FINANCIERO/CALCULADORA_PUNTO_EQUILIBRIO.html)** |

## Qué permite hacer
- **Cambiar todo:**
  - ventas (tickets por día × ticket, o un total mensual);
  - mix por línea (panificados / café / otros);
  - mix por producto;
  - PVP, merma, IVA, unidades por bulto y precio de lista de cada producto;
  - descuento sobre lista y flete;
  - impuestos y costos variables;
  - delivery;
  - costos fijos;
  - inversión y amortización.
- **Ver al instante:**
  - estado de resultados del mes;
  - margen de contribución;
  - **punto de equilibrio** en $ por mes, $ por día y **tickets por día**;
  - margen de seguridad;
  - gráfico de equilibrio;
  - contribución por producto.
- **Precio de equilibrio** (pestaña 6):
  - factor de precios que deja el resultado en cero con el volumen cargado;
  - PVP de equilibrio y PVP mínimo por producto;
  - PVP con markup objetivo.
- **Logística:** unidades y **bultos a pedir por mes y por quincena** de cada producto (sirve para dimensionar el freezer, R022).
- **Guardar escenarios** con nombre (en el navegador), **exportarlos e importarlos** en JSON para compartir, y bajar la tabla de productos a CSV.

## Escenario de partida [ESTIMACIÓN, 06/10/2026]

| Variable | Valor de partida | Fuente |
|---|---|---|
| Ventas | 220 tickets/día × $8.500 × 30 días = **$56,1 M con IVA** (≈ USD 36 mil) | I005b, I029 |
| Mix por línea | Panificados 60% · café y bebidas 30% · otros 10% | Supuesto |
| Costo de panificados | Lista UC + 5% de flete + merma del 2–8% según producto | Lista UC, supuesto |
| Costos variables | IIBB 4,5% · tasa municipal 1% · medios de pago 2,5% · débitos y créditos 1,2% · packaging 2% · apps (10% de la venta × 30%) | I005b, E-10, supuestos |
| Costos fijos | $17,0 M/mes (alquiler ≈ USD 1.300, 7 personas, energía, Director Técnico, etc.) + amortización de USD 100 mil en 60 meses | I011, I029, D003 |

**Resultado del escenario de partida:**
- margen de contribución del **55%** de la venta sin IVA;
- **equilibrio en ≈ $41 M por mes con IVA (≈ USD 26,6 mil), unos 162 tickets por día**;
- resultado de ≈ $7,1 M por mes;
- margen de seguridad del 27%.

Es un punto de partida para discutir, no una proyección.

## Puntos a confirmar
- **IVA de venta:**
  - 10,5% para pan y facturas de harina de trigo sin envasar;
  - 21% para pastelería envasada, chipá y congelados especiales.
  - **Confirmar con Fabiola.**
- **Ingresos Brutos y tasa municipal:** alícuotas reales para el rubro.
- **Flete Canals → Córdoba** por bulto (Q079, T024).
- **PVP reales:** surgen del test de precios (E004) y de los precios en mostrador del trabajo de campo.
- **Mix real:** se mide con las ventas de los primeros meses. Antes, con el trabajo de campo y los datos de clientes de UC que hornean en su local.

## Relación con otros documentos
I011 (modelo productivo: la regla del ~40% del precio de venta se ve acá en la columna "Markup") · A001 (ticket) · A010 (equilibrio en ≤ 12 meses) · A022 (precio de transferencia) · PD013 (precios) · PD014 (GO económico) · E-10 (delivery).

## Escenario de ejemplo: compras reales de un cliente de UC (agosto 2026) con medialunas de 50 g

En la calculadora aparece como **⭐ Ejemplo: compras de un cliente UC (ago-2026) con medialunas de 50 g** en el selector de escenarios. Usa el modo nuevo **"Bultos comprados por mes"**: la venta sale de los bultos (unidades vendidas = bultos × unidades por bulto × (1 − merma)).

| Supuesto | Detalle |
|---|---|
| Compra mensual | 92 bultos en 16 productos (chipá 14, facturas surtidas c/crema 10, margaritas 10, hojaldre 7, etc.) |
| Medialunas | Las 17 + 5 cajas de 40 g x150 (3.300 medialunas) se pasan a **super medialunas de 50 g x126**, manteniendo la cantidad de medialunas: ≈ 20,2 cajas dulces + 6,0 saladas |
| Medialuna salada de 50 g | **No está en la lista:** se supone igual precio que la 033 |
| Margaritas c/dulce de leche x90 | **No está en la lista:** precio estimado con el costo unitario de las facturas ($327,43) |
| Facturas de hojaldre | El cliente compra la caja x150; la lista tiene x135 (se usó la de la lista) |
| PVP, merma y costos fijos | Los de partida de la calculadora |

**Resultado [ESTIMACIÓN]:**

| | Solo panificados | Con café y otros (mix 60/30/10) |
|---|---|---|
| Ventas con IVA / mes | $14,9 M (≈ USD 9.600) | $24,8 M (≈ USD 16.000) |
| Margen de contribución | 57% | 58% |
| Resultado / mes | **−$12,1 M** | **−$7,1 M** |
| Punto de equilibrio | $38,8 M/mes | $38,9 M/mes |
| Compra necesaria para el equilibrio | **≈ 240 bultos/mes** (2,6 veces) | **≈ 145 bultos/mes** (1,6 veces) |
| Precios necesarios con ese volumen | ×2,08 | ×1,39 |

**Lectura [INTERPRETACIÓN]:**
- El volumen de compra de ese cliente (~3.100 medialunas y ~9.000 unidades por mes, ≈ 300 por día) **no alcanza para cubrir la estructura del local propuesto**: alquiler, 7 personas y amortización.
- Hace falta **1,6 veces ese volumen con café** o **2,6 veces solo con panificados**.
- **El café es el que acerca el equilibrio.**
- Si el local 1 arranca con un volumen parecido, conviene una estructura más chica: menos personal o formato corner (E-09).
