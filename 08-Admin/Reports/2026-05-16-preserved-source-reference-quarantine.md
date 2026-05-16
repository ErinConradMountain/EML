# Preserved Source Reference Quarantine

**Created:** 2026-05-16  
**Purpose:** record historical reference drift that remains inside preserved raw exports and backup-heavy source files.

## Why This Exists

A small cluster of January 2026 references remains inside preserved raw-source lanes. These references are historical capture artifacts, not active routing guidance.

## Quarantined Source Lanes

| Source lane | Why preserved | Known drift |
| --- | --- | --- |
| `00-Inbox/Weekly-Collection/2026-W04-Chat-Export/` | Raw chat export with `chat.html` and `conversations.json` | Repeats old weekly knowledge and ChatGPT instruction paths from January 2026 |
| `Journal Notes/Journal-1st-april-2026-ORIGINAL-BACKUP.md` | Provenance-heavy backup source | Repeats January 2026 weekly and instruction references across embedded historical material |

## Active Rule

Do not edit preserved raw exports or backup aggregates just to modernize path references.

Instead:
- keep the source intact
- update active guidance files elsewhere in the repo
- use this report to mark the stale references as quarantined historical residue

## Current Active Anchors

- Weekly knowledge: `02-Intake/Weekly/2026-W20/EML-Project-Update-Conversation-Knowledge-Surface-2026-05-16.md`
- Portable knowledge: `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md`
- Active workspace rule layer: `.github/copilot-instructions.md` and `.github/instructions/`
- Detailed operating supplement: `08-Admin/Instructions/agent.md`

## Follow-Up

If another preserved source lane contains stale references, add it here rather than normalizing the raw file itself.
