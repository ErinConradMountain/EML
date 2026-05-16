# Temporal Loom — Knowledge Surface (Repo-Side)

Purpose: this file is the **compact, stable context** for the Temporal Loom (Temporal Casting) component.

If you are configuring a dedicated ChatGPT Project for Temporal Loom, this is one of the best single files to attach as “knowledge” because it points to the canonical instructions and the repo-side storage conventions.

Important: the ChatGPT Project may be linked to **general ChatGPT memory** (not specific to the project). During casting, memory must be treated as contamination: **Page 0 is the only content source**.

---

## What Temporal Loom Is
Temporal Loom is a **Step 0 companion** in the EML workflow.

It generates a near-range “scaffold run” around a dated **Page 0**:
- five past pages (P−1…P−5)
- five future pages (P+1…P+5)

These pages are **input-only**: they may recombine and regress/progress Page 0 language, but may not import any external topics, domains, or proper nouns.

Temporal Loom outputs are **scaffolding, not evidence**. They are meant to help situate a “floating” dated fragment so it can be handed off cleanly into the Learning Journal Cycle.

---

## Canonical Instruction Surfaces
- Project orientation and usage: [07-Guides/Temporal-Loom/README.md](../../07-Guides/Temporal-Loom/README.md)
- Paste-ready instruction set for the Temporal Loom ChatGPT Project: [08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md](../../08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md)

---

## Where It Fits in the EML Mechanism
Use Temporal Loom when a dated page feels important but temporally unmoored.

Typical handoff:
1) Page 0 (dated anchor) + explicit request for Temporal Loom.
2) Temporal Loom scaffold run (P−5…P+5 excluding Page 0).
3) Step 1 on Page 0 (if Page 0 is raw) to preserve the source writing.
4) Step 2 can optionally use the scaffold run as an outline seed.
5) Step 6 questions may be derived from the future pages *only when requested*.

---

## Storage and Naming
Canonical library:
- Outputs live in [03-Working/Step-0-Temporal-Casting/](./)

Filename convention:
- `Temporal-Casting-YYYY-MM-DD.md` (YYYY-MM-DD = Page 0 anchor date)

Weekly bundle copy (optional):
- If a cast is part of a weekly intake packet, store a copy in:
  - `02-Intake/Weekly/YYYY-WW/Temporal-Casting-YYYY-MM-DD.md`

---

## Minimal “Knowledge Files” to Attach (Suggested)
This checklist is **canonical**. Other docs should link here rather than duplicating the list.

If you are attaching repo files to the dedicated Temporal Loom ChatGPT Project, these are the best anchors:

**Required (Temporal Loom itself)**
- [08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md](../../08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md)
- [07-Guides/Temporal-Loom/README.md](../../07-Guides/Temporal-Loom/README.md)
- [03-Working/Step-0-Temporal-Casting/Temporal-Loom-Knowledge-Surface.md](./Temporal-Loom-Knowledge-Surface.md)

**Recommended (keeps it aligned to the wider mechanism)**
- [08-Admin/Instructions/agent.md](../../08-Admin/Instructions/agent.md)
- [05-Assets/Templates/Weekly-Intake-Template.md](../../05-Assets/Templates/Weekly-Intake-Template.md)
- [08-Admin/Plans/EML-Book-Plan-2026.md](../../08-Admin/Plans/EML-Book-Plan-2026.md)

**Optional (vocabulary + rhythm constraints)**
- [01-Source/Reference/What is EML.txt](../../01-Source/Reference/What%20is%20EML.txt)
- [05-Assets/Readings/Weekend-Ingestion-Layer.md](../../05-Assets/Readings/Weekend-Ingestion-Layer.md)
- [05-Assets/Readings/Learning-as-Inscriptional-Emergence.md](../../05-Assets/Readings/Learning-as-Inscriptional-Emergence.md)
- [06-Lexicon/Definitions/Weekend-Ingestion-Layer.md](../../06-Lexicon/Definitions/Weekend-Ingestion-Layer.md)
- [06-Lexicon/Definitions/Inscriptional-Emergence.md](../../06-Lexicon/Definitions/Inscriptional-Emergence.md)

Notes:
- The “weekly knowledge file” is great context for Journal Reading, but it is often large and week-specific. For Temporal Loom, prefer the stable instruction surfaces above.
