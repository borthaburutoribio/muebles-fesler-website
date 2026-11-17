# -*- coding: utf-8 -*-
"""Genera index.html de Muebles Fesler.  python -I _build/build.py  (desde la carpeta del sitio)"""
import json, html, os

BASE = 'https://borthaburutoribio.github.io/muebles-fesler-website/'
WA = '5492983344855'
V = '14'

# ------------------------------------------------------------------ ambientes
# Productos reales sacados de los posteos de @mueblesfesler (2026). Sin precios: no los publican.
ROOMS = [
    ('cocina', 'Cocina', 'ambiente-cocina', 'Freidora Liliana DuoFry: dos cestas de 4,5 litros', [
        ('freidora-de-aire-liliana-duofry', 'Freidora de aire Liliana DuoFry', 'Dos cestas de 4,5 L: papas y pollo a la vez, sin mezclar'),
        ('multiprocesadora-liliana-digipros', 'Multiprocesadora Liliana Digipros', '6 velocidades, licuadora de 2 L, molinillo y exprimidor'),
        ('cafetera-oster-8-tazas', 'Cafetera programable Oster', '8 tazas, pantalla táctil y jarra térmica'),
        ('sandwichera-oster', 'Sandwichera Oster', 'Placa inferior más profunda: entran sándwiches cargados'),
        ('horno-de-pan-atma', 'Horno de pan Atma', 'Pan casero: cargás los ingredientes y él amasa y cocina'),
        ('cocina-florencia-5818', 'Cocina industrial Florencia 5818', 'Robusta y pensada para uso intensivo'),
    ]),
    ('lavadero', 'Lavadero y limpieza', 'ambiente-lavadero', 'Lavasecarropas Electrolux LSC11: lava 10,5 kg y seca 7', [
        ('lavasecarropas-electrolux-lsc11', 'Lavasecarropas Electrolux LSC11', 'Lava 10,5 kg y seca 7 kg, motor inverter'),
        ('lavarropas-tcl-effiwash-11-kg', 'Lavarropas TCL Effiwash 11 kg', '1400 RPM, inverter y función vapor'),
        ('lavasecarropas-smartlife-slim', 'Lavasecarropas Smartlife Slim', 'Inverter y angosto, para lavaderos chicos'),
        ('aspiradora-midea-directcyclone', 'Aspiradora Midea DirectCyclone', '2000 W, sin bolsa'),
        ('aspiradora-robot-smartlife', 'Aspiradora robot Smartlife', 'Barre sola mientras estás en el trabajo'),
        ('aspiradora-liliana-zuma-2-en-1', 'Aspiradora Liliana Zuma 2 en 1', 'Inalámbrica: de escoba pasa a aspiradora de mano'),
    ]),
    ('living', 'Living', 'ambiente-living', 'Biblioteca Kanazawa, línea Kyoto', [
        ('tv-philips-70-ambilight', 'Smart TV Philips 70" 4K Ambilight', 'Luces detrás de la pantalla que siguen la imagen'),
        ('tv-tcl-p8k-qled-65', 'Smart TV TCL P8K QLED 65"', 'QLED de 65 pulgadas, para ver los partidos en grande'),
        ('biblioteca-kanazawa-linea-kyoto', 'Biblioteca Kanazawa (línea Kyoto)', 'Estantes abiertos y una puerta para guardar'),
        ('bahiut-gammel-blanco-roble', 'Bahiut Gammel blanco y roble', '4 puertas y cajón, 150 x 45 x 100 cm'),
        ('sillon-en-deposito', 'Sillones', 'Hay más modelos en el depósito: preguntanos'),
        ('parlante-bluetooth-portatil', 'Parlante bluetooth portátil', 'Función TWS: se conectan dos a la vez'),
    ]),
    ('dormitorio', 'Dormitorio', 'ambiente-dormitorio', 'Colchón Beautyrest de resortes enfundados', [
        ('colchon-beautyrest', 'Colchón Beautyrest', 'Resortes enfundados: no sentís cuando el otro se da vuelta'),
        ('placard-multiuso-60x180', 'Placard multiuso', '60 x 1,80: de 2 puertas y 2 cajones o de 4 puertas'),
        ('estufas-y-caloventores', 'Estufas y caloventores', 'A leña, eléctricas y caloventores para el invierno'),
        ('maquina-de-coser-singer-m1605', 'Máquina de coser Singer M1605', 'Compacta, para quien recién empieza a coser'),
    ]),
    ('patio', 'Patio y verano', 'ambiente-patio', 'Juegos de jardín para la galería', [
        ('juego-de-jardin', 'Juegos de jardín', 'Para patios, galerías y quinchos'),
        ('conservadora-vintage-atma-30-l', 'Conservadora vintage Atma 30 L', 'Rosa, con carrito: se lleva sola a la laguna'),
        ('estaca-de-luz-solar', 'Estaca de luz solar', 'Se clava en el cantero y carga con el sol'),
        ('estacion-de-energia-kushiro-1000w', 'Estación de energía Kushiro 1000 W', 'Batería de 808 Wh para camping y cortes de luz'),
        ('termo-stanley-mate-system', 'Termo Stanley 1,2 L Mate System', 'El pico pensado para cebar'),
        ('valijas-elf', 'Valijas Elf', 'Sea cual sea el plan, empieza por el equipaje'),
    ]),
    ('chicos', 'Chicos y bienestar', 'ambiente-chicos', 'Tractor a pedal Full Dolu', [
        ('tractor-a-pedal-full-dolu', 'Tractor a pedal Full Dolu', '4 ruedas, marcha adelante y atrás'),
        ('triciclo-tractor-excavadora', 'Tractor excavadora a pedal', 'De 3 a 7 años, aguanta hasta 50 kg'),
        ('tablet-noblex-toy-story', 'Tablet Noblex Toy Story 10,1"', 'Con funda de goma para que aguante a los chicos'),
        ('set-de-pilates-proline', 'Set de pilates Proline', 'Rolo de foam, barra y más, en rosa'),
        ('set-de-yoga-proline', 'Set de yoga Proline', '6 piezas, para hacer en el living'),
    ]),
]

