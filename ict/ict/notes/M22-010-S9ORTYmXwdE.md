# M22-010 — 2022 ICT Mentorship Episode 10
ID: S9ORTYmXwdE · URL: https://www.youtube.com/watch?v=S9ORTYmXwdE · Duration: 1:06:46
Content type: lecture (with market review of Thu 17 Feb 2022 and a paper-trading demo)
Teaching density: high

## Summary
Episode 10, "Implementing economic calendar events with the open", is ICT's core statement on daily bias. Bias is simply whether the daily range is more likely to expand above or below the opening price, read through Power of Three on the daily candle. He walks through daily OHLC bars, counting how few opposite-colored candles appear in sustained swings. He defines a 3-candle swing low and rejects the Williams fractal. He then defines the **opening range** as the distance from the open to the manipulation high, projected below the open. Every short setup (FVG, stop raid, OTE) should form inside that range, which gives "close-proximity entries". Intraday he uses the midnight New York opening price, the 8:30 news embargo (price pumping into premium before bearish news), and the 15m "bellwether" chart. He also gives the top-down FVG search rule (5m, then 4m, 3m, 2m, 1m; stop at the first FVG; none means no trade), a bearish breaker stop rule, and a "lowest-threshold" entry. He closes with margin and leverage warnings, a paper-trading demonstration, and mindset ("traders are professional losers").

## Concepts

### Economic calendar and the 8:30 a.m. news embargo
- **Kind:** rule
- **What ICT says:**
  - Check the economic calendar every day you trade, or you may be surprised by volatility. He uses forexfactory.com (any calendar works). Red = high impact, orange = medium, yellow = low.
  - 8:30 a.m. ET is the crosshair time because the news embargo lifts then and many releases hit the market.
  - Releases can be a smoke screen or a catalyst. Often price builds up (or drops) right before the report, then the real move follows.
  - If price pumps higher ahead of the 8:30 release on a bearish-bias day, it's "tipping its hand". Price is being driven into a premium before the news so the news can be used to sink it. Shorts have already been accumulated above the opening price.
