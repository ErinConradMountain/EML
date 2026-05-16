---
description: "Use when creating or editing temporal casting outputs, temporal loom entries, or Step 0 scaffold runs. Covers input-only constraints, step detection, dating rules, and the output contract for temporal casting."
applyTo: "03-Working/Step-0-Temporal-Casting/**"
---

# Temporal Casting (Step 0) Conventions

## What It Is

An input-only scaffold run around a dated anchor (Page 0) that generates 5 past + 5 future entries. Creates a breadcrumb trail showing plausible daily sequence. **Scaffolding, not evidence** — must not overwrite source material.

## When to Use

- When a dated item feels "floating" (missing lead-up or continuation)
- During weekly intake or weekend ingestion
- As optional companion to Steps 1-3

## Input-Only Constraint

- All predictions come from Page 0 only
- No new topics, authors, theories, or proper nouns unless in Page 0 verbatim
- No background context, biography inference, or external knowledge
- Allowed: reuse exact words, recombine into earlier forms, project implied next moves

## Output Format

Exactly 10 entries. Each:

```
Date: YYYY-MM-DD
Title: Step N - <descriptive title> [AnchorDate: YYYY-MM-DD] [Page: P±N] [Cast: Temporal]
Rationale: <input-only causal rationale quoting ≥2 Page 0 phrases>
```

## File Naming

- Default: `Temporal-Casting-<AnchorDate>.md`
- Location: `03-Working/Step-0-Temporal-Casting/`
- Update `Temporal-Casting-Index.md` with anchor date, cast file, detected step, and handoff target

## After Casting

- If Page 0 is raw: run Step 1 on Page 0
- Use past pages to guide verification
- Use future pages as prompts or Step 2 outline seeds
