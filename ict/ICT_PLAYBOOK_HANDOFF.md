# ICT Playbook: handoff and implementation plan

Status as of 2026-10-16. **Work is stopped.** About 80% of the book is done. The work is now in **Step 6 (writing the last chapters)** and **Step 7 (publishing them)**.

---

## 1. The original ask

The user gave three YouTube playlists of ICT (The Inner Circle Trader) videos:

- https://www.youtube.com/playlist?list=PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s (2022 ICT Mentorship, 41 videos)
- https://www.youtube.com/playlist?list=PLVgHx4Z63paaM41aubnHOmqfeNjSAoBCV (ICT 2024 Mentorship, 51 videos)
- https://www.youtube.com/playlist?list=PLVgHx4Z63paaja3GW0dYSr6y_V2Sttx4- (2026 ICT Smart Money Concept Lecture, 141 videos)

The ask: pull every transcript, then turn them into a digital study book ("playbook") that makes the reader truly understand ICT's concepts. It should have definitions, examples, visuals, and everything else that helps understanding.

Agreed design:

- **Diagrams instead of screenshots.** Clean drawn diagrams plus timestamp links to the exact moment in each video.
- **Per concept:**
  - a plain-English definition
  - why it works
  - a checklist for spotting it
  - how to trade it
  - a worked example
  - mistakes and look-alikes
  - how the teaching changed from 2022 to 2024 to 2026
  - "Watch it" links
- **Per chapter:** a rules-and-numbers table, a quiz, and an answer key.
- **Whole book:** a glossary and a one-page cheat sheet.
- **Format:** the book is a Claude Docs doc with one tab per chapter.
- **Reader:** trades XAUUSD (CFD) and NQ/MNQ futures on an Apex prop evaluation, uses TradingView, and already knows FVGs and iFVGs.

## 2. The deliverable (already exists)

**Claude Docs doc "ICT Playbook"**

- Link: https://claude.ai/code/artifact/10f57aa8-312b-4cbd-9373-150b0942d6c9
- doc id: `10f57aa8-312b-4cbd-9373-150b0942d6c9`

Tabs: Start here, Parts 1–6 (each with its chapters as sub-tabs), Glossary, Cheat sheet. Every tab id, body id and pending-block id is in `ict/docids.json`.

| Tab | Status |
|---|---|
| Start here | Partly done. Only the **Diagram key** section is filled. Pending blocks remain for: How to use this book (`mpje5a2t2rz.298`), The map diagram (`.299`), Learning path (`.301`), Sources (`.302`). |
| Ch 1–16, 18, 19 | **Published** (text + 4–5 diagrams each) |
| Ch 17 · The ICT models | Not published. Text is ~15k words, ending at "## The 2026 coinages". **Missing:** Rules and numbers, Check yourself, Answers. Diagrams d1–d5 are written. |
| Ch 20 · Risk, sizing and instruments | Not published. Partial: ~8.4k words, ends at "## Contract months, rollover and the continuous chart". **Missing:** the rest of the sections, Rules, Check yourself, Answers, and the diagram files ch20_d1–d4 (the placeholders exist). |
| Ch 21 · Practice | Not published. Text is complete. **Missing:** the diagram files ch21_d1–d4 (the placeholders exist). |
| Ch 22 · Psychology | **Not written.** |
| Glossary | Not started (pending `mpje5a2t2rz.9`) |
| Cheat sheet | Not started (pending `mpje5a2t2rz.12`) |

## 3. Pipeline steps

| # | Step | Status |
|---|---|---|
| 1 | Pull transcripts from YouTube through a browser (youtube.com was blocked from the cloud shell) | Done: 215/233 have captions. 18 have none: mostly silent trade videos, plus 2024 Lecture #14 (age-restricted, needs sign-in), #15, #34 and Grey Pools. |
| 2 | Turn each transcript into per-video concept notes (`ict/notes/*.md`, 216 files) | Done |
| 3 | Parse the notes into concept sections and bucket them into 22 chapter source files (`ict/sources/chXX.md`) | Done |
| 4 | Create the Docs skeleton (tabs and pending blocks) | Done |
| 5 | Write chapters 1–19 as Markdown plus diagram `.jsx` files (`ict/book/`) | Done except ch17's ending |
| **6** | **Write the rest: finish ch17, finish ch20, write the ch21 diagrams, write ch22** | **In progress (stopped here)** |
| **7** | **Publish ch17, ch20, ch21, ch22 into their tabs** | Not started |
| 8 | Glossary tab: build from the `glossary` pool in `ict/pools.json` plus the chapters | Not started |
| 9 | Cheat sheet tab: build from each chapter's "Rules and numbers" table | Not started |
| 10 | Start here: fill How to use, a Map diagram (how the concepts connect), Learning path, Sources (the 3 playlists and the 18 videos with no captions) | Not started |
| 11 | Final check: spot-check definitions and timestamps against the notes, confirm no `pending` blocks are left in any tab, then leave one comment for the user | Not started |

