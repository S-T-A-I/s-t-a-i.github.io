(() => {
  const section = document.querySelector('[data-collaborators-api]');
  if (!section) return;
  const list = section.querySelector('[data-collaborator-list]');
  const status = section.querySelector('[data-collaborator-status]');
  const paragraph = (className, value) => {
    const p = document.createElement('p');
    p.className = className;
    p.textContent = value || '';
    return p;
  };
  let loading = false;
  async function refresh() {
    if (loading) return;
    loading = true;
    try {
      const response = await fetch(section.dataset.collaboratorsApi, { cache: 'no-store', credentials: 'omit' });
      if (!response.ok) throw new Error('Unavailable');
      const payload = await response.json();
      if (!Array.isArray(payload.members)) throw new Error('Invalid member list');
      const people = payload.members.filter(p => p.isCollaborator === true && p.status === 'active');
      const cards = people.map(person => {
        const card = document.createElement('article');
        card.className = 'person';
        card.append(paragraph('nm', person.name), paragraph('rl', person.organisation));
        if (person.bio) card.append(paragraph('text-muted', person.bio));
        if (person.websiteUrl) {
          try {
            const url = new URL(person.websiteUrl);
            if (['http:', 'https:'].includes(url.protocol) && !url.username && !url.password) {
              const link = document.createElement('a');
              link.href = url.href;
              link.rel = 'noopener noreferrer';
              link.textContent = 'Website';
              card.append(link);
            }
          } catch { /* Ignore malformed profile links. */ }
        }
        return card;
      });
      list.replaceChildren(...cards);
      status.textContent = people.length ? '' : 'No public collaborator profiles yet.';
    } catch {
      // Discard old cards if current consent cannot be read.
      list.replaceChildren();
      status.textContent = 'Collaborator profiles are temporarily unavailable.';
    } finally {
      loading = false;
    }
  }
  refresh();
  // Recheck when a visitor returns to a tab and while it remains open.
  window.addEventListener('pageshow', refresh);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refresh(); });
  window.setInterval(() => { if (!document.hidden) refresh(); }, 60000);
})();
