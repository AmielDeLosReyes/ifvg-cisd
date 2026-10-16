# Task: write one chapter of the "ICT Playbook"

You are writing one chapter of a study book on ICT (The Inner Circle Trader, Michael J. Huddleston) concepts. The book is built only from study notes taken on 215 of his YouTube videos: the 2022 Mentorship (41 episodes, the core model), the 2024 Mentorship (51 long lectures) and the 2026 Smart Money Concept lectures (141 videos, newest teaching). The notes for your chapter are already collected in one source file (path given in your assignment).

## The reader
A retail trader who already uses FVGs and inversion FVGs, trades gold (XAUUSD, as a CFD) and NQ/MNQ futures on a prop-firm evaluation, charts in TradingView, and wants to **truly understand** the framework: what each concept is, why ICT says it works, how to spot it, how to trade it, and how not to misread it. Write so that someone reading carefully, with a chart open, would come away able to apply the idea. Where a rule depends on the instrument (futures sessions, settlement, opening gaps, handles, contract specs), say what ICT taught it on and how it maps to gold/CFDs if ICT said so, otherwise say plainly that he taught it for index futures.

## What to read first
1. Your chapter's source file, **completely** (Read it in slices of ~250 lines with offset/limit; check `wc -l` first). Do not skim or grep instead of reading.
2. /home/claude/ict/chapters.json — the full chapter list, so you can cross-reference ("see Chapter 9") instead of re-teaching another chapter's topic. Teach your own topic in depth; give other chapters' topics one line and a pointer.
3. The diagram rules and the template below.

## What to produce (two kinds of files)
1. `/home/claude/ict/book/<chXX>.md` — the chapter text in Markdown.
2. One file per diagram: `/home/claude/ict/book/<chXX>_d<N>.jsx` (N = 1, 2, 3…), each holding exactly one diagram module (rules below).

If `/home/claude/ict/book/<chXX>.md` already exists, a previous writer was interrupted: read it, keep the finished sections (fix anything that contradicts the sources), and continue from where it stops; also write any diagram files its placeholders reference that don't exist yet.

Build the chapter in stages: write the outline and first sections with Write, then append the rest (Bash `cat >> file << 'EOF'`) section by section. Do not try to emit the whole chapter in one tool call.

## Chapter markdown format
- Do NOT start with a `#` title (the tab already has it). Start with the lead.
- Allowed: `##` and `###` headings, paragraphs, `-` bullets, `1.` numbered lists (sub-points indented 4 spaces), pipe tables, **bold**, *italic*, `[text](url)` links. No HTML, no images, no code fences, no emoji, no `####`.
- Diagram placement: put a line on its own, exactly like
  `[[DIAGRAM chXX_d1 | caption: what the picture shows, short | One sentence telling the reader what to notice.]]`
  where the picture belongs (usually right after the definition it illustrates). The publisher replaces it with the drawing.
- Timestamp links: `[2022 Ep 6 · 12:34](https://youtu.be/<ID>?t=<seconds>)`, `[2024 #13 · 1:02:05](https://youtu.be/<ID>?t=3725)`, `[2026 #96 · 7:15](...)`. Take IDs and seconds from the source notes (they contain ready links). Never invent a timestamp.

## Chapter structure
1. **Lead** (2–3 sentences, no heading): the chapter's point — what the concept family is and what you will be able to do after reading.
2. `## At a glance` — one diagram of the core idea + 4–6 bullets: the rules in one breath.
3. One `##` section per concept, ordered from foundational to advanced. Inside each, use these `###` subsections where they apply (skip any that would be empty or padding):
   - `### What it is` — plain-English definition, then ICT's precise definition (candle-by-candle when relevant).
   - `### Why it works` — the logic ICT gives (algorithmic delivery, liquidity, efficiency, time). Attribute it: "ICT's explanation is…".
   - `### How to spot it` — a numbered checklist.
   - `### How to trade it` — entry, stop, target, management, filters, timeframes and times of day, as he states them.
   - `### Worked example` — a real example from the notes: instrument, date, timeframe, session, levels, step by step, with its timestamp link. Prefer a diagram for it.
   - `### Mistakes and look-alikes` — common misreadings, how it differs from similar concepts (e.g. FVG vs volume imbalance vs BPR vs iFVG).
   - `### How the teaching changed` — 2022 → 2024 → 2026: refinements, renamings, contradictions. When he contradicts himself, state both versions with their sources; do not silently pick one. If nothing changed, skip.
   - `### Watch it` — 2–4 timestamp links to the best moments where he teaches it.
