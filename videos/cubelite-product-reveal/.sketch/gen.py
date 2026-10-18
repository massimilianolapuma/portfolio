# Generates the static sketch poses for the storyboard board (no motion yet).
import os
FR = [
 ("01-too-many-contexts", 4), ("02-one-interface", 5), ("03-discover-switch-manage", 6),
 ("04-local-first", 6), ("05-native", 5), ("06-cta", 4),
]
FONTS = """
@font-face { font-family: "Inter"; src: url("assets/fonts/inter-latin-400-normal.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Inter"; src: url("assets/fonts/inter-latin-500-normal.woff2") format("woff2"); font-weight: 500; }
@font-face { font-family: "Inter"; src: url("assets/fonts/inter-latin-700-normal.woff2") format("woff2"); font-weight: 700; }
@font-face { font-family: "Inter"; src: url("assets/fonts/inter-latin-800-normal.woff2") format("woff2"); font-weight: 800; }
@font-face { font-family: "JetBrains Mono"; src: url("assets/fonts/jetbrains-mono-latin-400-normal.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "JetBrains Mono"; src: url("assets/fonts/jetbrains-mono-latin-500-normal.woff2") format("woff2"); font-weight: 500; }
"""
def base(p):
    return f"""
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; color: #F1F5F9; font-family: "Inter", sans-serif;
  --paper: #0F172A; --paper-2: #1E293B; --ink: #F1F5F9; --accent: #60A5FA; --muted: #94A3B8; --border: #334155; --live: #30D098; --hover: #93C5FD; }}
.{p}-bg {{ position: absolute; inset: 0; background-color: var(--paper);
  background-image: linear-gradient(rgba(96,165,250,0.07) 1px, transparent 1px), linear-gradient(90deg, rgba(96,165,250,0.07) 1px, transparent 1px);
  background-size: 40px 40px; background-position: 0 0; }}
.{p}-rule {{ position: absolute; left: 80px; right: 80px; height: 1px; background: var(--border); }}
.{p}-chrome {{ position: absolute; bottom: 22px; font: 500 18px "JetBrains Mono", monospace; color: var(--muted); letter-spacing: 0.04em; }}
.{p}-layer {{ position: absolute; inset: 0; }}
.{p}-mono {{ font-family: "JetBrains Mono", monospace; }}
"""
def doc(fid, dur, p, idx, css, body):
    return f"""<template id="{fid}">
  <div id="root" data-composition-id="{fid}" data-width="1920" data-height="1080" data-duration="{dur}">
    <style>{FONTS}{base(p)}{css}
    </style>
    <div id="{p}-bg" class="{p}-bg clip" data-start="0" data-duration="{dur}" data-track-index="0">
      <div class="{p}-rule" style="top: 58px"></div>
      <div class="{p}-rule" style="top: 1021px"></div>
      <div class="{p}-chrome" style="left: 80px">CubeLite · Kubernetes Context Aggregator</div>
      <div class="{p}-chrome" style="right: 80px">{idx:02d} / 06</div>
    </div>
    <div id="{p}-stage" class="{p}-layer clip" data-start="0" data-duration="{dur}" data-track-index="1">
{body}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script>
      // Sketch pose only — motion arrives in the build pass.
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["{fid}"] = tl;
      tl.seek(0);
    </script>
  </div>
</template>
"""
out = {}

# ── 01 ──
chips = [("prod-eu-west-1",150,140,-3),("staging",560,110,2),("dev-local",1290,130,-2),("kind-cubelite",1600,210,3),
 ("minikube",110,330,2),("gke_prod_europe",1540,360,-2),("docker-desktop",90,700,-3),("eks-analytics",1560,680,2),
 ("aks-payments",230,880,2),("qa-2",720,890,-2),("sandbox",1180,880,3),("k3d-demo",1620,880,-3),
 ("preprod",420,250,-1),("ci-runners",1120,250,2),("homelab",330,760,-2),("edge-cluster",1330,780,1)]
