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

PEDIDO, PLAN10, PLAN20 = 125, 113, 100  # valor del crédito, plan de 3 meses (10%) y plan Mandioca (20%), en USD
MINIMO = 20                                 # créditos al mes en el plan = USD 2.000

# familia, imagen, ancla en la landing de IA, descripción, [(pieza, detalle, créditos)]
MENU = [
    ("Motion graphics con IA", "ejemplo-ionava-wallet.jpg", "#videos", "IA entrenada con la marca y motion graphics: tipografía en movimiento, íconos y pantallas. Para orgánico y pauta en Instagram y LinkedIn. Cada pieza incluye copy, música y se entrega en dos formatos, por ejemplo 9:16 y 1:1.", [
        ("Cápsula animada simple · corta", "Escenas simples con música, hasta 20 s.", 4),
        ("Cápsula animada simple · larga", "Escenas simples con música, de 30 a 60 s.", 8),
        ("Video explicativo de hasta 90 s", "Sobre un producto o servicio. Se entrega el video completo y, por separado, una cápsula por cada tema, para publicar sola. Key visual, guion, video vertical y horizontal, locución con IA, música y efectos.", 15),
    ]),
    ("Video generado con IA", "ref-louisville.jpg", "#videos", "Planos generados con IA: producto, acciones y escenas con personajes. Para orgánico y pauta en Instagram y LinkedIn. Cada pieza incluye copy, música y se entrega en dos formatos, por ejemplo 9:16 y 1:1.", [
        ("Video de hasta 30 s · simple", "Hasta 6 planos, cortes directos y gráficos 2D. Para mostrar producto o una acción.", 7),
        ("Video de hasta 60 s · avanzado", "Hasta 8 planos con personajes que interactúan con el producto, transiciones, efectos visuales y efectos de sonido.", 12),
    ]),
    ("Gráfica para redes", "grafica-redes.jpg", "", "Piezas sobre el key visual de la marca, con copy. Cada pieza incluye una adaptación.", [
        ("Pieza madre gráfica · simple", "Template de imagen y texto.", 1),
        ("Pieza madre gráfica · avanzada", "Ilustración o gráfica con más desarrollo de concepto.", 3),
        ("Carrusel de 4 slides", "Estático, con copy.", 3),
        ("Carrusel de 6 a 8 slides", "Con 1 o 2 slides animadas.", 5),
        ("Loop animado de 4 s · simple", "Gráfica simple animada en loop.", 3),
        ("Loop animado de 4 s · avanzado", "Gráfica avanzada animada en loop.", 4),
    ]),
    ("Avatares digitales", "yt:1yC-11vkWgE", "#avatares", "Avatar de una persona real de la empresa, con su voz, para presentaciones, videos explicativos y campañas.", [
        ("Configuración del avatar", "Grabación base de la persona, entrenamiento del avatar y clon de voz. Se suma una sola vez, al primer video.", 5),
        ("Video con avatar de hasta 30 s", "Guion, locución con la voz del avatar, edición con gráficos y subtítulos.", 6),
    ]),
    ("Edición con material de la marca", None, "", "La marca graba el material, por ejemplo al líder de la empresa, y Samsa lo edita con motion graphics, gráficos y textos, potenciado con IA. Si Samsa debe conseguir o producir el material, se cotiza por pedido. Todos los videos incluyen guion escrito con ustedes, portada y una adaptación.", [
        ("Video editado de hasta 45 s", "Guion, edición con motion graphics, textos y música.", 4),
        ("Video editado de 1 a 2 min", "Guion, edición con motion graphics, textos, transiciones y música.", 7),
        ("Video editado de 3 a 4 min", "Para presentaciones o videos institucionales. Guion, edición con motion graphics, textos, transiciones y música.", 10),
        ("Cápsula derivada de 30 a 45 s", "Un corte para redes de un video editado de 1 a 4 min.", 2),
    ]),
    ("Jingles con IA", None, "", "Audio para campañas, videos y redes.", [
        ("Jingle de hasta 30 s", "Letra, música y voz generadas con IA.", 4),
    ]),
]

LANDING = "https://anasamsa.github.io/samsa-inteligencia-artificial/"

def usd(n):
    return "USD " + f"{n:,.0f}".replace(",", ".")

def crs(c):
    return (f"{c:g}".replace(".", ",")) + " cr"

def media(img):
    """Video en loop si hay un .mp4 con el mismo nombre; si no, la imagen."""
    if img.startswith("yt:"):
        v = img[3:]
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{v}?autoplay=1&mute=1&loop=1&playlist={v}&controls=0&playsinline=1&rel=0" '
                'title="Reel Growie" referrerpolicy="strict-origin-when-cross-origin" allow="autoplay; encrypted-media; picture-in-picture"></iframe>')
    mp4 = Path(img).with_suffix(".mp4").name
    if (H / "img" / mp4).exists():
        return f'<video src="img/{mp4}" poster="img/{img}" autoplay muted loop playsinline aria-hidden="true"></video>'
    return f'<img src="img/{img}" alt="" loading="lazy">'

def menu_html():
    out = []
    for fam, img, anchor, desc, items in MENU:
        link = f'<a href="{LANDING}" target="_blank" rel="noopener">Ver trabajos →</a>' if anchor else ""
        rows = "".join(
            f'<div class="row"><div><b>{t}</b><small>{d}</small></div><span class="cr">{crs(c)}</span>'
            f'<span>{usd(c*PEDIDO)}</span><span class="pl">{usd(c*PLAN20)}</span></div>'
            for t, d, c in items)
        out.append(
            '<article class="fam">'
            + (f'<div class="fam__in"><div class="fam__img">{media(img)}</div>' if img else '<div class="fam__in fam--noimg">') +
            f'<div class="fam__body"><div class="fam__h"><h3>{fam}</h3>{link}</div><p class="fam__d">{desc}</p>'
            f'<div class="rows"><div class="rows__h"><span>Pieza</span><span>Créditos</span><span>Valor por pedido</span><span>Plan Mandioca</span></div>{rows}</div></div></div></article>')
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
