# M22-018 — 2022 ICT Mentorship Episode 18
ID: eai0nHhAC8w · URL: https://www.youtube.com/watch?v=eai0nHhAC8w · Duration: 1:01:07
Content type: lecture (step-by-step top-down walkthrough of one EURUSD day + chart setup/backtesting method)
Teaching density: high

## Summary
ICT shows his TradingView layout (daily top-left, hourly bottom-left, 15m "bellwether" chart on the right, drawings linked across timeframes, chart set to New York time) and walks the full top-down process on EURUSD for Thursday, 7 April 2022 — the follow-through of the bearish bias from Ep. 17. Daily: bearish bias, 5 down days put price in discount, so expect a bounce into a daily FVG; use the **previous day's high and low** as the intraday framework (premium level / target). Intraday: price rallies above relative equal highs into the daily FVG at 9:30 (Judas), displaces down, and a limit sell is placed in the 15m/5m FVG during the FX NY killzone (7–10 a.m.), with the stop above the intermediate-term high; target the 6 April low, filled at 2:45 for ~40 pips. The key conceptual content is a sharpened **order block** definition: an OB is only valid with an imbalance; a run of consecutive up-close candles is one OB; price need not reach the last up-close candle when the parent HTF imbalance stops it; ultimately "an order block is a change in the state of delivery." Also: killzones are for placing orders (cancel unfilled limits by 11:30), the stacked-FVG rule, leverage vs pips of risk, gold is event-driven, and a detailed backtesting/journal routine.

## Concepts

