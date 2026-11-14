#!/usr/bin/env python3
"""Builds the profile README visuals: a light/dark banner and window-framed project covers.

Usage: python scripts/build_assets.py

Screenshot covers read their JPEG from assets/src/ and embed it, so each cover is a single
self-contained SVG. Terminal covers are drawn from the text in this file. No dependencies.
"""
import base64
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
WORK = ASSETS / "work"
WORK.mkdir(parents=True, exist_ok=True)

SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'

# --------------------------------------------------------------------------- banner
# One composition, two colourings. Both are dark heroes with white type so the banner reads as a
# hero on either GitHub theme: ink with blue glow for dark mode, royal blue for light mode.
# The path runs cold to hot: blue where access starts, orange where it reaches the data.

BW, BH = 1200, 380

THEMES = {
    "dark": dict(
        base=("#070B16", "#0A1330", "#0A0E1C"), glow_a=("#2F6BFF", "0.42"), glow_b=("#FF7A2F", "0.34"),
        glow_c=("#1FB6FF", "0.16"), grid="0.05", ink="#0A1022", edge="0.24", dim="0.60",
        label="#AAB6D3", sub="#C3CEE6", pill_fill="0.06", pill_stroke="0.20",
    ),
    "light": dict(
        base=("#0B1D55", "#1741B0", "#0D2470"), glow_a=("#6CB0FF", "0.50"), glow_b=("#FF8A3D", "0.42"),
        glow_c=("#7FD4FF", "0.22"), grid="0.07", ink="#0E2466", edge="0.32", dim="0.70",
        label="#C9D8FF", sub="#DCE6FF", pill_fill="0.10", pill_stroke="0.30",
    ),
}

# highlighted path: who can reach the data?
ROUTE = [("token", 668, 252, "#4DA3FF", "below"), ("role", 790, 152, "#63A2FB", "above"),
         ("workload", 900, 238, "#8FA6F2", "below"), ("secret", 1004, 130, "#FFB37A", "above"),
         ("data", 1110, 206, "#FF8A3D", "above")]
DIM = {"a": (640, 112), "b": (722, 60), "c": (852, 62), "d": (760, 322), "e": (882, 332), "f": (992, 302),
       "g": (1092, 320), "h": (1152, 112), "i": (1062, 56), "j": (1168, 284), "k": (950, 34)}
RP = {name: (x, y) for name, x, y, _, _ in ROUTE}
EDGES = [("a", "role"), ("b", "role"), ("b", "c"), ("c", "role"), ("c", "secret"), ("c", "k"), ("k", "i"),
         ("token", "a"), ("token", "d"), ("d", "e"), ("d", "workload"), ("e", "workload"), ("e", "f"),
         ("f", "workload"), ("f", "g"), ("f", "data"), ("g", "data"), ("g", "j"), ("data", "j"),
         ("data", "h"), ("h", "i"), ("i", "secret")]


