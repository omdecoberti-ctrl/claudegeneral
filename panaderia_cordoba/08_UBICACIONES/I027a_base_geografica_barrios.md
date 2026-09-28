# G1 — Base geográfica y sociodemográfica (notas y fuentes)
Fecha de consulta: 2026-09-28. Solo WebSearch (fragmentos). Salida: `g1_geo.json` (66 barrios, 13 corredores, 12 hitos).

## Fuentes
- F700 Mapcarta, Nueva Córdoba — https://mapcarta.com/N2466082735 (-31.42547, -64.18651)
- F701 De Rutas y Destinos, Nueva Córdoba — https://www.derutasydestinos.com/mapas-Barrio-Nueva-Cordoba--Cordoba.html
- F702 Mapcarta, Alta Córdoba — https://mapcarta.com/es/N11242782450 (-31.39854, -64.1807; ~34.600 hab.)
- F703 Wikipedia, Cerro de las Rosas — https://es.wikipedia.org/wiki/Barrio_Cerro_de_las_Rosas_(C%C3%B3rdoba) (31°22′18″S 64°14′01″O)
- F704 Mapcarta, Argüello — https://mapcarta.com/20076630 (-31.34342, -64.25944; ~8.100 hab.)
- F705 Wikipedia, General Paz — https://es.wikipedia.org/wiki/Barrio_General_Paz_(C%C3%B3rdoba) (31°24′44″S 64°10′02″O)
- F706 Wikipedia, Güemes — https://es.wikipedia.org/wiki/Barrio_G%C3%BCemes_(C%C3%B3rdoba) (31°25′32″S 64°11′45″O)
- F707 Mapcarta, Villa Belgrano — https://mapcarta.com/20011276 (-31.35797, -64.2525)
- F708 De Rutas y Destinos, Alto Alberdi — https://www.derutasydestinos.com/mapas-Barrio-Alto-Alberdi--Cordoba.html (31°24′21″S 64°13′16″O)
- F709 Mapcarta, Alberdi — https://mapcarta.com/N3238146987 (~32.700 hab.; sin coord. en fragmento)
- F710 Mapcarta, Villa Cabrera — https://mapcarta.com/N2466286231 (-31.3876, -64.21158; 6.440 hab.)
- F711 Wikipedia, Cofico — https://es.wikipedia.org/wiki/Barrio_Cofico (31°24′10″S 64°11′07″O)
- F712 De Rutas y Destinos, Villa Rivera Indarte — https://www.derutasydestinos.com/mapas-Villa-Rivera-Indarte--Cordoba.html (31°19′08″S 64°17′40″O)
- F713 De Rutas y Destinos, Urca — https://www.derutasydestinos.com/plano_calles_Barrio-Urca_(Cordoba).html (31°22′57″S 64°14′13″O)
- F714 Mapcarta, Centro — https://mapcarta.com/N2466067899 (~28.200 hab.)
- F715 Mapcarta, Juniors — https://mapcarta.com/N3009902021 (~6.520 hab.)
- F716 Wikipedia, Barrio Jardín — https://es.wikipedia.org/wiki/Barrio_Jard%C3%ADn_(C%C3%B3rdoba) (65 manzanas, límites; Mapcarta ~3.200 hab.)
- F717 Nuestra Ciudad, Jardín Espinosa — https://nuestraciudad.info/portal/Barrio_Jard%C3%ADn_Espinosa (NSE alto)
- F718 Wikipedia, Nueva Córdoba — https://es.wikipedia.org/wiki/Barrio_Nueva_C%C3%B3rdoba (~36.000 hab. en 2008; +23% 2001-2008)
- F719 Wikipedia, Villa El Libertador — https://es.wikipedia.org/wiki/Villa_El_Libertador (SO, fuera de Circunvalación, Av. Armada Argentina)
- F720 Perfil, mapa de 5 NSE (FCS-UNC) — https://www.perfil.com/noticias/cordoba/como-es-y-que-dice-el-mapa-de-los-cinco-niveles-socioeconomicos-de-cordoba.phtml
- F721 FCS-UNC, "Córdoba capital: las desigualdades en el territorio" — https://sociales.unc.edu.ar/content/c-rdoba-capital-las-desigualdades-en-el-territorio (NSE alto: eje noroeste + countries del sur)
- F722 Censo 2022, Córdoba — https://censo.gob.ar/index.php/datos_definitivos_cordoba/ (ciudad: 1.498.060 hab.; sin desagregado por barrio en los resultados)
- F723 latitude.to, Córdoba — https://latitude.to/map/ar/argentina/cities/cordoba (-31.4135, -64.1811)
- F724 Turismo Córdoba, Cerro de las Rosas — https://turismo.cordoba.gob.ar/barrio-cerro-de-las-rosas/

## Limitaciones
- **Se agotó el tope de búsquedas web de la sesión (200/200)** en mitad de la tarea. Por eso solo 12 barrios tienen coordenadas verificadas con fuente; 49 son `estimada` / `estimada (baja confianza)` (conocimiento general, error de 300 a 800 m o más) y 5 quedaron en null (Marechal, Ameghino, Ciudad de mis Sueños, Los Plátanos, Autopista).
- Todas las coordenadas de **corredores e hitos son estimadas**. Paseo Rivera Shopping quedó en null. La ubicación del Paseo del Jockey, Dinosaurio Mall, Córdoba Shopping, Av. Gauss, Av. O'Higgins y Av. Fructuoso Rivera es de baja confianza.
- **Población**: no hay datos por barrio del Censo 2022 en los resultados. Las cifras de Mapcarta/OSM no traen año (probablemente vienen del censo municipal 2008).
- **NSE**: no se pudo leer el mapa FCS-UNC barrio por barrio. Los valores son estimaciones salvo lo que indica `nse_fuente`.
- Coordenadas de código postal (mapawi, "coordenadas promedio") descartadas: devuelven el centroide de la ciudad (p. ej., VEL -31.425, -64.175, que es erróneo).
- Circunvalación y río Suquía omitidos: no se encontró el trazado.
- Chequeo automático: todos los puntos quedan dentro de lat −31.30 a −31.52 y lon −64.08 a −64.32.