css1 = """
.f01-chip { position: absolute; padding: 12px 20px; border: 1px solid var(--border); border-radius: 10px; background: var(--paper-2);
  font: 500 26px "JetBrains Mono", monospace; color: var(--muted); white-space: nowrap; }
.f01-chip::before { content: ""; display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--border); margin-right: 12px; vertical-align: middle; }
.f01-head { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }
.f01-head h1 { margin: 0; font-weight: 800; font-size: 118px; line-height: 1.0; letter-spacing: -0.035em; text-align: center; max-width: 1400px; }
.f01-head h1 span { color: var(--accent); }
"""
b1 = "\n".join(f'      <div class="f01-chip" style="left:{x}px; top:{y}px; transform: rotate({r}deg)">{n}</div>' for n,x,y,r in chips)
b1 += '\n      <div class="f01-head"><h1>Too many Kubernetes <span>contexts?</span></h1></div>'
out["01-too-many-contexts"] = ("f01", css1, b1)

# ── 02 ──
nodes = [(-640,-170,"prod-eu-west-1"),(-330,-250,"staging"),(330,-250,"dev-local"),(640,-170,"kind-cubelite"),(-700,130,"minikube"),(-380,290,"gke_prod"),(380,290,"eks-analytics"),(700,130,"docker-desktop")]
cx, cy = 960, 540
css2 = """
.f02-head { position: absolute; top: 110px; left: 0; right: 0; text-align: center; font-weight: 700; font-size: 84px; letter-spacing: -0.03em; }
.f02-lines { position: absolute; inset: 0; }
.f02-node { position: absolute; padding: 10px 18px; border: 1px solid var(--border); border-radius: 10px; background: var(--paper-2);
  font: 500 22px "JetBrains Mono", monospace; color: var(--muted); white-space: nowrap; transform: translate(-50%, -50%); }
.f02-lock { position: absolute; left: 0; right: 0; top: 410px; display: flex; flex-direction: column; align-items: center; gap: 14px; }
.f02-mark { display: flex; align-items: center; gap: 30px; }
.f02-mark img { width: 128px; height: 128px; border-radius: 28px; }
.f02-mark b { font-weight: 800; font-size: 150px; letter-spacing: -0.04em; line-height: 1; }
.f02-tag { font: 500 34px "JetBrains Mono", monospace; color: var(--accent); }
"""
import math
def edge(dx,dy,rx=520,ry=175):
    t=1/math.sqrt((dx/rx)**2+(dy/ry)**2); return cx+dx*t, cy+20+dy*t
lines = "".join(f'<line x1="{edge(dx,dy)[0]:.0f}" y1="{edge(dx,dy)[1]:.0f}" x2="{cx+dx}" y2="{cy+dy}" />' for dx,dy,_ in nodes)
lines += f'<ellipse cx="{cx}" cy="{cy+20}" rx="520" ry="175" stroke-opacity="0.25" />'
b2 = f'      <svg class="f02-lines" viewBox="0 0 1920 1080" fill="none" stroke="#60A5FA" stroke-opacity="0.45" stroke-width="2">{lines}</svg>\n'
b2 += "\n".join(f'      <div class="f02-node" style="left:{cx+dx}px; top:{cy+dy}px">{n}</div>' for dx,dy,n in nodes)
b2 += '\n      <div class="f02-head">One unified interface.</div>'
b2 += '\n      <div class="f02-lock"><div class="f02-mark"><img src="assets/favicon.png" alt="" /><b>CubeLite</b></div><div class="f02-tag">Kubernetes Context Aggregator</div></div>'
out["02-one-interface"] = ("f02", css2, b2)

