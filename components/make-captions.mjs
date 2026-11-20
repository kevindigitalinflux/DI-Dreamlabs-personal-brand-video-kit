#!/usr/bin/env node
// Turn word timings into caption clips (1 to 3 words each) for the low caption band.
//
//   node components/make-captions.mjs words.json captions.html [keywords.txt]
//
// words.json: [{"word":"Designers,","start":0.12,"end":0.7}, ...]  (seconds, final-video clock, after cuts)
// keywords.txt (optional): one word per line to show as emphasis (accent colour, outlined).
// Output: HTML lines to paste inside the #main composition of your index.html (they use .caption-slot and
// .caption-art from brand.css). Each caption lasts until the next one starts, capped at 0.4 s per word, so
// speech is never covered by a stale caption. Check centring (x 540) and contrast on the ENCODED frame.
import fs from 'node:fs';

const [wordsPath, outPath, kwPath] = process.argv.slice(2);
if (!wordsPath || !outPath) { console.error('usage: node make-captions.mjs words.json captions.html [keywords.txt]'); process.exit(1); }
const words = JSON.parse(fs.readFileSync(wordsPath, 'utf8'));
const keys = new Set(kwPath ? fs.readFileSync(kwPath, 'utf8').split(/\r?\n/).map(s => s.trim().toLowerCase()).filter(Boolean) : []);
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const norm = s => s.toLowerCase().replace(/[^a-z0-9%$£€.-]/g, '');

// group: up to 3 words, break on gaps over 0.35 s or after sentence-ending punctuation
const groups = []; let cur = [];
for (let i = 0; i < words.length; i++) {
  const w = words[i];
  const gap = cur.length ? w.start - cur[cur.length - 1].end : 0;
  if (cur.length && (cur.length >= 3 || gap > 0.35)) { groups.push(cur); cur = []; }
  cur.push(w);
  if (/[.!?]$/.test(w.word)) { groups.push(cur); cur = []; }
}
if (cur.length) groups.push(cur);

const lines = groups.map((g, i) => {
  const start = g[0].start;
  const next = groups[i + 1] ? groups[i + 1][0].start : g[g.length - 1].end + 0.3;
  const dur = Math.max(0.2, Math.min(next - start, 0.4 * g.length + 0.1));
  const text = g.map(w => keys.has(norm(w.word)) ? `<strong>${esc(w.word)}</strong>` : esc(w.word)).join(' ');
  return `<div id="caption-${i}" class="clip caption-slot" data-start="${start.toFixed(3)}" data-duration="${dur.toFixed(3)}" data-track-index="40"><span class="caption-art" data-safe="caption">${text}</span></div>`;
});
fs.writeFileSync(outPath, lines.join('\n') + '\n');
console.log('wrote', lines.length, 'captions to', outPath);
