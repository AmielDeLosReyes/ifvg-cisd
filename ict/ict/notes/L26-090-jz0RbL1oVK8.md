# L26-090 — ICT 2026 Trading MNQ Futures & CFD US 100, April 28, 2026
ID: jz0RbL1oVK8 · URL: https://www.youtube.com/watch?v=jz0RbL1oVK8 · Duration: 30:54
Content type: live trade + execution
Teaching density: high

## Summary
Live execution tape on MNQ (Nasdaq 100 micro futures) short and US 100 CFD equivalent, demonstrating how to identify and execute a short from an inversion FVG + order block setup, use the "ICT gray pool" for precision targeting, manage stops, take partials at event horizon, and scale into sell-side liquidity. Proves CFD and futures equivalence by trading both simultaneously. Shows real-time order flow: respecting consequent encroachment, tracking wick behavior, recognizing gray pools, and executing with conviction.

## Concepts

### ICT Gray Pool (Two-Wick Liquidity Pool)
- **Kind:** new coinage
- **What ICT says:** The ICT gray pool is a liquidity zone formed by measuring the consequent encroachment of two adjacent wicks. You split the area between the two CE levels in half; the midpoint becomes a magnet on price and, when entered from above, acts as "rocket fuel" to send price lower. This is a proprietary technique ICT teaches; it is not published anywhere else.
- **How to identify:** Identify two discount wicks on a down move. Measure the CE of each; the gap between the two CEs is your gray pool. Mark the midpoint.
- **How to use:** Gray pool is used as an entry confirmation / accumulation zone. When price returns to the gray pool from above, expect a sharp drop through it. If price respends time in the pool (too many candles), give it 2–3 more candles to show willingness to move lower; if it doesn't, exit or re-evaluate.
- **Example in this video:** MNQ April 28, 2026. Two wicks (discount wicks) were measured; the CE of each was marked; the midpoint of the gray pool was ~27,205 (approximate). Price traded down into the gray pool, confirming the expected drop lower.
- **Timestamps:** [0:11:58](https://youtu.be/jz0RbL1oVK8?t=718) — gray pool creation · [0:13:37](https://youtu.be/jz0RbL1oVK8?t=817) — gray pool function as "rocket fuel" · [0:20:04](https://youtu.be/jz0RbL1oVK8?t=1204) — gray pool return confirmation · [0:23:16](https://youtu.be/jz0RbL1oVK8?t=1396) — time stop within gray pool
- **Nuance / caveats / changes:** Gray pool bodies must stay out of the upper half; if price allows bodies in the upper half, the setup is compromised and re-evaluation is needed.

### Event Horizon (Gap Between Liquidity Pools)
- **Kind:** definition
- **What ICT says:** Event horizon is the area between two liquidity points (e.g., between a gray pool and a sell-side liquidity pool, or between two relative equal lows). It marks a transition zone. When price pierces through event horizon with conviction, the next liquidity target becomes more likely. It is a measurement tool for partial profit-taking and conviction building.
- **How to identify:** Identify two sequential liquidity points (gray pool low, then the next sell-side pool, or two relative equal lows); the gap between them is the event horizon.
- **How to use:** Use event horizon as a partial-profit-taking zone. When price reaches event horizon, take 20–50% of position. Track whether price moves through event horizon quickly (strong) or slowly (weak). Speed of movement = confidence in the continuation.
- **Example in this video:** MNQ April 28. Event horizon was marked between the gray pool midpoint and the sell-side liquidity pool at ~27,069. Price needed to break through this area with heaviness (stretched out candles, extended bodies). When it did, ICT took 2–3 lots off the 10-lot position.
- **Timestamps:** [0:24:04](https://youtu.be/jz0RbL1oVK8?t=1444) — event horizon identified · [0:27:20](https://youtu.be/jz0RbL1oVK8?t=1640) — speed through event horizon as signal
- **Nuance / caveats / changes:** Do not demand a measured move through event horizon; speed and heaviness matter more than hitting exact price.

### Relative Equal Lows as Final Target
- **Kind:** example only
- **What ICT says:** After gray pool, event horizon, and sell-side liquidity pool come into play, the final target is often relative equal lows (prior swing lows repeated at similar price). These are the ultimate liquidity pools where market makers will run shorts' stops and absorb selling pressure.
- **How to identify:** Mark prior swing lows on the daily and intraday charts; if multiple are clustered within a few ticks, that is a relative equal low.
- **How to use:** Target relative equal lows as the final profit-taking zone. Do not expect price to go beyond relative equal lows easily; use them as hard stops for taking profits or managing the full position.
- **Example in this video:** MNQ April 28. Relative equal lows were at ~27,069 (MNQ futures) and ~2.6970 (US 100 CFD). ICT called these out on X pre-market and executed toward them. Price hit them and reversed, confirming the setup.
- **Timestamps:** [0:00:01](https://youtu.be/jz0RbL1oVK8?t=1) — short targeting relative equal lows · [0:29:42](https://youtu.be/jz0RbL1oVK8?t=1782) — relative equal lows hit and reversed
- **Nuance / caveats / changes:** None stated.

### Opening Range Gap (ORG) & Quadrants / Octants
- **Kind:** definition
- **What ICT says:** At the 9:30 AM ET open, the market creates a gap relative to yesterday's close. This gap is divided into quadrants (25% sections). The opening price at 9:30 and the high/low of the ORG are reference points. On April 28, the 9:30 opening was at 27,184.25 (MNQ); this became a magnet on price during the session.
- **How to identify:** Mark yesterday's close, mark the 9:30 open; the gap between them is the ORG. Divide into quadrants.
- **How to use:** Use the opening price as a reference; when price returns to it, expect either a bounce or a break-through depending on structure. In this session, price aimed to return to the 9:30 open on the short move.
- **Example in this video:** MNQ April 28. 9:30 open at 27,184.25; lower quadrant at 27,227.75. Price moved down from pre-market highs to eventually target the 9:30 open level.
- **Timestamps:** [0:00:49](https://youtu.be/jz0RbL1oVK8?t=49) — quadrant level reference · [0:04:51](https://youtu.be/jz0RbL1oVK8?t=291) — opening price as magnet
- **Nuance / caveats / changes:** On volatile days (high geopolitical uncertainty), the ORG may be less reliable; use it as reference but remain flexible.

### Inversion Fair Value Gap (iFVG) as Resistance
- **Kind:** example only
- **What ICT says:** An iFVG (a bullish FVG approached from above) acts as resistance. When shorting, price must stay out of the upper half of the iFVG; if bodies enter the upper half, weakness is confirmed. If bodies cannot return to the consequent encroachment level on rallies, the iFVG is being strongly respected (bearish signal).
- **How to identify:** Mark the original bullish FVG; observe how price treats it on the way down.
- **How to use:** Short entries can be placed just below the iFVG high. Use the iFVG high as a stop-loss level or as a reference for "does the structure hold?"
- **Example in this video:** MNQ April 28. An upper inversion FVG was marked; on the way down, bodies were not allowed in the upper half, confirming bearish order flow and conviction to move lower.
- **Timestamps:** [0:03:17](https://youtu.be/jz0RbL1oVK8?t=197) — iFVG identified · [0:06:24](https://youtu.be/jz0RbL1oVK8?t=384) — bodies respecting iFVG upper half
- **Nuance / caveats / changes:** None stated.

### Judas Swing
- **Kind:** definition
- **What ICT says:** A Judas swing is when price moves into a bullish order block, briefly reverses (creating a "fake out"), and then continues in the original direction. It "deceives" traders expecting a reversal.
- **How to identify:** Look for a sharp move into an order block, a quick reversal wick, and then a resumption of the original direction.
- **How to use:** Recognize Judas swings as entry confirmation, not as rejection of the setup. When you see a Judas into an order block on the expected direction, it is often a signal to add to the position.
- **Example in this video:** MNQ April 28. Price moved down, briefly "icked" up into the bullish order block on the daily chart (Judas swing), then continued lower (confirming the short thesis).
- **Timestamps:** [0:08:46](https://youtu.be/jz0RbL1oVK8?t=526) — Judas swing into order block
- **Nuance / caveats / changes:** A Judas swing is not a failed entry; it is confirmation of the direction.

### Gray Pool Entry & Time Stop
- **Kind:** rule + execution
- **What ICT says:** When price re-enters a gray pool after the initial move, expect a sharp drop. If price spends too many candles in the gray pool (more than 3–4), use a time stop: give it 2–3 more candles to show willingness to move lower; if it doesn't, exit the position and reassess.
- **How to identify:** Track how many candlesticks are forming inside the gray pool area.
- **How to use:** If 3–4 candles have formed in the gray pool without a strong lower move, manually close the trade or reduce size. This prevents being caught in a potential reversal.
- **Example in this video:** MNQ April 28. Price re-entered the gray pool; after spending several candles there, ICT noted "needs to show willingness to drop" and set a time stop of 2–3 more candles. When the next candle showed heaviness (extended body), the time stop was satisfied.
- **Timestamps:** [0:23:16](https://youtu.be/jz0RbL1oVK8?t=1396) — time stop within gray pool
- **Nuance / caveats / changes:** This is a discretionary risk management technique; it helps avoid being stopped out on artificial bounces.

### Sell-Side Liquidity Pool (SSLP) / Minor Sell Side
- **Kind:** definition
- **What ICT says:** A sell-side liquidity pool is a zone where sellers' stop-losses are clustered (above a market low). When price approaches this area, market makers will often run those stops briefly before allowing a larger continuation move. A minor sell side is a smaller cluster of liquidity; a major sell side is a larger one. Always identify the CE of the sell-side wick before breaking through.
- **How to identify:** Identify a wick that left behind inefficiency on the way down. The consequent encroachment of that wick marks the minor sell-side level.
- **How to use:** Before breaking below the sell-side level on a close, confirm the order flow by tracking whether bodies are respecting the midpoint. Once bodies close below the minor sell side with heaviness, the move lower is confirmed.
- **Example in this video:** MNQ April 28. A minor sell-side level was at ~27,082 (approximate, from wick CE); price had to close below this with heaviness to confirm the continuation to the relative equal lows.
- **Timestamps:** [0:11:58](https://youtu.be/jz0RbL1oVK8?t=718) — sell-side liquidity pool identified · [0:16:03](https://youtu.be/jz0RbL1oVK8?t=963) — minor sell side respecting and breakage
- **Nuance / caveats / changes:** Do not close below the minor sell side with just a wick; bodies must close below it for confirmation.

### Position Sizing & Partial Profit-Taking
- **Kind:** rule / execution
- **What ICT says:** Enter with a full position (e.g., 10 lots on MNQ). Use event horizon and relative equal lows as partial-profit-taking zones. Take 2–3 lots (20–30%) at event horizon. Let the rest run to the final target (relative equal lows). Once at relative equal lows, close all remaining lots or trail a stop.
- **How to identify:** Pre-plan your targets (gray pool, event horizon, relative equal lows); assign position reduction targets for each.
- **How to use:** Execution: enter 10 lots. At event horizon, close 2–3. At relative equal lows, close the remainder. This locks in profits early while still allowing the best runners to work.
- **Example in this video:** MNQ April 28. ICT entered 10 lots; took 2–3 lots off at event horizon (around 27,069); held 7–8 lots for the final target, closing them at the relative equal lows when price hit the target on X.
- **Timestamps:** [0:24:04](https://youtu.be/jz0RbL1oVK8?t=1444) — partial at event horizon · [0:25:45](https://youtu.be/jz0RbL1oVK8?t=1545) — position size and scaling
- **Nuance / caveats / changes:** If event horizon is reached quickly and with strong conviction, take more off (4–5 lots). If it's slow, take less.

### Consequent Encroachment (CE) as Hard Stop
- **Kind:** rule
- **What ICT says:** The consequent encroachment of a wick or candle is a hard boundary. When managing a short position, the CE of the iFVG high, the gray pool, and the sell-side wick are all reference points. If any of these CEs are violated by a closing body, stop-loss must be hit.
- **How to identify:** Mark the CE of each key wick/candle; track whether bodies are respecting or penetrating it.
- **How to use:** Place stops just above the CE of the iFVG or just above the gray pool high. Trail stops as price moves lower, placing new stops above the CE of each subsequent resistance level.
- **Example in this video:** MNQ April 28. Stop loss was placed above the initial iFVG CE; as the move developed, the stop was trailed down above the gray pool and then above the minor sell-side CE.
- **Timestamps:** [0:05:38](https://youtu.be/jz0RbL1oVK8?t=338) — stop placement above CE · [0:20:51](https://youtu.be/jz0RbL1oVK8?t=1251) — bodies respecting CE
- **Nuance / caveats / changes:** Always respect the CE; do not try to trail stops inside the structure or you risk getting stopped out.

## Rules, checklists & numbers stated
- Entry: Inversion FVG high (after Judas swing into bullish order block on daily).
- Stop loss: Just above the iFVG CE (or trailing upward as price moves lower).
- Gray pool: Identified by measuring CE of two wicks; midpoint is the magnet.
- Time stop in gray pool: If 3–4 candles form without a lower move, exit on the 3rd candle.
- Minor sell side: Identified by wick CE; must close below this level with body (not wick).
- Event horizon: Between gray pool and sell-side pool; partial-profit-taking zone.
- Relative equal lows: Final target; close remaining position when reached.
- Position size: 10 lots; take 2–3 at event horizon; close 7–8 at relative equal lows.
- CFD vs futures: Transposable; price points differ slightly; structure is identical.
- MNQ 9:30 open April 28: 27,184.25.
- Relative equal lows target: 27,069 (MNQ) / 2.6970 (US 100).

## Process, risk & psychology
- **Pre-market planning:** ICT posted the setup on X (Twitter) pre-market, showing targets and rationale. This allows real-time verification of the call.
- **Dual-market confirmation:** By trading MNQ and US 100 simultaneously, ICT verified that the structure works across different instruments and that CFD is a valid alternative to futures.
- **Patience in gray pool:** When price spent too long in the gray pool, ICT used a time stop to prevent being caught off guard. This is a practical risk-management tool.
- **Partial profit-taking:** By closing 20–30% at event horizon, ICT locked in profit and reduced risk. The remaining position had unlimited upside (from ICT's perspective, unlimited downside on a short).
- **Stop trailing:** Stops were trailed down as price moved lower, reducing risk as the trade worked in favor. This is a core money-management rule.
- **Heaviness as confirmation:** ICT emphasized "stretched out candles" and "extended bodies" as signals of strong order flow. This is visual order flow reading, not indicator-based.
- **No arrogance:** ICT noted "I might be wrong with this" even as the trade was working. This shows humility and willingness to adapt despite early success.

## Glossary candidates
`ICT gray pool` — a liquidity zone formed by the gap between the consequent encroachments of two adjacent discount wicks; a magnet for price and source of "rocket fuel" for continuation moves.
`Event horizon` — the gap between two sequential liquidity pools (e.g., between gray pool and sell-side pool); a partial-profit-taking zone and transition marker.
`Consequent Encroachment (CE)` — the first candlestick body to enter a liquidity pool; a hard boundary that must not be violated without stopping the position.
`Minor sell side / Major sell side` — clusters of stop-losses above a swing low; minor = small cluster, major = large cluster.
`Sell-side liquidity pool (SSLP)` — an area where sellers' stops are concentrated; market makers target this zone before allowing continuation lower.
`Judas swing` — a brief reversal into a bullish order block before continuation in the original (downside) direction; a setup confirmation, not a rejection.
`Relative equal lows` — prior swing lows that repeat at similar price; ultimate liquidity targets on downside moves.
`Time stop` — a discretionary exit if the position spends too many candles in a consolidation zone without showing directional conviction.
`Heaviness` — visual representation of strong order flow: extended candlestick bodies, stretched wicks, clear directional bias without reversals.
