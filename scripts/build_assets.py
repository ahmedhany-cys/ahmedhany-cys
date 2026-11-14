#!/usr/bin/env python3
"""Builds the profile README visuals: a light/dark banner and window-framed project covers.

Usage: python scripts/build_assets.py

Screenshot covers read their JPEG from assets/src/ and embed it, so each cover is a single
self-contained SVG. Terminal covers are drawn from the text in this file. No dependencies.
"""
import base64
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
WORK = ASSETS / "work"
WORK.mkdir(parents=True, exist_ok=True)

SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'

# --------------------------------------------------------------------------- banner
# A neural network held inside a cloud, drawn as line art: one thin contour for the cloud,
# hairlines joining each layer to the next, small nodes, one cool accent, one warm output and
# slow light. Two colourings of one composition, both navy with light type, so it holds up on
# either GitHub theme.

BW, BH = 1200, 380

THEMES = {
    "dark": dict(base=("#0B1020", "#0D1529", "#090E1B"), glow="0.22", border="0.10"),
    "light": dict(base=("#101C36", "#152647", "#0E1930"), glow="0.28", border="0.00"),
}
LINE, NODE, ACCENT, WARM = "#A9BAD6", "#D8E2F1", "#7FB2FF", "#E6BE8A"

# cloud = four circles sitting on one base line; the contour is traced arc by arc
BASE = 318
LOBES = [(704, 238, 80), (806, 150, 88), (952, 142, 102), (1068, 230, 88)]
COLUMNS = [676, 764, 852, 940, 1028, 1116]   # the network's layers
PAD, STEP = 24, 44                           # inset from the contour, node spacing
ROUTES = [0.5, 0.2, 0.8]                     # heights at which light crosses the cloud


