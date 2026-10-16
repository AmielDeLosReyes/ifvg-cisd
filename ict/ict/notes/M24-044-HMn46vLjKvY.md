# M24-044 — ICT 2024 Mentorship \ NQ Tape Reading \ October 15, 2024
ID: HMn46vLjKvY · URL: https://www.youtube.com/watch?v=HMn46vLjKvY · Duration: 1:34:17
Content type: mixed (live pre-market lecture + recap of prior-day executions)
Teaching density: high

## Summary
ICT teaches how to anticipate WHERE fair value gaps (and other PD arrays) should form in the pre-market, so you are not "surprised" by them. The method: measure the overnight range (12:01–4:59 ET) when the market has NOT been trending overnight, grade it with 0 / 0.25 / 0.5 / 0.75 / 1 levels, and with a higher-timeframe bias only take PD arrays that form on the correct side of the equilibrium (discount if bullish, premium if bearish) and close to a graded level, inside a macro window. He also gives a rule of thumb on opening-gap size (small gap = sit still, 50/50 morning), explains why macros exist (dealers feeding large orders through), shows old daily highs/lows as an "endless supply of setups" (not support/resistance), and reviews his Oct 14 live executions on a 30-second chart using volume imbalances. Heavy on "sit still" discipline.

## Concepts

