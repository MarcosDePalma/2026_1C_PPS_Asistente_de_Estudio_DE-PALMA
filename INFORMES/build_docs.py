#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los PDF de la documentacion de la PPS a partir de los .md.

El .md es la fuente (versionable y diffeable); el PDF es la entrega. La conversion
usa el modo headless de Chrome o Edge, asi que no hace falta LaTeX ni pandoc: en
Windows ya hay un navegador instalado.

    python INFORMES/build_docs.py                 todo
    python INFORMES/build_docs.py --solo informe_pps
    python INFORMES/build_docs.py --sin-diagramas  no llama a mmdc

Requiere:  pip install markdown
Opcional:  npm install -g @mermaid-js/mermaid-cli   (para los bloques ```mermaid```)
"""

import argparse
import base64
import hashlib
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Falta el modulo 'markdown'.  Instalalo con:  pip install markdown")

AQUI = Path(__file__).resolve().parent          # INFORMES/
RAIZ = AQUI.parent                              # raiz del repo de la PPS
ASSETS = AQUI / "assets"
SALIDA = AQUI / "pdf"

# Documentos a generar.  'secciones_en_pagina_nueva' arranca cada ## en una hoja:
# tiene sentido en el informe y no en los manuales, que son mas cortos.
DOCUMENTOS = [
    {"md": AQUI / "informe_pps.md",                     "secciones_en_pagina_nueva": True},
    {"md": AQUI / "cronograma.md",                      "secciones_en_pagina_nueva": False},
    {"md": AQUI / "gantt.md",                           "secciones_en_pagina_nueva": False},
    {"md": AQUI / "manuales" / "manual_instalacion.md", "secciones_en_pagina_nueva": False},
    {"md": AQUI / "manuales" / "manual_usuario.md",     "secciones_en_pagina_nueva": False},
    {"md": AQUI / "manuales" / "manual_tecnico.md",     "secciones_en_pagina_nueva": False},
    {"md": AQUI / "manuales" / "manual_corpus.md",      "secciones_en_pagina_nueva": False},
]

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }

html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: Cambria, Georgia, "Times New Roman", serif;
  font-size: 10.5pt; line-height: 1.5; color: #1c2333; margin: 0;
  text-align: justify; hyphens: auto;
}

h1, h2, h3, h4 {
  font-family: "Segoe UI", Calibri, Arial, sans-serif;
  color: #0b3d91; line-height: 1.25; text-align: left;
  break-after: avoid-page; page-break-after: avoid;
}
h1 { font-size: 21pt; margin: 0 0 .3em; }
h2 { font-size: 15pt; margin: 1.6em 0 .5em; padding-bottom: .18em;
     border-bottom: 1.5px solid #d5dbe6; }
h3 { font-size: 12pt; margin: 1.2em 0 .35em; color: #1f4e9c; }
h4 { font-size: 10.5pt; margin: 1em 0 .3em; color: #3a4a63; }

p { margin: .5em 0; orphans: 2; widows: 2; }
ul, ol { margin: .5em 0 .5em 1.1em; padding-left: .6em; }
li { margin: .22em 0; }
a { color: #1f6feb; text-decoration: none; word-break: break-word; }
strong { color: #101828; }

hr { border: none; border-top: 1px solid #d5dbe6; margin: 1.6em 0; }

table {
  width: 100%; border-collapse: collapse; margin: .9em 0; font-size: 9.2pt;
  break-inside: auto; text-align: left;
}
thead { display: table-header-group; }
tr { break-inside: avoid; page-break-inside: avoid; }
th {
  background: #0b3d91; color: #fff; font-family: "Segoe UI", Calibri, sans-serif;
  font-weight: 600; text-align: left; padding: .42em .6em; border: 1px solid #0b3d91;
}
td { padding: .38em .6em; border: 1px solid #ccd4e0; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f4f6fa; }

code {
  font-family: Consolas, "Courier New", monospace; font-size: 9pt;
  background: #eef1f7; padding: .1em .3em; border-radius: 3px; color: #0b3d91;
}
pre {
  background: #f4f6fa; border: 1px solid #d5dbe6; border-left: 3px solid #1f6feb;
  border-radius: 4px; padding: .7em .9em; overflow-x: auto; font-size: 8.8pt;
  line-height: 1.4; break-inside: avoid; page-break-inside: avoid; text-align: left;
}
pre code { background: none; padding: 0; color: #17233b; }

blockquote {
  margin: .9em 0; padding: .5em .9em; background: #f4f6fa;
  border-left: 3px solid #f6c343; color: #33415c; break-inside: avoid;
}
blockquote p { margin: .25em 0; }

img {
  display: block; margin: 1em auto; max-width: 100%; max-height: 20cm;
  break-inside: avoid; page-break-inside: avoid;
}

/* Portada: todo lo que va antes del primer separador. */
.portada {
  break-after: page; page-break-after: always;
  display: flex; flex-direction: column; justify-content: center;
  min-height: 24cm; text-align: center;
}
.portada img { max-width: 11cm; margin: 0 auto 1.6em; }
.portada h1 { font-size: 27pt; text-align: center; margin-bottom: .25em; }
.portada h2 { font-size: 14pt; border: none; color: #33415c; text-align: center;
              margin-top: 0; font-weight: 500; }
.portada p { text-align: center; font-size: 11pt; color: #33415c; }
.portada table { font-size: 9.5pt; margin: 2em auto 0; max-width: 16cm; }
/* La tabla de datos de la portada no tiene encabezados: la fila vacia se oculta. */
.portada thead { display: none; }
.portada td:first-child { width: 32%; font-weight: 600; }
"""

