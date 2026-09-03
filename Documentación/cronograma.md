# Cronograma de la PPS — StudIA

**Proyecto:** StudIA — Asistente de estudio sobre corpus académico
**Autor:** De Palma, Marcos Agustin — **Carrera:** Ingeniería Mecatrónica (FI-UNLZ)
**Docente / Tutor:** Cristian Lukaszewicz
**Período:** junio – septiembre de 2026 · 16 semanas · **Entrega:** 18/09/2026

**Dedicación:** **200 h en total**, con un régimen previsto de lunes a viernes de 8:00
a 12:00. Las horas por semana son una **estimación**: el reparto sigue lo que muestra el
repositorio, no el régimen teórico. La semana 10 lo excede con claridad —seis commits
entre el 5 y el 7 de agosto, dos de ellos de madrugada— y así queda reflejada.

> Las semanas 10 a 12 están respaldadas por commits con fecha verificable en el
> repositorio de código. Las semanas 1 a 8 son anteriores al primer commit y se
> reconstruyen a partir de los registros del repositorio local y del corpus.
> **Estados:** ✅ cumplido · 🔄 en curso · ⏳ planificado.

---

## 1. Cronograma semanal

| Sem. | Fechas | Etapa | Actividades | Entregable | h | Estado |
|---:|---|---|---|---|---:|---|
| 1 | 01–07/06 | Definición | Elección del tema. Identificación del problema: material de estudio disperso en cientos de PDF por materia. | Tema definido | 6 | ✅ |
| 2 | 08–14/06 | Definición | Relevamiento de alternativas: asistentes generales en la nube, buscadores de escritorio, RAG local. | Análisis de alternativas | 8 | ✅ |
| 3 | 15–21/06 | Definición | Objetivos, alcance y criterios de aceptación. Decisión de trabajar sobre el proyecto de la cátedra. | Propuesta de PPS | 8 | ✅ |
| 4 | 22–28/06 | Definición | Cierre del alcance: qué entra (RAG sobre corpus propio, modos de tutor) y qué no (nube, multiusuario). | Alcance aprobado | 8 | ✅ |
| 5 | 29/06–05/07 | Corpus | Recolección del material académico de la carrera. Organización por materia y cuatrimestre. | Corpus `DATA` (23 GB) | 12 | ✅ |
| 6 | 06–12/07 | Corpus | Depuración: formatos, duplicados, material que no es de estudio. Definición del criterio de exclusión. | Corpus depurado | 12 | ✅ |
| 7 | 13–19/07 | Entorno | **Fork de `cristianlukas/UNLZ_Llamacode` (17/07)**. Instalación de Qt, MSVC y CMake. Primera compilación. | Entorno funcionando | 12 | ✅ |
| 8 | 20–26/07 | Entorno | Estudio del código base: arquitectura Qt/QML + C++, `AppController`, backends, convenciones y suite de tests. | Base comprendida | 14 | ✅ |
| 9 | 27/07–02/08 | Desarrollo | Ingestor: extracción de texto, fragmentación e índice SQLite + FTS5. Primeras corridas sobre el corpus real. | `ingest.py` + índice | 16 | ✅ |
| 10 | 03–09/08 | Desarrollo | **Prototipo funcional (05/08)**. Modos de tutor, reorganización en 4 clases, citas agrupadas, figuras, OCR, Anki, búsqueda semántica, multiconversación. | 6 commits (`3da2c9b`→`dc8c122`) | 34 | ✅ |
| 11 | 10–16/08 | Empaquetado | Instalador Inno Setup, arranque autónomo del servidor de embeddings, reducción del corpus (23 → 7,7 GB), detección de dependencias. **Entrega instalable (13/08)**. | `4065803` + instalador | 22 | ✅ |
| 12 | 17–23/08 | Validación | Pruebas con usuario nuevo de Windows y plan de prueba en PC limpia. Corrección de rutas y perfiles. Calibración final de la abstención. | Informe de pruebas | 14 | ✅ |
| 13 | 24–30/08 | Documentación | Manuales, informe, cronograma, Gantt y diagramas de arquitectura. | Documentación completa | 14 | 🔄 |
| 14 | 31/08–06/09 | Validación | Validación en máquina virtual limpia (VirtualBox). Capturas de la aplicación y video de demostración. | Multimedia + informe de VM | 10 | ⏳ |
| 15 | 07–13/09 | Cierre | Revisión con el tutor y correcciones. OCR del remanente de documentos escaneados. | Documentación revisada | 6 | ⏳ |
| 16 | 14–18/09 | Cierre | Preparación de la defensa. **Entrega de la PPS (18/09)**. | Presentación + entrega | 4 | ⏳ |
| | | | **Total** | | **200** | |

