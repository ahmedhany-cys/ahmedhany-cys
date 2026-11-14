#!/usr/bin/env python3
"""Builds the profile README visuals: a light/dark banner and window-framed project covers.

Usage: python scripts/build_assets.py

Screenshot covers read their JPEG from assets/src/ and embed it, so each cover is a single
self-contained SVG. Terminal covers are drawn from the text in this file. No dependencies.
"""
import base64
import math
import random
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
WORK = ASSETS / "work"
WORK.mkdir(parents=True, exist_ok=True)

SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'

# --------------------------------------------------------------------------- banner
# Cloud security, in motion. One large cloud is built from horizontal bands of light that slide
# at different speeds, with a slipstream behind it. On top sits the security story: a shield in
# the cloud, a scan beam sweeping it, a patrolled perimeter, and threats stopped at the edge.
# Graphite throughout (black, grey, white) with one amber accent and red only for threats.
# Two colourings of one composition: near-black for dark mode, charcoal for light mode.

BW, BH = 1200, 360

THEMES = {
    "dark": dict(sky=("#09090B", "#18181B", "#2C2C31"), glow="0.12", border="0.12"),
    "light": dict(sky=("#141416", "#232327", "#3A3A40"), glow="0.14", border="0.00"),
}
PALE, GREY, ACCENT, THREAT = "#E4E4E7", "#A1A1AA", "#FBBF24", "#F87171"
SUB, SMALL, SLASH = "#C4C4CC", "#E4E4E7", "#71717A"

# cloud outline: four circles standing on one base line, relative to the cloud's centre
REL = [(-170, 40, 70), (-78, -34, 84), (58, -52, 100), (172, 26, 84)]
REL_BASE = 110
CX, CY, SCALE = 902, 190, 1.08
SHIELD = "M0 -52 L40 -38 V-6 C40 24 21 42 0 51 C-21 42 -40 24 -40 -6 V-38 Z"
TICK = "M-18 -3 L-5 10 L19 -16"
THREAT_STARTS = [(850, -20), (1215, -10), (1215, 372), (1000, 380), (700, -20)]  # where threats come from
TRAIL = [(118, 468, 150, 2.6), (150, 420, 190, 3.4), (186, 452, 170, 2.2), (222, 404, 210, 3.0),
         (258, 470, 140, 2.8), (290, 500, 110, 3.6)]                             # y, x, length, seconds


def cloud(cx, cy, s=1.0) -> str:
    """Outline of the cloud as an SVG path, traced arc by arc."""
    lobes = [(cx + x * s, cy + y * s, r * s) for x, y, r in REL]
    base = cy + REL_BASE * s

    def upper(c1, c2):
        (x1, y1, r1), (x2, y2, r2) = c1, c2
        d = math.hypot(x2 - x1, y2 - y1)
        a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
        h = math.sqrt(max(0.0, r1 * r1 - a * a))
        mx, my = x1 + a * (x2 - x1) / d, y1 + a * (y2 - y1) / d
        pts = [(mx + h * (y2 - y1) / d, my - h * (x2 - x1) / d), (mx - h * (y2 - y1) / d, my + h * (x2 - x1) / d)]
        return min(pts, key=lambda q: q[1])

    stops = [(lobes[0][0], base)] + [upper(lobes[i], lobes[i + 1]) for i in range(len(lobes) - 1)] + [(lobes[-1][0], base)]
    d = f"M{lobes[-1][0]:.1f} {base:.1f} H{lobes[0][0]:.1f}"
    for (x, y, r), (ax, ay), (bx, by) in zip(lobes, stops, stops[1:]):
        sweep = (math.atan2(by - y, bx - x) - math.atan2(ay - y, ax - x)) % (2 * math.pi)
        d += f" A{r:.1f} {r:.1f} 0 {1 if sweep > math.pi else 0} 1 {bx:.1f} {by:.1f}"
    return d + " Z"