CSS_SECCIONES = """
.cuerpo h2 { break-before: page; page-break-before: always; }
.cuerpo > h2:first-of-type { break-before: auto; page-break-before: auto; }
"""


# ── Mermaid ──────────────────────────────────────────────────────────────────

def render_mermaid(codigo, nombre, mmdc):
    """Renderiza un bloque mermaid a PNG en assets/ y devuelve la ruta."""
    ASSETS.mkdir(parents=True, exist_ok=True)
    salida = ASSETS / f"{nombre}.png"
    with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False,
                                     encoding="utf-8") as f:
        f.write(codigo)
        tmp = f.name
    try:
        r = subprocess.run([mmdc, "-i", tmp, "-o", str(salida), "-b", "white",
                            "-s", "2", "--quiet"],
                           capture_output=True, text=True, shell=(os.name == "nt"))
        if r.returncode != 0 or not salida.exists():
            print(f"   ! mermaid fallo en '{nombre}': {r.stderr.strip()[:200]}")
            return None
        return salida
    finally:
        os.unlink(tmp)


def extraer_mermaid(md, doc_stem, mmdc):
    """Cambia los bloques ```mermaid``` por imagenes ya renderizadas.

    El nombre del PNG sale de un comentario '<!-- fig: nombre -->' arriba del
    bloque, para que las rutas citadas en el texto no dependan del orden.
    """
    if not mmdc:
        return re.sub(r"<!-- fig:.*?-->\s*", "", md)

    contador = [0]

    def reemplazo(m):
        nombre = m.group("nombre")
        if not nombre:
            contador[0] += 1
            nombre = f"{doc_stem}_diagrama{contador[0]}"
        png = render_mermaid(m.group("codigo"), nombre.strip(), mmdc)
        if not png:
            return m.group(0)
        print(f"   · diagrama {png.name}")
        rel = os.path.relpath(png, AQUI).replace("\\", "/")
        return f"![{nombre}](/{rel})"   # ruta absoluta al repo, se resuelve luego

    patron = re.compile(
        r"(?:<!--\s*fig:\s*(?P<nombre>[\w-]+)\s*-->\s*)?"
        r"```mermaid\n(?P<codigo>.*?)```",
        re.DOTALL)
    return patron.sub(reemplazo, md)


# ── Imagenes ─────────────────────────────────────────────────────────────────

def incrustar_imagenes(html, base):
    """Pasa las imagenes locales a data URI: el PDF queda autocontenido."""
    def reemplazo(m):
        src = m.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        ruta = (AQUI / src[1:]) if src.startswith("/") else (base / src)
        ruta = ruta.resolve()
        if not ruta.exists():
            print(f"   ! falta la imagen {src}")
            return m.group(0)
        tipo = mimetypes.guess_type(ruta.name)[0] or "image/png"
        datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
        return m.group(0).replace(src, f"data:{tipo};base64,{datos}")

    return re.sub(r'<img[^>]*src="([^"]+)"', reemplazo, html)


