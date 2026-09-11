# Manuales

StudIA es un proyecto de software. Esta carpeta contiene los manuales para
**guiar a los usuarios**, desde instalarlo hasta armar un corpus propio.

## Contenido

| Archivo | Qué muestra |
|---|---|
| [`Guía_de_Instalación.pdf`](Gu%C3%ADa_de_Instalaci%C3%B3n.pdf) | Cómo instalar StudIA en una PC desde cero: el instalador, las dependencias, dónde dejar el material de estudio y cómo conectarlo. Incluye la resolución de los problemas más comunes. |
| [`Manual_de_Usuario.pdf`](Manual_de_Usuario.pdf) | Cómo usarlo día a día: elegir materia, preguntar, los modos de tutor, las citas que abren el PDF original y la exportación a Anki. |
| [`Manual_Técnico.pdf`](Manual_T%C3%A9cnico.pdf) | Cómo está hecho por dentro: arquitectura del módulo, índice y recuperación, embeddings, configuración y empaquetado. Para quien tenga que mantenerlo o extenderlo. |
| [`Vectorizar_Nuevo_Corpus.pdf`](Vectorizar_Nuevo_Corpus.pdf) | Cómo armar un índice con material propio: organizar los apuntes, correr la ingesta, vectorizar y verificar que el índice quedó bien. |

---

Cada manual tiene su fuente en [`fuentes/`](fuentes/), en Markdown, de modo que
se pueda regenerar o corregir sin rehacer el PDF a mano. La fuente y la entrega
comparten nombre: `fuentes/Manual_Técnico.md` produce `Manual_Técnico.pdf`.

Para regenerarlos:

```bash
python Manuales/fuentes/build_docs.py                          # los cuatro
python Manuales/fuentes/build_docs.py --solo Manual_de_Usuario # uno
```

Requiere Python 3 con el módulo `markdown` (`pip install markdown`) y Google
Chrome o Microsoft Edge instalados.

---

Estos archivos fueron creados con inteligencia artificial, a partir del código de la app.