---

## 2. Hitos

| Hito | Fecha | Verificación |
|---|---|---|
| H1 · Propuesta de PPS aprobada | 30/06/2026 | acuerdo con el tutor docente |
| H2 · Fork del proyecto base | 17/07/2026 | repositorio `UNLZ_Llamacode_StudIA` |
| H3 · Corpus indexado | 02/08/2026 | 2.690 documentos · ~139.000 fragmentos |
| H4 · Primer prototipo funcional | 05/08/2026 | commit `3da2c9b` |
| H5 · Módulo funcional completo | 07/08/2026 | commit `dc8c122` |
| H6 · Versión instalable | 13/08/2026 | commit `4065803` · instalador de 1,21 GB |
| H7 · Documentación completa | 30/08/2026 | repositorio de la PPS |
| H8 · **Entrega de la PPS** | 18/09/2026 | entrega formal a la cátedra |

---

## 3. Distribución del esfuerzo

| Etapa | Semanas | Horas | % |
|---|---|---:|---:|
| Definición y análisis | 1–4 | 30 | 15 % |
| Preparación del corpus | 5–6 | 24 | 12 % |
| Entorno y estudio del código base | 7–8 | 26 | 13 % |
| Desarrollo del módulo | 9–10 | 50 | 25 % |
| Empaquetado y distribución | 11 | 22 | 11 % |
| Validación y pruebas | 12 y 14 | 24 | 12 % |
| Documentación y cierre | 13, 15 y 16 | 24 | 12 % |
| **Total** | **16** | **200** | **100 %** |

Tres observaciones sobre el reparto:

- **El desarrollo se concentra en dos semanas (25 % del total).** No es que el módulo
  se haya hecho en dos semanas: es que las ocho anteriores —corpus, entorno y estudio
  del código base— dejaron el terreno preparado para que escribir el módulo fuera
  rápido. La semana 10 concentra seis commits en tres días.
- **El 13 % dedicado a comprender el código base no fue tiempo perdido.** El módulo se
  integró sin modificar el agente, el chat ni los backends del proyecto original; eso
  sólo es posible después de entender dónde están los límites de cada subsistema.
- **Validación, empaquetado y documentación suman 35 %.** No es sobrecosto: el trabajo
  no termina cuando el código anda en la máquina propia, sino cuando otra persona puede
  instalarlo, usarlo y mantenerlo.

---

## 4. Desvíos respecto de lo planificado

| Desvío | Causa | Resolución |
|---|---|---|
| La búsqueda por palabras (BM25) no resolvía preguntas equivalentes formuladas distinto | Limitación conocida del método léxico: compara términos, no significado | Se incorporó búsqueda semántica con embeddings y fusión RRF (semana 10), no prevista en el alcance inicial |
| 154 documentos del corpus quedaron sin texto extraíble | PDF escaneados sin capa de texto | Se agregó OCR con Tesseract y se registraron como `necesita_ocr` en vez de descartarlos |
| El primer umbral de abstención rechazaba preguntas válidas | Se normalizaba el score por el total de términos, castigando preguntas en lenguaje natural | Recalibración sobre 30 preguntas reales; se normaliza por términos discriminantes |
| El instalador superaba el límite de tamaño de un `.exe` | Windows no admite ejecutables de más de 4,2 GB y el corpus tiene rutas de más de 260 caracteres | El corpus se distribuye aparte con `robocopy` a un destino de ruta corta |
| Aparecían perfiles de usuario duplicados | Defecto heredado del proyecto base, no del módulo | Se corrigió en el proyecto base y se migran los perfiles existentes |

---

## 5. Trabajo futuro (posterior a la entrega)

| Actividad | Prioridad | Estimación |
|---|---|---:|
| Integrar el módulo sobre la versión actual del proyecto base | Alta | 12 h |
| Prueba con estudiantes de la carrera y medición de utilidad percibida | Media | 16 h |
| Ampliar el conjunto de calibración y medir precisión de las citas | Media | 10 h |
| Recalibración del umbral de abstención para corpus de otras carreras | Baja | 6 h |

> **Sobre la integración.** El desarrollo se hizo sobre el estado del proyecto base al
> 17/07/2026 y desde entonces el proyecto original avanzó **583 commits**. Un merge de
> `feature/studia` a `main` deja hoy **7 archivos en conflicto** —los mismos que el
> módulo tuvo que tocar: `CMakeLists.txt`, `NavBar.qml`, `AppController.cpp`,
> `Main.qml`, `CLAUDE.md`, `.gitignore` y un acceso directo eliminado aguas arriba—.
> Es trabajo de integración acotado pero real, y requiere recompilar y volver a correr
> la suite completa antes de darlo por bueno.
