# Planos

StudIA es un proyecto de software: en lugar de planos eléctricos o mecánicos, esta
carpeta contiene los **diagramas de arquitectura** del sistema — el equivalente
funcional para un desarrollo de este tipo.

## Contenido

| Archivo | Qué muestra |
|---|---|
| `diagrama_bloques.png` | Arquitectura general: corpus académico → ingesta → índice → aplicación → modelo. Dónde termina LlamaCode y dónde empieza StudIA. |
| `flujo_consulta.png` | Recorrido de una pregunta: recuperación híbrida, control de abstención, armado del prompt, generación y renderizado. |
| `pipeline_ingesta.png` | Proceso offline: extracción de texto, fragmentación, índice FTS5, vectorización y OCR. |
| `modulos_studia.png` | Módulos del core y sus responsabilidades (`StudiaController` y colaboradores). |

Cada diagrama tiene su fuente en `fuentes/*.mmd` ([Mermaid](https://mermaid.js.org/)),
de modo que se pueda regenerar o corregir sin rehacer la imagen a mano.

## Regenerar los diagramas

```bash
npm install -g @mermaid-js/mermaid-cli
cd PLANOS
mmdc -i fuentes/diagrama_bloques.mmd -o diagrama_bloques.png -b white -s 2
```

El script [`../INFORMES/build_docs.py`](../INFORMES/build_docs.py) los regenera
todos junto con los PDF del informe y los manuales.

## Otros planos

Si se agregan diagramas hechos con otra herramienta (draw.io, Visio, Inkscape),
dejar el archivo editable además del `.png` exportado, con el mismo nombre base.
