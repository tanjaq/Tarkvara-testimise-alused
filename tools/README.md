# tools — the page generators

The lesson decks, the homework pages and the course homepage are **generated**
from the Python files in this folder. The HTML in the repository root is build
output.

## Rebuilding everything

```bash
cd tools
python3 build.py
```

Needs only Python 3 — no packages to install. It writes `index.html`,
`lesson-*.html` and `homework/` into the repository root.

## ⚠️ Read this before editing a lesson by hand

**Editing the HTML directly works, but the next rebuild overwrites it.**
If you change a slide, change it here — in the matching `lNN_NN.py` — and run
`build.py`. Otherwise your edit lives until someone regenerates, and then
silently disappears.

If you would rather stop using the generators altogether, delete this folder and
treat the HTML as the source of truth. That is a perfectly reasonable choice —
just make it deliberately, because the two approaches cannot both be true.

## What lives where

| File | Produces |
|---|---|
| `tpl.py` | The shared template: CSS, the slide helpers, the nav bar, the ESC-to-index behaviour. Imported by the others, never run on its own. Change the design system here and every deck follows. |
| `l01_04.py` | `lesson-01.html`, `lesson-02.html` |
| `l03_05.py` | `lesson-03.html` … `lesson-05.html` |
| `l06_08.py` | `lesson-06.html` … `lesson-08.html` |
| `l09_10.py` | `lesson-09.html`, `lesson-10.html` |
| `l11_13.py` | `lesson-11.html` … `lesson-13.html` |
| `bonus.py` | `lesson-bonus-ai.html`, `lesson-bonus-performance.html`, `lesson-bonus-security.html` |
| `hw.py` | `homework/index.html` and `homework/hw-01.html` … `hw-12.html` |
| `index.py` | `index.html` — the course homepage cards and badges |

The file names are historical: `l01_04.py` no longer writes lessons 3 and 4.
What each one actually produces is the table above.

## Not generated

These are maintained by hand and `build.py` leaves them alone:

- `compact/index.html` — the six-session compact track
- `homework/testing-process-worksheet.html` — the fillable worksheet
- `materials/` — SRS template, worksheets, sample database, the trip planner form
- `images/` — diagrams extracted from the original lecture decks
- `README.md`

## How a lesson is put together

`write_lesson()` in `tpl.py` takes the lesson number, title, subtitle, the focus
line, the lesson-plan topics, the homework line, and then a list of slides. Each
slide is a plain `<section>…</section>` string. To add a slide, drop another
string into that list; to reorder, move it.

`img("file.png", "alt text", "62%", "caption")` builds a figure that is sized
against reveal.js's 700px slide box. Keep images at or under 380px tall for a
full-width figure and 300px inside a `.g2`/`.g3` grid, or the slide overflows
and reveal shrinks the whole thing.

Homework pages are data, not markup: the `HW` list in `hw.py` holds one dict per
assignment with its steps, deliverable, assessment criteria and resources.
Adding or removing an assignment there updates the briefs, the overview table
and the card grid together — but the badges on the homepage live in `index.py`,
and the homework slide at the end of each lesson lives in its `lNN_NN.py`, so
those two need the same change by hand.
