# Edging Math

Honest garden-edging arithmetic. The box claims twenty feet of edge; Edging Math counts the
sections, the hidden overlap and the stakes the bed was always going to ask for.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The length truth** - bed length against the section claim: the honest section count.
- **The overlap truth** - every interlocking joint spends a few inches: the hidden sections the box never mentions.
- **The stake truth** - the run at the stake-spacing norm: whole stakes.

## The boundary

Edging Math keeps section, overlap and stake arithmetic only. Every length, overlap and
spacing figure is a labeled norm, not a promise - soil, terrain and corner cuts change real
runs. Call 811 before any digging, and follow the manufacturer's instructions over anything
this page says. Every figure is hypothetical arithmetic on labeled norms, not a statement
about any real edging, stake or yard.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json
node test.js        # 24 cases / 24 checks, 0 failed
```