# ── 03 ──
css3 = """
.f03-verbs { position: absolute; left: 120px; top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center; gap: 6px; }
.f03-verbs div { font-weight: 800; font-size: 128px; letter-spacing: -0.04em; line-height: 1.02; color: #475569; }
.f03-verbs div.on { color: var(--ink); }
.f03-panel { position: absolute; left: 980px; top: 230px; width: 820px; border: 1px solid var(--border); border-radius: 16px; background: var(--paper-2); overflow: hidden; }
.f03-bar { padding: 18px 26px; border-bottom: 1px solid var(--border); font: 500 22px "JetBrains Mono", monospace; color: var(--muted); }
.f03-row { position: relative; display: flex; align-items: center; gap: 18px; padding: 20px 26px; font: 500 30px "JetBrains Mono", monospace; color: var(--muted); }
.f03-row i { width: 14px; height: 14px; border-radius: 50%; background: var(--border); }
.f03-row.on { background: rgba(96,165,250,0.14); color: var(--ink); box-shadow: inset 4px 0 0 var(--accent); }
.f03-row.on i { background: var(--live); box-shadow: 0 0 0 6px rgba(48,208,152,0.18); }
.f03-cap { position: absolute; left: 980px; top: 770px; font-weight: 600; font-size: 40px; color: var(--accent); letter-spacing: -0.01em; }
.f03-cursor { position: absolute; left: 1560px; top: 418px; width: 34px; height: 46px; }
"""
rows = ["prod-eu-west-1","staging","dev-local","kind-cubelite","minikube"]
b3 = '      <div class="f03-verbs"><div>Discover.</div><div class="on">Switch.</div><div>Manage.</div></div>\n'
b3 += '      <div class="f03-panel"><div class="f03-bar">contexts · 3 kubeconfig files</div>' + "".join(f'<div class="f03-row{" on" if r=="staging" else ""}"><i></i>{r}</div>' for r in rows) + '</div>\n'
b3 += '      <svg class="f03-cursor" viewBox="0 0 34 46"><path d="M2 2 L2 38 L11 29 L18 44 L24 41 L17 27 L30 27 Z" fill="#F1F5F9" stroke="#0F172A" stroke-width="2" stroke-linejoin="round"/></svg>\n'
b3 += '      <div class="f03-cap">One-click context switching</div>'
out["03-discover-switch-manage"] = ("f03", css3, b3)

# ── 04 ──
css4 = """
.f04-text { position: absolute; left: 120px; top: 0; bottom: 0; width: 800px; display: flex; flex-direction: column; justify-content: center; gap: 34px; }
.f04-text h2 { margin: 0; font-weight: 800; font-size: 112px; letter-spacing: -0.04em; line-height: 0.98; }
.f04-sub { font-weight: 500; font-size: 40px; color: var(--muted); }
.f04-neg { font-weight: 700; font-size: 50px; color: var(--accent); letter-spacing: -0.02em; line-height: 1.15; }
.f04-perim { position: absolute; left: 1000px; top: 190px; width: 620px; height: 700px; border: 2px dashed #475569; border-radius: 28px; }
.f04-perim-label { position: absolute; left: 1028px; top: 170px; padding: 0 12px; background: var(--paper); font: 500 24px "JetBrains Mono", monospace; color: var(--muted); }
.f04-keychain { position: absolute; left: 1060px; top: 380px; width: 500px; border: 1px solid var(--border); border-radius: 16px; background: var(--paper-2); }
.f04-kc-head { display: flex; align-items: center; gap: 14px; padding: 18px 24px; border-bottom: 1px solid var(--border); font-weight: 700; font-size: 30px; }
.f04-kc-row { padding: 16px 24px; font: 500 24px "JetBrains Mono", monospace; color: var(--muted); }
.f04-kc-row b { color: var(--ink); font-weight: 500; }
.f04-cloud { position: absolute; left: 1700px; top: 500px; font: 500 24px "JetBrains Mono", monospace; color: #475569; }
.f04-cut { position: absolute; inset: 0; }
"""
b4 = '      <div class="f04-text"><h2>Local-first by design.</h2><div class="f04-sub">Credentials in your Keychain</div><div class="f04-neg"><div>No telemetry.</div><div>No cloud account.</div></div></div>\n'
b4 += '      <div class="f04-perim"></div><div class="f04-perim-label">your machine</div>\n'
b4 += '      <div class="f04-keychain"><div class="f04-kc-head"><svg width="34" height="34" viewBox="0 0 34 34" fill="none" stroke="#60A5FA" stroke-width="3"><circle cx="11" cy="17" r="7"/><path d="M18 17 H31 M26 17 V23 M31 17 V22"/></svg>Keychain</div>'
b4 += '<div class="f04-kc-row"><b>client-cert</b> · prod-eu-west-1</div><div class="f04-kc-row"><b>bearer-token</b> · staging</div><div class="f04-kc-row"><b>client-cert</b> · dev-local</div></div>\n'
b4 += '      <svg class="f04-cut" viewBox="0 0 1920 1080" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="8 8"><path d="M1560 470 H1690"/><path d="M1560 560 H1690"/></svg>\n'
b4 += '      <svg class="f04-cut" viewBox="0 0 1920 1080" fill="none" stroke="#94A3B8" stroke-width="3"><path d="M1608 455 l24 30 M1632 455 l-24 30"/><path d="M1608 545 l24 30 M1632 545 l-24 30"/></svg>\n'
b4 += '      <div class="f04-cloud">cloud</div>'
out["04-local-first"] = ("f04", css4, b4)

