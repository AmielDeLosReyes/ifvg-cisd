# M22-019 — 2022 ICT Mentorship Episode 19
ID: IEa1N0rTtbc · URL: https://www.youtube.com/watch?v=IEa1N0rTtbc · Duration: 2:04:36
Content type: mixed (market review of DXY / EURUSD / GBPUSD / ES blended with lecture + long psychology segments)
Teaching density: medium (very long jaw-boning stretches, but the ES section from ~1:16:00 to ~1:49:00 is dense, key teaching on daily bias, midnight vs 8:30 opening price, Judas swing and purge-and-revert)

## Summary
ICT blends his private-mentorship midweek review with the YouTube episode (recorded the week after Passover, April 2022). He shows the 2022 model's "signature" (FVG, break of a low, retrace into the gap) on an hourly DXY chart to prove it is fractal and works across markets, defines an order block as a change in the state of delivery ("a bookmark" for the algorithm), and explains contrarian OTE trades against higher-timeframe bias (and why beginners should not take them). The core lesson is an ES case study (April 18–19, 2022): the daily chart retraced to equilibrium of its dealing range, so the next day was expected to be bullish toward a daily bearish order block and 15m relative equal highs; he explains buying below the New York midnight opening price, when to fall back to the 8:30 opening price, the Judas swing / Power of 3 and "purge and revert". He closes with a lot of process teaching: don't trade sloppy markets, don't trade every day, use realistic leverage, and write backtest annotations as positive reinforcement.

## Concepts