def bands():
    """The sliding bands that fill the cloud: one <line> and one @keyframes rule per row."""
    rng = random.Random(9)   # fixed seed, so every build draws the same cloud
    top, base = CY + (-52 - 100) * SCALE, CY + REL_BASE * SCALE
    lines, frames = [], []
    y, i = top + 15, 0
    while y < base - 6:
        segs = [rng.choice([34, 52, 76, 110, 150, 190]) for _ in range(4)]
        gaps = [rng.choice([16, 22, 30]) for _ in range(4)]
        dash = " ".join(f"{a} {b}" for a, b in zip(segs, gaps))
        dur = rng.choice([7, 9, 11, 13, 16])
        op = rng.choice([0.55, 0.7, 0.85, 1.0])
        lines.append(f'      <line x1="560" y1="{y:.0f}" x2="1240" y2="{y:.0f}" stroke-dasharray="{dash}" '
                     f'stroke-opacity="{op}" style="animation:slide{i} {dur}s linear infinite;animation-delay:-{rng.uniform(0, dur):.1f}s"/>')
        frames.append(f"    @keyframes slide{i} {{ to {{ stroke-dashoffset: -{sum(segs) + sum(gaps)}; }} }}")
        y += 21
        i += 1
    return "\n".join(lines), "\n".join(frames)


def threats(cx, cy, rx, ry) -> str:
    """Dots that fly in from outside and are stopped, with a flash, where they meet the perimeter."""
    out, cycle = "", 6.5
    for k, (sx, sy) in enumerate(THREAT_STARTS):
        dx, dy = sx - cx, sy - cy
        t = 1 / math.sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
        ex, ey = cx + dx * t, cy + dy * t
        begin = -k * cycle / len(THREAT_STARTS)
        out += f"""    <g class="motion">
      <g opacity="0">
        <circle r="8" fill="{THREAT}" opacity="0.3"/><circle r="3.4" fill="{THREAT}"/>
        <animateMotion dur="{cycle}s" begin="{begin:.2f}s" repeatCount="indefinite" path="M{sx} {sy} L{ex:.1f} {ey:.1f}" keyPoints="0;1;1" keyTimes="0;0.4;1" calcMode="linear"/>
        <animate attributeName="opacity" dur="{cycle}s" begin="{begin:.2f}s" repeatCount="indefinite" values="0;1;1;0;0" keyTimes="0;0.05;0.4;0.44;1"/>
      </g>
      <circle cx="{ex:.1f}" cy="{ey:.1f}" r="3" fill="none" stroke="{THREAT}" stroke-width="2" opacity="0">
        <animate attributeName="r" dur="{cycle}s" begin="{begin:.2f}s" repeatCount="indefinite" values="3;3;20;20" keyTimes="0;0.4;0.56;1"/>
        <animate attributeName="opacity" dur="{cycle}s" begin="{begin:.2f}s" repeatCount="indefinite" values="0;0;1;0;0" keyTimes="0;0.39;0.4;0.56;1"/>
      </circle>
    </g>
"""
    return out


