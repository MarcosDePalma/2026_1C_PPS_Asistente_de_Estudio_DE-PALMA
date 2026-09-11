# Diagramas

StudIA es un proyecto de software. Esta
carpeta contiene los diagramas de la **arquitectura del sistema**.

## Contenido

| Archivo | Qué muestra |
|---|---|
| `diagrama_bloques.png` | Arquitectura general.  |
| `flujo_consulta.png` | Recorrido de una pregunta. |
| `pipeline_ingesta.png` | Extracción de texto y fragmentación. |
| `modulos_studia.png` | Módulos y sus responsabilidades. |

---

Cada diagrama tiene su fuente en `fuentes/*.mmd` ([Mermaid](https://mermaid.js.org/)),
de modo que se pueda regenerar o corregir sin rehacer la imagen a mano.

---

El script [`../build_docs.py`](../Documentación/build_docs.py) los regenera a
todos, junto a los manuales.

Estos archivos fueron creados con inteligencia artificial, a partir del código de la app.