## 4. Files: everything is in `ict_playbook_workspace.zip`

The cloud workspace this ran in is private, so unzip the attached zip into the new session's working directory (it extracts to `ict/`).

| Path | What |
|---|---|
| `ict/transcripts/` | 233 transcript files (`M22-…`, `M24-…`, `L26-…`), with `[h:mm:ss]` timestamps |
| `ict/notes/` | Per-video concept notes |
| `ict/sources/chXX.md` | Source notes per chapter. **Read only these for writing.** |
| `ict/pools.json` | Process, rules, glossary and summary pools across all videos |
| `ict/chapters.json` | Chapter ids and titles |
| `ict/book/chXX.md`, `chXX_dN.jsx` | Chapter text and diagram modules |
| `ict/book/TEMPLATE_candles.jsx` | Validated candlestick diagram template |
| `ict/WRITE_PROMPT.md` | Full spec for writing a chapter: structure, style, accuracy and diagram rules |
| `ict/PUBLISH_PROMPT.md` | Exact procedure and API call shapes for publishing a chapter into its tab |
| `ict/DOC_GUIDE_FULL.txt`, `DOC_DIAGRAM_GUIDE.md` | Claude Docs API guide; the diagram validator rules are at lines 443–534 |
| `ict/docids.json` | Every tab, body and pending id |
| `ict/index.json` | Video index (playlist, number, id, title, duration, caption status) |

## 5. What to do next, in order

1. **ch17:** append `## Rules and numbers`, `## Check yourself` and `## Answers` to `book/ch17.md`, following `WRITE_PROMPT.md`. Use `sources/ch17.md` only to check facts.
2. **ch20:** read `book/ch20.md` and `sources/ch20.md`. Finish the remaining risk and instrument sections, add Rules, Check yourself and Answers, and write `ch20_d1`–`d4.jsx` to match their placeholders.
3. **ch21:** write `ch21_d1`–`d4.jsx` to match their placeholders. The text is already done.
4. **ch22:** write it fresh from `sources/ch22.md`, following `WRITE_PROMPT.md`.
5. **Publish** ch17, ch20, ch21 and ch22, each following `PUBLISH_PROMPT.md`:

| Chapter | FILE | BODY | PENDING |
|---|---|---|---|
| ch17 | `d637e37a-d492` | `7a40cc7c-cbef` | `mpje5a2t2rz.47` |
| ch20 | `b0fd21a6-e9c6` | `70d85ea6-ca8e` | `mpje5a2t2rz.42` |
| ch21 | `9aca6f7e-a391` | `00b13862-334c` | `mpje5a2t2rz.72` |
| ch22 | `d31e4ee5-84c1` | `cc84d757-b7a6` | `mpje5a2t2rz.49` |

   DOC = `10f57aa8-312b-4cbd-9373-150b0942d6c9`. Drop the literal `caption: ` prefix from placeholder captions when publishing.
6. **Glossary tab** (body `ebac8596-8ead`, pending `mpje5a2t2rz.9`): replace the pending block with an A–Z pipe table `| Term | Meaning | Chapter |`.
7. **Cheat sheet tab** (body `6adbe149-8645`, pending `mpje5a2t2rz.12`): one page with key times (ET), the opening-gap rules, FVG/iFVG/OB entry and stop rules, risk rules and the pre-trade checklist, taken from the chapters' Rules tables.
8. **Start here** (body `ebe308bd-5413`): fill pending blocks `.298`, `.299` (a concept-map diagram), `.301` and `.302`.
9. **Final check**, then tell the user it's done.

### Ways to keep usage low

- Use a mid-size model (Sonnet) for writing and a small model (Haiku) for publishing. Opus writers hit the weekly limit last time.
- Run 3–4 jobs at a time.
- Writers read only their `sources/chXX.md`. Publishers read only the chapter file plus the guide's relevant line ranges.
- Diagram rules that trip the validator:
  - every `<text>` needs a literal, unique `data-claude-text-id`
  - never put a `<text>` inside `.map()`
  - no `xs[i]` indexing
  - no identifiers named `top`, `parent`, `self` or `window`
  - colour tokens only
  - one line of code per diagram
