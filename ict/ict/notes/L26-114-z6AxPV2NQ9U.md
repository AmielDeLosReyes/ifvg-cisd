# L26-114 — ICT 2026 Market Commentary
ID: z6AxPV2NQ9U · URL: https://www.youtube.com/watch?v=z6AxPV2NQ9U · Duration: 1:53:05
Content type: live market review (lecture blend)
Teaching density: high

## Summary
A deep dive into inversion fair value gap (iFVG) mechanics and tape reading discipline on a Friday NQ/ES session. ICT demonstrates how failed consequent encroachment, time distortion inside gaps, and day-of-week context filter bad trades, emphasizing that *not* trading (sitting out) is sometimes the best trade. Teaches position management (trailing stops, taking partials on warning signals) and the importance of observing what price should do vs. what it actually does as real order flow feedback.

## Concepts

### Inversion Fair Value Gap (iFVG)
- **Kind:** core entry model / refinement
- **What ICT says:** An iFVG forms when price trades *above* a bullish gap (SIBI/volume imbalance), then pulls back into it. If it re-enters and refuses to lay a body in the upper half (stays in lower half), it becomes valid. An iFVG is *not* a zone idea; it's an inefficiency defined by open/close on specific candles. Must measure with precision: open and close matter, not just high/low.
- **How to identify:** 
  1. Spot a swing low, price drops, creates volume imbalance (gap).
  2. Price trades up above it, bodies leave the gap.
  3. Price retraces back into the gap.
  4. Check: if body *closes below* the midpoint (consequent encroachment), it is a bearish iFVG.
  5. If body refuses upper half when it re-enters, rejection is confirmed.
