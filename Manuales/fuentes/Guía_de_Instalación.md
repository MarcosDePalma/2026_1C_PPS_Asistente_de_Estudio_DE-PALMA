# Guía de Instalación — StudIA

**Versión:** 1.0 · **Fecha:** 18/09/2026
**Proyecto:** StudIA — Asistente de estudio sobre corpus académico (PPS · FI-UNLZ)

Este manual cubre las dos formas de poner StudIA en funcionamiento: **instalación
desde el instalador** (para usar el sistema) y **compilación desde el código fuente**
(para desarrollarlo o corregirlo).

---

## 1. Requisitos

### 1.1 Sistema

| | Mínimo | Recomendado |
|---|---|---|
| Sistema operativo | Windows 10 64 bits | Windows 11 64 bits |
| RAM | 8 GB | 16 GB |
| Disco (aplicación + modelo de embeddings) | 2 GB | 3 GB |
| Disco (índice `studia.db`) | 0,9 GB | 0,9 GB |
| Disco (documentos `DATA_StudIA`, opcional) | — | 6 GB |
| Disco (modelo de lenguaje, se descarga aparte) | 3 GB | 8 GB |
| GPU | no requerida | NVIDIA con 6 GB+ de VRAM |

En total conviene tener unos **10 GB libres**. Sin GPU el sistema funciona, pero el
modelo de chat responde más lento.

### 1.2 Dependencias externas

StudIA **funciona sin ninguna de estas**: el chat, la búsqueda, las citas y los modos
andan igual. Lo que se apaga son funciones puntuales:

| Dependencia | Qué habilita | Si falta |
|---|---|---|
| **Python 3** + librerías | Sumar bibliografía propia; herramientas de ingesta | El botón 📎 no procesa documentos |
| **matplotlib** | Gráficos de funciones | El gráfico se muestra como texto |
| **Node.js + mermaid-cli** | Diagramas | El diagrama se muestra como texto |
| **Tesseract** (con español) | OCR de PDF escaneados | Esos documentos no se pueden indexar |
| **Runtime de Visual C++** | Ejecución de `llama-server.exe` | El servidor del modelo muere al arrancar |

La aplicación **detecta cuáles faltan**, indica qué función se pierde en cada caso y
ofrece instalarlas con un clic. También se pueden instalar a mano (§3).

---

## 2. Instalación desde el instalador

### 2.1 Instalar la aplicación

1. Ejecutar **`StudIA-1.0-Setup.exe`** (≈ 0,59 GB).
2. Aceptar la carpeta de destino propuesta o elegir otra.
3. Finalizar.

**No requiere permisos de administrador:** instala para el usuario actual. La ruta
elegida queda registrada en `HKA\Software\StudIA\InstallDir`.

El instalador incluye:

