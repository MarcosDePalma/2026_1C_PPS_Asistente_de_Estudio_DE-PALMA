# Código

El desarrollo de **StudIA** se encuentra en el siguiente repositorio:

### 👉 [MarcosDePalma/UNLZ_Llamacode_StudIA](https://github.com/MarcosDePalma/UNLZ_Llamacode_StudIA)

El proyecto parte de [cristianlukas/UNLZ_Llamacode](https://github.com/cristianlukas/UNLZ_Llamacode)
y agrega el módulo de asistencia al estudio desarrollado para esta PPS.

---

## Por qué el código no está acá

El código vive en su propio repositorio por dos razones:

1. **Trazabilidad.** StudIA es un *fork*: lo que aporta esta PPS se lee como la
   diferencia entre el fork y el repositorio original. Copiar los archivos acá
   perdería esa diferencia y con ella la evidencia de qué se desarrolló.
2. **Separación de responsabilidades.** Este repositorio documenta la PPS —qué se
   hizo, por qué, con qué metodología y con qué resultados—. El repositorio de
   StudIA contiene: código fuente y su evolución a través del historial de commits.


## Qué se agregó

| Ubicación en el repo de código | Contenido |
|---|---|
| `src/core/studia/` | Módulo core en C++: índice y recuperación, prompts, sesiones, embeddings, gráficos, texto/fórmulas, detección de herramientas. |
| `qml/pages/StudiaPage.qml` | Interfaz de StudIA (selector de materia, modos de tutor, citas, figuras). |
| `qml/components/StudiaTemas.qml` | Conversaciones múltiples por materia. |
| `tools/studia/` | Herramientas Python: ingesta del corpus, vectorización, OCR, graficador, auditoría del índice, instalador de dependencias. |
| `tests/test_studia.cpp` + `tools/studia/test_*.py` | Suites de prueba del módulo. |
| `installer/` | Empaquetado con Inno Setup y distribución del corpus. |

**Volumen del aporte:** 55 archivos, ~14.700 líneas agregadas sobre el código base.


