# I001 — Demografía y socioeconomía de Córdoba Capital

| Campo | Valor |
|---|---|
| Código | I001 |
| Gate | G1 |
| Fecha inicio / fin | 2026-09-28 / 2026-09-28 (primera versión, desk) |
| Responsable | IA (investigación de escritorio) — pendiente de revisión por socios |
| Estado | FINALIZADA (v1 desk; con verificaciones pendientes, ver §7) |
| Preguntas que responde | Q015 (parcial), Q032 (parcial), Q016 (parcial) |
| Hipótesis que testea | — (insumo de contexto; no testea una A### puntual) |

## 1. Pregunta de investigación
¿Cuántas personas viven, trabajan y estudian en Córdoba Capital, dónde se concentran, con qué ingresos y hábitos? ¿Qué microzonas aparecen como candidatas para un local de panadería / bakery-café?

## 2. Objetivo
Armar la línea de base demográfica y socioeconómica de la ciudad para (a) dimensionar el mercado (Q015), (b) preseleccionar microzonas a relevar en campo (Q032 / PD016) y (c) dejar criterios reutilizables para expansión (red / franquicia).

## 3. Metodología
- **Tipo:** desk research. Búsquedas web el 2026-09-28.
- **Restricción técnica importante:** en esta sesión el acceso directo a páginas (WebFetch) estuvo **bloqueado por el proxy de red** para todos los dominios que se probaron (censo.gob.ar, indec.gob.ar, cba.gov.ar, wikipedia, citypopulation, cadena3, eldoce, etc.). Los datos salen de los **extractos devueltos por el buscador**, no de la lectura completa de cada documento. Por eso la confiabilidad de cada fuente se bajó un escalón respecto de la que tendría leída en origen, y todo dato clave queda marcado como **"a verificar en origen"** (ver §7).
- **Criterios:** prioridad a fuentes oficiales (INDEC, Gobierno de Córdoba, Municipalidad, UNC); después medios reconocidos; blogs sólo como indicio. Cuando dos fuentes no coinciden, se muestran las dos.
- **Período de los datos:** Censo 2022 (estructura), EPH 1.er semestre y 2.º trimestre 2026 (coyuntura), datos sectoriales 2024–2026.
- **Sin campo:** no hubo conteos peatonales, entrevistas ni encuestas.

## 4. Fuentes
Confiabilidad: **A** oficial/estadística · **B** estudio sectorial/medio reconocido · **C** blog/redes/opinión/wiki · **D** anecdótico. *(Todas consultadas vía extracto de buscador el 2026-09-28; ver §3.)*

| F### | Fuente | URL | Fecha consulta | Confiabilidad |
|---|---|---|---|---|
| F001 | Gobierno de Córdoba (prensa) — "Censo 2022: Córdoba tiene 3.978.984 habitantes" (resultados **provisionales**, feb-2023) | https://prensa.cba.gov.ar/informacion-general/censo-2022-cordoba-tiene-3-978-984-de-habitantes/ | 2026-09-28 | A |
| F002 | Telencuestas — Población del Departamento Capital 2022 (reprocesa INDEC, definitivos) | https://telencuestas.com/censos-de-poblacion/argentina/2022/cordoba/capital | 2026-09-28 | B |
| F003 | CityPopulation.de — Capital (Córdoba) / Córdoba localidad | https://www.citypopulation.de/es/argentina/cordoba/14014__capital/ | 2026-09-28 | B |
| F004 | Wikipedia — Córdoba (Argentina) / Capital Department | https://es.wikipedia.org/wiki/C%C3%B3rdoba_(Argentina) | 2026-09-28 | C |
| F005 | Cba24n — "Las 10 ciudades más pobladas de Córdoba según el último Censo" (definitivos por localidad) | https://www.cba24n.com.ar/cordoba/las-10-ciudades-mas-pobladas-de-cordoba-segun-el-ultimo-censo-nacional_a6692740c501eb5f0dc1610d1 | 2026-09-28 | B |
| F006 | Aguad Bienes Raíces (blog) — "En los últimos 30 años Córdoba se transformó: barrios que estallaron y otros que se vaciaron" (basado en cartografía censal de mapa.poblaciones.org) | https://www.aguadbienesraices.com.ar/blog/urbanismo-en-los-ultimos-30-anos-cordoba-se-transformo-hay-barrios-que-estallaron-y-otros-que-se-vaciaron/ | 2026-09-28 | C |
| F007 | Fundación Tejido Urbano — "Geografía inquilina de la ciudad de Córdoba" (2025, Censo 2022) | https://tejidourbano.net/wp-content/uploads/2025/02/36.-GEOGRAFIA-INQUILINA-DE-LA-CIUDAD-DE-CORDOBA.pdf | 2026-09-28 | B |
| F008 | Fundación Tejido Urbano — "Radiografía de las personas que viven solas" | https://tejidourbano.org.ar/informes/radiografia-de-las-personas-que-viven-solas-uno-de-cada-cuatro-hogares-en-argentina-es-unipersonal-mientras-que-en-la-ciudad-de-buenos-aires-trepa-al-40-de-los-hogares/ | 2026-09-28 | B |
| F009 | Cadena 3 / Perfil / ElDoce — Pobreza Gran Córdoba 1.er semestre 2026 (INDEC-EPH) | https://www.cadena3.com/noticia/sociedad/crecio-la-pobreza-en-cordoba-alcanzo-al-311-y-quedo-apenas-por-debajo-del-promedio-nacional_597489 | 2026-09-28 | B |
| F010 | INDEC — Incidencia de la pobreza y la indigencia en 31 aglomerados urbanos (1.er sem. 2026) *(no se pudo abrir)* | https://www.indec.gob.ar/uploads/informesdeprensa/eph_pobreza_09_2670733F4C4D.pdf | 2026-09-28 | A (no leída) |
| F011 | ElDoce / Cadena 3 / Telefe Córdoba — Desocupación Gran Córdoba 2.º trim. 2026 (INDEC-EPH) | https://eldoce.tv/politica/2026/09/17/la-desocupacion-subio-al-105-en-gran-cordoba-y-alcanzo-a-87-mil-personas-en-el-segundo-trimestre-de-2026/ | 2026-09-28 | B |
| F012 | Wikipedia — Gran Córdoba (población EPH 2.º trim. 2025) | https://es.wikipedia.org/wiki/Gran_C%C3%B3rdoba | 2026-09-28 | C |
| F013 | Facultad de Ciencias Sociales UNC — "Córdoba capital: las desigualdades en el territorio" (mapa de 5 NSE) + nota de Perfil | https://sociales.unc.edu.ar/content/c-rdoba-capital-las-desigualdades-en-el-territorio | 2026-09-28 | A |
| F014 | UNC — "Sobre la UNC" / Wikipedia UNC (≈180 mil estudiantes; 15 facultades) | https://www.unc.edu.ar/sobre-la-unc | 2026-09-28 | A |
| F015 | UNC — "La UNC abre sus puertas a casi 50 mil aspirantes" / Comercio y Justicia | https://www.unc.edu.ar/acad%C3%A9micas-comunicaci%C3%B3n/la-unc-abre-sus-puertas-casi-50-mil-aspirantes | 2026-09-28 | A |
| F016 | Wikipedia — Universidad Siglo 21 (matrícula total país) | https://es.wikipedia.org/wiki/Universidad_Siglo_21 | 2026-09-28 | C |
| F017 | Wikipedia (EN) — Catholic University of Córdoba / sitio UCC "Campus" | https://site.ucc.edu.ar/sin-asignar/sedes/campus-ucc/ | 2026-09-28 | C |
| F018 | UTN Facultad Regional Córdoba — página institucional | https://www.institucional.frc.utn.edu.ar/internacionales/frc.asp | 2026-09-28 | B |
| F019 | Gobierno de Córdoba (prensa) — "Ciclo Lectivo 2026: clases desde el 2 de marzo" | https://prensa.cba.gov.ar/educacion-3/ciclo-lectivo-2026-en-cordoba-las-clases-comenzaran-el-2-de-marzo-y-se-garantizan-los-190-dias-efectivos/ | 2026-09-28 | A |
| F020 | Vía País — "Ciclo lectivo 2027 en Córdoba: cuándo comienzan las preinscripciones" | https://viapais.com.ar/cordoba/ciclo-lectivo-2027-cordoba-comienzan-preinscripciones-asegurar-vacante_0_PyeR1eOtjR.html | 2026-09-28 | B |
| F021 | UNC — Calendarios académicos (FCQ; Fac. de Artes ene-2026/mar-2027) | https://www.fcq.unc.edu.ar/calendario-academico/ | 2026-09-28 | A |
| F022 | Municipalidad de Córdoba — "La tarifa del transporte urbano pasará a ser de $2.150" | https://cordoba.gob.ar/la-tarifa-del-transporte-urbano-pasara-a-ser-de-2-150/ | 2026-09-28 | A |
| F023 | Perfil — "Ciudad de Córdoba: el transporte recupera pasajeros y renueva unidades…" | https://www.perfil.com/noticias/cordoba/ciudad-de-cordoba-el-transporte-recupera-pasajeros-y-renueva-unidades-pero-este-ano-cae-el-corte-de-boleto.phtml | 2026-09-28 | B |
| F024 | Blog de turismo — "Transporte público en Córdoba 2026: guía SUBE" | https://swtucumanaventuras.com.ar/transporte/tarjeta-redbus-cordoba-la-guia-definitiva-para-moverte-en-transporte-publico-por-la-ciudad/ | 2026-09-28 | C |
| F025 | Officenter Argentina — "Los distritos crecen en la Ciudad de Córdoba" | https://officenterargentina.com/los-distritos-crecen-en-la-ciudad-de-cordoba/ | 2026-09-28 | C |
| F026 | La Nación — "Nueva comunidad empresarial" (Parque Empresarial Aeropuerto) | https://www.lanacion.com.ar/propiedades/inmuebles-comerciales/nueva-comunidad-empresarial-nid1622260/ | 2026-09-28 | B |
| F027 | Perfil — "Córdoba: las empresas de software crecen un 18% y ocupan a 18.342 personas" / Córdoba Cluster | https://www.perfil.com/noticias/cordoba/cordoba-las-empresa-de-software-crecen-un-18-y-ocupan-a-18342-personas.phtml | 2026-09-28 | B |
| F028 | CPI Córdoba — "La vacancia comercial se cuadruplicó en un año y llegó al 13,8%" | https://cpicordoba.org.ar/la-vacancia-comercial-se-cuadruplico-en-un-ano-en-cordoba-y-llego-al-138/ | 2026-09-28 | B |
| F029 | Perfil / Revista Container / CPI — vacancia 3.er trim. 2026 por zona y corredor | https://www.perfil.com/noticias/cordoba/senales-de-recuperacion-en-locales-comerciales-de-cordoba-nueva-cordoba-lidera-el-centro-mejora.phtml | 2026-09-28 | B |
| F030 | Hoy Día Córdoba — "Aumentó la cantidad de locales vacíos y en algunos sectores alcanza el 50%" (17-09-2026) | https://hoydia.com.ar/hoy-cordoba/aumento-la-cantidad-de-locales-vacios-y-en-algunos-sectores-alcanza-el-50/ | 2026-09-28 | B |
| F031 | Punto a Punto — "Dossier Manantiales: el plan de Edisur para crear un barrio-ciudad" | https://puntoapunto.com.ar/dossier-manantiales-se-expande-el-plan-de-edisur-para-crear-un-barrio-ciudad-en-cordoba | 2026-09-28 | C (sesgo de desarrollador) |
| F032 | Perfil — "Córdoba: los edificios y desarrollos inmobiliarios que se vienen este 2025" | https://www.perfil.com/noticias/cordoba/cordoba-los-edificios-y-desarrollos-inmobiliarios-que-se-vienen-este-2025.phtml | 2026-09-28 | B |
| F033 | Turismo Municipalidad de Córdoba — "Circuito: Córdoba y sus peatonales" | https://turismo.cordoba.gob.ar/circuito-cordoba-y-sus-peatonales/ | 2026-09-28 | A |
| F034 | Wikipedia — Centros de Participación Comunal (CPC) | https://es.wikipedia.org/wiki/Centros_de_Participaci%C3%B3n_Comunal | 2026-09-28 | C |
| F035 | Comercio y Justicia — "Casi 50.000 aspirantes en la UNC: Psicología, Económicas y Derecho, las más elegidas" | https://comercioyjusticia.info/profesionales/casi-50-000-aspirantes-en-la-unc-psicologia-economicas-y-derecho-las-carreras-mas-elegidas/ | 2026-09-28 | B |

## 5. Datos
> Cada dato etiquetado: [HECHO] [SUPUESTO] [ESTIMACIÓN] [INTERPRETACIÓN]. "[HECHO]" = dato publicado por la fuente citada (leído en extracto, ver §3).

### 5.1 Población total y hogares
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Población Depto. Capital, Censo 2022 **provisional** (feb-2023) | 1.565.112 | [HECHO] | F001 |
| Población Depto. Capital, Censo 2022 **definitivo** | 1.505.250 (F003, F004) / 1.505.150 (F002) — diferencia de 100 hab., probablemente error de tipeo en una de las dos | [HECHO] | F002, F003, F004 |
| Población localidad "Córdoba" (definitivos por localidad) | 1.498.060 hab. y 612.979 viviendas | [HECHO] | F005 |
| Viviendas Depto. Capital (provisional) | 621.595 (+148.724 vs 2010; 472.871 en 2010); el depto. con más viviendas del país | [HECHO] | F001 |
| Sexo (Depto. Capital, definitivo) | 789.399 mujeres (52,4%) / 715.751 varones (47,6%) | [HECHO] | F002 |
| Peso en la provincia | 39,2% de la población provincial | [HECHO] | F002 |
| Superficie / densidad | 576 km²; 2.610 hab/km² (F003). Wikipedia informa 2.273,5 hab/km² (otra base de superficie) | [HECHO] (inconsistente) | F003, F004 |
| Población Gran Córdoba (aglomerado EPH, 2.º trim. 2025) | 1.608.996 | [HECHO] | F012 |
| Capital dentro del Gran Córdoba | ≈93% (1,50 M / 1,61 M) | [ESTIMACIÓN] | F003, F012 |
| Tamaño medio del hogar (ciudad) | ≈2,5 personas | [HECHO] | F007 |
| Hogares que alquilan (ciudad) | 28,16% | [HECHO] | F007 |
| Hogares unipersonales | 26–30% de los hogares urbanos en Córdoba (provincia); 43% de los hogares en departamentos son unipersonales | [HECHO] | F008 |
| Hogares (cantidad) en la ciudad | ≈600 mil (1,5 M ÷ 2,5) — **dato oficial de hogares no encontrado** | [ESTIMACIÓN] | F003, F007 |

### 5.2 Estructura etaria (Depto. Capital, Censo 2022)
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Adultos mayores | 245.404 personas = 16,3% (59,4% mujeres) | [HECHO] | F002 |
| Menores de 18 | ≈24% (mayores de edad = 76,0%) | [HECHO] | F002 |
| Población 18–(umbral adulto mayor) | ≈60% (100 − 24 − 16,3) | [ESTIMACIÓN] | F002 |
| Grupos 0–14 / 15–64 / 65+ y edad mediana por depto. | **No encontrado** en extractos (existe en cuadros INDEC c2022_cordoba) | — | — |

> Nota: Telencuestas no aclara si "adulto mayor" es 60+ o 65+. A verificar en cuadro INDEC.

### 5.3 Distribución territorial y densidad por barrio
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Nueva Córdoba | 23.724 hab. (1991) → 51.018 (2022), +115%; "uno de los barrios de mayor densidad de la ciudad" | [HECHO] | F006 |
| Valle Escondido | 846 hab. (1991) → 6.174 (2022), +629,8%; hogares 228 → 1.950 (+755%); superficie urbana 0,4 → 2,7 km² | [HECHO] | F006 |
| Cerro de las Rosas | −48,5% de población 1991–2022; superficie 2,3 → 2,1 km² | [HECHO] | F006 |
| Patrón general | Periferias multiplicaron población (hasta ×7); Centro histórico y barrios tradicionales se vaciaron | [HECHO] | F006 |
| Inquilinos | Concentrados en el "mercado ciudad" (Centro histórico + Nueva Córdoba + alrededores), con >60% de hogares inquilinos en algunos radios; densificación en altura hacia General Paz, Pueyrredón, San Vicente, Alberdi y San Martín | [HECHO] | F007 |
| Hogares unipersonales | Concentración en Nueva Córdoba, General Paz y Güemes; en Centro histórico, Alta Córdoba y Alberdi predominan hogares de 2 personas (parejas) | [HECHO] | F007 |
| División administrativa | 14 CPC (Argüello, Centro América, Pueyrredón, Villa El Libertador, Empalme, Colón, Ruta 20, Monseñor Pablo Cabrera, Rancagua, Mercado de la Ciudad, Chalet San Felipe, San Vicente, Guiñazú, Jardín) | [HECHO] | F034 |
| Población por CPC / seccional / radio censal | **No encontrada** (existe capa de radios censales INDEC y portal Gobierno Abierto municipal, no accesibles en esta sesión) | — | — |

### 5.4 Nivel socioeconómico, ingresos y empleo
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Mapa NSE (FCS-UNC) | 5 niveles. **Alto:** eje noroeste (histórico) + periferia sur con countries/barrios cerrados (últimos 30 años). **Medio y medio-alto:** área central y pericentral. **Bajo y medio-bajo:** periferia, bordes de Av. Circunvalación | [HECHO] | F013 |
| Brecha por NSE | Gas natural: 6,8% hogares NSE bajo vs 99,2% NSE alto; PC de escritorio: 21,1% vs 61,2% | [HECHO] | F013 |
| % de hogares por NSE | **No encontrado** | — | — |
| Pobreza Gran Córdoba, 1.er sem. 2026 (personas) | 31,1% ≈ 503 mil personas (2.º sem. 2025: 23,2% → +7,9 pp) | [HECHO] | F009 (F010) |
| Pobreza (hogares) | 21,3% ≈ 125 mil hogares | [HECHO] | F009 |
| Indigencia | 7% ≈ 113 mil personas | [HECHO] | F009 |
| Promedio 31 aglomerados | 32,3% (Gran Córdoba 1,2 pp por debajo) | [HECHO] | F009 |
| Ingreso vs canastas (semestre) | Ingreso per cápita familiar +11,5% vs CBA +21,4% y CBT +19,6% → pérdida de poder de compra | [HECHO] | F009 |
| Ingreso medio per cápita en ARS Gran Córdoba | **No encontrado** (está en informe INDEC "Evolución de la distribución del ingreso" 1T2026, no accesible) | — | — |
| Desocupación Gran Córdoba 2T2026 | 10,5% (2T2025: 8,9%); ≈87 mil desocupados (vs 73 mil); 2.º más alto del país tras Gran Rosario (11,5%); promedio país 7,9% | [HECHO] | F011 |
| Tasa de empleo | 47,6% (1T2026) → 45,5% (2T2026) | [HECHO] | F011 |
| Ocupados que buscan otro empleo | 22,8% | [HECHO] | F011 (enredacción, mismo dato) |
| Personas bajo línea de pobreza en la Capital | ≈470 mil (31,1% × 1,5 M; supone misma tasa que el aglomerado) | [ESTIMACIÓN] | F003, F009 |

### 5.5 Población universitaria y campus
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| UNC — estudiantes | ≈180 mil (179.667 en una cita); 2.ª universidad más grande del país | [HECHO] | F014 |
| UNC — estructura | 15 facultades + 2 colegios preuniversitarios; 1,37 M m² en la ciudad, repartidos entre **Ciudad Universitaria** y el **casco histórico** (Manzana Jesuítica, Centro) | [HECHO] | F014 |
| UNC — preinscripciones | 49.724 (ciclo 2025; algún medio lo replica como 2026 — a verificar); más demandadas: Psicología, Económicas, Derecho, Arquitectura, Enfermería y Kinesiología | [HECHO] | F015, F035 |
| UTN-FRC | ≈10.000 estudiantes | [HECHO] | F018 |
| UTN-FRC — ubicación | Ciudad Universitaria / zona Maestro López (sur) | [SUPUESTO] (conocimiento general, a verificar) | — |
| UCC | >10.000 estudiantes, 3 sedes; Campus Camino a Alta Gracia (Rectorado + Derecho, Arquitectura, Económicas, Ciencia Política, Agropecuarias, Ingeniería) | [HECHO] | F017 |
| Siglo 21 | ≈90.000 estudiantes (2025) **en todo el país**, mayoría a distancia; matrícula presencial en Córdoba no encontrada | [HECHO] | F016 |
| Siglo 21 — campus | Campus en zona norte (Los Boulevares) | [SUPUESTO] (a verificar) | — |
| Estudiantes universitarios en la ciudad | ≥200 mil (UNC + UTN + UCC; sin Siglo 21 presencial, UBP, otras) | [ESTIMACIÓN] | F014, F017, F018 |
| Estudiantes de otras provincias / residentes en N. Córdoba | **No cuantificado** en fuentes encontradas | — | — |

### 5.6 Empleo y polos de oficinas
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Distritos corporativos | 7: Capitalinas, Alto Colón, Aeropuerto, Norte, Financiero, Nueva Córdoba y Sur; zona norte la de mayor dinamismo | [HECHO] | F025 |
| Parque Empresarial Aeropuerto (PEA) | 46 ha; inversión USD 22,5 M; potencial 316.000 m² de oficinas y >6.000 m² comerciales (nota no reciente) | [HECHO] | F026 |
| Ciudad Empresaria | Complejo sobre Av. La Voz del Interior (zona norte), con ampliación sostenida de m² | [HECHO] | F025 |
| Software/IT | 18.342 empleos (+12% interanual; fecha de la nota no confirmada) | [HECHO] | F027 |
| Economía del conocimiento (Córdoba Cluster) | >2.900 empresas y 57.000 empleos (provincia) | [HECHO] | F027 |
| Stock de m² de oficinas / vacancia de oficinas | **No encontrado** | — | — |
| Cantidad de personas que trabajan en el Centro | **No encontrado** | — | — |

### 5.7 Escuelas y calendario
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Calendario 2026 (Prov. Córdoba) | Inicio 2-mar-2026; receso invernal 6 al 17-jul; fin 18-dic; 190 días; docentes desde 18-feb | [HECHO] | F019 |
| Ciclo 2027 | Preinscripciones: inicial 24-ago a 21-sep-2026, primario 31-ago a 21-sep, secundario 7 a 21-sep. **Fecha de inicio de clases 2027 no publicada/encontrada** | [HECHO] | F020 |
| Inicio de clases 2027 | Primera semana de marzo 2027 (patrón histórico) | [SUPUESTO] | F019 |
| UNC 2027 | El año académico arranca en marzo con el 1.er cuatrimestre y cierra en febrero; la Fac. de Artes ya tiene calendario ene-2026/mar-2027. **Calendario 2027 completo no encontrado** | [HECHO] | F021 |
| Cantidad de escuelas y matrícula en Capital | **No encontrada** (existen Anuarios de Estadística Educativa provinciales y "Mapa de Establecimientos Educativos"; no accesibles). *Nota: varios resultados de búsqueda correspondían a Córdoba (España) y se descartaron.* | — | — |

### 5.8 Transporte público
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Boleto urbano | $2.150 desde 18-jul-2026 (nocturno $2.472,50; interbarrial $1.720; social $1.075; diferencial $8.600) | [HECHO] | F022 |
| Pasajeros subsidiados | 60% paga tarifa con algún beneficio | [HECHO] | F022 |
| Aporte municipal | ≈$7.000 millones/mes | [HECHO] | F022 |
| Pasajeros anuales | 124,2 M (2022) y 152 M (2023) | [HECHO] | F023 |
| Flota TUP (2024) | 724 unidades (Tamse 250, Coniferal 284, ex-Ersa 190), + SiBus | [HECHO] | F023 |
| Medio de pago | SUBE reemplaza a Red Bus desde ene-2026 | [HECHO] (fuente C, a verificar) | F024 |
| Pasajeros 2025–2026, corredores y líneas por zona | **No encontrado** | — | — |

### 5.9 Corredores comerciales y vacancia
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Vacancia comercial (CPI) | 3,1% (ago-2025) → 13,8% (ago-2026) | [HECHO] | F028 |
| Vacancia 3T2026 (otro relevamiento) | 4,3% en corredores; 15,8% en galerías. Por zona: Mercado Norte 9,2%, Centro 8,8%, Nueva Córdoba 6,2% | [HECHO] | F029 |
| Contradicción | 13,8% (F028) vs 4,3% (F029): metodologías/universos distintos; no comparables sin leer ambos | [INTERPRETACIÓN] | F028, F029 |
| Nueva Córdoba | Independencia, Buenos Aires y Rondeau recuperaron ocupación plena en sep-2026; tramos de Laprida, Obispo Salguero y Dámaso Larrañaga "a monitorear" | [HECHO] | F029 |
| Centro | Ituzaingó 300 / Ituzaingó y Corrientes (mayorista) con vacancia cero; algunas galerías 40–50% | [HECHO] | F029, F030 |
| Peatonales | 26 peatonales + 6 semipeatonales (desde 1969); San Martín la más popular | [HECHO] | F033 |
| Rafael Núñez (Cerro), Av. Colón, 25 de Mayo / Jerónimo Bardeu (General Paz), Av. Recta Martinoli (Argüello), etc. | Sin datos cuantitativos encontrados | [SUPUESTO] que son corredores relevantes; a verificar en campo | — |
| Flujo peatonal (personas/día) | **No encontrado** | — | — |

### 5.10 Desarrollos inmobiliarios / expansión
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Manantiales (sur) | >25.000 habitantes actuales; proyección 120.000 en la próxima década (dato del desarrollador); Manantiales I consolidado, II en expansión; club, colegio, locales, Hospital Allende | [HECHO] (fuente con sesgo) | F031 |
| Valle Escondido / Valle Cercano (noroeste) | Greenpark Torre Cuatro (30 unidades); >400 lotes a entregar en La Aventura, Los Arcos, Los Saltos (Valle Cercano) | [HECHO] | F032 |
| Crecimiento Valle Escondido | +629,8% de población 1991–2022 (ver 5.3) | [HECHO] | F006 |
| Zona norte ampliada | Crecimiento de Villa Allende, Mendiolaza, Río Ceballos, Salsipuedes (fuera del ejido) | [HECHO] | F032 |

### 5.11 Hábitos de consumo
| Dato | Valor | Etiqueta | Fuente |
|---|---|---|---|
| Hábitos de compra de pan/café, frecuencia, horarios, delivery por zona | **No encontrados** en esta investigación (corresponden a I002 / I007 / I016) | — | — |
| Proxies de hábito | Alta proporción de hogares unipersonales e inquilinos en el área central (F007, F008) + ≈200 mil universitarios → demanda de porciones individuales, consumo al paso, desayuno/merienda fuera de casa | [INTERPRETACIÓN] | F007, F008, F014 |

## 6. Conclusiones
1. **Tamaño:** Córdoba Capital tiene ≈1,5 M de habitantes (definitivo) y ≈600 mil hogares estimados de ≈2,5 personas; es ≈93% del Gran Córdoba. [HECHO]/[ESTIMACIÓN]
2. **Crecimiento desigual:** el centro histórico y barrios tradicionales (ej. Cerro de las Rosas, −48,5%) pierden residentes; crecen Nueva Córdoba (51 mil hab., +115% en 30 años), la periferia y las urbanizaciones (Valle Escondido +630%, Manantiales >25 mil). [HECHO]
3. **Área central = mercado de hogares chicos:** Nueva Córdoba, General Paz, Güemes concentran unipersonales e inquilinos (>60% en algunos radios), con densificación hacia Alberdi, San Vicente, Pueyrredón, San Martín. [HECHO]
4. **Ingresos bajo presión:** pobreza Gran Córdoba 31,1% (1S2026, +7,9 pp), desocupación 10,5% (2.º peor del país) e ingresos que crecen menos que las canastas. [HECHO] Implica consumo más sensible al precio y a la “ocasión justificable”. [INTERPRETACIÓN]
5. **NSE territorial claro:** alto en el eje noroeste (Cerro, Villa Belgrano, Argüello, Valle Escondido) y countries del sur; medio/medio-alto en el centro y pericentro; bajo en bordes de Circunvalación. [HECHO]
6. **Población universitaria enorme:** ≥200 mil estudiantes (UNC ≈180 mil) concentrados en Ciudad Universitaria, casco histórico y Nueva Córdoba; calendario marzo–diciembre con receso en julio. [HECHO]/[ESTIMACIÓN]
7. **Empleo formal de oficina:** se desplaza hacia zona norte (PEA, Ciudad Empresaria, distrito Aeropuerto) además de Centro y Nueva Córdoba; la economía del conocimiento es el segmento en crecimiento. [HECHO]
8. **Locales:** la vacancia subió fuerte en 2026 (CPI: 13,8%), pero Nueva Córdoba se mantiene baja (6,2%); Centro con focos de 40–50% en galerías → hay oferta de locales y poder de negociación, pero también señal de caída del consumo. [HECHO]/[INTERPRETACIÓN]

## 7. Limitaciones
- **Acceso:** WebFetch bloqueado por proxy; todos los datos provienen de extractos de buscador. Se agotó además el cupo de búsquedas de la sesión. **Ningún dato fue leído en el documento original** → verificar los críticos (población, pobreza, desocupación, vacancia) antes de usarlos en un memo de decisión.
- **Censo:** conviven cifras provisionales (1.565.112) y definitivas (1.505.250 / 1.505.150 depto.; 1.498.060 localidad). No se obtuvieron cantidad oficial de hogares, pirámide 0-14/15-64/65+, ni datos por radio censal/barrio/CPC salvo casos puntuales.
- **Barrios:** los datos de barrios (F006) vienen de un blog inmobiliario que reprocesa cartografía censal; confiabilidad C.
- **Ingresos:** no se obtuvo ingreso medio en ARS por aglomerado ni por zona; no hay dato de NSE en % de hogares.
- **Pobreza EPH:** es del aglomerado Gran Córdoba, no de la Capital ni por barrio. El salto 23,2% → 31,1% es muy fuerte: confirmarlo en el informe INDEC (F010).
- **Vacancia:** dos relevamientos con resultados muy distintos (13,8% vs 4,3%).
- **Educación:** no se consiguió cantidad de escuelas/matrícula en Capital; varios resultados eran de Córdoba (España) y se descartaron. Calendario escolar y universitario 2027 no publicados/encontrados.
- **Transporte:** sin pasajeros 2025–2026 ni carga por corredor; dato de SUBE de fuente C.
- **Hábitos de consumo:** fuera de alcance real de esta pesquisa; quedan para I002/I007/I016.
- Ubicaciones de UTN-FRC y campus Siglo 21 son [SUPUESTO] por conocimiento general.

## 8. Implicancias
| Para | Perspectiva 1 — Local 1 | Perspectiva 2 — Red / franquicia |
|---|---|---|
| Tamaño de mercado (Q015) | Base de ≈1,5 M hab./≈600 mil hogares alcanza para cualquier formato; el límite no es el tamaño sino el poder de compra (pobreza 31%, desempleo 10,5%). [INTERPRETACIÓN] | Córdoba soporta varias unidades; pero con ingresos cayendo, el modelo tiene que funcionar con ticket medio contenido, no sólo en NSE alto. [INTERPRETACIÓN] |
| Microzonas (Q032) | Candidatas a relevar: (a) Nueva Córdoba (densidad, estudiantes, unipersonales, vacancia baja), (b) General Paz/Alberdi/San Vicente (densificación, hogares chicos, alquiler más bajo supuesto), (c) Cerro/Villa Belgrano/Argüello (NSE alto, menos residentes pero alto gasto), (d) Zona norte/Aeropuerto (oficinas), (e) Centro (tránsito, oficinas, pero vacancia en galerías). [INTERPRETACIÓN] | Tipología de zonas replicable: "universitaria densa", "pericentral en densificación", "residencial NSE alto", "polo de oficinas", "urbanización nueva (Manantiales/Valle Escondido)". Cada tipo pide un formato distinto (take-away, salón, drive/estacionamiento). [INTERPRETACIÓN] |
| Estacionalidad | En zonas universitarias el flujo cae fuerte en ene-feb y en el receso de julio; la caja del local 1 debe aguantar ≈2–3 meses flojos si se instala en Nueva Córdoba. [INTERPRETACIÓN] | La red debería balancear zonas estudiantiles con residenciales/oficinas para suavizar la estacionalidad agregada. [INTERPRETACIÓN] |
| Surtido y precio | Área central: porciones individuales, combos desayuno/merienda, precio accesible; eje noroeste: producto premium y compra familiar de fin de semana. [INTERPRETACIÓN] | Menú modular (núcleo común + módulo por tipo de zona) facilita estandarizar producción centralizada. [INTERPRETACIÓN] |
| Alquileres | Vacancia en suba = oportunidad de negociar alquiler/meses de gracia en 2026–2027. [INTERPRETACIÓN] | Ventana para asegurar varias ubicaciones a precio bajo, pero riesgo de elegir zonas en declive (galerías del Centro). [INTERPRETACIÓN] |
| Crecimiento urbano | Manantiales / Valle Escondido crecen rápido pero con densidad baja y dependencia del auto; poco apto para local 1. [INTERPRETACIÓN] | Buenos candidatos para unidades 3–10 (formato con estacionamiento), sobre todo si el desarrollador reserva locales ancla. [INTERPRETACIÓN] |

## 9. Recomendaciones [RECOMENDACIÓN]
1. **Verificar en origen** (cuando haya acceso web completo): cuadros INDEC Censo 2022 depto. Capital (hogares, pirámide), informe INDEC pobreza 1S2026 e ingresos 1T/2T2026, informe CPI de vacancia, "Geografía inquilina" completo.
2. **Pedir datos por radio censal** (INDEC Redatam / mapa.poblaciones.org / Gobierno Abierto municipal) para calcular densidad por barrio en las 5 microzonas candidatas.
3. **Shortlist provisoria para relevamiento de campo (E### / I### de ubicaciones):** Nueva Córdoba (Independencia, Buenos Aires, Rondeau, Obispo Trejo), General Paz (25 de Mayo / Jerónimo Bardeu), Cerro de las Rosas (Rafael Núñez), zona norte (Ciudad Empresaria / Av. La Voz del Interior) y un punto del Centro. Hacer conteos peatonales por franja horaria (7–10 h, 16–19 h) en período lectivo y no lectivo.
4. **No descartar zonas NSE medio** por la coyuntura: evaluar el concepto en dos escenarios de precio.
5. Cruzar con I002 (consumo de pan) para transformar hogares en kg/mes y $/mes por zona.

## 10. Nuevas preguntas (→ OPEN_QUESTIONS)
- ¿Cuántos hogares y qué pirámide etaria tiene cada microzona candidata (dato por radio censal)?
- ¿Cuántas personas trabajan en el Centro, Nueva Córdoba y zona norte (empleo por lugar de trabajo, no de residencia)?
- ¿Qué parte de los ≈180 mil estudiantes de la UNC vive en Nueva Córdoba / Centro / Alberdi, y cuántos son de fuera de la ciudad?
- ¿Cuál es el ingreso medio (ARS) del Gran Córdoba y cómo se distribuye por NSE/zona?
- ¿Cuál de los relevamientos de vacancia (13,8% vs 4,3%) es comparable con nuestra búsqueda de local, y cuál es el alquiler $/m² por corredor?
- ¿Cuál es el flujo peatonal por franja horaria en los corredores candidatos?
- ¿Cuándo empiezan las clases escolares y universitarias en 2027 (publicación oficial)?
- ¿La caída de población de Cerro de las Rosas se tradujo en menos demanda comercial o sólo en reemplazo por comercio/oficinas en Rafael Núñez?
- ¿Qué tan rápido se ocupa realmente Manantiales / Valle Escondido y hay locales comerciales disponibles?

## 11. Actualizaciones realizadas
- [ ] ASSUMPTIONS · [ ] OPEN_QUESTIONS · [ ] RISKS · [ ] TASKS · [ ] STATUS · [ ] SOURCES · [ ] PROJECT_MASTER · [ ] FRANCHISE_READINESS_LOG

> Pendiente: por instrucción de esta tarea no se modificó ningún otro archivo del repo. Las fuentes F001–F035 deben volcarse a `00_MASTER/SOURCES.md` y las preguntas del §10 a `OPEN_QUESTIONS.md` por quien integre.
