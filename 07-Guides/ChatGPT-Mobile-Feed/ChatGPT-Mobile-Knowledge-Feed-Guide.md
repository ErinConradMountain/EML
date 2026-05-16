# ChatGPT Mobile Knowledge Feed Guide

Purpose: explain how phone-based capture, ChatGPT project knowledge, and the local EML folders work together.

## Why This Exists

The phone is the fastest capture surface. The EML folder is the stable knowledge space. ChatGPT sits between them as a digestion layer. This guide prevents mobile fragments from becoming scattered by giving every capture a return path.

## The Five-Part Loop

1. Capture on cell.
2. Preserve the raw phrase or image description.
3. Ask ChatGPT for a structured EML return packet.
4. Route the packet into the project.
5. Return one question to handwriting.

## What to Paste into ChatGPT

Use `09-ChatGPT-Knowledge-Feed/01-ChatGPT-Project-Knowledge/Current-EML-Project-Knowledge.md` as the active project knowledge file.

For a single mobile note, paste the note plus this request:

```text
Process this as an EML mobile capture. Preserve my phrasing. Return a faithful summary, 3-5 tags mapped to Book Part and EML Layer, the likely Learning Journal Cycle step, a proposed save location, and one question to take back into handwriting.
```

## Routing After ChatGPT Responds

- Save the response as a return packet in `09-ChatGPT-Knowledge-Feed/02-Return-Packets/`.
- If it is about the Read-Write Model, add or update a note in `03-Working/Read-Write-Model/`.
- If it is stable terminology, update `06-Lexicon/`.
- If it suggests a visual, create a diagram brief in `05-Assets/Diagrams/`.
- If it has book-ready prose, route it to the correct `04-Book/Part-*` folder.

## Quality Standard

A good mobile capture should not become polished too quickly. It should remain alive enough to return to handwriting.
