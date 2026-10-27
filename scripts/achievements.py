"""Render the GitHub achievements a user has actually earned into assets/achievements.svg.

Reads the public achievements tab (https://github.com/<user>?tab=achievements), so only
earned, publicly shown achievements appear. Badge artwork is GitHub's own, embedded as
data URIs because images referenced from an SVG do not load when it is shown via <img>.
Achievements not yet earned are drawn as clearly labelled "locked" outlines with no
official artwork. Standard library only.

Usage: python scripts/achievements.py <github-user> [output.svg]
"""

import base64
import html
import re
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (profile-achievements-renderer)"}

# The ones anyone can earn through normal activity; shown locked until earned.
EARNABLE = ["Pull Shark", "Quickdraw", "YOLO", "Pair Extraordinaire", "Galaxy Brain", "Starstruck"]

TIER = {  # pill fill, pill text
    "gold": ("#F3E58C", "#3A3000"),
    "silver": ("#DCE3EA", "#2A323B"),
    "bronze": ("#F0C4AE", "#4A2412"),
}

CARD = re.compile(r'<img src="([^"]+)"[^>]*alt="Achievement: ([^"]+)"[^>]*class="achievement-badge-card"')
TIER_LABEL = re.compile(r'achievement-tier-label--(\w+)[^>]*>(x\d+)<')


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read()


def earned(user):
    try:
        page = fetch(f"https://github.com/{user}?tab=achievements").decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:  # GitHub answers 404 when nothing is earned or shown
            return []
        raise
    found = []
    matches = list(CARD.finditer(page))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(page)
        tier = TIER_LABEL.search(page, m.end(), end)
        img = base64.b64encode(fetch(m.group(1))).decode()
        found.append({
            "name": html.unescape(m.group(2)),
            "img": f"data:image/png;base64,{img}",
            "tier": tier.group(1) if tier else None,
            "count": tier.group(2) if tier else None,
        })
    return found


def label(name, x, y, fill):
    """Badge name under a tile, split over two lines when it would collide with a neighbour."""
    words, lines = name.split(), [name]
    if len(name) > 15 and len(words) > 1:
        mid = max(range(1, len(words)), key=lambda k: -abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
        lines = [" ".join(words[:mid]), " ".join(words[mid:])]
    spans = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else 16}">{html.escape(t)}</tspan>' for i, t in enumerate(lines))
    return f'<text x="{x}" y="{y}" text-anchor="middle" class="t" font-size="13" fill="{fill}">{spans}</text>', len(lines)


def render(user, items):
    size, gap, per_row = 104, 36, 6
    locked = [n for n in EARNABLE if n not in {i["name"] for i in items}]
    tiles = [("earned", i) for i in items] + [("locked", {"name": n}) for n in locked]
    rows = max(1, -(-len(tiles) // per_row))
    width = per_row * size + (per_row - 1) * gap + 64
    height = 64 + rows * (size + 72) + 8
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="GitHub achievements earned by {user}: '
        f'{", ".join(i["name"] + (" " + i["count"] if i["count"] else "") for i in items) or "none yet"}">',
        "<style>.t{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}"
        ".m{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}</style>",
        f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="#0B0F15" stroke="#21262D" stroke-width="2"/>',
        f'<text x="32" y="40" class="m" font-size="13" fill="#7AA2F7">{len(items)} earned'
        f'<tspan fill="#6E7681"> · {len(locked)} locked</tspan></text>',
    ]
    for n, (state, it) in enumerate(tiles):
        col, row = n % per_row, n // per_row
        x, y = 32 + col * (size + gap), 60 + row * (size + 72)
        cx, cy, r = x + size / 2, y + size / 2, size / 2
        if state == "earned":
            out.append(f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="{it["img"]}" xlink:href="{it["img"]}"/>')
            if it["count"]:
                fill, ink = TIER.get(it["tier"], TIER["bronze"])
                out.append(f'<rect x="{x + size - 46}" y="{y + size - 30}" width="50" height="28" rx="14" fill="{fill}"/>'
                           f'<text x="{x + size - 21}" y="{y + size - 10}" text-anchor="middle" class="t" font-size="16" '
                           f'font-weight="700" fill="{ink}">{it["count"]}</text>')
            out.append(label(it["name"], cx, y + size + 26, "#C9D1D9")[0])
        else:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 2}" fill="#0D1117" stroke="#30363D" stroke-width="2" stroke-dasharray="6 6"/>'
                       f'<rect x="{cx - 11}" y="{cy - 2}" width="22" height="17" rx="3" fill="none" stroke="#484F58" stroke-width="2"/>'
                       f'<path d="M{cx - 6} {cy - 2}v-5a6 6 0 0 1 12 0v5" fill="none" stroke="#484F58" stroke-width="2"/>'
                       f'<text x="{cx}" y="{cy + 32}" text-anchor="middle" class="m" font-size="10" fill="#484F58">LOCKED</text>')
            out.append(label(it["name"], cx, y + size + 26, "#6E7681")[0])
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    user = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "assets/achievements.svg"
    items = earned(user)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(user, items))
    print(f"{len(items)} earned:", ", ".join(f'{i["name"]} {i["count"] or ""}'.strip() for i in items) or "none")
