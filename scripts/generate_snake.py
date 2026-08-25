#!/usr/bin/env python3
"""Generate an animated contribution-snake SVG from a GitHub contribution calendar JSON.

No GitHub Actions required - run locally:
    gh api graphql --input gql.json > contrib.json
    python scripts/generate_snake.py contrib.json assets/

Where gql.json contains:
    {"query": "query { user(login: \"LOGIN\") { contributionsCollection {
       contributionCalendar { totalContributions weeks { contributionDays {
       date contributionCount color } } } } } }"}
"""

import json
import math
import sys
from pathlib import Path

CELL = 11          # cell size in px
GAP = 3            # gap between cells
PITCH = CELL + GAP
MARGIN = 10        # outer margin

# Purple-themed contribution ramps (index 0 = empty)
DARK_RAMP = ["#21262d", "#3b2d63", "#5b3aa8", "#8250df", "#a855f7", "#c084fc"]
LIGHT_RAMP = ["#ebedf0", "#e2d6fb", "#c9aef7", "#a97ff0", "#8b5cf6", "#6d28d9"]


def level_for(count: int) -> int:
    """Map a contribution count to a palette level 0-5."""
    if count <= 0:
        return 0
    if count <= 2:
        return 1
    if count <= 4:
        return 2
    if count <= 6:
        return 3
    if count <= 9:
        return 4
    return 5


def load_grid(path: Path) -> list[list[int | None]]:
    """Return a matrix [col][row] of contribution counts (None = no day)."""
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    grid: list[list[int | None]] = []
    for week in weeks:
        col = [None] * 7
        for day in week["contributionDays"]:
            weekday = day["date"][0:10]
            import datetime
            row = datetime.date.fromisoformat(weekday).weekday()  # Mon=0..Sun=6
            col[(row + 1) % 7] = day["contributionCount"]  # GitHub rows start Sunday
        grid.append(col)
    return grid


def svg(grid: list[list[int | None]], ramp: list[str], dark: bool) -> str:
    cols = len(grid)
    width = MARGIN * 2 + cols * PITCH - GAP
    height = MARGIN * 2 + 7 * PITCH - GAP

    # --- cells ---
    cells = []
    centers: list[tuple[float, float]] = []
    for ci, col in enumerate(grid):
        for ri, count in enumerate(col):
            x = MARGIN + ci * PITCH
            y = MARGIN + ri * PITCH
            level = level_for(count) if count is not None else 0
            opacity = "0.15" if count is None else "1"
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
                f'fill="{ramp[level]}" opacity="{opacity}"/>'
            )
            centers.append((x + CELL / 2, y + CELL / 2))

    # --- boustrophedon snake path through every cell ---
    pts: list[tuple[float, float]] = []
    for ci in range(cols):
        col_centers = centers[ci * 7:(ci + 1) * 7]
        pts.extend(col_centers if ci % 2 == 0 else list(reversed(col_centers)))

    d_parts = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    total_len = 0.0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        total_len += seg
        d_parts.append(f"L {x1:.1f} {y1:.1f}")
    d = " ".join(d_parts)

    dur = "16s"
    glow_id = "glowDark" if dark else "glowLight"
    glow_color = "#c084fc" if dark else "#7c3aed"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="snakeGrad{'Dark' if dark else 'Light'}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ramp[2]}"/>
      <stop offset="100%" stop-color="{ramp[5]}"/>
    </linearGradient>
    <filter id="{glow_id}" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3.2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- contribution grid -->
  {chr(10).join(['  ' + c for c in cells])}

  <!-- snake body: draws itself through the year, loops forever -->
  <path d="{d}" fill="none" stroke="url(#snakeGrad{'Dark' if dark else 'Light'})"
        stroke-width="7" stroke-linecap="round" stroke-linejoin="round"
        stroke-dasharray="{total_len:.0f} {total_len:.0f}">
    <animate attributeName="stroke-dashoffset"
             values="{total_len:.0f};0;0" keyTimes="0;0.82;1"
             dur="{dur}" repeatCount="indefinite"/>
  </path>

  <!-- snake head -->
  <circle r="5.5" fill="{glow_color}" filter="url(#{glow_id})">
    <animateMotion dur="{dur}" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;0.82;1" calcMode="linear">
      <mpath href="#snakePath{'Dark' if dark else 'Light'}"/>
    </animateMotion>
  </circle>

  <!-- invisible path referenced by the head -->
  <path id="snakePath{'Dark' if dark else 'Light'}" d="{d}" fill="none" stroke="none"/>
</svg>
'''


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: generate_snake.py <contrib.json> <output_dir>")
        sys.exit(1)
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    grid = load_grid(src)
    (out_dir / "snake-dark.svg").write_text(svg(grid, DARK_RAMP, dark=True), encoding="utf-8")
    (out_dir / "snake-light.svg").write_text(svg(grid, LIGHT_RAMP, dark=False), encoding="utf-8")
    filled = sum(1 for col in grid for c in col if c)
    total = sum(c for col in grid for c in col if c)
    print(f"wrote {out_dir}/snake-dark.svg and snake-light.svg")
    print(f"grid: {len(grid)} weeks, {filled} active days, {total} contributions")


if __name__ == "__main__":
    main()
