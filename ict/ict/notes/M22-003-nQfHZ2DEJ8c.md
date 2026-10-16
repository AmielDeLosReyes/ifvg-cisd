# M22-003 — 2022 ICT Mentorship Episode 3
ID: nQfHZ2DEJ8c · URL: https://www.youtube.com/watch?v=nQfHZ2DEJ8c · Duration: 52:27
Content type: mixed (lecture + live trade)
Teaching density: high

## Summary
Recorded Tuesday, January 25, 2022: the "internal range liquidity and market structure shift" lecture. ICT defines the intraday Market Structure Shift (MSS) — a short-term swing high/low broken, but significant ONLY after price has first traded into liquidity (sell stops under an old low / buy stops above old highs) — and shows the earliest entry is the FVG created by the shifting candle. He gives his own definition of the order block as a "change in the state of delivery" (the opening price of a run of same-direction candles; when that open is violated the algorithm switches from offering one side to the other) — an early form of what later becomes CISD. He sets the session times to mark (London 2–5 AM, NY 7–10 AM, Asia 7–9 PM ET), trading hours (8:30–11:00, up to noon), defines internal range liquidity, assigns backtesting/journaling homework, and finishes with a live NQ long on TD Ameritrade from a bullish FVG (with stacked-FVG handling rule) targeting an imbalance in premium for about +$1,190.

