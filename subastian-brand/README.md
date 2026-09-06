# subastian-brand

Brand asset workspace: mascot prompts, generated art, and the placements it
feeds. No images are committed yet — this is the scaffold and the specs.

```
subastian-brand/
├── mascot/
│   ├── NAMING.md                 ← filename spec, palette, consistency workflow
│   ├── full-body-cinematic/      ← Set A: hero slots, portrait framing
│   ├── mid-shot-saas/            ← Set B: feature rows, UI-adjacent
│   └── silhouette-minimal/       ← Set C: small sizes, social, dividers
│       └── <each>/prompts.md + variations/
├── landing-page/   hero · features · pricing · faq · final-cta
├── appsumo/        hero · features · pricing
├── product-hunt/   gallery · tagline · first-comment
├── ui/             onboarding · purchase-guard · neglect-radar · renewal-alerts
└── cloud/
    ├── readme.md                 ← hosting: GitHub + jsDelivr
    ├── cdn-urls.sh               ← generates CDN URLs + <img> tags
    ├── deployment/
    └── assets/
```

## Start here

1. `mascot/NAMING.md` — read before generating anything. It covers the filename
   spec, the palette the art has to match, and how to stop nine prompts from
   producing nine different-looking men.
2. `mascot/<style>/prompts.md` — the prompts themselves.
3. `cloud/readme.md` — where the finished images live and how to link them.

## Two decisions still open

- **Gold.** Every prompt calls for gold trim and gold rim light, but the site
  has no gold token — see the palette section of `mascot/NAMING.md`. Settle this
  before generating, or the mascot will not match the page it sits on.
- **Transparency.** The site renders light *and* dark from one markup. A baked
  background will band against one of them.

## Note on visibility

This repo is public (it serves `subastian.us` via GitHub Pages), so everything
here is publicly readable — including these prompt files, both on GitHub and at
`subastian.us/subastian-brand/…`. That's fine for art assets; just don't put
anything in here you wouldn't publish.
