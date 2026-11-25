import test from 'node:test';
import assert from 'node:assert/strict';
import { isTextFile, scanText } from '../scripts/privacy.mjs';

test('privacy scan ignores risk wording and local development examples', () => {
  assert.deepEqual(scanText('risk-' + 'a'.repeat(30)), []);
  assert.deepEqual(scanText('Use http://localhost:4312, http://127.0.0.1:4312 and file:// as generic examples.'), []);
});

test('privacy scan still flags credential patterns, private hosts and real file paths', () => {
  assert.deepEqual(scanText('token = "sk-' + 'a'.repeat(28) + '"'), ['credential']);
  assert.deepEqual(scanText('https://10.12.0.8/private'), ['internal-url']);
  assert.deepEqual(scanText('file:///Users/example/private.md'), ['local-path']);
});

test('privacy scan reads Mermaid diagrams as text', () => {
  assert.equal(isTextFile('assets/system-context-template.mmd'), true);
});
