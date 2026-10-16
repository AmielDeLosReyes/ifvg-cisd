# L26-105 — Continuous Contract Function & PD Array Mastery

ID: RY67bW2UhxY · URL: https://www.youtube.com/watch?v=RY67bW2UhxY · Duration: 1:28:47
Content type: lecture | market review | mixed
Teaching density: high

## Summary
ICT explains the specific rules for toggling the continuous contract function—not to find fair value gaps but to identify volume imbalances hidden by contract rollover effects. He demonstrates how bodies that cannot touch key levels (lower quadrants, event horizons) signal bearish institutional order flow. The core lesson: market structure (breaker blocks, suspension blocks, consequent encroachment) is visible in candlestick bodies and wicks alone, without need for external tools. This 1:28 session covers 1-minute tape reading, opening range gap mechanics, and why the first hour (9:30–10:30) contains enough opportunity to trade full-time.

## Concepts

### Continuous Contract vs. Front Month Contract (aliases: contract rollover adjustment, settlement price toggle)
- **Kind:** refinement
- **What ICT says:** The continuous contract shows price as if contracts roll seamlessly; it smooths gaps that occur at rollover dates. But ICT does not use this toggle to find fair value gaps. He uses it to reveal volume imbalances that exist on one contract but are hidden on the other due to the gap. Both closing prices must agree (e.g., 25,333.00 on both); when they don't match exactly, the toggle is useful. The settlement price toggle also changes what you see; if you have settlement price toggled on/off differently than ICT, you won't see the same suspension blocks or volume imbalances.
- **How to identify:** In TradingView, the continuous contract has a toggle button for rollover adjustment (lower right, gray hue). The front month contract shows only settlement price toggle. Check both; compare the PD arrays across them.
- **How to use:** Start analysis on continuous contract to get historical context unobstructed by rollover gaps. Identify breaker blocks and key levels. Then compare how the same price action uses those levels on the front month. If one contract's suspension block aligns better with bodies closing, use that as your key reference. Document both in your notes as alternates.
- **Example in this video:** MNQ June (front month) vs. MNQ continuous: when toggling the continuous adjustment off/on, a suspension block appears with a volume imbalance that the front month doesn't show cleanly. The consequent encroachment of the continuous is 25,495 (10.5 handles above front month's 25,474.5). This 20-handle spread reveals whether traders on each contract are using the same level.
- **Timestamps:** [0:05:28](https://youtu.be/RY67bW2UhxY?t=328) shows the toggle button; [0:13:20](https://youtu.be/RY67bW2UhxY?t=800) explains why both levels matter; [0:18:03](https://youtu.be/RY67bW2UhxY?t=1083) contrast with spotty price action on front month only.
- **Nuance / caveats / changes:** Some traders have the settlement price toggle on when ICT doesn't; this is why they don't see suspension blocks. If you don't see a volume imbalance or suspension block in your chart, check both toggles. The continuous contract function is NOT for finding new fair value gaps; it is for finding volume imbalances that wouldn't be visible otherwise and for ensuring you have clean historical price data before contract rollovers.

### Volume Imbalance (aliases: suspension block, gap between bodies)
- **Kind:** definition
- **What ICT says:** A volume imbalance occurs when candlestick bodies do not connect (there's a gap between one candle's close and the next candle's open) but the wicks overlap or touch. This separation of bodies creates inefficiency that price will later come back to fill. A suspension block has a volume imbalance at high and low; it's bracketed. The gap is only in the bodies, not the wicks.
- **How to identify:** Look for candlesticks where the close of one and open of the next have space between them, but wicks reach into or past each other. Measure: candlestick 1 close to candlestick 2 open = volume imbalance.
- **How to use:** These are targets. If price gaps up above a volume imbalance, that level becomes a pull-back target; if it gaps down, the inefficiency is a recovery target. Use for both entry zones and stop-loss levels.
- **Example in this video:** Daily suspension block on MNQ: a volume imbalance with a low and high; lower quadrant at 25,000 level; trading back down into this imbalance signals discount sensitivity and potential continuation lower.
- **Timestamps:** [0:11:44](https://youtu.be/RY67bW2UhxY?t=704) defines suspension block visually; [0:12:33](https://youtu.be/RY67bW2UhxY?t=753) shows the toggle making it visible/invisible.
- **Nuance / caveats / changes:** None stated; this is foundational ICT teaching.

### Consequent Encroachment (aliases: half gap, 50% level, midpoint of suspension block)
- **Kind:** definition
- **What ICT says:** Consequent encroachment is the halfway point between the high and low of a suspension block (or any inefficiency). It's a key intraday target; 70% of the time, the opening range gap fill reaches at least the consequent encroachment. This makes it your first, easiest draw for the morning session.
- **How to identify:** Suspension block high + low ÷ 2 = consequent encroachment. Mark it on your chart.
- **How to use:** If price opens above the gap midpoint, expect it to trade down to consequent encroachment. If below, expect a run up to it. This gives you a bias for the first 30–60 minutes.
- **Example in this video:** MNQ opening range gap: gap high and low were far apart (huge premium opening); consequent encroachment became the first target. Price respected it, then continued lower.
- **Timestamps:** [0:20:24](https://youtu.be/RY67bW2UhxY?t=1224) defines "half gap"; [0:33:17](https://youtu.be/RY67bW2UhxY?t=1997) states 70% probability.
- **Nuance / caveats / changes:** This is not a guarantee, but the probability is high enough to base your session bias on it.

### Bodies Cannot Touch (Key Levels) — Bearish Signature
- **Kind:** rule
- **What ICT says:** When price is bearish (in downtrend, below a key level), the candlestick bodies must stay out of that level. Wicks are allowed to tag it; bodies are not. If the bodies breach or even rest on that level, it signals weakness to the downside is over and bullishness may return. This is algorithmic: smart money executes orders such that bodies honor the level while wicks test it.
- **How to identify:** Track the high and low (or close) of the candlestick body. If it stays below the key level (e.g., lower quadrant of daily suspension block), that's bearish. If a body pierces the level, that's a reversal signal.
- **How to use:** Use this as a filter. While price is below a level with bodies unable to touch it, continue with your downside bias. The moment a body closes above or within that level, prepare for a turn or continuation of the upside.
- **Example in this video:** Daily suspension block lower quadrant at 25,000: bodies repeatedly failed to close above this level during the downtrend, confirming bearishness. When bodies finally touched it during a retracement, that signaled potential bullish shift.
- **Timestamps:** [0:42:58](https://youtu.be/RY67bW2UhxY?t=2578) explains bodies vs. wicks in FVG context; [0:43:47](https://youtu.be/RY67bW2UhxY?t=2627) body placement as bearish/bullish indicator.
- **Nuance / caveats / changes:** This applies to all key levels (old highs/lows, breaker blocks, PD arrays). It's a universal rule of institutional order flow.

### Breaker Block (aliases: structural high/low, swing high/low used as support/resistance)
- **Kind:** definition
- **What ICT says:** A breaker is a swing high followed by a swing low, then a higher high—or the inverse. Price "breaks" the prior swing low/high with authority. The original swing low (or high) then becomes a key support (or resistance). Use it to identify premium/discount zones and anticipate where price will return.
- **How to identify:** Swing low → swing high → higher high (bullish breaker). Swing high → swing low → lower low (bearish breaker). Mark the original swing (the one that got "broken") as your breaker level.
- **How to use:** Target for fills, entry zones, stop-loss placement. If price breaks above a breaker block, expect it to come back and test the breaker itself before continuing.
- **Example in this video:** MNQ intraday: price formed a breaker on the continuous chart; ICT watched it to see how the price action used that level on the front month contract.
- **Timestamps:** [0:04:41](https://youtu.be/RY67bW2UhxY?t=281) introduces breaker concept; [0:07:04](https://youtu.be/RY67bW2UhxY?t=424) explains why breaker is important across contracts.
- **Nuance / caveats / changes:** None stated in this video.

### First Presented Fair Value Gap (aliases: first FVG, first inefficiency, gap before high)
- **Kind:** definition
- **What ICT says:** After price opens and begins to move, the first gap in candlestick bodies that forms is the "first presented" FVG. It shows where the first inefficiency is created. This is crucial because price typically honors this before moving to deeper targets. The wick that creates the gap is the real gap; the visual gap on the chart is secondary.
- **How to identify:** In the first 1–2 minutes post-open, watch for candlesticks with bodies that don't touch. The separation is your first FVG.
- **How to use:** This is a key level for short-term tape reading. If price breaks above it with a bullish wick, expect it to come back and test the bottom of the wick (not the visible gap). If it comes back in on a pullback, the lower half should remain untouched if you're bullish.
- **Example in this video:** MNQ 9:30 candle: the first FVG formed immediately. Bodies stayed out of the lower half even during retracements, confirming bullishness short-term; then price later failed and turned bearish.
- **Timestamps:** [0:37:18](https://youtu.be/RY67bW2UhxY?t=2238) example of first FVG and wick distinction; [0:52:10](https://youtu.be/RY67bW2UhxY?t=3130) shows how bodies use (or don't) the first FVG.
- **Nuance / caveats / changes:** The wick, not the visual gap, is the true inefficiency. Traders often miss this.

### Wicks vs. Bodies Distinction
- **Kind:** refinement
- **What ICT says:** A wick is created when price extends beyond the closing price of the body. The wick represents the rejection of that price. When you see a gap visually, the wick created that gap, not the bodies. If you only look at the visual gap between candlesticks, you miss the real story in the wick rejection. This distinction changes how you read fair value gaps: the wick is what matters for entry and target placement, not the open/close separation.
- **How to identify:** On each candle, the body is open-to-close; the wick extends from high/low beyond the body.
- **How to use:** When analyzing a "gap," look left to the prior candle's wick. If the wick already extends into what would be the gap, that wick rejection is the real PD array, not the gap itself. Place entries and stops accordingly.
- **Example in this video:** MNQ consolidation with no fair value gap: a wick forms; that wick's rejection is the key level, not an open/close gap. Price respects the wick level.
- **Timestamps:** [0:37:18](https://youtu.be/RY67bW2UhxY?t=2238) distinguishes wick gap from open/close gap; [0:42:10](https://youtu.be/RY67bW2UhxY?t=2530) applies to fair value gap mechanics; [0:52:10](https://youtu.be/RY67bW2UhxY?t=3130) shows wick as the real level.
- **Nuance / caveats / changes:** This is not commonly taught; ICT says no other methodology (Wyckoff, Elliott Wave, supply/demand) teaches this distinction.

### Opening Range Gap & 70% Rule (aliases: 9:30 gap, regular trading hours opening range gap, RTHORG)
- **Kind:** rule
- **What ICT says:** Every morning at 9:30 ET, the market opens with a price; 70% of the time in the first hour, price will trade to the consequent encroachment (midpoint) of the gap created by the overnight move. This is your highest-probability first-hour draw. If you only trade the opening range gap for the first hour, you'll have a significant edge.
- **How to identify:** Settlement price at 4:15 PM ET → opening price at 9:30 ET = opening range gap. Calculate the midpoint (consequent encroachment).
- **How to use:** This is your session bias. Premium gap → expect fill of midpoint on downside. Discount gap → expect fill on upside. Do not trade beyond this until you confirm 70% is working in your hands.
- **Example in this video:** April 11 market review: MNQ opened with a huge premium gap; price was expected to fill down to consequent encroachment, which it did repeatedly through the morning.
- **Timestamps:** [0:33:17](https://youtu.be/RY67bW2UhxY?t=1997) states 70% figure; [0:54:08](https://youtu.be/RY67bW2UhxY?t=3248) compares opening price to RTH opening range gap.
- **Nuance / caveats / changes:** The 70% applies to the first hour (first 30 minutes for newer traders). This is the foundation of session bias; everything else is optional.

### Low-Hanging Fruit Objectives (aliases: easy targets, conservative drawdowns, measured short runs)
- **Kind:** entry model
- **What ICT says:** Reject the desire to run for large moves (500 handles, 200 handles). Instead, aim for low-hanging fruit: small, repeatable drawdowns of 20–40 handles that happen dozens of times intraday. This build experience, confidence, and capital preservation. Once you have skill, scale up.
- **How to identify:** After identifying a PD array or key level, measure the distance to the next reasonable level (not the ultimate target). This is your low-hanging fruit.
- **How to use:** In live trading, this is your bread-and-butter model. Wait for price to present a PD array, take your small win at the next level, and move on. Repeat multiple times a day.
- **Example in this video:** MNQ: continuous contract offered a 160-handle run to consequent encroachment vs. 400-handle run on front month to a distant target. The 160-handle run is the low-hanging fruit; it's more likely and requires less luck.
- **Timestamps:** [0:24:24](https://youtu.be/RY67bW2UhxY?t=1464) contrasts high expectations with low-hanging fruit; [0:25:15](https://youtu.be/RY67bW2UhxY?t=1515) advises new traders to focus here.
- **Nuance / caveats / changes:** This is not weakness; it's wisdom. It's how you build a sustainable edge.

### Event Horizon (aliases: midpoint of a large range, void, ether level)
- **Kind:** definition
- **What ICT says:** When a range (premium to discount, old high to old low, PD array) is very wide, the midpoint often appears to be empty—a void. But price gravitates to it with uncanny precision. This "event horizon" is where the market holds balance; algorithms use it as a target.
- **How to identify:** Measure a large range (e.g., daily suspension block high to low). Find the exact midpoint. Draw it as a reference.
- **How to use:** Use as a pullback target, reversal zone, or continuation staging point. If price overshoots it, expect it to come back.
- **Example in this video:** MNQ daily chart: event horizon level between the low of suspension block and the upper quadrant; price bounced in this area, used it as support, then continued.
- **Timestamps:** [0:06:02](https://youtu.be/RY67bW2UhxY?t=362) introduces event horizon conceptually.
- **Nuance / caveats / changes:** This level is not marked on the chart; it's pure geometry. Some traders miss it because it "doesn't exist" visually.

### Inversion Fair Value Gap (aliases: inversion FVG, inverted inefficiency, gap in wrong direction)
- **Kind:** definition
- **What ICT says:** When price is in a premium (bullish) area but trades down and creates a fair value gap on the downside, that gap is an "inversion." It's bullish by structure (it's an FVG) but appears inverted (gap on wrong side relative to trend). Use inversions to understand directional context: an inversion FVG below a bullish level signals that downside is temporary and the higher trend resumes.
- **How to identify:** In an uptrend (or at a premium level), a candlestick gap forms on the downside. That's an inversion FVG.
- **How to use:** This is a strong continuation setup. When price trades back above an inversion FVG, it confirms bullishness. Sell-side is exhausted; re-test the level and run higher.
- **Example in this video:** MNQ: after a rally, an inversion FVG formed on a pullback. When price traded back above it with conviction, it resumed the uptrend.
- **Timestamps:** [0:06:17](https://youtu.be/RY67bW2UhxY?t=377) mentions Ryan (Dodgy D) and his iFVG focus; [0:39:24](https://youtu.be/RY67bW2UhxY?t=2364) shows inversion FVG usage live.
- **Nuance / caveats / changes:** Inversion FVGs are not on every chart; they're special. Dodgy D built a full strategy around them, which is valid but narrow. ICT uses them as one tool among many.

### Octant Levels (aliases: eighths, gradient levels, divisions of suspension block)
- **Kind:** definition
- **What ICT says:** A suspension block (or any large range) can be divided into eighths (octants). Mark the quarters (upper/lower quadrants) and the eighths. These provide micro-targets and precision entries. The lower octant is one-eighth up from the low; the upper octant is one-eighth down from the high.
- **How to identify:** Use Fibonacci tool set to octaves (1/8), or manually divide the range into eight equal parts.
- **How to use:** Pullbacks within these gradient levels help you fine-tune stops and targets. If price pulls back into a lower octant during a downtrend, that's support; if it pulls back into the upper octant during an uptrend, that's resistance.
- **Example in this video:** MNQ daily suspension block: ICT drew octant lines and used them to grade price action through the day.
- **Timestamps:** [0:35:41](https://youtu.be/RY67bW2UhxY?t=2141) shows Fibonacci octane settings; [0:30:00](https://youtu.be/RY67bW2UhxY?t=1800) references octants as gradients for measurement.
- **Nuance / caveats / changes:** This is precision work; it requires clean, wide ranges to be useful.

## Rules, checklists & numbers stated

- **70% rule:** Opening range gap is filled to consequent encroachment 70% of the time in first hour (first 30 min for new traders).
- **First hour (9:30–10:30 ET) is the universe:** All learning and profitability should focus here; you don't need to trade beyond it.
- **Bodies must not touch key levels when bearish.** Wicks are allowed; bodies are not. If bodies touch the level, bullishness is returning.
- **Opening price + opening price range = session bias.** Premium gap → bias down to consequent encroachment. Discount gap → bias up.
- **Suspension block high & low bracket all inefficiencies within that range.** Consequent encroachment is always at the 50% level.
- **Do not demand the full run.** Low-hanging fruit (20–40 handles, dozens of times a day) builds skill faster than chasing 500-handle targets once a week.
- **Settlement price and continuous contract toggles must match your intent.** If you toggle one but not the other, your PD arrays won't align with ICT's.
- **Breaker blocks become key levels.** Once broken, the original swing becomes support/resistance.
- **First presented fair value gap is the first inefficiency post-open.** Use this, not later ones, for session bias confirmation.
- **Manual intervention is not random.** Even when the market is being "played," the run goes to an algorithmic level, not a guess. Use stops to protect against these runs.
- **Never over-leverage in current market conditions.** Manual intervention is happening 2–3+ times per month, vs. normal historical frequency. Risk is elevated.

## Process, risk & psychology

- **Session structure:** Start by knowing what the opening range gap is and where consequent encroachment lies. This is your first 30–60-minute roadmap.
- **Chart setup:** Use continuous contract for historical context, then compare to front month for current trading. Both will show valid PD arrays; use the one with strongest body adherence.
- **Journaling:** Write down the levels you identify before market open. After the session, review which ones price actually used. Track your accuracy over weeks.
- **Avoid fundamental data in your decision-making.** CPI, economic reports, geopolitical news—all noise. Price structure (PD arrays, gaps, bodies on levels) is the truth. Focus on technicals only; let the technicals tell you whether the news matters.
- **Fear and impatience:** Many traders demand large moves, get bored waiting for the small moves, and overtrade. Resist this. Slow is smooth; smooth is fast.
- **Teaching approach:** ICT is live-streaming and calling drawdowns in advance (not cherry-picking). Watch his live streams and measure your chart-reading against his. This is the fastest way to train your eye.
- **Development timeline:** Expect 6–8 weeks of consistent tape reading (no trading) before you're ready to paper trade. Then another 6–8 weeks of paper trading before live trading. This is not negotiable if you want to succeed.
- **Stop-loss placement:** Use the high of the opening range if you're short; use the level you're targeting as your stop (e.g., if bearish and targeting consequent encroachment down, stop above the half-gap level or at the daily suspension block high).

## Glossary candidates

`CONTINUOUS CONTRACT` — Chart that shows prices as if contracts roll seamlessly at rollover dates; used to see historical context without gaps caused by front-month rollovers.

`FRONT MONTH` — The nearest expiring contract (e.g., June MNQ in mid-April); most actively traded; becomes spotty in historical data after rollover.

`SETTLEMENT PRICE` — Closing price of regular trading hours (RTH) at 4:15 PM ET; used to calculate the next day's opening range gap.

`VOLUME IMBALANCE` — Separation between candlestick bodies (close of one candle ≠ open of next) but overlap in wicks; marks inefficiency.

`SUSPENSION BLOCK` — Large volume imbalance bracketed by a high and low, often spanning multiple octants; key daily-level target.

`CONSEQUENT ENCROACHMENT` — The 50% midpoint of a gap or range; highest-probability target for price in first hour (70% rule).

`BODIES CANNOT TOUCH` — When price is bearish, candlestick bodies must stay below a key level; if bodies touch/breach it, bullishness may return.

`BREAKER BLOCK` — A swing high or low that gets "broken" by price (higher high or lower low); the original swing then acts as support/resistance.

`FIRST PRESENTED FAIR VALUE GAP` — The first inefficiency formed in the first few candles post-open; key for short-term bias confirmation.

`EVENT HORIZON` — The exact midpoint of a very large range; appears empty but price gravitates to it with precision.

`INVERSION FAIR VALUE GAP` — A gap that forms in the opposite direction of the trend (e.g., gap down during uptrend); bullish continuation signal when price re-enters it from above.

`OCTANT` — One-eighth division of a range (suspension block, gap, etc.); used for fine-tuning target and support/resistance levels.

`OPENING RANGE GAP` — Gap between settlement price (prior 4:15 PM) and open (9:30 AM); defines the range for first-hour trading.

`WICK` — Extension of price beyond the closing price of the body; represents rejection and often holds more significance than the body for PD array identification.
