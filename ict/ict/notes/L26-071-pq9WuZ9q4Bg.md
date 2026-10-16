# L26-071 — Futures Market Review \ Lecture On Shadows Validating PD Arrays
ID: pq9WuZ9q4Bg · URL: https://www.youtube.com/watch?v=pq9WuZ9q4Bg · Duration: 55:28
Content type: market review (with a live-trade recording at the start and a mindset segment near the end)
Teaching density: high for the first ~40 min (wick-CE grading, order block = CISD entry, shadows, octant/quadrant anchoring); low for the last ~15 min (DXY, crude, BTC, gold, silver, personal remarks)

## Summary
ICT reviews NQ (September contract) over Monday, Tuesday "the 30th" and the current Wednesday session, using a daily chart that carries a daily bearish FVG overlapping a daily "suspension block" that he splits into quadrants and octants. The lecture's core idea is the "shadow": where two imbalances overlap, the overlap is itself a PD array, and any lower-timeframe FVG or volume imbalance that touches (is anchored to) one of its quadrant/octant levels is validated. A fair value gap is valid only if it is the first-presented FVG, or if it is anchored to such a level; volume profile and low-volume nodes are explicitly rejected as the validation logic. Repeated again and again is the wick-consequent-encroachment test (bodies may not close beyond the CE of a wick), the order-block-as-change-in-state-of-delivery entry at a candle's opening price, and framing risk from the wick extreme to the entry zone. The last third is a market-by-market glance (DXY, EURUSD, crude, BTC, gold, silver), seasonal comments, and a strong mindset message: if you can argue both sides, don't trade.

Dates: the only date he states is "Tuesday 30th"; the other days are "Monday" (earlier in the same week) and "today" (Wednesday, in the month of July by his own remark). Prices below are NQ unless stated. Captions around tick-level prices are shaky; flagged where so.

## Concepts

### Shadow (PD array shadow)  (aliases ICT uses: "shadow", "bleeding over of two imbalances", "salmon area")
- **Kind:** new coinage
- **What ICT says:**
  - When one PD array overlaps another imbalance, the overlap is a PD array in its own right; he calls it a "shadow" because it casts a shadow over another imbalance.
  - On the daily NQ chart the bearish daily FVG is shaded pink and the daily suspension block is shaded orange; where they overlap the colour is salmon. That salmon overlap is the shadow, and it can be "graded" (measured with quadrant/octant/fib levels) just like any other range.
  - Other approaches (supply/demand, volume profile, footprint) would not look at that overlap or grade it this way.
  - Once such a range exists, you can measure any PD array that forms against it, but the new PD array "has to be touching" it: the high, the low, or anywhere in between. Touching = anchored.
