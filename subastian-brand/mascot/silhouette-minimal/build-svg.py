#!/usr/bin/env python3
"""
Generate the Set C silhouette mascots as standalone SVG.

One shared outline drives all three poses. That is the point: the character
consistency problem described in ../NAMING.md is a generative-model problem —
nine prompts produce nine different men. Here the conductor is the same
geometry every time; only the arm, the prop and the staging change.

The figure is a SINGLE closed path on purpose. A silhouette has one outer
contour, so the gold rim light lands only on the outside edge; building it
from stacked parts puts a rim on every interior seam.

    python3 build-svg.py        # writes variations/*.svg
"""
import math, pathlib

OUT = pathlib.Path(__file__).parent / "variations"

# ------------------------------------------------------------------ palette
INK       = "#0A0814"   # figure — darker than both site backgrounds
PURPLE    = "#6D28D9"   # --accent
PURPLE_HI = "#B296F5"
GOLD      = "#D4AF37"   # proposed, not yet a site token — see ../NAMING.md

# ------------------------------------------------------------- the outline
# Clockwise from the top of the hat: crown, brim, head, jaw, neck, right
# shoulder, [posed arm], coat side, tail, legs, and back up the left side.
PARTS = """
    <path d="M 556 216 L 644 216 L 652 296 L 548 296 Z"/>
    <ellipse cx="600" cy="304" rx="74" ry="13"/>
    <path d="M 566 300 L 634 300 L 636 356
             C 634 392 622 408 600 410 C 578 408 566 392 564 356 Z"/>
    <path d="M 584 400 L 616 400 L 618 440 L 582 440 Z"/>
    <path d="M 590 428 C 552 434 528 450 514 476 L 498 566 L 486 704
             L 472 874 L 494 898 L 556 764 L 552 704 L 648 704 L 644 764
             L 706 898 L 728 874 L 714 704 L 702 566 L 686 476
             C 672 450 648 434 610 428 Z"/>
    <path d="M 552 690 L 596 690 L 592 1030 L 600 1052 L 538 1052 L 550 1030 Z"/>
    <path d="M 604 690 L 648 690 L 650 1030 L 662 1052 L 600 1052 L 608 1030 Z"/>
"""

# The arm is spliced into the contour between shoulder and coat, so it reads
# as part of the body rather than a shape laid on top of it.
ARM_REST = '<path d="M 556 446 L 528 458 L 504 560 L 496 660 L 520 664 L 532 570 L 554 478 Z"/>'

ARMS = {
    "hero":     '<path d="M 640 446 L 674 440 L 762 380 L 814 326 L 794 304 L 740 360 L 656 412 Z"/>',
    "guardian": '<path d="M 642 452 L 672 462 L 754 512 L 810 550 L 796 572 L 736 536 L 654 498 Z"/>',
    "stack":    '<path d="M 644 458 L 672 470 L 734 556 L 772 634 L 748 648 L 708 574 L 652 502 Z"/>',
}

# Baton: (x1,y1) at the hand, (x2,y2) at the tip.
BATON = {
    "hero":     (816, 312, 986, 190),
    "guardian": (810, 570, 968, 656),
    "stack":    (768, 652, 880, 818),
}

NL_JOIN = chr(10).join

def figure(pose):
    return NL_JOIN([PARTS.rstrip(), "    " + ARM_REST, "    " + ARMS[pose]])

def icon(x, y, s, op, rot=0):
    """A subscription tile — rounded square with a slot, app-icon shaped."""
    return (f'<g transform="translate({x:.0f},{y:.0f}) rotate({rot:.0f}) '
            f'translate({-s/2:.0f},{-s/2:.0f})" opacity="{op:.2f}">'
            f'<rect width="{s:.0f}" height="{s:.0f}" rx="{s*0.26:.1f}" fill="none" '
            f'stroke="url(#icon-edge)" stroke-width="{max(1.8, s*0.055):.1f}"/>'
            f'<rect x="{s*0.26:.1f}" y="{s*0.42:.1f}" width="{s*0.48:.1f}" '
            f'height="{s*0.15:.1f}" rx="{s*0.07:.1f}" fill="url(#icon-edge)" '
            f'opacity="0.7"/></g>')

def icons_for(pose):
    out = []
    if pose == "hero":
        for i, ang in enumerate(range(-168, -6, 20)):     # halo arc, clears the body
            a = math.radians(ang)
            out.append(icon(600 + 372 * math.cos(a), 470 + 372 * math.sin(a) * 0.94,
                            50, 0.26 + 0.10 * (i % 4), rot=ang / 9))
    elif pose == "guardian":
        out.append(icon(1024, 686, 76, 0.85, rot=-16))    # the one being deflected
        out.append(icon(1092, 578, 52, 0.30, rot=10))
        out.append(icon(1078, 800, 46, 0.24, rot=-6))
    else:
        for i in range(4):                                 # the ordered stack
            out.append(icon(962, 936 - i * 74, 76 - i * 4, 0.28 + i * 0.17))
    return "\n    ".join(out)