### Overnight Range Grading (overnight range quadrants)  (aliases ICT uses: "grading" / "grading price", "overnight range", "the Fib on the overnight range", "defining the range")
- **Kind:** new coinage / refinement (a specific, repeatable way to pre-locate PD arrays; he links it to price-grading teaching in the 2016/2017 mentorship)
- **What ICT says:**
  - Range is defined by time: midnight New York to 5:00 a.m. New York (12:01 to 4:59). Take the highest high and lowest low BETWEEN those two times. Do NOT count the midnight candle or the 5:00 a.m. candle.
  - Chart time zone must be New York local time; "if your time is set to anything other than that you're doing it wrong."
  - Draw a Fib from the high to the low (or low to high) with levels 0, 0.25, 0.5, 0.75, 1. 0.5 = equilibrium; 0.25/0.75 = lower/upper quadrants. He draws these as dashed lines (to distinguish from the dotted quadrants of the daily SIBI).
  - Purpose: predicts the general location, "in close proximity", where PD arrays will form so you are not surprised by them.
  - ONLY use it when the overnight is part of a larger consolidation (price has been held inside the prior day's range, no new significant high/low). If the Asian session started running one-way and kept going (a "market protraction"/trend), do NOT use it; he has other tools for that but did not teach them here.
  - Applies to Forex as well as indices, not only stock index futures.
- **How to identify:** (1) Is overnight one-sided from Asia through London? If yes, skip. (2) If it is rotating inside yesterday's range, mark the 12:01–4:59 high/low, grade it.
- **How to use:**
  - First get a higher-timeframe bias. If bullish: look for PD arrays to form BELOW the graded levels (below equilibrium = discount; below the lower quadrant is even better); expect price to react at the lower levels and displace up away from them. Every bullish FVG below these gradient levels is "high probability."
  - If bearish: look for PD arrays forming just ABOVE the respective levels for shorts.
  - Upper half in a bullish day: do not expect pullbacks back to the low; the upper quadrant has "less degree of precision" because price is inclined to just rip through/clear the range high and keep going.
  - Use it before the 6:00 a.m. pre-market and act inside the macros (see Macros).
  - Extensions off the overnight range for targets/partials/reversals: first the -0.5 level, then -1 (one standard deviation).
  - If the bias flips (sentiment changes) everything inverts: bullish FVGs below become inversion FVGs, bullish order blocks become bearish order blocks, i.e. "market maker sell model" context.
  - If PD arrays you mark are not respecting price, that is manual intervention: sit on your hands.
- **Example in this video:** NQ 1m, Tue Oct 15, 2024. Bias bullish (election year, daily SIBI above). Overnight range 12:01–4:59 defined and graded. Price made the overnight low into ~4:30, turned up, then at ~5:08 swept down to the daily SIBI CE (see below) and reversed. Rally took out relative equal highs (minor BSL), into an inefficiency, then back down made an FVG below the overnight equilibrium (dash line) in the 5:50–6:10 macro; redelivered into it, ran up to overnight equilibrium, dropped to the lower quadrant, tapped the FVG, then ran above the minor BSL to the overnight upper quadrant (buy stops above the range high). Pullback from there made another FVG; a short-term low sat at equilibrium (SSL) with an FVG just below it = discount. At ~8:30 price spooled up; the upper-half action was less precise. Price then consolidated in the upper area below Monday Oct 14's daily high (BSL).
- **Timestamps:**
  - [0:08:58](https://youtu.be/HMn46vLjKvY?t=538) — defines the midnight-to-5:00 overnight range and excludes the boundary candles
  - [0:10:37](https://youtu.be/HMn46vLjKvY?t=637) — grading the range with Fib 0/.25/.5/.75/1
  - [0:12:12](https://youtu.be/HMn46vLjKvY?t=732) — do not use when market is trending overnight
  - [0:22:49](https://youtu.be/HMn46vLjKvY?t=1369) — why the FVG below equilibrium inside 5:50–6:10 qualifies
  - [0:36:07](https://youtu.be/HMn46vLjKvY?t=2167) — "an MO in the morning": grade overnight range, decide bull/bear, look for PDAs at the levels before 6:00
  - [1:00:12](https://youtu.be/HMn46vLjKvY?t=3612) — how to qualify FVGs: below the gradient levels while bullish = discount = high probability; scaling in
  - [1:04:11](https://youtu.be/HMn46vLjKvY?t=3851) — bias flip: everything inverts (bullish FVG -> iFVG, bullish OB -> bearish OB)
  - [1:05:00](https://youtu.be/HMn46vLjKvY?t=3900) — extensions -0.5 and -1 (one standard deviation)
- **Nuance / caveats / changes:** He frames this as "how I pick the right fair value gaps": the qualification is premium/discount relative to a time-defined range, not chart patterns. He says there are other refinements but this is "the easiest go-to." It is not a standalone signal: bias comes first, time (macro) second, PD array location third.

### Daily SIBI (Sell-side Imbalance Buy-side Inefficiency) as higher-timeframe draw, with quadrants and CE  (aliases: "civy"/"CBI" in captions = SIBI, "daily SIBI")
- **Kind:** example only (with a rule on gradient levels)
- **What ICT says:** The objective since the 2024 mentorship started was to draw up into the daily SIBI formed around July 17, 2024 (a single down-close candle on the daily). Its range gets the same 0 / 0.25 / 0.5 / 0.75 / 1 grading as the overnight range, drawn as dotted lines. Levels quoted: low 20410, lower quadrant 20489, CE/midpoint 20568 (low printed 20567.75), upper quadrant ~20646.75. (High not stated; by symmetry roughly 20726 -- derived, not quoted.) Because he is bullish, price should react to these levels and displace away upward; "we're not trying to short."
  - Consequent encroachment of a gap/inefficiency is the midpoint of the gap; for an order block it would be the mean threshold. He clarifies this daily level is CE because it is an inefficiency.
  - Perfect delivery to a CE level: price trades ONE TICK BEYOND it (e.g. buy at 20568 CE requires price to trade at least one tick lower, 20567.75), because a smart-money buyer needs to be filled; so don't expect the exact CE tick to be the low.
  - Being inside the upper quadrant of the daily SIBI while bullish means consolidation is likely (don't over-expect expansion); price "rebalances" an old gap only when it leaves the range higher/lower after trading in, merely touching it is "redelivery", not rebalance.
- **How to use:** Treat daily-level quadrants/CE as targets/reaction points while you hunt for lower-timeframe PD arrays; do not abandon the bullish daily narrative because of a pullback on the intraday chart.
- **Example in this video:** NQ 1m, Oct 15: the ~5:08 sweep traded exactly to the daily SIBI CE, 20567.75, one tick under 20568, then reversed (during the 4:50–5:10 macro/Asia close). Later price swept relative equal highs, hit the upper quadrant of the daily SIBI, and Monday's high BSL sat above.
- **Timestamps:**
  - [0:03:01](https://youtu.be/HMn46vLjKvY?t=181) — introduces the July 17 daily SIBI and its levels
  - [0:17:53](https://youtu.be/HMn46vLjKvY?t=1073) — low of 20567.75 vs. CE 20568 explained on daily
  - [0:19:32](https://youtu.be/HMn46vLjKvY?t=1172) — "one tick below" for perfect delivery
  - [0:32:23](https://youtu.be/HMn46vLjKvY?t=1943) — touch vs. rebalance
- **Nuance / caveats / changes:** The 4:50–5:10 window is called "Asia's close" and he describes a shift Asia -> London crossover -> NY pre-market; London "still active until around 11."

### Macros (algorithmic time windows) and why they exist  (aliases: "macro", "launch macro", "the 8:30 algo")
- **Kind:** rule / definition (with rationale)
- **What ICT says:**
  - A macro runs from 50 minutes past the hour to 10 minutes past the next hour (a 20-minute window every hour). During it price "spools" to run liquidity or reach into an inefficiency.
  - Pre-market (6:00–9:30 ET) macros: 5:50–6:10, 6:50–7:10, 7:50–8:10, 8:50–9:10 = four, plus the 8:30 algo = five opportunities, "the equivalent of the last hour of trading" and not a coincidence.
  - 8:30 is separate: the algorithm "comes online" and runs price around for the first hour before 9:30 regardless of news; a medium/high-impact news release at 8:30 just exaggerates it. It creates a sentiment-driven response that gets traders chasing and revved up before the open ("cheerleader" analogy). He says there has never been a need for an economic calendar.
  - Why: large institutions (funds, insurers) must push big blocks through; they cannot dump an order at once. Their dealer feeds the order through in staggered pieces, targeting an average price, during these high-traffic windows. This is not what moves price direction; price goes where it goes and the order flow just prints as time and sales. He says the sensitive windows are more prone to deliver price because of increased order flow.
  - He explicitly rejects numerology/odd time numbers (e.g. "8:11") as irrelevant.
  - "Time has to be the time for the market to move, otherwise it will stay stagnant or retrace against you."
- **How to use:** Combine macro timing with the graded overnight range and bias; the pre-market (6:00–9:30) alone offers enough opportunities; you never need to trade the morning session, launch macro, PM session or last hour if you can't or don't want to.
- **Example in this video:** The Oct 15 FVG below overnight equilibrium formed in the 5:50–6:10 macro (the second retest at 5:55) and delivered up to equilibrium of the overnight range. 4:50–5:10 macro ended at the daily SIBI CE reversal.
- **Timestamps:**
  - [0:22:49](https://youtu.be/HMn46vLjKvY?t=1369) — "5:50 to 6:10 macro"
  - [0:37:47](https://youtu.be/HMn46vLjKvY?t=2267) — counts the four pre-market macros plus 8:30
  - [0:52:06](https://youtu.be/HMn46vLjKvY?t=3126) — rule for any hour; why macros exist
  - [1:30:48](https://youtu.be/HMn46vLjKvY?t=5448) — 8:30 is the outlier; dealers and order flow explanation
- **Nuance / caveats / changes:** 6:00 a.m. is described as the changeover to the "pre-market" (6:00–9:30). Consistent with his statement elsewhere that the 8:30 algo is not news-dependent.

### Opening Gap Size Filter (NY opening gap / RTH opening range gap size)  (aliases: "anemic gap", "opening range gap")
- **Kind:** rule
- **What ICT says:** In the 2024 mentorship he taught that a small RTH opening gap implies a lackluster, low-impact morning session, no easy run from entry to target. Today's gap (previous close 4:14 p.m. settlement vs. open) was "anemic" (numbers around 20631.75 vs ~20662.75 stated, caption unclear which is which).
  - Minimum threshold he likes: about 45–50 handles (caption "4550"); preferred: 75 handles or more.
  - With a 75+ handle gap: "70% likelihood it goes back to half the gap" (the CE of the gap); he'd go in right at the opening bell, not even waiting for the first FVG.
  - With a tiny gap: no excitement/displacement at the open, so the morning delivery is 50/50. Sit still and wait for 10:00 (10:00–11:00 Silver Bullet) for an FVG that gives liquidity in line with bias; if it isn't clear, do nothing. Defer trading to lunch macro, PM session or last hour (e.g. come back at 1:30, watch the first 30 minutes into 2:00, trade PM; or sit down ~2:45 and trade the last hour).
- **Example in this video:** Oct 15 NQ: gap from the 4:14 p.m. close to the 9:30 open was too small to trade the opening; he waited for 10:00.
- **Timestamps:**
  - [0:39:24](https://youtu.be/HMn46vLjKvY?t=2364) — anemic opening gap
  - [0:40:15](https://youtu.be/HMn46vLjKvY?t=2415) — 45–50 handle minimum, 75 preferred, 70% to half-gap
  - [0:41:53](https://youtu.be/HMn46vLjKvY?t=2513) — wait until 10:00 Silver Bullet, otherwise do nothing
  - [0:42:41](https://youtu.be/HMn46vLjKvY?t=2561) — 50/50 morning, shift to lunch/PM/last hour
- **Nuance / caveats / changes:** The "handles" threshold and the 70% figure appear to be his personal heuristic, not a general law. The point he stresses is the permission to do nothing.

### Overnight Market Protraction (trending overnight) -> session planning  (aliases: "protracted state", "market protraction", "one-sided delivery")
- **Kind:** rule
- **What ICT says:** If Asia begins running one direction and keeps going through London, that is a protraction/trend; the overnight-range grading does not apply and its levels have no particular importance. Such an overnight move "usually puts you on the sidelines in the morning session": expect the NY session to be a reversal profile or consolidation, so unless you are very versed in reversal patterns, do not trade the morning; wait for the launch (lunch) reversal, the PM session, or the last hour.
- **Timestamps:**
  - [0:51:17](https://youtu.be/HMn46vLjKvY?t=3077) — what a protraction is and why not to grade it
  - [0:57:46](https://youtu.be/HMn46vLjKvY?t=3466) — example of a tiny 40-minute protraction today
  - [1:28:27](https://youtu.be/HMn46vLjKvY?t=5307) — overnight protraction implies reversal or consolidation morning

### PM Session Opening Range (1:30–2:00) liquidity  (aliases: "1:30 to 2 o'clock", "PM session highs/lows")
- **Kind:** rule / refinement
- **What ICT says:** Mark the PM session highs and lows and the 30-minute interval 1:30–2:00 p.m. ET for the last three days; the liquidity formed above/below that interval repeats because it is time-based and static. It sets up the initial direction/liquidity of the afternoon; price is likely to draw back into it. Like 8:30 and 9:30–10:00, "very specific elements of time" the algorithm always references.
- **Example in this video:** RTH view: yesterday's 1:30–2:00 interval formed relative equal lows; price rallied that afternoon; this morning price pierced underneath that low area and reacted.
- **Timestamps:** [0:45:59](https://youtu.be/HMn46vLjKvY?t=2759) — introduces the 1:30–2:00 reference; [0:46:46](https://youtu.be/HMn46vLjKvY?t=2806) — three-day lookback and why time-based liquidity is reliable.

### Old Highs/Lows of Previous Days and Week -- "endless supply of setups" (not support/resistance)  (aliases: "daily highs and lows", "old highs and lows")
- **Kind:** rule / example
- **What ICT says:**
  - Know each daily high and low of the last five days, at least last Friday's high/low, and the previous week's high and low. These are where order flow will come in; if bullish, wait for displacement.
  - He is not a support/resistance trader: price trading above an old high and returning to it does not mean it bounces from the line. He learned as a 20-year-old that textbook S/R doesn't reliably work that way.
  - Process (using last Thursday Oct 10 daily high): price rallies above the old high, dives back into the range, goes above again, drops again but does NOT take the relative equal lows (leaves the "bait"). That tells you it is unwilling to go lower; since you are already bullish ("in a buy program"), expect protraction higher. Do not buy just because it touched the level. Look for an inefficiency on the way down that acts as an inversion FVG; if it is good, price won't even touch it before leaving.
  - Assignment mindset: put the Oct 10 high on your own chart and watch how it gates above and returns; he leaves parts out deliberately for an interactive study.
- **Example in this video:** 30-second NQ chart, Mon Oct 14: price above the Thu Oct 10 daily high, back below, back above, below once more, then rallied; relative equal highs left behind (minor BSL). He went long on the inversion FVG formed on the drop, add-ons at the discount FVG at the 8:30 launch (see Volume Imbalances).
- **Timestamps:** [1:07:30](https://youtu.be/HMn46vLjKvY?t=4050) — yesterday's session; [1:09:59](https://youtu.be/HMn46vLjKvY?t=4199) — five days + last week's high/low = endless supply; [1:11:35](https://youtu.be/HMn46vLjKvY?t=4295) — watching how price gates above the old high; [1:13:08](https://youtu.be/HMn46vLjKvY?t=4388) — iFVG on the way down.

### Volume Imbalance (the PD array he calls most flexible)  (aliases: "volume imbalances", "little separations between bodies")
- **Kind:** definition / refinement
- **What ICT says:** A volume imbalance is the absence of overlap between one candle's body (open/close) and the next candle's body, with the wicks still touching, i.e. a tiny gap between bodies. It is "the most flexible" PD array in his repertoire: it measures whether price is willing to sustain a run; can be used as an entry, a partial, or for managing the stop. Its midpoint (CE) is also respected. Read the bodies, not the wicks: price "respecting" the imbalance between bodies is algorithmic delivery.
  - Timeframe: he used a 30-second chart because 15-second is "spotty" (too many volume imbalances) and 5-second gives too many to choose from; he wants a sub-1-minute chart with only a few imbalances. He stresses he is "a time-based price delivery trader," not a one-minute/five-minute chart trader.
  - An FVG below a volume imbalance on a bullish day is in discount and valid for entry.
- **How to use:** Enter as price trades down into the imbalance (when the candle is trading against your direction), not after the candle has started going your way; add more if price is inside the imbalance and runs away; use a limit order if you want a finer entry. Risk: he must keep a stop loss in every execution, being managed.
- **Example in this video:** See execution review below.
- **Timestamps:** [1:13:55](https://youtu.be/HMn46vLjKvY?t=4435) — body-to-body definition; [1:16:19](https://youtu.be/HMn46vLjKvY?t=4579) — "look at the bodies"; [1:21:03](https://youtu.be/HMn46vLjKvY?t=4863) — why 30-second; [1:21:52](https://youtu.be/HMn46vLjKvY?t=4912) — fewer imbalances = better timeframe.

### Executions review: Oct 14 (8:30 launch long, afternoon FVG/breaker, late-day short)  (example only)
- **Kind:** example only
- **What ICT says / what happened (NQ, 30-second chart, TradingView live, not Market Replay):**
  - 8:30: bullish, so he wants price to drop into a discount array. Price dropped into an FVG (could also have touched an inversion FVG; wouldn't have mattered). It had already left relative equal highs, so he knew it would come down to redeliver into the FVG. He posted "the launch time is now" at 8:30; entries in the lower half of the FVG / at the volume imbalance; first 6 contracts, then +4 as price touched the top of the FVG again ("pyramid"). Price rallied, tagged a volume imbalance, objective hit at 20538, a level he named the previous week as objective; he had a limit order there. He did not babysit the rest because he'd promised his wife to stay off the phone.
  - He enters while price is going against his direction and inside the lower half of the FVG; he does not chase bullish candles after they have started rising.
  - Afternoon: price traded into an FVG, he entered again (fills shown), ready for a drawdown into a breaker; added if it came back. Price traded up into a quadrant level, broke lower, created another FVG (entry); wait for willingness to take the buy stops at the quadrant. Timed entries at the CE of a wick/FVG.
  - Late: he went short as price aimed at the sell side below (abbreviated holiday session); limit order placed just above the low; didn't need the low to be taken ("I might be wrong"); expected a draw back to the middle of the range afterward.
  - A "first presented FVG" from last week (Wed or Thu) was marked with two thick lines.
- **Timestamps:** [1:14:43](https://youtu.be/HMn46vLjKvY?t=4483) — "launch time is now" logic; [1:18:40](https://youtu.be/HMn46vLjKvY?t=4720) — entries inside lower half of FVG; [1:22:40](https://youtu.be/HMn46vLjKvY?t=4960) — entry candle and confirmation by bodies; [1:25:56](https://youtu.be/HMn46vLjKvY?t=5156) — afternoon short to sell side with limit exit.
- **Nuance / caveats / changes:** The prior day (Oct 14) was an abbreviated session due to a holiday. Contract counts (6, then 4 more) are what he says he traded; not a recommendation.

### First Presented FVG  (aliases: "first presented fair value gap")
- **Kind:** example only (brief reference)
- **What ICT says:** He flags the first FVG presented after a given event from last week; he marks them as thick lines and recommends annotating your charts with such labels.
- **Timestamps:** [1:27:38](https://youtu.be/HMn46vLjKvY?t=5258)

## Rules, checklists & numbers stated
- Overnight range = 12:01–4:59 ET (exclude the 12:00 and 5:00 candles); grade at 0/.25/.5/.75/1; chart on New York time.
- Use overnight grading ONLY if overnight is consolidating; skip if Asia/London trended one way.
- Bullish: PD arrays in discount (below the graded levels) are the high-probability longs; bearish: PD arrays just above the levels for shorts.
- Extensions: -0.5 then -1 (one standard deviation) of the overnight range.
- Macros: :50 to :10 every hour; pre-market 5:50–6:10, 6:50–7:10, 7:50–8:10, 8:50–9:10, plus 8:30 algo = 5 opportunities; pre-market starts at 6:00 ET until 9:30.
- Pre-market alone is enough; never need to trade the open, morning session, launch macro, PM session or last hour.
- Opening gap: need ~45–50 handles minimum (prefers 75+); at 75+ handles he enters at the bell with ~70% expectation of going back to half the gap. Small gap = morning is 50/50, sit still, wait for 10:00–11:00 Silver Bullet or defer to lunch/PM/last hour.
- One-tick-beyond rule for CE: perfect delivery to a CE level means price trades one tick through it.
- Mark: last 5 daily highs/lows, last Friday, previous week's high/low, PM session (1:30–2:00) highs/lows for the last 3 days.
- Overnight protraction -> morning session is reversal or consolidation; don't trade it unless good at reversals.
- Chart timeframe preference for volume imbalances: 30-second (not 15s, not 5s).
- If the PD arrays aren't being respected, it's manual intervention; stay out.
- Don't expect price to hang around in FVGs: it should trade into them and leave.

## Process, risk & psychology
- Sit still: "nothing forces you to trade"; professionals look for the choicest setups; trading just because the market is open is gambling/impulsive (about [0:43:29](https://youtu.be/HMn46vLjKvY?t=2609)–[0:44:16](https://youtu.be/HMn46vLjKvY?t=2656)). He says he has taught sitting still more than any educator, because repeating conditions that say stay out aren't worth the risk.
- Always have a stop loss; "you can't stop them" from running stops, hence don't over-leverage ([0:28:24](https://youtu.be/HMn46vLjKvY?t=1704)). Manage the stop; he doesn't rush to break even.
- Beginners rush to pass a prop "combine" or get a payout; defer that and study first ([0:35:18](https://youtu.be/HMn46vLjKvY?t=2118)). He can't guarantee the skill set to make even one winner.
- Don't abandon the higher-timeframe bias because of an intraday pullback; many retail traders do ([0:56:58](https://youtu.be/HMn46vLjKvY?t=3418)).
- Review the lecture several times and test on old data; don't force new ideas into your existing model ([1:03:24](https://youtu.be/HMn46vLjKvY?t=3804)).
- Journaling: he wrote down the election-year bullish premise (the Street/"neophyte money" sees the stock market as the economy's gauge, so indices are pumped into the election); noted to write this in your journal ([0:08:10](https://youtu.be/HMn46vLjKvY?t=490)).
- Partials: tossing partials into levels ("ringer" horseshoe analogy) at overnight high, Monday high, daily SIBI levels.
- Exits via limit orders at pre-identified objectives, especially if you can't watch.
- Price is going to the point of "maximum damage" to whoever is making money.

## Glossary candidates
`GRADING` — marking a range with 0/.25/.5/.75/1 Fib levels to define quadrants and equilibrium.
`OVERNIGHT RANGE` — high/low between 12:01 and 4:59 ET, used when overnight is consolidative.
`PROTRACTION` — one-sided, trending delivery; opposite of consolidation.
`MACRO` — the :50 to :10 window each hour when price algorithmically spools for liquidity/inefficiency.
`8:30 ALGO` — algorithm "coming online" at 8:30 ET independent of news; first hour before the open.
`LAUNCH TIME` — his call-out that a macro/algo run is starting (here "launch time is now" at 8:30).
`VOLUME IMBALANCE` — gap between consecutive candle bodies (wicks touching); a flexible PD array.
`ANEMIC GAP` — a small opening gap indicating weak, low-excitement morning.
`HANDLES` — whole index points (e.g. 75 handles = 75 NQ points).
`SIBI (daily CBI in captions)` — sell-side imbalance buy-side inefficiency; a bearish-candle FVG.
`PYRAMID` — adding to a winning position at successive discount arrays.
