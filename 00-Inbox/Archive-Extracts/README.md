# Archive Extracts

Purpose: staging area for files extracted from compressed archives before they are classified into the EML system.

## 2026-05-02 Check

No `.zip`, `.7z`, `.rar`, or compressed archive signatures were found in the project tree during this structure pass. The existing `00-Inbox/Weekly-Collection/2026-W04-Chat-Export/` appears to be an already extracted ChatGPT export, containing `chat.html`, `conversations.json`, and processed text outputs.

## Future Archive Flow

1. Put compressed exports in `00-Inbox/Weekly-Collection/` or this folder.
2. Extract into a dated subfolder: `YYYY-MM-DD-archive-name/`.
3. Keep original files intact.
4. Route extracted files:
   - raw chat exports -> `00-Inbox/Weekly-Collection/YYYY-WW-Chat-Export/`
   - cleaned source -> `01-Source/Transcripts/` or `01-Source/Rough-Notes/`
   - weekly synthesis -> `02-Intake/Weekly/YYYY-WW/`
   - Read-Write Model material -> `03-Working/Read-Write-Model/`
   - diagrams/circuits/readings -> `05-Assets/`