def _upper_intersection(c1, c2):
    (x1, y1, r1), (x2, y2, r2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(r1 * r1 - a * a)
    mx, my = x1 + a * (x2 - x1) / d, y1 + a * (y2 - y1) / d
    pts = [(mx + h * (y2 - y1) / d, my - h * (x2 - x1) / d), (mx - h * (y2 - y1) / d, my + h * (x2 - x1) / d)]
    return min(pts, key=lambda q: q[1])


def cloud_path() -> str:
    """Contour of the cloud as an SVG path."""
    stops = [(LOBES[0][0], BASE)]
    stops += [_upper_intersection(LOBES[i], LOBES[i + 1]) for i in range(len(LOBES) - 1)]
    stops += [(LOBES[-1][0], BASE)]
    d = f"M{LOBES[-1][0]} {BASE} H{LOBES[0][0]}"
    for (cx, cy, r), (ax, ay), (bx, by) in zip(LOBES, stops, stops[1:]):
        sweep = (math.atan2(by - cy, bx - cx) - math.atan2(ay - cy, ax - cx)) % (2 * math.pi)
        d += f" A{r} {r} 0 {1 if sweep > math.pi else 0} 1 {bx:.1f} {by:.1f}"
    return d + " Z"


def _extent(x):
    """Top and bottom of the cloud at this x."""
    tops = [cy - math.sqrt(r * r - (x - cx) ** 2) for cx, cy, r in LOBES if abs(x - cx) < r]
    (lx, ly, lr), (rx, ry, rr) = LOBES[0], LOBES[-1]
    bottom = BASE
    if x < lx:
        bottom = ly + math.sqrt(lr * lr - (x - lx) ** 2)
    elif x > rx:
        bottom = ry + math.sqrt(rr * rr - (x - rx) ** 2)
    return min(tops), bottom


def network():
    """Layers of (x, [y...]) that fill the cloud."""
    layers = []
    for x in COLUMNS:
        top, bottom = _extent(x)
        top, bottom = top + PAD, bottom - PAD
        n = max(2, round((bottom - top) / STEP) + 1)
        layers.append((x, [round(top + i * (bottom - top) / (n - 1), 1) for i in range(n)]))
    return layers


def banner(theme: str) -> str:
    c = THEMES[theme]
    layers = network()
    links = [f'    <line x1="{xa}" y1="{y1}" x2="{xb}" y2="{y2}"/>'
             for (xa, ya), (xb, yb) in zip(layers, layers[1:]) for y1 in ya for y2 in yb]
    routes = [[(x, ys[min(len(ys) - 1, round(f * (len(ys) - 1)))]) for x, ys in layers] for f in ROUTES]
    main = routes[0]
    lit = {pt for r in routes for pt in r}
    nodes = "\n".join(f'    <circle cx="{x}" cy="{y}" r="3"/>' for x, ys in layers for y in ys if (x, y) not in lit)
    lit_nodes = "\n".join(f'    <circle cx="{x}" cy="{y}" r="3.6"/>' for x, y in sorted(lit) if (x, y) != main[-1])
    halos = "\n".join(f'    <circle class="tw t{i % 3}" cx="{x}" cy="{y}" r="11"/>' for i, (x, y) in enumerate(main[:-1]))
    paths = "\n".join(
        f'  <path d="M{" L".join(f"{x} {y}" for x, y in r)}" fill="none" stroke="{ACCENT}" stroke-width="1.2" stroke-opacity="0.55" stroke-linejoin="round"/>\n'
        f'  <path class="glide g{i}" d="M{" L".join(f"{x} {y}" for x, y in r)}" pathLength="1000" fill="none" stroke="#F1F6FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        for i, r in enumerate(routes))
    ex, ey = main[-1]
    cloud = cloud_path()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{BW}" height="{BH}" viewBox="0 0 {BW} {BH}" role="img" aria-labelledby="t d">
  <title id="t">Ahmed Hany, cloud security engineer</title>
  <desc id="d">Detection and response engineering on AWS, Azure and Kubernetes. A cloud in fine line art holds a neural network, and light travels slowly through its layers.</desc>
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c["base"][0]}"/>
      <stop offset="0.5" stop-color="{c["base"][1]}"/>
      <stop offset="1" stop-color="{c["base"][2]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="900" cy="190" r="440" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3D6FD6" stop-opacity="{c["glow"]}"/>
      <stop offset="1" stop-color="#3D6FD6" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="skin" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.07"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0.01"/>
    </linearGradient>
    <linearGradient id="contour" x1="620" y1="0" x2="1160" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#8FB4F0"/>
      <stop offset="0.55" stop-color="#E6EEFA"/>
      <stop offset="1" stop-color="#C9D6EC"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{BW}" height="{BH}" rx="14"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .glide {{ stroke-dasharray: 80 920; stroke-dashoffset: 80; animation: glide 8s linear infinite; }}
    .g1 {{ animation-duration: 11s; animation-delay: -4s; }}
    .g2 {{ animation-duration: 13s; animation-delay: -8s; }}
    .tw {{ animation: tw 7s ease-in-out infinite; }}
    .t1 {{ animation-delay: -2.3s; }} .t2 {{ animation-delay: -4.6s; }}
    @keyframes glide {{ to {{ stroke-dashoffset: -920; }} }}
    @keyframes tw {{ 0%, 100% {{ opacity: 0.08; }} 50% {{ opacity: 0.24; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .tw {{ animation: none; }}
      .glide {{ animation: none; opacity: 0; }}
    }}
  </style>

  <g clip-path="url(#frame)">
    <rect width="{BW}" height="{BH}" fill="url(#base)"/>
    <rect width="{BW}" height="{BH}" fill="url(#glow)"/>
  </g>
  <rect x="0.5" y="0.5" width="{BW - 1}" height="{BH - 1}" rx="14" fill="none" stroke="#FFFFFF" stroke-opacity="{c["border"]}"/>

  <!-- the cloud, one thin contour -->
  <path d="{cloud}" fill="url(#skin)" stroke="url(#contour)" stroke-width="1.6" stroke-opacity="0.85" stroke-linejoin="round"/>

  <!-- the network: every layer joined to the next -->
  <g stroke="{LINE}" stroke-opacity="0.20" stroke-width="0.8">
{chr(10).join(links)}
  </g>
{paths}
  <g fill="{ACCENT}" opacity="0.08">
{halos}
  </g>
  <g fill="{NODE}">
{nodes}
  </g>
  <g fill="{ACCENT}">
{lit_nodes}
  </g>
  <circle cx="{ex}" cy="{ey}" r="11" fill="none" stroke="{WARM}" stroke-opacity="0.6" stroke-width="1.2"/>
  <circle cx="{ex}" cy="{ey}" r="4.2" fill="{WARM}"/>

  <!-- identity -->
  <rect x="72" y="111" width="30" height="1.5" fill="{ACCENT}" opacity="0.9"/>
  <text x="116" y="117" class="sans" font-size="13" font-weight="600" letter-spacing="3.4" fill="#9DB6DC">CLOUD SECURITY ENGINEER</text>
  <text x="69" y="198" class="sans" font-size="78" font-weight="600" letter-spacing="-2" fill="#F4F7FB">Ahmed Hany</text>
  <text x="72" y="240" class="sans" font-size="22" fill="#A8B5CB">Detection and response engineering</text>
  <rect x="72" y="266" width="350" height="1" fill="#FFFFFF" opacity="0.14"/>
  <text x="72" y="298" class="sans" font-size="12.5" font-weight="600" letter-spacing="3" fill="#C6D1E3">AWS<tspan dx="16" fill="#5E6E8C">/</tspan><tspan dx="16">AZURE</tspan><tspan dx="16" fill="#5E6E8C">/</tspan><tspan dx="16">KUBERNETES</tspan></text>
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
