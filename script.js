(function () {
  'use strict';
  var WA = '5492983344855';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* menú móvil */
  var mb = $('.menu-btn'), nav = $('#nav');
  if (mb) {
    mb.addEventListener('click', function () {
      var open = mb.getAttribute('aria-expanded') === 'true';
      mb.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
    });
    $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { mb.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }); });
  }

  /* entradas escalonadas */
  var groups = [
    ['.hero', 'h1, .lead, .hero-act, .facts'],
    ['.casa', 'h2, .casa-intro'],
    ['.resumen', 'h2, table'],
    ['.verano', '.s-list h2, .s-list li, .disc-wrap'],
    ['.historia', 'h2, .p-photo, .p-block, .p-next, .btn'],
    ['.comprar', 'h2, .tile'],
    ['.opinion', '.score, blockquote, .txt-link'],
    ['.faq', 'h2, details'],
    ['.foot', '.f-brand, .f-menu a, .f-cols, .legal']
  ];
  var targets = [];
  groups.forEach(function (g) {
    $$(g[0]).forEach(function (root) {
      $$(g[1], root).forEach(function (el, i) { el.classList.add('rv'); el.style.setProperty('--d', Math.min(i, 8) * 75 + 'ms'); targets.push(el); });
    });
  });
  $$('.item').forEach(function (el, i) { el.classList.add('rv'); el.style.setProperty('--d', (i % 6) * 60 + 'ms'); targets.push(el); });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (t) { io.observe(t); });
  } else { targets.forEach(function (t) { t.classList.add('in'); }); }

  /* casa fija: cambia la foto según el ambiente en pantalla */
  var himg = $('#house-img'), hcap = $('#house-cap'), hfact = $('#house-fact');
  var start = { img: himg.getAttribute('src'), alt: himg.alt, cap: hcap.textContent, fact: hfact.textContent };
  var current = start.img;
  var mob = window.matchMedia('(max-width: 960px)');
  function show(img, alt, cap, fact) {
    if (img === current || mob.matches) return;
    current = img;
    himg.classList.add('swap');
    setTimeout(function () {
      himg.src = img; himg.alt = alt;
      hcap.textContent = cap; hfact.textContent = fact;
      var done = function () { himg.classList.remove('swap'); };
      if (himg.complete) requestAnimationFrame(done); else himg.onload = done;
    }, 260);
  }
  var rooms = $$('.room'), roomLinks = $$('.rooms-nav a');
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var r = e.target;
        show(r.dataset.img, 'Ambiente ' + r.dataset.cap + ' con productos de Muebles Fesler', r.dataset.cap, r.dataset.fact);
        roomLinks.forEach(function (a) { a.classList.toggle('is-on', a.getAttribute('href') === '#' + r.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    rooms.forEach(function (r) { ro.observe(r); });
    var hero = $('.hero');
    var ho = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { show(start.img, start.alt, start.cap, start.fact); roomLinks.forEach(function (a) { a.classList.remove('is-on'); }); } });
    }, { rootMargin: '-40% 0px -40% 0px' });
    ho.observe(hero);
  }

  /* lista de consulta → WhatsApp */
  var list = [];
  try { list = JSON.parse(localStorage.getItem('fesler-lista') || '[]'); } catch (e) { list = []; }
  var dock = $('#dock'), dbtn = $('#dock-btn'), dtxt = $('#dock-txt'), dclear = $('#dock-clear');
  var mobile = window.matchMedia('(max-width: 960px)');
  function msg() {
    if (!list.length) return 'Hola! Vi la web de Muebles Fesler y quería hacer una consulta.';
    return 'Hola! Vi la web de Muebles Fesler y quería consultar precio y formas de pago de:\n' +
      list.map(function (n) { return '• ' + n; }).join('\n') + '\n\nGracias!';
  }
  function render() {
    $$('.add').forEach(function (b) { b.setAttribute('aria-pressed', String(list.indexOf(b.dataset.name) > -1)); });
    dbtn.href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg());
    dtxt.textContent = list.length ? 'Consultar ' + list.length + (list.length === 1 ? ' producto' : ' productos') + ' por WhatsApp' : 'Consultar por WhatsApp';
    dclear.hidden = !list.length;
    dock.classList.toggle('show', list.length > 0 || mobile.matches);
    try { localStorage.setItem('fesler-lista', JSON.stringify(list)); } catch (e) {}
  }
  $$('.add').forEach(function (b) {
    b.addEventListener('click', function () {
      var n = b.dataset.name, i = list.indexOf(n);
      if (i > -1) list.splice(i, 1); else list.push(n);
      render();
    });
  });
  dclear.addEventListener('click', function () { list = []; render(); });
  if (mobile.addEventListener) mobile.addEventListener('change', render);
  render();

  /* verano: lista que cambia la foto */
  var simg = $('#s-img'), sfact = $('#s-fact'), disc = $('.disc');
  var tones = ['#C9D3C2', '#DDD6C7', '#C9D3C2', '#DDD6C7', '#C9D3C2', '#DDD6C7'];
  $$('.s-name').forEach(function (b, i) {
    b.addEventListener('click', function () {
      $$('.s-name').forEach(function (x) { x.classList.remove('is-on'); x.setAttribute('aria-pressed', 'false'); });
      b.classList.add('is-on'); b.setAttribute('aria-pressed', 'true');
      simg.classList.add('swap');
      setTimeout(function () { simg.src = b.dataset.img; simg.alt = b.textContent + ' en Muebles Fesler'; sfact.textContent = b.dataset.fact; simg.classList.remove('swap'); }, 220);
      disc.style.backgroundColor = tones[i];
    });
  });

  /* video: se reproduce solo cuando está en pantalla */
  var vid = $('.t3 video');
  if (vid && 'IntersectionObserver' in window) {
    if (reduce) { vid.removeAttribute('loop'); }
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { vid.preload = 'auto'; if (!reduce) { var p = vid.play(); if (p && p.catch) p.catch(function () {}); } }
        else vid.pause();
      });
    }, { threshold: 0.25 }).observe(vid);
  }

  /* compartir */
  var sh = $('.share');
  if (sh) sh.addEventListener('click', function () {
    var d = { title: 'Muebles Fesler', text: 'Todo para tu casa en Gonzales Chaves', url: location.href };
    if (navigator.share) navigator.share(d).catch(function () {});
    else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { sh.textContent = 'Link copiado'; });
  });
})();
