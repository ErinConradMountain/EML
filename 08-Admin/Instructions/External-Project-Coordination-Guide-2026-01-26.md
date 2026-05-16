# External Project Coordination Guide (EML Book System)

Purpose: give the external side of the project a clear view of roles, processes, and how this repository works so both sides stay aligned while working with handwritten notes and ChatGPT outputs.

## What This Side of the Project Does
This repository is the **core EML book workspace**. It stores the authoritative structure, workflows, and outputs that transform handwritten notes into book-ready assets. The system is designed to:
- turn handwritten fragments into structured, tagged writing
- preserve the author's voice and evolving lexicon
- produce diagrams, circuits, and readings that feed the book
- maintain a stable, repeatable weekly cycle

## Roles and Responsibilities
**EML Journal Reading assistant (ChatGPT role)**
- Digests handwritten notes into clear, tagged outputs.
- Runs the Learning Journal Cycle (Steps 1-7), one step per response unless asked otherwise.
- Uses the weekly knowledge file to keep context aligned.
- Tags outputs with Book Part and EML layers.
- Suggests file placement for every output so it lands in the correct folder.

**Human author**
- Provides handwritten notes, context, and direction.
- Chooses which steps to run and which topics to deepen.
- Updates weekly intake and decides what moves into the book.

**External side of the project**
- Holds or hosts the ChatGPT project configuration and conversation context.
- Ensures outputs are returned here for filing, tagging, and integration.
- Coordinates schedules (e.g., weekend ingestion mode) with this repository.

## Core System Loop (How the Two Sides Connect)
1. Handwritten notes are captured and shared with the ChatGPT assistant.
2. ChatGPT produces Step outputs (1-7) according to the Learning Journal Cycle.
3. Outputs are saved back into this repository under `03-Working/` and related folders.
4. Key ideas, diagrams, readings, and lexicon entries are promoted into `05-Assets/` and `06-Lexicon/`.
5. Weekly intake files in `02-Intake/Weekly/` are updated to keep the record complete.
6. The book plan and drafts in `04-Book/` are refreshed as new material stabilises.

## Weekly Operating Knowledge (Context Handshake)
The external side should always reference the current weekly knowledge file:
- `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md`

Use the portable ChatGPT knowledge file alongside it when working from mobile or a ChatGPT project:
- `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md`

Together these files provide the current cycle anchor and the portable project frame.
If the external project uses a different filename or location, record it here so both sides stay aligned:
- External weekly knowledge file: [INSERT PATH OR NAME]

## Process Rules to Preserve Alignment
- Always work from the weekly template: `05-Assets/Templates/Weekly-Intake-Template.md`.
- Treat fragmentation as structural; centralise digestion before branching outputs.
- Preserve the author's voice and distinctive phrases; avoid smoothing into generic prose.
- Respect weekend ingestion mode (listening and condensation, not acceleration).
- Keep any ChatGPT Project custom instructions under 8000 characters; trim before pasting if needed.
- Tag every Step 2-7 output with Book Part and EML layer(s).
- End file-ready outputs with a proposed save location so they can be filed quickly.

## Where Outputs Land (Repository Side)
- Step outputs: `03-Working/Step-1-Polished-Notes/` through `03-Working/Step-7-Cast-Ahead/`
- Readings: `05-Assets/Readings/`
- Diagrams and circuits: `05-Assets/Diagrams/` and `05-Assets/Circuits/`
- Book drafts: `04-Book/Part-*/`
- Lexicon entries: `06-Lexicon/Definitions/`, `06-Lexicon/Terms/`, `06-Lexicon/Phrases/`
- Weekly bundles: `02-Intake/Weekly/YYYY-WW/`

## Key Reference Files
- `08-Admin/Plans/EML-Book-Plan-2026.md` - master plan and Learning Journal Cycle.
- `.github/copilot-instructions.md` - active workspace rules and folder architecture.
- `08-Admin/Instructions/agent.md` - authoring rules and tone.
- `08-Admin/Instructions/Journal-Reading-ChatGPT-Custom-Instructions-2026-01-26.md` - paste-ready ChatGPT instructions.
- `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md` - portable project knowledge for ChatGPT/mobile work.
- `01-Source/Reference/What is EML.txt` - EML definition and book vision.

## Coordination Checklist (External Side)
- Use the current weekly knowledge file when prompting ChatGPT.
- Confirm the user wants Step 1, Step 2, etc. before generating each output.
- Ask for placement confirmation if a file path is uncertain.
- Return outputs to this repository promptly for filing and tagging.
- Log changes to instructions in `08-Admin/Instructions/EML-Project-Instructions-History.md`.

## Outcome
This system works when both sides share the same weekly knowledge and move outputs back into the repository. The external side provides context and prompts; this repository preserves structure, assets, and continuity. Together, the system builds the book through steady weekly cycles.
