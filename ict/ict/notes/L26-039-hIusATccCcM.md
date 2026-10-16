# L26-039 — Case Study With NonFarm Payroll & NQ Futures August 07, 2026
ID: hIusATccCcM · URL: https://www.youtube.com/watch?v=hIusATccCcM · Duration: 57:47
Content type: case study + live trade | Teaching density: high

## Summary
ICT demonstrates a complete non-farm payroll day trading case study on NQ, starting with pre-market range definition (7–9 AM before the 8:30 NFP release), predicting the post-NFP rally direction, placing a long entry at the beginning of the macro time window (8:50–9:10 AM), taking a partial at the 0.5 Fibonacci midpoint, and managing through a two-stage delivery (initial rally, then drop back into the range, then final break higher). The video teaches range definition, balanced price ranges, standard deviations, octants, and how major economic events create predictable algorithmic responses.

## Concepts

### Pre-Market Range Definition Before High-Impact News
- **Kind:** rule + example
- **What ICT says:** Before a major economic release (NFP at 8:30 ET, CPI, PPI, FOMC, etc.), you must establish the pre-release range (7:00–8:30 AM). Identify the highest high and lowest low during that 90-minute window. This range is the "dealing range" where price was willing to trade before the news. Once the news hits, price will typically break out of that range, so knowing the range boundaries allows you to anticipate the direction and magnitude of the move.
- **How to identify:** Chart the 1-minute from 7:00 to 8:30 ET; mark the highest candle high and lowest candle low.
- **How to use:** Breakout direction. If price breaks above the range, expect continuation higher. If below, continuation lower. Use range boundaries as support/resistance even after the news.
- **Example in this video:** NQ 7:00–8:30 pre-market range = [high, low]. High-impact NFP at 8:30 ET. Price subsequently breaks well above that range, rallying toward the 29,780 level ICT called for. The range high becomes a support zone on any pullback.
- **Timestamps:** [0:01:36](https://youtu.be/hIusATccCcM?t=96) — defining importance of pre-NFP range; [0:02:24](https://youtu.ye/hIusATccCcM?t=144) — measuring high/low of the range; [0:03:12](https://youtu.ye/hIusATccCcM?t=192) — anticipating breakout direction
- **Nuance / caveats / changes:** Do not trade the range itself expecting containment once NFP is released; the range breaks almost every time.

### Buy-Side Imbalance / Sell-Side Inefficiency (BSI/SSI)
- **Kind:** definition + rule + example
- **What ICT says:** (Refresher, but contextualized) When price trades down from a high into a low, there's an unfilled space (gap) if the move is fast. That gap is a buy-side imbalance (buyers moved price higher) + sell-side inefficiency (gap was not filled at every price level). Later, price will be drawn to fill some of this gap or use it as a support zone. Multiple BSI/SSI structures can appear in the pre-market range, each representing potential entry zones for a post-news move.
- **How to identify:** Look for gaps or unfilled spaces in the 7:00–8:30 pre-market range.
- **How to use:** Entry zones. When price trades into a BSI/SSI after the news, it's a valid long or short setup depending on direction.
- **Example in this video:** NQ pre-market shows multiple BSI/SSI gaps. Once NFP is released and price rallies, it trades back down into these BSI zones, offering pullback entry opportunities for longs.
- **Timestamps:** [0:03:59](https://youtu.ye/hIusATccCcM?t=239) — describing BSI/SSI in pre-market context; [0:04:47](https://youtu.ye/hIusATccCcM?t=287) — trading into BSI after NFP
- **Nuance / caveats / changes:** BSI/SSI become more significant in event-driven contexts because price needs to know where to retrace during consolidations within the larger trend.

### Balanced Price Range (BPR)
- **Kind:** definition + example
- **What ICT says:** A balanced price range is when two PD arrays (a buy-side imbalance + a sell-side imbalance, or vice versa) share the same high-low span. The highest high of both and the lowest low of both define a larger BPR. When price trades into a BPR, it's a zone of equilibrium where both sides of the order book are balanced; price tends to respect these levels repeatedly.
- **How to identify:** (1) Find a BSI (gap up, unfilled below), (2) Find an SSI (gap down, unfilled above), (3) If they span the same range, they're balanced. Mark the combined high/low.
- **How to use:** Support/resistance and turning points. Price respects BPR boundaries; use them for stops, partials, and bias confirmation.
- **Example in this video:** Two gaps (one up, one down) share the same high-low range. That combined range is the BPR. Price hits this BPR multiple times during the post-NFP consolidation, using it as a pivot zone. When bodies fail to breach BPR, a reversal is likely.
- **Timestamps:** [0:06:21](https://youtu.ye/hIusATccCcM?t=381) — defining BPR; [0:10:21](https://youtu.ye/hIusATccCcM?t=621) — BPR as support in the trade
- **Nuance / caveats / changes:** BPR is more complex than a single level but very reliable once identified.

### Octants and Standard Deviations
- **Kind:** definition + rule
- **What ICT says:** Divide the pre-NFP range into 8 equal parts (octants: upper quadrant, upper percentile, upper octant, midpoint/CE, lower octant, lower percentile, lower quadrant, below). Standard deviations of the range (±2.0 SD, ±1.0 SD, etc.) can align with these octants. When price reaches +2.0 or beyond, it's extended; expect potential reversal at macro times.
- **How to identify:** (1) Measure the range high/low, (2) Divide by 8 or apply SD formula, (3) Mark each octant.
- **How to use:** Reversal confirmation. If price reaches upper octant during a macro time, expect pullback. Octants also qualify PD arrays; if a gap sits at an octant, it's more significant.
- **Example in this video:** Pre-NFP range octants are marked. After NFP, price rallies beyond +2.0 SD during the macro window (8:50–9:10), confirming a turning point. Bodies fail to close above the +2.0 SD octant, signaling weakness.
- **Timestamps:** [0:08:42](https://youtu.ye/hIusATccCcM?t=522) — calculating standard deviations of the range; [0:09:33](https://youtu.ye/hIusATccCcM?t=573) — showing +2.0 SD reaching during macro; [0:10:21](https://youtu.ye/hIusATccCcM?t=621) — octants and PD array qualification
- **Nuance / caveats / changes:** Standard deviations require precise calculation; an off-by-one error invalidates the levels.

### Macro Time Window and Two-Stage Delivery
- **Kind:** rule + example
- **What ICT says:** Major economic events (NFP, FOMC, CPI) follow a two-stage delivery pattern: (1) initial reaction rally (or selloff) in one direction, often reaching extended levels (SD ±2.0+), (2) pullback and reversal, wiping out weak stops from the initial move. The macro time window (typically 8:50–9:10 AM for NFP) is when the turn is most likely. Stops from the initial move get run during the second stage.
- **How to identify:** Watch the initial 5–15 minute move post-event; if it extends into macro time (8:50–9:10), expect reversal in that window.
- **How to use:** Profit-taking and reversal entry. Take partials off at the turning point (macro time). Place reverse orders (shorts if initially long) just inside the previous support/resistance, anticipating the second-stage pullback.
- **Example in this video:** NFP at 8:30 ET. Rally from 8:30 to 8:50 (initial move). At 8:50 (start of macro window), ICT tweeted to take longs off. The market then dipped, hit the BPR, stopped out longs with tight stops, then resumed higher (two stages).
- **Timestamps:** [0:05:35](https://youtu.ye/hIusATccCcM?t=335) — warning to take profits at macro time; [0:06:21](https://youtu.ye/hIusATccCcM?t=381) — second-stage pullback confirming the pattern; [0:10:21](https://youtu.ye/hIusATccCcM?t=621) — completing the two-stage narrative
- **Nuance / caveats / changes:** Two-stage delivery is a pattern, not a guarantee; occasionally, one-stage rallies occur without pullback. Always have a stop.

### Institutional Order Flow Entry Drill (IOFED)
- **Kind:** observation + technique
- **What ICT says:** When a PD array (gap, order block, etc.) is "qualified" by sitting at a key octant or standard deviation, price trades into it as the institution are entering orders at that level. This is called an order flow entry drill: the market sweeps into a gap/level, and institutions add to their positions, creating a bounce or reversal. Watching for these drills helps time scalp entries.
- **How to identify:** (1) Mark key gaps/order blocks on your chart, (2) Note which octant they're at, (3) Watch if price trades into that gap on a pullback—that's the IOFED.
- **Example in this video:** Multiple PD arrays in the NQ trade are "qualified because [they sit at an octant]." When price trades into these qualified arrays, ICT knows it's an IOFED and manages the trade accordingly.
- **Timestamps:** [0:11:10](https://youtu.ye/hIusATccCcM?t=670) — describing IOFED; [0:11:56](https://youtu.ye/hIusATccCcM?t=716) — price trades into qualified PDA, executes IOFED
- **Nuance / caveats / changes:** Not all IOFEDs work; sometimes price breaks through the drill. Have a stop in case.

### Partial Taking Strategy at Fibonacci 0.5
- **Kind:** rule + example
- **What ICT says:** In an event-driven trade like NFP, don't hold the full position to the ultimate target. Take the first partial at the 0.5 Fibonacci midpoint between entry and a known target/resistance. This locks in a "halfway" profit and reduces risk on the runner.
- **How to identify:** Mark entry and a nearby resistance/target; measure 0.5 between them.
- **How to use:** Partial exit. At 0.5, close 25–50% of the position. Leave the rest to run.
- **Example in this video:** Long entry near the 29,780 level (after initial drop into the BSI zones). 0.5 Fibonacci midpoint between 29,780 entry and the pre-NFP range high = X price. ICT takes one contract off at X. The other contract continues to the macro high before being stopped out or exited.
- **Timestamps:** [0:07:55](https://youtu.ye/hIusATccCcM?t=475) — calculating 0.5 and exiting partial; [0:08:42](https://youtu.ye/hIusATccCcM?t=522) — confirming exit near midpoint
- **Nuance / caveats / changes:** The exact 0.5 is an ideal; a few ticks off is acceptable.

### Pre-NFP Risk Warning and Trading Suitability
- **Kind:** warning + rule
- **What ICT says:** New traders should NOT trade Thursday–Friday (last two days of week 1 of the month) because of high impact news and volatility. NFP Friday is especially challenging. Only experienced traders should participate. Even experienced traders must adjust position sizing and stop placements for event risk.
- **How to identify:** Mark first week of each month (especially Thursday–Friday) as high-danger trading days on your calendar.
- **How to use:** Risk management. Either avoid these days entirely or use micro contracts and tight stops only.
- **Example in this video:** ICT emphasizes upfront: "never really try to participate on Thursday and Friday" for new traders. He then shows his demo trade (not real money) to show how to manage it *if* you must trade NFP. This is honest warning.
- **Timestamps:** [0:00:00](https://youtu.be/hIusATccCcM?t=0) — opening warning; [0:07:09](https://youtu.ye/hIusATccCcM?t=429) — disclosure that trade is on demo account
- **Nuance / caveats / changes:** ICT is emphatic: if you're brand new, skip these days.

## Rules, checklists & numbers stated
- **Pre-NFP range (7:00–8:30 ET):** Identify and mark highest high, lowest low.
- **NFP release at 8:30 ET:** High-impact event; expect breakout of pre-NFP range.
- **Macro time window 8:50–9:10 ET:** Likely turning point; take partials here.
- **Two-stage delivery:** Initial move + pullback in reverse direction. First-stage stops get run in second stage.
- **Standard deviations ±2.0+:** Extended; expect reversal.
- **Octants:** 8 divisions of the range; PD arrays qualified when sitting at an octant.
- **Balanced price range:** Shared high-low of a BSI + SSI pair; acts as multi-touch support/resistance.
- **Partial at 0.5 Fibonacci:** Between entry and first target, take 25–50% off.
- **Demo trading on NFP:** Only experienced traders or paper trading; never gamble real money if new.

## Process, risk & psychology
- **Advance planning:** ICT tweeted his 29,780 target on Wednesday; he had the level pre-calculated before NFP Friday. This is preparation, not guessing.
- **Phone execution:** He took a screenshot while driving to drop his son off, set a screen recording on his home computer, and was ready to enter remotely on his phone if the setup triggered. This is logistical commitment to planned setups.
- **Demo account transparency:** He discloses upfront that this is a paper trade, not real money. This is integrity.
- **Partial discipline:** Despite the setup working perfectly, he doesn't get greedy. Takes one contract off at 0.5, trails the rest. Avoids the pitfall of holding too long into event risk.
- **Birthday milestone:** He mentions turning 54 tomorrow. This is a human touch—he's not infallible, just disciplined.
- **Summary statement:** "All in all, it's a nice little exercise this morning of prediction."—understated but confident. The setup worked; he executed; he's satisfied.

## Glossary candidates
`Pre-NFP range` — the highest high and lowest low traded between 7:00–8:30 ET (before the 8:30 non-farm payroll release). Establishes the "dealing range" before event impact; price typically breaks this range after 8:30.

`Two-stage delivery` — a pattern in major economic event reactions where price rallies/sells off in one direction (stage 1), extends into a macro time window, then reverses sharply (stage 2) to run stops from stage 1. Typical for NFP, FOMC, CPI.

`Balanced price range (BPR)` — a zone where a buy-side imbalance and a sell-side imbalance share the same high-low range, creating a zone of equilibrium. Price respects BPR boundaries repeatedly.

`Octant` — one of eight equal divisions of a price range, from high to low (upper quadrant, upper percentile, upper octant, CE, lower octant, lower percentile, lower quadrant, sub-low). Octants qualify PD arrays.

`Institutional order flow entry drill (IOFED)` — when price trades into a PD array (gap, order block) that is qualified by an octant or SD level, institutions are executing entry orders at that level. Expect a bounce or reversal.

`Standard deviation (SD)` — a statistical measure of how far price has extended from the range. ±1.0 SD is normal; ±2.0 SD is extended and likely reversal zone.

`Macro time window` — a specific time window (e.g., 8:50–9:10 ET for NFP) when algorithmic reversals or momentum shifts are historically likely. Often coincides with second-stage delivery of event reactions.
