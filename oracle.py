import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def length_truth(feet, piece):
    if not (feet > 0):
        raise ValueError("the run must be above zero")
    if not (piece > 0):
        raise ValueError("the section length must be above zero")
    pieces = math.ceil(feet / piece - 1e-9)
    if pieces <= 10:
        verdict = "a short run honestly"
    elif pieces <= 30:
        verdict = "a weekend run honestly"
    elif pieces <= 100:
        verdict = "a whole-yard run honestly"
    else:
        verdict = "an estate run honestly"
    return f"{feet} {plural(feet, 'foot', 'feet')} of bed against the {piece}-foot section claim is {pieces} {plural(pieces, 'section', 'sections')} - {verdict}."

def overlap_truth(feet, piece, overlap):
    if not (feet > 0):
        raise ValueError("the run must be above zero")
    if not (piece > 0):
        raise ValueError("the section length must be above zero")
    if not (overlap >= 0):
        raise ValueError("the overlap must be zero or more")
    if not (overlap < piece * 12):
        raise ValueError("the overlap must be less than the section length")
    real = piece - overlap / 12
    pieces = math.ceil(feet / real - 1e-9)
    naive = math.ceil(feet / piece - 1e-9)
    hidden = pieces - naive
    if hidden == 0:
        tail = "no hidden sections honestly"
    else:
        if hidden <= 2:
            verdict = "a small secret honestly"
        elif hidden <= 6:
            verdict = "a real secret honestly"
        else:
            verdict = "a pallet of secrets honestly"
        tail = f"{hidden} hidden {plural(hidden, 'section', 'sections')}, {verdict}"
    return f"{feet} feet against the {piece}-foot claim with a {overlap}-inch overlap really covers {fixed1(real)} feet a section: {pieces} {plural(pieces, 'section', 'sections')} - {tail}."

def stake_truth(feet, spacing):
    if not (feet > 0):
        raise ValueError("the run must be above zero")
    if not (spacing > 0):
        raise ValueError("the stake spacing must be above zero")
    stakes = math.ceil(feet / spacing - 1e-9)
    if stakes <= 10:
        verdict = "a pocketful honestly"
    elif stakes <= 25:
        verdict = "a small box honestly"
    elif stakes <= 60:
        verdict = "a box of stakes honestly"
    else:
        verdict = "several boxes honestly"
    return f"{feet} {plural(feet, 'foot', 'feet')} at a stake every {spacing} {plural(spacing, 'foot', 'feet')} is {stakes} {plural(stakes, 'stake', 'stakes')} - {verdict}."

FNS = {"lengthTruth": length_truth, "overlapTruth": overlap_truth, "stakeTruth": stake_truth}

cases = [
 {"fn":"lengthTruth","args":[120,4]},
 {"fn":"lengthTruth","args":[30,4]},
 {"fn":"lengthTruth","args":[200,4]},
 {"fn":"lengthTruth","args":[500,4]},
 {"fn":"lengthTruth","args":[1,4]},
 {"fn":"lengthTruth","args":[80,4]},
 {"fn":"lengthTruth","args":[0,4]},
 {"fn":"lengthTruth","args":[120,0]},
 {"fn":"overlapTruth","args":[120,4,3]},
 {"fn":"overlapTruth","args":[120,4,0]},
 {"fn":"overlapTruth","args":[40,4,6]},
 {"fn":"overlapTruth","args":[300,4,6]},
 {"fn":"overlapTruth","args":[1000,4,6]},
 {"fn":"overlapTruth","args":[50,4,2]},
 {"fn":"overlapTruth","args":[120,4,48]},
 {"fn":"overlapTruth","args":[120,4,-1]},
 {"fn":"overlapTruth","args":[0,4,3]},
 {"fn":"stakeTruth","args":[120,3]},
 {"fn":"stakeTruth","args":[20,3]},
 {"fn":"stakeTruth","args":[60,3]},
 {"fn":"stakeTruth","args":[300,3]},
 {"fn":"stakeTruth","args":[1,3]},
 {"fn":"stakeTruth","args":[0,3]},
 {"fn":"stakeTruth","args":[120,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
