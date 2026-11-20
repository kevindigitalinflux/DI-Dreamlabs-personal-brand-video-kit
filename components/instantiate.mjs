#!/usr/bin/env node
// Make a Hyperframes demo project from brand.json and the components in this folder.
//
//   node components/instantiate.mjs brand/brand.json videos/demo
//   (use brand/brand.example.json if you have not made brand.json yet)
//
// It writes: <project>/index.html (1080x1920, all components in sequence over a stand-in background),
//            <project>/compositions/*.html, <project>/assets/logos/* (placeholder logos if missing).
// Then run the pinned Hyperframes launcher inside the project:
//   node <launcher> check --timeout 30000 --json     and     node <launcher> preview
// To use YOUR logo: copy it to <project>/assets/logos/primary.svg (or .png and edit the src in offer-card.html).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const [brandPath, projectDir] = process.argv.slice(2);
if (!brandPath || !projectDir) { console.error('usage: node instantiate.mjs <brand.json> <projectDir>'); process.exit(1); }
const brand = JSON.parse(fs.readFileSync(brandPath, 'utf8'));
const c = brand.colors || {};
const f = brand.fonts || {};

const lighten = (hex, k) => {
  const n = parseInt(hex.replace('#', ''), 16);
  const ch = [n >> 16, (n >> 8) & 255, n & 255].map(v => Math.round(v + (255 - v) * k));
  return '#' + ch.map(v => v.toString(16).padStart(2, '0')).join('');
};
const fam = name => (name || '').replace(/\s+(ExtraBold|Bold|Medium|Italic|Regular)\b/gi, '').trim();
const q = s => '"' + s + '"';

let css = fs.readFileSync(path.join(here, 'brand.css'), 'utf8');
const rootBlock = `:root {
  --bg: ${c.background || '#0B1020'};
  --text: ${c.text || '#F5F5F7'};
  --accent: ${c.accent || '#7C3AED'};
  --accent-text: ${c.accentText || '#FFFFFF'};
  --accent-soft: ${lighten(c.accent || '#7C3AED', 0.35)};
  --font-emphasis: ${q(fam(f.emphasis) || 'Montserrat')}, "Arial Black", sans-serif;
  --font-body: ${q(fam(f.body) || 'DM Sans')}, Arial, sans-serif;
  --font-giant: ${q(fam(f.giantCaption) || 'Big Shoulders Display')}, "Arial Narrow", sans-serif;
  --font-serif: ${q(fam(f.accentSerif) || 'Instrument Serif')}, Georgia, serif;
}`;
const before = css;
css = css.replace(/:root \{[\s\S]*?\n\}/, rootBlock);
if (css === before) throw new Error('brand.css :root block not replaced');

const comps = [
  ['hook-giant', 0, 3, 10],
  ['logo-row', 3.5, 4, 11],
  ['checklist', 8, 5, 12],
  ['pay-board', 13.5, 7, 13],
  ['offer-card', 21, 9, 14],
];
const comp = path.join(projectDir, 'compositions');
const logos = path.join(projectDir, 'assets', 'logos');
fs.mkdirSync(comp, { recursive: true });
fs.mkdirSync(logos, { recursive: true });
for (const [name] of comps) fs.copyFileSync(path.join(here, name + '.html'), path.join(comp, name + '.html'));

// placeholder logos so the logo slots render. Replace with real, permitted logos.
const ph = (letter, name) => {
  const p = path.join(logos, name);
  if (fs.existsSync(p)) return;
  fs.writeFileSync(p, `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 72"><circle cx="36" cy="36" r="34" fill="${c.accent || '#7C3AED'}"/><text x="36" y="48" font-family="Arial" font-weight="800" font-size="34" text-anchor="middle" fill="${c.accentText || '#FFFFFF'}">${letter}</text></svg>`);
};
ph('A', 'logo-a.svg'); ph('B', 'logo-b.svg'); ph('C', 'logo-c.svg'); ph('D', 'logo-d.svg'); ph('Y', 'primary.svg');

const total = 30.5;
const mounts = comps.map(([name, start, dur, track]) =>
  `<div id="${name}" class="clip scene-host" data-start="${start}" data-duration="${dur}" data-track-index="${track}" data-width="1080" data-height="1920" data-composition-id="${name}" data-composition-src="compositions/${name}.html"></div>`).join('\n');

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>${(brand.name || 'Brand').replace(/</g, '')} component demo</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
${css}
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:var(--bg)}
#main{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;background:linear-gradient(180deg,color-mix(in srgb,var(--bg) 70%,#556) 0,var(--bg) 100%)}
.stand-in{position:absolute;left:290px;top:760px;width:500px;height:900px;border-radius:250px 250px 40px 40px;background:color-mix(in srgb,var(--text) 14%,transparent)}
.scene-host{position:absolute;left:0;top:0;width:1080px;height:1920px;pointer-events:none}
</style></head><body>
<div id="main" data-composition-id="main" data-start="0" data-duration="${total}" data-width="1080" data-height="1920">
<div id="stand-in" class="stand-in clip" data-start="0" data-duration="${total}" data-track-index="1"></div>
${mounts}
<div id="caption-demo" class="clip caption-slot" data-start="1" data-duration="1" data-track-index="40"><span class="caption-art" data-safe="caption">your <strong>caption</strong></span></div>
</div>
<script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});tl.to({},{duration:${total}},0);window.__timelines["main"]=tl;</script>
</body></html>
`;
fs.writeFileSync(path.join(projectDir, 'index.html'), html);
console.log('wrote', path.join(projectDir, 'index.html'), 'and', comps.length, 'components');
