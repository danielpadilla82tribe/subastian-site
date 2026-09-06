#!/usr/bin/env bash
# Emit hosting URLs for every image committed under subastian-brand/.
#
#   ./cdn-urls.sh              # branch @main — use while iterating
#   ./cdn-urls.sh brand-v1     # tag — permanent, use for external listings
#   ./cdn-urls.sh --html       # also print ready-to-paste <img> tags
#
set -euo pipefail

GH_USER="danielpadilla82tribe"
GH_REPO="subastian-site"
SITE="https://subastian.us"

REF="main"
EMIT_HTML=0
for arg in "$@"; do
  case "$arg" in
    --html) EMIT_HTML=1 ;;
    -*)     echo "unknown flag: $arg" >&2; exit 2 ;;
    *)      REF="$arg" ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

mapfile -t FILES < <(
  find subastian-brand -type f \
    \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \
       -o -iname '*.webp' -o -iname '*.avif' -o -iname '*.svg' \) \
  | sort
)

if [ ${#FILES[@]} -eq 0 ]; then
  echo "No images found under subastian-brand/ yet."
  echo "Generate them from mascot/<style>/prompts.md and name them per mascot/NAMING.md."
  exit 0
fi

if [ "$REF" = "main" ]; then
  echo "# ref: @main  (12-hour jsDelivr cache — fine while iterating)"
else
  echo "# ref: @$REF  (permanent, immutable cache — safe for external listings)"
fi
echo "# ${#FILES[@]} image(s)"
echo

for f in "${FILES[@]}"; do
  cdn="https://cdn.jsdelivr.net/gh/${GH_USER}/${GH_REPO}@${REF}/${f}"
  own="${SITE}/${f}"
  echo "$(basename "$f")"
  echo "  same-origin (use on subastian.us): $own"
  echo "  jsDelivr    (use off-site):        $cdn"
  if [ "$EMIT_HTML" -eq 1 ]; then
    alt="$(basename "${f%.*}" | sed 's/^subastian-mascot-//; s/-v[0-9]*$//; s/-/ /g')"
    echo "  <img src=\"$cdn\" alt=\"Subastian conductor mascot, $alt\" loading=\"lazy\" decoding=\"async\">"
  fi
  echo
done

if [ "$REF" = "main" ]; then
  echo "# Shipping to AppSumo / Product Hunt? Tag first, then re-run with the tag:"
  echo "#   git tag brand-v1 && git push origin brand-v1 && ./cdn-urls.sh brand-v1 --html"
fi