def banner(theme: str) -> str:
    c = THEMES[theme]
    pt = {**DIM, **RP}
    edges = "\n".join(f'    <line x1="{pt[a][0]}" y1="{pt[a][1]}" x2="{pt[b][0]}" y2="{pt[b][1]}"/>' for a, b in EDGES)
    dim_nodes = "\n".join(f'    <circle class="tw" cx="{x}" cy="{y}" r="4.5"/>' for x, y in DIM.values())
    d = "M" + " L".join(f"{x} {y}" for _, x, y, _, _ in ROUTE)
    nodes, labels = [], []
    for name, x, y, col, side in ROUTE[:-1]:
        nodes.append(f'    <circle cx="{x}" cy="{y}" r="22" fill="{col}" opacity="0.16"/>\n'
                     f'    <circle cx="{x}" cy="{y}" r="12" fill="{c["ink"]}" stroke="{col}" stroke-width="2.5"/>\n'
                     f'    <circle cx="{x}" cy="{y}" r="4.5" fill="{col}"/>')
    for name, x, y, col, side in ROUTE:
        ly = y + 38 if side == "below" else y - 28
        if name == "data":
            labels.append(f'    <text x="{x}" y="{ly - 6}" fill="#FFB37A" font-weight="700" font-size="15">{name}</text>')
        else:
            labels.append(f'    <text x="{x}" y="{ly}">{name}</text>')
    tx, ty = RP["data"]
    x0, x1 = ROUTE[0][1], ROUTE[-1][1]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{BW}" height="{BH}" viewBox="0 0 {BW} {BH}" role="img" aria-labelledby="t d">
  <title id="t">Ahmed Hany, cloud security engineer</title>
  <desc id="d">Detection and response engineering on AWS, Azure and Kubernetes. A network graph lights up one path, from a token through a role, a workload and a secret to the data it can reach.</desc>
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c["base"][0]}"/>
      <stop offset="0.55" stop-color="{c["base"][1]}"/>
      <stop offset="1" stop-color="{c["base"][2]}"/>
    </linearGradient>
    <radialGradient id="ga" cx="860" cy="170" r="470" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c["glow_a"][0]}" stop-opacity="{c["glow_a"][1]}"/>
      <stop offset="1" stop-color="{c["glow_a"][0]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gb" cx="{tx}" cy="{ty}" r="230" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c["glow_b"][0]}" stop-opacity="{c["glow_b"][1]}"/>
      <stop offset="1" stop-color="{c["glow_b"][0]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gc" cx="90" cy="400" r="330" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c["glow_c"][0]}" stop-opacity="{c["glow_c"][1]}"/>
      <stop offset="1" stop-color="{c["glow_c"][0]}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="{c["grid"]}" stroke-width="1"/>
    </pattern>
    <linearGradient id="reveal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0.30" stop-color="#000"/>
      <stop offset="0.72" stop-color="#fff"/>
    </linearGradient>
    <mask id="right"><rect width="{BW}" height="{BH}" fill="url(#reveal)"/></mask>
    <linearGradient id="heat" x1="{x0}" y1="0" x2="{x1}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#4DA3FF"/>
      <stop offset="0.55" stop-color="#8FA6F2"/>
      <stop offset="0.8" stop-color="#FFB37A"/>
      <stop offset="1" stop-color="#FF8A3D"/>
    </linearGradient>
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#4DA3FF" stop-opacity="0.9"/>
      <stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.14"/>
      <stop offset="1" stop-color="#FF8A3D" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0.35" stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#C4D8FF"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-60%" width="140%" height="220%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
    <clipPath id="frame"><rect x="1" y="1" width="{BW - 2}" height="{BH - 2}" rx="24"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; }}
    .flow {{ stroke-dasharray: 2 30; animation: flow 1.5s linear infinite; }}
    .tw {{ animation: tw 5s ease-in-out infinite; }}
    .tw:nth-child(3n) {{ animation-delay: -1.6s; }}
    .tw:nth-child(3n+1) {{ animation-delay: -3.3s; }}
    .live {{ animation: live 2.4s ease-in-out infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -32; }} }}
    @keyframes tw {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    @keyframes live {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .flow, .tw, .live {{ animation: none; }}
      .motion {{ display: none; }}
    }}
  </style>

  <g clip-path="url(#frame)">
    <rect width="{BW}" height="{BH}" fill="url(#base)"/>
    <rect width="{BW}" height="{BH}" fill="url(#grid)" mask="url(#right)"/>
    <rect width="{BW}" height="{BH}" fill="url(#ga)"/>
    <rect width="{BW}" height="{BH}" fill="url(#gc)"/>
    <rect width="{BW}" height="{BH}" fill="url(#gb)"/>
  </g>
  <rect x="1" y="1" width="{BW - 2}" height="{BH - 2}" rx="24" fill="none" stroke="url(#rim)" stroke-width="2"/>

  <!-- graph: every edge is a permission -->
  <g stroke="#B8C7E6" stroke-opacity="{c["edge"]}" stroke-width="1.2">
{edges}
  </g>
  <g fill="{c["ink"]}" stroke="#B8C7E6" stroke-opacity="{c["dim"]}" stroke-width="1.4">
{dim_nodes}
  </g>

  <!-- the one path that reaches the data, cold to hot -->
  <path d="{d}" fill="none" stroke="url(#heat)" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" opacity="0.75" filter="url(#soft)"/>
  <path id="route" d="{d}" fill="none" stroke="url(#heat)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path class="flow" d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity="0.95" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <g>
{chr(10).join(nodes)}
  </g>

  <!-- target -->
  <circle cx="{tx}" cy="{ty}" r="36" fill="#FF8A3D" opacity="0.20"/>
  <circle class="motion" cx="{tx}" cy="{ty}" r="14" fill="none" stroke="#FF8A3D" stroke-width="2" opacity="0">
    <animate attributeName="r" dur="2.6s" repeatCount="indefinite" values="14;46"/>
    <animate attributeName="opacity" dur="2.6s" repeatCount="indefinite" values="0.9;0"/>
  </circle>
  <circle class="motion" cx="{tx}" cy="{ty}" r="14" fill="none" stroke="#FFB37A" stroke-width="2" opacity="0">
    <animate attributeName="r" dur="2.6s" begin="1.3s" repeatCount="indefinite" values="14;46"/>
    <animate attributeName="opacity" dur="2.6s" begin="1.3s" repeatCount="indefinite" values="0.9;0"/>
  </circle>
  <circle cx="{tx}" cy="{ty}" r="15" fill="{c["ink"]}" stroke="#FF8A3D" stroke-width="3"/>
  <circle cx="{tx}" cy="{ty}" r="6" fill="#FF8A3D"/>

  <!-- comet -->
  <g class="motion" opacity="0">
    <circle r="11" fill="#FFFFFF" opacity="0.25"/>
    <circle r="5.5" fill="#FFFFFF"/>
    <animateMotion dur="3.6s" repeatCount="indefinite" calcMode="linear" keyPoints="0;1;1" keyTimes="0;0.8;1">
      <mpath href="#route"/>
    </animateMotion>
    <animate attributeName="opacity" dur="3.6s" repeatCount="indefinite" values="0;1;1;0;0" keyTimes="0;0.05;0.74;0.8;1"/>
  </g>

  <g class="mono" font-size="13.5" text-anchor="middle" fill="{c["label"]}">
{chr(10).join(labels)}
  </g>

  <!-- identity -->
  <rect x="64" y="56" width="288" height="34" rx="17" fill="#FFFFFF" fill-opacity="{c["pill_fill"]}" stroke="#FFFFFF" stroke-opacity="{c["pill_stroke"]}"/>
  <circle class="live" cx="84" cy="73" r="4.5" fill="#4ADE80"/>
  <text x="100" y="78" class="mono" font-size="13" font-weight="600" letter-spacing="2.2" fill="#DCE6FF">CLOUD SECURITY ENGINEER</text>

  <text x="60" y="182" class="sans" font-size="88" font-weight="800" letter-spacing="-3" fill="url(#name)">Ahmed Hany</text>
  <text x="64" y="228" class="sans" font-size="25" fill="{c["sub"]}">Detection and response engineering</text>

  <g class="sans" font-size="16" font-weight="600" fill="#FFFFFF" text-anchor="middle">
    <rect x="64" y="252" width="74" height="36" rx="18" fill="#FFFFFF" fill-opacity="{c["pill_fill"]}" stroke="#FFFFFF" stroke-opacity="{c["pill_stroke"]}"/>
    <text x="101" y="276">AWS</text>
    <rect x="148" y="252" width="86" height="36" rx="18" fill="#FFFFFF" fill-opacity="{c["pill_fill"]}" stroke="#FFFFFF" stroke-opacity="{c["pill_stroke"]}"/>
    <text x="191" y="276">Azure</text>
    <rect x="244" y="252" width="132" height="36" rx="18" fill="#FFFFFF" fill-opacity="{c["pill_fill"]}" stroke="#FFFFFF" stroke-opacity="{c["pill_stroke"]}"/>
    <text x="310" y="276">Kubernetes</text>
  </g>

  <text x="64" y="334" class="mono" font-size="14.5" fill="{c["label"]}"><tspan fill="#FFB37A">//</tspan> evidence first, never a guess</text>
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
