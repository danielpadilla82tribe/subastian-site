# Asset hosting — GitHub + jsDelivr (Option A)

## Read this first: you may not need the CDN for the site itself

This repository *is* the `subastian.us` site. GitHub Pages already serves
everything committed here, over its own CDN (Fastly), on your own domain. So an
image at:

```
subastian-brand/mascot/full-body-cinematic/variations/subastian-mascot-A1-full-body-hero-v01.png
```

is already reachable at:

```
https://subastian.us/subastian-brand/mascot/full-body-cinematic/variations/subastian-mascot-A1-full-body-hero-v01.png
```

For images used **on the landing page**, reference them with a root-relative
path (`/subastian-brand/...`) and skip jsDelivr entirely. Routing your own
page's images through a third-party CDN adds a DNS lookup and a TLS handshake
to a second origin for no benefit, and exposes you to jsDelivr's 12-hour
branch-cache staleness on every update.

**jsDelivr earns its place for placements you don't control**: AppSumo listing
images, Product Hunt gallery, email templates, a page builder on someone else's
domain. Those need an absolute public URL that isn't tied to your Pages deploy.

## URL format

```
https://cdn.jsdelivr.net/gh/danielpadilla82tribe/subastian-site@<ref>/<path>
```

Worked example:

```
https://cdn.jsdelivr.net/gh/danielpadilla82tribe/subastian-site@main/subastian-brand/mascot/full-body-cinematic/variations/subastian-mascot-A1-full-body-hero-v01.png
```

Run `./cdn-urls.sh` in this folder to generate these for every image present,
rather than assembling them by hand.

## Choosing `<ref>` — this is the part that bites people

| Ref form         | Example              | Cache behaviour                          |
|------------------|----------------------|-------------------------------------------|
| Branch           | `@main`              | **12 hours.** Updates appear, eventually.  |
| Omitted          | *(no `@`)*           | Same as default branch — same staleness.   |
| Tag              | `@brand-v1`          | **Permanent, immutable.** Never re-served. |
| Commit SHA       | `@2f362db`           | Permanent, immutable.                      |

The trap: a **tag or commit URL is cached permanently on jsDelivr's S3**. Once a
file has been fetched at that address, you cannot change what those bytes are —
re-pushing the tag will not help. That is exactly what you want for a shipped
AppSumo listing, and exactly what you must not do while still iterating.

So:

- **While iterating** → use `@main`, accept the 12-hour lag.
- **When shipping an external listing** → tag it (`git tag brand-v1 && git push
  origin brand-v1`) and use the tag URL. It can never break under you.
- **Never** overwrite a file behind a published tag. Ship `v02` and re-tag.

Purge for branch URLs is available at `purge.jsdelivr.net/gh/...`; purging
*versioned* URLs requires a valid semver release and access granted by request,
so do not plan around being able to undo a tagged mistake.

## Requirements and limits

- **The repository must be public.** jsDelivr only serves public GitHub repos.
  This one is public already (it's a Pages site on a custom domain), but confirm
  before relying on it.
- **File size:** jsDelivr's documented per-file cap could not be verified while
  writing this — their docs host is unreachable from this environment. Treat it
  as unresolved and check before committing anything large.
- **Size matters more for page speed than for the cap anyway.** A hero PNG
  above ~500 KB will hurt LCP badly enough to undo the performance work already
  in `index.html` (hero preload, `fetchpriority="high"`, explicit dimensions).
  Compress before committing: `pngquant --quality 65-85`, or ship WebP/AVIF with
  a PNG fallback.

## Workflow

1. Generate images from the prompts in `../mascot/<style>/prompts.md`.
2. Name them per `../mascot/NAMING.md`.
3. Drop them into the matching `variations/` folder.
4. Compress.
5. Commit and push.
6. Run `./cdn-urls.sh` to emit CDN URLs and ready-to-paste `<img>` tags.
7. Tag before using any URL in an external listing.

`deployment/` holds deploy notes and any tag manifests; `assets/` is for
hosting-related files that aren't mascot art (og-image composites, favicon
exports).
