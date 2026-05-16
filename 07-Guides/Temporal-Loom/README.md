# Temporal Loom (EML) — Orientation & Operating Guide

**Component name:** Temporal Loom  
**ChatGPT Project name (recommended):** **EML — Temporal Loom**  
**One-line purpose:** weave a dated Page 0 into a near-range sequence of *input-only* scaffold pages (five before, five after) so the writing has temporal context without importing external content.

---

## Why This Exists (What Problem It Solves)
Some pages arrive *true* but temporally unmoored.
- A dated fragment is strong, but it’s unclear what it emerged from.
- A dated note is coherent, but it doesn’t yet “sit” inside a daily sequence.
- A weekly intake has isolated islands; you want bridges made from the island’s own stone.

Temporal Loom creates a **scaffold run**: a short ring of plausible pages around Page 0.
- It does **not** claim historical accuracy.
- It does **not** plan a future.
- It describes **directional emergence** using only Page 0’s internal logic.

This makes it a precise fit for EML’s stance:
- writing as system memory
- learning as accretion and return
- time as a designed substrate

---

## Where It Fits in the EML Mechanism
Temporal Loom is a **Step 0 companion** that sits *before* (or alongside) the Learning Journal Cycle.

### Typical flow (external ChatGPT → repo)
1) **Capture** a dated text (handwritten transcript, weekly note, field-journal snippet).
2) Run **Temporal Loom** to generate P−5…P−1 and P+1…P+5.
3) File the result in one place (see “Storage & naming”).
4) Use it as a *map* for the Learning Journal Cycle:
   - Step 1 (Polished Notes) stays faithful to the handwriting.
   - Step 2 (Analytical Study) can use the scaffold run as an outline seed.
   - Step 3 (Essay) can use future pages as near-term test vectors.
   - Step 6 (Questions) can be derived from the “future move” logic *only when requested*.

### What it feeds (and what it must NOT do)
Feeds:
- Step 1/2 framing: what tensions and partial definitions were likely present.
- Step 2 structure: candidate ordering of terms/claims already in Page 0.
- Step 6 prompts: near-term questions latent in Page 0.

Must NOT:
- replace the source text
- introduce outside theory or extra facts
- become a “life coach” or a planning system

---

## Core Contract (Non-Negotiable)
Temporal Loom is deterministic, strict, and file-placeable.

### Trigger
Run only when the input includes:
- a dated anchor text, and
- an explicit request for casting / before-after pages.

### Output shape
Exactly 10 entries:
- 5 past pages (P−1 through P−5)
- 5 future pages (P+1 through P+5)

Each entry has exactly:
- Date
- Title
- Rationale

### Input-only constraint
The output must be generated from **Page 0 only**.
- No new proper nouns.
- No new domains.
- No new “helpful background.”

You are allowed to:
- recombine Page 0 language
- regress it into earlier scaffolds
- push it forward into near-term tests

---

## Global Memory Contamination (Important)
The **EML — Temporal Loom** ChatGPT Project may be linked to general ChatGPT memory (not specific to the project).

For Temporal Loom outputs:
- Memory and broader conversation context must be treated as **contamination**.
- The only semantic content source is the provided **Page 0** text.
- Knowledge files attached to the project are for **constraints and workflow**, not for feeding topic content into casts.

If a cast “mysteriously” introduces new topics, proper nouns, or external theory, treat it as contamination and re-run with stricter reminder language.

---

## Storage & Naming (Repo-Side)
This repo stores Temporal Loom outputs in:
- `03-Working/Step-0-Temporal-Casting/`

**Default filename**
- `Temporal-Casting-YYYY-MM-DD.md` (YYYY-MM-DD = Page 0 anchor date)

**When to store in weekly bundle instead**
- If the cast is explicitly part of a weekly intake packet, store a copy in:
  - `02-Intake/Weekly/YYYY-WW/Temporal-Casting-YYYY-MM-DD.md`

Rule of thumb:
- `03-Working/Step-0-Temporal-Casting/` = canonical library
- `02-Intake/Weekly/...` = weekly working copy

---

## How to Use the Output (Practical Moves)
Treat the scaffold run like a **staging diagram**.

### Using past pages (P−5…P−1)
- Identify which terms/phrases are “still liquid” in the run.
- Use them as *questions to ask the handwriting* during Step 1/2:
  - “Is this tension actually present in the scan?”
  - “Where does Page 0 declare something final that earlier pages were still testing?”

### Using future pages (P+1…P+5)
- Use as near-term continuation prompts:
  - next notebook entry ideas
  - Step 2 outline extension
  - Step 3 essay section candidates

### Converting to Step 6 (only when requested)
- Map each future page into a creative question.
- Keep the questions anchored to Page 0’s language (no new topics).

---

## Integration Points (Weekly Intake Template)
The weekly template now includes a **Temporal Casting (Optional Scaffold Run)** section.
Use it to record:
- which raw item was cast
- anchor date
- filename
- save location

This makes Temporal Loom auditable: you can always trace scaffold outputs back to the exact Page 0.

---

## Knowledge Files to Attach (ChatGPT Project Configuration)
Use the canonical checklist in the repo-side knowledge surface:
- [03-Working/Step-0-Temporal-Casting/Temporal-Loom-Knowledge-Surface.md](../../03-Working/Step-0-Temporal-Casting/Temporal-Loom-Knowledge-Surface.md)

That file is the single source of truth for Required/Recommended/Optional attachments.

Note: keep attached files as behavioral constraints only; during casting, Page 0 is the only semantic content source.

---

## Failure Modes (What to Watch For)
If the output feels “wrong,” it is usually one of these:

1) **Outside contamination**
   - The assistant imported external context.
   - Fix: restate “input-only constraint” and re-run.

2) **Summary drift**
   - The assistant summarized Page 0 instead of generating scaffold pages.
   - Fix: re-run; remind that Page 0 is never rewritten.

3) **Premature closure**
   - Past pages are too resolved, or future pages become “finished system.”
   - Fix: enforce exploratory past + near-term provisional future.

4) **Cadence mismatch**
   - The assistant assumes a weekly cadence or skips days.
   - Fix: enforce “one writing cycle per day; consecutive dates.”

---

## Creative Metaphor (So It Stays Memorable)
Temporal Loom is not a fortune-teller.
It is a loom.

- Page 0 is the **warp**: fixed strands, already present.
- Past and future pages are the **weft**: threads that must pass through the warp’s constraints.
- The output is a small swatch of fabric: enough to see pattern, not enough to claim a whole garment.

That is why the input-only constraint matters: the loom may weave, but it cannot import new fiber.

---

## Quickstart Prompts (External Chat Use)
Use one of these:

- “Apply Temporal Loom to the text below. Input-only. Ten entries. Use the deterministic step ladder.”
- “Temporal Loom: treat this as Page 0; generate P−5..P−1 and P+1..P+5, each with Date/Title/Rationale. Do not rewrite Page 0.”

Then paste the dated Page 0.

---

## Related Docs
- `08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md`
- `05-Assets/Templates/Weekly-Intake-Template.md`
- `08-Admin/Plans/EML-Book-Plan-2026.md`
