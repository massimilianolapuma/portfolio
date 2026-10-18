---
format: 1920x1080
duration: 30s
message: "CubeLite makes it simple to discover, switch and manage Kubernetes contexts from one interface — fast, local and privacy-respecting."
arc: Hook (pain) → Product intro → Feature cycle → Local-first trust → Native platforms → CTA
audience: developers and platform engineers who juggle many Kubernetes clusters
mode: collaborative
music: minimal precise electronic underscore, soft steady pulse, discreet, clean, no big drops
captions: none (no narration; every line is on-screen type)
---

<!-- No narration: every frame's copy is on screen (verbatim from the brief). `voiceover` stays empty;
     reveals pace to the on-screen cues listed in `onscreen`. Claims are limited to the six the brief
     lists, each traceable to capture/extracted/visible-text.txt. No invented app UI. -->

## Video direction

- **Palette (frame.md roles):** ground `paper` #0F172A with the faint blue graph grid and the two `border` hairlines on every frame; raised panels/chips `paper-2` #1E293B with a 1px `border` edge; text `ink` #F1F5F9; secondary `muted` #94A3B8; the ONE accent `ink-soft` #60A5FA for the active/selected thing, connection lines and one key word per headline; `live` #30D098 only for the small "active context" dot. No other hues (the "cut" marks in frame 4 are `muted`, not red).
- **Type:** display = Inter 800 (tight tracking, sentence case) for every headline; JetBrains Mono for every technical token (context names, kubeconfig paths, `Keychain` rows, platform stacks, the URL). Fonts ship in `assets/fonts/` — declare them with `@font-face` in every frame.
- **Motion grammar:** smooth long-tail decel (`power3.out` default, `expo.out` for the one hero arrival per frame); no bounce, no overshoot, no elastic. Entrances are short rises/fades/draws; reveals follow the on-screen copy order (this film has no voice-over — the copy IS the cue track). Nothing appears before its cue; the back half of each frame keeps resolving pieces rather than freezing a full canvas.
- **Holds:** frame 2 ends on a held lockup (~1.5s still), frame 5 ends on a held two-card read, frame 6 is the long held end card. During holds: stillness; at most subtle jitter or a live SVG internal (dash-flow on a connection line, the green dot's soft halo) — never breathing cards, never a back-half pan/push.
- **Legibility:** every headline stays fully readable and still for ≥ 1.2s; secondary copy for ≥ 0.8s. All content sits in the top ~83% (above y≈896) except the persistent footer chrome under the bottom hairline.
- **Negative list:** no app screenshots or fake app UI (panels stay abstract: labelled rectangles, rows, nodes, lines); no stock imagery, datacenters, robots, falling code, hooded hackers, fake Kubernetes dashboards; no glow-heavy "AI" gradients; no QR/pixel-glitch decor; no slideshow (front-load then freeze) and no screensaver (everything floating independently).
- **Continuity:** the same footer chrome (`CubeLite · Kubernetes Context Aggregator` left, `NN / 06` right) and hairlines sit still on every frame so cuts read as one film. Static sketch layouts in `boards/stills/` are approved — dress them, don't redraw them.

## Frame 1 — Too many contexts

- scene: A scatter of small mono context chips (prod-eu, staging, dev-local, kind-cubelite…) drifts in from every edge, crowding the frame; the headline lands; the chips converge and collapse into one bright blue point at center
- voiceover: ""
- onscreen: "Too many Kubernetes contexts?"
- duration: 4s
- transition_in: cut
- status: animated
- src: compositions/frames/01-too-many-contexts.html
- type: hook
- persuasion: Pain validation (rhetorical question the viewer answers "yes" to)
- beat: overwhelm → curiosity
- blueprint: compose
- focal: none (typography + abstract chips)
- roles: —
- sfx: none
- handoff_out: blue point — x 960, y 540 (frame center), 28px circle `ink-soft`, scale 1, opacity 1, static at the cut (all chips already absorbed)
- asset_candidates:

narrativeRole: name the daily friction in the viewer's own words and turn the clutter into a single point of focus.
keyMessage: context sprawl is the problem; there is one place it can resolve.
source: visible-text "Discover, switch, and manage Kubernetes contexts" — the chips are contexts, the convergence previews "aggregator".

Scene 1 (0.0–1.1s): empty grid ground; context chips (mono, `paper-2` with border, grey dot) drift in from all four edges with a small stagger and slight rotations, settling into the scattered sketch positions — layered-depth, chips at two sizes/opacities so the back layer reads deeper (keep the lowest row above y≈860). → center-outward-expansion run in reverse (edges → scattered rest)
Scene 2 (1.1–2.6s): "Too many Kubernetes contexts?" rises word-group by word-group, centered, `contexts?` in the accent; chips keep a barely-there jitter. Headline dominates (≥3:1 over chips). → per-word staggered reveal
Scene 3 (2.6–3.4s): headline holds still (readable); chips accelerate toward center along straight paths, shrinking and fading as they converge. → center-outward-expansion (inverted: cluster inward)
Scene 4 (3.4–4.0s): the headline fades up and out; everything collapses into one small blue point at exact center that holds for the cut. → scale-swap

## Frame 2 — One unified interface

- scene: The center point expands into an ordered node system — clusters as nodes on the faint grid, connected by thin blue lines into one hub; the CubeLite icon and wordmark resolve at the hub
- voiceover: ""
- onscreen: "One unified interface." · "CubeLite" · "Kubernetes Context Aggregator"
- duration: 5s
- transition_in: cut
- status: animated
- src: compositions/frames/02-one-interface.html
- type: product_intro
- persuasion: Order from chaos (negative contrast with frame 1)
- beat: relief + clarity
- blueprint: logo-assemble-lockup (Adapt)
- focal: assets/favicon.png
- roles: favicon = hub mark (128px, never upscaled) · nodes = supporting
- sfx: none
- handoff_in: blue point — x 960, y 540, 28px circle `ink-soft`, scale 1, opacity 1, static at the cut
- asset_candidates: assets/favicon.png — CubeLite app icon (blue isometric cube, green status dot), 128px

narrativeRole: land the value claim by beat 2 — every context, one interface — and name the product.
keyMessage: CubeLite brings every context into one place.
source: h1 "CubeLite", tagline "Kubernetes Context Aggregator", "from a unified interface".

Adapt: keep "the mark comes to exist built from parts" — the point opens into the hub ring and the node system orders itself around it; no CTA push-through (that's the close, not the intro).
Scene 1 (0.0–1.4s): the incoming point expands into the hub ellipse outline (self-drawing stroke); 8 context nodes slide from loose positions into their ordered ring slots around it while connector lines draw from each node to the ellipse edge. Centered, ring ~70% of frame width. → svg-path-draw
Scene 2 (1.4–2.6s): "One unified interface." rises at the top, centered; connectors get a slow dash-flow toward the hub (live SVG internal, low intensity). → per-word staggered reveal
Scene 3 (2.6–3.6s): inside the hub, the app icon arrives (fade + small rise, no upscale) and "CubeLite" reveals left→right beside it; then the mono tagline "Kubernetes Context Aggregator" in the accent fades up below. → spring-pop-entrance (smooth settle, no overshoot)
Scene 4 (3.6–5.0s): held lockup — still; only the dash-flow keeps moving.

## Frame 3 — Discover. Switch. Manage.

- scene: Three verbs cycle on a fixed left anchor, each with its own abstract proof on the right — Discover: KUBECONFIG paths merge into one list (multi-kubeconfig); Switch: one click moves the green active dot to another context; Manage: a menu-bar strip with a quick-switch dropdown of context names
- voiceover: ""
- onscreen: "Discover." · "Switch." · "Manage." · "Multi-kubeconfig" · "One-click context switching" · "Menu-bar quick-switch"
- duration: 6s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-discover-switch-manage.html
- type: feature_showcase
- persuasion: Rule of three + feature-to-benefit translation
- beat: control + ease
- blueprint: fixed-anchor-cycle (Adapt)
- focal: none (abstract panels)
- roles: —
- sfx: none
- asset_candidates:

narrativeRole: prove the promise with the three actions it names, each tied to one verifiable feature.
keyMessage: find every context, switch in one click, from the menu bar.
source: "Multi-Kubeconfig — resolves KUBECONFIG env paths, merges multiple files"; "Switch active Kubernetes context with a single click"; "Menu Bar Quick-Switch — click the status-bar icon to switch context".

Adapt: keep the anchor-unmoved / world-changes signature — the left verb column never moves, only its lit word and the right-hand proof change; three proofs instead of N tokens.
Scene 1 (0.0–0.5s): left column "Discover. / Switch. / Manage." rises in, all three in the dim inactive tone (#475569); asymmetric 45/55 split. → per-word staggered reveal
Scene 2 (0.5–2.2s): "Discover." lights to `ink`; right side: three mono path chips `~/.kube/config`, `~/.kube/work.yaml`, `~/.kube/lab.yaml` appear stacked, then slide together and merge into one contexts panel (header "contexts · 3 kubeconfig files", 5 mono rows) — caption under it: "Multi-kubeconfig". → center-outward-expansion (merge); card-morph-anchor
Scene 3 (2.2–4.0s): "Discover." dims, "Switch." lights; in the same panel a pointer glides to `staging`, a single click (small press + ripple), the green `live` dot and the accent row highlight move from `prod-eu-west-1` to `staging`; caption swaps to "One-click context switching". → cursor-click-ripple; hard-cut caption swap (discrete-text-sequence)
Scene 4 (4.0–6.0s): "Switch." dims, "Manage." lights; the panel scales down and docks up into an abstract menu-bar strip at the top of the right area (a thin bar with the CubeLite cube glyph drawn as 3 tinted rhombi, NOT a real menu bar screenshot) with a small dropdown listing three context names, active one with the green dot; caption swaps to "Menu-bar quick-switch". Ends with all three verbs lit `ink` for a 0.6s hold so the full line reads. → card-morph-anchor; discrete-text-sequence

## Frame 4 — Local-first by design

- scene: A drawn rounded perimeter labelled "your machine"; a credential token (key glyph + "client cert / bearer token") settles into a Keychain panel inside it; outbound lines toward a dimmed "cloud" edge are cut at the boundary; the two negations stamp in
- voiceover: ""
- onscreen: "Local-first by design." · "Credentials in your Keychain" · "No telemetry. No cloud account."
- duration: 6s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/04-local-first.html
- type: benefit_highlight
- persuasion: Risk reversal (privacy as a default, not a setting)
- beat: trust + peace of mind
- asset_candidates:

narrativeRole: remove the objection a platform engineer has about any tool touching cluster credentials.
keyMessage: nothing leaves the machine; secrets live in the Keychain.
source: "Bearer tokens and client certificates stored in the OS Keychain — never in plain text config files"; "Zero analytics, zero call-home, zero cloud accounts".

- focal: none (abstract perimeter + Keychain panel)
- roles: —
- sfx: none

Scene 1 (0.0–1.2s): "Local-first by design." rises on the left (asymmetric 45/55); on the right the dashed rounded perimeter draws itself and its mono label "your machine" fades in. → per-word staggered reveal; svg-path-draw
Scene 2 (1.2–3.0s): three credential rows (`client-cert · prod-eu-west-1`, `bearer-token · staging`, `client-cert · dev-local`) slide in from the left edge of the perimeter and settle into the Keychain panel, whose key glyph draws on; sub-line "Credentials in your Keychain" fades up under the headline. → dynamic-content-sequencing; svg-path-draw
Scene 3 (3.0–4.6s): two dashed lines start to run from the panel toward the dim "cloud" label at the right edge and are cut exactly at the perimeter — a `muted` ✕ stamps on each break, the outside segments fade away. → svg-path-draw (stopped) + css-marker-patterns (cross)
Scene 4 (4.6–6.0s): "No telemetry." then "No cloud account." land in the accent under the sub-line, one after the other; hold still. → kinetic-beat-slam in its smooth register (no overshoot)

## Frame 5 — Native where you work

- scene: Two abstract platform cards assemble side by side (no app screenshots): "macOS — native Swift 6 + SwiftUI, menu bar + main window, macOS 14+" and "Desktop — cross-platform with Tauri v2: macOS · Linux · Windows", the second tagged "early preview"
- voiceover: ""
- onscreen: "Native where you work." · "macOS · SwiftUI" · "Desktop · Tauri — macOS, Linux, Windows"
- duration: 5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-native.html
- type: feature_showcase
- persuasion: Authority by craft (native stack) + reach (cross-platform)
- beat: confidence
- blueprint: grid-card-assemble (Adapt)
- focal: none (abstract platform cards)
- roles: —
- sfx: none
- asset_candidates:

narrativeRole: show it fits the viewer's machine and feels native, without inventing UI.
keyMessage: a real native Mac app, and a desktop build for every OS.
source: "Native Swift 6 + SwiftUI menu-bar and main window. macOS 14+"; "Cross-platform via Tauri v2"; download list macOS / Linux AppImage / Linux deb / Windows; "CubeLite Desktop — early preview".

Adapt: two cards instead of a grid; keep the staggered self-assemble cascade; no camera zoom-out.
Scene 1 (0.0–1.0s): "Native where you work." rises top-left. → per-word staggered reveal
Scene 2 (1.0–2.4s): the macOS card assembles from below (border draws, fill fades, accent top edge sweeps left→right); inside, lines reveal in order: kicker "native app", title "macOS", then mono "Swift 6 + SwiftUI", "menu-bar quick-switch + main window", "macOS 14+". Two-column, left card first. → grid-card-assemble cascade; dynamic-content-sequencing
Scene 3 (2.4–3.6s): the Desktop card assembles the same way to its right: "cross-platform", "Desktop" + the "early preview" pill, mono "Tauri v2", then "macOS · Linux · Windows" with the three names revealing one by one. → dynamic-content-sequencing
Scene 4 (3.6–5.0s): held two-card read, still.

## Frame 6 — Without the friction

- scene: Clean dark end card: icon + "CubeLite" wordmark, the tagline below, the URL in mono as the call to action with a thin blue underline that draws on; grid fades to near-black for a clean final fade-out
- voiceover: ""
- onscreen: "CubeLite" · "Kubernetes contexts, without the friction." · "massimilianolapuma.github.io/cubelite"
- duration: 4s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-cta.html
- type: cta
- persuasion: Friction reduction (the promise restated as a feeling) + clear next step
- beat: ease → motivation
- blueprint: titlecard-reveal (Adapt)
- focal: assets/favicon.png
- roles: favicon = mark beside the wordmark (128px)
- sfx: none
- asset_candidates: assets/favicon.png — CubeLite app icon, 128px

narrativeRole: leave the viewer with the name, the promise and exactly where to go.
keyMessage: CubeLite — go to the site.
source: brief closing line; site URL.

Adapt: centered end card; reveal mark → name → line → URL in sequence, final fade is the film's only real exit.
Scene 1 (0.0–0.9s): icon fades/rises into place and "CubeLite" reveals left→right beside it, centered. → spring-pop-entrance (smooth)
Scene 2 (0.9–1.7s): "Kubernetes contexts, without the friction." rises beneath. → per-word staggered reveal
Scene 3 (1.7–2.6s): the mono URL types/reveals and its accent underline draws left→right. → svg-path-draw (underline) + discrete-text-sequence
Scene 4 (2.6–3.4s): held end card, still.
Scene 5 (3.4–4.0s): whole card + grid fade to the plain dark ground (film exit; music fades with it).
