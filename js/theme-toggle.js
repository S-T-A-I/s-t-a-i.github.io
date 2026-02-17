(function() {
  var STORAGE_KEY = 'theme-preference';

  function getStoredTheme() {
    return localStorage.getItem(STORAGE_KEY) || 'system';
  }

  function setStoredTheme(value) {
    localStorage.setItem(STORAGE_KEY, value);
  }

  function prefersDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function resolveDark() {
    var theme = getStoredTheme();
    return theme === 'dark' || (theme === 'system' && prefersDark());
  }

  function applyTheme() {
    var dark = resolveDark();
    document.documentElement.classList.toggle('dark-mode', dark);
    updateDropdownLabel();
  }

  function updateDropdownLabel() {
    var theme = getStoredTheme();
    var text = theme === 'light' ? 'Light' : theme === 'dark' ? 'Dark' : 'System';
    var labels = document.querySelectorAll('.theme-toggle-dropdown .theme-label');
    labels.forEach(function(label) { label.textContent = text; });
  }

  function handleChoice(e) {
    var choice = e.target && e.target.getAttribute && e.target.getAttribute('data-theme-choice');
    if (!choice) return;
    e.preventDefault();
    setStoredTheme(choice);
    applyTheme();
  }

  document.addEventListener('DOMContentLoaded', function() {
    applyTheme();
    document.addEventListener('click', function(e) {
      if (e.target.closest('[data-theme-choice]')) {
        handleChoice(e);
      }
    });
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addListener(function() {
        if (getStoredTheme() === 'system') applyTheme();
      });
    }
  });
})();
