<p align="center">
  <img src="MULTIMEDIA/logo_unlz.png" alt="Universidad Nacional de Lomas de Zamora — Facultad de Ingeniería" width="480">
</p>

# StudIA — Asistente de estudio sobre corpus académico

**Tipo:** PPS · **Año:** 2026 — **Cuatrimestre:** 1C

**Carrera:** Ingeniería Mecatrónica
**Materia / Curso:** Práctica Profesional Supervisada (PPS)
**Docente / Tutor:** Cristian Lukaszewicz
**Autor:** De Palma, Marcos Agustin
**Período:** junio – septiembre de 2026 · **Dedicación:** 200 h estimadas (régimen previsto: lunes a viernes, 8:00 a 12:00)
**Entrega:** 18/09/2026

> 📦 **El código vive en su propio repositorio:**
> **[MarcosDePalma/UNLZ_Llamacode_StudIA](https://github.com/MarcosDePalma/UNLZ_Llamacode_StudIA)** (rama `feature/studia`)
> Este repositorio contiene la **documentación formal de la PPS**: informe, cronograma,
> Gantt, manuales, diagramas y multimedia.

---

## Introducción / Objetivo

**Contexto.** Un estudiante de ingeniería acumula a lo largo de la carrera cientos de
archivos de material de estudio —apuntes, libros, guías de trabajos prácticos,
presentaciones—. En este caso concreto: **2.690 documentos y 23 GB**. La información
existe, pero encontrarla cuesta, y los asistentes de IA de propósito general responden
desde su conocimiento general en lugar de hacerlo desde el apunte de la cátedra.

**Problema a resolver.** No hay forma de consultar el material propio en lenguaje
natural con trazabilidad de la fuente y sin subirlo a un servicio de terceros.

**Objetivo general.** Desarrollar un asistente de estudio de escritorio que responda
preguntas **usando exclusivamente la documentación académica indexada**, citando el
documento y la página de cada afirmación, y ejecutándose **íntegramente en la
computadora del estudiante**.

**Objetivos específicos**

- Indexar el corpus académico y recuperar los fragmentos pertinentes a una pregunta en
  lenguaje natural.
- **Abstenerse** de responder cuando el material no cubre la pregunta, en vez de
  improvisar.
- Ofrecer modos de estudio: resumen, explicación, autoevaluación, flashcards,
  ejercitación y plan de estudio.
- Mostrar citas verificables que abran el documento original.
- Permitir sumar bibliografía propia sin contaminar el índice de la cátedra.
- Empaquetar el sistema para instalarlo en una PC sin herramientas de desarrollo.
- Integrarse al proyecto base **sin modificar** sus subsistemas existentes.

---

## Índice
- [Brief](#brief)
- [Descripción técnica](#descripción-técnica)
- [Arquitectura del sistema](#arquitectura-del-sistema)
- [Instrucciones de uso](#instrucciones-de-uso)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Listado de componentes](#listado-de-componentes)
- [Esquemáticos / Planos](#esquemáticos--planos)
- [Fotos / Videos](#fotos--videos)
- [Documentación](#documentación)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Autor](#autor)

---

## Brief

**One-liner.** StudIA responde preguntas sobre los apuntes del propio estudiante,
citando documento y página, sin conexión y sin que el material salga de su computadora.

**Elevator pitch.** Este proyecto **StudIA** (PPS, 2026 1C) resuelve el problema de
**consultar material de estudio disperso en miles de archivos** mediante un **asistente
con recuperación aumentada (RAG) sobre un índice local del corpus académico**. Está
orientado a **estudiantes de ingeniería** y permite **preguntar en lenguaje natural y
obtener respuestas con la cita exacta del apunte**. Se implementa con **C++/Qt, SQLite
FTS5 y modelos de lenguaje ejecutados localmente**, y se valida mediante **322 pruebas
automatizadas y un conjunto calibrado de 30 preguntas reales**.

### Problema
- **Contexto:** estudio de materias de ingeniería con material propio de la carrera.
- **Dolor principal:** encontrar dónde se explica un tema exige recordar en qué archivo
  estaba; un asistente general responde desde internet, no desde el apunte evaluable.
- **Impacto:** tiempo perdido, respuestas plausibles pero falsas, material académico
  subido a servicios de terceros.

### Solución propuesta
- **Qué hace:**
  - Responde preguntas sobre el material indexado, **con citas clickeables**.
  - **Se abstiene** cuando el material no alcanza, antes de llamar al modelo.
  - Siete **modos de tutor**, gráficos de funciones, diagramas y exportación a Anki.
- **Cómo lo hace:** ingesta offline → índice SQLite/FTS5 → recuperación híbrida
  (BM25 + embeddings, fusión RRF) → control de evidencia → prompt con fragmentos
  numerados → modelo local → respuesta con citas.
- **Valor diferencial:** la garantía anti-invención **no depende del prompt**: es una
  decisión previa a la llamada al modelo, verificable por pruebas.

### Alcance
**Incluye:** módulo integrado a la aplicación de escritorio; ingesta de PDF/DOCX/PPTX/
XLSX/TXT/MD/IPYNB con OCR; recuperación híbrida; modos de tutor; instalador.
**No incluye:** servicio en la nube o multiusuario; entrenamiento de modelos;
corrección automática de exámenes; sistemas operativos distintos de Windows en la
versión empaquetada.

### Estado del proyecto
- **Madurez:** MVP validado sobre corpus real, con instalador funcionando.
- **Qué funciona hoy:** ingesta, recuperación híbrida, abstención calibrada, 7 modos,
  citas, figuras, exportación a Anki, bibliografía propia, instalador de un archivo.
- **Próximos pasos:** validación en máquina virtual limpia, OCR del remanente de
  escaneados, prueba con estudiantes, merge a `main` y release.

### Demo rápida
- **Video / capturas:** [`MULTIMEDIA/`](MULTIMEDIA/)
- **Instrucciones express:**
  1. Instalar `StudIA-1.0-Setup.exe`.
  2. Abrir la aplicación → sección **🎓 StudIA**.
  3. Elegir una materia y preguntar.

---

## Descripción técnica

StudIA se implementó como **módulo del proyecto institucional**
[UNLZ_Llamacode](https://github.com/cristianlukas/UNLZ_Llamacode), una estación de
trabajo de IA local desarrollada en la Facultad (Qt/QML + C++).

El aporte de esta PPS son **55 archivos y ~14.700 líneas** en 7 iteraciones:

| Área | Líneas | Contenido |
|---|---:|---|
| Core C++ (`src/core/studia/`) | 5.246 | índice, prompts, sesiones, embeddings, gráficos, texto, herramientas |
| Herramientas Python (`tools/studia/`) | 3.668 | ingesta, vectorización, OCR, graficador, auditoría |
| Pruebas (`tests/`) | 3.139 | suite QtTest del módulo |
| Interfaz (`qml/`) | 1.625 | página de StudIA y conversaciones por materia |
| Instalador (`installer/`) | 543 | Inno Setup y distribución del corpus |
| Documentación y build | 437 | README, guía del proyecto, CMake |

**La decisión de diseño central es la abstención determinística.** Si la recuperación
no encuentra evidencia suficiente, el sistema responde que no tiene información **sin
llegar a llamar al modelo**, según tres reglas: la pregunta debe tener al menos un
término discriminante; el score BM25 normalizado por esos términos debe superar un
umbral calibrado; y algún fragmento del tope debe cubrir dos o más términos distintos.
Calibrado sobre 30 preguntas en lenguaje natural contra un corpus de 2.690 documentos,
responde las 16 cubiertas y se abstiene en las 14 ajenas.

El detalle completo está en el [informe](INFORMES/informe_pps.md) y en el
[manual técnico](INFORMES/manuales/manual_tecnico.md).

---

## Arquitectura del sistema

**Entradas:** corpus académico (carpetas por materia); pregunta del estudiante; modo de
tutor; bibliografía propia adjuntada.

**Procesamiento:**
- *Offline (Python):* extracción de texto → fragmentación (1.200 caracteres, 200 de
  solape) → índice SQLite + FTS5 → OCR → vectorización con bge-m3.
- *En línea (C++):* recuperación híbrida BM25 + coseno con fusión RRF → control de
  evidencia → armado del prompt → generación por streaming SSE.

**Salidas:** respuesta con citas agrupadas por documento; gráficos de funciones
(matplotlib); diagramas (Mermaid); flashcards exportables a Anki.

**Interfaz:** sección 🎓 StudIA de la aplicación de escritorio.

![Diagrama de bloques](PLANOS/diagrama_bloques.png)

Diagramas completos en [`PLANOS/`](PLANOS/): arquitectura general, flujo de una
consulta, pipeline de ingesta y módulos del core.

---

## Instrucciones de uso

### Requisitos previos
- Windows 10/11 de 64 bits, 8 GB de RAM (16 GB recomendados), ~3 GB de disco.
- GPU opcional (sin ella el modelo responde más lento).
- Opcionales, para funciones puntuales: Python 3, matplotlib, Node.js + mermaid-cli,
  Tesseract con español. **La aplicación detecta cuáles faltan y ofrece instalarlas.**

### Instalación
1. Ejecutar `StudIA-1.0-Setup.exe` (no requiere permisos de administrador).
2. Ejecutar `instalar_dependencias.bat` o aceptar la instalación que ofrece la app.
3. *(Opcional)* `copiar_documentos.bat` para que las citas abran el PDF original.

### Uso
1. Abrir la aplicación y entrar a **🎓 StudIA**.
2. Elegir una **materia** (obligatorio: cada una tiene su propia conversación).
3. Preguntar en lenguaje natural, o usar un modo: `/resumen/`, `/explicacion/`,
   `/autoevaluacion/`, `/flashcards/`, `/ejercitacion/`, `/plan/`.
4. Verificar las **citas** al pie de cada respuesta.

Guía completa: [manual de usuario](INFORMES/manuales/manual_usuario.md) ·
[manual de instalación](INFORMES/manuales/manual_instalacion.md) ·
[manual del corpus](INFORMES/manuales/manual_corpus.md).

### Troubleshooting
- **El selector de materias está vacío** → no se encuentra `studia.db`: verificar
  `<instalación>\StudIA\studia.db`.
- **Siempre se abstiene** → índice vacío o de otro corpus: re-indexar y recalibrar el
  umbral.
- **Las citas no abren el documento** → el corpus no fue copiado: `copiar_documentos.bat`.
- **Los gráficos salen como texto** → falta matplotlib o mermaid-cli.

---

## Tecnologías utilizadas
- **Programación:** C++17, QML, Python 3.
- **Framework:** Qt 6 (Quick/QML), CMake, Visual Studio 2022.
- **Datos / búsqueda:** SQLite con FTS5 (BM25), vectores normalizados para coseno.
- **IA:** modelos de lenguaje locales vía `llama.cpp` (GGUF); embeddings **bge-m3**;
  RAG con fusión **Reciprocal Rank Fusion**.
- **Procesamiento de documentos:** pypdf, python-docx, python-pptx, openpyxl,
  pypdfium2, Tesseract OCR (español).
- **Figuras:** matplotlib, mermaid-cli.
- **Empaquetado:** Inno Setup, robocopy.
- **Pruebas:** QtTest, unittest, ctest.

---

## Listado de componentes

Al tratarse de un desarrollo de software, el listado corresponde a los **componentes
del sistema** y sus dependencias.

| Componente | Cant. | Especificación | Función |
|---|---:|---|---|
| Módulo core StudIA | 9 clases | C++17 / Qt 6 | Recuperación, abstención, prompts, sesiones |
| Interfaz StudIA | 2 | QML | Selector de materia, modos, citas, figuras |
| Herramientas offline | 11 | Python 3 | Ingesta, OCR, vectorización, auditoría, graficador |
| Índice del corpus | 1 | SQLite + FTS5 · ~139.000 fragmentos | Almacenamiento y búsqueda del material |
| Modelo de chat | 1 | GGUF vía `llama.cpp` | Generación de las respuestas |
| Modelo de embeddings | 1 | bge-m3 (CPU, puerto 8081) | Búsqueda semántica |
| Suites de prueba | 4 | QtTest + unittest · 322 casos | Verificación automatizada |
| Instalador | 1 | Inno Setup · 1,21 GB | Despliegue en PC sin herramientas de desarrollo |

---

## Esquemáticos / Planos
- Arquitectura general → [`PLANOS/diagrama_bloques.png`](PLANOS/diagrama_bloques.png)
- Flujo de una consulta → [`PLANOS/flujo_consulta.png`](PLANOS/flujo_consulta.png)
- Pipeline de ingesta → [`PLANOS/pipeline_ingesta.png`](PLANOS/pipeline_ingesta.png)
- Módulos del core → [`PLANOS/modulos_studia.png`](PLANOS/modulos_studia.png)

Las fuentes editables (Mermaid) están en [`PLANOS/fuentes/`](PLANOS/fuentes/).

---

## Fotos / Videos
Capturas de la aplicación y video de demostración en [`MULTIMEDIA/`](MULTIMEDIA/).

---

## Documentación

| Documento | Fuente | PDF |
|---|---|---|
| Informe de PPS | [`INFORMES/informe_pps.md`](INFORMES/informe_pps.md) | [`pdf/informe_pps.pdf`](INFORMES/pdf/informe_pps.pdf) |
| Cronograma | [`INFORMES/cronograma.md`](INFORMES/cronograma.md) | [`pdf/cronograma.pdf`](INFORMES/pdf/cronograma.pdf) |
| Diagrama de Gantt | [`INFORMES/gantt.md`](INFORMES/gantt.md) | [`pdf/gantt.pdf`](INFORMES/pdf/gantt.pdf) |
| Manual de instalación | [`manuales/manual_instalacion.md`](INFORMES/manuales/manual_instalacion.md) | [`pdf/manual_instalacion.pdf`](INFORMES/pdf/manual_instalacion.pdf) |
| Manual de usuario | [`manuales/manual_usuario.md`](INFORMES/manuales/manual_usuario.md) | [`pdf/manual_usuario.pdf`](INFORMES/pdf/manual_usuario.pdf) |
| Manual técnico | [`manuales/manual_tecnico.md`](INFORMES/manuales/manual_tecnico.md) | [`pdf/manual_tecnico.pdf`](INFORMES/pdf/manual_tecnico.pdf) |
| Manual del corpus | [`manuales/manual_corpus.md`](INFORMES/manuales/manual_corpus.md) | [`pdf/manual_corpus.pdf`](INFORMES/pdf/manual_corpus.pdf) |

Los PDF se regeneran con `python INFORMES/build_docs.py`.

---

## Estructura del repositorio
- [`CODIGO/`](CODIGO/) — Referencia al repositorio donde vive el código fuente.
- [`INFORMES/`](INFORMES/) — Informe, cronograma, Gantt y manuales (fuentes y PDF).
- [`PLANOS/`](PLANOS/) — Diagramas de arquitectura y sus fuentes.
- [`MULTIMEDIA/`](MULTIMEDIA/) — Imágenes y videos.

---

## Checklist de entrega
- [x] Naming del repo: `2026_1C_PPS_Asistente_de_Estudio_DE-PALMA`
- [x] Título, autor, carrera, tipo, año y cuatrimestre
- [x] Brief completo (one-liner, pitch, problema, solución, alcance, estado)
- [x] Instrucciones de uso reproducibles
- [x] Listado de componentes
- [x] Diagramas en `PLANOS/`
- [x] Informe PDF en `INFORMES/`
- [x] Cronograma y Gantt
- [x] Manuales de instalación, usuario, técnico y corpus
- [ ] Capturas y video demostración en `MULTIMEDIA/`
- [x] Datos académicos completos (materia, docente, tutor)

---

## Autor
**De Palma, Marcos Agustin**
Ingeniería Mecatrónica · Facultad de Ingeniería, UNLZ
Docente / Tutor: **Cristian Lukaszewicz**
Contacto: marcosdepalma03@gmail.com · GitHub [@MarcosDePalma](https://github.com/MarcosDePalma)

---

## About (descripción corta del repositorio)

> PPS — StudIA: asistente de estudio con RAG local sobre corpus académico — FI-UNLZ — 2026 — De Palma, Marcos Agustin
