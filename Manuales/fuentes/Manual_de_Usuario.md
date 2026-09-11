# Manual de Usuario — StudIA

**Versión:** 1.0 · **Fecha:** 18/09/2026
**Proyecto:** StudIA — Asistente de estudio sobre corpus académico (PPS · FI-UNLZ)

---

## 1. Qué es StudIA

StudIA responde preguntas **usando el material de estudio indexado** —los apuntes,
libros y trabajos prácticos de la carrera— y **no** el conocimiento general de
internet. Cada afirmación viene con la cita del documento y la página de donde sale, y
esa cita se puede abrir.

Tres cosas que conviene saber desde el principio:

| | |
|---|---|
| **Funciona sin internet** | Todo corre en tu computadora. El material no sale de la máquina. |
| **Si no está en el material, no responde** | Cuando la documentación no cubre la pregunta, StudIA lo dice en lugar de inventar. No es una falla: es el comportamiento buscado. |
| **Trabaja por materia** | Hay que elegir una materia antes de preguntar. Cada una tiene sus propias conversaciones. |

---

## 2. Primer uso

1. Abrí **LlamaCode** y entrá a la sección **🎓 StudIA** de la barra de navegación.
2. Elegí una **MATERIA** en el selector de arriba. Están en orden de cursada, por
   cuatrimestre. Hasta que elijas una, la barra de escritura permanece deshabilitada.
3. Escribí tu pregunta y presioná Enter.

La primera respuesta puede demorar más que las siguientes: el modelo se está cargando
en memoria.

> **Si el chat no responde:** verificá que el servidor del modelo esté levantado desde
> la sección correspondiente de LlamaCode. StudIA usa el servidor que administra la
> aplicación; no levanta uno propio.

---

## 3. La pantalla

| Elemento | Para qué sirve |
|---|---|
| **MATERIA** | Selector de asignatura. Cambiarla conmuta de conversación. |
| **☰ Temas (n)** / **MIS CHATS** | Varias conversaciones dentro de la misma materia. Sirve para no mezclar temas: una para el parcial, otra para el TP. |
| **Barra de modos** | Resumen, Explicación, Autoevaluación, Flashcards, Ejercitación, Plan de estudio. Cada modo tiene su color. |
| **📎** | Agregar un documento propio a *Mi bibliografía*. |
| **MI BIBLIOGRAFÍA · + agregar** | Lista de lo que sumaste, con la opción de quitarlo. |
| **⧉ Copiar** | Copia la respuesta al portapapeles. |
| **⇩ Exportar a Anki (n)** | Aparece en las respuestas de Flashcards. |
| **Limpiar chat** | Vacía la conversación actual. No borra el índice ni el material. |
| **Fuentes** | Al pie de cada respuesta. Clickeables: abren el documento original. |

El texto de las respuestas **se puede seleccionar y copiar**, incluidas las fórmulas.

---

## 4. Los modos de estudio

Un modo cambia **qué se le pide al modelo con los mismos fragmentos recuperados**. No
cambia de dónde sale la información: siempre del material indexado.

Se elige con un botón, o se escribe a mano el prefijo al principio del mensaje.

| Modo | Prefijo | Para qué sirve | Ejemplo |
|---|---|---|---|
| **Conversación** | *(ninguno)* | Preguntas puntuales y repreguntas. | `¿qué es el deslizamiento en un motor asincrónico?` |
| **Resumen** | `/resumen/` | Condensar un tema para repasar. | `/resumen/ transformada de Laplace` |
| **Explicación** | `/explicacion/` | Entender algo desde cero, paso a paso. | `/explicacion/ criterio de estabilidad de Routh` |
| **Autoevaluación** | `/autoevaluacion/` | Tomarte examen: preguntas y después las respuestas. | `/autoevaluacion/ modelo OSI` |
| **Flashcards** | `/flashcards/` | Tarjetas pregunta/respuesta exportables a Anki. | `/flashcards/ tipos de sensores` |
| **Ejercitación** | `/ejercitacion/` | Resolver un problema paso a paso: datos, método, desarrollo, resultado y verificación. | `/ejercitacion/ calcular la corriente de arranque` |
| **Plan de estudio** | `/plan/` | Organizar el estudio de una materia en el tiempo disponible. | `/plan/ tengo 10 días para el final` |

El prefijo va **al principio** y no distingue mayúsculas ni tildes: `/Flashcards/`,
`/flashcards/` y `/autoevaluación/` funcionan igual.

### Modos exigentes y modos flexibles

Resumen, Autoevaluación, Flashcards y Plan de estudio son **exigentes**: generan
material que después vas a estudiar como si fuera fiel al apunte, así que StudIA
prefiere abstenerse antes que arriesgar.

Conversación, Explicación y Ejercitación son **flexibles**: son diálogo, y ahí sí
aprovecha lo que haya —respondiendo parcialmente o deduciendo, siempre marcándolo—.

---

## 5. Las citas

Al pie de cada respuesta aparecen las fuentes, **agrupadas por documento**: un PDF que
aportó tres páginas se muestra una sola vez, como `apunte.pdf · pág. 11, 14, 16`.