### Daily bias & commit to one direction
- **Kind:** rule
- **What ICT says:** Start bias analysis on the daily chart. A bias is "just an idea that you want to work within": you take shorts when bearish and filter out the other side unless clearly proven wrong. Flip-flopping intraday (going long, then short, back and forth) draws down or blows the account. Your bias won't be perfect and neither is his. Know what you're looking for ahead of time so you're not chasing impulsive swings.
- **Example in this video:** EURUSD bearish bias carried from the Ep. 17 (Tuesday) lesson; draw = the old daily low below.
- **Timestamps:** [0:08:01](https://youtu.be/eai0nHhAC8w?t=481) — bias bearish, FX-specific discussion. [0:11:12](https://youtu.be/eai0nHhAC8w?t=672) — commit to one direction. [0:11:59](https://youtu.be/eai0nHhAC8w?t=719) — bias isn't perfect; filter out the other side.

### Fair Value Gap (daily) — retracement target in discount; only need a touch
- **Kind:** rule
- **What ICT says:** After 5 consecutive down days, with price deep in the range (discount), a retracement is likely. As soon as the daily FVG forms, expect a short-term bounce up into it. Price only needs to trade to the FVG's edge (that candle's high) — "you can be greedy" and wait for the midpoint, deep fill, or full closure, but "I don't need that." Time of day then decides the entry; you don't need to catch the high of the day.
- **Example in this video:** EURUSD daily: big drop toward an old low, next day's candle traded up creating the FVG; Thursday's rally touched it (slightly above the marked premium level).
- **Timestamps:** [0:08:47](https://youtu.be/eai0nHhAC8w?t=527) — only need it to trade into the FVG. [0:15:57](https://youtu.be/eai0nHhAC8w?t=957) — five down days, discount, bounce into FVG.
- **Nuance / caveats / changes:** He says a pattern of high → low → higher high around the daily FVG might look like his "bearish breaker" but is not, because the discount (lower) edge of the FVG — the candle's high — is lower than the swing low (caption reasoning brief; see [0:02:26](https://youtu.be/eai0nHhAC8w?t=146)).

### Previous day's high & low as intraday framework (old highs/lows, last 3 days)
- **Kind:** rule
- **What ICT says:** The daily draw on liquidity (the old low) is not your intraday trade target — it may not happen in one day. Instead frame each day with the previous day's high (premium level) and low (target). There's lots of liquidity around daily highs and lows; "institutional mindset traders" use them and high-frequency algorithms attack them. His first lesson on BabyPips (2009–2010): mark the previous day's highs and lows for the last 3 days — "you're never going to run out of trades."
- **How to use:** Bearish day: expect the open to rally just above the previous day's high (Judas swing) back into the FVG, then sell targeting the previous day's low.
- **Example in this video:** EURUSD: Wednesday's high marked red (premium), Wednesday's low marked as target. Thursday opened, rallied, popped just above the short-term high into the daily FVG, then sold off toward Wednesday's low. Range of opportunity roughly 60 pips (he reads it as from ~…935 to ~…874 — figures caption unclear).
- **Timestamps:** [0:16:45](https://youtu.be/eai0nHhAC8w?t=1005) — targets; mark the FVG-day low. [0:17:32](https://youtu.be/eai0nHhAC8w?t=1052) — daily DOL isn't the intraday target. [0:18:20](https://youtu.be/eai0nHhAC8w?t=1100) — Thursday Judas into FVG; HFT attacks previous day highs/lows. [0:19:08](https://youtu.be/eai0nHhAC8w?t=1148) — last 3 days' highs/lows.

### Chart layout & multi-timeframe workflow (daily → hourly → 15m → 5m)
- **Kind:** rule / process
- **What ICT says:**
  - Layout: upper-left = daily, lower-left = hourly, right (biggest) = 15m. The **15m is his "bellwether" chart** — referenced throughout the day for managing positions, stalking new setups, and trusting intraday bias.
  - TradingView link button: drawings on one timeframe appear on all timeframes of that symbol. With one laptop/screen, just switch timeframes — annotations carry over.
  - Set the chart time zone to **New York** wherever you live, so time-of-day elements match his teaching.
  - Hourly: mark only the frame of reference (daily FVG, liquidity pool, relative equal highs, previous lows), then move to 15m.
  - 15m: vertical daily divider at midnight NY; midnight opening price (15m candle; if scalping use the 5m) drawn out in time to **11:00 a.m. NY**.
  - Don't enter new positions from a phone (too compressed, can't see the lay of the land); managing a trade on a phone is OK.
- **Timestamps:** [0:01:39](https://youtu.be/eai0nHhAC8w?t=99) — daily top-left. [0:23:08](https://youtu.be/eai0nHhAC8w?t=1388) — layout and 15m bellwether. [0:21:33](https://youtu.be/eai0nHhAC8w?t=1293) — no new entries on a phone. [0:28:43](https://youtu.be/eai0nHhAC8w?t=1723) — midnight open extended to 11:00; set chart to New York.

### Relative equal highs (hourly) + midnight open — higher first, then lower
- **Kind:** rule (applied)
- **What ICT says:** On the hourly, the daily FVG also shows, with relative equal highs below/at it (buy-side liquidity pool). On a bearish day, the market wants to "go higher first to go lower": after the midnight open, rally above the relative equal highs into the FVG, then displacement down breaking a swing low and creating an FVG.
- **Example in this video:** EURUSD: 6 April low mapped; new day 7 April at midnight NY. At ~5:25 a.m. NY (London) price swept the previous day's (6 April) low first; he ignored London because it didn't give the rally into his level. The rally into the premium level/daily FVG came at **9:30 a.m. NY**, above the relative equal highs, then displacement lower.
- **Timestamps:** [0:24:44](https://youtu.be/eai0nHhAC8w?t=1484) — hourly relative equal highs. [0:30:20](https://youtu.be/eai0nHhAC8w?t=1820) — rallied above them; displacement; swing low broken; FVG. [0:45:21](https://youtu.be/eai0nHhAC8w?t=2721) — 5:25 a.m. sweep of 6 April low; rally at 9:30.

### Killzones — FX New York session and order placement
- **Kind:** rule
- **What ICT says:**
  - FX NY session/killzone: **7:00–10:00 a.m. NY**; look for the setup to form inside it.
  - Killzones are when you **determine your entry and place your orders**, then walk away — the fill doesn't need to happen inside the killzone. If you can't derive an order placement by then, you have nothing to do that day.
  - If the limit isn't filled by **11:30 a.m.**, pull it — no good-till-cancel. Otherwise it may fill at a bad time of day, keep running through the relative equal highs and stop you out.
- **Example in this video:** EURUSD: setup identified ~10:00 a.m.; limit sell placed.
- **Timestamps:** [0:31:55](https://youtu.be/eai0nHhAC8w?t=1915) — FX killzone 7–10. [0:32:43](https://youtu.be/eai0nHhAC8w?t=1963) — order placed at 10:00. [0:47:42](https://youtu.be/eai0nHhAC8w?t=2862) — pull unfilled order by 11:30. [0:48:29](https://youtu.be/eai0nHhAC8w?t=2909) — killzones are for order placement.

### FVG entry — 15m minimum expectation, refined on 5m (parent/subordinate imbalances)
- **Kind:** entry model / refinement
- **What ICT says:**
  - 15m: after the displacement, put a limit sell at the FVG "or plus one pip"; stop above the high. If the imbalance is very stretched you can use it for the stop; if worried, put the stop above the swing high. This is the "minimum expectation" entry.
  - Then split the 15m down into 5m and look for FVGs inside that 15m down-leg for a fine-tuned entry (5, 4, 3, 2, 1-minute).
  - **Higher-timeframe imbalances are the parent; lower-timeframe imbalances are subordinate.** He rejects a viewer's claim that the smaller-timeframe FVG must form before the HTF one — "it never works like that."
  - You can choose any price within the 5m FVG range — that's where your unique style comes in; the more greedy, the more likely you don't get filled.
  - "Low threshold entry" (first touch) has the most pips of risk, but money risk is controlled by leverage/position size.
- **Example in this video:** EURUSD 5m inside the 15m leg: one small FVG, one stretched FVG, another small FVG; the entry used was in the 5m FVG with a secondary small FVG above it, which price traded up into.
- **Timestamps:** [0:32:43](https://youtu.be/eai0nHhAC8w?t=1963) — 15m limit and stop. [0:33:30](https://youtu.be/eai0nHhAC8w?t=2010) — drop to 5m. [0:34:17](https://youtu.be/eai0nHhAC8w?t=2057) — HTF imbalance is parent. [0:35:54](https://youtu.be/eai0nHhAC8w?t=2154) — pick any price in range; low-threshold entry.

### Stacked FVG rule (small FVG above your FVG)
- **Kind:** rule
- **What ICT says:** If you settle on an FVG and there's a small FVG right above it, expect price may trade up into the upper one — but place your limit in the lower one (it might not reach the upper), and your risk/stop must incorporate the upper one. Overzealous limit prices are "fleeting" — he's teaching how to avoid missing trades and operate consistently.
- **Timestamps:** [0:42:15](https://youtu.be/eai0nHhAC8w?t=2535), [0:43:02](https://youtu.be/eai0nHhAC8w?t=2582), [0:43:49](https://youtu.be/eai0nHhAC8w?t=2629).

### Order block — must have an imbalance; consecutive candles; change in state of delivery
- **Kind:** definition / refinement (corrects popular misuse)
- **What ICT says:**
  - "What makes an order block valid? It has to have an imbalance. Without the imbalance, there is no order block." That's why it's not supply and demand (he doesn't require "fresh" zones; he'll trade through candles/fractals).
  - Three consecutive up-close candles = **one consecutive bearish order block**; "the order block begins with this candle's low" (the lowest candle of the run).
  - Price does **not** need to reach the last up-close candle (the highest one, before the down move) — the common "last up-close candle" definition is wrong here. The reason it's not reached: the higher-timeframe parent imbalance (15m FVG range) stops price there. Trading into the bottom candle of the three is enough.
  - "What is an order block? It's a change in the state of delivery." As soon as price trades below the order-block candle's open, the algorithm starts delivering sell-side; then it breaks the swing low — "changed gears internally."
  - Many YouTubers parrot his order block buzzword without understanding it; learn it from the source.
- **How to identify:** Run of consecutive up-close candles into the premium/HTF array → displacement below the lowest candle's open → swing low broken → FVG present.
- **How to use:** Enter in the FVG that overlaps the lower portion of the OB; disqualify the upper candles (don't expect price to reach the top one).
- **Example in this video:** EURUSD 5m: the run into the daily FVG and above the hourly relative equal highs = 3-candle bearish OB; price traded into the lowest candle and the FVG, not to the last up-close candle; then sold off.
- **Timestamps:** [0:38:17](https://youtu.be/eai0nHhAC8w?t=2297) — three candles = one bearish OB. [0:40:39](https://youtu.be/eai0nHhAC8w?t=2439) — must have an imbalance; not supply & demand. [0:41:26](https://youtu.be/eai0nHhAC8w?t=2486) — why the last up-close candle isn't reached (parent 15m imbalance). [0:46:07](https://youtu.be/eai0nHhAC8w?t=2767) — "it's a change in the state of delivery."
- **Nuance / caveats / changes:** Refines/contradicts the simplified "last up-close candle before the down move" OB used in earlier YouTube teaching; also echoes Ep. 13's requirement of an imbalance. Early statement of the Change in State of Delivery (CISD) idea.

### Market structure shift (internal) & intermediate-term high as stop location
- **Kind:** rule
- **What ICT says:** Breaking the swing low = an internal bearish shift in market structure. Any rally after that is a "suspect rally" setting up another run lower. The high that has the imbalance is an intermediate-term swing high — it should not be exceeded — so the stop goes above it.
- **Timestamps:** [0:43:49](https://youtu.be/eai0nHhAC8w?t=2629) — internal shift. [0:46:56](https://youtu.be/eai0nHhAC8w?t=2816) — suspect rally; intermediate-term high; stop placement.

### Targets — previous day's low; trade result
- **Kind:** example
- **What ICT says:** Target = the 6 April low (previous day's low). The limit sell filled, price broke lower and reached the target at 2:45 (afternoon): ~**40 pips**. Not the highest high and price went a little lower afterwards — "who cares?"
- **Timestamps:** [0:45:21](https://youtu.be/eai0nHhAC8w?t=2721) — target the 6 April low. [0:49:16](https://youtu.be/eai0nHhAC8w?t=2956) — filled at 2:45, ~40 pips.

### Entries & stops — no ultra-tight stops
- **Kind:** rule
- **What ICT says:** Stops of 1 pip or half a pip might work occasionally, but not once you put on size; you'll sweat every tick. Wider (structure-based) stops let you walk away from the chart; he cares where price is going, not whether it touches his stop.
- **Timestamps:** [0:44:35](https://youtu.be/eai0nHhAC8w?t=2675).

### Risk management — leverage, not pips, is the real risk
- **Kind:** rule
- **What ICT says:** A larger stop in pips is not more risk in money — you control the amount via leverage/position size. Leverage is what traders abuse because they ask "how can I make the most?" — the axe that hits the target can come back and hit you in the head.
- **Timestamps:** [0:35:54](https://youtu.be/eai0nHhAC8w?t=2154), [0:36:41](https://youtu.be/eai0nHhAC8w?t=2201).

### Model simplicity (what to ignore)
- **Kind:** rule
- **What ICT says:** If starting over, he'd use only this 2022 model — not the central bank dealer's range, not the Asian range, nothing not mentioned in this model. "This literally is the simplest way to work with intraday and daily order flow." Applicable to forex, bonds, (with caveats) gold.
- **Timestamps:** [0:05:37](https://youtu.be/eai0nHhAC8w?t=337), [0:06:25](https://youtu.be/eai0nHhAC8w?t=385).

### Market selection — gold is event-driven
- **Kind:** rule / opinion
- **What ICT says:** Gold usually needs a geopolitical or "something crazy" event to move; otherwise it's highly manipulated with stop hunts and consolidations — frustrating, not ideal for aggressive short-term trading for new traders (he doesn't deny some people profit in it).
- **Timestamps:** [0:51:39](https://youtu.be/eai0nHhAC8w?t=3099).

## Rules, checklists & numbers stated
- Analysis starts on the daily; 15m is the bellwether; set charts to New York time.
- Bearish daily: after 5 down days into discount, expect a bounce into the daily FVG; a touch of its edge is enough.
- Intraday framework: previous day's high (premium) and low (target); mark the last 3 days' highs/lows.
- Midnight NY opening price, extended to 11:00 a.m.
- FX NY killzone 7:00–10:00 a.m. NY; place orders then; cancel unfilled limit by 11:30 a.m.; no GTC.
- 15m entry: limit at the FVG (or +1 pip); stop above the high/swing high.
- HTF FVG is parent; LTF FVGs are subordinate; refine on 5/4/3/2/1m.
- Stacked FVG: limit in the lower FVG, stop accommodates the upper one.
- OB is valid only with an imbalance; consecutive same-direction candles = one OB; price need not reach the last up-close candle; OB = change in state of delivery (break below the candle's open).
- Intermediate-term high with an imbalance should not be exceeded → stop above it.
- No 1-pip / half-pip stops; risk is controlled by leverage.
- Example: EURUSD 7 April 2022 short, target 6 April low, ~40 pips, filled 2:45; range of opportunity ~60 pips.
- Don't enter new trades on a phone.

## Process, risk & psychology
- No method wins every time; losses largely come from the operator — take ownership. [0:04:02](https://youtu.be/eai0nHhAC8w?t=242)
- If someone had a never-lose method, they'd never teach it. Imperfection still doubled his account; a low win rate can still double an account — he disputes that a fixed risk-to-reward model is essential to be net profitable (proved with the live account). [0:12:47](https://youtu.be/eai0nHhAC8w?t=767)
- Many live-account executions were done to answer private students' questions (e.g. overcoming fear of pulling the trigger), so commissions and odd trades are not "mistakes." [0:09:34](https://youtu.be/eai0nHhAC8w?t=574)
- Funded-account programs: some students are funded; not for everyone; with a $100k funded account he would use this exact model. [0:13:35](https://youtu.be/eai0nHhAC8w?t=815), [0:15:10](https://youtu.be/eai0nHhAC8w?t=910)
- Backtesting/journaling: annotate charts (rectangles only for highlighting imbalances while learning — no indicators), screenshot into a study journal; at week's end (Sat/Sun) review intraday days against the daily and weekly charts: when the weekly high/low formed, biggest day of the week and its framework, pips moved, risk incurred. [0:25:34](https://youtu.be/eai0nHhAC8w?t=1534), [0:53:14](https://youtu.be/eai0nHhAC8w?t=3194), [0:54:01](https://youtu.be/eai0nHhAC8w?t=3241), [0:55:35](https://youtu.be/eai0nHhAC8w?t=3335)
- Leave empty chart space for your own observations to investigate further; develop your own note style. [0:55:35](https://youtu.be/eai0nHhAC8w?t=3335)
- All learning is hindsight (like surgeons studying medical journals); you can't get hurt studying moves that already happened. [0:54:01](https://youtu.be/eai0nHhAC8w?t=3241), [0:57:59](https://youtu.be/eai0nHhAC8w?t=3479)
- Setups are like bear footprints: never identical, but recognizably the same signature. [0:57:12](https://youtu.be/eai0nHhAC8w?t=3432)
- Your study journal becomes "the greatest technical analysis book you'll ever own"; stop buying books (except those in his library video). [0:58:47](https://youtu.be/eai0nHhAC8w?t=3527)
- Daily work on charts and passion is required; arguing "there's no algorithm" is an excuse. [0:50:04](https://youtu.be/eai0nHhAC8w?t=3004)

## Glossary candidates
`Bellwether chart` — ICT's 15-minute chart, the reference timeframe for managing/stalking trades and trusting intraday bias.
`Parent / subordinate imbalance` — HTF FVG governs where price stops; LTF FVGs within it are used for refined entries.
`Consecutive bearish order block` — a run of consecutive up-close candles treated as one OB, starting from the lowest candle's low.
`Change in the state of delivery` — the algorithm switching from delivering buy-side to sell-side (or vice versa), e.g. trading below the OB candle's open; ICT's definition of what an OB is.
`Low threshold entry` — entering at the first edge of the FVG/OB (most likely to fill, most pips of risk).
`Suspect rally` — a retracement after a bearish internal structure shift; expected to fail.
`Previous day high/low framework` — using yesterday's high (premium/Judas level) and low (target) for intraday trades.
`Event-driven market` — ICT's description of gold: needs news/geopolitics to trend; otherwise choppy stop hunts.