SUMMER = [
    ('conservadora-vintage-atma-30-l', 'Conservadora Atma 30 L', '30 litros con carrito y manija, en rosa vintage. También está la de 20 L.'),
    ('juego-de-jardin-mesa', 'Juegos de jardín', 'Mesas y sillas para la galería. Preguntá qué modelos hay en el local.'),
    ('estaca-de-luz-solar', 'Estaca de luz solar', 'Se clava en el cantero, carga de día y prende sola de noche. Sin cables.'),
    ('estacion-de-energia-kushiro-1000w', 'Estación Kushiro 1000 W', 'Batería de 808 Wh y onda senoidal pura: para el camping o cuando se corta la luz.'),
    ('termo-stanley-mate-system', 'Termo Stanley 1,2 L', 'El Mate System: el pico está pensado para cebar sin mojar la yerba.'),
    ('set-de-pilates-proline', 'Set de pilates Proline', 'Rolo de foam, barra, pelota y aro, todo en rosa.'),
]

BRANDS = ['Atma', 'Liliana', 'Philips', 'Electrolux', 'TCL', 'Midea', 'Oster', 'Singer', 'Stanley', 'Smartlife',
          'Peabody', 'Lusqtoff', 'Telefunken', 'Noblex', 'Motorola', 'Beautyrest', 'Proline', 'Florencia', 'Ultracomb']

FAQ = [
    ('¿Hacen envíos?', 'Sí, el envío no tiene cargo. <span class="tbc">Lorem ipsum dolor sit amet: zona y días de reparto.</span><!-- A CONFIRMAR: hasta dónde llega el envío sin cargo (¿Chaves y zona rural? ¿De la Garma, Juan E. Barra?) y en qué días -->'),
    ('¿Se puede pagar en cuotas?', '<span class="tbc">Lorem ipsum dolor sit amet, consectetur adipiscing elit: tarjetas, cuotas y descuentos en efectivo.</span><!-- A CONFIRMAR: medios de pago, cuotas, Cuenta DNI, transferencia -->'),
    ('¿Tienen muebles o solo electrodomésticos?', 'Las dos cosas, y bazar. En muebles hay placares multiuso de 60 x 1,80, el bahiut Gammel (150 x 45 x 100), la biblioteca Kanazawa, sillones (con más modelos en el depósito), colchones Beautyrest y juegos de jardín, entre otros.'),
    ('¿Abren los sábados?', 'Sí, de 9:00 a 12:30. De lunes a viernes abrimos de 9:00 a 12:30 y de 15:00 a 20:00.'),
    ('¿Me pasan precios por WhatsApp?', 'Sí. Escribinos al 2983 34-4855 con el producto, o armá la lista en <a href="#casa">Recorré la casa</a> y el mensaje sale escrito.'),
    ('¿Por qué comprar acá y no por internet?', 'Porque compramos en red con casas de electro de todo el país y estamos cerca de esos precios, y además el que te lo vende está en Almirante Brown 324 si algo falla. Como dice Fernando: si se consume en Chaves, la plata se queda en Chaves.'),
]

