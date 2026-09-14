# Mascot naming + consistency spec

## Filename convention

```
subastian-mascot-<SET><N>-<slug>-v<NN>.png
```

| Part    | Meaning                          | Values                                    |
|---------|----------------------------------|-------------------------------------------|
| `<SET>` | Prompt set                       | `A` full-body · `B` mid-shot · `C` silhouette |
| `<N>`   | Pose number within the set       | `1`–`3`                                    |
| `<slug>`| Human-readable pose label        | see table below                            |
| `<NN>`  | Variation, zero-padded from `01` | `v01`, `v02`, …                            |

Lowercase throughout, hyphens only, no spaces or underscores — the filename
ends up inside a public CDN URL, so anything needing percent-encoding creates
avoidable breakage.

### The nine slugs

| ID | Slug                   | Full filename (v01)                                  |
|----|------------------------|------------------------------------------------------|
| A1 | `full-body-hero`       | `subastian-mascot-A1-full-body-hero-v01.png`         |
| A2 | `full-body-guardian`   | `subastian-mascot-A2-full-body-guardian-v01.png`     |
| A3 | `full-body-architect`  | `subastian-mascot-A3-full-body-architect-v01.png`    |
| B1 | `midshot-guard`        | `subastian-mascot-B1-midshot-guard-v01.png`          |
| B2 | `midshot-radar`        | `subastian-mascot-B2-midshot-radar-v01.png`          |
| B3 | `midshot-stack`        | `subastian-mascot-B3-midshot-stack-v01.png`          |
| C1 | `silhouette-hero`      | `subastian-mascot-C1-silhouette-hero-v01.png`        |
| C2 | `silhouette-guardian`  | `subastian-mascot-C2-silhouette-guardian-v01.png`    |
| C3 | `silhouette-stack`     | `subastian-mascot-C3-silhouette-stack-v01.png`       |

Variations of the same pose go in the same `variations/` folder and differ only
in the `vNN` suffix. Never renumber a published file — a jsDelivr URL pinned to
a tag is immutable, so a "corrected" `v01` and the original `v01` would be two
different bytes behind one address. Ship `v02` instead.

## Palette

Pulled from the live site's CSS custom properties so the art and the page agree:

| Token           | Light     | Dark      | Use in prompts                    |
|-----------------|-----------|-----------|-------------------------------------|
| `--accent`      | `#6D28D9` | `#B296F5` | the purple glow, backlight, aura  |
| `--accent-strong`| `#54169E`| `#D2C0FA` | deep purple fog, shadow side      |
| `--ink`         | `#15132A` | `#F2EFFA` | the suit black, stage dark        |
| `--bg`          | `#F8F7FC` | `#0B0A14` | what the PNG will sit on          |

**Decided (Sep 2026): gold is in.** The founder's locked reference render for
A1 (see `full-body-cinematic/prompts.md`) uses gold as a real accent — the halo
ring, the baton glow — not just purple. Brand gold is `#D4AF37`, which is also
what the Set C silhouette SVGs already use (`--gold` in each file's internal
`<style>`). That closes the option below in favor of #1: gold is now a real
brand token, so every future prompt and every future export (A, B, and any new
C variations) should render it, not skip it.

Still open: gold isn't yet wired into the site's own CSS custom properties
(`index.html` only has `--accent`/`--accent-strong` purple and `--money`
green) — someone should add a `--gold: #D4AF37` token there so the UI and the
mascot are pulling from the same source, instead of the mascot art being the
only place gold exists.

<details><summary>Original open question (resolved above, kept for history)</summary>

Every prompt asks for gold trim and gold rim light, but the site has no gold
token — its only non-purple accent is `--money: #0E9D6E` (green). Two options
were on the table:

1. **Add gold as a brand token** (suggested `#D4AF37`, which holds up against
   `#6D28D9`). Then the mascot and the UI share a language.
2. **Drop gold from the prompts** and let the purple carry it alone. Cheaper,
   and the page already works without it.

Generating nine images against a gold that never appears in the product is the
outcome to avoid — the mascot would look like it belongs to a different brand
than the site it sits on.

</details>

## Keeping the character consistent

Nine images from nine independent prompts will produce nine different men. The
prompts describe a costume, not a face. Before generating the set:

1. **Generate A1 first and iterate until the character is right.** That single
   image becomes the reference, not a deliverable.
2. **Feed it back as a character reference** for everything else — Midjourney
   `--cref <url>` with `--cw` around 40–70 (lower keeps the face, loosens the
   outfit), or an image-to-image / reference-image slot in whatever generator
   you use.
3. **Keep the seed fixed** across a pose's variations so `v01`/`v02` differ by
   composition, not by identity.
4. **Generate the silhouettes last.** Set C only has to match the *shape* —
   posture, hat, baton angle — so it is far more forgiving, and by then you'll
   know what the silhouette should look like.

## Transparency

The site renders light and dark from the same markup. A PNG with a baked purple
background will band visibly against `--bg` in one theme or the other. Ask for a
transparent background, or plan to cut it — the existing `hero.jpg`,
`vase.jpg` and `orrery.jpg` sidestep this by using rounded containers with
their own shadow, which is the fallback if transparency proves impractical.
