# M24-029 — ICT 2024 Mentorship \ How To Manage Missed Entries (September 17, 2024)
ID: fhBnnU44A6E · URL: https://www.youtube.com/watch?v=fhBnnU44A6E · Duration: 2:13:26
Content type: mixed (model lecture on the opening range gap + first FVG, then a long live market review of NQ on a paper account in which he never gets a trade he likes)
Teaching density: medium-high (the first ~1:15 contains a complete mechanical day-model; the rest is a frame-by-frame look at a choppy, one-sided late morning where he declines to trade)

## Summary
The announced topic is how to get into a move you missed (frozen, second-guessing, or late to the chart), but ICT's real answer is a complete, time-based model: on a day with an opening range gap of at least 40 handles, the gap's midpoint (CE) is the ~70% draw within the first 30 minutes, the first FVG to form after 9:31 is your entry mechanism toward it, and the stop goes above/below candle 2. He shows it on NQ (Dec contract) on 9/17/2024, the day before FOMC: short from a 9:33 FVG near 19,795, midpoint 19,728.25 delivered by 10:00. He also teaches that you can enter an already-started move by dropping to a lower time frame FVG, a no-bias "high frequency" drill off relative equal highs/lows on 15s/1m FVGs, SMT divergence read from candle bodies (NQ vs ES), "grey pools" (clustered wicks), breaker mean thresholds, a 20-handle minimum-range filter, and why a steady "buy program" is a place not to trade. The rest of the session is a live demonstration of patience and non-participation in a choppy pre-FOMC market.

## Concepts

### Opening range gap CE ("mid gap") — the 70% first-30-minutes draw and its size filter  (aliases: ORG midpoint, "consequent encroachment of the opening range gap", "70% strike rate")
- **Kind:** rule / model
- **What ICT says:**
  - Opening range gap = difference between yesterday's RTH settlement (last print at 4:14 PM ET; "settles at 4:15") and the first opening tick at 9:30 ET. The "opening range" is the 30-minute interval to 10:00.
  - Drop a Fibonacci from the previous settlement to the 9:30 open; the 50% level (CE) is the bias. About 70% of the time (not 100%, not a guarantee) price trades to the midpoint within the first 30 minutes (before 10:00).
  - Size filter: the gap should be more than 40 handles ("minimum 40"); larger is better; roughly 100 handles is a sweet spot; above about 200 handles he defers the setup because "heavy manipulation" means price may keep running.
  - If the gap is above price it makes the bias for the first 30 minutes down (premium gap -> expect a return to mid gap); mirror for a gap lower.
  - Combine with the economic calendar to improve the hit rate. A gap open above previous day's settlement is also described as a "premium" gap.
  - Expectation: one trade a week from this alone (~50 handles ≈ $1,000 on one mini, per ICT) would already be meaningful; "you have an experiment laboratory for 30 minutes every single day."
