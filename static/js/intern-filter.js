// Members page: show only members who are looking for interns.
(function () {
  var button = document.querySelector('[data-intern-filter]');
  var groups = document.getElementById('member-groups');
  if (!button || !groups) return;
  button.hidden = false;
  button.addEventListener('click', function () {
    var on = button.getAttribute('aria-pressed') !== 'true';
    button.setAttribute('aria-pressed', String(on));
    groups.classList.toggle('only-interns', on);
  });
})();
