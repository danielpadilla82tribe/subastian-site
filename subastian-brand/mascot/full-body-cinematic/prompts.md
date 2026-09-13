# Set A — Full-Body Cinematic Conductor

Tall, dramatic, stage-lit. This is the hero-slot mascot: the one that carries
the top of the landing page and the AppSumo hero. Portrait framing.

**Recommended output:** 1200×1600 (3:4). Export PNG with transparent background
where possible — the site's hero sits on `--bg` (`#F8F7FC` light / `#0B0A14`
dark), so a baked-in background will band against one of the two themes.

---

## Reference locked (v01, Sep 2026)

The founder generated a render matching the brief below and it's the one to
match going forward — every pose in this set, and any regeneration of an
existing one, should be produced as a character-reference / image-to-image
pass off this description (or the actual reference file, once it's added to
`variations/`) rather than from the bare prompt alone. See "Keeping the
character consistent" in `../NAMING.md` for the workflow this locks in.

Observed description of the locked reference (use this verbatim as the base
prompt, and prefer feeding the actual reference image back into the generator
as a character/style reference over retyping this from memory):

```
A conductor seen from behind at a slight three-quarter angle, dark wavy hair,
wearing a black tuxedo tailcoat with white cuffs and cufflinks. One arm raised
with an open hand, the other extended holding a thin glowing white baton. He
stands before a circular halo of glowing purple outlined app icons arranged in
an arc around him (a play button, a musical note, a cloud, two package/cube
icons, a letter "N"). Background is deep black with a soft purple radial glow
behind him and faint purple energy wisps/light trails. A thin gold ring/arc
traces part of the halo. Cinematic, moody lighting, high detail, portrait
orientation.
```

This also settles the open gold question in `../NAMING.md`: the reference
render uses gold as a real accent (the halo ring, the baton glow), not just
purple — see the updated palette note there.

---

## A1 — Hero Pose

**Output:** `subastian-mascot-A1-full-body-hero-v01.png`
**Used by:** `landing-page/hero/`, `appsumo/hero/`
**Status:** reference established (above) — pending the actual PNG being added to `variations/`

```
Full-body cinematic conductor standing on a dark stage. Black suit with gold trim. Purple top hat optional. Holding a glowing magical baton emitting purple and gold particles. Subscription icons swirl around him like a symphony. Dramatic purple backlight, gold rim light, high contrast, premium SaaS aesthetic, floating sparks, orchestral energy.
```

---

## A2 — Guardian Pose

**Output:** `subastian-mascot-A2-full-body-guardian-v01.png`
**Used by:** `ui/purchase-guard/`, `landing-page/features/`
**Status:** not yet generated — generate from the A1 reference (character-reference / image-to-image), not from this prompt alone.

```
Full-body conductor in heroic stance. Magical baton held like a sword, glowing purple aura. A duplicate subscription icon is blocked by a golden energy shield. Purple fog, gold highlights, dramatic lighting, premium tech-fantasy style.
```

---

## A3 — Architect Pose

**Output:** `subastian-mascot-A3-full-body-architect-v01.png`
**Used by:** `landing-page/features/`, `ui/onboarding/`
**Status:** not yet generated — generate from the A1 reference (character-reference / image-to-image), not from this prompt alone.

```
Full-body conductor arranging glowing subscription icons into a clean optimized stack. Magical baton emits soft particles guiding the icons. Purple and gold holographic interface floating in front. Cinematic lighting, elegant posture, premium SaaS aesthetic.
```

---

See `../NAMING.md` for the filename spec and character-consistency workflow.
