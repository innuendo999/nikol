/* Nikol Pavlova – progressive enhancement; pages work without JS */
(function () {
  'use strict';

  // Mobile menu
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
  }

  // Services dropdown
  document.querySelectorAll('.dd-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.dd-btn[aria-expanded="true"]').forEach(function (b) {
      b.setAttribute('aria-expanded', 'false');
      b.focus();
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.dd-btn[aria-expanded="true"]').forEach(function (b) {
      if (!b.parentNode.contains(e.target)) b.setAttribute('aria-expanded', 'false');
    });
  });

  // Portfolio: filter + "show more" (all images stay in the HTML)
  var grid = document.querySelector('[data-portfolio]');
  if (grid) {
    var STEP = 16;
    var items = Array.prototype.slice.call(grid.querySelectorAll('figure'));
    var pills = document.querySelectorAll('[data-filter]');
    var moreBtn = document.querySelector('button[data-more]');
    var status = document.querySelector('p[data-status]');
    var labels = grid.dataset;
    var cat = 'all';
    var limit = STEP;
    var render = function () {
      var matching = items.filter(function (f) { return cat === 'all' || f.dataset.cat === cat; });
      items.forEach(function (f) { f.hidden = true; });
      matching.slice(0, limit).forEach(function (f) { f.hidden = false; });
      var shown = Math.min(limit, matching.length);
      var rest = matching.length - shown;
      if (status) status.textContent = labels.labelShown.replace('{n}', shown).replace('{t}', matching.length);
      if (moreBtn) {
        moreBtn.hidden = rest <= 0;
        moreBtn.textContent = labels.labelMore.replace('{n}', rest);
      }
    };
    pills.forEach(function (p) {
      p.addEventListener('click', function () {
        cat = p.dataset.filter;
        limit = STEP;
        pills.forEach(function (q) { q.setAttribute('aria-pressed', String(q === p)); });
        render();
      });
    });
    if (moreBtn) moreBtn.addEventListener('click', function () { limit += STEP; render(); });
    render();
  }

  // Blog: pickers (radio groups) – show only the answer for the picked combination
  document.querySelectorAll('[data-finder]').forEach(function (box) {
    var ans = box.querySelectorAll('[data-ans]');
    var pick = function () {
      var key = Array.prototype.map.call(box.querySelectorAll('input[type="radio"]:checked'), function (i) { return i.value; }).join('-');
      ans.forEach(function (a) { a.classList.toggle('is-on', a.dataset.ans === key); });
    };
    box.classList.add('is-on');
    box.addEventListener('change', pick);
    pick();
  });

  // Blog (brush care): technique tabs – panes are stacked without JS
  document.querySelectorAll('[data-tabs]').forEach(function (box) {
    var list = box.querySelector('[role="tablist"]');
    var btns = list.querySelectorAll('[data-tab]');
    var panes = box.querySelectorAll('[data-pane]');
    var show = function (k) {
      btns.forEach(function (b) { b.setAttribute('aria-selected', String(b.dataset.tab === k)); });
      panes.forEach(function (p) { p.hidden = p.dataset.pane !== k; });
    };
    list.hidden = false;
    box.classList.add('is-on');
    btns.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.tab); }); });
    show(btns[0].dataset.tab);
  });

  // Blog (brush care): reveal once in view; SMIL animations play only while visible
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveal = document.querySelectorAll('[data-reveal]');
  var anims = document.querySelectorAll('svg[data-anim]');
  anims.forEach(function (s) { if (s.pauseAnimations) { s.pauseAnimations(); if (still) s.setCurrentTime(1.4); } });
  if ('IntersectionObserver' in window) {
    reveal.forEach(function (el) { el.classList.add('is-armed'); });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var t = e.target;
        if (t.hasAttribute('data-reveal')) { if (e.isIntersecting) { t.classList.add('is-in'); io.unobserve(t); } return; }
        if (still || !t.pauseAnimations) return;
        if (e.isIntersecting) t.unpauseAnimations(); else t.pauseAnimations();
      });
    }, { threshold: 0.25 });
    reveal.forEach(function (el) { io.observe(el); });
    anims.forEach(function (s) { io.observe(s); });
  } else if (!still) {
    anims.forEach(function (s) { if (s.unpauseAnimations) s.unpauseAnimations(); });
  }

  // Blog (travel): step-by-step guide with face zones and Minimal / Day / Evening switch
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-guide]').forEach(function (g) {
    var steps = Array.prototype.slice.call(g.querySelectorAll('.tg-step'));
    var zones = g.querySelectorAll('.tg-z');
    var cap = g.querySelector('.tg-cap');
    var count = g.querySelector('.tg-count');
    var modeBtns = g.querySelectorAll('[data-mode]:not(li)');
    var allow = { min: ['base'], day: ['base', 'opt'], eve: ['base', 'opt', 'eve'] };
    var mode = 'day', cur = 0;
    var visible = function () { return steps.filter(function (s) { return !s.hidden; }); };
    var open = function (i, scroll) {
      cur = i;
      var v = visible();
      steps.forEach(function (s, k) {
        var on = k === i;
        s.classList.toggle('is-on', on);
        s.querySelector('.tg-step-h').setAttribute('aria-expanded', String(on));
        s.querySelector('.tg-step-b').hidden = !on;
      });
      var z = (steps[i].dataset.zones || '').split(' ');
      zones.forEach(function (el) { el.classList.toggle('on', z.indexOf(el.dataset.z) >= 0); });
      cap.textContent = steps[i].querySelector('.tg-num').textContent + ' · ' + steps[i].querySelector('.tg-title').textContent;
      count.textContent = (v.indexOf(steps[i]) + 1) + ' / ' + v.length;
      if (scroll) steps[i].scrollIntoView({ block: 'nearest', behavior: calm ? 'auto' : 'smooth' });
    };
    var apply = function () {
      steps.forEach(function (s) { s.hidden = allow[mode].indexOf(s.dataset.mode) < 0; });
      var v = visible();
      v.forEach(function (s, k) { s.querySelector('.tg-num').textContent = (k < 9 ? '0' : '') + (k + 1); });
      open(v.indexOf(steps[cur]) >= 0 ? cur : steps.indexOf(v[0]), false);
    };
    steps.forEach(function (s, k) { s.querySelector('.tg-step-h').addEventListener('click', function () { open(k, false); }); });
    modeBtns.forEach(function (b) {
      b.addEventListener('click', function () {
        mode = b.dataset.mode;
        modeBtns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        apply();
      });
    });
    var go = function (d) {
      var v = visible(), p = v.indexOf(steps[cur]);
      var n = v[Math.max(0, Math.min(v.length - 1, p + d))];
      open(steps.indexOf(n), true);
    };
    g.querySelector('[data-prev]').addEventListener('click', function () { go(-1); });
    g.querySelector('[data-next]').addEventListener('click', function () { go(1); });
    g.querySelector('.tg-modes').hidden = false;
    g.querySelector('.tg-ctrl').hidden = false;
    g.classList.add('is-on');
    apply();
  });

  // Blog (travel): packing checklist counter
  document.querySelectorAll('[data-pack]').forEach(function (box) {
    var out = box.querySelector('[data-tpl]');
    var boxes = box.querySelectorAll('input[type="checkbox"]');
    var upd = function () {
      var n = box.querySelectorAll('input:checked').length;
      out.textContent = out.dataset.tpl.replace('{n}', n).replace('{t}', boxes.length);
    };
    out.hidden = false;
    box.addEventListener('change', upd);
    upd();
  });

  // Blog (travel): dry vs damp sponge
  document.querySelectorAll('[data-sponge]').forEach(function (f) {
    var r = f.querySelector('input[type="range"]'), cov = f.querySelector('.tg-cover'), out = f.querySelector('[data-out]');
    var upd = function () {
      var v = +r.value / 100;
      cov.setAttribute('opacity', String(0.92 - v * 0.55));
      out.textContent = v < 0.5 ? out.dataset.dry : out.dataset.wet;
    };
    r.addEventListener('input', upd);
    upd();
  });

  // Blog (transition blush): concealer + blush mixer builds the gradient strip
  document.querySelectorAll('[data-mix]').forEach(function (f) {
    var svg = f.querySelector('.tb-strip'), range = f.querySelector('input[type="range"]'), out = f.querySelector('output');
    var hex = function (h) { return [1, 3, 5].map(function (i) { return parseInt(h.substr(i, 2), 16); }); };
    var gcd = function (a, b) { return b ? gcd(b, a % b) : a; };
    var draw = function () {
      var n = +range.value, col = f.querySelector('input[name="tb-blush"]:checked').value;
      var a = hex(f.dataset.con), b = hex(col), w = 600 / n, html = '';
      out.textContent = n;
      for (var i = 0; i < n; i++) {
        var t = i / (n - 1);
        var c = 'rgb(' + a.map(function (x, k) { return Math.round(x + (b[k] - x) * t); }).join(',') + ')';
        var lab = i === 0 ? f.dataset.lCon : i === n - 1 ? f.dataset.lBlush : (function () { var p = n - 1 - i, q = i, g = gcd(p, q); return (p / g) + ' : ' + (q / g); })();
        html += '<rect x="' + (i * w + 3).toFixed(1) + '" y="4" width="' + (w - 6).toFixed(1) + '" height="84" rx="2" fill="' + c + '"></rect>' +
          '<text x="' + (i * w + w / 2).toFixed(1) + '" y="114" text-anchor="middle">' + lab + '</text>';
      }
      svg.innerHTML = html;
    };
    f.addEventListener('input', draw);
    f.addEventListener('change', draw);
  });

  // Blog (transition blush): dense vs fluffy brush softness
  document.querySelectorAll('[data-blur]').forEach(function (f) {
    var r = f.querySelector('input[type="range"]'), blur = f.querySelector('feGaussianBlur'), el = f.querySelector('ellipse'), out = f.querySelector('[data-out]');
    var upd = function () {
      var v = +r.value / 100;
      blur.setAttribute('stdDeviation', String(2 + v * 22));
      el.setAttribute('fill-opacity', String(0.85 - v * 0.35));
      el.setAttribute('rx', String(80 + v * 40));
      el.setAttribute('ry', String(36 + v * 16));
      out.textContent = v < 0.5 ? out.dataset.a : out.dataset.b;
    };
    r.addEventListener('input', upd);
    upd();
  });
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(b.dataset.copy).then(function () {
        b.classList.add('is-done'); b.setAttribute('aria-label', b.dataset.done);
      });
    });
  });
})();
