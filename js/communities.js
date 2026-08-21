/* STAI - research themes on the publications page.
   Stacked bars per year, plus a key that filters the list below. No framework. */
(function () {
  var payload = document.getElementById('comm-data');
  var root = document.querySelector('.comm');
  if (!payload || !root) return;

  var NS = 'http://www.w3.org/2000/svg';
  var data = JSON.parse(payload.textContent);
  var themes = data.themes.map(function (t) { return t.name; });

  var slot = {}, theme = {};
  data.themes.forEach(function (t) {
    slot[t.name] = t.slot;
    t.tags.forEach(function (tag) { theme[tag] = t.name; });
  });
  var OTHER = themes[themes.length - 1];

  /* A paper with n tags is split n, n-1, ... 1 across them and normalised, so
     the tag listed first counts most and every paper still counts once. Tags
     that share a theme add up. Untagged papers count as Other. */
  var years = [], counts = {}, totals = {};
  data.publications.forEach(function (pub) {
    var tags = pub.tags && pub.tags.length ? pub.tags : [];
    var span = tags.length * (tags.length + 1) / 2;
    if (!counts[pub.year]) { counts[pub.year] = {}; years.push(pub.year); }
    if (!tags.length) return add(pub.year, OTHER, 1);
    tags.forEach(function (tag, i) {
      add(pub.year, theme[tag] || OTHER, (tags.length - i) / span);
    });
  });
  years.sort();

  function add(year, name, share) {
    counts[year][name] = (counts[year][name] || 0) + share;
    totals[name] = (totals[name] || 0) + share;
  }

  var total = data.publications.length;
  var sel = [];   /* selected themes; empty means no filter, so everything shows */
  var plot = root.querySelector('.comm-plot');
  var tip = root.querySelector('.comm-tip');
  var svg;

  buildKey();
  root.hidden = false;   /* the plot has to be laid out before it can be measured */
  draw();
  bind();

  /* ---- chart ---- */

  function draw() {
    var w = Math.max(300, plot.clientWidth);
    var h = w < 560 ? 240 : 320;
    var padL = 36, padR = 4, padT = 10, padB = 26;
    var top = niceMax(Math.max.apply(null, years.map(function (y) { return sum(counts[y]); })));
    var step = top / 5;
    var scale = (h - padT - padB) / top;
    var band = (w - padL - padR) / years.length;
    var barW = Math.min(120, band * 0.6);

    svg = node('svg', { viewBox: '0 0 ' + w + ' ' + h, width: w, height: h, class: 'comm-svg' });

    for (var t = 0; t <= 5; t++) {
      var y = h - padB - t * step * scale;
      svg.appendChild(node('line', { class: 'comm-grid', x1: padL, x2: w - padR, y1: y, y2: y }));
      svg.appendChild(text(padL - 7, y + 4, trim(t * step), 'comm-ax comm-ax-y'));
    }

    years.forEach(function (year, i) {
      var base = h - padB;
      var x = padL + i * band + (band - barW) / 2;
      /* Reversed, so the last theme - Untagged - sits at the foot of the bar. */
      var stack = themes.filter(function (name) { return counts[year][name]; }).reverse();
      stack.forEach(function (name, j) {
        var height = counts[year][name] * scale;
        base -= height;
        svg.appendChild(node('path', {
          class: 'comm-bar', d: segment(x, base, barW, height, j === stack.length - 1),
          style: '--c:var(--s' + slot[name] + ')', 'data-comm': name, 'data-year': year
        }));
      });
      svg.appendChild(text(x + barW / 2, h - padB + 17, year, 'comm-ax comm-ax-x'));
    });

    plot.insertBefore(svg, tip);
    paint();
  }

  /* A segment is a plain box, minus a hairline of surface above it so the
     stack reads as parts. The one on top gets the rounded end. */
  function segment(x, y, w, h, top) {
    var gap = h >= 6 ? 2 : 0;
    var r = top ? Math.min(4, (h - gap) / 2, w / 2) : 0;
    var y0 = y + gap, y1 = y + h;
    return 'M' + x + ',' + y1 + 'L' + x + ',' + (y0 + r) +
      (r ? 'Q' + x + ',' + y0 + ' ' + (x + r) + ',' + y0 : '') +
      'L' + (x + w - r) + ',' + y0 +
      (r ? 'Q' + (x + w) + ',' + y0 + ' ' + (x + w) + ',' + (y0 + r) : '') +
      'L' + (x + w) + ',' + y1 + 'Z';
  }

  function redraw() {
    if (svg) svg.remove();
    draw();
  }

  /* ---- key ---- */

  function buildKey() {
    var key = root.querySelector('.comm-key');
    themes.forEach(function (name) {
      if (!totals[name]) return;
      var row = document.createElement('button');
      row.type = 'button';
      row.className = 'comm-row';
      row.setAttribute('data-comm', name);
      row.style.setProperty('--c', 'var(--s' + slot[name] + ')');

      var chip = document.createElement('span');
      chip.className = 'comm-chip';

      var label = document.createElement('span');
      label.className = 'comm-nm';
      label.textContent = name;

      var num = document.createElement('span');
      num.className = 'comm-num';
      num.textContent = totals[name].toFixed(1);

      row.appendChild(chip);
      row.appendChild(label);
      row.appendChild(num);
      key.appendChild(row);
    });
  }

  /* ---- state ---- */

  function dimmed(name) {
    return sel.length > 0 && sel.indexOf(name) === -1;
  }

  function paint() {
    each('.comm-bar', function (bar) { bar.classList.toggle('off', dimmed(bar.getAttribute('data-comm'))); }, svg);
    each('.comm-row', function (row) {
      var name = row.getAttribute('data-comm');
      row.classList.toggle('off', dimmed(name));
      row.setAttribute('aria-pressed', dimmed(name) ? 'false' : 'true');
    }, root);
  }

  /* The first pick narrows to that theme alone; later picks add to the
     selection or drop out of it. Dropping the last one clears the filter. */
  function pick(name) {
    var at = sel.indexOf(name);
    if (!sel.length) sel = [name];
    else if (at === -1) sel.push(name);
    else if (sel.length > 1) sel.splice(at, 1);
    else sel = [];
    paint();
    filter();
  }

  function filter() {
    var active = sel.length ? sel : themes;
    var all = !sel.length;
    var shown = 0;

    each('.pub[data-comm]', function (pub) {
      var tags = pub.getAttribute('data-comm') ? pub.getAttribute('data-comm').split(' ') : [];
      var names = tags.length ? tags.map(function (tag) { return theme[tag] || OTHER; }) : [OTHER];
      var on = all || names.some(function (name) { return active.indexOf(name) !== -1; });
      pub.hidden = !on;
      if (on) shown++;
    });

    each('.yblk', function (blk) {
      var any = !!blk.querySelector('.pub:not([hidden])');
      blk.hidden = !any;
      var link = document.querySelector('.pubnav a[href="#' + blk.id + '"]');
      if (link) link.hidden = !any;
    });

    var count = document.querySelector('[data-comm-count]');
    if (count) count.textContent = shown === total ? total + ' papers' : shown + ' of ' + total + ' papers';
  }

  /* ---- interaction ---- */

  function bind() {
    plot.addEventListener('mousemove', function (e) {
      var bar = e.target.closest('.comm-bar');
      if (!bar) return hover(null);
      hover(bar.getAttribute('data-comm'));
      showTip(e, bar);
    });
    plot.addEventListener('mouseleave', function () { hover(null); });
    plot.addEventListener('click', function (e) {
      var bar = e.target.closest('.comm-bar');
      if (bar) pick(bar.getAttribute('data-comm'));
    });

    var key = root.querySelector('.comm-key');
    key.addEventListener('mouseover', function (e) {
      var row = e.target.closest('.comm-row');
      if (row) hover(row.getAttribute('data-comm'));
    });
    key.addEventListener('mouseleave', function () { hover(null); });
    key.addEventListener('click', function (e) {
      var row = e.target.closest('.comm-row');
      if (row) pick(row.getAttribute('data-comm'));
    });

    var timer;
    window.addEventListener('resize', function () {
      clearTimeout(timer);
      timer = setTimeout(redraw, 150);
    });
  }

  function hover(name) {
    svg.classList.toggle('is-hover', !!name);
    each('.comm-bar', function (bar) { bar.classList.toggle('on', bar.getAttribute('data-comm') === name); }, svg);
    each('.comm-row', function (row) { row.classList.toggle('on', row.getAttribute('data-comm') === name); }, root);
    root.querySelector('.comm-key').classList.toggle('is-hover', !!name);
    if (!name) tip.hidden = true;
  }

  function showTip(e, bar) {
    var name = bar.getAttribute('data-comm');
    var year = bar.getAttribute('data-year');
    tip.textContent = name + ', ' + counts[year][name].toFixed(1) + ' in ' + year;
    tip.hidden = false;
    var box = plot.getBoundingClientRect();
    var x = e.clientX - box.left;
    tip.style.left = Math.min(Math.max(x, 4), box.width - tip.offsetWidth - 4) + 'px';
    tip.style.top = (e.clientY - box.top - tip.offsetHeight - 12) + 'px';
  }

  /* ---- helpers ---- */

  function node(name, attrs) {
    var n = document.createElementNS(NS, name);
    Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    return n;
  }

  function text(x, y, value, cls) {
    var n = node('text', { x: x, y: y, class: cls });
    n.textContent = value;
    return n;
  }

  function each(selector, fn, scope) {
    Array.prototype.forEach.call((scope || document).querySelectorAll(selector), fn);
  }

  function sum(row) {
    return Object.keys(row).reduce(function (acc, k) { return acc + row[k]; }, 0);
  }

  function trim(v) {
    return Math.round(v * 10) % 10 === 0 ? String(Math.round(v)) : v.toFixed(1);
  }

  function niceMax(v) {
    var steps = [1, 2, 5, 10, 20, 25, 50, 100];
    for (var i = 0; i < steps.length; i++) {
      if (v / steps[i] <= 5) return steps[i] * Math.ceil(v / steps[i]);
    }
    return v;
  }
})();
