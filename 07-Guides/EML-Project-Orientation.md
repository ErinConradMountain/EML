# EML Project Orientation and Workflow Guide

Purpose: keep bearings by explaining how this folder is structured, how weekly work flows through it, and how external ChatGPT work connects to the handwritten notes.

## What This Project Is
EML (Educational Modelling Language) is a book and system that models learning as relationships across time, not just content. The project uses weekly handwritten work as the primary input, then runs it through a defined cycle to produce readings, diagrams, circuits, and book drafts.

## Folder Map and What Each Area Does
- `00-Inbox/` - drop zone for new scans, photos, and raw transcripts before cleanup.
- `01-Source/` - cleaned source material (handwritten, transcripts, rough notes, reference).
- `02-Intake/` - weekly bundles that capture the learning cycle and the week's synthesis.
- `03-Working/` - step outputs (Steps 1-7), field journal, and intermediate drafts.
- `03-Working/Read-Write-Model/` - focused study of inscription, AI projection, re-entry, revision, and drift control.
- `03-Working/Knowledge-Space-Semiotics/` - focused study of knowledge-space terrain, semiotics, colour grammar, markers, and perspective.
- `04-Book/` - draft chapters and part-level manuscript sections.
- `05-Assets/` - diagrams, circuits, readings, templates, visual language assets.
- `06-Lexicon/` - definitions, terms, and phrases that stabilize the project vocabulary.
- `07-Guides/` - workflow and writing guides (this file lives here).
- `08-Admin/` - plans, instructions, history, indices, and change logs.
- `09-ChatGPT-Knowledge-Feed/` - mobile/ChatGPT capture, portable project knowledge, return packets, routing queue, and promotion receipts.

Reference the full directory map in `EML-Folder-Structure.md` when you need the canonical layout.

## The Weekly Cycle (How Work Moves)
1. **Capture**: collect handwritten pages or transcripts into `00-Inbox/`.
2. **Source cleanup**: move cleaned material into `01-Source/`.
3. **Weekly intake**: create or open the weekly folder in `02-Intake/Weekly/YYYY-WW/`.
4. **Run the Learning Journal Cycle** (Steps 1-7) in `03-Working/`.
5. **Distill**: make a one-page synthesis, tag by Book Part and EML layer, note assets.
6. **Extract assets**: promote readings/diagrams/circuits into `05-Assets/`.
7. **Feed the book**: update `04-Book/Part-*/` drafts and outline notes.
8. **Lexicon growth**: add terms/definitions to `06-Lexicon/`.
9. **Return loop**: update the ChatGPT/mobile knowledge feed when project rules, terms, or current focus change.

Use the full weekly template in `05-Assets/Templates/Weekly-Intake-Template.md` to keep all steps in one place.

## How ChatGPT Connects to the Folder
External chat work is not separate from the folder. It is an extension of the weekly intake process.

**Core linkages**
- The active workspace instruction layer is `.github/copilot-instructions.md` plus `.github/instructions/`; `08-Admin/Instructions/agent.md` is the detailed operating supplement.
- Custom instructions for the ChatGPT project live in `08-Admin/Instructions/Journal-Reading-ChatGPT-Custom-Instructions-2026-01-26.md`.
- The current portable knowledge file for ChatGPT/mobile work lives in `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md`.
- The weekly operating knowledge is stored in `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md`.
- The authoritative process rules are in `08-Admin/Plans/EML-Book-Plan-2026.md` and `08-Admin/Instructions/agent.md`.

**Workflow in chat**
1. Paste the custom instructions into the ChatGPT project when you start a session.
2. Attach or reference the current weekly knowledge file so the model uses the right context.
3. Provide handwritten images/transcripts as inputs.
4. Request the correct step output (Step 1, Step 2, etc).
5. Save outputs into the correct folders in `03-Working/` and promote assets to `05-Assets/`.
6. Update the weekly intake template with tags, key ideas, and the bridge checklist.
7. If the output came from mobile capture, save or reference it through `09-ChatGPT-Knowledge-Feed/02-Return-Packets/` before promoting it.

## Intake-Digestion-Redistribution Architecture
- **Intake**: WhatsApp or other low-friction capture channels act as membranes for raw fragments.
- **Digestion**: AI summarizes, sorts, and returns fragments into structured outputs.
- **Redistribution**: cleaned outputs feed notebooks, readings, diagrams, and book drafts.

This is the structural response to fragmentation. It keeps the notebook generative and centralizes digestion before any branch-level work.

## Weekend Ingestion Layer
Weekends are not for acceleration. They are a protected ingestion phase:
- shift from production to listening, rereading, and low-pressure capture
- condense keywords and scaffolds before the next cycle

This is documented in `05-Assets/Readings/Weekend-Ingestion-Layer.md`.

## File Naming and Stability
- Use `YYYY-MM-DD` for dated notes and `YYYY-WW` for weekly bundles.
- Keep filenames stable once cited in drafts.
- Prefer short, descriptive prefixes (example: `2026-01-26-weekly-knowledge.md`).

## How to Keep Bearings
If you feel lost, start here in order:
1. `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md` (weekly knowledge)
2. `05-Assets/Templates/Weekly-Intake-Template.md` (what to fill this week)
3. `08-Admin/Plans/EML-Book-Plan-2026.md` (why the cycle exists)
4. `08-Admin/Instructions/agent.md` (how to write and tag)
5. `01-Source/Reference/What is EML.txt` (definition and vision)

## Where Outputs Belong (Quick Map)
- Step outputs: `03-Working/Step-1-Polished-Notes/` through `03-Working/Step-7-Cast-Ahead/`
- Readings: `05-Assets/Readings/`
- Diagrams and circuits: `05-Assets/Diagrams/` and `05-Assets/Circuits/`
- Book drafts: `04-Book/Part-*/`
- Lexicon: `06-Lexicon/Definitions/`, `06-Lexicon/Terms/`, `06-Lexicon/Phrases/`
- Read-Write Model study: `03-Working/Read-Write-Model/`
- Knowledge Space / Semiotics study: `03-Working/Knowledge-Space-Semiotics/`
- ChatGPT/mobile feed: `09-ChatGPT-Knowledge-Feed/`

## Change Tracking
When instructions or workflows change, append a dated entry to:
- `08-Admin/Instructions/EML-Project-Instructions-History.md`

This is how the project retains memory across cycles.