e = html.escape


def wa_link(text):
    from urllib.parse import quote
    return f'https://wa.me/{WA}?text={quote(text)}'


def room_html(i, r):
    rid, name, amb, caption, items = r
    rows = []
    for slug, pname, fact in items:
        rows.append(f'''        <li class="item">
          <img src="assets/img/{slug}.webp" width="800" height="1000" alt="{e(pname)} en Muebles Fesler" loading="lazy" decoding="async">
          <div class="item-txt"><p class="item-name">{e(pname)}</p><p class="item-fact">{e(fact)}</p></div>
          <button class="add" type="button" aria-pressed="false" data-name="{e(pname)}"><span class="add-on">Sumar</span><span class="add-off">En tu lista</span></button>
        </li>''')
    return f'''      <section class="room" id="{rid}" data-img="assets/img/{amb}.webp" data-cap="{e(name)}" data-fact="{e(caption)}" aria-labelledby="h-{rid}">
        <img class="room-pic" src="assets/img/{amb}.webp" width="1090" height="1000" alt="" loading="lazy" decoding="async">
        <h3 id="h-{rid}">{e(name)}</h3>
        <ul class="items">
{chr(10).join(rows)}
        </ul>
      </section>'''


def page():
    rooms = '\n'.join(room_html(i, r) for i, r in enumerate(ROOMS))
    summer_names = '\n'.join(
        f'          <li><button type="button" class="s-name{" is-on" if i == 0 else ""}" aria-pressed="{"true" if i == 0 else "false"}" data-img="assets/img/{s}.webp" data-fact="{e(f)}">{e(n)}</button></li>'
        for i, (s, n, f) in enumerate(SUMMER))
    brands = ''.join(f'<span>{b}</span>' for b in BRANDS)
    faq = '\n'.join(f'''        <details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>''' for q, a in FAQ)
    faq_ld = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q,
                        'acceptedAnswer': {'@type': 'Answer', 'text': __import__('re').sub(r'<!--.*?-->|<[^>]+>', '', a)}}
                       for q, a in FAQ if 'Lorem' not in a]}
    biz_ld = {
        '@context': 'https://schema.org', '@type': ['HomeGoodsStore', 'FurnitureStore'],
        'name': 'Muebles Fesler', 'url': BASE,
        'image': BASE + 'assets/img/vidriera-muebles-fesler-chaves-panoramica.webp',
        'logo': BASE + 'assets/img/logo-muebles-fesler.png',
        'telephone': '+54 9 2983 34-4855', 'foundingDate': '1998',
        'founder': {'@type': 'Person', 'name': 'Fernando Arias'},
        'address': {'@type': 'PostalAddress', 'streetAddress': 'Almirante Brown 324', 'postalCode': 'B7513',
                    'addressLocality': 'Adolfo Gonzales Chaves', 'addressRegion': 'Buenos Aires', 'addressCountry': 'AR'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': -38.0356382, 'longitude': -60.1001215},
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '09:00', 'closes': '12:30'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '15:00', 'closes': '20:00'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '09:00', 'closes': '12:30'}],
        'aggregateRating': {'@type': 'AggregateRating', 'ratingValue': '4.6', 'reviewCount': '77'},
        'sameAs': ['https://www.instagram.com/mueblesfesler/', 'https://www.facebook.com/mueblesfesler1/'],
        'memberOf': {'@type': 'Organization', 'name': 'Liga de Comercio e Industria de Adolfo Gonzales Chaves'}}
    wa_main = wa_link('Hola! Vi la web de Muebles Fesler y quería hacer una consulta.')
    first = SUMMER[0]
    return f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Muebles Fesler · Electro, muebles y colchones en Gonzales Chaves</title>