## Concepts
### Market Structure Shift (MSS) vs market structure break  (aliases ICT uses: "intraday market structure shift", "shift in market structure", "break in market structure")
- **Kind:** definition / rule
- **What ICT says:** For intraday use he says "shift", not "break". An intraday MSS signals a likely intraday draw up or down; it may produce just an intraday leg and the opposing high can still be taken the same day. "Market structure break" means more in context (can lead to prolonged multi-day movement). You do not force or anticipate ahead of the shift; you wait for the evidence. He says this is the complete, algorithmic definition — nothing else is needed.
- **How to identify:** (1) Price runs liquidity first: trades below an old low (sell stops under retail "support": a double bottom or single low) or above old highs/relative equal highs. (2) The short-term swing high (for bullish) formed right before the low is taken out — a swing high = a candle with lower highs on both sides. (3) The candle that trades through that short-term high: it does NOT need to close above it. The break is significant ONLY if liquidity was taken first.
- **How to use:** After the MSS candle closes, watch the next candle: when it closes, has an FVG been created? That FVG is the earliest place to trade. Bearish mirror: after buy stops are taken, a short-term swing low is broken and an FVG forms; sell the retrace into it.
- **Example in this video:** NQ March 2022 15m (homework chart): old low ~14,600 with sell stops below it; relative equal highs ~14,820–14,860 (caption gives both) with buy stops above. 2m chart same day: price dives under ~14,600 into sell stops, then rallies through the short-term swing high formed before that low ("light bulb" candle) — bullish MSS; the next candles leave an FVG, price trades down into it and "takes off" to run buy stops above the highs and through the relative equal highs. Then above the equal highs, a swing low forms and is broken — bearish MSS (because buy stops were taken); rally into the FVG = short, targeting sell stops below lows and an imbalance below the 50% of the range.
- **Timestamps:** [0:01:50](https://youtu.be/nQfHZ2DEJ8c?t=110) — anticipate MSS at the liquidity points, don't force it; [0:02:39](https://youtu.be/nQfHZ2DEJ8c?t=159) — shift vs break; [0:06:35](https://youtu.be/nQfHZ2DEJ8c?t=395) — short-term high taken is significant only if price ran sell stops; [0:13:45](https://youtu.be/nQfHZ2DEJ8c?t=825) — need not close above; watch next candle for FVG.
- **Nuance / caveats / changes:** He notes there are ways to sell right above the highs (or buy at the low) without waiting for the MSS, but says students won't have that skill yet. HFT algorithms use market structure on 3m/2m/1m and sub-minute (45s/30s/15s) charts.

### Buy-side / sell-side liquidity (marking the pools)  (aliases ICT uses: "buy stops", "sell stops", "relative equal highs", "retail support/resistance")
- **Kind:** rule
- **What ICT says:** Old low → sell stops below. Relative equal highs → buy stops above. If equal highs exist and they are higher than an older single high, he uses the equal highs as the reference. Liquidity location is pure logic: retail places stops beyond obvious support/resistance. Buying/selling "pressure" has no bearing on where price goes. Highs left just below a level "building up more interest" engineer liquidity for a later run.
- **How to identify:** Mark the 15m buy-side and sell-side liquidity pools, then drop to 3m/2m/1m.
- **How to use:** The run into these pools is the precondition for the MSS. When the market runs buy stops, smart money that bought lower sells to "high-seeking buyers".
- **Example in this video:** NQ 15m: shaded sell-stop area below ~14,600; relative equal highs above.
- **Timestamps:** [0:01:04](https://youtu.be/nQfHZ2DEJ8c?t=64) — old low and relative equal highs; [0:12:56](https://youtu.be/nQfHZ2DEJ8c?t=776) — sell-stop zone below 14,600; [0:28:03](https://youtu.be/nQfHZ2DEJ8c?t=1683) — highs building interest = engineering liquidity.
- **Nuance / caveats / changes:** none.

### Fair Value Gap (FVG) as MSS entry; stacked FVGs rule
- **Kind:** entry model / refinement
- **What ICT says:** FVG = a candle with one single pass up, and the next candle's low doesn't fully overlap the prior candle's high (gap remains). The candle after the MSS that forms an FVG is "at the earliest" where you'd trade. When there are two FVGs, one above the other (for a long), he lets price trade down into the lower one, sacrificing that better entry; if it trades into the lower one and comes back up into the higher (first) FVG, he enters there and expects the lower one won't be retraded. If price runs up into the target zone first, before retracing to the entry FVG, he nixes the trade and sits out.
- **How to identify:** After an MSS, the gap left by the displacement candle.
- **How to use:** Enter on the retrace into the FVG (limit or market). During the trade, a dip back into the lower FVG is permissible; if price overlaps the entire lower FVG and goes lower, close the trade (save the stop). Watch whether candle bodies stay inside the FVG (sign of accumulation).
- **Example in this video:** Live NQ 1m, Jan 25, 2022: bullish MSS, green-box FVG with a smaller FVG just below it. Price dips into the lower FVG, leaving wicks, comes back into the green FVG; he buys at market. Price stabs down once more into the wicks (he says they took it down to accumulate more longs, not selling pressure); max drawdown about $455. Then rallies to the bottom of the pink rectangle (an imbalance in premium) where he flattens: +$1,190, account $27,915.11.
- **Timestamps:** [0:13:45](https://youtu.be/nQfHZ2DEJ8c?t=825) — FVG after MSS, earliest entry; [0:41:38](https://youtu.be/nQfHZ2DEJ8c?t=2498) — two FVGs rule; [0:43:12](https://youtu.be/nQfHZ2DEJ8c?t=2592) — nix trade if target hit first; [0:45:36](https://youtu.be/nQfHZ2DEJ8c?t=2736) — permissible dip into lower FVG; close if it overlaps fully.
- **Nuance / caveats / changes:** He says he only draws these on the chart for teaching; trades a naked chart.

### Order block = change in the state of delivery  (aliases ICT uses: "one continuous order block", "consecutive bearish order block", "change in the state of delivery")
- **Kind:** definition / refinement
- **What ICT says:** He invented the order block (first mentioned on BabyPips in 2010; taught one-on-one since 1996). Not every down-close candle is a bullish OB (or up-close a bearish OB). A series of consecutive down-close candles is "all one continuous order block"; the reference is the opening price of the first candle of that series, extended out in time. The order block "is just a change in the state of delivery": while price is delivered higher via a run of up-close candles, that run began at the first candle's open; when price trades below that open, the state of delivery changes (from offering buy side to offering sell side, i.e., now seeking sell stops), and the algorithm "remembers" that level, making it sensitive. Mirror for down-close candles: when their opening price is violated upward, it changes to offering buy side and seeks buy stops.
- **How to identify:** A high-probability OB: (1) it sits inside a liquidity pool (e.g., the down-close series inside the sell-stop zone), (2) has an FVG/gap, (3) there was a market structure shift. "Takes liquidity + gap + MSS."
- **How to use:** Bullish: buy limit at the opening price of the down-close candle series, located inside the FVG, plus about 3 pips "or whatever for spread". Bearish: mirror with up-close candles.
- **Example in this video:** NQ 2m: series of down-close candles inside the sell-stop pool below 14,600; their opening price lies inside the FVG = buy limit; price runs to buy stops above highs. NQ 1m: two up-close candles before a drop form one consecutive bearish OB (open extended out), with gap, liquidity taken and MSS: "high probability" bearish OB.
- **Timestamps:** [0:14:32](https://youtu.be/nQfHZ2DEJ8c?t=872) — down-close series = one order block; [0:15:20](https://youtu.be/nQfHZ2DEJ8c?t=920) — open of series inside FVG = buy limit; [0:23:16](https://youtu.be/nQfHZ2DEJ8c?t=1396) — bearish OB with gap, liquidity and MSS; [0:24:06](https://youtu.be/nQfHZ2DEJ8c?t=1446) — OB = change in state of delivery.
- **Nuance / caveats / changes:** This is the root of the later "CISD" concept. He says that's all he'll give at the free level. He criticizes others for treating every opposite-colored candle as an OB.

### Price delivery by algorithm (not buying/selling pressure)
- **Kind:** definition
- **What ICT says:** When price rallies, the HFT orders hitting the market are volume, not the cause; the price-delivery algorithm keeps offering price higher. Explains slippage: market buy expected at 14,662 filled at 14,664 = negative slippage; filled better = positive slippage. "Bull squeeze/bear squeeze" are cop-outs.
- **How to identify:** n/a.
- **How to use:** Don't interpret price via pressure/volume; read liquidity and delivery state.
- **Example in this video:** NQ 1m rally after MSS.
- **Timestamps:** [0:20:55](https://youtu.be/nQfHZ2DEJ8c?t=1255); [0:21:43](https://youtu.be/nQfHZ2DEJ8c?t=1303).
- **Nuance / caveats / changes:** Belief statement; he challenges students to verify in charts.

### Premium / discount; targets & partials (low-hanging fruit)
- **Kind:** rule (applied)
- **What ICT says:** Bearish leg: price goes from premium to below the 50% (equilibrium) of the range into discount, into the gap there. Partials can be taken below each short-term low (sell stops), but don't take them where there's too little movement; reach for the next one. First objective = the high end of the target FVG (the closest candle's low/high), the easiest target; over time grow into holding to see it fill the whole gap.
- **How to identify:** 50% of the leg's high and low; FVG/imbalance below.
- **How to use:** Multiple contracts: scale out at successive sell-stop pools and the FVG in discount. Live trade: exit at the low end of the target rectangle; the ideal is the top, but while learning take the low end.
- **Example in this video:** NQ 2m bearish leg to FVG below 50%; live long target = bottom of pink imbalance in premium.
- **Timestamps:** [0:17:43](https://youtu.be/nQfHZ2DEJ8c?t=1063) — targets below; partials; [0:19:20](https://youtu.be/nQfHZ2DEJ8c?t=1160) — 50% level, first objective in gap, low-hanging fruit; [0:27:16](https://youtu.be/nQfHZ2DEJ8c?t=1636) — premium to equilibrium to discount; [0:49:07](https://youtu.be/nQfHZ2DEJ8c?t=2947) — target low end of rectangle.
- **Nuance / caveats / changes:** none.

### Timeframe progression 3m → 2m → 1m
- **Kind:** rule
- **What ICT says:** The same MSS/FVG logic appears on 1m with more execution points; a single gap on 2m may appear as two candles on 1m. Progress from 3m to 2m to 1m to find structure and imbalances.
- **How to identify:** n/a.
- **How to use:** Mark 15m liquidity pools; execute on 3m/2m/1m.
- **Example in this video:** Same NQ day shown on 2m and 1m.
- **Timestamps:** [0:20:07](https://youtu.be/nQfHZ2DEJ8c?t=1207); [0:27:16](https://youtu.be/nQfHZ2DEJ8c?t=1636).
- **Nuance / caveats / changes:** none.

### Session highs/lows to mark (killzone-like windows)  (aliases ICT uses: "London session", "New York session", "Asia")
- **Kind:** rule
- **What ICT says:** Always use New York local time. London session 2:00–5:00 AM; New York session 7:00–10:00 AM; Asia 7:00–9:00 PM (caption). Mark each session's high and low: the market will probably sweep above those highs or below those lows and create MSS setups. Also mark any intraday high/low forming right before the 9:30 equities open.
- **How to identify:** Session high/low in each window.
- **How to use:** These are the "key highs and lows" whose sweep precedes the MSS.
- **Example in this video:** n/a.
- **Timestamps:** [0:32:52](https://youtu.be/nQfHZ2DEJ8c?t=1972); [0:33:40](https://youtu.be/nQfHZ2DEJ8c?t=2020).
- **Nuance / caveats / changes:** The Asia window as captioned (7–9 PM) is narrower than his usual Asian killzone; treat as stated.

### Trading hours, lunch, and afternoon session
- **Kind:** rule
- **What ICT says:** Hours of operation generally 8:30–11:00 AM NY, can extend to noon. He does not tend to trade after noon; the noon hour (lunch) is problematic — don't even look for setups. Wait until 1:00 PM, preferably 1:30–4:00 PM for the afternoon trend; a setup usually forms between 2:00 and 3:00 PM. The afternoon session is outside this mentorship's scope.
- **How to identify:** n/a.
- **How to use:** Backtest/stalk 8:30–noon ET.
- **Example in this video:** n/a.
- **Timestamps:** [0:33:40](https://youtu.be/nQfHZ2DEJ8c?t=2020); [0:34:28](https://youtu.be/nQfHZ2DEJ8c?t=2068).
- **Nuance / caveats / changes:** none.

### Internal range liquidity (IRL)
- **Kind:** definition
- **What ICT says:** IRL = short-term lows or highs inside a price leg that price is retracing back into; i.e., a short-term high or low with stops above/below it, or an imbalance in that same range.
- **How to identify:** Within the current leg, swing points and FVGs.
- **How to use:** Targets/partials when retracing within a leg.
- **Example in this video:** Sell stops below internal short-term lows in the bearish NQ leg.
- **Timestamps:** [0:34:28](https://youtu.be/nQfHZ2DEJ8c?t=2068); [0:35:15](https://youtu.be/nQfHZ2DEJ8c?t=2115).
- **Nuance / caveats / changes:** External range liquidity not defined here.

## Rules, checklists & numbers stated
- MSS is valid only after liquidity is taken (old low/high, double bottom/top, relative equal highs/lows).
- The breaking candle need not close beyond the short-term high/low.
- Earliest entry: the FVG formed after the MSS candle.
- Two stacked FVGs: allow the lower one to be hit; enter when price comes back to the upper one; abort if target hit first; close if the lower FVG is fully overlapped and price goes lower.
- Order block entry: buy limit at the opening price of the down-close series inside the FVG (+~3 pips spread for forex).
- Sessions (NY time): London 2–5 AM, NY 7–10 AM, Asia 7–9 PM (as captioned); also the high/low before 9:30.
- Trade window: 8:30–11:00 AM, extendable to noon; no trades during noon hour; afternoon 1:30–4:00, setup often 2–3 PM (out of scope).
- MNQ (micro): $2 per handle, $0.50 per tick; NQ: $20 per handle, 4 ticks per handle.
- His risk: about 3.25% on this trade; comfortable 3–3.5%; maximum 4.5% per trade "when trading competitively" (not a recommendation).
- Homework: on e-mini intraday charts 8:30–noon ET, find stop hunts leading to MSS on 3/2/1m; annotate 15m BSL/SSL pools; log examples back as far as data allows.

## Process, risk & psychology
- Backtesting = dressing the chart up with annotations and studying it: how many points/pips it moved, how long, how much drawdown a position would have taken; save in a study journal ([0:38:28](https://youtu.be/nQfHZ2DEJ8c?t=2308)).
- Revisit the study journal in periods of confusion; examples encourage you ([0:39:14](https://youtu.be/nQfHZ2DEJ8c?t=2354)).
- The volume of backtesting and logging examples "is the secret"; most people claim to do it but don't ([0:40:01](https://youtu.be/nQfHZ2DEJ8c?t=2401)).
- Hunter analogy: you must be shown what the "deer track" looks like, then find it yourself ([0:36:52](https://youtu.be/nQfHZ2DEJ8c?t=2212)).
- Keep charts naked while trading to remain flexible; heavy annotations lock you into "your will be done" ([0:31:15](https://youtu.be/nQfHZ2DEJ8c?t=1875), [0:32:04](https://youtu.be/nQfHZ2DEJ8c?t=1924)).
- In a live trade, watch the chart, not the P&L number; pre-accept likely drawdown scenarios to desensitize yourself ([0:45:36](https://youtu.be/nQfHZ2DEJ8c?t=2736), [0:47:29](https://youtu.be/nQfHZ2DEJ8c?t=2849)).
- Uses a flatten button at the target to cancel all orders and exit ([0:49:53](https://youtu.be/nQfHZ2DEJ8c?t=2993)).
- Faith in the setup comes from seeing it work many times; without it, never use live money ([0:42:26](https://youtu.be/nQfHZ2DEJ8c?t=2546)).

## Glossary candidates
`Market structure shift (MSS)` — intraday break of a short-term swing high/low after liquidity was taken; signals an intraday draw.
`Change in the state of delivery` — when the opening price of a series of same-direction candles is violated, the algorithm switches from offering one side to the other; ICT's definition of an order block (precursor to CISD).
`Offering buy side / sell side` — algorithm delivering price up to buy stops / down to sell stops.
`Internal range liquidity (IRL)` — short-term highs/lows (stops) or imbalances inside the leg price is retracing into.
`Engineering liquidity` — price building repeated highs/lows just below a level so stops accumulate for a later run.
`Flatten` — platform button that cancels all orders and exits the position.
