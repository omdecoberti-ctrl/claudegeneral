# R2 — Censo de panaderías de barrio: Z01 Centro, Z06 Norte cercano, Z09 Sur

Consulta: 2026-09-29 (se usaron 32 de 32 búsquedas WebSearch). Archivo de datos: `r2_barrio.json`, con **37 registros**.

## Conteo por zona y barrio
| Zona | Total | Barrios |
|---|---|---|
| Z01 Centro | 6 | Centro 6 (Jobs, en Deán Funes 1031, queda en el límite con Alberdi) |
| Z06 Norte cercano | 13 | Alta Córdoba 5 · General Bustos 2 · barrio s/d 6 (zona inferida por avenida: Capdevila, Castro Barros, Pablo Cabrera, Avellaneda; Alonso ×2 sin verificar) |
| Z09 Sur | 18 | Jardín 6 · Santa Isabel 2 · Las Flores 2 · Villa Revol 1 · Villa El Libertador 1 · Parque Capital 1 · barrio s/d 5 (Belardinelli, Fuerza Aérea, J. J. Díaz, Valparaíso, O'Higgins, Tronador) |

Por tipo: panaderia_barrio 25 · medialuneria_dulces 5 · bakery_cafe 3 · cadena_panaderia 3 (Santa Claus, mini-cadena local con 3 locales) · otro 1 (Dozen St., sin TACC).

Algunos barrios quedan fuera de la tabla del BRIEF y se asignaron a la zona más cercana: Las Flores y Parque Capital van a Z09.

## Deduplicación
- No se repiten los que ya teníamos: Artesanos del Sabor, Frocca, Panadero, Los Dos Chinos, Mocafe, Panadería Lugones. Tampoco van las cadenas excluidas (La Celeste, Del Pilar, Lo+Rico, Independencia, Perdú).
- Se descartaron por estar ya cargados en archivos de otros analistas: Medialunas 707 JB Justo 3475 y Panicafé Barrio Jardín (en r1 como cadenas), y Kerrycopan, Nueva Delhi, Corradini y Le Donne (en r5).
- Se mantienen como complemento de r5, que no tenía dirección o tenía otro local: Bakeria, Celins, Alonso, Lihué (Centro) y Acapulco (Vélez Sarsfield 3184).
- **Para r1:** La Mejor Medialuna del País 707 (Belgrano 181, Centro) es una sucursal de 707 que no figura en r1.

## Fuentes (F1200–F1246)
- F1200–F1202, F1232: panaderiasanfrancisco.com.ar (fichas con barrio y rating propio en escala /10)
- F1203, F1231, F1245: argentino.com.ar
- F1204, F1212, F1225: restaurantguru.com (los ratings son de RG, no de Google, salvo Bakeria, donde RG cita 4.6 de Google)
- F1205–F1246 (resto): ar.near-place.com. Es la fuente principal: el título incluye nombre, dirección y teléfono, y a veces barrio. Los datos vienen de directorios de 2016–2018 y pueden estar desactualizados.
- F1233: panaderiasintacc.aarg.ar
- Cada registro tiene su URL en "fuente" y su ID en "nota".

## Limitaciones
- **No se llegó a la meta de 80 o más.** WebSearch devuelve resúmenes con 1 a 5 locales útiles por consulta y no listas completas. Las páginas índice (argentino.com.ar/…/panaderias, lahelveticaonline por ubicación, paginasamarillas) aparecen como enlace pero no se pueden leer, porque WebFetch está bloqueado. Waze no dio resultados útiles para Córdoba.
- El Centro quedó con poca cobertura (6 registros): la mayoría de los locales del micro y macrocentro son cadenas.
- Faltan por completo Cofico, Providencia, Los Paraísos, Villa Azalais, Poeta Lugones, Yofre Norte, Alto Verde, Iponá, Villa Eucarística, Manantiales, Cerro Chico, Ciudad de mis Sueños y San Carlos.
- Hay 11 registros con barrio null y zona inferida por la altura de la avenida. Están marcados en "nota" y hay que verificarlos, en especial Alonso ×2, La Migliore y Del Boulevard.
- Rubro por verificar: Lucy Cosas Ricas y Pandy & Co.
- En ningún registro hay horario, delivery ni rating de Google verificado; esos campos quedaron en null o vacíos.
- Siguiente paso sugerido: con Google Maps o Places, barrer "panadería" por barrio en los que faltan. Se estiman 5 a 15 panaderías independientes por barrio, así que el universo real de las 3 zonas probablemente supera las 150.

---

# R3: censo de panaderías de barrio (Z04, Z05, Z07, Z08, Z10, Z02/Z03)

Consulta: 2026-09-28/29. Se usaron 32 de 32 búsquedas WebSearch. Hay **21 registros nuevos** en r3_barrio.json, muy por debajo de la meta de más de 100 (ver "Limitaciones").

## Conteo por zona y barrio
| Zona | Registros | Barrios |
|---|---|---|
| Z04 Oeste | 5 | Alberdi 2, Alto Alberdi 2, Don Bosco (inferido) 1 |
| Z05 Este | 7 | General Paz 2, Juniors 2, Talleres Este 1, Yofre I 1, Altamira 1 |
| Z07 Noroeste | 4 | Cerro de las Rosas 3, Urca 1 |
| Z08 Norte premium | 4 | Argüello 2, Villa Rivera Indarte 1, zona norte (s/d) 1 |
| Z10 Periferia | 0 | (lo único que se encontró fue Vucetich 6946, que ya estaba cargado) |
| Z02/Z03 | 1 | Güemes 1 |
| **Total** | **21** | 13 con dirección completa o calle y altura; 8 con dirección parcial o s/d |

## Fuentes (F1300–F1320 = un registro cada una, en el orden del JSON)
F1300 restaurantguru Futura · F1301 panaderiasanfrancisco Mediterránea · F1302 lahelvetica Santa Rosa · F1303 lahelvetica Marvic · F1304 restaurantguru Trezeri · F1305 lahelvetica Panicafé GP · F1306 circuitogastronomico Bäckerhaus · F1307 lahelvetica La Blanca · F1308 panaderiasanfrancisco Perikos · F1309 lahelvetica Balcánica · F1310 lahelvetica Selva · F1311 lahelvetica La Preferida · F1312 lahelvetica Urban Bakery · F1313 lahelvetica Panicafé Cerro · F1314 lahelvetica Augustus · F1315 lahelvetica Independencia URCA · F1316 argentino Delizziosa · F1317 guiacordoba Buen Día · F1318 guiacordoba Marcel · F1319 argentino Córdoba Capital (Domingo Albariños 8443) · F1320 facebook Panadería Güemes.

## Excluidos a propósito
- **Cadenas (≥3 locales):** El Vergel (Av. Emilio Caraffa 2495 Villa Cabrera, Virgen de la Merced 2897, Gral. Paz), La Celeste (Belgrano, Chacabuco, Obispo Oro), Armando medialunas (Güemes, Vélez Sarsfield 816), Andrea Franceschini, Pugliese (suc. Av. Pueyrredón 170), Corradini (Av. Fuerza Aérea 2966, probablemente varios locales).
- **Fuera de las zonas asignadas (para R-Z06/Z09 si sirve):** Panadería Córdoba (Lavalleja 1351/1357, Cofico, Z06), Panadero (Alta Córdoba, Z06), Kerrycopan (J. L. de Cabrera 902, Z06 probable), Panificadora y bar (Mons. Pablo Cabrera 3186, Zumarán, Z06), Nueva Delhi (Av. Armada Argentina 738, Z09), La Pana de Ana (Agua de Oro 3296, X5014, Z09 probable).
- **Localidad dudosa:** el listado de argentino.com.ar "Alto Alberdi (21)" parece mezclar datos de Santa Fe: Ayacucho 2828 figura con teléfono 0342 y aparece Av. Facundo Zuviría 5779, que es una avenida de Santa Fe. Por eso no cargué Cornelio Saavedra 2883 ni Facundo Zuviría 5779. **Ojo: el registro "Ayacucho 2828" que ya está en la base podría no ser de Córdoba.** "Panadería Castillo SRL, Don Bosco 2706, San Vicente" y las confiterías de "San Vicente" en argentino.com.ar (Boston, Arrayanes, El Boulevard, La Primavera) podrían ser de San Vicente, provincia de Buenos Aires, así que no se cargaron.
- **Sin barrio ni dirección (hacen falta más búsquedas):** Cardamomo Panadería y Café, Bakeria, Panadería Villegas, Panadería Patagonia, Panadería San Alberto, Marcel Bakery (probablemente la misma que F1318), Panadería pan comido, Panadería Del Valle, Love Panadería y Confitería; en Páginas Amarillas: Santa Claus, Del Boulevard, Los Cubanitos, Del Pilar, Acapulco; en argentino.com.ar: Panificadoras La Castellana, Morval, Il Molino, Wilson, Del Valle, La Capillita, La Suiza, Sime, Hornett, Maná.

## Limitaciones
- WebSearch solo devuelve unos 10 títulos y un resumen por consulta, así que no permite leer listados completos (argentino, paginasamarillas, nuevaeranet, dirtel). El rendimiento real fue de unos 0,7 registros nuevos por búsqueda.
- Waze no dio resultados útiles para panaderías de Córdoba en 3 búsquedas.
- Z10 y Z04 fuera de Alberdi (Villa Páez, Marechal, Las Palmas, Siburu, Quebrada) quedaron prácticamente vacías.
- Los ratings que figuran en las notas son de restaurantguru, no de Google, así que google_rating queda en null.