def banner(theme: str) -> str:
    c = THEMES[theme]
    shape = cloud(CX, CY, SCALE)
    lines, frames = bands()
    px, py, rx, ry = CX, CY + 6, 300, 148          # the perimeter
    ring = f"M{px - rx} {py} A{rx} {ry} 0 1 1 {px + rx} {py} A{rx} {ry} 0 1 1 {px - rx} {py}"
    trail = "".join(
        f'      <line x1="{x0}" y1="{y}" x2="{x0 + ln}" y2="{y}" stroke-dasharray="26 18" '
        f'style="animation:wind {dur}s linear infinite;animation-delay:-{k * 0.5:.1f}s"/>\n'
        for k, (y, x0, ln, dur) in enumerate(TRAIL))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{BW}" height="{BH}" viewBox="0 0 {BW} {BH}" role="img" aria-labelledby="t d">
  <title id="t">Ahmed Hany, cloud security engineer</title>
  <desc id="d">Detection and response engineering on AWS, Azure and Kubernetes. A cloud built from sliding bands of light carries a shield. A scan beam sweeps it and threats are stopped at its perimeter.</desc>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c["sky"][0]}"/><stop offset="0.55" stop-color="{c["sky"][1]}"/><stop offset="1" stop-color="{c["sky"][2]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="{CX}" cy="{CY}" r="440" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="{c["glow"]}"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="band" x1="640" y1="0" x2="1170" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF"/><stop offset="0.5" stop-color="{PALE}"/><stop offset="1" stop-color="{GREY}"/>
    </linearGradient>
    <linearGradient id="trailfade" x1="400" y1="0" x2="650" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/>
    </linearGradient>
    <mask id="tm"><rect width="{BW}" height="{BH}" fill="url(#trailfade)"/></mask>
    <linearGradient id="rimlight" x1="0" y1="20" x2="0" y2="320" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"/><stop offset="0.6" stop-color="#FFFFFF" stop-opacity="0.15"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.42"/>
    </linearGradient>
    <filter id="aura" x="-30%" y="-40%" width="160%" height="180%"><feGaussianBlur stdDeviation="26"/></filter>
    <clipPath id="shape"><path d="{shape}"/></clipPath>
    <clipPath id="frame"><rect width="{BW}" height="{BH}" rx="16"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .hero {{ animation: bob 8s ease-in-out infinite; }}
{frames}
    .perim {{ stroke-dasharray: 3 9; animation: march 2.6s linear infinite; }}
    .scan {{ animation: scan 5.5s ease-in-out infinite; }}
    .shield {{ stroke-dasharray: 100; animation: draw 8s ease-in-out infinite; }}
    .tick {{ stroke-dasharray: 100; animation: tick 8s ease-in-out infinite; }}
    @keyframes march {{ to {{ stroke-dashoffset: -24; }} }}
    @keyframes scan {{ 0% {{ transform: translateX(0); opacity: 0; }} 8% {{ opacity: 1; }} 62% {{ transform: translateX(680px); opacity: 1; }} 70%, 100% {{ transform: translateX(680px); opacity: 0; }} }}
    @keyframes draw {{ 0% {{ stroke-dashoffset: 100; }} 30%, 100% {{ stroke-dashoffset: 0; }} }}
    @keyframes tick {{ 0%, 30% {{ stroke-dashoffset: 100; }} 45%, 100% {{ stroke-dashoffset: 0; }} }}
    @keyframes wind {{ to {{ stroke-dashoffset: -44; }} }}
    @keyframes bob {{ 0%, 100% {{ transform: translateY(3px); }} 50% {{ transform: translateY(-5px); }} }}
    @media (prefers-reduced-motion: reduce) {{
      .hero, .hero line, .trail line, .perim, .shield, .tick {{ animation: none !important; }}
      .scan, .motion {{ display: none; }}
    }}
  </style>

  <g clip-path="url(#frame)">
    <rect width="{BW}" height="{BH}" fill="url(#sky)"/>
    <rect width="{BW}" height="{BH}" fill="url(#glow)"/>

    <!-- slipstream -->
    <g class="trail" mask="url(#tm)" stroke="{PALE}" stroke-opacity="0.5" stroke-width="2.5" stroke-linecap="round">
{trail}    </g>

    <g class="hero">
      <path d="{shape}" fill="{GREY}" opacity="0.5" filter="url(#aura)"/>

      <!-- perimeter and its patrol -->
      <path class="perim" d="{ring}" fill="none" stroke="{PALE}" stroke-opacity="0.55" stroke-width="1.3" stroke-linecap="round"/>
      <g class="motion">
        <circle r="10" fill="{ACCENT}" opacity="0.35"><animateMotion dur="14s" repeatCount="indefinite" path="{ring}"/></circle>
        <circle r="4.5" fill="#FFFFFF"><animateMotion dur="14s" repeatCount="indefinite" path="{ring}"/></circle>
      </g>

      <!-- the cloud: bands of light sliding inside its outline -->
      <path d="{shape}" fill="#FFFFFF" fill-opacity="0.07"/>
      <g clip-path="url(#shape)" stroke="url(#band)" stroke-width="11" stroke-linecap="round">
{lines}
      </g>
      <path d="{shape}" fill="none" stroke="url(#rimlight)" stroke-width="1.6"/>

      <!-- scan beam -->
      <g clip-path="url(#shape)">
        <g class="scan">
          <rect x="{px - rx - 70}" y="0" width="90" height="{BH}" fill="url(#beam)"/>
          <rect x="{px - rx + 18}" y="0" width="2" height="{BH}" fill="#FFFFFF" opacity="0.85"/>
        </g>
      </g>

      <!-- shield -->
      <g transform="translate({px} {py + 6})" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round">
        <path d="{SHIELD}" fill="{c["sky"][1]}" fill-opacity="0.55" stroke="#FFFFFF" stroke-opacity="0.4" stroke-width="1.5"/>
        <path class="shield" pathLength="100" d="{SHIELD}" stroke-width="3.2"/>
        <path class="tick" pathLength="100" d="{TICK}" stroke-width="4.5"/>
      </g>
    </g>

    <!-- threats, stopped at the perimeter -->
{threats(px, py, rx, ry)}  </g>
  <rect x="0.5" y="0.5" width="{BW - 1}" height="{BH - 1}" rx="16" fill="none" stroke="#FFFFFF" stroke-opacity="{c["border"]}"/>

  <!-- identity -->
  <text x="72" y="112" class="sans" font-size="13" font-weight="600" letter-spacing="3.6" fill="{ACCENT}">CLOUD SECURITY ENGINEER</text>
  <text x="68" y="196" class="sans" font-size="82" font-weight="700" letter-spacing="-2.6" fill="#FFFFFF">Ahmed Hany</text>
  <text x="72" y="238" class="sans" font-size="22" fill="{SUB}">Detection and response engineering</text>
  <text x="72" y="292" class="sans" font-size="12.5" font-weight="600" letter-spacing="3" fill="{SMALL}">AWS<tspan dx="14" fill="{SLASH}">/</tspan><tspan dx="14">AZURE</tspan><tspan dx="14" fill="{SLASH}">/</tspan><tspan dx="14">KUBERNETES</tspan></text>
</svg>
"""


# --------------------------------------------------------------------------- covers

W, BAR, H = 1200, 44, 675  # content area is 16:9
WIN = dict(bg="#0D1117", bar="#161B22", border="#30363D", dot="#3D444D", title="#9198A1")


def window(title: str, alt: str, body: str, defs: str = "") -> str:
    total = BAR + H
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{total}" viewBox="0 0 {W} {total}" role="img" aria-labelledby="t">
  <title id="t">{alt}</title>
  <defs>
    <clipPath id="win"><rect x="1" y="1" width="{W - 2}" height="{total - 2}" rx="15"/></clipPath>
{defs}  </defs>
  <style>.mono {{ font-family: {MONO}; }}</style>
  <g clip-path="url(#win)">
    <rect width="{W}" height="{total}" fill="{WIN["bg"]}"/>
{body}
    <rect width="{W}" height="{BAR}" fill="{WIN["bar"]}"/>
    <line x1="0" y1="{BAR}" x2="{W}" y2="{BAR}" stroke="{WIN["border"]}" stroke-width="2"/>
    <circle cx="30" cy="22" r="6.5" fill="{WIN["dot"]}"/>
    <circle cx="52" cy="22" r="6.5" fill="{WIN["dot"]}"/>
    <circle cx="74" cy="22" r="6.5" fill="{WIN["dot"]}"/>
    <text x="{W // 2}" y="27" class="mono" font-size="15" fill="{WIN["title"]}" text-anchor="middle">{title}</text>
  </g>
  <rect x="1" y="1" width="{W - 2}" height="{total - 2}" rx="15" fill="none" stroke="{WIN["border"]}" stroke-width="2"/>
</svg>
'''


def shot(src: Path, title: str, alt: str) -> str:
    data = base64.b64encode(src.read_bytes()).decode()
    body = (f'    <image x="0" y="{BAR}" width="{W}" height="{H}" preserveAspectRatio="xMidYMin slice" '
            f'href="data:image/jpeg;base64,{data}"/>')
    return window(title, alt, body)


FG, DIMC, BLUE, ORANGE, YELLOW, GREEN, GREY = "#C9D1D9", "#8B949E", "#7AA2F7", "#FF9E64", "#E0AF68", "#9ECE6A", "#6E7681"
X0, LH, FS = 48, 43, 23


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def term(title: str, alt: str, rows: list) -> str:
    """rows: list of (gap_before_px, [(x, fill, weight, text), ...])"""
    y = BAR + 60
    out = [f'    <g class="mono" font-size="{FS}" fill="{FG}" xml:space="preserve">']
    for gap, spans in rows:
        y += gap
        parts = "".join(
            "<tspan" + (f' x="{x}"' if x is not None else "") + f' fill="{fill}"'
            + (' font-weight="700"' if bold else "") + f">{esc(t)}</tspan>"
            for x, fill, bold, t in spans
        )
        out.append(f'      <text x="{X0}" y="{y}">{parts}</text>')
        y += LH
    out.append("    </g>")
    return window(title, alt, "\n".join(out))


def trustmint() -> str:
    def row(level, colour, ident, cloud, provider, access):
        return (0, [(X0, colour, True, level), (206, FG, False, ident), (640, DIMC, False, cloud),
                    (740, GREY, False, "<-"), (790, FG, False, provider), (960, DIMC, False, access)])
    rows = [
        (0, [(X0, BLUE, False, "$ trustmint scan -s examples/acme/snapshot.json")]),
        (0, [(X0, FG, False, "TrustMint 0.1.0: 20 federation trusts")]),
        (0, [(X0, FG, False, "Findings: "), (None, ORANGE, False, "11 critical"), (None, FG, False, ", 7 high, 3 medium, 1 low, 4 info")]),
        (22, [(X0, DIMC, False, "WHO CAN MINT A TOKEN EACH IDENTITY ACCEPTS")]),
        row("PUBLIC", ORANGE, "role/gh-release-main", "aws", "github", "write"),
        row("PUBLIC", ORANGE, "projects/acme-artifacts", "gcp", "gitlab", "write"),
        row("TENANT", YELLOW, "role/gh-org-admin", "aws", "github", "admin"),
        row("TENANT", YELLOW, "platform-automation", "azure", "github", "admin"),
        row("PROJECT", BLUE, "role/tfc-prod-network", "aws", "terraform", "admin"),
        row("PROTECTED", GREEN, "role/gh-payments-immutable", "aws", "github", "write"),
        row("NONE", GREY, "role/gh-web-broken", "aws", "github", "write"),
        (22, [(X0, GREY, False, "Synthetic Acme estate from examples/acme. Every ID is made up.")]),
    ]
    return term("trustmint", "TrustMint scan of the synthetic Acme estate: 20 federation trusts ranked from PUBLIC to NONE by who can mint a token each identity accepts", rows)


def attackpath() -> str:
    def f(sev, colour, text):
        return (0, [(X0, colour, True, sev), (182, FG, False, text)])
    rows = [
        (0, [(X0, BLUE, False, "$ python -m attackpath analyze \\")]),
        (0, [(X0, BLUE, False, "    --input fixtures/sample_environment.json --output reports/")]),
        (0, [(X0, FG, False, "environment: synthetic-demo-account (synthetic, account 111111111111)")]),
        (0, [(X0, FG, False, "findings: "), (None, ORANGE, False, "critical=4"), (None, FG, False, ", high=22, medium=11, low=8, informational=4")]),
    ]
    findings = [
        ("CRITICAL", ORANGE, "Instance legacy-jump is reachable from the internet on all ports"),
        ("CRITICAL", ORANGE, "User legacy-automation can reach role ops-admin-legacy in 1 step(s)"),
        ("CRITICAL", ORANGE, "Role vendor-support-access can be assumed by any AWS principal"),
        ("CRITICAL", ORANGE, "Role ops-admin-legacy has administrative permissions"),
        ("HIGH", YELLOW, "User legacy-automation may assume any role matching a broad pattern"),
        ("HIGH", YELLOW, "User break-glass-admin has administrative permissions"),
        ("HIGH", YELLOW, "User ci-deployer may pass any role to AWS services"),
        ("HIGH", YELLOW, "Function public-webhook can be invoked by anyone"),
    ]
    for i, (sev, colour, text) in enumerate(findings):
        gap, spans = f(sev, colour, text)
        rows.append((22 if i == 0 else 0, spans))
    rows.append((0, [(X0, GREY, False, "... 41 more")]))
    return term("attackpath", "AWS Cloud Attack Path Analyzer run on its synthetic demo account: 49 findings, 4 of them critical, including a one-step path from a user to an admin role", rows)


def main() -> None:
    (ASSETS / "banner-dark.svg").write_text(banner("dark"))
    (ASSETS / "banner-light.svg").write_text(banner("light"))
    src = ASSETS / "src"
    (WORK / "kubeshield.svg").write_text(shot(
        src / "kubeshield.jpg", "kubeshield · security overview",
        "KubeShield security overview of a local lab cluster: open incidents, high and critical events, vulnerable images, policy violations and detection activity by source"))
    (WORK / "honeytrap.svg").write_text(shot(
        src / "honeytrap.jpg", "aws-honeytrap · live proof of concept, 2026-10-31",
        "AWS HoneyTrap dashboard filtered to live data from the proof of concept: 23 events, 11 sessions and 8 sources, with IPs pseudonymised"))
    (WORK / "sentinel.svg").write_text(shot(
        src / "sentinel.jpg", "supplychain-sentinel · demonstration data",
        "Azure SupplyChain Sentinel security overview: six analysed releases with PASS, FAIL and INDETERMINATE decisions on demonstration data"))
    (WORK / "trustmint.svg").write_text(trustmint())
    (WORK / "attackpath.svg").write_text(attackpath())
    for p in sorted(list(ASSETS.glob("banner-*.svg")) + list(WORK.glob("*.svg"))):
        print(f"{p.relative_to(REPO)}  {p.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
