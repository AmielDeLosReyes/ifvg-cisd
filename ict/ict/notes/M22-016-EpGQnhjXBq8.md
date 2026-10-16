# M22-016 — 2022 ICT Mentorship Episode 16
ID: EpGQnhjXBq8 · URL: https://www.youtube.com/watch?v=EpGQnhjXBq8 · Duration: 50:56
Content type: lecture (built around one Friday of ES price action)
Teaching density: high

## Summary
ICT answers "what do you mean by multiple setups per session?" using a single Friday on the E-mini S&P June 2022 contract (ES). He frames the day top-down: daily run above relative equal highs, a 3-candle swing high, Power of 3 with a manipulation above the midnight/8:30 opening price, and a draw to relative equal lows plus a daily bullish order block at 4504. He then teaches his **body-based Fibonacci swing projection** (anchor on the highest/lowest candle bodies, not wicks), which projected 4501.25 — the exact daily low. On 15m/5m/1m he walks through 3–4 morning short setups (each a short-term low broken → FVG → retrace → short, targeting the next low), partials and lunch-hour rules, then the PM reversal: the Friday "PM session buy-side liquidity pool," discount-to-premium repricing, mitigation block and old-high-as-support longs, and a final MSS short. Closes with heavy backtesting/journaling advice, rejection of the DOM and "buying/selling pressure," and the "unique model" idea.

## Concepts

