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

  // Blog (brush care): bristle finder – show only the answer for the picked pair
  document.querySelectorAll('[data-finder]').forEach(function (box) {
    var ans = box.querySelectorAll('[data-ans]');
    var pick = function () {
      var f = box.querySelector('input[name="bc-fiber"]:checked');
      var q = box.querySelector('input[name="bc-quality"]:checked');
      var key = (f ? f.value : '') + '-' + (q ? q.value : '');
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
})();
