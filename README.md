# News summary v2 — 11 November 2026 world news

Second entry for the make.fun `news-summary-01` bounty: a program that writes
one English summary of 11 November 2026 world news, with no network access.

## What it does

`main.py` writes a single UTF-8 summary to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`). The summary covers seventeen specific,
checkable events from 11 November 2026 across regions and fields — diplomacy,
energy, climate, economics, health, politics, defence, technology, science,
religion, and sport — naming the source outlet for each event. It stays
inside the 1-2000 character gate and uses plain ASCII text.

## Why a second version

The first entry ranked in the mid-60s on the live development leaderboard.
This version adds broader regional and topical coverage and is shorter,
because the leaderboard breaks judge-score ties by artifact size (smaller
wins). Every event was verified against a published report dated
11 November 2026 before it was included.

## Files

- `main.py` — the entry program (Python 3 standard library only).
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout wallet binding.

## Run it

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
wc -c /tmp/out/entry.txt
```

## Determinism

Same input, same output: the program is a fixed string written to disk, so
repeated runs are byte-identical.
