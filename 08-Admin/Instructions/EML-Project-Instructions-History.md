# EML Project Instructions History

This file tracks how project and chat instructions evolve over time. It is intended to be:
- A memory of past operating rules.
- A surface for pattern-finding (what keeps changing, what stabilises).
- A source to reuse or merge earlier instruction sets when refining the system.

When instructions are updated in chat, append a new dated section with:
- A short summary of changes.
- Any revised definitions or cycles in full.

## 2026-02-01 Custom Instructions Length Limit

Summary of changes:
- Added a hard length limit: ChatGPT Project custom instructions must be under 8000 characters.
- Applied the limit to `Journal-Reading-ChatGPT-Custom-Instructions-2026-01-26.md` and `Temporal-Casting-ChatGPT-Project-Custom-Instructions.md`.
- Trimmed and re-encoded the Temporal Casting instructions to stay under the limit.
- Updated `agent.md` and the external coordination guide to enforce the limit.

## 2026-02-01 Weekly Integration and Instruction Alignment

Summary of changes:
- Integrated the Journal Reading custom instructions into `08-Admin/Instructions/agent.md`.
- Re-affirmed distinct step outputs (one step per response unless asked to combine).
- Added explicit tagging requirements for Step 2-6 outputs (Book Part + EML layer).
- Added file placement rule: end file-ready outputs with a proposed save location.
- Re-emphasized weekend ingestion mode and the weekly knowledge file as the context anchor.
- Normalized `agent.md` to ASCII to avoid encoding drift in instructions.

## 2026-01-26 Learning Journal Cycle Default Engine Update

Summary of changes:
- Updated the Learning Journal Cycle operating rule: Steps 1–3 are the default engine; Steps 4–6 are selective.
- Clarified that every step output should carry Book Part and EML layer tags (and can include an additional layer tag if relevant).
- Standardised wording/characters (removed stray control characters) to keep the instructions copy-paste safe for ChatGPT custom instructions.
Summary of changes:
- Expanded the weekly intake workflow by codifying Steps 0-10 in `05-Assets/Templates/Weekly-Intake-Template.md`, ensuring Step 5 key ideas, Step 6 evaluation, asset mapping, style notes, and the bridge checklist live in one place.
- Added readings (`Learning-as-Inscriptional-Emergence` and `Weekend-Ingestion-Layer`) plus lexicon entries to keep the intake-digestion-metabolism metaphors accessible for future weeks.

Summary of changes:
- Added explicit focus on evolving personal voice and lexicon to the agent instructions.
- Treated handwritten notes and daily entries as the primary source of tone and vocabulary.
- Updated the weekly intake template to track new phrases, emerging terms, and tone shifts.
- Adopted a refined, six-step Learning Journal Cycle as the core process for working with handwritten notes.

### Learning Journal Cycle (Core Process) – Version 2026-01-18
**Goal**  
Turn handwritten notes into a scaffolded reading platform that (a) strengthens your own thinking, and (b) produces tagged assets (readings, diagrams, circuits, concepts) that feed the next writing cycle and the EML book (by Part and by EML layer).

Not every piece of writing needs to go through all six steps. Steps 1–2 are the default engine; Steps 3–6 are used selectively when a topic is ready to be extended or tested.
---


**Input:**
- Images or scans of handwritten notes (first draft), plus any immediate context from the week.

**Output:**
  - improves clarity and language,

**Purpose:**
- Preserve the lived thinking in a clean, readable form.
- Create a stable "reading object" that later steps can analyse, extend, and reuse.
---


**Input:**
- The original handwriting and the Step 1 polished notes.

**Output:**
- A structured analysis that includes:
  - Date and working title,
  - notes on implications, tensions, or design questions.
**Purpose:**
- Make the implicit structure explicit.
- Surface where time, canon, scaffolds, and agency are at work.
- Decide whether this topic merits Step 3 and beyond.
---


**Input:**
- Step 1 and Step 2 outputs for a selected topic.

**Output:**
- An academic-style essay that:
  - has a short abstract,
  - identifies which book part(s) it might feed (Orientation / Grammar / Circuits / Futures),

**Purpose:**
- Push promising ideas to the next conceptual level.
- Generate book-ready material while still anchored in the original notes.
---


**Input:**
- Steps 1–3 for a chosen topic.

**Output:**
- A short, beginner-friendly guide that:
  - includes reflection and action prompts (Reflect / Try),

**Purpose:**
- Translate dense thinking into accessible language for teachers/students/general readers.
- Build a library of "short readings" that can plug into the exhibit, the book, or training.
---


