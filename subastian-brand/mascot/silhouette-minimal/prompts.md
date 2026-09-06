# Set C — Silhouette Minimal Conductor

Reduced to shape and rim light. This is the set that survives being shrunk:
favicons, social cards, section dividers, the Product Hunt gallery, and any
place where a detailed render would turn to mush.

**Recommended output:** 1200×1200 (1:1). PNG with transparent background —
silhouettes are the set where a baked background hurts most.

---

## C1 — Silhouette Hero

**Output:** `subastian-mascot-C1-silhouette-hero-v01.png`
**Used by:** `product-hunt/gallery/`, social cards, `landing-page/final-cta/`

```
Silhouette of conductor holding glowing magical baton. Strong purple backlight, gold rim outlining figure. Minimalist, elegant, mysterious. Subscription icons faintly glowing behind him in a halo formation.
```

---

## C2 — Silhouette Guardian

**Output:** `subastian-mascot-C2-silhouette-guardian-v01.png`
**Used by:** `ui/purchase-guard/`, `ui/renewal-alerts/`

```
Minimal silhouette conductor blocking a subscription icon with glowing magical baton. Purple backlight, gold rim, magical particle effects. Simple, powerful, premium branding.
```

---

## C3 — Silhouette Stack Formation

**Output:** `subastian-mascot-C3-silhouette-stack-v01.png`
**Used by:** `landing-page/features/`, `appsumo/features/`

```
Silhouette conductor arranging glowing icons into a stack using magical baton. Purple glow, gold rim, minimalist composition, premium SaaS branding.
```

---

## Hand-authored SVG alternative

`variations/*.svg` holds this set built as vector rather than generated raster,
via `build-svg.py`. Three reasons it may be the better format here:

- **The character is identical across all three poses by construction.** The
  consistency problem in `../NAMING.md` is a generative-model problem; these
  share one geometry definition and only vary the arm, prop and staging.
- **No background to bake.** Transparent by nature, so the light/dark question
  does not arise.
- **~6 KB each, and infinitely scalable.** Colors are CSS custom properties at
  the top of each file, so the open gold decision is a one-line change rather
  than a re-render.

Verified legible down to **64px**; below that the legs, tiles and particles
collapse. A true favicon-scale mark (16–32px) needs a further reduction — hat
and baton only — and does not exist yet.

They are a geometric mark, not cinematic art. For Sets A and B, generated
raster is still the right call.

See `../NAMING.md` for the filename spec and character-consistency workflow.