| Contenido | Ubicación tras instalar |
|---|---|
| Aplicación (LlamaCode + StudIA) | carpeta de instalación |
| Modelo de embeddings (bge-m3) | `<instalación>\StudIA\modelos\` |
| Script de dependencias | `<instalación>\StudIA\` |
| `Instrucciones de instalación.txt` | carpeta de instalación y menú de inicio |

> **El material de estudio no viene adentro.** Un `.exe` de Windows no puede superar los
> 4,2 GB y el material los excede. Además el programa y el índice cambian a ritmos
> distintos —el índice sólo cuando se reindexa—, así que actualizar uno no obliga a
> rehacer el otro. Viaja aparte: ver §2.3.

### 2.2 Instalar las dependencias

Desde la propia aplicación, cuando avisa que faltan herramientas, o a mano:

```
<instalación>\StudIA\instalar_dependencias.bat
```

Instala Python con sus librerías, Node.js con mermaid-cli, Tesseract con el paquete de
español y el runtime de Visual C++. Es **idempotente**: correrlo dos veces no
reinstala nada.

Para ver qué falta sin instalar:

```powershell
.\instalar_dependencias.ps1 -SoloRevisar
```

### 2.3 Copiar el material de estudio

El material viaja aparte del instalador, en una carpeta con dos cosas adentro:

| Contenido | Qué es | ¿Hace falta? |
|---|---|---|
| `studia.db` | El índice: el texto de todos los apuntes | Sí |
| `DATA_StudIA` | Los PDF originales (5,93 GB) | Sólo para abrir el PDF desde una cita |

Copiar esa carpeta a donde se quiera —disco interno, externo o pendrive— **sin separar
sus dos partes**. Esa es la única condición: al elegir el `studia.db` desde la
aplicación (§2.4), de esa misma ruta sale también dónde están los documentos, porque se
buscan en la carpeta `DATA_StudIA` hermana del índice.

No hay scripts de copiado, ni rutas fijas, ni una segunda ubicación que registrar.

> Copiando sólo el `studia.db`, StudIA responde igual y sigue indicando de qué apunte y
> qué página salió cada afirmación. Lo único que se pierde es que la cita abra el PDF.

### 2.4 Primera ejecución

1. Abrir **StudIA** desde el menú de inicio.

2. **Descargar un modelo de lenguaje.** No viene con el instalador: son varios GB y
   conviene elegir el que le sirva a cada placa. Desde la página de perfiles:

   | Placa de video | Perfil |
   |---|---|
   | 8 GB | `[general] 8GB - Gemma 4 12B` (recomendado) |
   | 4 GB | `[general] 4GB - Gemma 4 E4B` |
   | 2 GB | `[general] 2GB - Gemma 4 E2B` |
   | sin placa | `[general] 0GB CPU - Qwen3.5 4B` (lento) |

3. **Arrancar el servidor y esperar.** Tarda unos 30 segundos en cargar el modelo. El
   cuadro de texto se habilita antes de que termine: preguntar en ese rato devuelve
   `[error: Connection refused]`. No está roto —hay que esperar y volver a preguntar—.

4. Ir a la sección **🎓 StudIA**, apretar **Abrir índice** y elegir el `studia.db` de la
   carpeta copiada en §2.3. Queda recordado: no hay que repetirlo.

5. Elegir una materia y preguntar.

El servidor de embeddings se levanta solo al abrir la aplicación y se cierra al salir.

### 2.5 Desinstalación

Panel de control → *Aplicaciones* → **StudIA** → Desinstalar.

Si el material quedó **dentro** de la carpeta del programa, el desinstalador borra el
`studia.db` y `DATA_StudIA` para no dejar varios GB huérfanos que después nadie
encuentra. Si se copió a otro lado —lo recomendado— no se toca: hay que borrarlo a mano
si ya no se usa.

---

## 3. Instalación manual de dependencias

Si se prefiere no usar el script:

```powershell
# Python 3 (o desde python.org marcando "Add to PATH")
winget install --id Python.Python.3.12 --source winget

# Librerías: extracción de texto, gráficos y OCR
pip install pypdf python-docx python-pptx openpyxl numpy matplotlib pypdfium2 pytesseract

# Node.js y mermaid-cli para los diagramas
winget install --id OpenJS.NodeJS.LTS --source winget
npm install -g @mermaid-js/mermaid-cli

# Tesseract con español
winget install --id UB-Mannheim.TesseractOCR --source winget

