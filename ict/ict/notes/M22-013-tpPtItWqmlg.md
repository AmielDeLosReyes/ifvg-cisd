# M22-013 — 2022 ICT Mentorship Episode 13
ID: tpPtItWqmlg · URL: https://www.youtube.com/watch?v=tpPtItWqmlg · Duration: 46:52
Content type: mixed (trade recap of a demo/paper NQ micro trade + mindset)
Teaching density: medium

## Summary
An "extra" episode recorded on a Friday in early March 2022, the day after the advanced market-structure lesson (Ep. 12). ICT walks through a single demo (TradingView paper) long on Micro E-mini Nasdaq (MNQ), scaled in three times, to show the previous night's structure theory applied in a simplified form. The core teaching is his definition of a **high-probability bullish order block**: a down-close candle + an imbalance (FVG) created when price leaves it + a narrative of reaching for buy-side liquidity, and nothing else (no engulfing pattern). He also gives a concrete stop-trailing rule (stops stay below the low of the down-close candles supporting each leg, not inside them), the intermediate-term-low rule, a 9:30 opening "Judas" retracement idea, and a pyramiding rule (largest size first, smaller adds). The second half is mindset: demo for 6 months with a documented plan before live funds, set weekly/monthly goals (20%/month aim), one good trade a week is enough.

## Concepts

### Order block (high-probability bullish order block)  (aliases: bullish order block, down-closed candle, "higher time frame order block")
- **Kind:** definition / rule
- **What ICT says:**
  - In a bullish move, down-close candles should not be violated; they act as support. In a bearish move, up-close candles should not be breached.
  - A high-probability bullish order block = (1) the down-close candle, (2) an imbalance (fair value gap) left when price moves away from / above it, and (3) the underlying narrative that price is likely to go higher to reach buy-side liquidity. "That's it."
  - No engulfing-candle requirement — "forget all that, you don't need that."
  - An hourly down-close candle can be made up of two down-close candles on the 5-minute chart; consecutive down-close candles together are treated as one order block.
  - The "mean threshold" of the order block = the middle of the candle (body/range) — used as the line below which price should not trade once entered.
