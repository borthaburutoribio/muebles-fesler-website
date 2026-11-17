"""Procesa las fotos de assets/raw -> assets/img (webp, nombres descriptivos).
Correr desde la carpeta del sitio:  python -I _build/fotos.py
"""
from PIL import Image, ImageOps, ImageDraw
import os

RAW = 'assets/raw'
OUT = 'assets/img'
os.makedirs(OUT, exist_ok=True)


def crop(src, name, w, h, cx=0.5, cy=0.5, q=80):
    im = Image.open(os.path.join(RAW, src)).convert('RGB')
    im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(cx, cy))
    im.save(os.path.join(OUT, name + '.webp'), 'WEBP', quality=q, method=6)


# --- Productos (4:5) ---
P = {
    # cocina
    'freidora-de-aire-liliana-duofry': ('ig-DavGmwYFQKX.jpg', .5, .5),
    'multiprocesadora-liliana-digipros': ('ig-Da0DdX8FURG.jpg', .5, .5),
    'cafetera-oster-8-tazas': ('ig-DY2wNjQD5Ku.jpg', .5, .5),
    'sandwichera-oster': ('ig-DY2wkIRDxwh.jpg', .5, .5),
    'horno-de-pan-atma': ('ig-Dbf9epglTCS.jpg', .5, .5),
    'cocina-florencia-5818': ('ig-DZ7eyBwlZuz.jpg', .5, .5),
    # lavadero y limpieza
    'lavarropas-tcl-effiwash-11-kg': ('ig-DbDpTgwFaMe.jpg', .5, .5),
    'lavasecarropas-electrolux-lsc11': ('ig-DbYNZ36le-p.jpg', .5, .5),
    'lavasecarropas-smartlife-slim': ('ig-DZh9TXIlTCI.jpg', .5, .5),
    'aspiradora-midea-directcyclone': ('ig-DeH8r2dj1fk.jpg', .5, .5),
    'aspiradora-robot-smartlife': ('ig-DYUiIH9Ixv3.jpg', .5, .5),
    'aspiradora-liliana-zuma-2-en-1': ('ig-Dd91lGID3pv.jpg', .5, .5),
    # living
    'tv-philips-70-ambilight': ('ig-DZ5GTJEFd9I.jpg', .5, .5),
    'tv-tcl-p8k-qled-65': ('ig-DY7F6X3lVPp.jpg', .5, .5),
    'biblioteca-kanazawa-linea-kyoto': ('ig-DbT0W3zDw2d.jpg', .5, .5),
    'bahiut-gammel-blanco-roble': ('ig-DbT0HZHj_7t.jpg', .5, .5),
    'sillon-en-deposito': ('ig-Dby9ijHvJoe.jpg', .5, .55),
    'parlante-bluetooth-portatil': ('ig-DeCHWlmFf01.jpg', .5, .5),
    # dormitorio
    'colchon-beautyrest': ('ig-DZr63w4FW-L-colchon.jpg', .5, .5),
    'placard-multiuso-60x180': ('ig-DbT4j25Dytb.jpg', .5, .5),
    'estufas-y-caloventores': ('ig-DYfprS6vF9f.jpg', .5, .5),
    'maquina-de-coser-singer-m1605': ('ig-DZ7Zb9JFblN.jpg', .5, .5),
    # patio y verano
    'juego-de-jardin': ('ig-Dd7IALHj-76.jpg', .5, .5),
    'juego-de-jardin-mesa': ('ig-Dd7IkUZj1ie.jpg', .5, .5),
    'conservadora-vintage-atma-30-l': ('ig-DemJYrPFQ0P.jpg', .5, .5),
    'conservadora-vintage-atma-20-l': ('ig-DemHxLMlQgR.jpg', .5, .5),
    'estaca-de-luz-solar': ('ig-DemOaemlU64.jpg', .5, .6),
    'estacion-de-energia-kushiro-1000w': ('ig-DZYLtlUj3Gz.jpg', .5, .5),
    'termo-stanley-mate-system': ('ig-DYVbZ9OD7R5.jpg', .5, .5),
    'valijas-elf': ('ig-DdUlH4Oj_Yg.jpg', .5, .5),
    # chicos y bienestar
    'tractor-a-pedal-full-dolu': ('ig-Dbsr01aFWck.jpg', .5, .5),
    'triciclo-tractor-excavadora': ('ig-Dbsr5o_lfyz.jpg', .5, .5),
    'tablet-noblex-toy-story': ('ig-Dan8Ek_GgZW.jpg', .5, .5),
    'set-de-pilates-proline': ('ig-DemGqaSleir.jpg', .5, .5),
    'set-de-yoga-proline': ('ig-DemINoClUU9.jpg', .5, .5),
}
for name, (src, cx, cy) in P.items():
    crop(src, name, 800, 1000, cx, cy)

