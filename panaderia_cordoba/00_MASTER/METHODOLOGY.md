# METODOLOGÍA DE TRABAJO

## 1. Ciclo de trabajo (se aplica a cada tema)
```
PROBLEMA → HIPÓTESIS → INVESTIGACIÓN → EVIDENCIA → ALTERNATIVAS → ANÁLISIS
→ REVISIÓN CRÍTICA → DECISIÓN HUMANA → DOCUMENTACIÓN → EJECUCIÓN
→ MEDICIÓN → APRENDIZAJE → ACTUALIZACIÓN DEL MODELO
```
| Paso | Qué produce | Dónde queda |
|---|---|---|
| Problema | Pregunta clara (Q###) | OPEN_QUESTIONS |
| Hipótesis | Supuesto testeable (A###) | ASSUMPTIONS |
| Investigación | Ficha I### | 18_INVESTIGACIONES o carpeta de área |
| Evidencia | Datos etiquetados + fuentes F### | Ficha I### + SOURCES |
| Alternativas | ≥ 2–3 opciones reales (incluida "no hacer") | Ficha / memo de decisión |
| Análisis | Comparación con criterios y números | Ficha / memo |
| Revisión crítica | Argumentos en contra, sesgos, huecos | Sección obligatoria del memo |
| Decisión humana | Aprobación de socios | DECISIONS (D###) |
| Ejecución | Tareas T### | TASKS |
| Medición | KPIs / experimentos E### | 16_KPIS / 19_EXPERIMENTOS |
| Aprendizaje | L### | LEARNINGS |

## 2. Doble perspectiva (obligatoria)
Todo análisis de alternativas incluye estas dos columnas:
| Criterio | Perspectiva 1 — Primera unidad | Perspectiva 2 — Red (5/10/50/100) |
|---|---|---|
| ¿Mejora rentabilidad del local 1? | | |
| ¿Se puede estandarizar/documentar? | | |
| ¿Depende de personas clave? | | |
| ¿Facilita o dificulta franquiciar? | | |

Si una opción es buena para el local 1 pero mala para escalar, se explicita el trade-off y lo deciden los socios.

## 3. Etiquetas de evidencia
| Etiqueta | Significado | Ejemplo |
|---|---|---|
| [HECHO] | Dato verificable con fuente | "Córdoba Capital tiene X hab. (INDEC 2022, F003)" |
| [SUPUESTO] | Se toma como cierto sin verificar aún | "El cliente de oficina compra 3 veces/semana" |
| [ESTIMACIÓN] | Número calculado a partir de datos + supuestos | "Mercado estimado: $X/año" |
| [INTERPRETACIÓN] | Lectura propia de los datos | "La competencia premium se concentra en Nueva Córdoba" |
| [RECOMENDACIÓN] | Sugerencia de la IA / consultor | "Priorizar segmento oficinas" |
| [DECISIÓN] | Aprobado por socios (con D###) | "D004: el local 1 tendrá cafetería" |

Nivel de confianza (hipótesis y estimaciones): **Alta / Media / Baja**.

## 4. Protocolo de decisión
1. La IA detecta que hace falta decidir → crea PD### en `DECISIONS.md`.
2. Arma un memo con `PLANTILLAS/TEMPLATE_MEMO_DECISION.md`: problema, opciones, pros, contras, números, riesgos, doble perspectiva, recomendación.
3. **Se detiene y espera** la decisión de los socios.
4. Aprobada → se registra como D### (fecha, responsable, fecha de revisión). PD### queda cerrada con referencia al D###.
5. Toda decisión es revisable: si la evidencia cambia, se abre nueva PD que puede reemplazar ("supersede") a la anterior.

Clasificación: **Estratégica** (socios) · **Táctica** (responsable de área, informada a socios) · **Operativa** (equipo).

## 5. Gate Reviews
Al completar los entregables de un Gate se hace un Gate Review con `PLANTILLAS/TEMPLATE_GATE_REVIEW.md`:
- ¿Se respondieron las preguntas del Gate? ¿Con qué nivel de evidencia?
- ¿Se cumplen los criterios de avance?
- Resultado: **GO** / **GO CONDICIONAL** (con acciones) / **RECICLAR** (volver a trabajar) / **STOP** (pivotar o frenar).
- El resultado lo aprueban los socios y se registra como decisión D###.
- Los Gates G1–G3 pueden correr en paralelo; G8 (metodología de ubicación) puede arrancar antes de cerrar G7. Ningún Gate se cierra automáticamente.

## 6. Validación antes de invertir (principio "evidencia creciente, inversión creciente")
Nivel 0 — escritorio (datos secundarios) → Nivel 1 — observación en calle / mystery shopping → Nivel 2 — entrevistas y encuestas → Nivel 3 — pruebas de producto (degustaciones ciegas) → Nivel 4 — pruebas de venta real (pop-up, preventa, stand, venta a oficinas) → Nivel 5 — local piloto.
Cada peso invertido debería respaldarse con el nivel de evidencia proporcional.

## 7. Cadencia sugerida
| Frecuencia | Qué | Salida |
|---|---|---|
| Por sesión de trabajo | Trabajo + regla de documentación | SESSION_LOG, STATUS |
| Semanal | Revisión de STATUS, tareas y decisiones pendientes con socios | Minuta, decisiones D### |
| Por Gate | Gate Review | Decisión GO/NO GO |
| Mensual (desde piloto) | Revisión de KPIs y P&L | Reporte 16_KPIS |

## 8. Regla de documentación
Ver `../CLAUDE.md` §3. Después de cada trabajo importante se actualizan: hallazgos, hipótesis, preguntas, decisiones, tareas, STATUS, PROJECT_MASTER, CHANGELOG, y el log de franquiciabilidad si aplica.

## 9. "Documentar para franquiciar" desde el día 1
Cada vez que se defina un proceso, receta, estándar, criterio o formato, preguntarse: **¿en qué manual futuro termina esto?** y registrarlo en `17_FRANQUICIA/FRANCHISE_READINESS_LOG.md`. Los procedimientos se escriben con `TEMPLATE_SOP.md` (formato ya apto para manual operativo).

## 10. Reglas de higiene de información
- Un tema = un lugar. Se enlaza, no se duplica.
- Todo dato externo: fuente, URL, fecha de consulta, dato obtenido (SOURCES.md).
- Montos en ARS siempre con mes/año de referencia; comparaciones de largo plazo en USD o ARS constantes.
- Nada se borra: lo obsoleto se marca o se mueve a `99_ARCHIVO/`.
