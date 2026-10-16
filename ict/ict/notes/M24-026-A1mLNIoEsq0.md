# M24-026 — ICT 2024 Mentorship \ September 11, 2024
ID: A1mLNIoEsq0 · URL: https://www.youtube.com/watch?v=A1mLNIoEsq0 · Duration: 1:19:34
Content type: mixed (live NQ session after an 8:30 news release, with a long lecture on micro-structure, algorithms and stop/risk management)
Teaching density: high (the wick consequent-encroachment idea, the "price engine / HFT algorithm handshake", volume imbalance definition, stop placement logic and dynamic risk rules are all taught explicitly)

## Summary
Wednesday 2024-09-11 (CPI morning, post-8:30 high-impact news). NQ opens with a huge premium gap above a 18,846 settlement (opens in the 18,920s), immediately closes most of the gap, then ranges "wildly" around daily-chart inefficiencies and the opening range gap. ICT uses the session on 15-second/1-minute charts to teach that there is always liquidity at micro scale (minor buy side / sell side around candle bodies, wick midpoints and tiny gaps), that high-frequency algorithms and the "price engine" meet ("handshake") at predetermined levels, and that a simple repeatable model is: a short-term high is taken, price trades up to the consequent encroachment (midpoint) of an earlier wick, bodies build around it, and price delivers lower. He then walks through stop placement for that trade (use the order block / CISD opening price, allow the wick to "color outside the lines"), dynamic risk management (don't rush to break even; consider it at 25% of target; pyramid only before 50% of target), position sizing, a measured-move/fib extension, and admits his own weakness is exits.

## Concepts

### Opening range gap — half-gap and full-gap closure at the open (RTH)  (aliases: opening gap, previous settlement to opening price, gap closure)
- **Kind:** example only (applies earlier teaching) + RTH/ETH nuance
- **What ICT says:**
  - The opening range gap is previous settlement (RTH close) to the open price. Today's reference: previous settlement 18,846 and an open in the high 18,920s, "a large gap". He shows it on RTH data.
  - Price immediately traded half the gap (opening bell, ~9:30 ET) and then did an almost full gap closure; a deep retracement back inside the opening range gap followed. He marks the midpoint (CE) of the gap and the "full gap closure" level, and notes that after the closure price kept "wicking" and printing bodies at a key level near the previous-settlement area.
  - For regular-trading-hours versus electronic-trading-hours: he deliberately switches the 1-minute chart to ETH (electronic trading hours) data when he wants to use a particular wick (the wick consequent-encroachment idea below), because those candles' highs/lows differ from RTH-only candles. At the end (1:17:33) he again notes the pocket he's studying shows on ETH data.
  - After the full gap closure it is "retracement back into the open range" in the first 30 minutes, and then "new day opening gap" levels (Sept 11 and Sept 10) act as draw on liquidity targets.
- **How to identify:** Mark prior settlement (4:15 PM ET close) and the first 9:30 print; mark the midpoint.
- **How to use:** Treat the gap's midpoint and far edge as targets from a premium; after closure, watch whether bodies respect the gap's prior-settlement level (deliver below = decidedly weak).
- **Example in this video:** NQ Wed 2024-09-11: settlement 18,846, opens ~18,920s; half gap traded in the first minute after the opening bell (video 0:06:50), near-full gap closure by 0:07:38, then deep retracement and a long back-and-forth.
- **Timestamps:**
  - [0:02:11](https://youtu.be/A1mLNIoEsq0?t=131) — previous settlement 18,846, huge premium opening on 15m
  - [0:06:50](https://youtu.be/A1mLNIoEsq0?t=410) — opening bell: half the gap already traded
  - [0:07:38](https://youtu.be/A1mLNIoEsq0?t=458) — almost full gap closure, retracement inside the gap
  - [0:11:51](https://youtu.be/A1mLNIoEsq0?t=711) — new day opening gap as draw on liquidity; full gap closure then bodies at a key level
- **Nuance / caveats / changes:** Same opening range gap framework as 09-09 (M24-025) but the gap here closed within minutes. He does not state the 70% / 30-minute rule again in this video.

### Daily / weekly inefficiency (FVG) as reference levels; volume imbalance under it  (aliases: "inefficiency" = FVG, dash lines, high of the inefficiency, volume imbalance)
- **Kind:** example only
- **What ICT says:**
  - He annotates a daily chart inefficiency (a larger weekly one above and another inside it). The dash line (high of the inefficiency, and its low) is watched by 1-minute and 15-second bodies: price opens, trades down to it, and also reprices a small volume imbalance between a candle's close and the next open (around 18,924.75 and 18,921; caption says "924 3/4" and "21 even"). Both are "accomplished" at once.
  - Bodies staying at the top of the inefficiency's dash line (not just wicks) is the evidence price is "respecting" it; it then likely explores the other side (the low of the inefficiency), and because sell-side liquidity rests just below that low, price accomplishes two things: uses the PD array and runs the sell-side.
  - A Thursday September 5 daily candle low (dash line) is also tracked as a key level; sell-side was resting around the 18,886–18,888 area on the 15-second chart (caption unclear on exact numbers).
- **How to identify:** Draw the daily inefficiency on lower time frames with a shaded box; note the dash line for the high and the low. Look for bodies (not wicks) holding the top.
- **How to use:** If bodies respect the top, expect an exploration of the bottom and the sell-side under it.
- **Example in this video:** 0:03:02–0:03:51: daily chart annotated, price opens above, trades down to the candle low and volume imbalance; later, at 0:30:59, bodies closing at the top of the inefficiency inside the opening range gap on the 1m predicts the rotation to its low.
- **Timestamps:**
  - [0:03:02](https://youtu.be/A1mLNIoEsq0?t=182) — daily inefficiency, weekly one, volume imbalance annotated
  - [0:26:09](https://youtu.be/A1mLNIoEsq0?t=1569) — body lays right at the top dash line of the inefficiency; delivers lower
  - [0:31:46](https://youtu.be/A1mLNIoEsq0?t=1906) — lower side: sell-side below the low plus new day opening gap
- **Nuance / caveats / changes:** He prefers numbers and a few lines on the chart rather than clutter, but shows boxes for teaching.

### Balanced Price Range (BPR) and the "paint roller" test of efficiency  (aliases: balanced price range, porous price, bodies overlapping, "blue box")
- **Kind:** refinement / new coinage ("paint roller analogy")
- **What ICT says:**
  - Paint roller analogy: price is efficiently delivered where bodies have rolled "paint" over a range; ranges between two bodies with no body overlapping (only wicks) are thin paint, i.e. porous/inefficient. Example: between the previous day's settlement candle body and another body only one single body-pass down occurred, so there is "not a lot of paint" there.
  - A BPR formed (the blue box) in the 15m/1m; price trading below its top is "decidedly weak" and price needs to respect the top end of that area; if it goes below it, it was just a retracement into the opening range.
  - Minor buy side lies on the far side of the BPR and minor sell side on the other; "that's the cool liquidity that matters, not your book math".
  - Later (1:17:33) he asks Caleb to study the pocket on RTH data: it becomes a BPR once price leaves it, with bodies respecting it, and everything then goes lower.
- **How to identify:** An area where one move down and one move up overlap so that opposing FVGs share the same price zone (his blue box); porous = bodies not overlapping.
- **How to use:** Price below the BPR top = weak; if it respects the top, short with the BPR as premium array; watch the minor liquidity on each side.
- **Timestamps:**
  - [0:15:18](https://youtu.be/A1mLNIoEsq0?t=918) — BPR, respect of the top of the blue box
  - [0:19:40](https://youtu.be/A1mLNIoEsq0?t=1180) — paint roller analogy
  - [0:26:09](https://youtu.be/A1mLNIoEsq0?t=1569) — minor buy side / sell side around the BPR
- **Nuance / caveats / changes:** Uses BPR for micro scale on the 1m; the "paint roller" analogy is a new way to explain efficient vs inefficient delivery.

### Micro liquidity and "bread-and-butter" scalps (high-frequency scalps, "Scout" (caption unclear))  (aliases: minor buy side / sell side, small structure)
- **Kind:** rule / refinement
- **What ICT says:**
  - There is always liquidity, not only above old highs and below old lows: small micro structure (candle lows/highs, tiny BPRs, wick midpoints) also holds stops. If you have the higher-timeframe inefficiencies on the chart and watch price gravitate to short-term sell side / buy side, you don't need the full daily range to deliver; you get small repeating scalps.
  - On a 15-second or 30-second chart there are many examples inside one daily range; adding all the up/down fluctuations NQ could "move" 1,500 points in a day even if the daily range is smaller.
  - Quants/HFT algorithms don't need a daily directional bias; they frame specific reference points and need a confirming quality (bodies' opens/closes matching the reference level), then trade both directions all day.
  - Claim: finding 2–3 of these per day and making 1.5–3% a day is feasible even with a very small account and micro lots; he contrasts this with swinging for 10–15%.
  - Warning: don't instantly start trading every OTE/FVG/iFVG/order block on a 15-second chart without a model; complexity comes from not knowing what you're looking for.
  - The factor to look for: a discount array that stops price falling (but not sideways) to afford buy-side delivery, or a premium array that stops price rising (not sideways) to afford sell-side delivery.
- **How to identify:** Bodies at a higher-timeframe inefficiency high/low plus a nearby small liquidity pool (candle low, equal lows).
- **How to use:** Scalp from the micro premium/discount arrays; it works because it needs only a small run, not the full range.
- **Timestamps:**
  - [0:26:59](https://youtu.be/A1mLNIoEsq0?t=1619) — wick CE hit and delivery is "enough for a scalp"
  - [0:28:35](https://youtu.be/A1mLNIoEsq0?t=1715) — "always liquidity", micro structure
  - [0:32:36](https://youtu.be/A1mLNIoEsq0?t=1956) — 2–3 setups/day, 1.5–3% a day claim; micro lots
  - [0:34:13](https://youtu.be/A1mLNIoEsq0?t=2053) — the premise: premium array -> not higher, not sideways, so lower; discount array the reverse
- **Nuance / caveats / changes:** Extends "buy-side / sell-side liquidity" teaching down to micro scale; the % claim is his statement, not a backtested figure.

### Consequent Encroachment of a wick (wick CE) — opposing premium and discount CEs  (aliases: "consequent encroachment of the wick", wick midpoint)
- **Kind:** entry model / new refinement (he says "this could be your model")
- **What ICT says:**
  - Take a 1-minute candle with a prominent wick (ETH data); mark the 50% point (consequent encroachment) of that wick. Price returns to it after taking a short-term/old high above (buy stops) and reverses to the tick: that is "turtle soup old high" behavior plus a hit on the wick CE.
  - It does two things at once: it takes the short-term high (liquidity) and goes to a price the algorithms refer back to.
  - Once price reaches it, bodies start building around the CE ("hanging around", blocky bodies). Spending a lot of time there with bodies at the CE means it will go lower. He says there are "very few absolutes" but "we do technical science" and that this is as close as it gets: bodies of candles built around the wick CE -> price goes lower.
  - He calls the pairing "opposing premium and discount consequent encroachments on the wicks": the upper wick CE at a premium acts as the sell, and a lower wick CE (the discount wick CE) acts as the target (price delivered "right to the tick", e.g. a low of about 18,741.75 — caption unclear).
  - Qualifier: wait for a qualifying signature that bodies are respecting the high of the inefficiency/range (see above).
  - You do not need price to trade down to the low of the daily inefficiency; since this is a wick, "the damage is probably done" (0:43:00).
- **How to identify:**
  1. Pick a 1m candle with a long wick; draw its midpoint (the wick CE).
  2. Wait for a short-term high to be run above, taking buy stops.
  3. Price trades up into the wick CE and bodies begin building at it; the bodies' opens/closes line up with the high of the daily inefficiency.
- **How to use:** Short at/around the wick CE (often with a small add on 15s), target the lower wick CE and the sell-side liquidity beyond; expansion past it goes into the new day opening gap (Sept 10 NDOG in this case).
- **Example in this video:** NQ 1m (ETH data), ~10:00 to 10:08 ET (video 0:36:39–0:44:36): price runs the short-term old high (about 18,875 — caption unclear) up into the CE of an earlier wick, hits it exactly, then sells; the bodies sit at the CE too long; then price delivers lower toward the lower CE and beyond.
- **Timestamps:**
  - [0:24:22](https://youtu.be/A1mLNIoEsq0?t=1462) — "wick's consequent encroachment" on 1m ETH data; relative equal lows
  - [0:36:39](https://youtu.be/A1mLNIoEsq0?t=2199) — old high hits the wick CE (turtle soup old high)
  - [0:43:47](https://youtu.be/A1mLNIoEsq0?t=2627) — "this could be your model": opposing premium and discount CEs on the wicks
  - [0:44:36](https://youtu.be/A1mLNIoEsq0?t=2676) — two things at once: takes the short-term high and meets algo reference
- **Nuance / caveats / changes:** A new, quite specific model ICT presents live; there are no prices stated cleanly in the captions so replication requires re-watching.

### Algorithmic price delivery: the "price engine", HFT algorithms and the "handshake"  (aliases: price engine, high-frequency trading algorithm, handlers, map like a video game)
- **Kind:** new coinage / conceptual framing
- **What ICT says:**
  - HFT algorithms operate on a simple premise: above an old high and below an old low there is liquidity, regardless of whether it is one contract or 10,000. They harvest fluctuations in both directions all day long, adding and taking partials.
  - He compares price delivery to a video game map (Pac-Man, Call of Duty): the maze/map is predetermined; the "price engine" delivers price within it, calculated from prior range data (previous day, last three days, previous week, previous month). Each session window (morning, lunch, afternoon, London, Asia) is a "map". Neither retail nor large institutions control price; they only operate inside the map unless there is manual intervention.
  - "Handshake": when the algorithms trading on the price engine's logic and the price engine's delivery agree at a level, price hits it to the tick (e.g. the exact wick CE). Not random.
  - Days with news (he mentions NFP and similar) let the "handlers" stir price up so it looks disorganized; the setups are still there, but framing them takes understanding.
  - He says to ignore indicators and moving averages; none of them tells price what it will do. Also defends algorithms as adding liquidity.
- **Timestamps:**
  - [0:35:03](https://youtu.be/A1mLNIoEsq0?t=2103) — HFT algorithms add liquidity; retail blames them
  - [0:40:37](https://youtu.be/A1mLNIoEsq0?t=2437) — video-game map analogy
  - [0:41:25](https://youtu.be/A1mLNIoEsq0?t=2485) — price pre-determined by time windows and prior ranges
  - [0:44:36](https://youtu.be/A1mLNIoEsq0?t=2676) — "handshake" between algorithms and the price engine
- **Nuance / caveats / changes:** Conceptual; the practical content is the wick CE model and micro liquidity above. Strong claims (e.g. "nobody else teaches this") are marketing, not testable rules.

### Volume Imbalance and porous price ("patchwork")  (aliases: volume imbalance, porous price action, inefficient delivery; "patchwork" (caption reads "Patrick"))
- **Kind:** definition + refinement
- **What ICT says:**
  - A real volume imbalance: two broad candle bodies with an indecisive (small) candle in between; the bodies don't overlap each other across that area. He says the volume imbalance is defined by the range the body "encapsulates" (the range between those bodies), and you do not draw it on the indecisive candle's body (some viewers said he drew it wrong; he rejects that).
  - Porous price: a down-closed candle with a small wick, then the next candle, with no bodies touching/overlapping between them; "no rhyme or reason" from a retail perspective, but "in need of patchwork": price will come back up and redeliver into that area. When it does, HFT algorithms "fire in shorts" there, targeting the smooth lows (the lower wick CE).
  - He notes gaps/FVGs are not all the same; "they actually do certain things differently", to be learned later.
- **How to identify:** Adjacent candles whose bodies don't overlap, with wicks overlapping; a tiny pocket on 15s that sits inside a higher-level 1m wick area.
- **How to use:** Treat as a short entry area on the retrace; it is an additional PD array, along with the small inefficiency between two other candles.
- **Timestamps:**
  - [0:46:13](https://youtu.be/A1mLNIoEsq0?t=2773) — porous price action described
  - [0:47:02](https://youtu.be/A1mLNIoEsq0?t=2822) — "in need of patchwork"; algorithms short into it
  - [0:52:39](https://youtu.be/A1mLNIoEsq0?t=3159) — how a real volume imbalance is drawn
- **Nuance / caveats / changes:** Clarifies how he draws volume imbalances (bodies, not wicks), consistent with the 09-09 note about a "tiny separation" between a candle's low and another's high (a related but different case).

### Adding to a short (pyramiding) at a short-term premium array
- **Kind:** rule
- **What ICT says:** When bodies build around a short-term premium array/wick CE and you are already short, you can add a small amount ("toss on one or two contracts" if holding 15–20 contracts, "kick it up a notch"); then take something off lower. HFT algos do the same: short, add more, take something off below.
- **How to use:** Add small, on confirmation; he says you shouldn't fear adds if you understand what price is telling you.
- **Timestamps:** [0:47:52](https://youtu.be/A1mLNIoEsq0?t=2872), [0:54:23](https://youtu.be/A1mLNIoEsq0?t=3263), [0:57:33](https://youtu.be/A1mLNIoEsq0?t=3453)
- **Nuance / caveats / changes:** Pyramid only while not past the 50% threshold of the target (see risk section).

### Stop placement for the wick-CE short: "how far can it color outside the lines"  (aliases: stop above the order block, CISD opening price)
- **Kind:** rule / entry model detail
- **What ICT says:**
  - The 15-second inefficiency (one candle's low to another's high) is the entry zone, but the 1m wick above it can trade up to its consequent encroachment, so price can color "outside the lines" of the small gap. Entry at the low end of the 15s rectangle (the 1m candle's high), but the stop must account for how far the wick can go.
  - Also: an up-closed candle among down-closed candles is a bearish order block; the stop must at least cover that candle's opening price, which marks the change in state of delivery (CISD) of the run lower.
  - Stop = one tick above that, which is above the inefficiency. That looks like a big stop, but it is only large relative to a size like 30 contracts; fix size, not the stop.
  - Confirmation: when a candle trades a little outside the inefficiency without closing a body at its high end, it validates; then the middle of the inefficiency should hold price at bay ("shouldn't go higher; it's done the work of going into the upper half").
  - If you missed the run, you can still use the premium array / wick CE and the order block as your stop.
  - Balance size: small enough that being stopped doesn't hurt, big enough that you care. If you panic on entry you're too large; start with micros.
- **Timestamps:**
  - [0:59:58](https://youtu.be/A1mLNIoEsq0?t=3598) — 15s vs 1m inefficiency ranges; outside the lines
  - [1:07:07](https://youtu.be/A1mLNIoEsq0?t=4027) — entry at low end of the rectangle; stop considering CE of wick and the bearish order block
  - [1:07:56](https://youtu.be/A1mLNIoEsq0?t=4076) — stop one tick above the order block's open / inefficiency
  - [1:10:22](https://youtu.be/A1mLNIoEsq0?t=4222) — use the order block as stop; size balance
- **Nuance / caveats / changes:** Explains why his stops look "wide" in his trade-execution videos. "Mohawk" (caption unclear) is his label for the price action when a candle trades slightly outside the inefficiency.

### Dynamic risk management: stop reduces risk only after the trade develops  (aliases: stop to breakeven at 25%, pyramid threshold 50%)
- **Kind:** rule
- **What ICT says:**
  - Once in, the stop should reduce risk in a dynamic way, but not "jam to break even immediately"; you must accept the initial risk and give the trade time to develop.
  - After price has run 25% of your expected profit target, you may move the stop to breakeven (covering commissions). You'll still get stopped out sometimes and it may then run without you; that is the "paid premium education".
  - You can pyramid new entries if the trade is paying and price isn't past the 50% threshold of the target (example: a 100-handle target).
  - Never trade without a stop; posting a screenshot of an open profit with no stop is a sign of a clout chaser.
  - Resistance is normal even in low-resistance liquidity runs: price still pauses and creates add opportunities.
- **Timestamps:** [1:01:34](https://youtu.be/A1mLNIoEsq0?t=3694), [1:02:21](https://youtu.be/A1mLNIoEsq0?t=3741), [1:03:09](https://youtu.be/A1mLNIoEsq0?t=3789), [1:04:45](https://youtu.be/A1mLNIoEsq0?t=3885), [1:06:18](https://youtu.be/A1mLNIoEsq0?t=3978)
- **Nuance / caveats / changes:** The 25% breakeven and 50% pyramid thresholds are specific numbers worth quoting.

### Standard-deviation / measured-move projection from a dealing range to external range liquidity  (aliases: measure move, 1 standard deviation, fib extension)
- **Kind:** refinement
- **What ICT says:**
  - Take any inefficiency (any timeframe, not only daily) and project its range (high to low) lower: one "standard deviation" is where price is reasonable to reach.
  - To anticipate going beyond that, the simple Fibonacci change: a viewer said "1.25"; ICT said go to the 1.5 level and add a 2 (likely meaning a -2.5 extension; caption unclear). That is "a beautiful area to anticipate external range beyond a measured move"; being content there means "you're done".
  - In this session price went down to the wick low, which would have been a superstar move; but a limit at the wick CE would never have been filled, hence the need for flexibility.
- **Timestamps:** [1:12:47](https://youtu.be/A1mLNIoEsq0?t=4367), [1:13:34](https://youtu.be/A1mLNIoEsq0?t=4414), [1:15:11](https://youtu.be/A1mLNIoEsq0?t=4511)
- **Nuance / caveats / changes:** Exact extension numbers unclear in captions; verify against other videos on fib/standard deviations.

## Rules, checklists & numbers stated
- Previous settlement 18,846; open in the 18,920s (NQ, 2024-09-11).
- Use ETH data on the 1m chart for the wick CE idea; RTH data for the opening range gap.
- Short-term high taken + price trades to wick CE + bodies build at it (and respect the high of the inefficiency) => expect lower.
- Stop above the bearish order block's opening price / above the inefficiency; stop = one tick above.
- Move stop to breakeven only after ~25% of the expected profit target; pyramid only before the 50% point of the target.
- Never trade without a stop.
- Aim size so an initial loss is tolerable but meaningful; practice with micros.
- A target of "1.5–3% a day from 2–3 micro-structure setups" is his stated potential (his claim).
- Video length: he intends to keep streams to about an hour (his son/viewers can't keep up).
- He will stop the stream at 10:30 and recap earlier moments.

## Process, risk & psychology
- Don't try to trade everything on a 15-second chart; know your catalyst (what makes price not go higher/sideways but lower). [0:33:22](https://youtu.be/A1mLNIoEsq0?t=2002)
- Screenshot the moments he says "watch this" and write down your own words; then study old charts at any time frame; sub-one-minute charts only give more examples to study. [0:50:16](https://youtu.be/A1mLNIoEsq0?t=3016)
- Adversity is needed: you can't improve without resistance (weight-training analogy); trying to avoid all initial risk is the "neophyte" way. [1:05:32](https://youtu.be/A1mLNIoEsq0?t=3932)
- Short horizons and too-high expectations get in the way; the cleanest runs still pause. [1:06:18](https://youtu.be/A1mLNIoEsq0?t=3978)
- His own weakness: exits/targets, a perfectionism problem. Entries, stops, adding and partials are strengths; he is "never content" with exits. If your rules catch most of a move, missing the last 15–20 handles is not a disaster. [1:15:58](https://youtu.be/A1mLNIoEsq0?t=4558)
- Journaling harshly ("I should be better") creates scar tissue that resurfaces in later trades; don't do it in your journal. [1:16:46](https://youtu.be/A1mLNIoEsq0?t=4606)
- Money psychology on micros: $20 win feels huge, $10 loss feels like a catastrophe; this reveals your mindset; keep size low until it doesn't. [1:11:08](https://youtu.be/A1mLNIoEsq0?t=4268)
- Limit order at an exact CE may never fill: allow flexibility on entries and exits. [1:15:11](https://youtu.be/A1mLNIoEsq0?t=4511)

## Glossary candidates
`Inefficiency` — ICT's word for a fair value gap (high-to-low area between non-overlapping candles).
`Wick CE` — the 50% point (consequent encroachment) of a candle's wick, used as a reaction level.
`Price engine` — his term for the algorithm that delivers price along predetermined levels.
`Handshake` — the moment HFT algorithms and the price engine agree on a level so price hits it to the tick.
`Porous price` — price areas where bodies don't overlap (only wicks), so inefficient delivery needing "patchwork" (caption unclear).
`Paint roller analogy` — bodies "roll paint" across a range; thin paint means inefficient.
`Mohawk` — (caption unclear) label for a candle that trades a little outside an inefficiency without closing a body at its high end.
`Minor buy side / sell side` — small micro-structure liquidity around candle highs/lows and small BPRs.
`ETH vs RTH` — electronic trading hours data vs regular trading hours data; levels (highs/lows/wicks) differ between them.
