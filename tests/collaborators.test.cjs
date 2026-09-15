const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync('static/js/collaborators.js', 'utf8');
class Element {
  children = [];
  textContent = '';
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; }
}
async function fixture(members) {
  const list = new Element(), status = new Element();
  const events = new Map();
  const state = { members, failed: false };
  const section = { dataset: { collaboratorsApi: 'https://example.test/members' },
    querySelector: key => key.includes('list') ? list : status };
  runInNewContext(source, {
    document: { querySelector: () => section, createElement: () => new Element(), hidden: false,
      addEventListener: (key, fn) => events.set(key, fn) },
    window: { addEventListener: (key, fn) => events.set(key, fn), setInterval: () => {} },
    URL,
    fetch: async (_url, options) => {
      assert.equal(options.cache, 'no-store'); assert.equal(options.credentials, 'omit');
      return { ok: !state.failed, json: async () => ({ members: state.members }) };
    },
  });
  await new Promise(resolve => setImmediate(resolve));
  return { list, status, state, refresh: events.get('pageshow') };
}
test('only active collaborators appear and profile content stays plain text', async () => {
  const f = await fixture([
    { isCollaborator: true, status: 'active', name: '<img onerror=alert(1)>', organisation: 'Example University', websiteUrl: 'javascript:alert(1)' },
    { isCollaborator: true, status: 'archived', name: 'Archived' },
    { status: 'active', name: 'Ordinary member' },
  ]);
  assert.equal(f.list.children.length, 1);
  assert.equal(f.list.children[0].children[0].textContent, '<img onerror=alert(1)>');
  assert.equal(f.list.children[0].children.length, 2);
});
test('withdrawal and failed requests remove previously visible cards', async () => {
  const person = { isCollaborator: true, status: 'active', name: 'Example Person' };
  const f = await fixture([person]);
  f.state.members = [];
  await f.refresh();
  assert.equal(f.list.children.length, 0);
  f.state.members = [person];
  await f.refresh();
  assert.equal(f.list.children.length, 1);
  f.state.failed = true;
  await f.refresh();
  assert.equal(f.list.children.length, 0);
  assert.match(f.status.textContent, /unavailable/);
});
test('website links permit only http and https without credentials', async () => {
  for (const [websiteUrl, expectedLinks] of [['https://example.test', 1], ['https://user:pass@example.test', 0], ['/relative', 0]]) {
    const f = await fixture([{ isCollaborator: true, status: 'active', name: 'Example Person', websiteUrl }]);
    assert.equal(f.list.children[0].children.filter(n => n.href).length, expectedLinks);
  }
});
