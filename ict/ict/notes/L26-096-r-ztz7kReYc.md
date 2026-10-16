# L26-096 — ICT 2026 Lecture: Trading ATH In The ICT PD Array Matrix \ April 20, 2026
ID: r-ztz7kReYc · URL: https://www.youtube.com/watch?v=r-ztz7kReYc · Duration: 1:02:15
Content type: mixed (lecture on a method + review of that morning's executed MNQ short + intermarket note)
Teaching density: high   (a genuinely new technique for finding reference levels at all-time highs, plus several refinements; maybe a third is tangents, politics, Q&A about drills and personal remarks)

## Summary
The question ICT answers is "how do I engage price at all-time highs, where there are no old highs above to use as levels?" His answer, shown on MNQ (Monday 20 April 2026, recorded in the afternoon, about 1:24 PM ET at the start): toggle the continuous-contract back-adjustment (the "B-ADJ" button) on the daily chart. With it off, the old highs are far away and useless; with it on, the contract history is shifted so that the October 30, 2025 daily high, which has the longest premium wick, sits in range, and the consequent encroachment (CE) of that wick becomes a premium PD array. He then stacks it with the RTH opening range gap (a discount gap at the Monday 9:30 open), the CE of the prior Friday's RTH opening range gap, and a TGIF 20% retracement of last week's range, and describes how he shorted the morning: the open ran up into the CE of a wick/gap, bodies refused to trade at or above it, price displaced lower, and the first-presented FVG (which then inverted) served as the entry catalyst, with targets at two sell-side levels. He also explains a new "defensive" PD array (spelling caption-unclear), how he scales, why he did not re-add partials, why NQ leads ES here, and why the "entry drills" he assigned are for overcoming fear, not for profit.

## Concepts

### Trading all-time highs with the continuous-contract back-adjustment toggle (B-ADJ)  (aliases ICT uses: "continuous contract", "toggling", "the secret")
- **Kind:** new coinage / rule
- **What ICT says:**
  - On the MNQ daily chart there is a "B-ADJ" button. With it off (continuous contract unadjusted) the relative equal highs and old highs are very far from price: classic S/R would say price should return to that high, which he rejects as a way of working.
  - The title shows no contract month (not "June 2026"), which tells you you are looking at the continuous contract.
  - Toggling the adjustment on "brings price back down into a range where we can use it": an old high (October 30, 2025) is now in close proximity to price from last week, so the PD array matrix has levels to work with again.
  - "The secret is that continuous contract toggling it on and off and where we're at in deference to previous all-time highs": focus on the market that, after toggling, has price action close to a previous all-time high.
  - He calls it a guarded concept (from a list of things he said he'd never teach back on BabyPips).
- **How to identify:** daily chart of the continuous contract; toggle the back-adjust setting and look for an old high near current price.
- **How to use:** after toggling, grade the old high (see Premium Wick CE) and carry the level down to the 1-minute chart (it stays drawn there; the heavy blue line is the candle high, the purple line its wick CE).
- **Example in this video:** MNQ daily, October 30, 2025 candle high = 26,864.50 (the "heavy blue line" on the 1-minute chart) with wick CE ≈ 26,745 (caption: "26,000 745 even", purple line). Monday 20 April price is trading around this area.
- **Timestamps:** [0:03:17](https://youtu.be/r-ztz7kReYc?t=197) — daily chart, B-ADJ not toggled, equal highs far away; [0:07:15](https://youtu.be/r-ztz7kReYc?t=435) — toggle on brings old highs within range; [1:00:35](https://youtu.be/r-ztz7kReYc?t=3635) — "the secret is that continuous contract toggling".
- **Nuance / caveats / changes:** the mechanics of why back-adjustment pulls old highs closer are not explained in the transcript beyond "it brings price back down into a range".

### Premium wick / discount wick and its Consequent Encroachment as a PD array  (aliases: "wick CE", "grading the wick")
- **Kind:** definition + rule
- **What ICT says:**
  - Pick the high whose wick is longer than the wicks of the previous candle and of the two subsequent candles; that is why October 30, 2025 was selected.
  - A "premium wick" is a wick at the high of a candle (above the body). A wick below the body is a "discount wick". But relative to price: if market price is below a wick it is a premium wick; if price is above, it is a discount wick. First thing to check: where is market price relative to that specific wick.
  - Grade the wick with a midpoint: "when we're having a midpoint like that, that's consequent encroachment". It matters more because it is part of Friday's daily range and today's, i.e. current price is inside the same area.
  - Treat the wick as a premium gap, "think of this as an inversion fair value gap": price below it coming up into it should not be able to leave a body at or above the CE of that wick; if a body lays at or above it, "I'm probably wrong".
  - Best entry for a short: from the CE down to the low of that wick ("anything inside of that is useful for an entry looking for shorts").
  - First order of business after the first test: price must show no willingness to get up into the CE of the wick, "not even for a wick", because the wick test has already been done; bodies staying low and "blunt-ended" confirm it.
  - He colours the wick/gap with his usual inversion FVG colour so it looks familiar.
- **How to identify:** longest wick vs neighbours; measure its 50%; mark it; watch bodies.
- **How to use:** short between wick CE and the wick low after the first test; stop outside the wick high / CE; targets sell-side below.
- **Example in this video:** MNQ 1-minute, Monday 20 April open: price runs up to the CE of a wick (around the 9:30–10:00 area) and shows no body at/above; ICT shorts the CE-to-close region of that candle ("anything in here is fair game").
- **Timestamps:** [0:08:02](https://youtu.be/r-ztz7kReYc?t=482) — longest wick selection; [0:08:50](https://youtu.be/r-ztz7kReYc?t=530) — premium vs discount wick; [0:22:30](https://youtu.be/r-ztz7kReYc?t=1350) — shorting at wick CE; [0:33:44](https://youtu.be/r-ztz7kReYc?t=2024) — wick as inversion FVG, bodies stay in lower half; [0:34:31](https://youtu.be/r-ztz7kReYc?t=2071) — best entry zone CE to low.
- **Nuance / caveats / changes:** the premium/discount wick terminology is explained a little confusingly in the captions; the rule of thumb is "relative to market price".

### RTH Opening Range Gap at highs: gap high = prior RTH settlement; octants and CE as read of intent  (aliases: "RTH ORG", "discount gap", "lowest octant")
- **Kind:** rule / refinement
- **What ICT says:**
  - RTH opening range gap = Friday's settlement (RTH close at 4:14 PM ET candle) versus Monday's 9:30 open. Monday opened lower: a discount gap near all-time highs. The gap high is Friday's settlement; he labels the gap box "RTH ORG" and its midpoint is consequent encroachment.
  - Expectations at ATH when bullish: price can trade above the gap high and then use the gap as a discount PD array ("something to support price"), possibly making a higher ATH; or price can fill to half (CE) and on to full closure.
  - Gap-fill tendency: price tends to go all the way to full closure, but if still bullish "you have to at least yield" to the possibility it trades above the high and uses the gap for support.
  - He was not interested in trading the first run into half gap, being unsure of full closure, and he would not have entered at full closure either: he would wait to see if it uses the high.
  - Reading the morning: a candle went to CE of the gap and closed below the gap's lowest octant (an eighth-division line, caption unclear). Because bodies would not even sit near the lowest octant, let alone above it, he read that as unlikely to run for full closure, and perhaps the extreme high of the gap, so the session high might be in.
  - Same gap logic as in the L26-086 video (RTH opening range gap and its overcome-then-retest behaviour).
- **How to identify:** prior day RTH settlement vs 9:30 open; box; midpoint; octant lines.
- **How to use:** at ATH a discount gap can be bought only if price proves it by exceeding the gap high and holding the gap as support; a sale idea starts when bodies refuse to approach the gap's upper range.
- **Example in this video:** MNQ, Mon 20 April 2026: Friday 4:14 PM settle vs 9:30 open lower; the first candle goes to CE and closes below the lowest octant; ICT interprets as the high of the morning.
- **Timestamps:** [0:16:07](https://youtu.be/r-ztz7kReYc?t=967) — RTH gap and discount gap; [0:19:19](https://youtu.be/r-ztz7kReYc?t=1159) — CE, full closure, or use as discount array; [0:20:55](https://youtu.be/r-ztz7kReYc?t=1255) — close below the lowest octant.
- **Nuance / caveats / changes:** "octant"/"quadrant" use is thin; same octant term appears in L26-074.

### TGIF: 20–30% retracement of the weekly range  (aliases: "Thank God It's Friday", "20% of the weekly range")
- **Kind:** rule
- **What ICT says:**
  - On Friday (or as early as Thursday at 1:00 PM ET) if the weekly candle is forming as an up-close/bullish week, look for a retracement from the weekly high of 20% to 30% of the full weekly range, in some instances up to 40%.
  - Method: Fibonacci anchored at the weekly low dragged to the highest high; set the 50 level to 20 (0.2) to show the 20%. Do this intraday on Thursday around 1:00 PM and keep referring back.
  - If it does not form on Friday and a new week starts, still look for it on Monday; if it has not formed by Tuesday, abandon it: price is probably continuing in its longer-term direction.
  - Last week closed up on the high without the TGIF pullback, so the Monday retracement was still a potential.
- **How to identify:** weekly range fib; 20% level.
- **How to use:** as a downside objective/bias anchor for the short (the "two key levels" together with Friday's RTH ORG CE).
- **Example in this video:** MNQ weekly: the 20% level = 26,489.25 (caption: "26,489 quarter"). It was anchored in green on the lower time frames.
- **Timestamps:** [0:11:16](https://youtu.be/r-ztz7kReYc?t=676) — last week closed on the high, no TGIF; [0:12:05](https://youtu.be/r-ztz7kReYc?t=725) — 20–30% (up to 40%) and the fib method; [0:28:56](https://youtu.be/r-ztz7kReYc?t=1736) — Monday allowed, abandon by Tuesday.
- **Nuance / caveats / changes:** the Tuesday cut-off is an "extra little rule" stated here.

### Prior Friday's RTH opening range gap CE as a target level (two-key-level framework)
- **Kind:** rule / example
- **What ICT says:** the gap from Thursday's 4:14 PM ET settle to Friday's 9:30 open: its consequent encroachment (50%) is a key level (he coloured it deep blue, bold and dashed). He does not need the high and low of that gap. The framework going into the day was two levels: (1) 50% of last Friday's RTH opening range gap, and (2) 20% of the weekly range (TGIF); "specifically anchored the majority to TGIF". The short idea had a best-case target there.
- **Example in this video:** later in the day price dropped to Friday's RTH ORG CE "perfectly" (taken at the day's lows), then retraced; after that he considered the liquidity pools "no longer of interest for the rest of today".
- **Timestamps:** [0:26:33](https://youtu.be/r-ztz7kReYc?t=1593) — Friday's gap CE; [0:27:21](https://youtu.be/r-ztz7kReYc?t=1641) — two key levels; [0:42:24](https://youtu.be/r-ztz7kReYc?t=2544) — price reaches Friday's gap CE.
- **Nuance / caveats / changes:** this is an afternoon (PM session) target, used only because of the climate (heavily manipulated markets).

### First-presented FVG → inversion, used as the catalyst to get short  (aliases ICT uses: "first presented fair value gap", "BISI → inversion", "premium fair value gap")
- **Kind:** entry model
- **What ICT says:**
  - He marks the FVG that formed right before the displacement down that takes a short-term low; "I want to see this be treated as first presented fair value gap" (the first one in the leg). He notes the 9:31 candle's gap is not the first-presented one; he promised to explain why (the explanation is not in this transcript).
  - If price lacks conviction at the wick, wait: once the buy-side imbalance sell-side inefficiency breaks down, it becomes a premium FVG / inversion FVG: "use it as a catalyst to get short".
  - Price keeps returning to the low end of the inversion FVG; each time it fails to reach CE (bodies below), he adds ("every time we were working toward the low end of that gap, which is first presented, I felt confident we weren't coming back up").
  - Keep such gaps on the chart: "they don't go stale; they're not supply and demand zones"; extend them into the next session (here Friday's → Monday's).
  - Tiny gaps ("common gap", small separations) are not helpful; the gap needs to be more significant.
  - Small time frame check on a 15-second chart: the first 15-second candle to close below the iFVG low, then a retrace that does not reach CE; "if this can't trade up to the low of that, that's heaviness"; look for minor sell-side first and a more significant sell-side further down.
- **How to identify:** BISI formed in the displacement leg; later broken and inverted; bodies staying in the lower half.
- **How to use:** add on retests into the low end that fail to reach CE; partials at minor sell-side below; do not re-add if close to the exits.
- **Example in this video:** MNQ, 20 April: price takes out a short-term low after displacing lower, the FVG before that displacement becomes the first-presented gap; shorts fill on retests into it; price then dives below the iFVG and the lows, hits minor sell-side, and finally Friday's RTH ORG CE.
- **Timestamps:** [0:31:20](https://youtu.be/r-ztz7kReYc?t=1880) — displacement lower and first-presented FVG; [0:36:06](https://youtu.be/r-ztz7kReYc?t=2166) — use the breakdown as the catalyst; [0:25:45](https://youtu.be/r-ztz7kReYc?t=1545) — keep gaps on charts, extend into next session; [0:53:26](https://youtu.be/r-ztz7kReYc?t=3206) — 15-second detail.
- **Nuance / caveats / changes:** he says traders who prefer "turtle soup or climax reversal" ideas near highs can use this and that it is "not your model" if you doubt it.

### Execution & management: stacked limits, partials, no pyramiding near exits, and the "BOLO" defensive PD array  (aliases: "bolo" (caption unclear), "defensive PD array")
- **Kind:** refinement / new coinage
- **What ICT says:**
  - He took the TP away after placing several buy limit orders: with limits stacked between two lows and no TP, the position would partly fill lower but not be closed there, leaving room to capture more of the run. Later he reversed his mind again about "probably wrong... probably going to Friday's CE" and removed the take-profit; hindsight showed the target would have paid more.
  - Partials: taken when price broke below the inversion FVG and below two lows (minor sell-side). He did not add them back: if price were another 20–30 handles lower and retraced to the iFVG he would have re-added, but not when it is close to the exit ("why did I take partials just to get back in?").
  - Stop idea: if price trades to the stop level at 26,806.75 or 26,806.25 (caption: "26,806 3/4 or quarter") he considers that no concern — it is above where he expects price to go.
  - A "new defensive PD array" he taught recently (spelling "Bolo" in captions): not an entry; the point price should not come back to. As long as the stop is outside it he is comfortable, could walk away from the chart; if price trades to it, you are wrong about direction; do not re-enter with the same trade idea ("it will trip me up").
  - He will not teach his specific stop-loss management because the market would learn where his stops sit; he teaches PD arrays.
  - This day he scaled in smaller than possible because of the environment: "I could have built a larger position today if it would have been a more favourable market environment."
- **How to use:** if a defined PD array that should not be revisited (the BOLO) is touched, accept that the idea is wrong, don't revenge-re-enter on the same idea.
- **Timestamps:** [0:37:42](https://youtu.be/r-ztz7kReYc?t=2262) — TP removed, limits stacked; [0:43:58](https://youtu.be/r-ztz7kReYc?t=2638) — defensive PD array not an entry; [0:44:47](https://youtu.be/r-ztz7kReYc?t=2687) — touched means wrong, don't re-enter; [0:48:42](https://youtu.be/r-ztz7kReYc?t=2922) — don't re-add partials near exits.
- **Nuance / caveats / changes:** the name "bolo" is unclear in the captions; check the earlier video in the series where it was introduced.

### Intermarket: NQ leads ES/YM (relative strength among correlated averages) and the ES sell-side pool  (aliases: "relative strength between correlated markets", "continuous contract trick doesn't work on ES")
- **Kind:** rule / refinement
- **What ICT says:**
  - The method needs a previous all-time high within reach after toggling. For MES the price is "significantly higher than the previous all-time high" and toggling still leaves it far away, so he cannot use the same method; therefore trade NQ/MNQ and trust NQ to lead the market lower.
  - NQ, ES and YM are positively correlated; generally all three should make higher highs together. When one is relatively strongest (here ES) and another near a level (NQ), use the one with price near the prior ATH; "the first shall later be last" (strongest first could lead down last).
  - On 1-minute he ran diagonal levels under the up-move (supposed retail diagonal support) aiming at a pool of liquidity; price tagged it then dropped. A significant MES sell-side pool about 20 handles below was marked as an intraweek objective (he doesn't require it today or tomorrow).
  - He wants NQ to lead a break down with ES following, then MYM (the Dow, which he says was unruly again).
- **Timestamps:** [0:56:35](https://youtu.be/r-ztz7kReYc?t=3395) — daily MES; [0:58:11](https://youtu.be/r-ztz7kReYc?t=3491) — why NQ over ES; [0:59:00](https://youtu.be/r-ztz7kReYc?t=3540) — relative strength between correlated markets; [1:00:35](https://youtu.be/r-ztz7kReYc?t=3635) — intraweek ES sell-side pool.
- **Nuance / caveats / changes:** extends his SMT/intermarket logic: choose the instrument by proximity to a usable all-time high.

### Entry drills and the "first-presented" practice on a 15-second chart
- **Kind:** process
- **What ICT says:** his assigned entry drills (the Wednesday and Thursday series) are meant to teach people to get into trades and overcome fear, not to produce profit; people clip them to claim "ICT can't trade". Judge his tape-reading narration, not the P&L. Give yourself permission to do it wrong in the beginning because you have no sample data yet. On a 15-second chart you see details otherwise missed, whether or not you trade that time frame.
- **Timestamps:** [0:51:53](https://youtu.be/r-ztz7kReYc?t=3113) — drills are for fear, not profit; [0:54:14](https://youtu.be/r-ztz7kReYc?t=3254) — permission to do it wrong.
- **Nuance / caveats / changes:** none.

## Rules, checklists & numbers stated
- At ATH: toggle B-ADJ on the continuous contract, find an old high in range; pick the candle whose wick is longer than its neighbours (previous candle and two subsequent).
- MNQ levels (caption numbers): Oct 30, 2025 high 26,864.50; its wick CE ≈ 26,745; TGIF 20% = 26,489.25; short stop mention 26,806.75/26,806.25.
- RTH settle used = 4:14 PM ET candle (Friday); the RTH ORG from there to Monday's 9:30 open.
- TGIF: Thursday 1:00 PM or Friday: look for 20–30% retracement (to 40%) of the weekly range if up-close; if not Friday, Monday; if not by Tuesday, abandon.
- Short entry zone: from CE of the wick down to the low of the wick; bodies must not be at/above CE.
- Gaps need to be significant; tiny gaps are of little use.
- Do not re-add partials close to the exit; re-add only if price retraces after 20–30 handles lower.
- Intraweek ES sell-side pool about 20 handles below.
- Drills: not meant to be profitable.

## Process, risk & psychology
- The climate is difficult: lots of manipulation, headlines and tweets; he second-guessed himself, was "really wrong" at times lately, and needed more confirmation; smaller positions are appropriate [0:40:03](https://youtu.be/r-ztz7kReYc?t=2403).
- Look for feedback from price constantly (a wick that doesn't get a body above CE is a test, "laboratory experiment") rather than forcing a position [0:31:20](https://youtu.be/r-ztz7kReYc?t=1880).
- Whatever the weekend sentiment, the opening sentiment is probably the opposite because someone is trading it [0:13:41](https://youtu.be/r-ztz7kReYc?t=821).
- Write down the tips from lectures that are not in the compendium in your journal [0:49:28](https://youtu.be/r-ztz7kReYc?t=2968).
- Don't quit because others discourage you: it takes time, but "there's nothing better" once it clicks [0:55:49](https://youtu.be/r-ztz7kReYc?t=3349).
- Judge a defined PD array by whether your stop sits outside it; if touched, you're wrong; don't re-enter [0:43:58](https://youtu.be/r-ztz7kReYc?t=2638).

## Glossary candidates
`B-ADJ (BACK-ADJUSTED CONTINUOUS CONTRACT)` — TradingView toggle that shifts older contract history; toggled on to bring old highs into range at ATH.
`PREMIUM WICK` — a wick above the candle body (or above current price); its CE is graded as a premium PD array.
`DISCOUNT WICK` — a wick below the body (or below current price).
`TGIF (WEEKLY)` — 20–30% (to 40%) retracement of the weekly range expected Thursday 1 PM / Friday; check Monday; drop by Tuesday.
`RTH OPENING RANGE GAP (RTH ORG)` — prior RTH settle (4:14/4:15 PM ET) versus 9:30 open.
`LOWEST OCTANT` — bottom eighth-division line of a gap; bodies below it signal no run to full closure (caption unclear).
`FIRST PRESENTED FVG` — the first FVG formed in a displacement leg; later inverted and used as a short catalyst.
`BOLO` — a recently taught "defensive PD array" (caption unclear): a price level price should not revisit; touching it means you are wrong; not an entry.
`HANDLES` — whole-point/price units of the index (as in "20 handles").