- **How to identify:** Check the gap size (settlement to 9:30 open) in handles, plot the 50% and the 25%/75% quadrants.
- **How to use:** Direction of the first FVG trade is set by where mid gap sits relative to price; target = mid gap (or partials en route, lower quadrant, etc.).
- **Example in this video:** NQ Dec contract, Tue 9/17/2024: previous settlement about 19,661.5, open about 19,795 (over 100 handles up, caption figures partly garbled), mid gap 19,728.25, lower quadrant about 19,694.5. Price sweeps Friday's high, forms a 9:33 FVG, trades down and delivers mid gap before 10:00 ("70% strike rate true today"), then lower quadrant 19,694.5 is the next objective. ICT says the gap-down mirror is to go long off the first FVG for mid gap.
- **Timestamps:** [0:13:39](https://youtu.be/fhBnnU44A6E?t=819) how the gap is defined (4:14/4:15 settlement to 9:30 open); [0:24:45](https://youtu.be/fhBnnU44A6E?t=1485) mid gap delivered; [0:33:04](https://youtu.be/fhBnnU44A6E?t=1984) "gap open higher more than 40 handles... 70% strike rate"; [0:52:29](https://youtu.be/fhBnnU44A6E?t=3149) larger gap = more opportunity; [1:09:21](https://youtu.be/fhBnnU44A6E?t=4161) 40 minimum / ~100 sweet spot / over 200 defer.
- **Nuance / caveats / changes:** Adds the explicit 40-handle minimum and 200-handle caution to the #28 teaching of the 70% rule. He says "50 handles" to mid gap although the quoted figures work out to roughly 67 handles; treat the numbers as approximate.

### First presented FVG after 9:31 as the entry mechanism to mid gap  (aliases: "first fair value gap", "first presented FVG", "ICT's blue ribbon recipe")
- **Kind:** entry model
- **What ICT says:**
  - Use the very first FVG that forms after the open (between 9:31 and 10:00). The earliest possible one has candle 2 at 9:31, because it cannot be built on the 9:30 candle as its middle candle (he corrected himself on this).
  - Trade it in the direction of mid gap. For a short from a premium gap: entry anywhere inside the gap, with candle 3's high (or one tick below it if you are aggressive) as the most direct level, with CE or the lower quadrant as other levels (all in the lower part of the gap); stop above candle 2's high. For longs, stop below candle 2's low.
  - Wicks above the gap ("Mohawk") do not invalidate the trade as long as the stop is above candle 2.
  - Stay in the trade until it is stopped out or reaches the target, as long as price stays beyond the stop and has not yet reached mid gap.
  - Time-based, mechanical, finite parameters: "every day at 9:00 ET you sit down and open NQ (or ES)..."; he first automated this kind of logic years ago in TradeStation EasyLanguage ("ATM with a pin code"), because the setup is rule-based.
  - Do not modify the recipe or rename it; the failure modes are over-leveraging, trading before the FVG is offered, not taking the trade because you haven't desensitized, and adding your own "horseradish."
- **How to identify:** First 3-candle imbalance after 9:31 on the 1m chart (also usable on 15s). Candle 2 = the displacement candle, candle 1 = prior, candle 3 = entry.
- **How to use:** Short entry near the lower edge of the bearish gap, stop above candle 2, target mid gap; then manage via partials (see next concept).
- **Example in this video:** NQ 1m 9/17/2024: the gap formed at 9:33 after a run to about 19,794–19,795; candle 3's high about 19,795; ICT's referenced entry is a limit near 19,794.75 (one tick below). Price spikes slightly above the gap (Mohawk) without taking out candle 2's high, then falls to mid gap 19,728.25 by 10:00.
- **Timestamps:** [0:29:50](https://youtu.be/fhBnnU44A6E?t=1790) first presented FVG and entry; [0:33:53](https://youtu.be/fhBnnU44A6E?t=2033) "first FVG that forms at 9:31, the earliest"; [0:36:17](https://youtu.be/fhBnnU44A6E?t=2177) stop above candle 2; [0:55:41](https://youtu.be/fhBnnU44A6E?t=3341) why it cannot be the 9:30 candle; [1:11:46](https://youtu.be/fhBnnU44A6E?t=4306) rules recap.
- **Nuance / caveats / changes:** Clarifies the 9:30-candle slip from #28. He pairs this with the 9:50–10:10 macro and the "10:00 hour Silver Bullet" idea but chose to wait.

### Managing the first-FVG trade — partials, break-even, and holding for mid gap
- **Kind:** rule
- **What ICT says:**
  - Once price breaks a short-term low after you are short, move the stop to cover costs (break-even); if you have more than one contract, take a partial below that short-term low.
  - At mid gap he suggests taking 75–80% off; if you want to try for the whole gap, put the stop above the short-term low and leave the balance ("if it stops you out on the balance, who cares, you had a free look").
  - If you don't know how to select partials: take two partials, keep the stop where it covers costs, and "let the market take you out" on the remainder; the target is only a reference. This "removes all the I have to be right stuff."
  - If trading one contract and the stop runs, accept it and record how you felt; don't think "I wish I had closed it at the maximum open profit."
  - After a loss do not "make up": next day, simply take the setup by the parameters on the smallest size.
- **How to use:** Stage 1: one exit at mid gap; later: partial -> stop to cost -> second partial at the next liquidity (e.g., relative equal lows) -> trail.
- **Example in this video:** In the hypothetical late-session short he walks through (2:00–2:07): short limit one tick above the CE of a wick (~19,745.25), stop above that wick's CE, first partial at the FVG, second partial at the relative equal lows, stop stays at cost, remainder runs to the rejection-block low.
- **Timestamps:** [0:57:15](https://youtu.be/fhBnnU44A6E?t=3435) stop to cover costs, partial below short-term low; [0:58:04](https://youtu.be/fhBnnU44A6E?t=3484) 75–80% off at mid gap; [2:04:31](https://youtu.be/fhBnnU44A6E?t=7471) two partials booked; [2:07:28](https://youtu.be/fhBnnU44A6E?t=7648) let the market take you out.
- **Nuance / caveats / changes:** First time in the series he states explicit % partial sizes for the mid-gap model.

### Mohawk (wick through a PD array) and being selective on "muddy" days  (aliases: "coloring outside the lines", "curveball", "feint")
- **Kind:** new coinage / refinement
- **What ICT says:** A Mohawk is price poking beyond a PD array (e.g., a wick above a bearish FVG) before honoring it; it is not a failure of the method. He compares it to a boxer's feint or a pitcher's curveball. Ideally price stays inside the gap, but on days before high-impact news the delivery is "muddier" and less crisp.
- **How to use:** On such days do not use the lowest entry threshold (candle 3's edge); be more selective: let price run to the extreme of the gap first, then sell inside the wick that creates the Mohawk, getting very good premium pricing with a stop above candle 2.
- **Timestamps:** [0:30:37](https://youtu.be/fhBnnU44A6E?t=1837) Mohawk created; [0:31:28](https://youtu.be/fhBnnU44A6E?t=1888) curveball analogy; [0:32:17](https://youtu.be/fhBnnU44A6E?t=1937) entry selectivity on muddy days.
- **Nuance / caveats / changes:** Refines #28's "specific price levels" teaching: on news-adjacent days the deepest part of the gap/wick is the better entry.

### FOMC-day behavior and avoiding it as a learner  (aliases: news driver, two-stage delivery)
- **Kind:** rule / context
- **What ICT says:** FOMC day is heavily manipulated and delivered in two stages: at 2:00 PM price goes one direction (higher or lower; he doesn't know which), and at the 2:30 press conference there is a counter-run, "usually, not all the time," over the top of the earlier move. Like NFP but more exaggerated. The day before FOMC is ranging/choppy with consolidations and less crisp price, and large players don't position ahead of it. For his inexperienced son: avoid FOMC day entirely (so no regret/temptation), and if trading the day before, only the morning session. Don't position large or swing-trade into it; the afternoon on the day before is dead and difficult.
- **Timestamps:** [0:12:52](https://youtu.be/fhBnnU44A6E?t=772) 2:00 / 2:30 two-stage delivery; [0:15:16](https://youtu.be/fhBnnU44A6E?t=916) why positioning ahead makes no sense; [1:14:14](https://youtu.be/fhBnnU44A6E?t=4454) day-before afternoon is spotty.
- **Nuance / caveats / changes:** "Usually" counter-run; he does not claim direction.

### Missed entries — getting into a move that has already started  (aliases: late entry, "regret", chase vs fade)
- **Kind:** rule / process
- **What ICT says:**
  - Missed entries come from freezing, second-guessing, turning the charts on late, or not noticing the setup. The title topic is "how to get into a move that's already happened or started," a skill he calls very valuable.
  - Time-frame translation: treat your execution time frame as the "hourly" of a smaller one: for a higher-time-frame trader, use a 15m or 5m (or in the examples 1m/15s) chart to get into a move that you missed on the hour, e.g., you scan the hourly chart, see a setup that has already started to move, and then trade into the first presented/next FVG on the lower time frame.
  - You have two choices when you miss a move: (1) regret, get angry, chase it or, worse, fade it because you are mad at the market; or (2) accept that the setups repeat, find another one, and wait for the FVG to be offered. He pushes (2): "wrestling the marketplace" is never good.
  - If the FVG isn't offered (price runs without giving you a gap), log it and don't get angry.
  - Use the time frame above the executable time frame and the time frame you intend to trade to frame the move.
- **How to use:** After the move starts, wait for a lower-time-frame FVG/imbalance to form in the move's direction (or an inversion), enter per the entry model, and require at least 20 handles of room to the first target.
- **Timestamps:** [0:04:36](https://youtu.be/fhBnnU44A6E?t=276) topic stated; [0:07:53](https://youtu.be/fhBnnU44A6E?t=473) hourly vs 15m/5m/1m translation; [0:09:29](https://youtu.be/fhBnnU44A6E?t=569) "get into a move that's already happened"; [0:41:58](https://youtu.be/fhBnnU44A6E?t=2518) two choices (regret/chase/fade); [1:16:37](https://youtu.be/fhBnnU44A6E?t=4597) don't be mad, find another setup.
- **Nuance / caveats / changes:** Builds on #28's "if you miss your limit, market in at the better price" with a lower-time-frame and psychology framing.

### "High frequency" no-bias drill: relative equal highs/lows on 1m/5m with a 15s FVG entry  (aliases: short-term liquidity runs, sub-one-minute model)
- **Kind:** entry model (drill)
- **What ICT says:** For FVG trading you can do high-frequency trading with no bias at all: map relative equal highs (or lows) on the 5m/1m chart near price, then use the 15-second FVG to enter a run to short-term buy-side/sell-side liquidity (take out short-term highs/lows). It works for any session (morning, afternoon, lunch). It gives a framework while learning but you will be stopped out more than with anything else he has taught, because you are chasing every small liquidity run. You get caught offside when you ignore time of day, day of week, week of the month, seasonal tendency and the daily/weekly order flow. 20–30 trades a day is possible and "wouldn't be overtrading" with the model, but in impulsive hands it blows accounts.
- **How to use:** Filter by the higher time frame draw: if the daily is drawing to a pool above, only take longs; do the unfiltered version only for baseline drills (non-monetized) to learn how you react.
- **Example in this video:** 15s chart drill with 1m/5m relative equal highs; HTF draw = hourly relative equal highs around 19,926 on the Dec contract (the Aug 27–29 highs: "four or five" smooth highs); also the Sept 13 daily high near 19,862.75 (caption unclear).
- **Timestamps:** [0:16:58](https://youtu.be/fhBnnU44A6E?t=1018) the no-bias idea; [0:47:36](https://youtu.be/fhBnnU44A6E?t=2856) risks and filters; [1:15:01](https://youtu.be/fhBnnU44A6E?t=4501) drill described; [1:19:02](https://youtu.be/fhBnnU44A6E?t=4742) filter longs only when monetized.
- **Nuance / caveats / changes:** Explicitly a drill/baseline tool; he does not recommend monetized use without the HTF filter.

### SMT divergence read from candle bodies (NQ vs ES), with the Dow as an early warning  (aliases: SMT)
- **Kind:** rule / refinement
- **What ICT says:**
  - Compare NQ with ES (Dec contract). In the example, NQ made a higher high in both wick and bodies; ES's wick went higher but its bodies at the high were lower than the prior high: that is an SMT divergence ("wicks do the damage," but bodies hold the bulk of the volume).
  - Look at the bodies of the swing highs/lows, not just the wicks.
  - Prefer NQ vs ES; the Dow is only an early warning, not the deciding factor. ICT does not trade YM: only 30 stocks, spotty, more wicks, moves first. S&P = 500 stocks (smoother), NASDAQ = 100, Dow = 30.
  - Make sure you are comparing the same contract month (he mistakenly reached for the Sept contract).
- **Timestamps:** [0:38:44](https://youtu.be/fhBnnU44A6E?t=2324) index composition; [0:39:31](https://youtu.be/fhBnnU44A6E?t=2371) the comparison; [0:41:10](https://youtu.be/fhBnnU44A6E?t=2470) bodies show the divergence.
- **Nuance / caveats / changes:** Body-based reading is a refinement of how he previously described SMT; direction implied (bearish divergence on highs) is not spelled out here.

### Grey pools — clusters of overlapping wicks as a PD array  (aliases: "gr pools", "grey pools")
- **Kind:** new coinage (introduced, not fully taught)
- **What ICT says:** Wicks are a PD array. The "gray area" of a cluster of overlapping wicks of different lengths is something nobody pays attention to, but the algorithm refers back to it; when looking lower, he looks for discount arrays and a clustering of wicks, not just FVGs, relative equal lows or a single low. He teases "x-ray view" of price and very precise, time-based new material for his book; he made a video on it the night before.
- **Timestamps:** [0:43:32](https://youtu.be/fhBnnU44A6E?t=2612) introduced; [0:44:21](https://youtu.be/fhBnnU44A6E?t=2661) why clusters matter; [0:46:48](https://youtu.be/fhBnnU44A6E?t=2808) time-based teaser.
- **Nuance / caveats / changes:** Details are deferred to the book/another video.

### Breaker block, mean threshold and "inverted" PD arrays  (aliases: low-high-lower-low breaker, MT)
- **Kind:** definition / refinement
- **What ICT says:**
  - A breaker here is the low-high-lower-low structure whose range he marks; he watches whether price gets above its mean threshold (the midpoint of the block).
  - Naming: for an order block (or breaker) the 50% is the mean threshold; for a gap or wick the 50% is consequent encroachment.
  - As long as price is below half of the breaker's range he has no interest in longs; a run below the breaker's low sets up a short.
  - "Everything I key off of... has an inverted aspect"; PD arrays can be treated the opposite way once violated. It looks like classic support/resistance but it is "very specific candles, very specific prices": the low, the lower quadrant and the halfway of the block.
  - Prefers to see price spike through a block or take liquidity then show inversion/displacement, and bodies staying inside a block are not displacement.
- **Example in this video:** 15s/1m NQ late morning: price rallies to the top of a breaker (Sept 13 daily high area), bodies stay inside it, no inversion, then drops to a lower low.
- **Timestamps:** [1:35:09](https://youtu.be/fhBnnU44A6E?t=5709) PD arrays have inverted aspects; [1:49:41](https://youtu.be/fhBnnU44A6E?t=6581) mean threshold vs CE naming; [1:52:10](https://youtu.be/fhBnnU44A6E?t=6730) bodies inside = no displacement outside.
- **Nuance / caveats / changes:** He holds off explaining why the names were chosen ("the books will explain").

### Minimum range filter — 20 handles from entry to first target
- **Kind:** rule
- **What ICT says:** If you can't frame at least about 20 handles from entry to the target, sit still: "we can see the moves coming but it's not framable" for his son's model. Later: finding a setup and getting 20–25 handles is "a nice little bread and butter setup."
- **Timestamps:** [1:32:44](https://youtu.be/fhBnnU44A6E?t=5564) "that's the filter"; [2:08:16](https://youtu.be/fhBnnU44A6E?t=7696) 20–25 handles.
- **Nuance / caveats / changes:** Consistent with #28 (15–20 handles; avoid 10).

### "Buy program" / one-sided delivery — where not to trade
- **Kind:** example only / refinement
- **What ICT says:** When price keeps ticking higher with no FVG (only tiny volume imbalances that rebalance immediately), bodies stay inside the prior PD array, and no displacement forms, the market is in a buy program and will keep offering higher prices regardless of how many people are short or what liquidity tools show; it squeezes until it reaches an inefficiency or liquidity (here the 1m short-term high, the top of the breaker/Sept 13 high). Being offside is "extremely painful." He declined the short to illustrate this ("exactly where you do not want to trade").
- **How to use:** If no FVG is offered, do not force an entry. After a one-sided run, wait for an energetic run/displacement and an inefficiency.
- **Example in this video:** From about 1:44 to 1:52, NQ grinds up to the top of the breaker, he shows there is no FVG, then a sharp drop; "I want to see this small portion stay open" before shorting.
- **Timestamps:** [1:43:56](https://youtu.be/fhBnnU44A6E?t=6236) screenshot this; [1:45:32](https://youtu.be/fhBnnU44A6E?t=6332) buy program; [1:51:21](https://youtu.be/fhBnnU44A6E?t=6681) classic; [2:09:04](https://youtu.be/fhBnnU44A6E?t=7744) one-sided runs hide inefficiencies.
- **Nuance / caveats / changes:** Contrasts with his trade-with-the-gap lecture: the gap must exist to take the trade.

### Why a candidate setup was rejected — shallow, justifiable both ways, too long inside the gap
- **Kind:** example only
- **What ICT says:** He passed on a short because price spent too long inside the gap (a stop-out scenario), the setup was too easy/shallow, and he could justify both a rally and a sweep of equal lows, so it was not high probability; selling at the low end of the day's range after a big drop means selling a discount to people wanting to buy cheap. He also wanted price to take a higher short-term high first and then give an FVG and inversion before shorting. Capital preservation is the main thing; knowing how you can lose and saying "no, this isn't it" comes with experience.
- **Timestamps:** [1:38:31](https://youtu.be/fhBnnU44A6E?t=5911), [1:39:21](https://youtu.be/fhBnnU44A6E?t=5961), [1:56:00](https://youtu.be/fhBnnU44A6E?t=6960).
- **Nuance / caveats / changes:** A balanced price range (single candle up/single candle down sharing the same range) is also mentioned at 1:41 and 1:56 as the area to wait for a trade-through before acting.

### Swing low validation and minor buy side
- **Kind:** definition
- **What ICT says:** A swing low is validated as soon as the candle after it closes; sell stops sit below it theoretically; buy-side is the nearby high. Annotating minor buy side/sell side follows from where the market turned.
- **Timestamps:** [1:24:16](https://youtu.be/fhBnnU44A6E?t=5056), [1:25:05](https://youtu.be/fhBnnU44A6E?t=5105).
- **Nuance / caveats / changes:** Brief.

### Macro windows referenced (ET)
- **Kind:** example
- **What ICT says:** He wanted to work inside the 10:00 hour for a Silver Bullet but would wait for the 9:50–10:10 macro; he later points to the 10:50–11:10 macro (lunch macro) as the time sell-side is taken out and price moves against traders who are long.
- **Timestamps:** [0:08:41](https://youtu.be/fhBnnU44A6E?t=521), [1:29:09](https://youtu.be/fhBnnU44A6E?t=5349), [1:31:04](https://youtu.be/fhBnnU44A6E?t=5464).
- **Nuance / caveats / changes:** No new windows defined.

## Rules, checklists & numbers stated
- ORG = previous settlement (last print 4:14 PM ET) to the 9:30 open; opening range = 9:30–10:00.
- Gap filter: minimum 40 handles; larger better; sweet spot ~100; above ~200 defer.
- Mid gap (50%) hit ~70% of the time by 10:00; quadrants also plotted.
- First FVG after 9:31 only (candle 2 no earlier than 9:31); trade toward mid gap.
- Stop: beyond candle 2's extreme; short entry near candle 3's high (aggressive: one tick below) or deeper in the gap.
- Management: stop to cost after short-term low breaks; partial there; 75–80% at mid gap; remainder to try to close the gap; two partials then let market take you out.
- 20-handle minimum range to first target (20–25 handles = bread and butter).
- Use one micro/one contract in a demo for at least a month, every day, and log how you feel.
- Day before FOMC: morning only (for beginners) and avoid FOMC day entirely; 2:00 / 2:30 PM two-stage delivery.
- SMT: compare NQ with ES bodies; Dow = early warning only.
- Use only the same contract month on all charts (Dec at this date).

## Process, risk & psychology
- Demo drills reveal your habits and "character flaws"; the goal is baseline data on how you respond when wrong or when a trade runs away; do not hide from it ([1:19:02](https://youtu.be/fhBnnU44A6E?t=4742)).
- Do not monetize the exercise; do not copy his paper trades; he is not a signal service and asks viewers not to report profits or he blocks them ([2:10:41](https://youtu.be/fhBnnU44A6E?t=7841)).
- Record emotion for a full month of daily practice; "the you is what's going to mess it up" ([1:07:43](https://youtu.be/fhBnnU44A6E?t=4063)).
- Don't over-leverage after a missed trade to "make it up"; no make-up trades ([1:06:54](https://youtu.be/fhBnnU44A6E?t=4014)).
- Only 1-2 drills a day is fine; it's like an exercise routine ([1:15:01](https://youtu.be/fhBnnU44A6E?t=4501)).
- Sit still when nothing is framable; there has to be a reason to take every trade; "I'm here to teach my son patience" ([1:41:45](https://youtu.be/fhBnnU44A6E?t=6105)).
- Being stopped out is acceptable; he does not teach that you have to be right.
- His paper trade was blocked by TradingView paper-trading maintenance, so the last setup was only described.
- Short tangent on carrying charge vs inverted ("commercial bull") futures curves: December NQ trades at a premium to September (normal carrying charge), more relevant for real commodity markets; he credits Larry Williams' book for premium pricing ideas and refers to the 2017 mentorship commodity month (caption says "2027," unclear).

## Glossary candidates
`Mid gap` — the 50% (CE) of the opening range gap.
`Opening range gap (ORG)` — previous RTH settlement (4:14 PM last print) to the 9:30 open.
`First presented FVG` — the first FVG forming after 9:31 used as the entry mechanism toward mid gap.
`Mohawk` — a wick that pokes beyond a PD array before price honors it ("coloring outside the lines").
`Grey pools` — clusters of overlapping wicks treated as a PD array.
`Mean threshold (MT)` — midpoint of an order block/breaker; for a gap or wick the midpoint is CE.
`Buy program` — a steady, gapless, bodies-inside run higher in which price keeps offering higher prices.
`Terminus` — final exit target (stage 2 after a first partial) — see #28.
`Premium gap` — an opening gap above the previous settlement.
`Handle` — one NQ point (4 ticks).
