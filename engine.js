// Edging Math engine - hypothetical arithmetic on labeled norms only.
// Section, overlap and stake figures are illustrative norms; soil, terrain
// and corner cuts change real runs.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function lengthTruth(feet, piece) {
  if (!(feet > 0)) throw new Error("the run must be above zero");
  if (!(piece > 0)) throw new Error("the section length must be above zero");
  const pieces = Math.ceil(feet / piece - 1e-9);
  let verdict;
  if (pieces <= 10) verdict = "a short run honestly";
  else if (pieces <= 30) verdict = "a weekend run honestly";
  else if (pieces <= 100) verdict = "a whole-yard run honestly";
  else verdict = "an estate run honestly";
  return `${feet} ${plural(feet, "foot", "feet")} of bed against the ${piece}-foot section claim is ${pieces} ${plural(pieces, "section", "sections")} - ${verdict}.`;
}

function overlapTruth(feet, piece, overlap) {
  if (!(feet > 0)) throw new Error("the run must be above zero");
  if (!(piece > 0)) throw new Error("the section length must be above zero");
  if (!(overlap >= 0)) throw new Error("the overlap must be zero or more");
  if (!(overlap < piece * 12)) throw new Error("the overlap must be less than the section length");
  const real = piece - overlap / 12;
  const pieces = Math.ceil(feet / real - 1e-9);
  const naive = Math.ceil(feet / piece - 1e-9);
  const hidden = pieces - naive;
  let tail;
  if (hidden === 0) tail = "no hidden sections honestly";
  else {
    let verdict;
    if (hidden <= 2) verdict = "a small secret honestly";
    else if (hidden <= 6) verdict = "a real secret honestly";
    else verdict = "a pallet of secrets honestly";
    tail = `${hidden} hidden ${plural(hidden, "section", "sections")}, ${verdict}`;
  }
  return `${feet} feet against the ${piece}-foot claim with a ${overlap}-inch overlap really covers ${fixed1(real)} feet a section: ${pieces} ${plural(pieces, "section", "sections")} - ${tail}.`;
}

function stakeTruth(feet, spacing) {
  if (!(feet > 0)) throw new Error("the run must be above zero");
  if (!(spacing > 0)) throw new Error("the stake spacing must be above zero");
  const stakes = Math.ceil(feet / spacing - 1e-9);
  let verdict;
  if (stakes <= 10) verdict = "a pocketful honestly";
  else if (stakes <= 25) verdict = "a small box honestly";
  else if (stakes <= 60) verdict = "a box of stakes honestly";
  else verdict = "several boxes honestly";
  return `${feet} ${plural(feet, "foot", "feet")} at a stake every ${spacing} ${plural(spacing, "foot", "feet")} is ${stakes} ${plural(stakes, "stake", "stakes")} - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { lengthTruth, overlapTruth, stakeTruth };
}
