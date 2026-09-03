# Informes

Documentación formal de la PPS: informe, cronograma, diagrama de Gantt y manuales.

Los documentos se escriben en Markdown (versionable y diffeable) y se publican en
PDF con [`build_docs.py`](build_docs.py). El `.md` es la fuente; el PDF de
`pdf/` es la entrega.

## Contenido

| Documento | Archivo | Entrega |
|---|---|---|
| **Informe de PPS** | [`informe_pps.md`](informe_pps.md) | [`pdf/informe_pps.pdf`](pdf/) |
| **Cronograma** | [`cronograma.md`](cronograma.md) | [`pdf/cronograma.pdf`](pdf/) |
| **Diagrama de Gantt** | [`gantt.md`](gantt.md) · [`assets/gantt.png`](assets/) | incluido en el informe |
| **Manual de instalación** | [`manuales/manual_instalacion.md`](manuales/manual_instalacion.md) | [`pdf/manual_instalacion.pdf`](pdf/) |
| **Manual de usuario** | [`manuales/manual_usuario.md`](manuales/manual_usuario.md) | [`pdf/manual_usuario.pdf`](pdf/) |
| **Manual técnico** | [`manuales/manual_tecnico.md`](manuales/manual_tecnico.md) | [`pdf/manual_tecnico.pdf`](pdf/) |
| **Manual del corpus e ingesta** | [`manuales/manual_corpus.md`](manuales/manual_corpus.md) | [`pdf/manual_corpus.pdf`](pdf/) |

## Generar los PDF

```bash
python INFORMES/build_docs.py
```

Requiere Python 3 con el módulo `markdown` (`pip install markdown`) y Google
Chrome o Microsoft Edge instalados: la conversión a PDF usa el modo *headless*
del navegador, sin dependencias de LaTeX.

Opciones útiles:

```bash
python INFORMES/build_docs.py --solo informe_pps    # un documento
python INFORMES/build_docs.py --sin-diagramas       # omite Mermaid (mmdc)
```

## Cómo se arma la documentación

El cronograma y el Gantt **no son estimaciones a posteriori**: se derivan del
historial de commits del repositorio de código
([UNLZ_Llamacode_StudIA](https://github.com/MarcosDePalma/UNLZ_Llamacode_StudIA),
rama `feature/studia`). Cada tarea del Gantt corresponde a commits verificables;
las etapas previas al primer commit están marcadas como estimadas.

## Otros archivos a adjuntar

- Presentación de la defensa (`presentacion_defensa.pdf`).
- Planilla de horas / seguimiento con el tutor, si la cátedra la requiere.
- Actas o constancias de avance.
