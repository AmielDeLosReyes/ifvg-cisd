# Task: turn ICT video transcripts into precise study notes

You are helping build a study book ("playbook") of ICT (The Inner Circle Trader, Michael J. Huddleston) trading concepts from his YouTube lectures. The reader is a retail trader who already knows basic FVGs/iFVGs and wants to *truly understand* the full framework. Your notes are the raw material the book will be written from, so precision matters more than polish.

Transcripts are YouTube auto-captions: expect mis-hearings. Fix obvious ones silently using ICT vocabulary (e.g. "fair value gap", "order block", "SIBI", "BISI", "NWOG", "NDOG", "SMT", "CISD", "IPDA", "OTE", "PD array", "killzone", "Judas swing", "consequent encroachment", "displacement", "Silver Bullet", "macro", "draw on liquidity", "buy side / sell side liquidity", "market maker buy/sell model", "RTH", "opening range gap", "NQ", "ES", "YM", "DXY", "EURUSD"). If a term is ambiguous, write it as you best understand it and add "(caption unclear)".

Each transcript file has a header (title, playlist, video ID, URL) and paragraphs that start with a timestamp `[h:mm:ss]`. A timestamp link is `https://youtu.be/<ID>?t=<seconds>` (convert h:mm:ss to seconds).

## What to do

Read EVERY assigned transcript IN FULL with the Read tool. Each line is ~45 seconds of speech (~600–900 characters), so read in slices of 60 lines (offset 1, 61, 121, …) until you reach the end — do not skim, sample, grep, or stop early. Check the line count first with `wc -l`. Write each video's notes file as soon as you finish reading that video, before starting the next one. Then, for EACH video, write one notes file to:

`/home/claude/ict/notes/<same base name as the transcript>.md`

ICT often teaches a concept for only a minute in the middle of a long market review. Catch those moments — they are the most valuable part.

## Notes file format (Markdown)

```
# <CODE-NUM> — <video title>
ID: <id> · URL: https://www.youtube.com/watch?v=<id> · Duration: <dur>
Content type: lecture | market review | live trade | Q&A/mindset | mixed
Teaching density: high | medium | low   (how much transferable concept teaching vs. narration of price)

## Summary
3–6 sentences: what this video teaches and why it matters.

## Concepts
### <Canonical concept name>  (aliases ICT uses: ...)
- **Kind:** definition | rule | entry model | refinement | example only | new coinage
- **What ICT says:** precise paraphrase. Keep every number, time (ET), timeframe, percentage, candle count, condition, and "must / never / only" rule. Several bullets are fine.
- **How to identify:** criteria / checklist as he states them.
- **How to use:** entry, stop placement, targets, management, filters.
- **Example in this video:** instrument, date, timeframe, session, and what price did step by step — described so someone could draw it as a diagram (e.g. "NQ 1m, 9:50 ET: price runs 9:30 high (BSL), displaces down leaving 3-candle SIBI 18450–18438, retraces into it at 10:02, delivers to 18390 SSL").
- **Timestamps:** [h:mm:ss](https://youtu.be/<ID>?t=<sec>) — what happens at that moment. Give 1–4 key ones.
- **Nuance / caveats / changes:** anything that refines, contradicts, or updates earlier teaching (say what it contradicts if you know).

(repeat for every concept taught or meaningfully applied — typically 3–15 per lecture, fewer for short reviews)

## Rules, checklists & numbers stated
Bullet list of explicit rules ("only trade X when Y"), times (e.g. "8:50–9:10 macro"), parameters.

## Process, risk & psychology
His advice on risk, position sizing, journaling, backtesting, trade management, mindset (paraphrased, with timestamps).

## Glossary candidates
`TERM` — one-line meaning as used here (only ICT-specific jargon).
```

## Canonical concept names (use these when they match; add new ones when ICT coins a term)

Market structure: Swing high/low · Short/intermediate/long-term high/low · Market Structure Shift (MSS) · Break of Structure · Displacement · Change in State of Delivery (CISD)
Liquidity: Buy-side liquidity (BSL) · Sell-side liquidity (SSL) · Equal highs/lows (relative equal) · Old highs/lows · Liquidity sweep / raid / stop run · Draw on liquidity (DOL) · Internal vs external range liquidity (IRL/ERL) · Liquidity voids
PD arrays: Fair Value Gap (FVG; BISI/SIBI) · Inversion FVG (iFVG) · Implied FVG · Balanced Price Range (BPR) · Volume imbalance · Consequent encroachment (CE) · Order block · Breaker block · Mitigation block · Rejection block · Propulsion block · Vacuum block · Opening gaps (NWOG / NDOG / RTH opening range gap) · PD array matrix · Premium / discount / equilibrium · Dealing range · Optimal Trade Entry (OTE) / Fibonacci levels
Time: Killzones (Asian, London, NY AM, NY PM) · Midnight open · 8:30 open · 9:30 RTH open · Macros (algorithmic time windows) · Silver Bullet · Daily/weekly profiles · Day of week tendencies · Power of 3 / AMD · Judas swing · Opening range · Lunch
Bias & context: Daily bias · Higher-timeframe narrative · SMT divergence · Intermarket (DXY, bonds) · IPDA data ranges (20/40/60 days) · Quarterly shifts · Seasonal tendencies · News drivers (NFP, CPI, FOMC)
Models: 2022 Mentorship model · Market Maker Buy/Sell Model (MMBM/MMSM) · Seek & destroy days · High/low resistance liquidity run conditions · Turtle soup · One Shot One Kill · Any named model (Reaper, Enigma, Obsidian, Zircon, Terminus, Chain of custody, Grey pools, Hangman, Reflection FVG, Time & price grids, etc.)
Execution: Entries & stops · Targets & partials · Trade management · Missed entries · Limit orders · Tape reading · Micro vs mini / futures vs CFDs · Risk management · Journaling & backtesting · Psychology

## Rules
- Paraphrase; do not copy long passages. At most one short quote (under 15 words) per concept, only when the exact wording is itself the lesson.
- Never invent prices, dates or rules not in the transcript. If you're unsure, say so.
- Skip chit-chat, greetings, livestream housekeeping, and personal stories unless they carry a trading lesson.
- If a video has no captions or no trading content, still write a short notes file saying so.
- When finished, reply with ONLY: the list of notes files written, and for each, a one-line summary + the top concept names. Keep that reply under 300 words total.