**Input:**
- Steps 1–4, with emphasis on Step 3.

**Output:**
- A list or table of key ideas where each entry includes:
  - a one-sentence claim,
  - relevant EML layer(s) (structural / cognitive-temporal / agentic),

**Purpose:**
- Distil the weeks work into portable units that are easy to move into outlines, diagrams, and chapters.
- Maintain a running "idea index" that grows over the year.
---

### Step 6 – Evaluation (Questions and Feedback Loop)

- Any topic that has reached at least Step 2 (ideally Step 3 or 4), plus fresh handwritten responses.

**Output:**

- Four generative questions that:
  - extend or complicate the topic,
  - can seed next weeks handwriting or classroom experiments.

  - what worked, whats missing,

**Purpose:**
- Close the loop from reading back to new writing.
- Turn the weeks work into prompts and feedback that shape the next cycle.
---


**Distinct steps:**

**Grounding:**

**Selective deepening:**
- Not every item needs all six steps. Use Steps 36 for topics that feel alive, central, or recurrent in the weeks work.

- As you go, tag outputs with:
  - Book Part (Orientation / Grammar / Circuits / Futures),

**Reading layer:**
- Treat the final outputs (especially Steps 35) as a reading platform for your future self: they should be calm, clear, re-readable, and ready to be dropped into the book or into teacher-facing materials.

**Temporal function:**
- Every cycle should both harvest the weeks learning and aim the next week (via questions, experiments, and focus areas).

## 2026-01-18 Folder Structure and Intake Organization

Summary of changes:
- Added a folder structure that mirrors the handwritten-first intake -> cycle -> assets -> book flow.
- Created a weekly collection inbox and dedicated locations for writing help and definitions.
- Documented naming conventions and suggested placements in `EML-Folder-Structure.md`.

Notes:
- Structure is additive; no files were moved.

## 2026-02-01 Temporal Loom (Temporal Casting) Added

Summary of changes:
- Added **Temporal Loom** as an integrated Step 0 companion that generates an input-only scaffold run around a dated Page 0 (five past pages + five future pages).
- Established a dedicated ChatGPT-side instruction set to keep casting deterministic and prevent outside-context contamination.
- Integrated a capture slot for casting into the weekly intake template so casts can be indexed and filed during the week.

Key rules (canonical):
- Casting is input-only: no new topics, domains, or proper nouns beyond the Page 0 text.
- Output is exactly 10 entries (5 past, 5 future), each with Date/Title/Rationale.
- Casting output is scaffolding, not evidence; it must not overwrite source writing.

New/updated locations:
- Instructions: `08-Admin/Instructions/Temporal-Casting-ChatGPT-Project-Custom-Instructions.md`
- Guide: `07-Guides/Temporal-Loom/README.md`
- Output library: `03-Working/Step-0-Temporal-Casting/`
- Weekly template updated: `05-Assets/Templates/Weekly-Intake-Template.md`

## 2026-02-01 Step 7 Cast Ahead Added

Summary of changes:
- Added **Step 7 – Cast Ahead** as a forward-only 5-day projection step in the Learning Journal Cycle.
- Updated templates and core guides to reference Steps 1–7 and renumber weekly intake sections.
- Added a dedicated output folder for cast-ahead files.

New/updated locations:
- `08-Admin/Instructions/Journal-Reading-ChatGPT-Custom-Instructions-2026-01-26.md`
- `08-Admin/Plans/EML-Book-Plan-2026.md`
- `05-Assets/Templates/Weekly-Intake-Template.md`
- `03-Working/Step-7-Cast-Ahead/`

## 2026-05-02 Read-Write Model and ChatGPT Mobile Knowledge Feed Added

Summary of changes:
- Added a root `AGENTS.md` so Codex and other assistants can orient from one project-level contract.
- Created `03-Working/Read-Write-Model/` as the focused study lane for inscription, AI projection, human re-entry, revision, and drift control.
- Created `09-ChatGPT-Knowledge-Feed/` as the controlled membrane between Erin's cell, ChatGPT project work, and the local EML folder.
- Added project-local skill files under `08-Admin/Skills/`.
- Added new Copilot/Codex agent and instruction files for Read-Write Model development and mobile knowledge intake.

Key rules (canonical):
- Preserve raw mobile wording before polishing.
- Every ChatGPT/mobile return packet should include source, faithful summary, Book Part, EML Layer(s), proposed route, and one question to return to handwriting.
- Read-Write Model work should identify the loop stage: inscription, projection, re-entry, revision, or drift control.
- Large journal sources should be indexed and routed, not duplicated or silently moved.