# --- Ambientes para el marco-casa (aprox. 1,09:1, como el logo) ---
R = {
    'ambiente-cocina': ('ig-DavGmwYFQKX.jpg', .5, .5),
    'ambiente-lavadero': ('ig-DbYNZ36le-p.jpg', .5, .5),
    'ambiente-living': ('ig-DbT0W3zDw2d.jpg', .5, .5),
    'ambiente-dormitorio': ('ig-DZr63w4FW-L-colchon.jpg', .5, .5),
    'ambiente-patio': ('ig-Dd7IALHj-76.jpg', .5, .5),
    'ambiente-chicos': ('ig-Dbsr01aFWck.jpg', .5, .5),
}
for name, (src, cx, cy) in R.items():
    crop(src, name, 1090, 1000, cx, cy)

# --- Local ---
crop('liga-38658499_1811122745662197_5441571170002403328_n.jpg', 'local-muebles-fesler-almirante-brown-324-de-noche', 1090, 1000, .52, .55, 82)
crop('liga-38658499_1811122745662197_5441571170002403328_n.jpg', 'vidriera-muebles-fesler-chaves-panoramica', 2000, 1126, .5, .5, 80)
crop('liga-Imagen-de-WhatsApp-2025-11-19-a-las-19.04.32_a09100bc.jpg', 'fernando-arias-y-delfina-frente-al-local', 1000, 1000, .55, .7, 82)
crop('liga-Imagen-de-WhatsApp-2025-11-19-a-las-19.04.32_a09100bc.jpg', 'frente-del-local-cartel-mf', 1200, 1500, .52, .3, 82)
crop('liga-Imagen-de-WhatsApp-2025-11-19-a-las-19.04.31_e1ab4760.jpg', 'fernando-y-delfina-arias-en-la-puerta', 800, 1100, .5, .6, 82)
crop('liga-Imagen-de-WhatsApp-2025-11-19-a-las-19.04.32_a09100bc.jpg', 'fachada-de-piedra-almirante-brown', 1600, 900, .5, .45, 80)

# --- Logo: recorte del posteo #ModoMundial, fondo transparente ---
im = Image.open(os.path.join(RAW, 'ig-DZbENsiIMwg.jpg')).convert('RGB')
im = im.crop((201, 444, 455, 678))
im = im.resize((im.width * 4, im.height * 4), Image.LANCZOS)
px = im.load()
W, H = im.size
green = Image.new('L', (W, H), 0)
gp = green.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        if g > r + 12 and g < 150 and b < g:
            gp[x, y] = 255
# afuera = flood desde las esquinas sobre lo no-verde
outside = green.copy()
for c in [(0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1)]:
    if outside.getpixel(c) == 0:
        ImageDraw.floodfill(outside, c, 128)
mask = outside.point(lambda v: 0 if v == 128 else 255)
from PIL import ImageFilter
mask = mask.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
# colores limpios: casa verde #21422B, letras crema
lum = im.convert('L')
letters = lum.point(lambda v: 255 if v > 150 else (0 if v < 90 else int((v - 90) / 60 * 255)))
base = Image.new('RGB', (W, H), (33, 66, 43))
cream = Image.new('RGB', (W, H), (246, 244, 238))
logo = Image.composite(cream, base, letters)
logo.putalpha(mask)
bb = mask.getbbox()
logo = logo.crop(bb)
logo.save(os.path.join(OUT, 'logo-muebles-fesler.png'))
logo.resize((180, int(180 * logo.height / logo.width)), Image.LANCZOS).save(os.path.join(OUT, 'favicon-180.png'))
logo.resize((64, int(64 * logo.height / logo.width)), Image.LANCZOS).save(os.path.join(OUT, 'favicon-64.png'))
print('ok', logo.size)