- **How to identify:** Down-close candle after (or during) a bullish run; price displaces away and leaves an FVG; higher-timeframe narrative points to a BSL target above (e.g. relative equal highs).
- **How to use:** Wait for price to trade back down into the down-close candle, ideally overlapping with the FVG, at a meaningful time (after the 9:30 equities open). Buy there; stop below the order block; target the buy stops above relative equal highs. A lower-timeframe order block + FVG nested inside a higher-timeframe order block gives the entry ("hierarchy higher time frame to a lower time frame").
- **Example in this video:** MNQ, 1-hour chart then 5m / 1m / 30-second, morning session of a Friday in early March 2022. After a run up, a down-close hourly candle formed; price rallied away leaving an imbalance. Relative equal highs above held buy stops, which he marked as roughly 14,110 (red line). After the 9:30 open, price retraced down into the hourly down-close candle (and its gap), in a discount of the low-to-high range (below 50%). On the 5m, price hit the order block, rallied, and traded back down into the gap between one candle's high and another's low, overlapping a lower-timeframe order block = his first long entry. Price went above the next down-close candle's high, retraced into an imbalance without eating through those down-close candles, he bought again; a third, shallower retracement only into an FVG (not back to the order block) was the final add. Price ran to the target above the relative equal highs.
- **Timestamps:** [0:12:51](https://youtu.be/tpPtItWqmlg?t=771) — rally leaves down-close candle; BSL above relative equal highs (~14,110). [0:13:39](https://youtu.be/tpPtItWqmlg?t=819) — rule: in bullish moves down-close candles should not be violated. [0:17:38](https://youtu.be/tpPtItWqmlg?t=1058) — definition: gap + down-close candle + BSL narrative, no engulfing. [0:20:00](https://youtu.be/tpPtItWqmlg?t=1200) — 5m order block + FVG overlap entry.
- **Nuance / caveats / changes:** Explicitly rejects the "engulfing candle" retail version of order blocks (and mocks a $7 order-block indicator). Simplified "public" language for the advanced structure taught in Ep. 12.

### Fair Value Gap (FVG) — entry inside the gap; shallow retracement near the objective  (aliases: imbalance, gap)
- **Kind:** rule / refinement
- **What ICT says:**
  - Retracements in a bullish leg go down into an imbalance "so smart money can buy again."
  - When price is close to the profit objective, the algorithm generally does not retrace all the way back into the order block to rebalance; it only makes a small retracement into the FVG — buy at that candle's low.
- **How to identify:** The gap between one candle's high and a later candle's low (3-candle FVG) left during the rally.
- **How to use:** Enter on the retracement into the FVG, especially when it overlaps an order block; near the target expect only a partial fill of the gap.
- **Example in this video:** Third add on MNQ: retracement didn't reach the order block, only dipped into the FVG, then ran to target.
- **Timestamps:** [0:22:24](https://youtu.be/tpPtItWqmlg?t=1344) — retracement into imbalance without breaking the down-close candles. [0:23:12](https://youtu.be/tpPtItWqmlg?t=1392) — "classic": small retracement inside the FVG near the objective.
- **Nuance / caveats / changes:** none stated.

### Intermediate-term low  (aliases: "intermediate term low")
- **Kind:** rule / example
- **What ICT says:** A low with a higher low to its left and a higher low to its right (a short-term low flanked by higher short-term lows) is an intermediate-term low. Once price fills the gap and starts rallying from it, that intermediate-term low should not be taken out until the objective is reached.
- **How to identify:** Swing low flanked on both sides by higher lows (short-term lows), forming at the retracement into the imbalance/order block.
- **How to use:** Its integrity confirms the bullish leg; the whole leg is trusted while it holds.
- **Example in this video:** MNQ hourly/5m: the retracement low into the hourly order block was the intermediate-term low; "should never be overtaken until the objective's reached."
- **Timestamps:** [0:16:01](https://youtu.be/tpPtItWqmlg?t=961) — higher low left and right = intermediate-term low. [0:21:35](https://youtu.be/tpPtItWqmlg?t=1295) — once the gap is filled it becomes an intermediate-term low that should not be taken out.
- **Nuance / caveats / changes:** He admits classifying short/intermediate/long-term highs is the hard part from Ep. 12 and that this simplified language is meant to sidestep it.

### Entries & stops — trailing stops below down-close candles
- **Kind:** rule
- **What ICT says:**
  - Initial stop below the middle (mean threshold) of the bullish order block candle.
  - When price trades above a new down-close candle's high, your stop must remain below that candle's low — not inside it — because price can "dig into" that candle (it acts as an order block). Putting the stop inside it gets you stopped prematurely.
  - Once price rallies and takes out (goes above) a cluster of down-close candles, the stop can be raised to below that down-close candle (cluster), treating the consecutive down-close candles as one order block.
  - If price breaks the low of those down-close candles, being stopped out was correct — the move may be failing.
- **How to identify / use:** Each new bullish leg has its supporting down-close candle(s); trail the stop below their lows.
- **Example in this video:** MNQ: two consecutive down-close candles; price got very close to them on a retracement but did not eat through their range; he held.
- **Timestamps:** [0:24:49](https://youtu.be/tpPtItWqmlg?t=1489) — stop below mean threshold; stop must stay below the candle's low. [0:25:37](https://youtu.be/tpPtItWqmlg?t=1537) — raise stop once the down-close candles are taken out.
- **Nuance / caveats / changes:** Getting stopped early often leaves beginners afraid to re-enter — he calls that "infancy."

### Judas swing / 9:30 opening retracement
- **Kind:** example / rule
- **What ICT says:** In a bullish context, price retracing lower into the 9:30 a.m. NY equities open is the "initial incorrect move" — like a Judas swing. Don't chase this down move, and don't chase price higher right before the 9:30 open either. The public reads the prior bounce area as resistance/support; the algorithm keeps pressing higher toward buy-side.
- **How to identify:** Bullish narrative + price dropping into the open into a discount PD array (order block/FVG).
- **How to use:** Time of day matters — he takes the opening price, extends it out in time, and wants the order-block retracement to occur after the 9:30 open; then look for the long.
- **Example in this video:** MNQ dropped after 9:30 into the hourly down-close candle/imbalance, below 50% of the range, then rallied.
- **Timestamps:** [0:15:14](https://youtu.be/tpPtItWqmlg?t=914) — time of day; opening price extended out. [0:18:24](https://youtu.be/tpPtItWqmlg?t=1104) — retracement after 9:30 = Judas-like fake move. [0:19:11](https://youtu.be/tpPtItWqmlg?t=1151) — checklist: discount, inside order block, equities open has happened, bullish.
- **Nuance / caveats / changes:** none.

### Premium / discount (discount entry)
- **Kind:** rule (applied)
- **What ICT says:** For a long, look for a discount of the low-to-high range — below 50%.
- **Example in this video:** MNQ entry was below 50% of the range and inside the order block.
- **Timestamps:** [0:19:11](https://youtu.be/tpPtItWqmlg?t=1151) — "I'm below 50, yes; I'm inside the order block, yes."

### Buy-side liquidity (BSL) at relative equal highs / draw on liquidity
- **Kind:** rule / example
- **What ICT says:** Relative equal highs look like "resistance / a ceiling" to retail traders; buy stops rest above them. The algorithm, unwilling to let price go lower, goes after profitable shorts' stops. The ideal exit for longs is where willing buyers (buy stops of shorts) are — when price trades above the level, buy stops become market buy orders, flooding liquidity so longs can sell at a higher price. Don't exit 6 or 10 points higher arbitrarily.
- **How to identify:** Two highs at roughly the same level; mark the level just above them.
- **How to use:** That level is the profit objective of the trade.
- **Example in this video:** MNQ, ~14,110 above the relative equal highs (red level).
- **Timestamps:** [0:12:51](https://youtu.be/tpPtItWqmlg?t=771) — "just going to call it 14,110." [0:16:49](https://youtu.be/tpPtItWqmlg?t=1009) — retail sees ceiling; price should go over. [0:20:49](https://youtu.be/tpPtItWqmlg?t=1249) — why exits sit at buy stops.

### Intermarket: index correlation (ES leading NQ)
- **Kind:** rule / example
- **What ICT says:** NQ and ES generally move in tandem. If ES has energy to the upside while NQ is lethargic, NQ tends to be drawn higher "in sympathy" — "all boats rise in a high tide."
- **Example in this video:** The morning of the trade, ES had a lot of upside energy; NQ lagged; he expected NQ to follow.
- **Timestamps:** [0:10:29](https://youtu.be/tpPtItWqmlg?t=629) — markets move in tandem.
- **Nuance / caveats / changes:** This is a "laggard catches up" use, not an SMT divergence signal.

### Higher-timeframe draw before a counter-trend move (bearish macro, bullish retracement target)
- **Kind:** example
- **What ICT says:** He is technically bearish on equities, but price already ran below the lows (his weekly objective), so he would not sell short. Instead he asks what price could reach up into: the open (or low) of a prior up-close candle and/or an FVG above, then could resume lower.
- **Timestamps:** [0:09:41](https://youtu.be/tpPtItWqmlg?t=581) — possible retracement targets above.

### Risk management — pyramiding (largest position first)
- **Kind:** rule
- **What ICT says:** Build the biggest position at the initial entry, then each add is smaller (3 micros, then 2, then 1) — a stable pyramid. Buying 1, then 2, then 3 is an "inverted pyramid" — unstable. The earlier, larger position's equity supports the adds so you can weather a deeper retracement. Adds only while price is still below the objective. He counts the whole thing as one trade.
- **Example in this video:** MNQ demo: 3 + 2 + 1 = 6 micro contracts; $10,000 hypothetical account → $12,111 (≈21% on one trade). 6 micros required about $1,200 margin (hypothetical AMP Futures discount broker). MNQ = $2 per point (4 ticks).
- **Timestamps:** [0:31:59](https://youtu.be/tpPtItWqmlg?t=1919) — pyramid: 3 then 2. [0:32:47](https://youtu.be/tpPtItWqmlg?t=1967) — inverted pyramid unstable. [0:33:34](https://youtu.be/tpPtItWqmlg?t=2014) — one trade, 3 scalings, $10,000 → $12,111. [0:34:21](https://youtu.be/tpPtItWqmlg?t=2061) — 6 micros ≈ $1,200 margin.
- **Nuance / caveats / changes:** Says this gearing was "optimal" for $10k; more would have been too much leverage. "Stop thinking you need a lot to make a lot."

### Micro vs mini futures
- **Kind:** example
- **What ICT says:** Micro E-mini Nasdaq: 1 point = 4 ticks = $2. Micros are enough to grow an account if you compound.
- **Timestamps:** [0:11:16](https://youtu.be/tpPtItWqmlg?t=676) — MNQ point value.

## Rules, checklists & numbers stated
- Bullish move: down-close candles should not be violated; bearish move: up-close candles should not be breached.
- High-probability bullish OB = down-close candle + imbalance/FVG leaving it + narrative toward BSL. No engulfing needed.
- Long checklist used: bullish narrative; price in discount (<50% of range); inside the order block; after the 9:30 ET equities open.
- Don't chase the drop into 9:30 or the rise right before 9:30.
- Intermediate-term low (higher lows each side) should not be taken out before the objective.
- Initial stop below the OB's mean threshold (middle of candle); trail stops below the low of the newest down-close candle(s) — never inside them.
- Near the objective, expect only a shallow FVG retracement, not a full return to the OB.
- Pyramid: 3 → 2 → 1 contracts; never 1 → 2 → 3.
- MNQ: $2/point; 6 micros ≈ $1,200 margin; demo result $10,000 → $12,111 (21%+) in one trade.
- Goal framing: aim for 20% per month (a goal, not a promise). Setups "absolutely form every single week" and often every day.
- Demo consistently for 6 months with a documented plan before considering live funds.

## Process, risk & psychology
- He won't trade live when his weekly/monthly objective is already hit and conditions (Ukraine, black-swan risk) are uncertain; he uses a demo to stay connected to the tape instead of risking his February gains. [0:07:15](https://youtu.be/tpPtItWqmlg?t=435)
- Weekly, daily and monthly objectives: he always has a target for each. People who say goals are stupid are "not profitable"; "if you don't aim for a target you're going to hit nothing." [0:37:29](https://youtu.be/tpPtItWqmlg?t=2249)
- 20% per month is a percentage goal — compounding matters, not account size. [0:02:27](https://youtu.be/tpPtItWqmlg?t=147)
- Readiness: refined model + documented trading plan (what you do / won't do, entry trigger, stop, risk, target, partials — all decided before entering) + six months of consistent demo results. He never tells students they're ready for live trading. [0:03:15](https://youtu.be/tpPtItWqmlg?t=195), [0:06:28](https://youtu.be/tpPtItWqmlg?t=388)
- If you feel butterflies/anxiety while in a trade, you're not ready; you must be indifferent to the outcome. [0:05:40](https://youtu.be/tpPtItWqmlg?t=340)
- His own failure: went live in 1992 after one book, no backtesting; lost 50% on the first trade; later took 60–70 trades a day out of control. [0:04:50](https://youtu.be/tpPtItWqmlg?t=290), [0:36:42](https://youtu.be/tpPtItWqmlg?t=2202)
- Beginners collapse profitable trades when an opposing candle forms — experience from months of watching ideas play out fixes this. [0:13:39](https://youtu.be/tpPtItWqmlg?t=819)
- One trade a week, then stop and go to demo — reduces overtrading. "Setups form every day" is not an invitation to trade every day. [0:35:09](https://youtu.be/tpPtItWqmlg?t=2109), [0:35:55](https://youtu.be/tpPtItWqmlg?t=2155)
- Six months of practice should let a YouTube student find one such trade per week consistently. [0:38:17](https://youtu.be/tpPtItWqmlg?t=2297)
- Study by going through price repeatedly (backtesting) — price teaches you; books only show handpicked examples. [0:44:37](https://youtu.be/tpPtItWqmlg?t=2677)
- Everyone takes losses; expect drawdowns. [0:43:50](https://youtu.be/tpPtItWqmlg?t=2630)

## Glossary candidates
`Mean threshold` — the midpoint of an order block candle; price should not close/trade beyond it once the OB is used.
`High-probability bullish order block` — down-close candle + FVG left on departure + BSL draw narrative.
`Intermediate-term low` — a low with higher (short-term) lows on both sides; must hold until the objective.
`Inverted pyramid` — adding larger size on each subsequent entry; ICT says it is unstable.
`Relative equal highs` — highs at roughly the same price, holding buy stops; retail treats them as resistance.