# ── Conversion ───────────────────────────────────────────────────────────────

def saltos_en_portada(md):
    """En la portada cada renglon es un renglon.

    El resto del documento va con parrafos plegados a 85 columnas, asi que no se
    puede activar nl2br en todo: los renglones de la portada llevan el salto
    explicito de Markdown (dos espacios al final).
    """
    partes = md.split("\n---\n", 1)
    if len(partes) != 2:
        return md
    lineas = partes[0].split("\n")
    for i, l in enumerate(lineas[:-1]):
        if l.strip() and lineas[i + 1].strip() and not l.endswith("  "):
            lineas[i] = l + "  "
    return "\n".join(lineas) + "\n---\n" + partes[1]


def a_html(md_texto, titulo, secciones_en_pagina_nueva):
    cuerpo = markdown.markdown(
        saltos_en_portada(md_texto),
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
    )
    # Portada = todo lo anterior al primer <hr>.
    partes = cuerpo.split("<hr />", 1)
    if len(partes) == 2:
        cuerpo = (f'<div class="portada">{partes[0]}</div>'
                  f'<div class="cuerpo">{partes[1]}</div>')
    else:
        cuerpo = f'<div class="cuerpo">{cuerpo}</div>'

    css = CSS + (CSS_SECCIONES if secciones_en_pagina_nueva else "")
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<title>{titulo}</title><style>{css}</style></head>'
            f'<body>{cuerpo}</body></html>')


def a_pdf(html_path, pdf_path, navegador):
    perfil = Path(tempfile.gettempdir()) / ("perfil_pdf_" +
             hashlib.md5(str(html_path).encode()).hexdigest()[:8])
    cmd = [navegador, "--headless", "--disable-gpu", "--no-sandbox",
           f"--user-data-dir={perfil}",
           "--no-pdf-header-footer",
           f"--print-to-pdf={pdf_path}",
           html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    shutil.rmtree(perfil, ignore_errors=True)
    if not pdf_path.exists():
        print(r.stderr[-600:])
        return False
    return True


def main():
    ap = argparse.ArgumentParser(description="Genera los PDF de la PPS")
    ap.add_argument("--solo", help="nombre del documento sin extension")
    ap.add_argument("--sin-diagramas", action="store_true",
                    help="no renderiza los bloques mermaid")
    args = ap.parse_args()

    navegador = next((n for n in NAVEGADORES if Path(n).exists()), None)
    if not navegador:
        sys.exit("No se encontro Chrome ni Edge. Instalá alguno o generá el HTML a mano.")

    mmdc = None if args.sin_diagramas else (shutil.which("mmdc") or shutil.which("mmdc.cmd"))
    if not mmdc and not args.sin_diagramas:
        print("! mmdc no esta instalado: los diagramas mermaid quedan como texto.")
        print("  npm install -g @mermaid-js/mermaid-cli\n")

    SALIDA.mkdir(parents=True, exist_ok=True)
    docs = [d for d in DOCUMENTOS
            if not args.solo or d["md"].stem == args.solo]
    if not docs:
        sys.exit(f"No hay ningun documento llamado '{args.solo}'.")

    ok = 0
    for doc in docs:
        md_path = doc["md"]
        if not md_path.exists():
            print(f"! falta {md_path.name}")
            continue
        print(f"-> {md_path.name}")
        texto = md_path.read_text(encoding="utf-8")
        texto = extraer_mermaid(texto, md_path.stem, mmdc)
        titulo = next((l.lstrip("# ").strip() for l in texto.splitlines()
                       if l.startswith("# ")), md_path.stem)
        html = a_html(texto, titulo, doc["secciones_en_pagina_nueva"])
        html = incrustar_imagenes(html, md_path.parent)

        html_path = Path(tempfile.gettempdir()) / f"{md_path.stem}.html"
        html_path.write_text(html, encoding="utf-8")
        pdf_path = SALIDA / f"{md_path.stem}.pdf"
        if a_pdf(html_path, pdf_path, navegador):
            print(f"   OK  {pdf_path.relative_to(RAIZ)}  "
                  f"({pdf_path.stat().st_size/1024:.0f} KB)")
            ok += 1
        else:
            print(f"   ERROR generando {pdf_path.name}")
        html_path.unlink(missing_ok=True)

    print(f"\n{ok}/{len(docs)} documentos generados en {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