### Fair Value Gap — fractal "signature" of the 2022 model  (aliases: imbalance, fair value gap, "the gap")
- **Kind:** refinement / example
- **What ICT says:** The repeating signature he wants students to look for is: price creates a FVG, breaks a low (or high), comes back and fills the gap. It may partially fill, go halfway, or completely close it; you do not need pinpoint precision, an "average" entry with sound money management is enough. The same pattern he teaches on 1m–5m exists on the hourly chart; it applies to forex, bonds and futures, not just index futures.
- **How to identify:** Break in structure, then a FVG made by one candle (the gap between the candle before's low and candle after's high); look at candle *bodies*, allow wicks/tails to poke through ("the volume of the move is inside the bodies").
- **How to use:** The retrace into the gap typically lands near 50% of the "parent" price swing (the whole swing from the low to the high that produced the gap).
- **Example in this video:** DXY hourly at the 101 level: market drops, takes a swing low, leaves a FVG; price comes back up and the candle bodies respect the gap while wicks go slightly above it. Then it "breaks aggressively," runs stops below several lows, fills the gap and goes right below the low, which was ~50% (equilibrium) of the parent swing.
- **Timestamps:** [0:06:29](https://youtu.be/IEa1N0rTtbc?t=389) — the signature described; [0:10:27](https://youtu.be/IEa1N0rTtbc?t=627) — DXY hourly, bodies respecting the FVG = algorithmic delivery; [0:13:38](https://youtu.be/IEa1N0rTtbc?t=818) — hourly fractal of the YouTube model, 50% of parent swing; [0:15:14](https://youtu.be/IEa1N0rTtbc?t=914) — single-candle imbalance, bodies vs wicks.
- **Nuance / caveats / changes:** He stresses this is "algorithm delivering price," not supply/demand, harmonics or indicators.

### Order Block (bearish and bullish)  (aliases: OB, "up close candle", "down close candles", "bookmark")
- **Kind:** definition / refinement
- **What ICT says:** A bearish order block is the up-close candle(s) right before displacement lower; a bullish order block is the down-close candle(s) right before displacement higher. It is a *change in the state of delivery*: price was dropping, pauses with up-close candles, then resumes. The algorithm "bookmarks" that spot and refers back to it, like a bookmark in a book you return to and pick up the storyline. The displacement "qualifies" the order block because it creates a fair value gap. He says the order-block material sold by others (books on Amazon) is "completely wrong" and that he is withholding more order block theory for his book trilogy (volume 2).
- **How to identify:** Bearish: lowest up-close candle in the cluster before the down-move; use its *low* and its *opening price*, extend them forward in time. Multiple consecutive same-direction candles together form the block (two up-close candles on DXY 15m; three consecutive down-close candles on ES 1m). Must be followed by displacement that leaves a FVG.
- **How to use:** Levels within the block: candle low (easiest to reach for a bearish OB above price), the open/body, the **mean threshold** (50% / midpoint of the order block), and the high (least likely). As a target, pick the "lowest hanging fruit" (for a bearish OB above price, its low).
- **Example in this video:** DXY 15m: hourly FVG with an additional 15m imbalance inside; price comes up deeper, closes it in; two up-close candles before the drop = bearish OB; low of lowest up-close candle + its open, projected forward, "hammered it." ES 5m and 1m: down-close candles + FVG at the low of the day act as bullish OB entries (see ES case study).
- **Timestamps:** [0:20:47](https://youtu.be/IEa1N0rTtbc?t=1247) — DXY 15m bearish OB, low and open of lowest up-close candle; [0:23:08](https://youtu.be/IEa1N0rTtbc?t=1388) — OB = change in state of delivery, bookmark analogy; [0:25:29](https://youtu.be/IEa1N0rTtbc?t=1529) — displacement qualifies OB by creating FVG; [1:20:58](https://youtu.be/IEa1N0rTtbc?t=4858) — target levels inside the OB (low, open, mean threshold, high).
- **Nuance / caveats / changes:** He says the algorithm does not know where *your* stop is; it works off the common logic of stops placed/trailed just above recent short-term highs.

### Mean Threshold  (aliases: half of the order block, median of the order block)
- **Kind:** definition
- **What ICT says:** The mean threshold is the halfway point (median) of an order block. On the ES daily he draws it as the midpoint of the bearish OB candle and uses it on lower timeframes as one of the possible targets.
- **How to identify:** 50% of the order-block candle's range (he draws it from the daily up-close candle).
- **How to use:** Intermediate target between the OB's low/open and its high.
- **Timestamps:** [1:18:37](https://youtu.be/IEa1N0rTtbc?t=4717) — mean threshold defined on the ES daily OB.

### Trailing-stop liquidity above short-term highs  (aliases: buy stops above short-term high, trailing stop loss mentality)
- **Kind:** rule
- **What ICT says:** In a decline, shorts trail their stop to just above the most recent short-term high (because books teach it). So above the short-term high in a down-move there are buy stops; in an up-move, longs trail stops under recent lows. He is "not a big fan" of rushing his own stop for this reason.
- **How to use:** Treat those trailed-stop levels as liquidity targets. In the ES afternoon he points to a run down into sell stops of traders who trailed stops up before the final PM push.
- **Timestamps:** [0:24:41](https://youtu.be/IEa1N0rTtbc?t=1481) — trailing stops above short-term highs; [1:23:21](https://youtu.be/IEa1N0rTtbc?t=5001) — buy stops above the high of a down-move.

### Higher-timeframe bias vs. contrarian (counter-trend) trading  (aliases: institutional order flow, contrarian setups)
- **Kind:** rule / refinement
- **What ICT says:** Institutional order flow is rooted in higher-timeframe bias. Short-term counter-bias moves are part of natural retracements; you "can and will absolutely lose money" trading them as a new student, swinging buy/sell/buy/sell. Some of his students are naturally contrarian and pick spots where retail sees a reversal of the HTF bias (e.g., he is long-term bullish DXY; they short where retail thinks DXY has topped). That's fine because it matches their personality, but new students should learn to trust HTF bias first; if you are contrarian it will show over time.
- **How to use:** Don't try to pick tops/bottoms; there is plenty of opportunity between intermediate-term highs and lows. He doesn't mind missing the long-term high/low.
- **Timestamps:** [0:16:50](https://youtu.be/IEa1N0rTtbc?t=1010) — staying on right side of institutional order flow; [0:18:26](https://youtu.be/IEa1N0rTtbc?t=1106) — don't pick tops and bottoms; [0:25:29](https://youtu.be/IEa1N0rTtbc?t=1529) — counter-trend warning; [0:26:16](https://youtu.be/IEa1N0rTtbc?t=1576) — contrarian students.
- **Nuance / caveats / changes:** "I'm not teaching the trend is your friend": his frame is discount→premium / premium→discount within market structure, not trend-following indicators.

### Optimal Trade Entry (OTE) in a counter-trend retracement  (aliases: 62–79 retracement, short-term premium)
- **Kind:** example / refinement
- **What ICT says:** 62% and 79% retracement levels are the OTE range he teaches. In a contrarian long against a bearish bias, you can buy the low and simply target the 62% retracement level (or "above the bodies" of the candles in the prior down-move), keeping it easy. That's a "bread and butter" ~30–40 pip move.
- **Example in this video:** EURUSD hourly: daily low at 1.0806 + one pipette (1.08061) gets run on a slam lower (during Passover week); price rallies, creates a FVG, runs back toward old highs into the 62% retracement of the high-to-low (short-term premium). EURUSD 15m: displacement off the old daily low leaves a clean FVG; buy the retrace into it, sell at the hourly 62% retracement, ~30 pips.
- **Timestamps:** [0:47:41](https://youtu.be/IEa1N0rTtbc?t=2861) — EURUSD hourly, daily low 1.08061 swept; [0:48:28](https://youtu.be/IEa1N0rTtbc?t=2908) — OTE into short-term premium, contrarian; [0:49:15](https://youtu.be/IEa1N0rTtbc?t=2955) — 62 and 79 = OTE range, target 62%; [0:54:49](https://youtu.be/IEa1N0rTtbc?t=3289) — 15m version, ~30 pips, not recommended for new students.
- **Nuance / caveats / changes:** Explicitly "against the order flow"; something to backtest, not for developing students to trade live.

### Narrative after a liquidity run (sell-side taken → seek buy-side)  (aliases: draw on liquidity, short-term oversold)
- **Kind:** rule
- **What ICT says:** Once an old daily low is taken, the market is "short-term oversold on the daily"; sell stops/sell-side liquidity have been removed, so the market now looks for buy-side liquidity. An energetic displacement off that low that leaves a FVG is the algorithmic tell; a trade back down into the gap is a buy even though newer traders fear "it'll go below these equal lows."
- **How to use:** Buy the retrace into the displacement FVG; target the short-term high / above the bodies / 62% retracement.
- **Timestamps:** [0:53:15](https://youtu.be/IEa1N0rTtbc?t=3195) — EURUSD 15m clean FVG off old daily low; [0:54:02](https://youtu.be/IEa1N0rTtbc?t=3242) — narrative: SSL taken, now BSL.

### Consolidation → wait for displacement  (aliases: sideways consolidation, congestion, sloppy price action)
- **Kind:** rule
- **What ICT says:** When a market goes back into sideways congestion, he has no bias and waits for displacement in either direction to define a new range. After displacement, use the range: if it breaks lower, look for a retrace above 50% into the 62–79% premium; vice versa if it breaks higher. When charts are sloppy/back-and-forth (GBPUSD hourly and 15m in this video), there is "nothing" to trade; close the charts.
- **Example in this video:** EURUSD: price went below short-term lows, short-term break in structure, came back to fill the FVG, spent a lot of time there (holiday + new week, slow volume) and popped back into the range. GBPUSD: bearish below the FVG (invalidated if it trades above it), but hourly/15m have nothing worth trading; he hasn't traded cable for months.
- **Timestamps:** [0:50:52](https://youtu.be/IEa1N0rTtbc?t=3052) — no bias, wait for displacement; [0:51:41](https://youtu.be/IEa1N0rTtbc?t=3101) — 50% of range, 62–79 objective; [0:59:36](https://youtu.be/IEa1N0rTtbc?t=3576) — GBPUSD "nothing on this chart"; [1:09:54](https://youtu.be/IEa1N0rTtbc?t=4194) — manipulated market = rattlesnake, back away.
- **Nuance / caveats / changes:** Messy price means "heavily manipulated," not that the algorithm stopped working. Holiday weeks (Passover/Easter) leave money on the sidelines; give it a few days to a week to clean up.

### Swing low (3-candle definition) & Dealing range  (aliases: daily dealing range, range high/low)
- **Kind:** definition
- **What ICT says:** A swing low has a candle to its left with a higher low and a candle to its right with a higher low. The daily dealing range is drawn from the most recent swing low to the swing high of the move (he skips older relatively-equal lows and uses the swing where "this move started"). On the 15m he picks "the most energetic, most recent" low and the higher high above relative equal highs as the dealing range.
- **How to use:** Measure equilibrium (50%) of the dealing range; a retrace to ~50% = short-term discount (bullish bias for next day) or premium.
- **Timestamps:** [1:17:04](https://youtu.be/IEa1N0rTtbc?t=4624) — swing low definition, daily dealing range; [1:32:52](https://youtu.be/IEa1N0rTtbc?t=5572) — 15m dealing range choice.

### Daily bias from equilibrium of the dealing range  (aliases: daily bias, short-term discount)
- **Kind:** rule
- **What ICT says:** If the daily chart retraces to ~50% (equilibrium / short-term discount) of its dealing range, there's a likelihood the next day (or the day after) will be bullish. You go into the next day expecting higher prices; if the next day is down or flat you still expect higher. Then identify the premium array the market will draw to (e.g., a daily bearish order block above) and pick the easiest target.
- **How to identify:** Daily dealing range → 50% hit → look above for the premium PD array (OB low / open / mean threshold / high) and for old highs / relative equal highs.
- **How to use:** You're not predicting the daily close; you want to participate in the *morning-session* move in the bias direction into the target, not the whole leg.
- **Example in this video:** ES June 2022 daily: market traded into a deep discount, retraced to ~50% of the dealing range from the most recent swing low; next-day bias bullish; premium array = last up-close daily candle before the down-displacement (bearish OB), targets its low, body, mean threshold, high. Buying below the opening price on the bullish day could reach the candle's low (easiest), body, and the mean threshold.
- **Timestamps:** [1:18:37](https://youtu.be/IEa1N0rTtbc?t=4717) — equilibrium → bullish bias; [1:19:24](https://youtu.be/IEa1N0rTtbc?t=4764) — "you want to be taught about bias, I'm teaching it"; [1:20:10](https://youtu.be/IEa1N0rTtbc?t=4810) — premium array; [1:21:47](https://youtu.be/IEa1N0rTtbc?t=4907) — pick the easiest target.
- **Nuance / caveats / changes:** Even if the market eventually goes lower, the intraday "surgical strike" up into liquidity still works; he doesn't care about the longer-term direction for the intraday trade.

### Purge and Revert  (aliases: purge and revert, run on sell stops then revert to 3-day high)
- **Kind:** definition / model (refers to an older YouTube teaching)
- **What ICT says:** Price takes a short-term low (purges sell-side liquidity / sell stops) and then reverts back to the high of the last three days. The high of a three-day decline has buy stops resting above it (shorts' trailed stops). He tells viewers to search his channel for the original "purge and revert" video.
- **How to use:** After the purge of the short-term low, expect a draw back to the 3-day high (combined here with the daily OB target and the 15m relative equal highs).
- **Example in this video:** ES: on the 18th price took out a short-term low below old lows (≈50% of the daily range); counting day 1, 2, 3, the high three days back is the revert target, which coincides with the relative equal highs on 15m.
- **Timestamps:** [1:17:04](https://youtu.be/IEa1N0rTtbc?t=4624) — introduces purge and revert as a variation; [1:22:33](https://youtu.be/IEa1N0rTtbc?t=4953) — purged sell stops, revert to high of last three days; [1:48:02](https://youtu.be/IEa1N0rTtbc?t=6482) — confirmed on the ES outcome.

### Relative equal highs/lows as engineered liquidity  (aliases: relative equal highs, REH, engineered buy stops, "too clean" support/resistance)
- **Kind:** rule / example
- **What ICT says:** Two level highs = relative equal highs; they "engineer" buy stops because retail sees double-top resistance, shorts there with stops above, and treats the sideways drift as a bear flag (projecting a measured move lower). When it "looks too perfect, too pristine, too classic support/resistance," expect it to be run. Old highs/lows and relative equal highs/lows are the easiest, most visual targeting method; that logic will never change because stops always rest above old highs and below old lows.
- **Example in this video:** ES hourly/15m: two level highs above the consolidation = BSL; this became the day's target.
- **Timestamps:** [1:26:33](https://youtu.be/IEa1N0rTtbc?t=5193) — relative equal highs engineer buy stops; [1:27:20](https://youtu.be/IEa1N0rTtbc?t=5240) — retail sees resistance / bear flag / measured move; [1:48:49](https://youtu.be/IEa1N0rTtbc?t=6529) — Monday clip: "too perfect, too pristine"; [1:49:37](https://youtu.be/IEa1N0rTtbc?t=6577) — old highs/lows + REH/REL = easiest targeting.

### Smart-money order pairing  (aliases: offset, pairing orders, counterparty)
- **Kind:** rule (narrative logic)
- **What ICT says:** When price purges sell stops below old lows, smart money pairs their buy orders with those sell stops and is now net long. To get out they must sell to willing buyers at higher prices: the buy stops resting above old highs. So after sell-side is taken, the draw is to buy-side. Continuum: smart-money buys ↔ retail sells, smart-money sells ↔ retail buys. If you don't think about how orders are paired before you click "enter," you are gambling.
- **Timestamps:** [1:28:07](https://youtu.be/IEa1N0rTtbc?t=5287) — narrative: purge sell stops, net long, need buy-side; [1:28:54](https://youtu.be/IEa1N0rTtbc?t=5334) — "think algorithmically how you pair your orders"; [1:31:17](https://youtu.be/IEa1N0rTtbc?t=5477) — point of origin / terminus, SM vs retail order continuum.

### New York Midnight Opening Price vs. 8:30 Opening Price  (aliases: midnight open, midnight candle opening price, 8:30 open, "last ditch for Power of 3")
- **Kind:** rule / refinement (answers viewer confusion)
- **What ICT says:** Set TradingView to the New York time zone regardless of where you live. The New York midnight candle's opening price, extended forward, is the price he preferably wants to buy *below* when bullish (sell above when bearish). 8:30 ET is when the news embargo lifts; the 8:30 candle's opening price is the "last ditch" Power-of-3 reference. Rule: if bullish and the midnight opening price is *lower* than where price trades around/after 8:30 (price never comes back below midnight open), midnight isn't a factor, so use the 8:30 opening price. If price is below the midnight open and, after 8:30, also below the 8:30 open, the market is "really in a discount" and that is the "dandy," silver-platter setup.
- **How to identify:** Use the actual opening price of the 00:00 ET candle and the actual opening price of the 8:30 ET candle (wait for 8:30 exactly). He does *not* use the daily candle's opening price on TradingView (nothing inherently wrong with it, but for clarity and continuity he doesn't).
- **How to use:** Bullish day: buy below midnight open; best when price also drops below the 8:30 open into a FVG/OB taking short-term sell-side. Bearish day: mirror. No indicators, divergence or Fibonacci are needed to see the "oversold" condition.
- **Example in this video:** ES 15m/5m, April 19, 2022: price below the midnight open; at 8:30 price drops below the 8:30 open too, runs short-term swing lows into a bullish FVG + two down-close candles (OB), finds support at the 8:30 opening price, springs aggressively above short-term highs. Daily low ~4377 (caption "43.77"); the daily bar open on TradingView (~4404.5, caption unclear) differs from his midnight open.
- **Timestamps:** [1:25:43](https://youtu.be/IEa1N0rTtbc?t=5143) — introduces midnight and 8:30 opening prices; [1:34:28](https://youtu.be/IEa1N0rTtbc?t=5668) — set chart to New York, buy below midnight open, 8:30 = news embargo lifts; [1:36:52](https://youtu.be/IEa1N0rTtbc?t=5812) — the midnight-vs-8:30 decision rule; [1:44:52](https://youtu.be/IEa1N0rTtbc?t=6292) — doesn't use TradingView daily open, uses actual midnight and 8:30 candle opens.
- **Nuance / caveats / changes:** Clarifies earlier 2022 mentions of "opening price at midnight / 8:30" that confused viewers. You don't need the low of the day.

### Judas Swing & Power of 3 (daily and session level)  (aliases: Judas swing, micro Judas swing, AMD, accumulation-manipulation-distribution)
- **Kind:** definition / rule
- **What ICT says:** The Judas swing is the move opposite to what you expect the daily range to be; if bullish, you "love" the move down after midnight. You don't have to buy the London/overnight lows; you can wait for 8:30. A drop below the 8:30 opening price (after already being below midnight open) is a *micro* Judas swing for the New York session; the move below midnight open builds the low of the daily candle. Both are Power of 3 (accumulation, manipulation, distribution): each move below an opening price is "the trap / snare" catching traders who think it's going down.
- **How to use:** On a bullish day, look for that *specific* drop (below opens, into short-term sell stops and a FVG/OB) then expect displacement higher into liquidity; then offset, sell to buyers, move to the sidelines.
- **Example in this video:** ES: price moves from the range down after midnight (Judas swing of the day); then 8:30 drop below the 8:30 open (micro Judas), rally.
- **Timestamps:** [1:32:05](https://youtu.be/IEa1N0rTtbc?t=5525) — narrative steps: daily delivery, Judas swing, buy below opening, displacement, run into liquidity, offset; [1:38:29](https://youtu.be/IEa1N0rTtbc?t=5909) — Judas swing definition, don't need London lows; [1:39:15](https://youtu.be/IEa1N0rTtbc?t=5955) — micro Judas swing for NY session, Power of 3 AMD; [1:40:02](https://youtu.be/IEa1N0rTtbc?t=6002) — each move below opening price is the trap.

### ES case study, April 18–19, 2022 (full intraday sequence)  (aliases: "dandy of a setup")
- **Kind:** example only
- **What ICT says / what price did:**
  1. Daily: ES traded into deep discount, retraced ~50% of dealing range, purged short-term sell-side on the 18th. Monday evening (18th) he told the private group ES should go higher to the 15m relative equal highs.
  2. Hourly/15m: brutal back-and-forth consolidation; relative equal highs above = BSL target; dealing range = most recent swing low to the higher high above the REH.
  3. 5m: after midnight, price drops (Judas). At 8:30 price drops below the 8:30 open into a bullish FVG + two down-close candles (OB), taking short-term swing lows; rallies, returns to the 8:30 opening price for support, then springs above short-term highs ("by itself that's enough").
  4. Holding for the daily range: price reaches the target area; consolidates at lunch; around 2:00–3:00 pm runs down into sell stops of traders who trailed stops up; then pumps into the PM session up into the 15m relative equal highs.
  5. 1m "YouTube model" overlay: run above a short-term high = bullish market structure shift; FVG; trades down into it, three consecutive down-close 1m candles = OB + FVG → buy; retests; retraces up into the NY midnight opening price, back into another gap and its midpoint; rallies, consolidates, expands into the 15m REH.
  6. At the 9:30 equities open another opportunity forms: OTE retrace, then rally up the daily range to the candle high that equals the 15m REH. Low of day ≈4377.
- **Timestamps:** [1:24:09](https://youtu.be/IEa1N0rTtbc?t=5049) — ES June contract hourly; [1:40:55](https://youtu.be/IEa1N0rTtbc?t=6055) — 5m FVG + OB at 8:30; [1:41:43](https://youtu.be/IEa1N0rTtbc?t=6103) — lunch, 2–3pm stop run, PM push to REH; [1:43:19](https://youtu.be/IEa1N0rTtbc?t=6199) — 1m MSS + FVG + 3 down-close OB entry; [1:47:15](https://youtu.be/IEa1N0rTtbc?t=6435) — 9:30 open OTE.
- **Nuance / caveats / changes:** "We're looking for surgical strikes intraday"; you don't need the low of the day.

### Intermarket: DXY as the anchor for FX bias  (aliases: dollar index, bullish dollar)
- **Kind:** rule / example
- **What ICT says:** Bullish DXY = bearish EURUSD, GBPUSD and all foreign currencies vs USD. His DXY targets were the 100 level, 101, 101.947 and just short of 103 (rounded to 103). Treats the drop from 101 as a retracement, not a top; would change his mind only if price goes below "these lows" (and even then it would take time). If he were making the market he'd take DXY just below 100 (~99.95/99.92) to convince everyone it topped, then reverse it higher.
- **Timestamps:** [0:08:02](https://youtu.be/IEa1N0rTtbc?t=482) — DXY daily targets; [0:19:13](https://youtu.be/IEa1N0rTtbc?t=1153) — bullish dollar = bearish all foreign currencies; [0:20:01](https://youtu.be/IEa1N0rTtbc?t=1201) — how he'd engineer a fake top below 100.
- **Nuance / caveats / changes:** Don't take one sentence of his as a sentiment justification for your own trade.

### Asset-class rotation & sloppy markets  (aliases: "salad days", forex is asleep)
- **Kind:** rule
- **What ICT says:** Forex was quiet (supply-chain/trade disruption) so he wasn't trading it; index futures had been the mover; May can get dry/bearish. Navigate to the asset class where the excitement is. A market that's sloppy/manipulated is a rattlesnake: don't touch it. His motto "every week, every day" does not mean every market every day; it may be futures one day, forex or bonds another.
- **Timestamps:** [0:39:47](https://youtu.be/IEa1N0rTtbc?t=2387) — forex quiet; [1:02:46](https://youtu.be/IEa1N0rTtbc?t=3766) — "salad days" coming; [1:37:40](https://youtu.be/IEa1N0rTtbc?t=5860) — every week every day ≠ every market.

### Old-low draw on liquidity (EURUSD daily)  (aliases: DOL, run on old low)
- **Kind:** example only
- **What ICT says:** EURUSD daily: he had pointed YouTube viewers to an old low as the draw on liquidity; price consolidated for several days, then whipped below it (breakout shorts below the low were squeezed the same day), and spent ~5 daily candles below the old low before coming back up. Up-close candles in that decline were just opportunities to short. This "reaching for that low" is what he'll do in the live streams on intraday charts.
- **Timestamps:** [0:41:22](https://youtu.be/IEa1N0rTtbc?t=2482) — draw on liquidity below the low; [0:42:09](https://youtu.be/IEa1N0rTtbc?t=2529) — five days below the old low; [0:46:05](https://youtu.be/IEa1N0rTtbc?t=2765) — up-close candles = opportunities to short.

## Rules, checklists & numbers stated
- Retrace into the FVG often ≈ 50% of the parent swing; partial / half / full fill all acceptable — precision not required.
- Bearish OB: low and opening price of the lowest up-close candle before displacement; displacement must create a FVG to qualify it.
- OB target ladder: low → open/body → mean threshold (50%) → high; take the easiest one as a developing student.
- OTE = 62% and 79% retracement; for a quick counter-trend scalp, target the 62% or "above the bodies."
- Swing low: candle to left and candle to right both have higher lows.
- Daily retrace to equilibrium (50%) of dealing range → expect next day bullish (mirror for bearish).
- Purge and revert: purge short-term SSL → revert to the high of the last three days.
- Always set TradingView to New York time.
- Bullish: buy below the NY midnight opening price; if price is above midnight open around/after 8:30, use the 8:30 opening price instead; below both = deep intraday discount. Use actual 00:00 and 8:30 candle opens, not the TradingView daily open.
- 8:30 ET = news embargo lifts; "last ditch" for Power of 3.
- Judas swing = move opposite the expected daily range; drop below 8:30 open = micro Judas for NY session.
- Afternoon pattern seen: lunch consolidation, ~2:00–3:00 pm run into trailed stops, then PM-session expansion into the target.
- Stops rest above old highs (buy stops) and below old lows (sell stops) — "always will be that way."
- Don't trade sloppy/consolidating markets; after holidays (Passover/Easter) allow a few days to a week for volume to return.
- DXY levels mentioned: 100, 101, 101.947, ~103; EURUSD daily low 1.08061; ES low ≈4377.

## Process, risk & psychology
- Coin-flip demo experiment: flip a coin daily, heads buy / tails sell at the open, 30-pip stop on a forex pair, risk ≤0.5%, aim for 1%; shows how hard it is to blow an account with sound money management. Profitability comes from rule adherence, money management, not over-trading/over-leveraging. [0:34:17](https://youtu.be/IEa1N0rTtbc?t=2057)
- Refine everything into a "recipe" (algorithm): which days of the week, what time of day, which asset class, which market, bullish or bearish. [0:35:04](https://youtu.be/IEa1N0rTtbc?t=2104)
- Position traders (no time for intraday) can use daily/4h charts; it's slower. [0:38:12](https://youtu.be/IEa1N0rTtbc?t=2292)
- You must learn to tape read; profits without it are circumstance/luck (his 1990s bull-market experience). [0:42:57](https://youtu.be/IEa1N0rTtbc?t=2577)
- Don't expect a setup you saw once to work every day between 8:30 and 11:00. It takes more than 40/120 days or a year; treat trading as a business. [0:55:37](https://youtu.be/IEa1N0rTtbc?t=3337)
- Knowing when *not* to trade prevents blown accounts, removes FOMO; you don't need to trade every day — you need an expectation of where price is going; if you can't outline it, you're gambling. [1:03:35](https://youtu.be/IEa1N0rTtbc?t=3815)
- Trade one contract, lowest leverage, aim to double the account; rushing = gambling = blown account. [1:05:13](https://youtu.be/IEa1N0rTtbc?t=3913)
- One bread-and-butter setup a week is enough; money management does the heavy lifting; going two weeks without a trade is fine, don't system-hop. [1:11:33](https://youtu.be/IEa1N0rTtbc?t=4293)
- Time and price only: ask where price was an hour ago, last Friday, where it's likely to go today and by end of week. [1:13:08](https://youtu.be/IEa1N0rTtbc?t=4388)
- Have a hobby/outlet to avoid burnout; be accountable to someone; join a like-minded community. [1:01:10](https://youtu.be/IEa1N0rTtbc?t=3670)
- Focus on points/pips and managing risk, not money; use realistic leverage even in demo — over-leveraged paper trades condition you to ignore drawdown and chase "clout." [1:54:24](https://youtu.be/IEa1N0rTtbc?t=6864), [1:59:58](https://youtu.be/IEa1N0rTtbc?t=7198)
- Backtesting annotations: write them as if you saw the trade beforehand, always positive (e.g., "it felt good to see this deliver from this FVG to this BSL pool during these hours as my model says"); never write self-criticism in the backtest journal. This builds positive "pseudo memories" so you don't freeze live. [1:55:11](https://youtu.be/IEa1N0rTtbc?t=6911), [1:56:46](https://youtu.be/IEa1N0rTtbc?t=7006)

## Glossary candidates
`Mean threshold` — 50% / median of an order block.
`Change in the state of delivery` — where price delivery flips direction; the order block marks it.
`Purge and revert` — run of short-term sell stops followed by reversion to the high of the last three days (and mirror).
`Relative equal highs/lows` — roughly level highs/lows that engineer resting stops.
`Micro Judas swing` — the session-level fake move below the 8:30 opening price (inside the daily Judas).
`Last ditch for Power of 3` — the 8:30 opening price as the final reference when midnight open isn't usable.
`Parent price swing` — the full swing whose 50% the FVG retrace tends to reach.
`Salad days` — easy, clean trading conditions when an asset class comes alive.
`Bread and butter setup` — a simple repeatable ~30-pip / modest move setup.
`Surgical strike` — a precise intraday trade into a defined liquidity target.
