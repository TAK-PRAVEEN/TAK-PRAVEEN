"""Animated README header (light + dark), fonts embedded so GitHub shows the portfolio's type.

SVG CSS animations play inside <img> on GitHub (no hover/JS — GitHub strips those).
Usage: python -I make-header.py <portfolio-public-dir> <out-dir>
"""
import base64, sys, pathlib

PUB, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
f64 = lambda p: base64.b64encode((PUB / p).read_bytes()).decode()
FONTS = f"""
@font-face{{font-family:IT;src:url(data:font/woff2;base64,{f64('fonts/inter-tight-var.woff2')}) format('woff2');font-weight:100 900}}
@font-face{{font-family:SM;src:url(data:font/woff2;base64,{f64('fonts/space-mono-400.woff2')}) format('woff2')}}
@font-face{{font-family:VA;src:url(data:font/woff2;base64,{f64('fonts/valorant.woff2')}) format('woff2')}}
"""
MASK = f64("icons/monogram-mask.png")

W, H = 1200, 420


def svg(theme: str) -> str:
    bg, fg, mute, line = ("#FAF8F3", "#08090B", "#6b6b70", "#08090B") if theme == "light" else ("#08090B", "#FAF8F3", "#9a9a96", "#FAF8F3")
    LIME = "#CDF22B"
    # Lime is for fills on ivory (unreadable as text there); as text only on black.
    acc_text = fg if theme == "light" else LIME
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>{FONTS}
.m{{font-family:SM,monospace;font-size:14px;letter-spacing:2px;fill:{mute};text-transform:uppercase}}
.n{{font-family:IT,sans-serif;font-weight:700;font-size:120px;letter-spacing:-5px;fill:{fg}}}
.r{{font-family:VA,sans-serif;font-size:36px;letter-spacing:2px}}
@keyframes up{{from{{opacity:0;transform:translateY(40px)}}to{{opacity:1;transform:none}}}}
@keyframes rule{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes glitchA{{0%,86%,100%{{opacity:0;transform:none}}87%{{opacity:1;transform:translate(-5px,-1px)}}90%{{opacity:1;transform:translate(6px,1px)}}93%{{opacity:1;transform:translate(-3px,0)}}96%{{opacity:0}}}}
@keyframes glitchB{{0%,86%,100%{{opacity:0;transform:none}}88%{{opacity:1;transform:translate(5px,1px)}}91%{{opacity:1;transform:translate(-6px,0)}}94%{{opacity:1;transform:translate(3px,-1px)}}97%{{opacity:0}}}}
@keyframes jit{{0%,86%,100%{{transform:none}}88%{{transform:translateX(2px) skewX(-8deg)}}91%{{transform:translateX(-2px)}}94%{{transform:skewX(6deg)}}96%{{transform:none}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes blink{{0%,60%{{opacity:1}}61%,100%{{opacity:0}}}}
@keyframes pulse{{0%,100%{{r:6}}50%{{r:9}}}}
.a1{{animation:up .9s cubic-bezier(.16,1,.3,1) both}}
.a2{{animation:up .9s .15s cubic-bezier(.16,1,.3,1) both}}
.a3{{animation:up .9s .3s cubic-bezier(.16,1,.3,1) both}}
.rule{{transform-origin:60px 0;animation:rule 1.2s cubic-bezier(.65,0,.35,1) both}}
.ga{{animation:glitchA 5.2s steps(1) infinite}} .gb{{animation:glitchB 5.2s steps(1) infinite;mix-blend-mode:{'multiply' if theme=='light' else 'screen'}}}
.jit{{animation:jit 5.2s steps(1) infinite}}
.orbit{{transform-origin:1010px 215px;animation:spin 18s linear infinite}}
.orbit2{{transform-origin:1010px 215px;animation:spin 30s linear infinite reverse}}
.cur{{animation:blink 1s steps(1) infinite}}
.dot{{animation:pulse 2s ease-in-out infinite}}
@keyframes dash{{to{{stroke-dashoffset:-880}}}}
.ring{{animation:dash 9s linear infinite}}
</style>
<rect width="{W}" height="{H}" fill="{bg}"/>
<!-- meta row + rule -->
<g class="a1">
  <text x="60" y="58" class="m">01 — Portfolio 2026</text>
  <text x="600" y="58" class="m" text-anchor="middle">N 26°54′ / E 75°47′</text>
  <circle class="dot" cx="905" cy="53" r="6" fill="{LIME}" stroke="{fg}" stroke-width="1.5"/>
  <text x="1140" y="58" class="m" text-anchor="end">Open to AI / ML roles</text>
</g>
<rect class="rule" x="60" y="76" width="1080" height="2" fill="{line}"/>
<!-- name -->
<text x="54" y="215" class="n a2">Praveen Tak</text>
<!-- role with glitch -->
<g class="a3">
  <rect x="50" y="244" width="430" height="50" rx="4" fill="{LIME}"/>
  <g class="jit"><text x="62" y="282" class="r" fill="#08090B">AI / ML ENGINEER</text></g>
  <text x="62" y="282" class="r ga" fill="#ffffff">AI / ML ENGINEER</text>
  <text x="62" y="282" class="r gb" fill="#6b6b70">AI / ML ENGINEER</text>
  <text x="62" y="338" class="m">01 AI/ML engineering · 02 Full-stack systems · 03 Creative technology<tspan class="cur" fill="{acc_text}"> ▍</tspan></text>
</g>
<!-- orbiting mark -->
<defs>
  <radialGradient id="ball" cx="38%" cy="32%" r="75%">
    <stop offset="0" stop-color="#f1ff9e"/><stop offset=".45" stop-color="{LIME}"/><stop offset="1" stop-color="#8fae0c"/>
  </radialGradient>
</defs>
<g transform="translate(1010 215)">
  <circle r="150" fill="none" stroke="{line}" stroke-opacity=".14" stroke-dasharray="2 8"/>
  <circle r="96" fill="url(#ball)"/>
  <ellipse rx="140" ry="34" fill="none" stroke="{fg}" stroke-width="10" stroke-linecap="round" transform="rotate(-24)" stroke-dasharray="250 630" class="ring"/>
  <ellipse rx="128" ry="52" fill="none" stroke="{fg}" stroke-opacity=".55" stroke-width="2" transform="rotate(18)"/>
</g>
<g class="orbit"><circle cx="1160" cy="215" r="7" fill="{fg}"/></g>
<g class="orbit2"><circle cx="1010" cy="365" r="5" fill="{LIME}" stroke="{fg}" stroke-width="1.5"/></g>
<g transform="translate(960 178)">
  <image width="100" height="76" xlink:href="data:image/png;base64,{MASK}"/>
  <rect x="88.8" y="10.2" width="9.6" height="9.6" fill="#08090B"/>
</g>
<text x="60" y="396" class="m">praveentak.dev</text>
<text x="1140" y="396" class="m" text-anchor="end">Jaipur · IN</text>
</svg>"""


for t in ("light", "dark"):
    (OUT / f"header-{t}.svg").write_text(svg(t), encoding="utf-8")
    print(t, len(svg(t)) // 1024, "KB")
