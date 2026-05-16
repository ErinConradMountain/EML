# EML Folder Structure

Purpose: keep handwritten inputs, weekly intake, and book outputs aligned with the four-part vision.

## Intake flow (handwritten-first)

1) Drop new scans/photos/transcripts into `00-Inbox/Weekly-Collection/`.
2) Move cleaned sources into `01-Source/Handwritten/` and `01-Source/Transcripts/`.
3) Create a weekly folder in `02-Intake/Weekly/` (use `YYYY-WW` or `YYYY-MM-DD`) and store:
   - Weekly intake file
   - Step outputs used that week
   - 1-page synthesis
   - 3-5 tags
4) Promote outputs:
   - Step outputs live in `03-Working/Step-*`
   - Drafts and chapters live in `04-Book/Part-*`
   - Diagrams, circuits, and readings live in `05-Assets/`
5) Capture new terms and definitions in `06-Lexicon/`.
6) Use `07-Guides/` for writing help and fine-tuning.

## Directory map

- `00-Inbox/` - drop zone for new weekly material before processing.
  - `Weekly-Collection/` - primary intake bin for weekly files.
  - `Handwritten-Scans/` - raw scans or photos.
  - `Transcripts/` - raw OCR or typing before cleanup.
- `01-Source/` - curated, cleaned sources.
  - `Handwritten/`, `Transcripts/`, `Rough-Notes/`, `Reference/`.
- `02-Intake/` - weekly and periodic intake bundles.
  - `Weekly/`, `Monthly/`, `Quarterly/`, `Index/`.
- `03-Working/` - Learning Journal Cycle outputs by step.
- `03-Working/Step-0-Temporal-Casting/` - input-only scaffold runs around a dated Page 0 (past/future pages used to situate writing in a plausible daily sequence).
- `03-Working/Step-7-Cast-Ahead/` - forward-only 5-day projections based on the current discussion.
- `03-Working/Read-Write-Model/` - focused studies, source maps, diagram briefs, and chapter seeds for the Read-Write Model.
- `03-Working/Knowledge-Space-Semiotics/` - focused studies for visual grammar, page navigation, marker systems, colour logic, perspective, and semiotics.
- `04-Book/` - book parts and chapter drafts.
- `05-Assets/` - diagrams, circuits, templates, short readings.
- `06-Lexicon/` - terms, phrases, definitions.
- `07-Guides/` - writing help, fine-tuning, intake guidance.
- `08-Admin/` - plans, instructions, change logs, indices.
- `08-Admin/Skills/` - project-local skill files for recurring EML workflows.
- `09-ChatGPT-Knowledge-Feed/` - portable project knowledge, mobile capture templates, ChatGPT return packets, routing queue, and promotion receipts.
  - `00-Mobile-Capture/` - raw phone-originated notes, voice summaries, image descriptions, and quick fragments.
  - `01-ChatGPT-Project-Knowledge/` - portable knowledge files for Erin's ChatGPT project.
  - `02-Return-Packets/` - structured outputs returning from ChatGPT.
  - `03-Routing-Queue/` - return packets waiting for classification.
  - `04-Promoted-To-EML/` - receipts for material absorbed into the main project.

## Instruction Authority

- `.github/copilot-instructions.md` plus `.github/instructions/` are the active workspace instruction layer.
- `08-Admin/Instructions/agent.md` is the detailed operating supplement for the repo.
- Other files in `08-Admin/Instructions/` remain useful as project memory, external coordination material, or dated reference sets.

## Preserved Legacy Lanes

- `Journal Notes/` remains a valid source lane because active indices and source maps already cite it.
- `April 2026 Archive/` remains a preserved archive root because its routed Markdown copies point back to the original archive paths.

## Naming conventions

- Use `YYYY-MM-DD` for dated notes and `YYYY-WW` for weekly folders.
- Prefix with short descriptors, e.g., `2026-01-19-weekly-intake.md`.
- Keep filenames stable once cited in drafts.

## Current placement (as of 2026-02-01)

- `08-Admin/Plans/EML-Book-Plan-2026.md`
- `08-Admin/Instructions/EML-Project-Instructions-History.md`
- `08-Admin/Instructions/agent.md`
- `05-Assets/Templates/Weekly-Intake-Template.md`
- `02-Intake/Weekly/2026-W03/EML-Weekly-Intake-2026-01-19-Week01.md`
- `02-Intake/Weekly/2026-W03/Weekly-Intake-2026-01-17.md`
- `02-Intake/Weekly/2026-W04/EML-Weekly-Knowledge-2026-01-26.md`
- `03-Working/EML-Field-Journal-2026-01-17.md`
- `03-Working/Step-1-Polished-Notes/` (Jan 26 - Feb 1 outputs)
- `03-Working/Step-2-Analytical-Study/` (Jan 26 - Feb 1 outputs)
- `03-Working/Step-3-Essays/` (Jan 26 - Feb 1 outputs)
- `03-Working/Step-7-Cast-Ahead/`
- `01-Source/Rough-Notes/rough-notes-journal.txt`
- `01-Source/Reference/What is EML.txt`
- `05-Assets/Readings/2026-01-26-supports-return.md`
- `05-Assets/Readings/2026-01-30-knowing-is-not-possession-but-occupation.md`
- `05-Assets/Readings/2026-01-28-comparative-study-orientation-grammar.md`

## Current additions (as of 2026-05-02)

- `AGENTS.md` - project-level agent guide.
- `00-Inbox/Archive-Extracts/README.md` - extraction route for future compressed archives.
- `03-Working/Read-Write-Model/README.md`
- `03-Working/Read-Write-Model/2026-04-read-write-model-study-index.md`
- `06-Lexicon/Definitions/Read-Write-Model.md`
- `05-Assets/Diagrams/2026-05-02-read-write-model-loop-diagram-brief.md`
- `08-Admin/Indices/Read-Write-Model-Source-Map.md`
- `08-Admin/Skills/Read-Write-Model.skill.md`
- `08-Admin/Skills/ChatGPT-Mobile-Knowledge-Feed.skill.md`
- `08-Admin/Skills/Knowledge-Space-Semiotics.skill.md`
- `09-ChatGPT-Knowledge-Feed/README.md`
- `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md`

## April 2026 archive integration (as of 2026-05-02)

- `02-Intake/Monthly/2026-04/April-2026-Integration-Map.md`
- `08-Admin/Indices/April-2026-Archive-Import-Manifest.md`
- `03-Working/Knowledge-Space-Semiotics/README.md`
- `03-Working/Knowledge-Space-Semiotics/2026-04-knowledge-space-semiotics-index.md`
- `05-Assets/Visual-Language/2026-05-02-colour-as-functional-grammar.md`
- `05-Assets/Diagrams/2026-05-02-page-as-navigation-system-diagram-brief.md`
- `09-ChatGPT-Knowledge-Feed/04-Promoted-To-EML/2026-05-02-promotion-receipt-april-archive.md`

## Current status (as of 2026-05-16)

- `03-Working/Read-Write-Model/Step-2-Analytical-Study/` and `03-Working/Knowledge-Space-Semiotics/Step-2-Analytical-Study/` now match the main Learning Journal naming.
- Root-level stray intake items were folded back into `00-Inbox/`.
- The current weekly knowledge anchor is `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md`.
- The portable ChatGPT knowledge anchor remains `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md`.