- Los números `[1]`, `[2]` dentro del texto corresponden a esa lista.
- Un click en la cita abre el documento original.
- Para que la cita abra el PDF, la carpeta `DATA_StudIA` tiene que estar **junto al
  `studia.db`** que abriste. Si se separaron, StudIA explica el motivo en lugar de no
  hacer nada.

**Verificá siempre la cita antes de darle un uso importante a una respuesta.** Esa es
la razón por la que las citas existen.

---

## 6. Cuando StudIA no responde

Si el material indexado no cubre la pregunta, StudIA lo dice. Ante esa respuesta:

| Situación | Qué hacer |
|---|---|
| La pregunta es muy genérica (*«¿cuál es el mejor método?»*) | Reformulá con términos concretos de la materia. |
| El tema existe pero preguntaste con otras palabras | Usá el vocabulario del apunte. Con la búsqueda semántica activa esto importa menos. |
| El material no está en el índice | Sumalo con 📎 (§7) o pedí que se re-indexe el corpus. |
| El apunte está escaneado sin texto | Necesita OCR: ver el *Vectorizar_Nuevo_Corpus*. |

---

## 7. Sumar tu propia bibliografía

El botón **📎** agrega un documento tuyo (PDF, DOCX, PPTX, XLSX, TXT, MD, IPYNB).

- Va a un **índice separado** del de la cátedra. Nunca se mezclan, y en las citas se
  distingue el origen.
- Se puede **listar y quitar** desde **MI BIBLIOGRAFÍA**. Quitar un documento del
  índice **no borra el archivo**.
- El material de la cátedra nunca se modifica.
- Requiere **Python instalado** (la extracción de texto la hace la misma herramienta de
  ingesta). Si falta, StudIA lo avisa y ofrece instalarlo.

---

## 8. Figuras: gráficos y diagramas

Cuando la pregunta lo justifica, StudIA puede acompañar la respuesta con:

- **Gráficos de funciones** — `graficá x²-3x+2 entre -2 y 5 y sombreá el área entre 1 y 2`.
- **Diagramas** — `hacé un diagrama del proceso de arranque de un motor`.

Mientras la figura se genera se muestra el texto que la origina, así que nunca se
pierde información. Si falta la herramienta correspondiente (matplotlib o mermaid-cli),
la figura se muestra como texto y **el resto de la respuesta funciona igual**. StudIA
indica qué falta y ofrece instalarlo.

---

## 9. Exportar flashcards a Anki

1. Pedí las tarjetas con `/flashcards/ <tema>`.
2. En la respuesta, tocá **⇩ Exportar a Anki (n)**.
3. Se genera un archivo de texto separado por tabulaciones.
4. En Anki: **Archivo → Importar**, elegí el archivo, mazo y tipo de nota, e importá.

Los saltos de línea internos se convierten al formato que Anki interpreta, de modo que
las tarjetas de varias líneas se ven bien.

---

## 10. Búsqueda semántica

Con la búsqueda semántica activa, StudIA encuentra por **significado** además de por
palabras: *«¿qué pasa si…?»* y *«¿qué sucede si…?»* llegan al mismo material.

En la versión instalada **se activa sola**: la aplicación levanta el servidor de
embeddings al abrir y lo cierra al salir. Si el cartel del panel indica que no está
disponible, un click permite configurar la URL del servidor
(`http://127.0.0.1:8081`). Dejarla vacía es válido: StudIA sigue funcionando con
búsqueda por palabras.

---

## 11. Recomendaciones de uso

1. **Preguntá con los términos de la materia.** El índice es tu apunte, no internet.
2. **Una conversación por tema.** Las repreguntas usan el hilo previo como contexto;
   mezclar temas lo ensucia.
3. **Aprovechá las repreguntas.** *«Explicalo más simple»*, *«repetí la ecuación
   anterior»*, *«no entendí el paso 2»* funcionan: la respuesta sale de la
   conversación.
4. **Usá Autoevaluación antes del parcial** y Flashcards para lo que hay que memorizar.
5. **Chequeá las citas.** Un asistente que cita se controla; uno que no cita, no.
6. **Si algo no anda, mirá el aviso de herramientas.** StudIA informa qué falta y qué
   función se pierde por eso.

---

## 12. Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La barra de escritura está deshabilitada | No hay materia seleccionada | Elegí una materia. |
| No responde nada | El servidor del modelo no está levantado | Levantalo desde LlamaCode. |
| Responde siempre que no tiene información | No se abrió el índice, o es de otro corpus | Apretá **Abrir índice** y elegí el `studia.db` correcto (ver *Guía de Instalación*). |
| El botón 📎 no hace nada | Falta Python | Ejecutá el instalador de dependencias que ofrece la aplicación. |
| Los gráficos salen como texto | Falta matplotlib o mermaid-cli | Ídem. |
| Las citas no abren el documento | `DATA_StudIA` falta o quedó separada del `studia.db` | Poné las dos cosas en la misma carpeta y volvé a elegir el índice. |
| Un apunte no aparece nunca | Está escaneado sin capa de texto | Necesita OCR: ver el *Vectorizar_Nuevo_Corpus*. |