- **How to use:** Bearish iFVG = anticipate lower prices. If price fails to enter the lower half or spends too much time in the gap (time distortion), the setup is compromised. When invalid, it may act as a balanced price range instead. Use as entry bias on lower timeframes after confirming on higher timeframe structure.
- **Example in this video:** NQ 1m, ~9:31 ET: price creates volume imbalance (SIBI) off swing low. At 0:04:46–0:06:25, price dips into first present-to-iFVG, which becomes valid as inversion. By 0:20:42–0:27:52, ICT enters short into consequent encroachment of an iFVG wick with minimal risk, exiting below 24,351 1/4. Price then delivers lower as the iFVG expected.
- **Timestamps:** 
  - [0:04:46](https://youtu.be/z6AxPV2NQ9U?t=286) — first present-to-FVG identified (volume imbalance, 1-minute)
  - [0:20:42](https://youtu.be/z6AxPV2NQ9U?t=1242) — iFVG bias setup and why NOT to trade Friday morning
  - [0:27:52](https://youtu.be/z6AxPV2NQ9U?t=1672) — short entry on consequent encroachment; exit below 24,351 1/4
  - [0:45:01](https://youtu.be/z6AxPV2NQ9U?t=2701) — Bitcoin example: sell-side inefficiency becomes iFVG; fails to touch consequent encroachment = immediate bearish feedback
- **Nuance / caveats / changes:** 
  - An iFVG is *not* valid until price lays a body in it. Only re-entry + body closure in lower half = valid.
  - If too many candles (>2) spend time inside the gap, it loses power (time distortion weakness). Price should enter in 1–2 candles and *leave immediately* if the gap is truly valid.
  - iFVG trades *above* the gap first, then retraces into it (unlike a standard FVG which is hit first).
  - On Fridays (TGIF), iFVGs are less reliable because gap risk from Sunday open overrides intraday moves.

### Consequent Encroachment
- **Kind:** definition / rule
- **What ICT says:** Split any gap or wick in half. That midpoint is consequent encroachment. If price reaches it but fails to touch it, that is immediate feedback on the direction. Failure to touch midpoint = weakness in the opposite direction.
- **How to identify:** Measure gap/wick high and low, divide by 2. Draw a line at that midpoint.
- **How to use:** 
  - Bearish signal: if price runs up but refuses to touch consequent encroachment midpoint of a daily wick, expect reversal lower.
  - Entry signal: when price re-enters an iFVG and trades to consequent encroachment of that wick, that's a premium entry point.
  - Stop placement: if shorting and price gets a body above consequent encroachment of a gap, consider closing the trade.
- **Example in this video:** Daily chart, March 9 wick: price fails to reach the halfway point (consequent encroachment). This is distribution; even on a 1-minute chart, the failure to touch the daily wick's midpoint signals lower prices coming. ~0:13:35–0:14:22.
- **Timestamps:**
  - [0:13:35](https://youtu.be/z6AxPV2NQ9U?t=815) — daily wick graded; consequent encroachment marked and how failure to reach it = distribution
  - [0:29:31](https://youtu.be/z6AxPV2NQ9U?t=1771) — entry at consequent encroachment of a wick separation; tight, precise entry
  - [0:45:50](https://youtu.be/z6AxPV2NQ9U?t=2750) — Bitcoin: "split the range in half. That's consequent encroachment. It trades up to it, but it fails to touch it. This is just like immediate rebounds."
- **Nuance:** Consequent encroachment is *always* the midpoint; it is a precise level, not a range. It is used to measure both gaps and wicks.

### Fair Value Gap (FVG) – Present-to-FVG Entry Recognition
- **Kind:** entry model
- **What ICT says:** A volume imbalance (gap between candle open and prior close with no trade between) is a FVG. When price pulls back into it after moving away, that's the entry opportunity. A "present-to-FVG" is the first FVG to form in a session or structure.
- **How to identify:** 
  1. Spot a candle whose open is more than 1 tick away from the prior candle's close.
  2. Measure that gap; it is the FVG.
  3. When price re-enters it, measure consequent encroachment of that gap.
  4. Entry occurs as price approaches the consequent encroachment.
- **How to use:** Present-to-FVG acts as the first bias entry for the day or sequence. After the first FVG delivers, subsequent gaps have less weight. Use to anchor initial bias and initial stop placement.
- **Example in this video:** NQ 1m, 9:31: first present-to-FVG identified at 0:04:46. Price then dips to that level and sets up the trade. The video uses this FVG as the foundational bias for the morning setup.
- **Timestamps:**
  - [0:04:46](https://youtu.be/z6AxPV2NQ9U?t=286) — first present-to-FVG (volume imbalance on open)
  - [0:19:05](https://youtu.be/z6AxPV2NQ9U?t=1145) — returning to the first present-to-FVG, explaining why it's the first bias
- **Nuance:** Present-to-FVG is most relevant at session open. Later FVGs may act differently depending on time of day and prior context.

### Volume Imbalance (Order Block / PD Array)
- **Kind:** definition / rule
- **What ICT says:** A candle with an open and close that creates a gap to the previous candle (no trade between them) is a volume imbalance. It is a specific inefficiency that price is likely to revisit. Do not treat it as a zone; treat it as a precise range to be filled or respected.
- **How to identify:** Compare prior candle close to current candle open. If there's a gap (no bodies in between), that is the imbalance. Measure it by the open and close of the candle that created it.
- **How to use:** Price returning to the imbalance (FVG) can act as continuation, reversal, or balanced price range depending on context and how price interacts with consequent encroachment.
- **Example in this video:** 0:04:46, 0:05:33 — volume imbalance on the 9:31 1-minute candle with open 13 1/4, close 13 1/2 (1-tick imbalance). This becomes the first-present-to-FVG reference.
- **Nuance:** Volume imbalance and FVG are used interchangeably here; the term depends on context (imbalance = the raw gap; FVG = imbalance with price action interpretation).

### Tape Reading / Order Flow Observation
- **Kind:** process / refinement
- **What ICT says:** Tape reading is *visual* observation of open, high, low, close (OHLC) to determine intent without looking at footprint, order book, or data crunching. If price can't reach a level it "should," that's feedback: it's weak in that direction. If it does reach it quickly and decisively, that's strength. Your job as a beginner is to *observe*, not to trade. Watch price interaction with PD arrays and document whether it behaves as expected.
- **How to identify:** When learning, don't place trades. Instead, draw levels and watch price:
  - Does price reach the level it should?
  - Does it leave a body or just a wick?
  - How fast does it move through/away from the level?
  - How much time does it spend in inefficiencies?
- **How to use:** Use tape reading as a *defensive practice*. If a level *should* be hit but isn't, that's a sign not to trade, or to scale out of a position. Document this feedback loop to refine your model. Do not force trades; let the market confirm your bias through observable price behavior.
- **Example in this video:** ~0:33:54–0:37:01 — ICT watches price action and notes that the inversion FVG is not delivering as expected (lethargic, time distortion). Rather than forcing a short, he sits out, observing. By 0:34:40–0:36:13, he walks through what should happen vs. what is happening, using that gap to decide *against* trading.
- **Timestamps:**
  - [0:33:54](https://youtu.be/z6AxPV2NQ9U?t=2034) — "tape reading purposes, while you're learning… you're not trying to take a demo entry… you want to measure the willingness"
  - [0:47:48](https://youtu.be/z6AxPV2NQ9U?t=2868) — "when you're tape reading, you're not trying to hold yourself to being right or wrong… you're trying to collect information"
- **Nuance:** Tape reading is *not* a trade method; it is a *learning* method. Only after weeks of observing should you attempt small paper trades.

### Time Distortion in Gaps (Weakness Indicator)
- **Kind:** rule / refinement
- **What ICT says:** If price spends too much time (more than 1–2 candles) inside a FVG, the gap has lost validity. A strong gap is entered and exited in 1–2 candles *maximum*. Time inside = hesitation = weakness. Prolonged candles in a gap means the market is not in a hurry to move, which contradicts the premise that the gap should be filled/rejected urgently.
- **How to identify:** Count how many candles price spends with bodies inside the gap. If >2, flag it as weak.
- **How to use:** 
  - If you're short and price lingers in a gap for 3+ candles, consider taking off a position.
  - If gap time distortion occurs, do not anticipate immediate continuation in your bias direction.
  - Use time distortion as a stop or pivot signal: if price *should* be moving but isn't, it's a warning.
- **Example in this video:** ~0:16:48–0:17:34 — "See how many times it's used that little area? Now, compare contrast that with when the market's really wanting to move, it'll go on there one candle and then it's gone. Elvis has left the building." Also at 0:31:08–0:31:57: "Too many candlesticks inside a fair value gap. It needs to be one, maybe two at most, and leave."
- **Timestamps:**
  - [0:16:48](https://youtu.be/z6AxPV2NQ9U?t=1008) — multiple uses of the same gap area = weakness
  - [0:31:08](https://youtu.be/z6AxPV2NQ9U?t=1868) — "Too many candlesticks inside a fair value gap… they're not going to waste your time… [if valid] they're going to try to run"
  - [0:98:46](https://youtu.be/z6AxPV2NQ9U?t=5926) — "See how much time [is] staying in that gap? We don't want to see time distortion inside of inefficiencies."
- **Nuance:** Time distortion is most relevant when you have a clear directional bias. If price should move quickly to an objective but doesn't, it's a sign of trapped traders or a lack of conviction on that move.

### Buy-Side Liquidity (BSL) / Sell-Side Liquidity (SSL) and Liquidity Pools
- **Kind:** definition / concept
- **What ICT says:** Liquidity rests at certain levels. A high where many traders have stops above is "sell-side liquidity" (SSL); a low where stops are placed below is "buy-side liquidity" (BSL). Market makers hunt these levels. You must identify them on your structure and expect price to run to them. Sell-side imbalance = inefficiency below a high (e.g., gap down after a high). Buy-side imbalance = inefficiency above a low (e.g., gap up after a low).
- **How to identify:** 
  - Identify swing highs and lows.
  - Assume stops are placed just beyond them (e.g., 2–5 ticks above a high, 2–5 ticks below a low).
  - That aggregated stop placement = the liquidity pool.
  - When a gap forms adjacent to such a level, it is imbalance near liquidity.
- **How to use:** 
  - Bias towards price running to liquidity (e.g., if you're bullish, look for price to run to a prior swing high's SSL).
  - Use liquidity objectives as targets, not precise entry triggers.
  - Recognize that liquidity hunts are a market maker behavior; expect sudden runs and reversals at these levels.
- **Example in this video:** 0:07:12–0:08:46 — daily chart shows "an intermediate-term sell side liquidity pool" below the daily suspension block. ICT notes this as a target or resistance if price continues lower. On the 1m, multiple references to "buy side here" and "sell side there" throughout.
- **Timestamps:**
  - [0:07:12](https://youtu.be/z6AxPV2NQ9U?t=432) — sell-side intermediate-term liquidity pool on daily
  - [0:19:05](https://youtu.be/z6AxPV2NQ9U?t=1145) — buy-side order imbalance in opening range gap
  - [0:34:40](https://youtu.be/z6AxPV2NQ9U?t=2080) — daily buy-side imbalance / sell-side inefficiency trade example
- **Nuance:** Liquidity pools are not precisely defined; they are inferred from structure. Precision comes from the imbalance (gap) adjacent to them, not the exact high/low.

### Judas Swing / False Move
- **Kind:** pattern / rule
- **What ICT says:** A Judas swing is a move in one direction (e.g., down) that pulls traders in, then reverses sharply against them. It is often followed immediately by the opposite move. Used to trap traders and generate liquidity for the real move.
- **How to identify:** Price breaks a level or takes out a low, then reverses hard. The break can be 1 tick or several ticks; the key is the false direction followed by sharp reversal.
- **How to use:** 
  - Do not chase breakouts blindly.
  - Expect Judas swings around key levels.
  - If you see a break followed by quick reversal, assume it was a Judas swing and expect the opposite direction to dominate next.
- **Example in this video:** 0:26:58 — "this Judas swing there. We gave up the ghost came back up inside here." Price runs down, traps shorts, then reverses.
- **Timestamps:**
  - [0:26:58](https://youtu.be/z6AxPV2NQ9U?t=1618) — Judas swing on daily chart, Wednesday session
- **Nuance:** Judas swings are common before large moves. Expect them and use them to filter out early entries.

### Consequent Correction
- **Kind:** definition / refinement (related to consequent encroachment)
- **What ICT says:** "Consequent correction" is the midpoint of a wick (similar to consequent encroachment but applied to a wick structure). If price gaps below a wick and then pulls back up, the midpoint of that wick is resistance; price staying below it confirms bearishness.
- **How to identify:** Measure the wick high and low, find the midpoint, and observe price interaction.
- **How to use:** Entry point: if price gaps below and you want to short, look for a pull-back toward consequent correction of the wick, then short the rejection from there. Stop: place it 1 tick above consequent correction of the wick.
- **Example in this video:** 0:42:39–0:43:26 — gold chart: ICT draws consequent correction of a wick, then says "I'd like to see a gap below that" on Sunday opening. If price gaps below and stays heavy (not returning into the upper half), very bearish.
- **Timestamps:**
  - [0:42:39](https://youtu.be/z6AxPV2NQ9U?t=2559) — gold gap and consequent correction of wick
  - [0:55:04](https://youtu.be/z6AxPV2NQ9U?t=3304) — consequent correction in real-time chart setup on MES
- **Nuance:** Consequent correction is used when there is a gap (suspension block or open gap). If no gap, use consequent encroachment instead.

### TGIF (Thursday Is FUN) / Day-of-Week Effects
- **Kind:** rule / bias filter
- **What ICT says:** Friday (TGIF) is a high-risk day for shorts because weekend gap risk is extreme. Traders may not hold bearish positions overnight. Instead, the market may keep price rangebound on Friday and gap open radically lower on Sunday at 6 pm ET. Do not assume Friday will deliver bearish moves; use caution. If in doubt on Friday, sit out the trade.
- **How to identify:** It's Friday. Check the calendar.
- **How to use:** 
  - Reduce position size on Fridays.
  - Avoid shorting setups unless the bias is very clear (e.g., a strong break below a key level *with* price already moving decisively).
  - Be willing to miss Friday trades and wait for Monday.
  - Anticipate gap risk; assume the gap will be filled or exceeded on Sunday open.
- **Example in this video:** 0:20:42–0:23:02 — "Because it's Friday, I'm a little reluctant to trust this going down." ICT has a bearish setup but does not take it because it's Friday and TGIF dynamics apply. Also at 0:34:09 onwards: the entire afternoon is spent managing this because it's TGIF and Friday behavior is unpredictable.
- **Timestamps:**
  - [0:20:42](https://youtu.be/z6AxPV2NQ9U?t=1242) — "because it's Friday, I'm a little reluctant"
  - [0:23:02](https://youtu.be/z6AxPV2NQ9U?t=1382) — explaining TGIF and why he won't short the setup despite bias
  - [0:49:48](https://youtu.be/z6AxPV2NQ9U?t=2988) — "just be careful… don't marry the vein… Because it's TGIF"
- **Nuance:** TGIF is a contextual filter, not a rule that prevents all Friday trades. High-conviction setups (e.g., a break below a critical structure level) can still work, but require tighter risk management.

### Opening Range Gap (ORG) / RTH Opening Range
- **Kind:** definition / context
- **What ICT says:** The opening range gap is the gap between the pre-market or previous day's close and the 9:30 ET RTH open. It can be a gap up (bullish) or gap down (bearish). This gap's size and location relative to prior structure matters. A "deep deep discount opening range gap" means we opened much lower than expected relative to prior price. The low of this opening range and its high are key liquidity points.
- **How to identify:** 
  - Pre-market close or previous day settlement.
  - 9:30 RTH open candle.
  - Measure the gap between them.
  - Identify the high and low of the opening range for the day (typically the 9:30 candle or first few minutes).
- **How to use:** 
  - If it's a deep discount, shorts may be cautious (too good to be true).
  - If it's a gap up into resistance, longs are chasing.
  - Use the opening range high/low as pivotal support/resistance.
  - The liquidity inside the gap is a target for price to visit.
- **Example in this video:** 0:03:08 — "opening price at 9:30 there" (opening range gap low). The opening range high is also identified, and ICT explains that price must clear it to confirm bullish action.
- **Timestamps:**
  - [0:00:30](https://youtu.be/z6AxPV2NQ9U?t=30) — "I have deep deep deep deep discount opening range gap here"
  - [0:03:08](https://youtu.be/z6AxPV2NQ9U?t=188) — opening price identified; trading hour opening range gap defined
  - [0:19:05](https://youtu.be/z6AxPV2NQ9U?t=1145) — "opening range gap low, which is at opening price at 9:30"
- **Nuance:** Opening range gaps are session-specific. On Friday, opening gaps are less reliable guides due to weekend gap risk.

### Suspension Block / Breaker Block
- **Kind:** definition / PD array variant
- **What ICT says:** A suspension block (also called a breaker block in some contexts) forms when price consolidates with a high and low that define a range, then breaks out. If it breaks higher and is bullish, price is expected to stay above the midpoint (consequent encroachment) of that block going forward; if bearish, it should stay below. If it re-enters and trades back into the block, the nature of that re-entry (which half it enters) determines continuation or reversal.
- **How to identify:** A candle or multi-candle range with a clear high and low, followed by a break in one direction.
- **How to use:** 
  - If bullish suspension block and price re-enters it, expect it to stay in the upper half and continue higher.
  - If it lays a body in the lower half, that is bearish rejection of the bullish bias.
  - Use consequent encroachment of the block as the dividing line.
- **Example in this video:** 0:06:25–0:07:12 — daily chart: "we have a suspension block here and that is noteworthy… a bullish suspension block, if we trade down in the lower half of it, if we're bearish."
- **Timestamps:**
  - [0:06:25](https://youtu.be/z6AxPV2NQ9U?t=385) — suspension block identified on daily
  - [0:07:12](https://youtu.be/z6AxPV2NQ9U?t=432) — explaining suspension block rules
- **Nuance:** Suspension block is a structural concept; the rules depend on whether it is bullish or bearish and how price re-enters it.

### Balanced Price Range (BPR)
- **Kind:** definition / PD array state
- **What ICT says:** A balanced price range forms when price trades both above and below a gap/FVG (or any PD array) without committing to either direction. This means the gap has acted as both support and resistance (buy side AND sell side). Once established, a BPR is neutral; price can break either way next.
- **How to identify:** 
  1. Price moves above the gap/array.
  2. Price pulls back and trades inside/below the gap/array.
  3. Price re-enters and moves above it again.
  4. Two passes (above and below) = balanced price range.
- **How to use:** Once a BPR is established, do not trade off the gap alone. Wait for price to break decisively in one direction, ideally with additional confluence (e.g., a fresh lower-timeframe FVG, a time-of-day macro, a liquidity level). Do not assume the gap will deliver anymore.
- **Example in this video:** 0:54:50–0:57:13 — MES on 1m: a gap is traded above, then below, then above again. This creates a BPR. ICT notes that the gap is no longer a reliable bias tool after it becomes balanced.
- **Timestamps:**
  - [0:54:50](https://youtu.be/z6AxPV2NQ9U?t=3290) — price above gap, then below, then above again = balanced price range
  - [0:56:26](https://youtu.be/z6AxPV2NQ9U?t=3386) — "that specific candlestick right there… that's what it's doing. That's the function."
- **Nuance:** A BPR is a neutral state; it does not predict direction. Use it to *avoid* trading, not to set up entries.

### Discount / Premium / Equilibrium (Daily Range Context)
- **Kind:** definition / context
- **What ICT says:** 
  - Discount: price in the lower half of a daily range (RTH).
  - Premium: price in the upper half of a daily range.
  - Equilibrium: price at the midpoint.
  Being in deep discount when you're trying to short is a problem: the move has already happened, and price should accelerate lower if the bias is correct, not linger. Linger = weakness.
- **How to identify:** Calculate the daily high and low (RTH only), find the midpoint. Check where current price sits relative to it.
- **How to use:** 
  - If bearish and price is in deep discount, the burden is on price to accelerate lower. If it doesn't, the trade is suspect.
  - If bullish and price is in deep premium, expect a pullback to equilibrium or lower before continuation up.
  - Use discount/premium as a bias confirmation: a strong move should accelerate when it reaches discount/premium, not consolidate.
- **Example in this video:** 0:88:25 onwards — ICT checks where NQ is relative to the daily range, finds it in deep discount. He notes that being short from deep discount means price *should* be accelerating lower, but it's not, which is a warning sign.
- **Timestamps:**
  - [0:84:21](https://youtu.be/z6AxPV2NQ9U?t=5061) — range calculation and discount/premium concept
  - [0:88:25](https://youtu.be/z6AxPV2NQ9U?t=5305) — "we're in a deep deep deep discount… you don't want to be getting short like this"
  - [0:104:21](https://youtu.be/z6AxPV2NQ9U?t=6261) — "in the lowest portion of [the daily] range"
- **Nuance:** Discount/premium is contextual. On a strong trend day, price can remain in premium or discount for hours. Use it as a *pressure* signal, not a reversal signal.

### Market Structure Break / Consequent Encroachment Failure (as a Weakness Signal)
- **Kind:** rule / refinement
- **What ICT says:** If price is expected to break a level (e.g., a high) but fails even to reach the midpoint (consequent encroachment) of a gap/wick before that level, that is weakness. It indicates lack of conviction. "Failure to touch consequent encroachment" is immediate bearish or bullish feedback depending on direction.
- **How to identify:** Price moves toward a level, reaches only the midpoint or less of a gap/wick, reverses before reaching the level. That is failure.
- **How to use:** 
  - If you expect bullish breakout and price fails to reach the midpoint of a resistance gap, expect lower prices.
  - If bearish and price fails to reach the midpoint of a support gap, expect higher prices.
  - Use failure as a signal to exit or avoid the trade.
- **Example in this video:** 0:13:35–0:14:22 — "the fact that it can't get up to its halfway point on that daily wick… this is distribution. This is not a bull flag."
- **Timestamps:**
  - [0:13:35](https://youtu.be/z6AxPV2NQ9U?t=815) — failure to touch daily wick midpoint = distribution
  - [0:22:01](https://youtu.be/z6AxPV2NQ9U?t=1321) — "this is heavy distribution"
- **Nuance:** Failure is contextual; one instance is interesting, but repeated failure confirms weakness.

## Rules, checklists & numbers stated

- **Inversion fair value gap rules:**
  - An iFVG requires price to trade *above* it first, then re-enter it.
  - A valid iFVG has price laying a body in the *lower half* upon re-entry (bearish) or upper half (bullish).
  - If too many candles (>2) spend time in the iFVG, it is compromised and may act as a balanced price range instead.
  - An iFVG that fails to enter the correct half is invalid; do not trade it.

- **Consequent encroachment (midpoint) rules:**
  - Always measure gap/wick high to low and split in half.
  - Failure to touch it = immediate feedback (weakness in opposite direction).
  - Entry into an iFVG at the consequent encroachment of the wick is a premium entry.
  - Stop placement: 1 tick above/below consequent encroachment of your bias structure.

- **Time distortion rule:**
  - 1–2 candles in a gap = normal, valid.
  - 3+ candles in a gap = weakness, time distortion; reduce size or sit out.

- **TGIF (Friday) rules:**
  - Assume extreme gap risk from Friday close to Sunday 6 pm ET open.
  - Do not short aggressively on Friday unless setup is very strong and structure is clear.
  - Expect price to be rangebound on Friday while market makers prep for gap on Sunday open.
  - If biased bearish on Friday, expect gaps lower on Sunday open, not Friday afternoon delivery.

- **Discount rule (position management):**
  - If bearish from deep discount (lower half of daily range), price *must* accelerate lower, not linger.
  - Linger in discount while bearish = warning sign to exit or reduce.
  - If price does not accelerate when in discount, assume trade is suspect.

- **Liquidity pool rule:**
  - Price runs to liquidity (prior swing highs/lows with stops).
  - Use liquidity objectives as targets, but do not demand precision; scale out on approaches.

- **Balanced price range rule:**
  - Once price trades both above and below a gap (two passes), it is balanced.
  - Do not trade a balanced gap on gap interaction alone; require additional confluence.

- **Time-of-day context (this session):**
  - 10:00 ET: consumer sentiment (medium impact).
  - 10:00–11:00 (lunch macro): expect retracement to first short-term high before continuation.
  - Friday session: cap risk due to day-of-week effects.

- **Tape reading rules (for learning):**
  - Observe 2+ weeks before attempting trades.
  - Do not force trades; let price confirm bias through observable action at levels.
  - Document whether price does what it "should" do; if not, that is valuable data.
  - If a setup is unclear or price is acting unexpectedly, sit out; no trade is worth the risk of misinterpretation.

## Process, risk & psychology

**Position Management & Stops:**
- ICT uses a multi-contract approach: enter with 2 contracts, peel off 1 on warning signals, trail the stop on the remaining 1.
- Example (0:39:38–0:40:26): if long 2 contracts with a stop below a key low, and price gives a warning (e.g., closes in the lower half of a structure), peel off 1 contract and use the open of that warning candle as the new stop for the remaining contract. This reduces loss if the trade turns, but keeps upside exposure.
- Warning signals (reasons to peel off):
  - Price lays a body in the "wrong half" of a gap/block.
  - Time distortion (too many candles in the gap).
  - Price fails to reach an expected level (consequent encroachment).
  - Lethargic action when should be aggressive.
- ICT emphasizes scaling out and taking partials, not demanding full targets. In hard markets, he has "dialed it back considerably," taking smaller wins and moving on.

**When NOT to Trade:**
- ICT sits out the entire Friday setup (0:20:42 onwards) despite having a clear bearish bias. Reasons: TGIF risk, one-sided move already complete, opening range gap is deep discount, and Friday volatility dynamics.
- He explicitly states: "I would just let it go. Wouldn't do anything with it."
- This teaches the vital lesson: **not trading is a valid trade decision.** Missing a winner because you sat out is better than blowing an account on a bad setup.

**Defensive Mechanisms / Protocols:**
- ICT operates with a checklist of boxes that must be ticked before he enters: market structure, time of day, higher-timeframe narrative, confluence of levels, price action validation (bodies, no time distortion, etc.).
- If the boxes are not all ticked, he sits out. He does not "force" trades for clout or FOMO.
- He tells students: "I want things to be in my favor. And the more things I have in my favor, algorithmically, all the boxes that I like to look for, the more of those being toggled off in my favor that I'm probably going to see the move materialize. Then I'm going to trade in those environments. But if it's likely that I'm going to be wrong… I'm not interested and I wouldn't be a part of this move anymore." (0:86:49)

**Risk Tolerance & Psychology:**
- ICT emphasizes using *micros* (MES, MNQ, micro contracts) when learning and in hard markets. Leverage is evil; he tells students he teaches micros "so that way if you do something wrong in your hands, you don't hurt yourself catastrophically." (0:51:23)
- He criticizes students who FAFO (figure it out) with live funds or funded accounts without backtesting: "you discover you don't know what you're doing. And instead of being responsible and saying, well, I didn't really do the job of testing it, backtesting it, figuring out how I'm supposed to do it myself for a couple months in a row, you just jumped ahead and try to just FAFO and then you did." (0:59:35)
- Mental discipline: "You have to weigh all that stuff out... that's the reality of the market trading in real time with real risks." (0:108:46)

**Current Market Climate:**
- ICT states: "Too many things in the market right now that are concerns" and "we are in a market environment right now that is absolutely war." (0:121–0:122)
- This informs his cautious stance. He has had to dial back precision on exits and be more flexible because of "interference constantly coming in." (0:127:56)
- He expects the market to be "hard" for an extended period and adjusts strategy accordingly: tighter stops, smaller targets, willingness to sit out.

**Journaling & Backtesting:**
- ICT expects students to spend weeks in tape-reading mode, documenting price action, checking whether their model holds water.
- Example (0:78:46–0:79:35): "In the beginning, you shouldn't expect to know what you're doing cuz you have to discover whether or not these things I'm teaching you hold water or not. So many of you skip over that."
- The practice is the foundation; rushing to live trading or funded accounts is the fastest way to wreck an account.

**Mindset / Humility:**
- ICT explicitly says: "I know everything because there's interference constantly coming in… I don't know everything… I don't know that. I'm right a couple times, but I don't… I have to sit and wait." (0:130:32)
- He also says: "I'm not smart. I'm just blessed. And I prefer being blessed over being smart." (0:124)
- This reflects humility: markets are hard, you can't control external interference, and respecting risk is more important than being right.

## Glossary candidates

`SIBI` — Sell-side imbalance / buy-side inefficiency; a volume imbalance where the bodies are in the upper part of the gap (sell-side liquidity has been taken out, creating an imbalance below).

`BISI` — Buy-side imbalance / sell-side inefficiency; a volume imbalance where the bodies are in the lower part of the gap (buy-side liquidity has been taken out).

`Consequent Encroachment` — The midpoint of a gap or wick; a precise level, not a range. Failure to reach it indicates weakness.

`Consequent Correction` — Similar to consequent encroachment but applied to a wick that has gapped below it; the midpoint of that wick used as resistance.

`Time Distortion` — Price spending more than 1–2 candles inside a FVG or gap, indicating lack of conviction and weakness in the expected direction.

`Balanced Price Range (BPR)` — A PD array that has been traded both above and below, making it neutral; neither support nor resistance until broken decisively.

`TGIF` — "Thursday Is FUN"; Friday is a high-risk day for shorts due to extreme weekend gap risk; price often gaps open lower on Sunday rather than delivering on Friday.

`Suspension Block` — A consolidation range (high/low) followed by a break; interior structure that defines support/resistance based on which half price trades in upon re-entry.

`Breaker Block` — Similar to a suspension block; a range structure where price is expected to respect the midpoint upon re-entry after a breakout.

`Order Flow` — The visual representation of open, high, low, close (OHLC) on a candle; real order flow requires no footprint data or advanced tools, only observation of bodies and wicks.

`Tape Reading` — The practice of observing price action (bodies, wicks, levels, time) without trading, to learn whether a model holds water; a learning method, not a trading method.

`Judas Swing` — A false break in one direction (e.g., below a low) followed by a sharp reversal, designed to trap traders and generate liquidity for the real move.

`Discount / Premium / Equilibrium` — Discount: price in the lower half of a daily range. Premium: price in the upper half. Equilibrium: price at the midpoint.

`Liquidity Pool` — A concentration of stops resting at or near a swing high or low; market makers hunt these levels for fill and reversal.

`Draw on Liquidity (DOL)` — Price moving to and potentially through liquidity (e.g., to a prior swing high, especially on a liquidity run).

`Opening Range Gap (ORG)` — The gap between pre-market / prior day close and the 9:30 ET RTH open; defines initial session bias.

`RTH` — Regular Trading Hours; 9:30 am to 4:00 pm ET.

`Tomfoolery / Shenanigans` — Manipulation or false moves by market makers, especially in pre-market or post-market sessions.
