# L26-070 — Missed Entry How To Navigate The Same Trade Idea
ID: EZB4vBUFdHw · URL: https://www.youtube.com/watch?v=EZB4vBUFdHw · Duration: 19:12
Content type: live trade (a live short on NQ-like prices around 29,9xx; narrated; date not stated, "holiday volume" is mentioned)
Teaching density: medium-high (the specific lesson is how to handle a limit order that misses by a hair and how to keep the same idea alive with a fallback entry and strict no-re-entry rules)

## Summary
ICT plans a short: sell on a limit just above the consequent encroachment (CE) of a fair value gap, stop above the gap's volume imbalance, "let it come to you, don't chase." Price trades into the gap but only to within about two handles of his level and his limit order is not filled ("sometimes perfection and being so precise is a curse"). He then keeps the same idea by selling inside the lower half of the bearish order block once the change in the state of delivery appears, uses a rejection block to reduce the stop risk, and manages with partials into relatively equal lows and the "event horizon." The video teaches the missed-entry protocol: don't chase, don't re-enter after exiting, accept missed trades because demanding perfect fills yields them, and use a pre-defined fallback inside the same PD array. It also labels the day as a Market Maker Sell Model with second-stage redistribution after a 9:30 Judas run, and notes holiday volume.

## Concepts

### Limit order just above the CE; "let it come to you"  (aliases ICT uses: sell limit above consequent encroachment, don't chase, needless drawdown)
- **Kind:** rule (execution)
- **What ICT says:**
  - He plans to sell short with a limit just above the consequent encroachment of the fair value gap; stop above the gap's volume imbalance.
  - "Let it come to you. Don't chase it." It is real important not to think you must have the fill, "even if you know it's likely to go down and take out that low." If you sell lower down and it retraces, that is "needless drawdown. You don't have to endure that."
  - He also rejects the use of market replay in demonstrations.
