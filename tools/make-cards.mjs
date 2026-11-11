/**
 * Portfolio-style project cards for the GitHub profile README (light + dark).
 * Run from the portfolio folder: node make-cards.mjs <outDir>
 */
import { chromium } from "playwright";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const OUT = resolve(process.argv[2]);
mkdirSync(OUT, { recursive: true });
const ROOT = resolve(".");
const f = (p) => pathToFileURL(join(ROOT, p)).href;

const cards = [
  { id: "rtcom", n: "P—01", meta: "DESIGO® Milk · In daily use", title: "RTCOM® — DESIGO's Operating System", text: "Six connected apps that trace milk from farm to doorstep for ~2,100 customers and 30+ riders.", stack: ["Flutter", "Supabase", "React 19", "Postgres RLS"], img: "src/assets/work/rtcom-erp.jpg", nums: [["2,100", "customers"], ["3,491", "DB tests"]] },
  { id: "milkofit", n: "L—01", meta: "Computer vision · R&D", title: "Reading a 16-Test Milk Card", text: "Finds a milk-adulteration test card in a phone photo and reads all 16 reaction pads.", stack: ["OpenCV", "YOLO", "Python"], img: "src/assets/lab/milkofit-pads.jpg", nums: [["16/16", "pads located"], ["~1 px", "placement error"]] },
  { id: "crew", n: "L—02", meta: "Computer vision · In progress", title: "Crew Fit Check — PPE Detection", text: "Checks helmet, crew jacket, gloves and shoes from one photo before the morning round.", stack: ["YOLO11", "Grounding DINO", "OCR"], img: "src/assets/lab/crew-fit-check.jpg", nums: [["9", "classes"], ["PASS/FAIL", "verdict"]] },
  { id: "wholeway", n: "P—02", meta: "Wholeway® · Live — wholeway.org", title: "Wholeway® — Website", text: "Brand website for bajra cookies and dairy, with an interactive 3D map of where they are made.", stack: ["Astro", "three.js", "Blender"], img: "src/assets/work/wholeway-cover.jpg", pos: "right center" },
  { id: "desigo-site", n: "P—03", meta: "DESIGO® Milk · Live", title: "DESIGO® Milk — Website", text: "Editorial brand site telling the story of traceable milk, from indigenous cow to glass bottle.", stack: ["Next.js 16", "GSAP", "Lenis"], img: "src/assets/work/desigo-site-master26.png" },
  { id: "kandy", n: "P—04", meta: "Concept · Jodhpur bakery", title: "Kandy Crumbs — Website", text: "Menu that builds your order as a receipt, and a five-step cake studio that sends to WhatsApp.", stack: ["Astro", "Vercel"], img: "src/assets/work/kandy-crumbs-hero.jpg", pos: "left center" },
];

const FONTS = `
@font-face{font-family:IT;src:url("${f("public/fonts/inter-tight-var.woff2")}");font-weight:100 900}
@font-face{font-family:SM;src:url("${f("public/fonts/space-mono-400.woff2")}")}
@font-face{font-family:PX;src:url("${f("public/fonts/ibm-plex-sans-400.woff2")}")}`;

const html = (c, dark) => {
  const LIME = "#CDF22B";
  const bg = dark ? "#08090B" : "#FAF8F3", fg = dark ? "#FAF8F3" : "#08090B", mute = dark ? "#9a9a96" : "#6b6b70", line = dark ? "#2a2b2e" : "#dcd9cf";
  return `<!doctype html><html><head><meta charset="utf-8"><style>${FONTS}
*{margin:0;box-sizing:border-box}html,body{width:1200px;height:760px;background:${bg};overflow:hidden}
.c{position:absolute;inset:0;padding:44px 48px;border:2px solid ${line};border-radius:28px;color:${fg};font-family:PX}
.m{font-family:SM;font-size:16px;letter-spacing:2.4px;text-transform:uppercase;color:${mute}}
.top{display:flex;justify-content:space-between;padding-bottom:14px;border-bottom:2px solid ${fg}}
.top b{background:${LIME};color:#08090B;font-weight:400;padding:3px 8px;border-radius:4px}
h2{font-family:IT;font-weight:700;letter-spacing:-2px;font-size:58px;line-height:1;margin:30px 0 16px;max-width:620px}
p{font-size:23px;line-height:1.45;color:${mute};max-width:560px}
.img{position:absolute;right:48px;top:118px;width:470px;height:470px;border-radius:18px;overflow:hidden;border:1px solid ${line};background:#080809}
.img img{width:100%;height:100%;object-fit:cover;object-position:top center}
.nums{display:flex;gap:40px;margin-top:28px}.nums div{border-left:4px solid ${LIME};padding-left:12px}
.nums strong{display:block;font-family:IT;font-size:40px;letter-spacing:-1px;color:${fg}}
.stack{position:absolute;left:48px;bottom:44px;display:flex;gap:10px;flex-wrap:wrap;max-width:600px}
.stack span{font-family:SM;font-size:15px;letter-spacing:1.5px;text-transform:uppercase;padding:8px 12px;border:1px solid ${line};border-radius:999px;color:${fg}}
.go{position:absolute;right:48px;bottom:38px;font-family:SM;font-size:16px;letter-spacing:2px;text-transform:uppercase;background:${LIME};color:#08090B;padding:10px 18px;border-radius:999px}
</style></head><body><div class="c">
<div class="top m"><span><b>${c.n}</b>&nbsp; ${c.meta}</span><span>praveentak.dev</span></div>
<h2>${c.title}</h2><p>${c.text}</p>
${c.nums ? `<div class="nums">${c.nums.map(([v, l]) => `<div><strong>${v}</strong><span class="m">${l}</span></div>`).join("")}</div>` : ""}
<div class="img"><img src="${f(c.img)}" style="object-position:${c.pos ?? "top center"}"></div>
<div class="stack">${c.stack.map((s) => `<span>${s}</span>`).join("")}</div>
<div class="go">Open case study →</div>
</div></body></html>`;
};

const b = await chromium.launch({ channel: "msedge" });
const p = await b.newPage({ viewport: { width: 1200, height: 760 }, deviceScaleFactor: 1 });
const tmp = join(OUT, "_t.html");
for (const c of cards) for (const dark of [false, true]) {
  writeFileSync(tmp, html(c, dark));
  await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: join(OUT, `card-${c.id}-${dark ? "dark" : "light"}.png`) });
}
await b.close();
console.log("cards done");
