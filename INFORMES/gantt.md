# Diagrama de Gantt — PPS StudIA

**Proyecto:** StudIA — Asistente de estudio sobre corpus académico
**Autor:** De Palma, Marcos Agustin · **Docente / Tutor:** Cristian Lukaszewicz
**Período:** junio – septiembre de 2026 · **Entrega:** 18/09/2026
**Carrera:** Ingeniería Mecatrónica (FI-UNLZ)

Este Gantt no es una estimación hecha a posteriori. Las etapas 3 a 5 se derivan del
historial de commits del repositorio de código
([UNLZ_Llamacode_StudIA](https://github.com/MarcosDePalma/UNLZ_Llamacode_StudIA),
rama `feature/studia`) y de los registros del repositorio local: cada tarea termina
en un commit verificable, con su fecha y su hash. Las etapas 1 y 2 son anteriores al
primer commit y están marcadas como **estimadas**.

---

## 1. Gantt general de la PPS

<!-- fig: gantt -->
```mermaid
gantt
    title StudIA — Plan general de la PPS (junio a septiembre de 2026)
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    tickInterval 1week
    weekday monday

    section 1 Definicion
    Definicion del tema y objetivos (est.)        :done, a1, 2026-06-01, 10d
    Relevamiento del problema y alternativas (est.) :done, a2, 2026-06-11, 12d
    Propuesta y alcance del modulo (est.)         :done, a3, 2026-06-23, 8d

    section 2 Corpus y entorno
    Recoleccion y organizacion del corpus (est.)  :done, b1, 2026-07-01, 16d
    Fork de UNLZ_Llamacode                        :milestone, m0, 2026-07-17, 0d
    Entorno de compilacion Qt QML y C++           :done, b2, 2026-07-17, 5d
    Estudio del codigo base y sus convenciones    :done, b3, 2026-07-22, 7d

    section 3 Desarrollo
    Ingesta del corpus e indice FTS5              :done, c0, 2026-07-25, 6d
    Diseno e integracion del modulo StudIA        :done, c1, 2026-07-29, 8d
    Prototipo funcional                           :milestone, m1, 2026-08-05, 0d
    Modos de tutor y reorganizacion en 4 clases   :done, c2, 2026-08-05, 2d
    Figuras OCR y exportacion a Anki              :done, c3, 2026-08-06, 1d
    Busqueda semantica con embeddings y RRF       :done, c4, 2026-08-06, 2d
    Multiconversacion por materia y ajustes de UI :done, c5, 2026-08-07, 1d
    Consignas por modo y formatos de salida       :done, c6, 2026-08-07, 2d
    Modulo funcional completo                     :milestone, m2, 2026-08-08, 0d

    section 4 Empaquetado
    Instalador Inno Setup y arranque autonomo     :done, d1, 2026-08-08, 6d
    Deteccion de dependencias y autodiagnostico   :done, d2, 2026-08-10, 4d
    Entrega instalable                            :milestone, m3, 2026-08-13, 0d
    Validacion en PC limpia y usuario nuevo       :done, d3, 2026-08-14, 7d

    section 5 Documentacion y cierre
    Manuales tecnicos y de usuario                :done, e1, 2026-08-21, 6d
    Informe cronograma y Gantt                    :active, e2, 2026-08-25, 6d
    Validacion en VM limpia y multimedia          :e3, 2026-08-31, 7d
    Revision con el tutor y correcciones          :e4, 2026-09-07, 7d
    Preparacion de la defensa                     :e5, 2026-09-14, 5d
    Entrega de la PPS                             :milestone, m4, 2026-09-18, 0d
```

---

## 2. Gantt de detalle — desarrollo del módulo (5 al 13 de agosto)

Las barras corresponden a la **ventana entre commits**, con la fecha y hora reales
registradas en el repositorio. No representan horas continuas de trabajo, sino el
tramo de calendario en el que se produjo cada entrega parcial.

<!-- fig: gantt_detalle -->
```mermaid
gantt
    title StudIA — Desarrollo del modulo, commit a commit
    dateFormat YYYY-MM-DD HH:mm
    axisFormat %d/%m %Hh

    section Iteraciones
    3da2c9b Primer prototipo funcional          :done, i1, 2026-08-05 00:00, 2026-08-05 14:06
    ad020b9 Reorganizacion y nuevas funciones   :done, i2, 2026-08-05 14:06, 2026-08-06 00:01
    910bb15 Ploteos OCR y export a Anki         :done, i3, 2026-08-06 00:01, 2026-08-06 03:58
    c42106c Busqueda semantica y abstencion     :done, i4, 2026-08-06 03:58, 2026-08-06 21:09
    0b1779d Temas por materia y graficador      :done, i5, 2026-08-06 21:09, 2026-08-07 00:47
    dc8c122 Personalidad en cada modo           :done, i6, 2026-08-07 00:47, 2026-08-07 20:34
    4065803 Instalador y arranque autonomo      :done, i7, 2026-08-07 20:34, 2026-08-13 12:35
```

---

## 3. Tabla de respaldo del Gantt

| # | Etapa / tarea | Inicio | Fin | Evidencia |
|---:|---|---|---|---|
| 1.1 | Definición del tema y objetivos | 01/06/2026 | 10/06/2026 | estimada |
| 1.2 | Relevamiento del problema y alternativas | 11/06/2026 | 22/06/2026 | estimada |
| 1.3 | Propuesta y alcance del módulo | 23/06/2026 | 30/06/2026 | estimada |
| 2.1 | Recolección y organización del corpus académico | 01/07/2026 | 16/07/2026 | estimada · corpus `DATA` (23 GB) |
| 2.2 | **Fork de `cristianlukas/UNLZ_Llamacode`** | 17/07/2026 | — | registro de clonado del repositorio |
| 2.3 | Entorno de compilación (Qt/QML + C++/CMake) | 17/07/2026 | 21/07/2026 | estimada sobre fechas de archivos |
| 2.4 | Estudio del código base y sus convenciones | 22/07/2026 | 28/07/2026 | estimada |
| 3.1 | Ingesta del corpus e índice FTS5 | 25/07/2026 | 30/07/2026 | `tools/studia/ingest.py` |
| 3.2 | Diseño e integración del módulo | 29/07/2026 | 05/08/2026 | commit `3da2c9b` |
| 3.3 | **Primer prototipo funcional** | 05/08/2026 | — | commit `3da2c9b` (18 arch., +3.312 líneas) |
| 3.4 | Modos de tutor y reorganización en 4 clases | 05/08/2026 | 06/08/2026 | commit `ad020b9` (21 arch., +3.375) |
| 3.5 | Figuras, OCR y exportación a Anki | 06/08/2026 | 06/08/2026 | commit `910bb15` (25 arch., +2.778) |
| 3.6 | Búsqueda semántica (embeddings + RRF) | 06/08/2026 | 06/08/2026 | commit `c42106c` (16 arch., +1.174) |
| 3.7 | Multiconversación por materia y ajustes de UI | 06/08/2026 | 07/08/2026 | commit `0b1779d` (14 arch., +1.573) |
| 3.8 | Consignas por modo y formatos de salida | 07/08/2026 | 07/08/2026 | commit `dc8c122` (10 arch., +1.624) |
| 4.1 | Instalador y arranque autónomo del servidor | 08/08/2026 | 13/08/2026 | commit `4065803` (26 arch., +1.796) |
| 4.2 | Detección de dependencias y autodiagnóstico | 10/08/2026 | 13/08/2026 | `StudiaHerramientas`, `instalar_dependencias.ps1` |
| 4.3 | **Entrega instalable** | 13/08/2026 | — | commit `4065803` |
| 4.4 | Validación en PC limpia y usuario nuevo | 14/08/2026 | 20/08/2026 | `installer/PROBAR_EN_PC_LIMPIA.md` |
| 5.1 | Manuales técnicos y de usuario | 21/08/2026 | 26/08/2026 | `INFORMES/manuales/` |
| 5.2 | Informe, cronograma, Gantt y diagramas | 25/08/2026 | 30/08/2026 | este repositorio |
| 5.3 | Validación en VM limpia, capturas y video | 31/08/2026 | 06/09/2026 | planificada |
| 5.4 | Revisión con el tutor y correcciones | 07/09/2026 | 13/09/2026 | planificada |
| 5.5 | Preparación de la defensa | 14/09/2026 | 18/09/2026 | planificada |
| 5.6 | **Entrega de la PPS** | 18/09/2026 | — | — |

---

## 4. Cómo regenerar la imagen

El Gantt está escrito en [Mermaid](https://mermaid.js.org/): GitHub lo renderiza
solo al abrir este archivo. Para obtener el PNG que se inserta en el informe:

```bash
npm install -g @mermaid-js/mermaid-cli
python INFORMES/build_docs.py          # regenera assets/gantt.png y los PDF
```

La imagen queda en [`assets/gantt.png`](assets/) y en
[`assets/gantt_detalle.png`](assets/).