- **How to use:** place the limit at the level (just above the CE for a short), stop beyond the volume imbalance, wait; never chase price lower.
- **Example in this video:** NQ-like 1m chart (prices near 30,1xx / 29,9xx; caption digits partial): short limit just above the FVG CE; price pops into it and then comes up to the wick that prints to a candle's open; the limit is just short of a fill.
- **Timestamps:** [0:00:00](https://youtu.be/EZB4vBUFdHw?t=0) — plan: sell on limit just above CE, stop above the volume imbalance; [0:00:48](https://youtu.be/EZB4vBUFdHw?t=48) — don't chase, needless drawdown; [0:02:28](https://youtu.be/EZB4vBUFdHw?t=148) — price pops up toward the level
- **Nuance / caveats / changes:** Same concept as "limit orders" in earlier teaching; here the lesson is the cost of missing.

### Perfect analysis yields missed trades; fallback entry in the lower half of the order block  (aliases ICT uses: missed entry, "perfection will yield missed trades", premium sensitivity, immediate rebalance)
- **Kind:** rule / entry refinement
- **What ICT says:**
  - His limit at the level did not fill: the candle's low was 120.5 and the high 122.5 (partial digits), so price went into the gap and two handles beyond but missed his price. "Sometimes perfection and being so precise is a curse." He asks nobody to feel bad: "It is what it is."
  - "When your analysis is perfect, your executions could not execute. So perfection will yield missed trades. That's the oxymoron." You demand the best-case scenario and the spread/fills do not always afford it.
  - Fallback: sell inside the lower half of the (bearish) order block on a confirmed change in the state of delivery - the "premium sensitivity" portion of that candle. "Notice my entries in the lower half of the order block on this fill." Required signs: change in state of delivery occurs; "no immediate rebalance" (price does not immediately fill/retrace the gap after displacement = strength).
  - A close below the wick's CE is "confirmation that follow-through is likely"; he measures it with a fib; it needed to happen on that candle.
  - He has "something to work with": with a rejection block he reduces his stop risk.
- **How to identify:** (1) a defined limit price; (2) a candle that comes within a few handles but doesn't fill; (3) a bearish OB that confirms with CISD.
- **How to use:** if the limit misses by a small distance and the OB confirms, enter in its lower half (below its CE); tighten the stop using the rejection block; targets: relatively equal lows (best case), then nearer lows.
- **Example in this video:** NQ 1m: limit fails by ~2 handles; CISD at the OB; he sells in the lower half; price delivers hard ("institutional delivery, hammered it"), then retraces back to the OB.
- **Timestamps:** [0:03:18](https://youtu.be/EZB4vBUFdHw?t=198) — "perfection is a curse"; limit short of fill; CISD, short if it touches; [0:04:09](https://youtu.be/EZB4vBUFdHw?t=249) — went two handles beyond; use a rejection block to reduce stop risk; [0:05:54](https://youtu.be/EZB4vBUFdHw?t=354) — entries in the lower half of the OB; close below the wick CE = follow-through; [0:16:26](https://youtu.be/EZB4vBUFdHw?t=986) — perfection yields missed trades
- **Nuance / caveats / changes:** The caption conflates "discount sensitivity" and "premium sensitivity"; he means the premium (sell) side sensitivity of the bearish OB, i.e., the lower half entry still being valid because price stays below the OB's midpoint.

### Bearish order block retest = smart money accumulating more shorts  (aliases ICT uses: order block to sell side, implemented order block)
- **Kind:** refinement
- **What ICT says:** "Whenever there's an order block being implemented and it starts to sell off, and then it goes right back to it again, it's allowing smart money to accumulate more shorts" (bearish OB). So the return to the OB is another opportunity to add short; price then takes out the low, accelerates below it, and continues lower. The model: "order block to sell side," not requiring a precise re-use of the block.
- **How to use:** add shorts on the first pullback into the OB while bodies hold below its midpoint; stop just above the OB/high.
- **Timestamps:** [0:05:54](https://youtu.be/EZB4vBUFdHw?t=354) — order block to sell side as a model; [0:06:40](https://youtu.be/EZB4vBUFdHw?t=400) — return to the OB lets smart money accumulate more shorts; [0:07:29](https://youtu.be/EZB4vBUFdHw?t=449) — stop lowered just above the high
- **Nuance / caveats / changes:** Same pyramiding idea as L26-049 ("add on retraces into a validated OB").

### Partials to relatively equal lows and event horizon; scaling out contracts  (aliases ICT uses: best-case scenario, event horizon, runner)
- **Kind:** management / example
- **What ICT says:**
  - Best-case target: the relatively equal lows; then this low and that low as intermediate targets; if the low is taken he'll "limit out" three contracts.
  - First partial: three contracts off, "leave six contracts for a runner." He holds risk "at 1920" (caption; probably dollars) until the first partial.
  - Later, as price nears an old low and "event horizon" (midpoint between the old low and the next low, ballparked), he takes single contracts off from the remaining three just above the event horizon since the old low sits just below; the platform lagged and executions registered late.
  - He ends the trade "content": "Too much of a retracement on my part for the trade I was in."
- **How to use:** stagger partials: first three off at the first target, then singles into event horizon, runner for the relatively equal lows; lower the stop progressively.
- **Example in this video:** NQ-like 1m: short; three off; six runner; ~"29,965" is the "hottest nightclub" level; price falls toward ~29,230 area (caption), he exits before the equal lows.
- **Timestamps:** [0:04:58](https://youtu.be/EZB4vBUFdHw?t=298) — relatively equal lows as best case; [0:07:29](https://youtu.be/EZB4vBUFdHw?t=449) — three off, six runner; [0:10:46](https://youtu.be/EZB4vBUFdHw?t=646) — event horizon partial plan; [0:12:24](https://youtu.be/EZB4vBUFdHw?t=744) — partial just above event horizon, old low just below
- **Nuance / caveats / changes:** The "nightclub" analogy is only a story to describe a level at 29,965 (price magnet).

### Wick that fails to close below its CE as a warning; Market Maker Sell Model with second-stage redistribution  (aliases ICT uses: MMSM, Judas, smart money reversal, first-stage distribution, second-stage redistribution, warning sign)
- **Kind:** refinement / model label
- **What ICT says:**
  - He labels the day a Market Maker Sell Model: the 9:30 run up was Judas, the drop followed, and he used "the second stage redistribution." Sequence he lists: smart money reversal (low-risk short), first-stage distribution, second-stage redistribution; you look for key highs to get short "on the right side of the curve" (the sell side of the curve from the highest point down).
  - The earlier drop wick did not close below its CE: that is "a warning sign" - "real order flow is in jeopardy if you're looking for it to go lower"; "if it's dropping down it's going to make a run for buy side." He says other mentors hide this wick use but will copy it.
  - A tight block of bodies (a "big square area") would be disrupted, cleared through, then used; equilibrium of the block drops down, a gap forms.
- **How to use:** after a drop where the wick fails to close below its CE, take profit sooner or expect a rally to the buy side; label the stages for context.
- **Timestamps:** [0:14:03](https://youtu.be/EZB4vBUFdHw?t=843) — MMSM, second-stage redistribution, Judas from 9:30; [0:14:50](https://youtu.be/EZB4vBUFdHw?t=890) — failure to close below the wick CE = warning sign; [0:15:38](https://youtu.be/EZB4vBUFdHw?t=938) — block of price action disrupted
- **Nuance / caveats / changes:** The block-of-bodies passage is hard to read from captions (caption unclear). Related: the 9:30 run itself was a "hype" move from the employment numbers (ICT's words).

### No re-entry after you are out; rules over regret  (aliases ICT uses: "there has to be rules", leave some for everybody else)
- **Kind:** rule (psychology/process)
- **What ICT says:** After the exit he refuses to re-enter even if price drops into the 29,230 area: "I can't do it. There has to be rules." You looked for the key high to get short at the right side of the curve; if you aren't in at that location, you don't chase lower. He won't be able to stay with it to the relatively equal lows "and that's okay... if I take it all, it's just greedy."
- **How to use:** define a no-chase/no-re-entry rule before the trade: once the planned entry zone has passed and you've exited, stop.
- **Timestamps:** [0:17:13](https://youtu.be/EZB4vBUFdHw?t=1033) — I can't re-enter; there have to be rules; [0:18:00](https://youtu.be/EZB4vBUFdHw?t=1080) — leave some for everybody else
- **Nuance / caveats / changes:** Complements "let it come to you" at the start.

## Rules, checklists & numbers stated
- Short plan: limit just above the CE of the FVG; stop above the volume imbalance; don't chase.
- If the limit misses by a few handles: use the lower half of the bearish order block after CISD; require "no immediate rebalance"; reduce stop risk with a rejection block.
- Close below the wick's CE = follow-through likely; failing to close below = warning sign that price may run to the buy side.
- Bearish OB pullback = chance to add shorts.
- Take 3 contracts off first; remaining runners; partials just above event horizon.
- Do not re-enter after exiting; no market replay.
- Levels (caption digits): level 29,965 ("965 club"); lower area ~29,230; candle low 120.5 / high 122.5 (partial digits); risk "1920" (likely dollars).
- Holiday volume: "things can get squirrely."

## Process, risk & psychology
- Missing a fill is acceptable; perfection yields missed trades; demanding perfection costs trades ([0:16:26](https://youtu.be/EZB4vBUFdHw?t=986)).
- Don't chase; extra drawdown is needless ([0:00:48](https://youtu.be/EZB4vBUFdHw?t=48)).
- Be content with what you got; don't be greedy ([0:13:14](https://youtu.be/EZB4vBUFdHw?t=794), [0:18:00](https://youtu.be/EZB4vBUFdHw?t=1080)).
- Never use market replay in teaching; show live executions ([0:08:20](https://youtu.be/EZB4vBUFdHw?t=500), [0:18:46](https://youtu.be/EZB4vBUFdHw?t=1126)).
- Platform lag and slow fills are a real execution risk ([0:13:14](https://youtu.be/EZB4vBUFdHw?t=794)).
- Skip political asides about employment data; the lesson is that the 9:30 run was hype driven by news ([0:06:40](https://youtu.be/EZB4vBUFdHw?t=400)).

## Glossary candidates
`MISSED ENTRY` — a planned limit that price misses by a small distance; handled with a fallback entry or by passing.
`IMMEDIATE REBALANCE` — price quickly returning to fill a just-created gap; its absence signals strength.
`REJECTION BLOCK (STOP USE)` — using the wick/body zone to tighten stop risk.
`RIGHT SIDE OF THE CURVE` — entering at the key high/low where the move begins rather than lower in the move.
`SECOND-STAGE REDISTRIBUTION` — the continuation stage of a market maker sell model after the first distribution.
