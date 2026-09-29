# R4 — Competidores indirectos (desayuno/merienda/pan) · Córdoba Capital
Consulta: 2026-09-28 · Método: solo WebSearch (27 búsquedas) · Datos: `r4_indirectos.json` (62 registros).

## Conteos
| Tipo | Registros con dirección | Universo según fuentes |
|---|---|---|
| fast_food | 19 (Mostaza 8, McDonald's 11) | Mostaza: 11 locales en la **provincia** (feb-2026, F1404); sucursales24 lista 5 en Capital (F1400); se identificaron 8 en Capital. McDonald's: 19 en Capital (F1405) → 11 con dirección |
| conveniencia | 9 (YPF Full 3, Shell 3, Axion 2, Puma 1) | Universo total s/d (el mapa oficial mapa.ypf.com y find.shell.com no se pueden leer con este método) |
| supermercado | 34 | Carrefour: 4 hiper + 19 Express + 1 Market + 1 Maxi (F1424); Disco 12 (F1426); Hiper Libertad/La Anónima 4 (F1427); Cordiez 9 (F1429); Vea 4 (F1431); Walmart/Changomás 4 (F1432); Super MaMi ≥5; Makro 1; Maxiconsumo 1 |

Por zona (62): Z01 9 · Z05 9 · Z04 8 · Z07 7 · Z08 7 · Z09 7 · Z10 7 · Z02 4 · Z06 4 · Z03 0.
Sin registros en Z03 (Güemes/Observatorio): no apareció ningún indirecto verificado ahí (hueco de datos, no necesariamente de oferta).

## Precios (café + medialunas)
- YPF Full, CABA, ago-2026: combo café + 2 medialunas ≈ **$7.700** (citado en nota de iProfesional sobre el split de acciones, F1437). Es referencia de CABA, no de Córdoba.
- Menú online YPF Full (sin fecha/ubicación clara): café mediano/jarrito **$5.200** (F1438).
- Post de Bella Vista YPF (San Luis): 2 cafés + 2 medialunas $300 / 2 café con leche + 2 medialunas $350 → **precios viejos (pre-inflación), no usar** (F1436).
- Shell Select, Axion Spot, Puma, Mostaza y McCafé: sin precio de desayuno verificado en Córdoba.

## Observaciones
- **Horarios de desayuno de fast food**: McDonald's Sabattini abre 7:00; Rafael Núñez y Gral. Paz 8:00; Ruta 20 figura con horario continuo sáb-dom. Las fichas oficiales de McDonald's (Plaza España, 25 de Mayo 52, Ruta 20, Sabattini, Gral. Paz) mencionan McCafé, desayuno y, en algunos casos, 24 h, pero no se pudo confirmar qué local es 24 h → `abre_24h: null`.
- **Mostaza Nueva Córdoba** (Yrigoyen 564, frente a Plaza España) abre 6:00 con menú de desayuno/merienda y espresso; anunció "Open 24" jue-sáb (F1403). Es el indirecto de fast food más directo para la franja temprana en Z02. Plan 2026 de la marca: ~30 aperturas nacionales; foco en Córdoba.
- **YPF Full**: 3 tiendas 24 h confirmadas (La Voz del Interior 6350, Las Malvinas 2595, Duarte Quirós 3607). Surtidores informa que en 2026 llega una nueva marca a las tiendas Full (F1439): posible cambio de la oferta de cafetería.
- **Supermercados con panadería propia verificada**: Hiper Libertad/La Anónima (panadería artesanal), Super MaMi (panadería "casera" extensa) y Disco (panadería listada como servicio, varía por sucursal). En Cordiez la mención es genérica. En Carrefour, Vea, Changomás y los mayoristas no se verificó → `panaderia_propia: null`. Carrefour Express → false (formato de proximidad; supuesto razonable, verificar).
- **Hiper Libertad → La Anónima**: las 4 bocas de Capital (Rodríguez del Busto, Gral. Paz, Paseo Rivera, Sabattini) pasan a la bandera La Anónima en 2026 (F1428).
- Axion: además hay estaciones sobre Av. Colón y Av. Juan B. Justo (altura s/d, no cargadas). Puma: estación en Recta Martinolli (altura s/d, no cargada). YPF en Av. Capdevila (no se confirmó Full).
- Zonas marcadas como "estimada" en `nota` cuando el barrio no vino en la fuente.

## Fuentes
- F1400: https://www.sucursales24.com.ar/cordoba-capital/mostaza/
- F1401: https://www.sucursales24.com.ar/cordoba-capital/mostaza/9-de-julio-28-4/
- F1402: https://www.sucursales24.com.ar/cordoba-capital/mostaza/rincn-1100-1/
- F1403: https://infonegocios.info/plus/mostaza-copa-el-corazon-de-nueva-cordoba-con-un-local-de-350-m2-frente-a-plaza-espana-y-compite-con-mcdonald-s-con-su-open-24
- F1404: https://infonegocios.info/y-ademas/con-2-nuevos-locales-en-cordoba-van-11-en-la-provincia-mostaza-ya-supera-las-216-sucursales-en-argentina
- F1405: https://www.sucursales24.com.ar/cordoba-capital/mcdonalds/
- F1406: https://www.mcdonalds.com.ar/restaurantes/cordoba
- F1407: https://m.yelp.com/biz/mcdonalds-c%C3%B3rdoba-3
- F1408: https://m.yelp.com/biz/mcdonalds-c%C3%B3rdoba-9
- F1409: https://mapdoor.com/ar/cb/c%C3%B3rdoba/mcdonalds/av-nu%C3%B1ez-cerro
- F1410: https://www.mcdonalds.com.ar/restaurantes/cordoba/plaza-espana-cordoba-pec
- F1411: https://www.mcdonalds.com.ar/restaurantes/cordoba/25-de-mayo-52-cordoba-p9c
- F1412: https://www.mcdonalds.com.ar/restaurantes/cordoba/ruta-20-rvc
- F1413: https://www.mcdonalds.com.ar/restaurantes/cordoba/av-sabattini-cordoba-lsc
- F1414: https://www.mcdonalds.com.ar/restaurantes/cordoba/general-paz-cordoba-gpc
- F1415: https://www.sucursales24.com.ar/cordoba-capital/mcdonalds/nuevo-centro-shopping-10/
- F1416: https://jpcoil.com.ar/
- F1417: https://ypfelcruce.com.ar/ypf/ypf-326/
- F1418: https://ypfelcruce.com/ypf/ypf-estacion-de-servicio-3/
- F1419: https://www.argentino.com.ar/cordoba-capital/estaciones+de+servicio+shell
- F1420: https://find.shell.com/ar/fuel/locations/cordoba/en_US
- F1421: https://www.waze.com/es-419/live-map/directions/axion-energy-av.-bulnes-1108-cordoba?to=place.w.193856974.1938766348.273266
- F1422: https://www.waze.com/live-map/directions/ar/cordoba/cordoba/axion-energy?to=place.ChIJ1aJ7WEyiMpQRoSe06fxaXNc
- F1423: https://www.elestacionero.com/general/nueva-tienda-super-7-en-la-estacion-de-servicio-puma-energy-servisud-s-a-en-cordoba-capital/2023/08/01/
- F1424: https://www.sucursales24.com.ar/cordoba-capital/supermercados/
- F1425: https://www.sucursales24.com.ar/cordoba-capital/carrefour-express/
- F1426: https://www.sucursales24.com.ar/cordoba-capital/supermercado-disco/
- F1427: https://www.sucursales24.com.ar/cordoba-capital/hiper-libertad/
- F1428: https://viapais.com.ar/cordoba/hiper-libertad-cordoba-letra-chica-acuerdo-anonima-pondria-vilo-100-trabajadores_0_NwfoG9bUPv.html
- F1429: https://www.sucursales24.com.ar/cordoba-capital/cordiez/
- F1430: https://www.tiendeo.com.ar/Tiendas/cordoba/super-mami
- F1431: https://www.sucursales24.com.ar/cordoba-capital/vea/
- F1432: https://www.sucursales24.com.ar/cordoba-capital/walmart/
- F1433: https://www.tiendeo.com.ar/Tiendas/cordoba/changomas
- F1434: https://www.sucursales24.com.ar/cordoba-capital/makro/
- F1435: https://directoriomayorista.com/cordoba/maxiconsumo-cordoba-mayorista/
- F1436: https://www.facebook.com/bellavistaypf/videos/combos-para-compartir-bella-vista-ypf-sl-ar/483557712909359/
- F1437: https://www.iprofesional.com/finanzas/461449-las-acciones-de-ypf-ahora-son-mas-baratas-y-se-podran-comprar-al-precio-de-un-cafe
- F1438: https://surtidoreslatam.com/cuanto-cuesta-cafe-estacion-servicio-surtidores-latam-comparativa/
- F1439: https://surtidores.com.ar/grandes-cambios-en-las-ypf-full-una-nueva-marca-llega-a-partir-de-2026/
- F1440: https://www.sucursales24.com.ar/cordoba-capital/vea/av-24-de-septiembre-1330-3/
- F1441: https://www.sucursales24.com.ar/cordoba-capital/walmart/av-fuerza-aerea-argentina-4372-2/
- F1442: https://infonegocios.info/y-ademas/mostaza-tiene-planes-de-seguir-consolidando-su-presencia-en-cordoba-ya-tiene-9-locales-y-genero-mas-de-240-empleos
- F1443: https://www.pumaenergyarg.com.ar/encontra_tu_estacion