<meta name="description" content="Casa de electrodomésticos, muebles, colchones y jardín en Almirante Brown 324, Adolfo Gonzales Chaves. Desde 1998. Atma, Liliana, Philips, Electrolux y más. Envío sin cargo y consultas por WhatsApp.">
<!-- Sitio de muestra: no indexar hasta que el local lo apruebe -->
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{BASE}">
<meta property="og:type" content="website">
<meta property="og:title" content="Muebles Fesler · Todo para tu casa en Chaves">
<meta property="og:description" content="Electro, muebles, colchones y jardín desde 1998 en Almirante Brown 324. Armá tu lista y consultá por WhatsApp.">
<meta property="og:image" content="{BASE}assets/img/vidriera-muebles-fesler-chaves-panoramica.webp">
<meta name="theme-color" content="#21422B">
<link rel="icon" type="image/png" href="assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="assets/img/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Libre+Caslon+Display&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="assets/img/local-muebles-fesler-almirante-brown-324-de-noche.webp">
<link rel="stylesheet" href="styles.css?v={V}">
<script type="application/ld+json">{json.dumps(biz_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#casa">Saltar a los productos</a>

<header class="bar" id="top">
  <a class="brand" href="#top" aria-label="Muebles Fesler, inicio">
    <img src="assets/img/logo-muebles-fesler.png" width="988" height="906" alt="">
    <span>Muebles Fesler</span>
  </a>
  <!-- A CONFIRMAR: logo recortado de un posteo de Instagram; pedir el archivo original -->
  <nav class="nav" id="nav" aria-label="Secciones">
    <a href="#casa">La casa</a>
    <a href="#marcas">Marcas</a>
    <a href="#historia">Historia</a>
    <a href="#comprar">Cómo comprar</a>
    <a href="#visitanos">Visitanos</a>
  </nav>
  <a class="btn btn-sm bar-wa" href="{wa_main}" target="_blank" rel="noopener">WhatsApp</a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav"><span class="sr">Menú</span><i></i><i></i></button>
</header>

<main>
<div class="stage">
  <div class="stage-copy">
    <section class="hero" aria-labelledby="h1">
      <h1 id="h1">Todo para tu casa, desde 1998 en Chaves</h1>
      <p class="lead">Electro, muebles, colchones y cosas para el patio, de marcas como Atma, Liliana, Philips y Electrolux, entre otras. Te atienden Fernando y Delfi en Almirante Brown 324, y el envío no tiene cargo.</p>
      <div class="hero-act">
        <a class="btn" href="{wa_main}" target="_blank" rel="noopener">Consultanos por WhatsApp</a>
        <a class="txt-link" href="#casa">o recorré la casa</a>
      </div>
      <p class="facts"><strong>4,6</strong> en Google con 77 opiniones <span aria-hidden="true">·</span> Lunes a viernes 9 a 12:30 y 15 a 20 <span aria-hidden="true">·</span> Sábados 9 a 12:30</p>
    </section>

    <section class="casa" id="casa" aria-labelledby="h-casa">
      <h2 id="h-casa">Recorré la casa</h2>
      <p class="casa-intro">Elegí un ambiente, tocá <strong>Sumar</strong> en lo que te interese y te armamos el mensaje para mandarnos por WhatsApp con toda la lista. Te contestamos precio, cuotas y cuándo te lo llevamos.</p>
      <nav class="rooms-nav" aria-label="Ambientes">
        {''.join(f'<a href="#{r[0]}">{e(r[1].split(" y ")[0])}</a>' for r in ROOMS)}
      </nav>
{rooms}
      <p class="casa-more">Esto es una parte. En el local hay mucho más: bazar, pequeños electro, calefacción y regalos. Lo nuevo sale primero en <a href="https://www.instagram.com/mueblesfesler/" target="_blank" rel="noopener">@mueblesfesler</a>.</p>
    </section>
  </div>

  <aside class="stage-pic" aria-label="Vista del ambiente">
    <figure class="house">
      <div class="house-frame">
        <img id="house-img" src="assets/img/local-muebles-fesler-almirante-brown-324-de-noche.webp" width="1090" height="1000" alt="Vidriera de Muebles Fesler de noche, Almirante Brown 324, con televisores, lavarropas y un sillón rojo">
      </div>
      <figcaption><span id="house-cap">Almirante Brown 324</span> <span id="house-fact">La vidriera de noche, con el cartel encendido</span></figcaption>
    </figure>
  </aside>
</div>

<section class="resumen" aria-labelledby="h-resumen">
  <h2 id="h-resumen">En resumen</h2>
  <table>
    <tr><th scope="row">Qué hay</th><td>Electrodomésticos, televisores, muebles, colchones, bazar, jardín y verano</td></tr>
    <tr><th scope="row">Dónde</th><td>Almirante Brown 324, Adolfo Gonzales Chaves</td></tr>
    <tr><th scope="row">Cuándo</th><td>Lunes a viernes 9:00 a 12:30 y 15:00 a 20:00 · Sábados 9:00 a 12:30</td></tr>
    <tr><th scope="row">Envíos</th><td>Sin cargo <span class="tbc">(Lorem ipsum: zona)</span></td></tr>
    <tr><th scope="row">Consultas</th><td><a href="{wa_main}" target="_blank" rel="noopener">WhatsApp 2983 34-4855</a></td></tr>
  </table>
</section>

<section class="marcas" id="marcas" aria-labelledby="h-marcas">
  <h2 id="h-marcas" class="sr">Marcas</h2>
  <div class="band" aria-hidden="true"><div class="track">{brands}{brands}</div></div>
  <p class="band-note">Algunas de las marcas que tenemos, entre muchas otras. Compramos junto a <strong>Hogarnet</strong>, una red de casas de electro de todo el país (en 2020 ya éramos unos 280 socios): así llegamos a precios de cadena sin dejar de atenderte en persona.</p>
</section>

<section class="verano" id="verano" aria-labelledby="h-verano">
  <div class="disc-wrap">
    <div class="disc" aria-hidden="true"></div>
    <img id="s-img" class="s-img" src="assets/img/{first[0]}.webp" width="800" height="1000" alt="Productos para el verano en Muebles Fesler" loading="lazy">
    <p id="s-fact" class="s-fact">{e(first[2])}</p>
  </div>
  <div class="s-list">
    <h2 id="h-verano">Para este verano</h2>
    <ul>
{summer_names}
    </ul>
  </div>
</section>

<section class="historia" id="historia" aria-labelledby="h-historia">
  <div class="panel">
    <div class="p-left">
      <h2 id="h-historia">Desde 1998, de padre a hija</h2>
      <div class="p-photo">
        <img src="assets/img/fernando-y-delfina-arias-casa.webp" width="1090" height="1000" alt="Fernando Arias y su hija Delfina frente a Muebles Fesler, en Almirante Brown 324" loading="lazy">
      </div>
    </div>
    <div class="p-right">
      <div class="p-block">
        <h3>De la mueblería del suegro al electro</h3>
        <p>Muebles Fesler nació en 1998 como mueblería, en Vélez Sarsfield. En el 2000 el suegro de Fernando se la pasó a él y a Silvia, y a fines de 2006, cuando su suegra se retiró, empezaron con los electrodomésticos. Fernando tenía 27 años cuando quedó al mando.</p>
      </div>
      <div class="p-block">
        <h3>Delfi, desde el último año del secundario</h3>
        <p>En 2017 operaron a su mamá y Fernando le preguntó si podía cubrirla en el local. Se quedó. Hoy es la cara visible del negocio y la que te contesta el WhatsApp.</p>
        <blockquote>“Me encanta trabajar con él y me encanta el vínculo que tenemos.” <cite>Delfina Arias</cite></blockquote>
      </div>
      <p class="p-next">Ya está terminado un segundo local, que esperan inaugurar en 2026. <!-- A CONFIRMAR: qué va a ser el segundo local y cuándo abre (nota de la Liga, nov. 2025) --></p>
      <a class="btn btn-light" href="{wa_main}" target="_blank" rel="noopener">Escribinos</a>
    </div>
  </div>
</section>

<section class="comprar" id="comprar" aria-labelledby="h-comprar">
  <h2 id="h-comprar">Cómo se compra acá</h2>
  <ol class="tiles">
    <li class="tile t1">
      <div class="t-pic"><img src="assets/img/freidora-de-aire-liliana-duofry.webp" width="800" height="1000" alt="Freidora de aire Liliana DuoFry, publicada en el Instagram de Muebles Fesler" loading="lazy"></div>
      <h3>Mirás</h3>
      <p>En la vidriera, en el local o en el Instagram, donde subimos lo que va llegando.</p>
    </li>
    <li class="tile t2">
      <div class="t-pic"><img src="assets/img/fernando-y-delfina-arias-en-la-puerta.webp" width="800" height="1100" alt="Fernando y Delfina Arias en la puerta del local" loading="lazy"></div>
      <h3>Consultás</h3>
      <p>Por WhatsApp o en el mostrador. Delfi te pasa precio, cuotas y formas de pago. <span class="tbc">Lorem ipsum.</span></p>
    </li>
    <li class="tile t3">
      <div class="t-pic"><video src="assets/img/delfina-recorre-el-local-muebles-fesler.mp4" poster="assets/img/delfina-recorre-el-local-poster.webp" muted loop playsinline preload="none" aria-label="Delfina recorre el local: ayudantes de cocina, lavarropas y televisores"></video></div>
      <h3>Lo ves en el local, y te lo llevamos</h3>
      <p>Almirante Brown 324 por dentro, como lo mostró Delfi en un reel. El envío no tiene cargo. <span class="tbc">Lorem ipsum: zona.</span></p>
    </li>
  </ol>
</section>

<section class="opinion" aria-labelledby="h-op">
  <h2 id="h-op" class="sr">Opiniones</h2>
  <p class="score"><strong>4,6</strong> <span>de 5 en Google, con 77 opiniones</span></p>
  <blockquote>
    <p>“Muy buenos precios, y sobre todo, excelente atención.”</p>
    <cite>Opinión publicada en Google Maps</cite>
  </blockquote>
  <a class="txt-link" href="https://www.google.com/maps/search/?api=1&amp;query=Muebles+Fesler+Almirante+Brown+324+Gonzales+Chaves" target="_blank" rel="noopener">Ver todas las opiniones</a>
</section>

<section class="faq" id="preguntas" aria-labelledby="h-faq">
  <h2 id="h-faq">Lo que más nos preguntan</h2>
  <div class="qs">
{faq}
  </div>
</section>

<section class="visit" id="visitanos" aria-labelledby="h-visit">
  <img class="visit-bg" src="assets/img/vidriera-muebles-fesler-chaves-panoramica.webp" width="2000" height="1126" alt="Frente de Muebles Fesler de noche, con la pared de piedra y la vidriera iluminada" loading="lazy">
  <div class="card">
    <h2 id="h-visit">Vení al local</h2>
    <p>Almirante Brown 324<br>B7513 Adolfo Gonzales Chaves</p>
    <dl class="hours">
      <div><dt>Lunes a viernes</dt><dd>9:00 – 12:30</dd></div>
      <div><dt></dt><dd>15:00 – 20:00</dd></div>
      <div><dt>Sábados</dt><dd>9:00 – 12:30</dd></div>
    </dl>
    <p><a href="{wa_main}" target="_blank" rel="noopener">WhatsApp 2983 34-4855</a></p>
    <a class="btn btn-block" href="https://www.google.com/maps/dir/?api=1&amp;destination=-38.0356382,-60.1001215" target="_blank" rel="noopener">Cómo llegar</a>
  </div>
</section>
<div class="map">
  <iframe title="Mapa: Muebles Fesler, Almirante Brown 324, Gonzales Chaves" src="https://www.google.com/maps?q=-38.0356382,-60.1001215&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
</main>

<footer class="foot">
  <div class="f-pic"><img src="assets/img/frente-del-local-cartel-mf.webp" width="1200" height="1500" alt="Cartel verde con el logo mf sobre la entrada de Muebles Fesler" loading="lazy"></div>
  <div class="f-side">
    <p class="f-brand">Muebles Fesler</p>
    <nav class="f-menu" aria-label="Pie">
      <a href="#casa">Recorré la casa</a>
      <a href="#verano">Para este verano</a>
      <a href="#historia">Nuestra historia</a>
      <a href="#preguntas">Preguntas</a>
      <a href="#visitanos">Visitanos</a>
    </nav>
    <div class="f-cols">
      <p>Almirante Brown 324, Gonzales Chaves<br><a href="{wa_main}" target="_blank" rel="noopener">WhatsApp 2983 34-4855</a></p>
      <p><a href="https://www.instagram.com/mueblesfesler/" target="_blank" rel="noopener">Instagram</a><br><a href="https://www.facebook.com/mueblesfesler1/" target="_blank" rel="noopener">Facebook</a><br><button type="button" class="share">Compartir esta página</button></p>
    </div>
    <p class="legal">Socios de la Liga de Comercio e Industria de Adolfo Gonzales Chaves. Sitio de muestra hecho por <a href="https://tranqueraweb.com.ar" target="_blank" rel="noopener">Tranquera Digital</a>.</p>
  </div>
</footer>

<div class="dock" id="dock">
  <a class="btn dock-btn" id="dock-btn" href="{wa_main}" target="_blank" rel="noopener"><span id="dock-txt">Consultar por WhatsApp</span></a>
  <button type="button" class="dock-clear" id="dock-clear" hidden>Vaciar</button>
</div>

<script src="script.js?v={V}" defer></script>
</body>
</html>
'''


open('index.html', 'w', encoding='utf-8').write(page())
print('index.html ok')