- **Example in this video:** Thu 17 Feb 2022 calendar (several medium-impact events). NQ rallied ahead of 8:30, then sold off with the bearish daily bias.
- **Timestamps:** [0:00:54](https://youtu.be/S9ORTYmXwdE?t=54) — ForexFactory, colour codes · [0:01:42](https://youtu.be/S9ORTYmXwdE?t=102) — 8:30 embargo; buildup before the report, then the real move · [0:36:11](https://youtu.be/S9ORTYmXwdE?t=2171) — pricing in a premium ahead of the news to sink it

### Daily bias = will the daily range expand above or below the open  (aliases ICT uses: the key to bias)
- **Kind:** definition / rule
- **What ICT says:**
  - The most-requested question over the years is how to find daily bias. He says this is "really all I teach my students", with nothing more secret than this.
  - You only need to know whether the daily range is more likely to expand higher or lower than the opening price. Predicting the close is "more advanced" and not needed to be profitable.
  - Bearish day: open, a rally (small, or even a large wick), down, close near the low. Bullish day: the reverse.
  - Not every candle in a swing conforms. In sustained HTF swings there are few opposite candles. Don't let one counter day knock you out of your bias.
  - Once bias is set (e.g. bearish after a daily MSS and a retrace into a FVG), "any rally or up-close candle should be viewed as a potential shorting candidate".
  - Stay with the bias until the draw (e.g. relative equal highs, BSL) is reached. Then study whether it wants to continue.
- **How to identify:** daily structure (swing points), daily FVG and premium/discount, the draw on liquidity.
- **How to use:** Each day, expect a Power-of-Three candle in the bias direction. Losses on counter days are expected. Keep the bias until the target liquidity is taken.
- **Example in this video:**
  - NQ daily (1992-style OHLC bars, then candles). Bullish sequence:
    - A 3-bar swing low forms. The next day washes out below the open and closes on its high.
    - The following day is expected to rally into the FVG above (bullish bias).
    - Price then retraces below equilibrium of the swing into discount, followed by a series of open-near-low, close-near-high days.
    - It keeps reaching for relative equal highs (BSL). Bias stays bullish until above them.
  - Bearish sequence: the rally into a daily FVG, then open-rally-close-on-low days toward sell-side lows, then a potential key reversal and chop.
  - Current context: NQ traded up to the top of the daily FVG (from Ep. 9), the bias is bearish, and the targets are the lows below.
- **Timestamps:** [0:03:18](https://youtu.be/S9ORTYmXwdE?t=198) — "number one question": daily bias · [0:06:31](https://youtu.be/S9ORTYmXwdE?t=391) — rallies are shorting candidates · [0:17:44](https://youtu.be/S9ORTYmXwdE?t=1064) — expand higher or lower than the open is "the key to bias" · [0:20:57](https://youtu.be/S9ORTYmXwdE?t=1257) — daily bullish Power-3 sequence to relative equal highs
- **Nuance / caveats / changes:** Simplifies the "draw on liquidity" framing from Ep. 7 into the open-relative expansion question.

### Power of Three on the daily candle (AMD components, precise)
- **Kind:** definition
- **What ICT says (bearish day):**
  - **Accumulation:** the open and anything above it is where shorts are accumulated (smart money, and ICT and his students, aim to enter there).
  - **Manipulation:** the initial rally above the open, the "sucker play" for breakout traders. It only goes up to go down. This is the Judas swing.
  - **Distribution:** from the low of the day to the close, where the short positions are distributed (closed).
  - The low of the day often forms late. If price has been beaten down all day, around 3:30–3:45 p.m. ET it's probably close to the low. Not always: sometimes there's a sudden continuation.
  - Bullish is mirrored: open near the low, a false move down, a rally, distribution of longs near the close.
- **Timestamps:** [0:12:56](https://youtu.be/S9ORTYmXwdE?t=776) — components defined; open and above = accumulation of shorts · [0:16:09](https://youtu.be/S9ORTYmXwdE?t=969) — manipulation = sucker play; distribution · [0:16:56](https://youtu.be/S9ORTYmXwdE?t=1016) — low of day near 3:30–3:45 p.m.

### Opening range (open-to-manipulation-extreme, projected through the open) and close-proximity entries
- **Kind:** definition / rule (new framing)
- **What ICT says:**
  - On a bearish day, measure the range from the opening price up to the high (the Judas swing). Subtract that range from the opening price: project it below the open. That projected zone is what he calls the **opening range**.
  - "Every premium array" (every FVG, stop raid and OTE short setup in any approach he teaches, including the paid mentorship) will form between the open and its high, and within that projection below the open.
  - This tells you how much leeway to give the market once it trades below the open while still taking a favorable short. These are **close-proximity entries**: there are many opportunities just below the opening price.
  - If price leaves that zone without you, don't chase. "I don't care how good it looks later in the day."
- **How to identify:** Opening price (intraday, the midnight NY open) and the manipulation high. Distance = high minus open. Zone = open plus or minus that distance.
- **How to use:** Write down intentions before the session: "bearish; look for shorts in the open-to-high range, or just below the open within the projected range." Only take setups inside it.
- **Example in this video:** NQ 15m, 17 Feb 2022. From the midnight opening price, price rallied above it into a FVG (a sell above the open). The open-to-high distance was projected below the open, and a further short formed there at the equities open. He describes the projection as "multiply that by two": from the high, double the high-to-open distance downward.
- **Timestamps:** [0:12:56](https://youtu.be/S9ORTYmXwdE?t=776) — open-to-high range subtracted from the open · [0:13:45](https://youtu.be/S9ORTYmXwdE?t=825) — every premium array forms in that range · [0:14:34](https://youtu.be/S9ORTYmXwdE?t=874) — close-proximity entries below the open; don't chase · [1:00:18](https://youtu.be/S9ORTYmXwdE?t=3618) — write intentions; outside the range, no trade
- **Nuance / caveats / changes:** This is ICT's specific 2022-Ep.10 meaning of "opening range". It differs from the RTH 9:30 opening range and gap concepts taught elsewhere.

### Midnight New York opening price (intraday anchor for Power 3)
- **Kind:** rule
- **What ICT says:** The dashed level at midnight New York time is the opening price he uses when applying daily Power of Three intraday. Price trading above it on a bearish day is the equivalent of the open-and-rally tick on the daily candle diagram. Sell there, even though it "feels unnatural" to short a rising market.
- **Timestamps:** [0:30:34](https://youtu.be/S9ORTYmXwdE?t=1834)
- **Nuance / caveats / changes:** In Ep. 9 he said he "likes 8:30" as the opening price for the intraday Power 3 checklist. Here the midnight open is the daily-candle open he projects from. Both appear in 2022 teaching.

### Swing high/low = 3 candles (no Williams fractal)
- **Kind:** definition
- **What ICT says:** A swing low is a low with a higher low to its left and a higher low to its right: three candles or bars. You don't need a Williams fractal; that's too many candles and you've missed the move. Three candles plus the proper context is enough to start hunting.
- **Timestamps:** [0:17:44](https://youtu.be/S9ORTYmXwdE?t=1064) · [0:18:31](https://youtu.be/S9ORTYmXwdE?t=1111)

### Paint-roller analogy for imbalance and rebalancing (FVG logic)
- **Kind:** definition
- **What ICT says:** The chart background is the wall and each candle is a paint roller. A big, long candle leaves "porous" places where price wasn't efficiently offered to the other side (not enough time or back-and-forth for buyers to participate). There's a strong (not universal) tendency for price to go back and overlap the whole range, repainting it evenly. Once a range is "completely balanced" there's no reason for price to hang around there.
- **Timestamps:** [0:12:06](https://youtu.be/S9ORTYmXwdE?t=726) — range fully balanced, no reason to stay · [0:27:22](https://youtu.be/S9ORTYmXwdE?t=1642) — paint roller: long candles get overlapped

### Model works across sessions
- **Kind:** rule
- **What ICT says:** NQ 1h: price supported at the daily FVG low, rallied to the FVG high, broke down right before midnight on the 17th, then traded back up into a FVG during the overnight London session. The same model works in the Asian session (little movement), London open (can catch "enormous moves" with daily bias), London close, and New York open.
- **Timestamps:** [0:25:45](https://youtu.be/S9ORTYmXwdE?t=1545) · [0:26:34](https://youtu.be/S9ORTYmXwdE?t=1594)

### 15-minute chart as the "bellwether" timeframe
- **Kind:** rule
- **What ICT says:** The 15m is his bellwether chart for day trades and scalps. "You can find everything for intraday trading" on it. If forced to pick one timeframe, he'd choose the 15m: he can swing trade, short-term trade, day trade and scalp from it. Even if you execute on the 1m (indices), you need the 15m storyline for the full panoramic view.
- **Timestamps:** [0:33:46](https://youtu.be/S9ORTYmXwdE?t=2026) · [0:34:35](https://youtu.be/S9ORTYmXwdE?t=2075)

### Bearish market structure shift (energetic break) and the two-FVG rule
- **Kind:** rule / entry model
- **What ICT says:**
  - Framework: a swing high is broken to the upside, taking buy stops (BSL), then a swing low is broken.
  - Was the decline lethargic? No: sudden, with momentum, obvious down-close candles. That's how you know you have a shift in market structure.
  - When there are two FVGs, try to trade the first one, but your money management must allow your stop to weather a run up into the second. "That's part of the rules."
- **Example in this video:** NQ 5m, 17 Feb 2022. At 7:00 a.m. price rallied above relative equal highs and cleaned up an imbalance, then broke down energetically.
- **Timestamps:** [0:36:58](https://youtu.be/S9ORTYmXwdE?t=2218) — 7:00 a.m. run above relative equal highs, two FVGs · [0:37:44](https://youtu.be/S9ORTYmXwdE?t=2264) — energetic down-close candles = MSS

### Top-down FVG search: 5m, then 4m, 3m, 2m, 1m (first one found wins; none means no trade)
- **Kind:** rule
- **What ICT says:**
  - If the 5m leg has no FVG, step down through the 4m, 3m, 2m and 1m.
  - The first timeframe where you find a FVG is your trading timeframe. Don't go lower once you've found one.
  - If there's no FVG even on the 1m, you have no trade.
  - On the 4m the candles looked "beefier" and cleaner than on the 5m. You want clean price action where the FVG (the break in even distribution) stands out.
- **Timestamps:** [0:37:44](https://youtu.be/S9ORTYmXwdE?t=2264) — strip 5m to 1m · [0:38:32](https://youtu.be/S9ORTYmXwdE?t=2312) — no FVG on 1m means no trade; 4m chart

### Bearish breaker (stop placement)
- **Kind:** definition / rule
- **What ICT says:**
  - The breaker pattern (taught in his free YouTube lessons): a high, a low, then a higher high (the run above BSL), followed by a return into it.
  - Bearish breaker candle = the down-close candle right before the big move up that took out the short-term high.
  - The market will "mostly stay in the lower half" of the breaker candle. So use the breaker candle and just above it for the stop, not the higher imbalance further up.
- **How to use:** Short the FVG inside or below the breaker. Stop just above the breaker candle.
- **Example in this video:** NQ 4m, 17 Feb 2022. BSL was run after rebalancing, then the breakdown. A FVG and a small imbalance were above. The stop was placed just above the breaker candle.
- **Timestamps:** [0:40:07](https://youtu.be/S9ORTYmXwdE?t=2407) — breaker = high, low, higher high; stop just above the breaker candle · [0:40:56](https://youtu.be/S9ORTYmXwdE?t=2456) — price mostly stays in the lower half of the breaker candle

### "Lowest-threshold" FVG entry
- **Kind:** refinement
- **What ICT says:** The FVG is defined by one candle's low and another candle's high. Extend it forward in time. As soon as price trades above the near edge of the FVG (the candle's high), go short. Don't wait for a deeper fill that may never come. Use "the easiest, lowest threshold entry technique" to make sure you're part of the move.
- **Example in this video:** NQ 4m, 17 Feb 2022. Price entered the FVG on the 8:28 candle and the short was taken there. Target: relative equal lows at 14,381.00. Filled around 14,515 aiming for 14,381: well over 100 points on one contract.
- **Timestamps:** [0:41:45](https://youtu.be/S9ORTYmXwdE?t=2505) — 8:28 candle, lowest-threshold entry, target 14,381 · [0:57:56](https://youtu.be/S9ORTYmXwdE?t=3476) — 14,515 to 14,381, "more than 100"

### Sell-side target: relative equal lows
- **Kind:** example only
- **What ICT says:** The relative equal lows below were sell-side liquidity, the low candle at 14,381.00 ("go look at your own chart"). That was the draw for the session's short.
- **Timestamps:** [0:34:35](https://youtu.be/S9ORTYmXwdE?t=2075) · [0:35:23](https://youtu.be/S9ORTYmXwdE?t=2123)

### Margin, leverage and volatility risk (discount brokers)
- **Kind:** rule
- **What ICT says:**
  - Discount brokers that let you trade a NQ mini for a couple of thousand dollars, or a micro for under $100, are "absolutely stupid". You're asking to blow the account.
  - He saw a 100-point NQ move in a single 1m candle. Slippage example: 50 points against 8 minis is $1,000 per contract, times 8 (the caption's "$88,000" is a mis-hearing). One candle can roast an account.
  - He wants at least $10,000 per NQ mini, and $15,000 is fair given current volatility. That day alone NQ moved about $8,000 per contract top to bottom.
  - TD Ameritrade required about $22,000 per NQ mini (exchange-based initial margin; a figure of about $17,604 is also mentioned, caption unclear).
  - When the exchange raises margins, it's "tipping their hand" that big moves are coming.
- **Timestamps:** [0:43:20](https://youtu.be/S9ORTYmXwdE?t=2600) — discount broker margins · [0:44:08](https://youtu.be/S9ORTYmXwdE?t=2648) — 100-point 1m candle; slippage · [0:45:44](https://youtu.be/S9ORTYmXwdE?t=2744) — $10k minimum, $15k fair · [0:57:08](https://youtu.be/S9ORTYmXwdE?t=3428) — margin hikes signal big moves

### Paper-trading demonstration (hypothetical discount-broker margin)
- **Kind:** example only
- **What ICT says:** At viewers' request he ran a TradingView paper account starting at $10,000 on 3 Feb 2022, NQ only, using hypothetical discount-broker margin. On 17 Feb he took a "heavy-handed, quant-style" short above the open and took partials into 14,381. About two weeks later the account showed a large hypothetical return (≈582% per caption). Three losing trades on the 14th were visible. He stresses it's paper money and that he wouldn't do this live.
- **Timestamps:** [0:48:59](https://youtu.be/S9ORTYmXwdE?t=2939) · [0:50:36](https://youtu.be/S9ORTYmXwdE?t=3036) · [0:51:24](https://youtu.be/S9ORTYmXwdE?t=3084)

### Backtesting by annotation ("I was expecting...") and journaling
- **Kind:** rule
- **What ICT says:** When backtesting, annotate the chart as if live ("I was expecting...") to build pseudo-experience. It trains your subconscious to see the pattern as if you'd seen it in real time. Log it in your journal and review Monday to Friday plus the previous week on the weekend to see the repetition.
- **Timestamps:** [1:01:53](https://youtu.be/S9ORTYmXwdE?t=3713) · [1:02:40](https://youtu.be/S9ORTYmXwdE?t=3760)

### Studying live price via screen recordings (tape reading practice)
- **Kind:** rule
- **What ICT says:** Practice for months reading the tape and studying price, without demo trades or target-picking. Live watching is best. If time zones or a job prevent it, record the screen (he uses TechSmith Camtasia) for about 8 hours and replay it in real time. TradingView replay is "clunky and wooden": it doesn't show the ebb and flow of candles forming.
- **Timestamps:** [0:31:25](https://youtu.be/S9ORTYmXwdE?t=1885) · [0:32:12](https://youtu.be/S9ORTYmXwdE?t=1932)

## Rules, checklists & numbers stated
- Economic calendar: ForexFactory; red high, orange medium, yellow low impact.
- 8:30 a.m. ET is when the news embargo lifts. A pre-news pump on a bearish day means premium being built to sell into.
- Daily bias = will the range expand above or below the opening price. The close needn't be predicted.
- Bearish Power 3: open and above = accumulation; the rally = manipulation (Judas); low-to-close = distribution. Bullish is mirrored.
- Low (or high) of the day often near 3:30–3:45 p.m. ET on trending days.
- Opening range = |open to manipulation extreme|, projected through the open. All entries must form there; leave it and you don't chase.
- Intraday opening price for Power 3: midnight New York.
- Swing point = 3 candles. No Williams fractal.
- 15m = bellwether chart.
- MSS must be energetic (sudden down-close candles), not lethargic.
- Two FVGs: aim for the first, size the stop to survive the second.
- FVG search: 5m, then 4m, 3m, 2m, 1m. Stop at the first FVG found. No FVG on 1m means no trade.
- Bearish breaker: stop just above the breaker candle; price mostly stays in its lower half.
- Lowest-threshold entry: enter as soon as price trades into the FVG's near edge.
- Example: short from about 14,515 (8:28 4m candle) to relative equal lows 14,381.00.
- NQ mini account size: at least $10k, $15k preferred. Avoid discount margins. A margin hike means big moves are coming.
- Write down the day's intentions (bias plus valid zone) before the market opens.

## Process, risk & psychology
- Bias isn't wrong because one day closes against it. Count the opposite candles in a swing: there are few (e.g. 2 down candles in a bullish run, 5 up candles in a bearish leg). If a loss on each of those days would blow your account, you're overleveraging or overtrading. ([1:04:17](https://youtu.be/S9ORTYmXwdE?t=3857), [1:05:04](https://youtu.be/S9ORTYmXwdE?t=3904))
- "Traders are professional losers." Every trade opens as a loser (commission, spread). A trader is a management company of losing trades: they turn losers into winners, but not all of them. ([1:03:29](https://youtu.be/S9ORTYmXwdE?t=3809))
- Missing a move is fine. Don't be upset; backtest and you'll see many opportunities near the open. ([0:14:34](https://youtu.be/S9ORTYmXwdE?t=874))
- Discipline: once price leaves your opening-range zone, don't chase. Brokers profit from your clicking. ([1:00:18](https://youtu.be/S9ORTYmXwdE?t=3618))
- Don't trade setups against your bias. Buying a bullish FVG on a bearish-bias day is a model violation. ([0:59:32](https://youtu.be/S9ORTYmXwdE?t=3572))
- Build a written model: when to buy and sell, stop placement, when to move the stop, how many contracts, and what makes a no-trade day. ([0:53:04](https://youtu.be/S9ORTYmXwdE?t=3184))
- Layered learning: be patient with the content order. Ten episodes in, you aren't ready to trade live. ([0:15:21](https://youtu.be/S9ORTYmXwdE?t=921), [1:05:54](https://youtu.be/S9ORTYmXwdE?t=3954))
- Patterns repeat. Familiarity builds comfort. Make the learning fun. ([0:53:52](https://youtu.be/S9ORTYmXwdE?t=3232))

## Glossary candidates
`Opening range (Ep.10 sense)` — the distance from the opening price to the manipulation high (or low), projected beyond the open; the zone where all valid entries form.
`Close-proximity entry` — an entry taken just beyond the opening price (within the projected opening range) after the ideal above-open entry was missed.
`Bellwether chart` — the 15-minute chart, used for intraday narrative and setups.
`Premium array` — any bearish PD array (FVG, OB, stop raid, OTE) used to sell in a premium.
`Lowest-threshold entry` — entering as soon as price touches the near edge of the FVG.
`Breaker (bearish)` — high, low, higher high; the down-close candle before the up-move is the breaker, and price tends to stay in its lower half.
`Paint roller (imbalance)` — a fast single-direction candle leaves unevenly offered price that tends to be revisited and overlapped.
`News embargo` — the 8:30 a.m. ET release time for scheduled economic data.
`Key reversal` — (mentioned in passing) a daily bar that overlaps and reverses the prior bar's range.
