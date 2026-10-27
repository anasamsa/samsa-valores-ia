"""Valores de los servicios de IA de Samsa.
Usa los estilos de la landing de IA (../Landing Servicios IA/landing) + _valores.css.
El menú de piezas vive en MENU: de ahí salen las tablas por familia y la calculadora.
_body.html -> artifact.html (para revisar en Claude) e index.html (GitHub Pages)."""
import json
from pathlib import Path

H = Path(__file__).parent
L = H.parent / "Landing Servicios IA" / "landing"
css = "\n".join((L / f).read_text() for f in ("_base.css", "_ia.css", "_show.css")) + "\n" + (H / "_valores.css").read_text()
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap">\n'

PEDIDO, PLAN15, PLAN20 = 100, 85, 80  # valor del crédito en USD
MINIMO = 25                            # créditos al mes en el plan

# familia, imagen, ancla en la landing de IA, descripción, [(pieza, detalle, créditos)]
MENU = [
    ("Videos explicativos", "ref-natura-referidos.jpg", "#videos", "Un video de hasta 90 s dividido en cápsulas por tema. Incluye key visual, guion, video vertical y horizontal, locución con IA, música, efectos y dos rondas de ajustes.", [
        ("Video de hasta 90 s · Nivel 1 · Motion graphics con IA entrenada", "IA entrenada con la marca y motion graphics: tipografía en movimiento, íconos y pantallas.", 25),
        ("Video de hasta 90 s · Nivel 2 · Premium con IA generativa", "Motion graphics con personajes, ilustraciones y escenas generados con IA.", 34),
        ("Cápsula de 10 a 20 s · Nivel 1", "Motion graphics sobre el key visual.", 3),
        ("Cápsula de 10 a 20 s · Nivel 2", "Con personajes y escenas generados con IA.", 5),
    ]),
    ("Avatares digitales", "mariana.jpg", "#avatares", "Avatar de una persona real de la empresa, con su voz, para presentaciones, videos explicativos y campañas.", [
        ("Creación del avatar", "Grabación base de la persona, entrenamiento del avatar y clon de voz. Se paga una vez.", 10),
        ("Video con avatar de hasta 60 s", "Guion, locución con la voz del avatar, edición con gráficos y subtítulos.", 8),
        ("Video con avatar adicional", "Mismo formato con un guion nuevo.", 4),
    ]),
    ("Adaptaciones", "reel-bg.jpg", "", "Versiones de una pieza ya aprobada.", [
        ("Versión en otro idioma de un video de hasta 90 s", "Traducción, voz con IA, sincronía de labios y subtítulos.", 3),
        ("Formato adicional de un video", "Por ejemplo 1:1 o 4:5, además del vertical y el horizontal.", 1),
        ("Adaptación de una pieza gráfica", "Otro formato o medida de una pieza madre.", 0.5),
    ]),
    ("Imagen con IA", "ppt-retrato-ia.jpg", "#imagen", "A partir de fotos reales, con fidelidad al producto y a la persona.", [
        ("Imágenes de producto · 6 imágenes", "Producto en escenas y ambientes nuevos.", 5),
        ("Retratos a partir de una foto real · 6 imágenes", "La misma persona en otros escenarios y vestuarios.", 5),
    ]),
    ("Gráfica para redes", "fruti-key.jpg", "", "Piezas sobre el key visual de la marca.", [
        ("Pieza madre gráfica · simple", "Gráfica con copy. Incluye 1 adaptación.", 1),
        ("Pieza madre gráfica · avanzada", "Ilustración o tratamiento especial. Incluye 1 adaptación.", 2),
        ("Carrusel de 3 a 5 slides", "Estático, con copy.", 2),
        ("Loop animado de 4 s", "Gráfica animada en loop.", 2),
    ]),
    ("Personajes y audio", "ppt-stout.jpg", "#personajes", "Personajes propiedad de la marca y audio generado con IA.", [
        ("Concept del universo y primer personaje", "Model sheet, expresiones y poses.", 20),
        ("Personaje adicional", "Mismo universo visual.", 10),
        ("Imágenes con personaje · 6 imágenes", "Con el personaje de la marca.", 5),
        ("Jingle con IA de hasta 30 s", "Letra, música y voz.", 4),
    ]),
]

LANDING = "https://anasamsa.github.io/samsa-inteligencia-artificial/"

def usd(n):
    return "USD " + f"{n:,.0f}".replace(",", ".")

def crs(c):
    return (f"{c:g}".replace(".", ",")) + " cr"

def menu_html():
    out = []
    for fam, img, anchor, desc, items in MENU:
        link = f'<a href="{LANDING}" target="_blank" rel="noopener">Ver trabajos →</a>' if anchor else ""
        rows = "".join(
            f'<div class="row"><div><b>{t}</b><small>{d}</small></div><span class="cr">{crs(c)}</span>'
            f'<span>{usd(c*PEDIDO)}</span><span class="pl">{usd(c*PLAN20)}</span></div>'
            for t, d, c in items)
        out.append(
            f'<article class="fam"><div class="fam__img"><img src="img/{img}" alt="" loading="lazy"></div>'
            f'<div class="fam__body"><div class="fam__h"><h3>{fam}</h3>{link}</div><p class="fam__d">{desc}</p>'
            f'<div class="rows"><div class="rows__h"><span>Pieza</span><span>Créditos</span><span>Por pedido</span><span>Con el plan</span></div>{rows}</div></div></article>')
    return "\n".join(out)

calc = [[fam, t, d, c] for fam, _, _, _, items in MENU for t, d, c in items]
body = ((H / "_body.html").read_text()
        .replace("{{MENU}}", menu_html())
        .replace("{{CALC}}", json.dumps(calc, ensure_ascii=False)))

title = "Samsa · Valores IA"
desc = "Valores de los servicios de IA de Samsa Creative: precio por pedido y plan de créditos de 3 meses."
head = (f'<title>{title}</title>\n<meta name="robots" content="noindex">\n<meta name="description" content="{desc}">\n'
        + FONT + f'<style>\n{css}\n</style>\n')
(H / "artifact.html").write_text('<meta name="claude:viewport-fit-sides" content="cover">' + head + body)
(H / "index.html").write_text('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
print("ok")