4. `## Rules and numbers` — a pipe table: `| Rule | Detail | Source |` with every explicit number, time (ET), threshold and must/never rule in the chapter, each with a timestamp link in Source.
5. `## Check yourself` — 6–10 numbered questions that test understanding (scenarios, "what's wrong with this", "which level would he use"), not trivia.
6. `## Answers` — numbered answers with one-line reasons and the section to reread.

Target length: 4,000–7,000 words (up to ~9,000 for the biggest topics). Depth beats breadth: a concept ICT teaches heavily gets a full treatment; a passing remark gets a sentence or is left out.

## Style
- Plain, direct, specific. Sentences under ~25 words, paragraphs ≤ 4 sentences. Numbers with units (handles, points, pips, ET times).
- Teach, don't summarise videos: never "In episode 6 ICT says…" as the structure. Organise by concept; cite videos only as evidence.
- Explain jargon the first time it appears in the chapter (one clause), and point to the chapter where it's taught.
- No hype, no investment advice. You are explaining ICT's method as he teaches it; where his claims are statistical ("70% of the time"), present them as his claims.

## Accuracy and copyright (strict)
- Use only what the source notes say. Do not add ICT concepts from your own memory, even if you know them. If you think something important is missing from the notes, leave it out.
- Never invent prices, dates, times, percentages or timestamps. Items flagged "(caption unclear)" in the notes: use only if the meaning is clear from context, and keep the hedge; otherwise omit.
- Paraphrase. At most one short direct quote (under 15 words, in quotation marks) per concept, and only when the wording itself is the lesson.
- Before finishing, re-read your chapter file against the sources and fix any number, time or rule that doesn't match.

## Diagrams (2–5 per chapter)
Each diagram is a module that a validator checks strictly, then renders as SVG in a doc column ~672 px wide. Draw what the reader most needs to see: candle-by-candle anatomy of a pattern, a level grid, a timeline of a session, a decision flow. Use real example levels from the notes when the caption says it's a real example; otherwise use clean illustrative prices and say "illustrative" in the caption.

Start from this validated template (it renders correctly), copy its conventions, and change the content:
/home/claude/ict/book/TEMPLATE_candles.jsx
For box-and-arrow flows, see example ex.1 in /home/claude/ict/DOC_DIAGRAM_GUIDE.md (read that whole file once; it is the authoritative rule set).

Hard rules (the validator refuses the module otherwise):
- The file holds ONE line: `export default () => { …consts…; return <svg viewBox='0 0 760 H' role='img' aria-label='<title words>' fontSize='13'>…</svg>; };`
- Single quotes for JSX attribute strings; template literals with backticks are allowed inside `{}`.
- EVERY `<text>` you type has its own literal `data-claude-text-id='unique-slug'` and literal words. Never put a `<text>` inside `.map()` and never compute its words or id. Two lines = two separate `<text>` elements (or two `<tspan data-claude-text-id=…>` with no id on the parent).
- Shapes (candles, lines, rects) MAY be generated with `.map()`; give each mapped element `key={i}`.
- Data as objects with named fields (`{o: 150, h: 156, l: 140, c: 144}`), read as `k.o`. No computed indexing `xs[i]` / `pos[k]` (use `.at(i)` or named fields).
- Never use the identifiers `top`, `parent`, `self`, `window` (even as local names). Use `y0`, `rowA`, etc.
- Group each part in `<g data-claude-anchor='literal-slug'>`.
- Colours only via tokens: text `var(--cds-text-primary)` / `var(--cds-text-secondary)`; lines/borders `var(--cds-chart-axis)`; grid `var(--cds-chart-grid)`; up candles `var(--cds-chart-status-good)`; down candles `var(--cds-chart-status-critical)`; zones/accents `var(--cds-chart-categorical-1)` (more hues: `-categorical-2`…`-8`) with `fillOpacity='0.12'`; warning `var(--cds-chart-status-warning)`. No hex, no named colours. Every `<text>` sets `fill`.
- No `<style>`, `<use>`, `<foreignObject>`. fontSize ≥ 10.5 (13 for body labels, 11.5 for notes, 15/600 for the title).
- Width 760; every label inside the frame with ≥ 24 units clear on the right; set H to the drawing's height + ~24. Estimate text widths (13px ≈ 7 units/char, 11.5px ≈ 6.2 units/char, 13/600 ≈ 7.4) and make sure labels don't overlap candles, zones or each other.
- The first `<text>` is the title and states the finding ("Price returns to the gap's midpoint before expanding"), not the topic.
- Every word in a diagram must be supported by the notes.

## When you finish
Reply with only: the chapter file path, word count (`wc -w`), the list of `##` sections, and the diagram files with one-line captions. Under 200 words.