### Swing high / swing low (3-candle definition)
- **Kind:** definition
- **What ICT says:** A swing high is a candle with a lower high on the candle before and the candle after. Not to be confused with an MT4 fractal — that takes more candles (five), and "five candles later... you've already missed the move."
- **How to use:** Once the swing-high candle's following candle closes (on the daily, "this candle closes the next day"), start looking for a short opportunity.
- **Example in this video:** ES M2022 daily: price ran above relative equal highs (BSL), then printed a 3-candle swing high; next day (Friday) he looks for shorts.
- **Timestamps:** [0:01:00](https://youtu.be/EpGQnhjXBq8?t=60) — run above relative equal highs, swing high. [0:01:50](https://youtu.be/EpGQnhjXBq8?t=110) — not an MT4 fractal.

### Power of 3 / AMD with opening prices (midnight and 8:30)
- **Kind:** rule
- **What ICT says:**
  - Anticipate an open, a rally (manipulation), then distribution — accumulation, manipulation, distribution — combined with premium/discount analysis.
  - For index futures there are two opening prices: **midnight New York** and **8:30 a.m.** (the open of whatever candle begins at 8:30 — 1m, 3m, 15m, hourly; "it doesn't matter what candle you use").
  - If bearish, ideally price trades **above** the opening price — that's the manipulation, a Judas swing ("market protraction"): price going opposite to where it will go later in the day.
- **How to identify:** Bearish daily bias; mark midnight and 8:30 opens; look for the rally above them into a premium PD array.
- **How to use:** Sell after the run above the opening price once structure breaks and a FVG retrace occurs.
- **Example in this video:** ES Friday: price traded higher in the morning above the opening price, then broke lower attacking sell-side liquidity and ran into the daily bullish order block.
- **Timestamps:** [0:01:50](https://youtu.be/EpGQnhjXBq8?t=110) — Power of 3. [0:04:58](https://youtu.be/EpGQnhjXBq8?t=298) — two opening prices: midnight and 8:30. [0:05:45](https://youtu.be/EpGQnhjXBq8?t=345) — bearish: trade above the opening price = manipulation / Judas.
- **Nuance / caveats / changes:** Clarifies student confusion: any timeframe's 8:30 candle open is fine.

### Order block (daily bullish order block as draw / discount array)
- **Kind:** rule (applied)
- **What ICT says:** In a premium after a run above old highs, the down-close candle below is the bullish order block — a likely target if price goes lower. Its level is the **opening price of the down-close candle**, extended out in time onto lower timeframes. Relative equal lows above it add sell-side liquidity: SSL "by itself... is likely, but it's further likely if we have a discount array."
- **Example in this video:** ES daily bullish order block at **4504** (open of the down-close candle). Relative equal lows on the hourly sat above it. Price ran the lows and tapped the OB; the reaction was strong.
- **Timestamps:** [0:02:36](https://youtu.be/EpGQnhjXBq8?t=156) — down-close candle as bullish OB. [0:03:24](https://youtu.be/EpGQnhjXBq8?t=204) — level 4504; relative equal lows. [0:07:19](https://youtu.be/EpGQnhjXBq8?t=439) — OB level extended onto the hourly; reaction.

### Fibonacci swing projection on candle bodies ("fulcrum point" targeting)
- **Kind:** entry model / refinement (targeting)
- **What ICT says:**
  - When structure has shown a willingness to go lower — swing low "decisively broken," then a retrace into the FVG — the broken low is a **fulcrum point**. Measure from the swing high down to that low and project the same distance lower ("this is my swing trading model and I'm applying it to targeting").
  - Anchor the Fibonacci on the **highest body** (open or close, doesn't matter which) of the swing high and the **lowest body** (open or close) of the swing low — not the wicks. "The wicks and the tails are all distractions"; this is how the algorithm reads price. He learned it in forex and says it carries over to index futures; it was less pure in the open-outcry era.
  - Using wick high to wick low will not give the measurement — "that's why everybody that uses Fibonacci struggles."
  - Precision only helps when the narrative is already in place (liquidity + discount array); otherwise "a thousand lines on your chart" will hit something.
- **How to identify:** Displacement breaks a swing low; retrace into FVG; measure the bodies of that high-to-low swing.
- **How to use:** Use the projections as targets; choose the one that confluences with the HTF draw (OB / below relative equal lows).
- **Example in this video:** ES 15m, Friday morning: projection levels **4514.50** (first) and **4501.25** (next). 4501.25 sits just below the daily OB at 4504 — and the actual daily low was exactly **4501.25**. Exact Fibonacci extension settings were shown on screen, not spoken.
- **Timestamps:** [0:08:06](https://youtu.be/EpGQnhjXBq8?t=486) — swing low broken, retrace into FVG, fulcrum point. [0:08:53](https://youtu.be/EpGQnhjXBq8?t=533) — anchor on highest/lowest bodies. [0:10:29](https://youtu.be/EpGQnhjXBq8?t=629) — targets 4514.5 and 4501.25. [0:12:05](https://youtu.be/EpGQnhjXBq8?t=725) — daily low 4501.25 exactly.
- **Nuance / caveats / changes:** Explicitly contrasts with standard wick-anchored Fibonacci use. "You can't predict daily highs and lows" — he says you can, if you understand the algorithm's elements.

### Daily bias framed on the daily chart
- **Kind:** rule
- **What ICT says:** "The majority of your analysis should be framed on your daily chart" — where is the expansion likely to take price, higher or lower? That carves out your bias. The daily draw (OB at 4501.25/4504) doesn't need to be hit yet; you know it's the draw.
- **Timestamps:** [0:14:32](https://youtu.be/EpGQnhjXBq8?t=872).

### Bearish setup checklist (15m) — displacement, MSS, FVG, above opening price
- **Kind:** rule / checklist
- **What ICT says:** Build-up into premium; market breaks aggressively (displacement down); did it take out the swing low? yes; did it trade back up into the imbalance? yes; did it trade above the opening price? yes — "probabilities are now going through the roof." Then price traded to the old swing low (SSL), through it, aggressively rebalanced the down move back into a bearish order block, sold off again, into and past lunch to the daily bullish OB.
- **Example in this video:** ES 15m Friday; the 9:30 retrace into the 15m FVG was the main entry.
- **Timestamps:** [0:15:19](https://youtu.be/EpGQnhjXBq8?t=919), [0:16:06](https://youtu.be/EpGQnhjXBq8?t=966).

### Higher-timeframe FVG as framework for lower-timeframe entries
- **Kind:** refinement
- **What ICT says:** On the 5m, the return into the 15m FVG at 9:30 "does not look clean"; you might not see it as a sell because it wasn't filled on the 5m. The 15m provides the framework/context — "we don't need it to trade up into that [fully]." On the 1m, a small FVG right above a short-term high was the setup.
- **Timestamps:** [0:17:41](https://youtu.be/EpGQnhjXBq8?t=1061) — 5m vs 15m. [0:19:17](https://youtu.be/EpGQnhjXBq8?t=1157) — 1m view of the same retrace.

### Multiple setups per session (morning session)
- **Kind:** rule / example
- **What ICT says:**
  - Split day: morning session 8:30 a.m.–noon; NY lunch noon–1:00 p.m.; PM session after.
  - Max four trades: two in the morning, two in the afternoon (from his "real money, real results" series).
  - Morning typically offers **2–3 setups** because volatility comes in at the 9:30 open; the open is tricky — you can get caught offside. He prefers students wait for the initial move to "qualify" the expected direction.
  - Repeating pattern: short-term low broken with displacement → FVG → return into FVG → short → target the broken short-term low (fulcrum) / next SSL.
- **Example in this video (ES 1m, Friday morning, bearish):**
  1. First FVG after a short-term low broken with energetic displacement; short on the return; first objective the fulcrum short-term low. E.g. 2 contracts: take 1 off there, let the other ride toward the lower-timeframe objective (daily OB) later in the day.
  2. Another short-term low taken, FVG, retrace into it → short; target the run below the next low.
  3. Another imbalance after an aggressive move lower; retrace came close to the stop of the earlier short.
  4. A shallow run below an old low → anticipate a deeper run; take a partial below that low.
- **Timestamps:** [0:00:10](https://youtu.be/EpGQnhjXBq8?t=10) — sessions and lunch. [0:16:54](https://youtu.be/EpGQnhjXBq8?t=1014) — max four trades, 2 AM / 2 PM. [0:18:28](https://youtu.be/EpGQnhjXBq8?t=1108) — 2–3 setups in morning; qualify the initial move. [0:22:33](https://youtu.be/EpGQnhjXBq8?t=1353) — walkthrough of setups 1–2. [0:26:29](https://youtu.be/EpGQnhjXBq8?t=1589) — setup 4, re-entry after missed entries.
- **Nuance / caveats / changes:** Some days have only one or two retracements, or the move happens right at the open and you miss it — be happy your analysis was right.

### Lunch hour rule & partials
- **Kind:** rule
- **What ICT says:** He doesn't take entries during lunch (noon–1:00 p.m. NY) but profits can be taken then. A limit order at the order-block level "plus a couple points" can fill during lunch; no need to babysit once the position is funded (one contract off, stop to break-even).
- **Timestamps:** [0:22:33](https://youtu.be/EpGQnhjXBq8?t=1353), [0:23:21](https://youtu.be/EpGQnhjXBq8?t=1401).

### Index futures vs forex delivery
- **Kind:** rule / opinion
- **What ICT says:** Index futures are more precise and uniform — everyone works with the same price; many of his trades came within a quarter point of his stop without hitting it. In forex you trade in your broker's in-house liquidity pool and they can widen spreads. Forex is "quiet" now; he tells students (private and YouTube) to follow index futures until currencies loosen up.
- **Timestamps:** [0:24:55](https://youtu.be/EpGQnhjXBq8?t=1495), [0:25:42](https://youtu.be/EpGQnhjXBq8?t=1542).

### PM session buy-side liquidity pool (Friday reversal / position squaring)  (new coinage: "PM session buy-side liquidity pool")
- **Kind:** new coinage / rule
- **What ICT says:**
  - The pink-box zone above the **most energetic high of the morning session** — the high that launched price down to the daily target.
  - Because it's Friday, the daily objective has been hit, price is in a discount and has traded to the lower end of the week, expect a retracement back into the weekly range: position squaring / short covering by smart money that sold all morning. Shorts holding over the weekend put stops above that high → liquidity.
  - Retail sees relative equal lows broken ("support broken") and sells when price returns to them; smart money buys from those sellers — "engineering buy-side liquidity on the basis of sell-side flow."
  - Premium for the PM: take the morning high (the 8:30/9:30 rotation high — either works) down to the low; above 50% = premium; the PM draw is into that premium.
- **How to use:** Look for longs in the PM targeting the buy stops above the morning's energetic high.
- **Example in this video:** ES Friday PM: after tagging the daily OB, price repriced from discount to premium into the pink buy-side pool.
- **Timestamps:** [0:28:05](https://youtu.be/EpGQnhjXBq8?t=1685) — defines the pink rectangle. [0:28:52](https://youtu.be/EpGQnhjXBq8?t=1732) — Friday, weekly range retracement, weekend-hold stops. [0:29:42](https://youtu.be/EpGQnhjXBq8?t=1782) — 50% of the morning high-to-low = premium. [0:32:49](https://youtu.be/EpGQnhjXBq8?t=1969) — short covering; engineering BSL on sell-side flow.
- **Nuance / caveats / changes:** He personally won't hold index positions over the weekend (gap risk).

### Algorithm summary: discount ↔ premium, liquidity, imbalance, time then price
- **Kind:** rule
- **What ICT says:** The algorithm seeks discount to premium and premium to discount; within that it reaches for liquidity (buy stops / sell stops) and/or imbalances (creating FVGs or returning to them) — on the basis of **time, then price**. He calls it a gross oversimplification but "by and large that's all these things do." All you need: liquidity, imbalances, time of day.
- **Timestamps:** [0:30:28](https://youtu.be/EpGQnhjXBq8?t=1828), [0:42:19](https://youtu.be/EpGQnhjXBq8?t=2539).

### Mitigation block (PM long)
- **Kind:** example
- **What ICT says:** Market structure breaks (to the upside), price comes back down into the mitigation block which also has an imbalance/FVG → be a buyer, aim for the buy stops in the PM pool. He references levels 4532 and 4540 as the price ranges to think about (relation to the earlier chart).
- **Timestamps:** [0:34:23](https://youtu.be/EpGQnhjXBq8?t=2063), [0:35:09](https://youtu.be/EpGQnhjXBq8?t=2109).

### Old high as support (old highs become a discount array)
- **Kind:** rule
- **What ICT says:** If price trades above an old high, that old high becomes a discount array — broken old highs can act as support ("not all the time"). What makes them real support/resistance is the narrative: when you know price is drawing up to buy stops, a retest of a broken old high that also fills an imbalance is a buy.
- **Example in this video:** ES PM: price traded back down, hit an old high to the left and filled an imbalance, then ran up to the pink BSL area.
- **Timestamps:** [0:35:09](https://youtu.be/EpGQnhjXBq8?t=2109), [0:35:58](https://youtu.be/EpGQnhjXBq8?t=2158) — "something for your notes."

### Market structure shift + stacked FVGs (confirmation entry)
- **Kind:** rule / entry model
- **What ICT says:** After filling buy-side liquidity in the pink area, price breaks a swing low (MSS); short on the retrace into the FVG aiming for the low or the order block. Or wait for a confirmation entry: after hitting the FVG it breaks lower again, another 1m structure break with an imbalance. Rule restated: **if you have an FVG with a small FVG right above it, anticipate price trading up into the upper one** — use it as the entry; target the order block.
- **Timestamps:** [0:36:47](https://youtu.be/EpGQnhjXBq8?t=2207), [0:37:34](https://youtu.be/EpGQnhjXBq8?t=2254).

### "Buying and selling pressure" myth / DOM
- **Kind:** rule / opinion
- **What ICT says:** He doesn't trade with the DOM — spoofing means resting orders may not be there; he sees no advantage in it (but won't argue if it works for you). Price doesn't need volume to move: a candle can be created with two transactions — price reprices/gaps to a level and one market order trades there.
- **Timestamps:** [0:31:14](https://youtu.be/EpGQnhjXBq8?t=1874), [0:43:54](https://youtu.be/EpGQnhjXBq8?t=2634).

### Unique model / fractal setups
- **Kind:** rule
- **What ICT says:** Your unique model is a setup so similar every time it repeats the same idea on a different chart, day, or timeframe. Traders using the same concepts can take opposite trades on the same day. Everything is fractal — 30-second and 15-second charts show even more setups; staying on a 15m chart and trading the daily range is fine.
- **Timestamps:** [0:47:05](https://youtu.be/EpGQnhjXBq8?t=2825), [0:47:54](https://youtu.be/EpGQnhjXBq8?t=2874).

### Risk management — pyramiding
- **Kind:** rule
- **What ICT says:** Biggest position first, then smaller adds (e.g. 5, then 3, then 2), roll into the objective — gives equity velocity. Buying 1, 2, 4, 8 is reckless; he has "roasted accounts" doing it.
- **Timestamps:** [0:48:41](https://youtu.be/EpGQnhjXBq8?t=2921), [0:49:28](https://youtu.be/EpGQnhjXBq8?t=2968).

## Rules, checklists & numbers stated
- Swing high = 3 candles (lower high each side); not a 5-candle MT4 fractal.
- Opening prices for index futures: midnight NY and 8:30 a.m. NY (any timeframe candle opening at 8:30).
- Bearish day: want price to trade above the opening price first (manipulation/Judas).
- Daily OB level = open of the down-close candle; ES daily OB = 4504.
- Fib projection: anchor on highest body / lowest body (open or close), project the high-to-fulcrum-low distance; ES targets 4514.50 and 4501.25 (daily low = 4501.25).
- Bearish 15m checklist: displacement down, swing low taken, retrace into FVG, traded above the opening price.
- Sessions: AM 8:30–12:00; lunch 12:00–1:00 p.m.; PM after 1:00 p.m. No entries at lunch; exits/limit fills OK.
- Max 4 trades per day: 2 AM, 2 PM. Morning usually 2–3 setups.
- 2 contracts: 1 off at first target (fulcrum low), stop to break-even, runner to HTF objective; limit at OB level + a couple of points.
- PM premium: morning high to low, above 50% = premium.
- Old highs broken can act as support when narrative points higher.
- FVG with a small FVG above it → expect the upper one to be reached.
- Pyramid 5/3/2; never 1/2/4/8.
- Backtest/annotate for at least a year minimum.
- Live account up another $1,000 → over $51,000.

## Process, risk & psychology
- Pause the video and work the chart yourself — "don't Netflix binge-watch ICT"; active participation is the best way to learn. [0:20:09](https://youtu.be/EpGQnhjXBq8?t=1209)
- You don't need the perfect entry at the open; later setups let you get in line with the market. [0:20:56](https://youtu.be/EpGQnhjXBq8?t=1256)
- Missed trades are like scheduled buses — you have "no right to be angry"; focus on where price is likely to reach. [0:27:16](https://youtu.be/EpGQnhjXBq8?t=1636)
- Understanding makes it easy to know what to look for — not "easy to make money"; that follows over time. [0:28:05](https://youtu.be/EpGQnhjXBq8?t=1685)
- Won't hold over the weekend — gap risk. [0:28:52](https://youtu.be/EpGQnhjXBq8?t=1732)
- Backtesting: annotate charts in the empty space, type out the logic; it's discovery, not doing it correctly; if you can't see repetition, go back to the core concept lessons. Minimum one year; keep annotating even when trading live. [0:38:21](https://youtu.be/EpGQnhjXBq8?t=2301), [0:39:58](https://youtu.be/EpGQnhjXBq8?t=2398), [0:40:46](https://youtu.be/EpGQnhjXBq8?t=2446)
- Journal "self-talk": write annotations as if you foresaw the move; review them during drawdowns for encouragement. Never write negative comments ("I was stupid") — positive reinforcement only. [0:40:46](https://youtu.be/EpGQnhjXBq8?t=2446), [0:41:32](https://youtu.be/EpGQnhjXBq8?t=2492)
- Holding through a near-stop retrace is scary with size; if you follow the model you don't move your stop. [0:24:55](https://youtu.be/EpGQnhjXBq8?t=1495)
- Give it a couple of months of focused study; you don't need all answers now. [0:50:16](https://youtu.be/EpGQnhjXBq8?t=3016)

## Glossary candidates
`Fulcrum point` — the broken swing low (or high) used as the pivot for a measured swing projection.
`Body-anchored Fib` — Fibonacci drawn from the highest/lowest open-or-close, ignoring wicks.
`PM session buy-side liquidity pool` — buy stops above the morning's most energetic high, a Friday-afternoon draw after the daily objective is met.
`Opening price (index futures)` — midnight NY open and the 8:30 a.m. candle open.
`Market protraction` — the early opposing move (Judas swing) before the real daily direction.
`Engineering liquidity on sell-side flow` — retail sells broken "support"; smart money buys from them to reach buy stops.
`Position squaring` — late-week profit-taking/short-covering that causes a retracement.
`Unique model` — your personal repeatable setup built from ICT concepts.
