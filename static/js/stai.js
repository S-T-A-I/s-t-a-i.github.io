/* STAI — mobile nav + follow the OS colour scheme. No jQuery, no framework. */
(function () {
  function prefersDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function apply() {
    document.documentElement.classList.toggle('dark-mode', prefersDark());
  }

  document.addEventListener('click', function (e) {
    var tog = e.target.closest('[data-nav-toggle]');
    if (tog) {
      e.preventDefault();
      var nav = document.getElementById('sitenav');
      if (nav) {
        var open = nav.classList.toggle('open');
        tog.setAttribute('aria-expanded', open ? 'true' : 'false');
      }
      return;
    }
    // close the mobile menu after following a link
    if (e.target.closest('#sitenav a')) {
      var n = document.getElementById('sitenav');
      if (n) n.classList.remove('open');
    }
  });

  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    if (mq.addEventListener) mq.addEventListener('change', apply);
    else if (mq.addListener) mq.addListener(apply);
  }

  if (document.readyState !== 'loading') apply();
  else document.addEventListener('DOMContentLoaded', apply);
})();
