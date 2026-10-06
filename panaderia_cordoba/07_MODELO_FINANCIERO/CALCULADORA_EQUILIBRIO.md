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