def sparks(pose):
    pts = {
        "hero":     [(950,232,5),(906,282,3.4),(1010,164,3),(870,200,2.6),(982,292,2.4),
                     (842,336,3),(922,154,2.2),(1038,240,2.8)],
        "guardian": [(884,600,4.8),(926,572,3.2),(948,632,2.8),(858,640,2.4),(908,664,2.2),
                     (972,552,2.6),(834,608,2.0)],
        "stack":    [(838,760,4.6),(874,716,3.2),(892,792,2.8),(814,818,2.4),(860,846,2.6),
                     (908,740,2.2)],
    }[pose]
    return "\n    ".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#spark)" opacity="{0.85-i*0.07:.2f}"/>'
        for i, (x, y, r) in enumerate(pts))

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200"
     width="1200" height="1200" role="img" aria-labelledby="t d">
  <title id="t">{title}</title>
  <desc id="d">{desc}</desc>
  <style>
    /* Retune the brand here; nothing else needs to change.
       If gold leaves the brand, set --gold to the same value as --purple-hi. */
    svg {{ --ink: {ink}; --purple: {purple}; --purple-hi: {purple_hi}; --gold: {gold}; }}
  </style>
  <defs>
    <radialGradient id="backlight" cx="50%" cy="42%" r="52%">
      <stop offset="0%"   stop-color="var(--purple)" stop-opacity="0.92"/>
      <stop offset="45%"  stop-color="var(--purple)" stop-opacity="0.34"/>
      <stop offset="100%" stop-color="var(--purple)" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="icon-edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="var(--purple-hi)"/>
      <stop offset="100%" stop-color="var(--gold)"/>
    </linearGradient>
    <linearGradient id="baton" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="var(--gold)" stop-opacity="0.35"/>
      <stop offset="55%"  stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="var(--purple-hi)"/>
    </linearGradient>
    <radialGradient id="spark">
      <stop offset="0%"   stop-color="#FFFFFF"/>
      <stop offset="60%"  stop-color="var(--gold)"/>
      <stop offset="100%" stop-color="var(--gold)" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft"  x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="16"/></filter>
    <!-- Directional rim: offset the union alpha, keep only what falls outside
         the original. Applied to the group, so interior seams never show. -->
    <filter id="rim-gold" x="-25%" y="-25%" width="150%" height="150%">
      <feOffset in="SourceAlpha" dx="9" dy="-8" result="o"/>
      <feFlood flood-color="{gold}" result="c"/>
      <feComposite in="c" in2="o" operator="in" result="r"/>
      <feComposite in="r" in2="SourceAlpha" operator="out"/>
    </filter>
    <filter id="rim-cool" x="-25%" y="-25%" width="150%" height="150%">
      <feOffset in="SourceAlpha" dx="-7" dy="6" result="o"/>
      <feFlood flood-color="{purple_hi}" result="c"/>
      <feComposite in="c" in2="o" operator="in" result="r"/>
      <feComposite in="r" in2="SourceAlpha" operator="out"/>
    </filter>
    <filter id="tight" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="6"/></filter>
    <g id="conductor">
{figure}
    </g>
  </defs>

  <!-- backlight: this is what separates the figure from a dark page -->
  <ellipse cx="600" cy="500" rx="430" ry="470" fill="url(#backlight)"/>

  <!-- subscription tiles -->
  <g>
    {icons}
  </g>

  <!-- rim light: the same contour, offset, so gold shows only on the lit edge -->
  <use href="#conductor" filter="url(#rim-cool)" opacity="0.5"/>
  <use href="#conductor" filter="url(#rim-gold)"/>
  <use href="#conductor" fill="var(--ink)"/>

  <!-- baton -->
  <g stroke-linecap="round">
    <line x1="{bx1}" y1="{by1}" x2="{bx2}" y2="{by2}"
          stroke="var(--purple-hi)" stroke-width="22" opacity="0.55" filter="url(#soft)"/>
    <line x1="{bx1}" y1="{by1}" x2="{bx2}" y2="{by2}"
          stroke="url(#baton)" stroke-width="9" filter="url(#tight)"/>
    <line x1="{bx1}" y1="{by1}" x2="{bx2}" y2="{by2}"
          stroke="url(#baton)" stroke-width="4.5"/>
    <circle cx="{bx2}" cy="{by2}" r="13" fill="#FFFFFF" opacity="0.9" filter="url(#tight)"/>
    <circle cx="{bx2}" cy="{by2}" r="4.5" fill="#FFFFFF"/>
  </g>

  <!-- particles -->
  <g>
    {sparks}
  </g>
</svg>
"""

POSES = {
    "C1-silhouette-hero": dict(
        arm="hero",
        title="Subastian conductor silhouette, hero pose",
        desc="Silhouette of a conductor in a top hat and tailcoat raising a glowing "
             "baton, backlit in purple with a gold rim light, subscription tiles "
             "arced behind him in a halo."),
    "C2-silhouette-guardian": dict(
        arm="guardian",
        title="Subastian conductor silhouette, guardian pose",
        desc="Silhouette of a conductor extending a glowing baton to deflect a "
             "duplicate subscription tile, backlit in purple with a gold rim light."),
    "C3-silhouette-stack": dict(
        arm="stack",
        title="Subastian conductor silhouette, stack formation",
        desc="Silhouette of a conductor directing a glowing baton downward, "
             "arranging subscription tiles into an ordered stack, backlit in "
             "purple with a gold rim light."),
}

OUT.mkdir(parents=True, exist_ok=True)
for slug, cfg in POSES.items():
    pose = cfg["arm"]
    x1, y1, x2, y2 = BATON[pose]
    svg = TEMPLATE.format(
        title=cfg["title"], desc=cfg["desc"],
        ink=INK, purple=PURPLE, purple_hi=PURPLE_HI, gold=GOLD,
        figure=figure(pose), icons=icons_for(pose), sparks=sparks(pose),
        bx1=x1, by1=y1, bx2=x2, by2=y2)
    p = OUT / f"subastian-mascot-{slug}-v01.svg"
    p.write_text(svg)
    print(f"  {p.name}  {len(svg):,} bytes")
