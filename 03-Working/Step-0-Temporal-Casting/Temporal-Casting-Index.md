# Temporal Casting Index (Temporal Loom)

Purpose: a running index of all Temporal Loom casts produced and filed in this repository.

This index is meant to make casts auditable:
- What was cast?
- When?
- Where is the file?
- What was the handoff into Steps 1–3?

---

## Index

| Anchor date | Anchor item ID (weekly intake) | Cast file | Stored in weekly bundle? | Detected Page 0 Step | Notes / handoff target |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

---

## How to update
Add one row per cast run.

Guidance:
- **Anchor date** is the date found inside Page 0.
- **Anchor item ID** is the ID from the weekly intake file (section 1.1 Raw Items Index), if relevant.
- **Cast file** should point to `03-Working/Step-0-Temporal-Casting/Temporal-Casting-YYYY-MM-DD.md`.
- **Stored in weekly bundle?** is `Y`/`N`.
- **Detected Page 0 Step** must match the strict marker rules in the Temporal Loom instructions.
- **Notes / handoff target** is a short pointer like “Run Step 1 on Page 0 next” or “Use as Step 2 outline seed.”
