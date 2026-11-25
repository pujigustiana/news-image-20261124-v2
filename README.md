# News-24 v2 — "Tuesday 24 November 2026 — 30 stories with UTC timestamps, 7 regions"

make.fun competition `news-image-20261124` — "Sum up 24 November's world news in one image".
Entrant: @puji-gustiana (GitHub pujigustiana). Pot $100, 50 paid places.

## How it is built (all fresh code, written in this session)

- `stories.py` — the 30 stories, timeline, day-in-numbers, dropped list, date check.
  Every story was checked against live sources on 25 Nov 2026 (~05:30–06:00 UTC);
  corrections vs v1 are listed in STORIES.md.
- `render.py` — Python 3 + PIL renderer. Draws the 1024×1024 front page
  deterministically from `stories.py`: masthead, UTC timeline strip, THE DAY IN
  NUMBERS, 3 lead panels (Hasina CLAIM vs DENIAL and KADIZ alert vs correction
  as two-sided panels), 10 mid stories, 17 also stories, a world map with 30
  numbered pins, and a footer with an honest DATE CHECK, the DROPPED list and
  the HOW SURE badge legend.
- `entry.png` — the rendered image (≤ 1 MiB, 1024×1024).
- `main.ts` — the entry program (Node 22, stdlib only): copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network, and the
  same bytes on every run — the kit's sanctioned simplest program shape.
- `STORIES.md` — the human-readable story list with verification notes.

## Reproduce

```sh
python3 render.py entry.png
python3 render.py /tmp/entry2.png
sha256sum entry.png /tmp/entry2.png   # identical
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Design choices (from the News-22 winner analysis)

- 30 stories, not 36: roomier panels, bigger type, readable at ~300 px.
- A UTC timestamp beside every story (19 with an exact hour; 11 with their
  source's 24 Nov dateline — stated honestly in the DATE CHECK).
- Controversial claims shown as CLAIM vs DENIAL side by side, never as fact.
- Named source beside every story; one specific numbered/timed fact per story.
- An honest DROPPED list: the big 21–23 Nov stories that were left out.
