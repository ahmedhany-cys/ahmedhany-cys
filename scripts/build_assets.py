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

THEMES = {
    "dark": dict(
        bg0="#10151D", bg1="#0B0F15", border="#30363D", dot="#222A35",
        name="#F0F6FC", muted="#9198A1", faint="#6E7681",
        accent="#7AA2F7", alert="#FF9E64",
        node="#0D1117", dim_stroke="#3D444D", dim_edge="#2A313C", glow="0.16",
    ),
    "light": dict(
        bg0="#FFFFFF", bg1="#F6F8FA", border="#D1D9E0", dot="#DCE2E9",
        name="#1F2328", muted="#59636E", faint="#818B98",
        accent="#3558D6", alert="#BC4C00",
        node="#FFFFFF", dim_stroke="#C2CAD3", dim_edge="#DCE2E9", glow="0.10",
    ),
}

# graph: who can reach the data? token -> role -> workload -> data
N = {
    "n0": (716, 70), "token": (716, 204), "role": (836, 122), "n3": (836, 270),
    "workload": (956, 204), "n5": (956, 70), "data": (1082, 122), "n7": (1082, 270),
    "n8": (1146, 204),
}
DIM_EDGES = [("n0", "role"), ("n0", "n5"), ("token", "n3"), ("n3", "workload"), ("role", "n5"),
             ("n5", "data"), ("workload", "n7"), ("n3", "n7"), ("data", "n8"), ("n7", "n8")]
PATH = ["token", "role", "workload", "data"]


def banner(theme: str) -> str:
    c = THEMES[theme]
    edges = "\n".join(
        f'    <line x1="{N[a][0]}" y1="{N[a][1]}" x2="{N[b][0]}" y2="{N[b][1]}"/>' for a, b in DIM_EDGES
    )
    dim_nodes = "\n".join(
        f'    <circle cx="{x}" cy="{y}" r="6"/>' for k, (x, y) in N.items() if k not in PATH
    )
    d = "M" + " L".join(f"{N[k][0]} {N[k][1]}" for k in PATH)
    path_nodes = "\n".join(
        f'    <circle cx="{N[k][0]}" cy="{N[k][1]}" r="10" fill="{c["node"]}" stroke="{c["accent"]}" stroke-width="2"/>\n'
        f'    <circle cx="{N[k][0]}" cy="{N[k][1]}" r="3.5" fill="{c["accent"]}"/>'
        for k in PATH[:-1]
    )
    tx, ty = N["data"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340" role="img" aria-labelledby="t d">
  <title id="t">Ahmed Hany, cloud security engineer</title>
  <desc id="d">Detection and response on AWS, Azure and Kubernetes. A graph traces one path from a token through a role and a workload to the data it can reach.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{c["bg0"]}"/>
      <stop offset="1" stop-color="{c["bg1"]}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="1.2" fill="{c["dot"]}"/>
    </pattern>
    <linearGradient id="reveal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0.42" stop-color="#000"/>
      <stop offset="0.78" stop-color="#fff"/>
    </linearGradient>
    <mask id="right"><rect width="1200" height="340" fill="url(#reveal)"/></mask>
    <radialGradient id="glow" cx="{tx}" cy="{ty}" r="300" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{c["accent"]}" stop-opacity="{c["glow"]}"/>
      <stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="frame"><rect x="1" y="1" width="1198" height="338" rx="20"/></clipPath>
  </defs>
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; }}
    @media (prefers-reduced-motion: reduce) {{ .motion {{ display: none; }} }}
  </style>

  <g clip-path="url(#frame)">
    <rect width="1200" height="340" fill="url(#bg)"/>
    <rect width="1200" height="340" fill="url(#dots)" mask="url(#right)"/>
    <rect width="1200" height="340" fill="url(#glow)"/>
  </g>
  <rect x="1" y="1" width="1198" height="338" rx="20" fill="none" stroke="{c["border"]}" stroke-width="2"/>

  <!-- identity -->
  <rect x="64" y="85" width="28" height="2" rx="1" fill="{c["accent"]}"/>
  <text x="106" y="91" class="mono" font-size="14" font-weight="600" letter-spacing="2.6" fill="{c["accent"]}">CLOUD SECURITY ENGINEER</text>
  <text x="61" y="168" class="sans" font-size="70" font-weight="700" letter-spacing="-2.2" fill="{c["name"]}">Ahmed Hany</text>
  <text x="64" y="214" class="sans" font-size="22" fill="{c["muted"]}">Detection and response on AWS, Azure and Kubernetes</text>
  <text x="64" y="272" class="mono" font-size="14" fill="{c["faint"]}">evidence first, never a guess</text>

  <!-- graph: every edge is a permission; one path reaches the data -->
  <g stroke="{c["dim_edge"]}" stroke-width="1.5">
{edges}
  </g>
  <g fill="{c["node"]}" stroke="{c["dim_stroke"]}" stroke-width="1.5">
{dim_nodes}
  </g>
  <path id="route" d="{d}" fill="none" stroke="{c["accent"]}" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.75"/>
  <g>
{path_nodes}
  </g>
  <circle class="motion" cx="{tx}" cy="{ty}" r="12" fill="none" stroke="{c["alert"]}" stroke-width="2" opacity="0">
    <animate attributeName="r" dur="4.2s" repeatCount="indefinite" values="12;12;30" keyTimes="0;0.7;1"/>
    <animate attributeName="opacity" dur="4.2s" repeatCount="indefinite" values="0;0.85;0" keyTimes="0;0.7;1"/>
  </circle>
  <circle cx="{tx}" cy="{ty}" r="11" fill="{c["node"]}" stroke="{c["alert"]}" stroke-width="2"/>
  <circle cx="{tx}" cy="{ty}" r="4" fill="{c["alert"]}"/>
  <circle class="motion" r="5" fill="{c["accent"]}" opacity="0">
    <animateMotion dur="4.2s" repeatCount="indefinite" calcMode="linear" keyPoints="0;1;1" keyTimes="0;0.7;1">
      <mpath href="#route"/>
    </animateMotion>
    <animate attributeName="opacity" dur="4.2s" repeatCount="indefinite" values="0;1;1;0;0" keyTimes="0;0.06;0.66;0.7;1"/>
  </circle>

  <g class="mono" font-size="13" text-anchor="middle" fill="{c["muted"]}">
    <text x="{N["token"][0]}" y="{N["token"][1] + 32}">token</text>
    <text x="{N["role"][0]}" y="{N["role"][1] - 22}">role</text>
    <text x="{N["workload"][0]}" y="{N["workload"][1] + 32}">workload</text>
    <text x="{tx}" y="{ty - 24}" fill="{c["alert"]}" font-weight="600">data</text>
  </g>
</svg>
'''


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