# Runtime de Visual C++ (lo necesita llama-server.exe)
winget install --id Microsoft.VCRedist.2015+.x64 --source winget
```

> Después de instalar algo que modifica el `PATH`, **cerrar y volver a abrir la
> consola**: el `PATH` de un proceso ya iniciado no se actualiza solo.

---

## 4. Compilación desde el código fuente

### 4.1 Requisitos de desarrollo

| Herramienta | Versión |
|---|---|
| Visual Studio 2022 | con *Desktop development with C++* |
| Qt | 6.x (Quick / QML) |
| CMake | 3.21 o superior |
| Git | cualquiera |
| Python 3 | para las herramientas y sus pruebas |

### 4.2 Obtener el código

```bash
git clone https://github.com/MarcosDePalma/UNLZ_Llamacode_StudIA.git
cd UNLZ_Llamacode_StudIA
git checkout feature/studia
```

### 4.3 Compilar y probar

```bash
build.bat Release      # compila la aplicación
tests.bat Release      # compila y corre la suite completa
```

**La condición para dar por buena una modificación es build más suite en verde.** Si
la máquina no tiene Python, las suites en Python se omiten y el resto igual corre.

### 4.4 Preparar el índice

La aplicación necesita un `studia.db`. Para generarlo a partir de un corpus propio, ver
**Vectorizar_Nuevo_Corpus**:

```bash
python tools/studia/ingest.py --corpus "D:\FACULTAD\DATA" --db "D:\StudIA\studia.db"
python tools/studia/vectorizar.py --db "D:\StudIA\studia.db" --url http://127.0.0.1:8081
```

### 4.5 Generar el instalador

Requiere [Inno Setup](https://jrsoftware.org/isinfo.php) instalado.

```
installer\compilar.bat
```

Genera `dist\StudIA-1.0-Setup.exe`. El script copia además el runtime de MSVC junto al
ejecutable —sin eso la aplicación no abre en una PC sin Visual Studio— y actualiza los
scripts empaquetados con la versión del repositorio.

El instalador **no incluye el índice**: se arma sólo con la aplicación, el modelo de
embeddings y las dependencias. El `studia.db` y `DATA_StudIA` se entregan aparte (§2.3).

---

## 5. Verificación de la instalación

| Comprobación | Resultado esperado |
|---|---|
| La aplicación abre y muestra la sección 🎓 StudIA | ✅ |
| El selector de materias lista las asignaturas | el índice se encontró |
| Una pregunta sobre un tema del material devuelve respuesta con citas | recuperación operativa |
| Una pregunta ajena al material devuelve la respuesta de abstención | control de abstención operativo |
| El aviso de herramientas no reporta faltantes | dependencias completas |
| Un click en una cita abre el documento | `DATA_StudIA` está junto al `studia.db` |

---

## 6. Problemas frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| La aplicación no abre, error de DLL | Falta el runtime de MSVC | Instalarlo (§3) |
| LlamaCode abre pero el servidor del modelo muere sin mensaje | Falta el runtime de Visual C++ para `llama-server.exe` | Ídem: el ejecutable vive en otra carpeta y no ve las copias locales |
| `[error: Connection refused]` al preguntar | El modelo todavía se está cargando | Esperar a que el servidor avise que está listo (~30 s) y volver a preguntar |
| «Abrí un índice para empezar» | No se eligió el `studia.db` | Botón **Abrir índice** (§2.4) |
| El selector de materias aparece vacío | No se encuentra el índice | Verificar que se haya abierto el `studia.db` correcto |
| StudIA se abstiene siempre | El índice está vacío o es de otro corpus | Re-indexar y recalibrar el umbral |
| Las citas no abren el documento | `DATA_StudIA` falta o quedó separada del `studia.db` | Ponerlas en la misma carpeta y volver a elegir el índice |
| La búsqueda parece ignorar sinónimos | Falta el modelo de embeddings | Verificar `<instalación>\StudIA\modelos\` |
| El botón 📎 no procesa | Falta Python | `instalar_dependencias.bat` |

---

## 7. Validación en una PC limpia

El instalador se verificó en la máquina de desarrollo y con un **usuario nuevo de
Windows**, que reproduce el estado de perfiles y configuración de una instalación
limpia sin instalar nada:

```
Configuración → Cuentas → Otros usuarios → Agregar cuenta
→ "No tengo los datos de esta persona" → "Agregar un usuario sin cuenta Microsoft"
```

Eso detecta rutas que apuntan a la carpeta personal del desarrollador, configuración
que se creía por defecto y perfiles duplicados. **No** detecta lo que se instala a
nivel de máquina (Python, Node, Tesseract, runtime de Visual C++), que ya está presente
en el equipo de desarrollo. Para eso hace falta una máquina virtual: el procedimiento
completo está en `installer/PROBAR_EN_PC_LIMPIA.md` del repositorio de código.