New/updated locations:
- `AGENTS.md`
- `03-Working/Read-Write-Model/`
- `09-ChatGPT-Knowledge-Feed/`
- `08-Admin/Skills/Read-Write-Model.skill.md`
- `08-Admin/Skills/ChatGPT-Mobile-Knowledge-Feed.skill.md`
- `.github/agents/read-write-model.agent.md`
- `.github/agents/mobile-knowledge-intake.agent.md`
- `.github/instructions/read-write-model.instructions.md`
- `.github/instructions/chatgpt-mobile-feed.instructions.md`

## 2026-05-02 April Archive Integrated

Summary of changes:
- Integrated the extracted `April 2026 Archive/` into the broader EML project.
- Converted 97 `.docx` files into routed Markdown working copies while preserving originals.
- Routed EML Book outputs into the main Learning Journal Cycle folders.
- Routed Reading-Writing Model outputs into `03-Working/Read-Write-Model/`.
- Created `03-Working/Knowledge-Space-Semiotics/` for visual grammar, page navigation, marker stability, colour logic, satellite perspective, staged observation, and semiotic sequencing.
- Routed April lexicon/key terms into `06-Lexicon/Definitions/April-2026-Archive/`.

Key rules (canonical):
- Original archive files remain preserved in `April 2026 Archive/`.
- Converted working copies must keep provenance comments naming the original archive path.
- Knowledge Space / Semiotics is now a distinct working lane, not a miscellaneous asset bucket.
- Colour, markers, page position, and perspective should be treated as functional grammar, not visual decoration.

New/updated locations:
- `02-Intake/Monthly/2026-04/April-2026-Integration-Map.md`
- `08-Admin/Indices/April-2026-Archive-Import-Manifest.md`
- `03-Working/Knowledge-Space-Semiotics/`
- `05-Assets/Visual-Language/2026-05-02-colour-as-functional-grammar.md`
- `05-Assets/Diagrams/2026-05-02-page-as-navigation-system-diagram-brief.md`
- `08-Admin/Skills/Knowledge-Space-Semiotics.skill.md`
- `.github/agents/knowledge-space-semiotics.agent.md`
- `.github/instructions/knowledge-space-semiotics.instructions.md`

## 2026-05-16 Architecture Cleanup and Knowledge Base Refresh

Summary of changes:
- Normalized the focused-study Step 2 folders to `Step-2-Analytical-Study` so they match the main Learning Journal naming.
- Moved stray root-level capture files back into `00-Inbox/`.
- Updated the active weekly anchor to `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md`.
- Clarified authority between the active `.github/` instruction layer and the detailed project guidance in `08-Admin/Instructions/agent.md`.
- Refreshed the portable ChatGPT knowledge docs and external coordination guides so they point to the current May 2026 operating context.
- Added a quarantine report for stale January references that remain inside preserved raw exports and backup-heavy source files.
- Added README scaffolds for `04-Book/`, `04-Book/Part-04-Futures/`, `06-Lexicon/`, and the empty `Terms/` and `Phrases/` lanes.
- Normalized `06-Lexicon/Definitions/Weekend-Ingestion-Layer.md` and `06-Lexicon/Definitions/Inscriptional-Emergence.md` from generic template-style headings into stable lexicon entries.
- Added active orientation files for `02-Intake/`, `02-Intake/Quarterly/`, and `05-Assets/`.
- Updated `02-Intake/Index/Knowledge-Feed-Intake-Register.md` to include the May 16 Gemini/promotions intake and the current weekly project-update anchor.
- Renamed the rough duplicate April 22 satellite note in `03-Working/Knowledge-Space-Semiotics/Step-1-Polished-Notes/` to make its archive-variant status explicit.
- Promoted the first Part IV manuscript seed: `04-Book/Part-04-Futures/2026-05-16-staged-observation-and-agentic-visual-mediation-chapter-seed.md`.
- Updated `04-Book/README.md` and `04-Book/Part-04-Futures/README.md` so the Futures lane is described as active rather than empty.

Key rules (canonical):
- Preserve provenance-rich lanes such as `Journal Notes/` and `April 2026 Archive/`; route out of them instead of flattening them.
- Use `.github/copilot-instructions.md` plus `.github/instructions/` as the active workspace rule layer.
- Use `08-Admin/Instructions/agent.md` as the detailed operating supplement and keep its weekly anchor current.
