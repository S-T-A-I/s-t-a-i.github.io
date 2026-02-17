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
    var label = document.querySelector('.theme-toggle-dropdown .theme-label');
    if (label) {
      var theme = getStoredTheme();
      label.textContent = theme === 'light' ? 'Light' : theme === 'dark' ? 'Dark' : 'System';
    }
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