# ── 05 ──
css5 = """
.f05-head { position: absolute; left: 120px; top: 150px; font-weight: 800; font-size: 112px; letter-spacing: -0.04em; line-height: 1; }
.f05-cards { position: absolute; left: 120px; right: 120px; top: 380px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.f05-card { border: 1px solid var(--border); border-radius: 20px; background: var(--paper-2); padding: 44px 48px; min-height: 470px; display: flex; flex-direction: column; gap: 22px; }
.f05-card.main { box-shadow: inset 0 3px 0 var(--accent); }
.f05-kicker { font: 500 24px "JetBrains Mono", monospace; color: var(--accent); }
.f05-title { display: flex; align-items: center; gap: 22px; font-weight: 800; font-size: 76px; letter-spacing: -0.035em; line-height: 1; }
.f05-pill { font: 500 22px "JetBrains Mono", monospace; color: var(--muted); border: 1px solid #475569; border-radius: 99px; padding: 6px 16px; letter-spacing: 0; }
.f05-line { font: 500 32px "JetBrains Mono", monospace; color: var(--ink); }
.f05-line.dim { color: var(--muted); }
"""
b5 = '      <div class="f05-head">Native where you work.</div>\n'
b5 += '      <div class="f05-cards">'
b5 += '<div class="f05-card main"><div class="f05-kicker">native app</div><div class="f05-title">macOS</div><div class="f05-line">Swift 6 + SwiftUI</div><div class="f05-line dim">menu-bar quick-switch + main window</div><div class="f05-line dim">macOS 14+</div></div>'
b5 += '<div class="f05-card"><div class="f05-kicker">cross-platform</div><div class="f05-title">Desktop <span class="f05-pill">early preview</span></div><div class="f05-line">Tauri v2</div><div class="f05-line dim">macOS · Linux · Windows</div></div>'
b5 += '</div>'
out["05-native"] = ("f05", css5, b5)

# ── 06 ──
css6 = """
.f06-lock { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px; padding-bottom: 40px; }
.f06-mark { display: flex; align-items: center; gap: 34px; }
.f06-mark img { width: 128px; height: 128px; border-radius: 28px; }
.f06-mark b { font-weight: 800; font-size: 176px; letter-spacing: -0.045em; line-height: 1; }
.f06-tag { font-weight: 500; font-size: 58px; letter-spacing: -0.02em; color: var(--ink); }
.f06-url { position: relative; font: 500 38px "JetBrains Mono", monospace; color: var(--accent); padding-bottom: 12px; margin-top: 18px; }
.f06-url::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 2px; background: var(--accent); }
"""
b6 = '      <div class="f06-lock"><div class="f06-mark"><img src="assets/favicon.png" alt="" /><b>CubeLite</b></div><div class="f06-tag">Kubernetes contexts, without the friction.</div><div class="f06-url">massimilianolapuma.github.io/cubelite</div></div>'
out["06-cta"] = ("f06", css6, b6)

for i,(fid,dur) in enumerate(FR, start=1):
    p, css, body = out[fid]
    open(f"compositions/frames/{fid}.html","w").write(doc(fid, dur, p, i, css, body))
print("ok")