- **How to identify:** an overlap between two higher-timeframe PD arrays (here: daily bearish FVG and daily suspension block); the shaded overlap region is the shadow. The suspension block's high/low sit at its edges.
- **How to use:** project quadrants/octants (and even 16ths) across the shadow; look for lower-timeframe FVGs, volume imbalances or wicks that touch those levels; trade them with the wick-CE and CE rules below. He says he plots the fib levels on it ("don't tell anybody what they are") but does not state exact fib percentages in this video.
- **Example in this video:** Wednesday session (today): price sells off at 9:30 inside the upper octant of the daily suspension block / daily bearish FVG, then later in the day a bullish FVG forms at the low of the overlap (the shadow) — wick/body prices around 146.50 (full price likely 30,146.50; caption unclear). He calls this FVG "anchored to the low of that shadow", then price trades lower and the next FVG he finds sits exactly on an octant level; he says that is what makes it valid.
- **Timestamps:** [0:34:32](https://youtu.be/pq9WuZ9q4Bg?t=2072) — FVG forms at the low of the overlap of pink bearish FVG and the suspension block; [0:36:12](https://youtu.be/pq9WuZ9q4Bg?t=2172) — he names it a "shadow"; [0:36:59](https://youtu.be/pq9WuZ9q4Bg?t=2219) — the upper quadrant of the range, and "it has to be touching"; [0:39:30](https://youtu.be/pq9WuZ9q4Bg?t=2370) — next FVG is on an octant = valid.
- **Nuance / caveats / changes:** The title promise ("shadows validating PD arrays") is exactly this: a smaller PD array is validated by being anchored to a level of the shadow's range. How the suspension block itself is constructed is only partly explained here (see next concept).

### Daily suspension block with quadrants / octants (and 16ths)  (aliases: "daily suspension block", "octant levels", "upper octant", "lower quadrant")
- **Kind:** definition (partial) / refinement
- **What ICT says:**
  - The daily chart has a "suspension block" PD array (orange). He subdivides its range into quadrants (quarters) and octants (eighths), and uses those levels as reaction points for intraday entries (Monday short at the "lower quadrant", Tuesday long off the "high of the suspension block", Wednesday selloff in the "upper octant").
  - Partial explanation of the build here: the suspension block's edge exists because one daily candle's high is lower than the next candle's body, so the two overlap; that overlap with the daily bearish FVG creates the colour change. The clean definition is in the next video (L26-072, [0:47:07](https://youtu.be/rbNhlJSXDaA?t=2827)): a single candle suspended between two volume imbalances (one at its low, one at its high), treated as an inversion FVG.
  - He suggests going finer: split the space between an octant and a quadrant in half (16ths). He admits he doesn't do it publicly ("too good") but says everyone should start doing it.
- **How to identify:** the suspension block's high and low; then draw quarters and eighths between them.
- **How to use:** these levels are where lower-timeframe FVGs, order blocks and wicks are anchored. Premium levels (upper octants/quadrants) are used for shorts at macro time; discount levels / the block's high on a dip are used for longs depending on narrative.
- **Example in this video:** Monday: short at the lower quadrant of the daily suspension block, at the session high around the 9:50–10:10 macro. Tuesday 9:30–10:10: opening trades down into the high of the daily suspension block, wick is graded, price rips higher.
- **Timestamps:** [0:00:01](https://youtu.be/pq9WuZ9q4Bg?t=1) — short at daily suspension block octant levels; [0:08:30](https://youtu.be/pq9WuZ9q4Bg?t=510) — orange block, lower quadrant, another octant; [0:14:57](https://youtu.be/pq9WuZ9q4Bg?t=897) — Tuesday: high of the suspension block + macro start; [0:40:18](https://youtu.be/pq9WuZ9q4Bg?t=2418) — 16s comment ([0:39:30](https://youtu.be/pq9WuZ9q4Bg?t=2370) leads in).
- **Nuance / caveats / changes:** "Daily suspension block" and its octant grid are 2026-era vocabulary; treat as a dealing-range grid applied to a specific daily PD array, not to the whole dealing range.

### Fair value gap validation: first presented, or anchored  (aliases: "first presented fair value gap", "anchored FVG")
- **Kind:** rule
- **What ICT says:**
  - An FVG is valid in one of two ways: (1) it is the first-presented FVG (the first one that forms after the relevant move/open), or (2) if it is not first-presented, it is always anchored to an octant or quadrant level. "Period."
  - Volume profile / low-volume-node logic is explicitly rejected as the way to find "real" FVGs ("wrong, wrong, wrong"); sometimes they agree, but "that is not the logic".
  - On Tuesday, the first FVG after the 9:30 open (about 9:35) was acceptable as first-presented, but he preferred the later one because the run out of it was more prominent.
- **How to identify:** (a) first FVG after the opening/impulse, or (b) FVG whose high, low or interior touches an octant/quadrant (or shadow) level of the higher-timeframe range.
- **How to use:** after validation, wait for price to retrace into the FVG; strength = no trade into the lower half (for longs) and no bodies in the lower half; then enter using the wick/CE entry mechanism below.
- **Example in this video:** Tuesday 9:35 first presented FVG after the open; Wednesday 9:30 selloff clears an area, creates "first presented fair value gap", rallies; price cannot reach the FVG's CE, then a wick forms and also does not touch its own CE.
- **Timestamps:** [0:12:37](https://youtu.be/pq9WuZ9q4Bg?t=757) — Tuesday first-presented FVG at 9:35; [0:26:26](https://youtu.be/pq9WuZ9q4Bg?t=1586) — Wednesday first presented FVG, "very strong entry mechanism"; [0:35:23](https://youtu.be/pq9WuZ9q4Bg?t=2123) — the validation rule stated.
- **Nuance / caveats / changes:** contradicts the many retail "validate FVG with volume profile" methods. Does not discard FVGs that are neither first-presented nor anchored; they simply aren't treated as valid.

### Wick consequent-encroachment grading  (aliases: "grade that wick", "premium sensitivity", "discount sensitivity")
- **Kind:** rule / refinement
- **What ICT says:**
  - When you anticipate a run off an order block/PD array and that candle prints a wick, measure the wick's consequent encroachment (its 50%). The wick then behaves with "discount sensitivity" for longs (and "premium sensitivity" for shorts).
  - Long case: price may touch the CE of the wick, but must not put a body below it. A body below the wick's CE invalidates the short-term bullishness. If price cannot even touch the CE, that validates the bullishness even more strongly.
  - Short case (mirror): bodies must stay below the CE of the wick above; "I don't want to see the body above that consequent encroachment level — that's the whole point of plotting that." On higher timeframes, a daily wick's CE needs a close beyond it to open the target (Monday recap: a daily wick CE needed a close below it to target the sell side; price did not close below, so no continuation).
  - Wicks are allowed to poke through; it is the bodies that matter. He admits you cannot know in real time if the wick will hold; "trust your analysis" and use a stop.
  - EURUSD example (end of video): he marked a wick CE the previous session and wanted no bodies above its half; bodies stayed below it and price dived. For a continuation lower, price would need to close beyond another wick's CE below.
- **How to identify:** pick the wick created by the candle/order block you are trading; draw its midpoint; track bodies, not wicks.
- **How to use:** a clean wick-CE test is the entry qualifier; stop goes at the wick extreme (see entry mechanism below).
- **Example in this video:** Tuesday PM (2:06 p.m. ET low): after sell side is raided at 2:06, the candle's wick is graded and price never gets a body below the CE; next candle open trades below the order block's opening price and he says "just go in there and take a long." Wednesday morning: a wick forms after the FVG, drawn down to the wick low; it does not touch CE, "perfect... strong qualification that it's going to go higher."
- **Timestamps:** [0:02:34](https://youtu.be/pq9WuZ9q4Bg?t=154) — short side: want the body to stay below the wick's CE; [0:20:41](https://youtu.be/pq9WuZ9q4Bg?t=1241) — long side: touch allowed, body below invalidates; [0:11:50](https://youtu.be/pq9WuZ9q4Bg?t=710) — "premium sensitivity" + allow wicks to wick; [0:44:22](https://youtu.be/pq9WuZ9q4Bg?t=2662) — EURUSD application.
- **Nuance / caveats / changes:** in the EURUSD/NQ "no man's land" case two opposing wick-CE conditions held at once (price trapped between two CE levels), which he treats as a reason not to trade (see Process).

### Order block as Change in State of Delivery (opening-price entry)  (aliases: "order block change in the state of delivery", "OB = CISD")
- **Kind:** entry model / refinement
- **What ICT says:**
  - An order block is not a "demand zone"; it is one specific price: the opening price of a candle. The change in state of delivery is validated when price trades above (for bullish) that opening price; it does not need to close above it.
  - Context for a bullish one: price is running from a discount to a premium / into a higher-timeframe PD array; price opens, trades down, shows willingness to go higher, and as soon as it trades above the candle's open it validates.
  - Then, when price trades back down into it (back below the open), you can long; if you lack conviction, wait for the candle close down to the wick CE. Anywhere between the open and the wick CE is a valid long.
  - Smooth lows being taken (sell side purged) is why a close above isn't needed.
- **How to identify:** pick the down-close candle at the low whose opening price is later traded above; measure its wick CE.
- **How to use:** entry between the open and the CE of the wick; stop at the wick low; target the nearby buy side (he runs to "buy side right there").
- **Example in this video:**
  - Tuesday ~9:49 ET: a candle opens at 30,226.00. Price had hit the high of the daily suspension block (higher-timeframe PDA), opened and traded down, then trades above that opening price. The retrace low is around 30,224 (caption "224 12"; unclear). Price then runs aggressively through the highs and buy side and rises to the high of the daily bearish FVG (pink).
  - Tuesday PM: an order block opens at 30,519.75; the low of the candle trades to 30,519.00 (three ticks below the open) to "trade into" the CISD, then price runs. Sell-side raid and low at 2:06 p.m. ET, then trades above the opening price, validates, comes back into it on a later candle for the long entry.
- **Timestamps:** [0:15:46](https://youtu.be/pq9WuZ9q4Bg?t=946) — 9:49 candle open 30,226; [0:16:35](https://youtu.be/pq9WuZ9q4Bg?t=995) — "that's not a demand zone... a very specific price"; [0:19:52](https://youtu.be/pq9WuZ9q4Bg?t=1192) — 30,519.75 open, three-tick poke; [0:21:32](https://youtu.be/pq9WuZ9q4Bg?t=1292) — 2:06 pm low and validation.
- **Nuance / caveats / changes:** "Does not need to close above" is the key difference from the stricter CISD/close-based definitions. This is order block theory expressed through CISD and opening price rather than a zone drawn from the body.

### Entry mechanism around a validated wick/FVG: open-to-CE entry with wick-low stop  (aliases: "bangers", "strong entry mechanism")
- **Kind:** entry model
- **What ICT says:**
  - After the FVG/OB is validated and a wick has formed, enter anywhere from the candle's open (body) down to the wick's midpoint (CE). Use the low of the wick as the stop. For a more conservative entry: use the candle's close down to the CE.
  - Frame risk "from the candle's low of that wick to whatever your entry would be in the upper half to CE."
  - Target: the buy side immediately above.
  - He stresses he's showing the logic, not telling people where to buy in live conditions, and claims this is entire-model teaching (entry, targets, stops) that critics say he withholds.
- **How to identify:** validated FVG/OB + wick that does not trade below its CE with a body.
- **How to use:** see above; stops are the wick low; targets are BSL/SSL beyond.
- **Example in this video:** Wednesday: first presented FVG forms after the sell-off; price cannot reach FVG CE; wick below does not touch wick CE; long from the open of the candle down to wick CE with stop at wick low; price rises and tags buy side "right above here" and then dips back into the suspension block before trading significantly higher outside the bearish daily FVG (a market structure shift).
- **Timestamps:** [0:22:20](https://youtu.be/pq9WuZ9q4Bg?t=1340) — risk frame; [0:26:26](https://youtu.be/pq9WuZ9q4Bg?t=1586) — "very strong entry mechanism"; [0:29:36](https://youtu.be/pq9WuZ9q4Bg?t=1776) — open-to-CE entry, wick low stop.
- **Nuance / caveats / changes:** no fixed R multiples or size in the video; stops are purely structural.

### Inversion fair value gap (iFVG) in use  (aliases: "failure inversion FVG")
- **Kind:** example only / refinement
- **What ICT says:**
  - Bullish FVG inverts when price trades back down below it (Tuesday last hour: a bullish FVG, then price trades below it, validating an ICT inversion FVG that will act as resistance later).
  - In a short: he lowered his stop above the highs to the left; wants the iFVG not to fail, but to be broken through aggressively; wants no bodies back in the upper half of the iFVG; if the low of that iFVG never gets traded back to, that is "indicative of a very weak market".
  - He looks for a failure iFVG at highs (gold: high forms, failed iFVG, then sells off).
  - Monday: a bullish FVG that price traded down through, then above ("bodies respecting it even though we wick through it") before the rally.
- **How to identify:** an FVG that is traded through in the opposite direction (body close beyond).
- **How to use:** after an inversion, wait for retrace; bodies should not return beyond the CE/half; use as trailing structure for the stop.
- **Example in this video:** Recording at start: short at the daily suspension block octant level; iFVG forms; stop lowered above all highs; price breaks through aggressively, "no more bodies in the upper half" so risk is removed; another iFVG appears and he scales off below its low.
- **Timestamps:** [0:00:01](https://youtu.be/pq9WuZ9q4Bg?t=1) — iFVG management; [0:23:09](https://youtu.be/pq9WuZ9q4Bg?t=1389) — Tuesday bullish FVG inverting; [0:07:42](https://youtu.be/pq9WuZ9q4Bg?t=462) — Monday's iFVG.
- **Nuance / caveats / changes:** he doesn't re-teach the definition; he assumes the viewer already knows.

### Macro time false breakout at premium  (aliases: "9:50–10:10 macro", "false breakout", "bull flag lovers get smoked")
- **Kind:** rule / example only
- **What ICT says:**
  - Price running to a premium level (upper octant/quadrant of the daily suspension block) at the 9:50–10:10 macro is expected to create a false breakout (a raid of smooth highs/buy side), and price then goes lower.
  - Retail "bull flag" breakouts get trapped by this.
  - Macro windows are where the algorithmic run happens; the run begins in the macro and the displacement follows.
- **How to identify:** time inside macro window + price touching a premium octant/quadrant + taking out smooth/equal highs.
- **How to use:** short at the level as price ticks to it; grade the execution (see below); target the sell-side liquidity beneath.
- **Example in this video:** Monday: macro 9:50–10:10 run takes out smooth highs and relative equal highs at the lower quadrant of the daily suspension block, then sells off; he shorts at the session high.
- **Timestamps:** [0:08:30](https://youtu.be/pq9WuZ9q4Bg?t=510) — "the key point here, during the macro time"; [0:11:50](https://youtu.be/pq9WuZ9q4Bg?t=710) — premium sensitivity at that time of day creates the false breakout; [0:02:34](https://youtu.be/pq9WuZ9q4Bg?t=154) — "my short started between the 950 and 1010 macro."
- **Nuance / caveats / changes:** Only the 9:50–10:10 window is named explicitly here; other macros mentioned only as "macro time" (caption unclear).

### Volume imbalance precision and including imbalances in FVG measurement  (aliases: "volume imbalance", "include the volume imbalances")
- **Kind:** refinement / example only
- **What ICT says:**
  - When measuring an FVG for its CE, include the volume imbalances adjacent to it; otherwise bodies can appear to touch/not touch CE incorrectly. (He changed colours to show bodies are not touching the CE once the imbalances are included.)
  - Tick-level precision example: one candle's open is 173.75 and another candle's high is also 173.75 = a perfect volume imbalance; and a wick low at 175.00 vs high 175.50, with a close at 175.25 shows how price works inside a volume imbalance to the tick.
  - He says order flow, volume profile, Elliott Wave, Wyckoff and Gann don't give this level of precision.
  - He double-checks (admits he misread) whether a volume imbalance exists on one FVG: the candle close and open both at 146.50; using the wick low down to the wick high as the FVG instead.
- **How to identify:** gap between bodies of consecutive candles where the wicks overlap.
- **How to use:** include in the FVG range when measuring CE; levels used as exact reaction prices.
- **Example in this video:** NQ Wednesday PM: candle with low 30,175.00 vs candle high 30,175.50, close 175.25, open 173.75 vs high 173.75 (caption partially unclear).
- **Timestamps:** [0:31:15](https://youtu.be/pq9WuZ9q4Bg?t=1875) — include volume imbalances; [0:34:32](https://youtu.be/pq9WuZ9q4Bg?t=2072) — checking for imbalance; [0:37:47](https://youtu.be/pq9WuZ9q4Bg?t=2267) — tick-level example.
- **Nuance / caveats / changes:** not a new concept, just a reminder of how to draw it.

### Series of down-close candles with increasing bodies  (new coinage / caption unclear)
- **Kind:** new coinage (unclear)
- **What ICT says:** In a series of down-close candles, each one with a larger body than the last ("this down close candle's larger in the body than this one, then that one, and this one"), there is a recurring pattern he "just recently taught in a Space" and says "it works all the time". He ties it to the Tuesday PM order block (the 30,519.75 candle). The rest of the lesson is in that Space and not captured here.
- **How to identify:** consecutive down-close candles where body size grows.
- **How to use:** not stated in this video; presumably as exhaustion/entry into the order block that follows (my reading, caption-unclear).
- **Example in this video:** Tuesday 1:30 PM session: drop in the PM session, a little V-shaped gap, wick trading down into CE, body sizes growing as it falls; then the order block open at 30,519.75 and the three-tick poke.
- **Timestamps:** [0:18:14](https://youtu.be/pq9WuZ9q4Bg?t=1094) — observation; [0:19:52](https://youtu.be/pq9WuZ9q4Bg?t=1192) — "almost like it works all the time."
- **Nuance / caveats / changes:** He says that if you don't listen to the Spaces you won't get everything; worth checking the Spaces/other lectures. Cross-reference: in L26-072 ([0:44:41](https://youtu.be/rbNhlJSXDaA?t=2681)) he states that the largest down-close candle in a series is the change-in-state-of-delivery order block, which very likely is the point of this remark (the growing bodies identify which candle is the order block).

### Market on close (MOC) algorithmic window and iFVG  (aliases: "merger on close", "MOC")
- **Kind:** example only
- **What ICT says:** In the last few minutes of the last hour of regular trading, the "market on close" period is very algorithmic: price rips lower, comes right back up and hits an iFVG ("there's your iFVG for MOC"). You have to blend time and price. A wick down there can be graded by its CE; no bodies above it.
- **How to identify:** last minutes of RTH + an earlier bullish FVG that was inverted + a violent run to it.
- **How to use:** as an entry/target level around the close.
- **Example in this video:** Tuesday final hour: bullish FVG breaks above a high, later inverted when price trades below; at MOC, a quick drop and reversal back up taps the iFVG; sell side then trades down into the "450" area (caption unclear) at a macro time and rebounds into the range.
- **Timestamps:** [0:23:58](https://youtu.be/pq9WuZ9q4Bg?t=1438) — iFVG + MOC; [0:24:47](https://youtu.be/pq9WuZ9q4Bg?t=1487) — wick grade.
- **Nuance / caveats / changes:** exact clock times for MOC and the final macro are not stated.

### RTH opening range gap (historical origin and use)  (aliases: "premium gap opening", "regular trading hours opening range gap")
- **Kind:** definition / history
- **What ICT says:** If the market opens above the prior day's close, that is a premium gap (an RTH opening range gap higher). Early in his career he took the idea from Larry Williams' "open vs yesterday's close" observations and reformulated it: look for a fill; if bullish, even half of the gap being filled is enough to see price go higher; if bearish, want price to break through the gap and then use the gap range to measure projections lower. He says this is not part of the current model but influenced him as a technician.
- **How to use:** Monday NQ: opened and traded up into the gap but could not reach its midpoint (CE), then broke lower, which he used for the short.
- **Timestamps:** [0:46:47](https://youtu.be/pq9WuZ9q4Bg?t=2807) — description; [0:10:14](https://youtu.be/pq9WuZ9q4Bg?t=614) — Monday gap and CE.
- **Nuance / caveats / changes:** in the Monday example the gap is described briefly and may be a daily/RTH gap (caption unclear).

### Execution grading and management  (aliases: "one execution, not one of 17")
- **Kind:** rule / process
- **What ICT says:**
  - He grades execution by whether the candle after the entry candle goes meaningfully above (for shorts) the entry candle; ideally the entry candle is the high, and bodies don't go higher. A wick through then displacement lower is acceptable. Not a self-beating exercise but a grading method.
  - Live management in the recording: build up the position on iFVG; lower stop above highs to the left; remove risk; scale partials at each new sell-side pool/small FVG; limit order just below an SSL; final target new intraday low; done for the day when hit.
  - He logs screenshots at each step to show it was one managed position, not 17 entries ("no market replay").
- **Timestamps:** [0:09:26](https://youtu.be/pq9WuZ9q4Bg?t=566) — execution grading; [0:01:42](https://youtu.be/pq9WuZ9q4Bg?t=102) — screenshots, one execution; [0:04:11](https://youtu.be/pq9WuZ9q4Bg?t=251) — final partial and exit at the new low.

### Other markets and seasonal remarks (brief)
- **DXY:** daily buy/sell-side efficiency high formed where he guessed, then traded lower and closed outside a bullish FVG; he doesn't need the high; EUR and GBP hit his targets. Not trading forex.
- **Crude oil:** price working into the lower part of a volume imbalance he flagged earlier; the position of that imbalance depends on the "adjust for contract rollover" chart setting (back-adjusted vs not; toggling shows it "there but not there"); over $24,000 of movement per contract. Not buying it there even though a seasonal tendency (Steve Moore's seasonal data) begins around the second week of July (summer driving, supply build-up for winter); a geopolitical escalation could extend the upside.
- **Bitcoin:** target two at 54,353 (midpoint of the low and an old low at 49,656, "event horizon line", caption unclear), target three higher; bias lower while below the high; he doesn't trade crypto.
- **Gold / silver:** gold wilting inside an FVG after a short-term high is taken; silver inside an FVG with sell side and relative equal lows beneath; a break would disrupt long-term bullishness in metals. He says he is content with "$60,000 of just this run" (most likely the dollar value of the move per contract, not his P&L; caption unclear).
- **Timestamps:** [0:41:06](https://youtu.be/pq9WuZ9q4Bg?t=2466) — DXY; [0:49:13](https://youtu.be/pq9WuZ9q4Bg?t=2953) — crude; [0:51:38](https://youtu.be/pq9WuZ9q4Bg?t=3098) — BTC; [0:53:16](https://youtu.be/pq9WuZ9q4Bg?t=3196) — gold; [0:54:07](https://youtu.be/pq9WuZ9q4Bg?t=3247) — silver.

## Rules, checklists & numbers stated
- FVG valid only if first-presented, or anchored (touching) an octant/quadrant level of the higher-timeframe range or shadow.
- Do not validate FVGs with volume profile / low-volume nodes.
- Wick CE test: long, can touch CE but no body below it; short, no bodies above the CE of the wick above; a daily wick CE needs a close beyond it to open the target.
- Order block (CISD) validates when price trades through the candle's open; no close required.
- Entry zone: open of the candle to the wick CE; stop at wick low (long) / high (short).
- 9:50–10:10 macro is the window where the false breakout at premium occurred (Monday short).
- Tick-level examples: open 30,226.00 (Tue 9:49); 30,519.75 open with 30,519.00 low (3 ticks); Tuesday PM sell-side low at 2:06 p.m. ET.
- Quadrants, octants, and 16ths of the daily suspension block.
- Include volume imbalances when measuring an FVG's CE.
- July/summer: expect finicky markets, not conducive to low-resistance liquidity runs.
- Take only one or two setups per week in those conditions; once you get it, be done.
- If you can argue both sides, don't trade.

## Process, risk & psychology
- [0:06:46](https://youtu.be/pq9WuZ9q4Bg?t=406): if your daily-chart conviction is strong, trust your own analysis; he prefers to play intraday with a modest bias when he isn't in sync with the larger consolidation.
- [0:17:23](https://youtu.be/pq9WuZ9q4Bg?t=1043): some price delivery is simply untradeable; he lets those segments go without him; find significance in your own efforts rather than attaching his name to results.
- [0:42:46](https://youtu.be/pq9WuZ9q4Bg?t=2566): in low-probability summer conditions slow down, look for one or two setups a week, then stop; a longer weekend is a blessing.
- [0:47:36](https://youtu.be/pq9WuZ9q4Bg?t=2856) to [0:49:13](https://youtu.be/pq9WuZ9q4Bg?t=2953): if you can frame both sides ("could go higher, could go lower"), "turn your chart off"; one-sided conditions are what he calls high probability; otherwise you are chasing a "participation award" because of lack of discipline, impatience or no model. If you're right it was a guess; if wrong you knew better.
- [0:32:53](https://youtu.be/pq9WuZ9q4Bg?t=1973): "simple" is not always precise; a coin flip is the simplest system but has no logic behind it.
- [0:28:00](https://youtu.be/pq9WuZ9q4Bg?t=1680) to [0:28:47](https://youtu.be/pq9WuZ9q4Bg?t=1727): rebuts claims he doesn't teach entries/exits; he says precision requires more words because every rule has validation and invalidation, which removes ambiguity.
- [0:11:50](https://youtu.be/pq9WuZ9q4Bg?t=710): you can't know everything at all times; rely on analysis plus a stop loss.
- [0:45:10](https://youtu.be/pq9WuZ9q4Bg?t=2710): Larry Williams influence (seasonals, COT); Steve Moore for seasonal data; he avoids chasing indicator/pattern ideas because he has no faith in them.

## Glossary candidates
`SHADOW` — the overlap region of two imbalances (e.g. daily bearish FVG and daily suspension block), itself a gradeable PD array.
`SUSPENSION BLOCK` — a daily PD array (orange) used with quadrant/octant levels; partially defined here (candle high lower than another candle's body, overlapping).
`OCTANT / QUADRANT` — eighth and quarter subdivisions of a range; "16s" splits the gap between them again.
`PREMIUM SENSITIVITY / DISCOUNT SENSITIVITY` — how a wick behaves relative to its CE: bodies must not cross the CE of the wick on the bearish/bullish side.
`FIRST PRESENTED FVG` — the first FVG after an impulse/open; otherwise FVGs must be anchored.
`ANCHORED (PD ARRAY)` — touching an octant/quadrant/shadow level.
`CHANGE IN STATE OF DELIVERY (as order block)` — a candle's opening price that is traded through; not a zone.
`SMOOTH HIGHS / SMOOTH LOWS` — equal/flat highs or lows that are liquidity (also "smooth edges").
`MOC` — market on close; algorithmic last minutes of RTH.
`EVENT HORIZON LINE` — a midpoint-type target line mentioned for Bitcoin (caption unclear).
`BUY/SELL-SIDE EFFICIENCY` — wording used for DXY highs/lows being run (caption unclear).
