# M24-047 — ICT 2024 Mentorship \ Premarket Tape Reading NQ Futures \ October 21, 2024
ID: CQk-5lAirn0 · URL: https://www.youtube.com/watch?v=CQk-5lAirn0 · Duration: 41:55
Content type: lecture (pre-market walk-through on NQ, Monday 21 Oct 2024; he leaves before the 9:30 open)
Teaching density: high (a complete "no-news day" pre-market protocol: gap references, session highs/lows, opening range gap 50% bias, daily handle goals)

## Summary
With no medium/high-impact news on Monday or Tuesday and unable to stream the open, ICT teaches a repeatable daily framework for pre-market tape reading on NQ. He shows exactly how to mark the previous RTH settlement (4:14 ET last 1-minute candle), the new week opening gap, and the opening range gap high/low; how to frame the day with session highs and lows (Asian, London, NY AM, NY PM) as the draws on liquidity when there is no news; and how to combine those with the opening range gap rule that when the market opens lower than the prior settlement (a discount gap), the first-30-minute bias is bullish until 50% of the gap has been traded, which he states happens about 70% of the time. He stresses retail vs. professional perspective on opening gaps, daily handle goals for new traders (5 ES / 10 NQ), and the "one good setup, then stop" discipline.

## Concepts

### Opening Range Gap (previous RTH settlement to 9:30 open): how to mark it
- **Kind:** definition | how-to
- **What ICT says:**
  - Switch the chart from electronic trading hours (ETH) to regular trading hours (RTH) to find the previous day's settlement. On the 1-minute chart, the last RTH candle is the 4:14 ET candle (it settles at 4:14; there is no 4:15 candle because RTH is closed). On a 5-minute chart the 4:10 candle is displayed instead, which is why he tells you to drop to the 1-minute chart to read the exact close/open when marking any gap (new week or new day).
  - Previous day for Monday is always the previous Friday (unless Friday was a holiday; then use the last settlement).
  - Label convention: always label by the day you are trading, not the date of the data: on Monday it is "Monday's opening range gap high/low", not "Friday's." Until the 9:30 first print you do not know which side is high/low: if the market opens BELOW the prior settlement, the settlement is the opening range gap HIGH and the 9:30 open is the gap LOW (discount gap). If price travels back above it before 9:30 (here he notes it would have to traverse over 100 handles), relabel: the settlement becomes the low and the 9:30 first print the high.
  - Trading sessions context: ETH resumes Sunday 6:00 p.m. ET; Friday ETH stops at 5:00 p.m. ET.
- **How to identify:** Previous day RTH close (1m, 4:14 ET) to today's 9:30 first print.
- **How to use:** Mark the settlement now; pre-open label it provisionally; once the 9:30 open prints, set the FIB across the gap and take the 50% level (see below).
- **Example in this video:** NQ, Monday 21 Oct 2024: Friday's RTH settlement line (caption value ~20,494.25) annotated in black as "Monday's opening range gap high"; pre-market price ~20,39x (caption: "20,39 even") below it, so it is a prospective discount gap.
- **Timestamps:** [0:05:08](https://youtu.be/CQk-5lAirn0?t=308) — ETH vs RTH toggle; [0:05:55](https://youtu.be/CQk-5lAirn0?t=355) — use the 1-minute chart, 4:14 last candle; [0:10:57](https://youtu.be/CQk-5lAirn0?t=657) — labeling convention and relabel scenario.
- **Nuance / caveats:** Price digits in the captions are inconsistent; do not rely on them. Reinforces the Oct 7 and Oct 17 videos ("mid gap" = 50% of this gap).

### New Week Opening Gap (NWOG) — drawing it  (aliases: "new week opening gap", "Monday gap")
- **Kind:** definition | how-to
- **What ICT says:** NWOG is the gap between Friday's ETH settlement (the last electronic print Friday, 5:00 p.m. ET) and the first print Sunday at 6:00 p.m. ET. Since the market settled at one price and started at another, the lower value is the NWOG low and the higher is the NWOG high. Draw it by copying a horizontal line (ctrl-drag in TradingView), put it on the opening price, and flip low/high. This week it was very small: caption reads "484¼ to 496¼" with CE 490¼ (digits caption-derived; likely 20,484.25–20,496.25). Add a line segment at the consequent encroachment and use a contrasting color. The NWOG here encapsulated the Friday RTH settlement price.
- **How to use:** It is a reference/PD array; the CE of the gap is used. Also "Monday's opening range gap" (RTH) is a separate and generally more relevant reference for the opening session.
- **Timestamps:** [0:07:31](https://youtu.be/CQk-5lAirn0?t=451) — Sunday 6 p.m. open; [0:08:32](https://youtu.be/CQk-5lAirn0?t=512) — drawing NWOG; [0:09:20](https://youtu.be/CQk-5lAirn0?t=560) — size and CE.

### Session highs and lows as the default draw on liquidity (no-news protocol)  (aliases: "previous session highs and lows", "four opportunities per day")
- **Kind:** rule | entry-framing model
- **What ICT says:**
  - When there is no significant data (empty economic calendar, no volatility injection at 8:30), aim for session highs and lows: the high/low of London, Asia, the previous day's PM session and AM session (not just the daily high/low). Four sessions per day = four chances to frame a setup: Asian, London, NY AM, NY PM. He does NOT want people trading every session, but if your schedule allows, tape-reading them all makes you a well-rounded trader.
  - It also applies on news days; it is just his "usual reach."
  - Use these finite reference points ("not something that's always morphing") to anticipate where the next premium/discount array forms, including pre-market without being present for the bell.
  - London's range: use the "overnight dealing range" (taught last week). Midnight NY time is the true day open; the London killzone is 2:00–5:00 a.m. ET; the highest high and lowest low in that window are the London session high/low (the algorithm looks for liquidity and PD arrays in that window). If price is in a clean protraction in one direction, don't grade the range; if there is a consolidation, grade it.
  - Which buy side matters? He asks which is more likely the draw for the morning: the London session high (a cluster of relative equal "smooth" highs) or a single nearby candle high. His answer: the London session high is the more salient; the single-candle high is a minor objective on the way, and he wants to see price accelerate through it to reach the London session high ("before they take their stops out").
  - The NY AM window referenced: 9:30 to 11:00 (London close) going into noon.
  - Applies equally to Forex, bonds, currency futures: "time is universal" across asset classes except crypto (he has not investigated crypto) and he has no experience with the Nifty 50.
  - On any day, these references mean "you'll never run out of setups," including on high resistance liquidity run days; on low resistance days they are "absolute bangers" for easy low-hanging objectives.
- **How to identify:** Mark Asian, London, previous NY AM/PM highs/lows; annotate relative equal highs/lows; Thursday's/Wednesday's Asian lows can be older sell-side targets (he shows Thursday 17 Oct's Asian session sell-side low, at about 8:30 p.m. ET, and Wednesday's Asian session SSL with relative equal lows).
- **How to use:** Pick the nearest significant session level on the side of your bias, framed with the opening range gap and the 9:30–10:00 window. Annotate minor liquidity thinly (ghosted) and the major reference levels bold, so your eye goes to the impactful level; minor buy side "top left" is noted as a stop-trail level of shorts.
- **Example in this video:** NQ 5m, Mon 21 Oct pre-market: Thursday's opening range gap low and Thursday's Asian session sell-side lie below; the London session high (relative equal highs) is above; the current range between a minor high and minor low is "either it stays in the range or runs for the buy side or the sell side."
- **Timestamps:** [0:13:22](https://youtu.be/CQk-5lAirn0?t=802) — session highs/lows when no data; [0:15:00](https://youtu.be/CQk-5lAirn0?t=900) — four sessions per day; [0:19:49](https://youtu.be/CQk-5lAirn0?t=1189) — midnight true day, London killzone 2–5 a.m., London high/low; [0:21:32](https://youtu.be/CQk-5lAirn0?t=1292) — which buy side is the real draw.
- **Nuance / caveats:** Forms the bridge between the "overnight dealing range" (last week) and the opening range gap rule below.

### Opening Range Gap 50% rule — discount gap = bullish first 30 minutes  (aliases: "mid gap", "half gap", "gap closure", "70% likelihood")
- **Kind:** rule
- **What ICT says:**
  - If the market opens at 9:30 BELOW the previous RTH settlement (a discount gap), the bias for 9:30–10:00 ET is bullish, expecting at least 50% of the gap's range to be traded to. He states there is a "70% likelihood of half the gap being traded to during the first 30 minutes of trading, 9:30 to 10:00 Eastern."
  - The 50% level does not make the bias bearish afterward: "it just means that 70% of the time that's what's usually unfolding." If it does not reach 50% within 30 minutes, he still looks for it later; this is an immediate bias to study/tape-read, not a guarantee.
  - Implementation: take the first 9:30 print as the gap low, drop the Fib to the previous settlement (gap high), read the 50% level. (He says this is for a gap lower; the converse for a premium gap is implied but not restated here.)
  - Beyond 50%: price could go to a full gap closure or 3/4 gap closure; the 50% level is the minimum expectation.
  - "I'm never ever ever going in there on the basis of simply 'I'm going to go short because we open lower'" — worst thing to do, retail-minded.
  - Hypothetical he builds: assume the next tick opens at ~20,408 (caption "408", also rendered "20,480" — caption unclear; likely 20,40x given pre-market ~20,39x), annotated as Monday's opening range gap low; the Fib to the gap high (caption "494 and A4" ≈ 20,494.25) gives a 50% level near the top of the London relative equal highs, so the mid gap AND the London session high buy side agree as the draw.
- **How to identify:** (a) 9:30 open below prior RTH settlement; (b) measure the gap; (c) 50% level; (d) check what session highs lie in the path.
- **How to use:** Be long-biased until the 50% is traded; look for a partial near the first session high/relative equal highs, but aim for the draw above if the relative equal highs sit close to the 50% level, because the other half of the gap remains (3/4 or full closure). Use "any fair value gap, the first presented fair value gap" for the entry; if it wins, you're done; if it loses, don't do it again, sit still.
- **Example in this video (hypothetical, not a live trade):** NQ 21 Oct 2024: if price opens ~20,40x, 9:30–10:00 bias is long; first target the 50% level; pre-open he suggests a "modest little tiny Judas swing lower" taking out a short-term 1-minute low after 9:30, then a rally to attack the London session highs/mid gap. If instead price sells off first and takes out the London low, he'd look for a change in direction and then target the London session high.
- **Timestamps:** [0:26:21](https://youtu.be/CQk-5lAirn0?t=1581) — hypothetical open and gap labeling; [0:27:09](https://youtu.be/CQk-5lAirn0?t=1629) — 70% likelihood, 9:30–10:00; [0:29:32](https://youtu.be/CQk-5lAirn0?t=1772) — bullish until 50% traded; [0:31:09](https://youtu.be/CQk-5lAirn0?t=1869) — confluence of mid gap and London highs; [0:36:46](https://youtu.be/CQk-5lAirn0?t=2206) — not bearish afterwards, just usual 70% behavior; [0:39:08](https://youtu.be/CQk-5lAirn0?t=2348) — scenario if sell-off first.
- **Nuance / caveats / changes:** Same 70%/50% statement as the Oct 17 video (M24-046). Here he adds the explicit "never short just because we opened lower" prohibition and the idea that this alone "could be your entire model."

### Retail vs. professional perspective on the opening price  (aliases: "opening price = rough-cut sentiment")
- **Kind:** definition | psychology
- **What ICT says:** Retail looks at yesterday's close versus today's open ("we're way down"), sees weakness, chases shorts and then gets wiped out when the gap starts to fill — even a quarter or half of the gap is enough to stop out over-leveraged traders. The professional perspective is today's close relative to today's open (open-to-close), which is actual accumulation/distribution. The opening price is "rough-cut sentiment" meant to inspire or discourage less-informed, impulsive traders. He challenges indicator builders to plot cumulative close-to-open (retail view) vs open-to-close (professional view).
- **Timestamps:** [0:32:46](https://youtu.be/CQk-5lAirn0?t=1966), [0:33:33](https://youtu.be/CQk-5lAirn0?t=2013).

### Daily handle goals and the "one good setup then stop" discipline
- **Kind:** rule (risk/psychology)
- **What ICT says:** A new trader should not aim for 100 handles a day. First-rung objective: 5 handles per day on S&P (ES) and 10 on NASDAQ (NQ); later grow to 15–20 handles NQ and 10–15 ES. Once you have the day's objective, stop and tape-read the rest. Pressing the button on every impulse is not following a model; look for the one setup that has "a plethora of things" supporting the idea at the PD array you trade, and build accountability around trading only that setup. The way to find it is knowing the likely candidates for draws on liquidity (framed by session times) rather than only nearby swing highs/lows.
- **Timestamps:** [0:18:14](https://youtu.be/CQk-5lAirn0?t=1094), [0:19:00](https://youtu.be/CQk-5lAirn0?t=1140).

### Price delivery continuum (PD to PD, timeframe to timeframe)
- **Kind:** definition
- **What ICT says:** Technical traders should view price as continuously delivering from one PD array to the next and from one timeframe to the next; not just a generic "top-down." He means specific criteria that create a setup with the probability of moving from a discount to a premium array or the reverse: an obvious place to get short and an obvious place to take profits lower, or an obvious long and obvious sell level. He stripped his chart down to opening range gaps and Asian session liquidity pools and uses 5-min and 30-second charts.
- **Timestamps:** [0:03:31](https://youtu.be/CQk-5lAirn0?t=211), [0:04:20](https://youtu.be/CQk-5lAirn0?t=260).

### Choosing the framing: "do you know which level gets traded to"
- **Kind:** refinement
- **What ICT says:** Without a protocol you are guessing off one candlestick pattern, one order block, one FVG. When price sits between a minor high and a minor low, the only question is whether it takes the minor buy side or the minor sell side; staying in the range, running the buy side, or running the sell side are the only options. The gap aspect provides the tie-breaker: since price is below the prior settlement, you want to see it draw higher into 9:30.
- **Timestamps:** [0:35:11](https://youtu.be/CQk-5lAirn0?t=2111), [0:35:58](https://youtu.be/CQk-5lAirn0?t=2158).

## Rules, checklists & numbers stated
- RTH settlement = last RTH 1-minute candle at 4:14 ET (no 4:15 candle). ETH reopens Sunday 6:00 p.m. ET; Friday ETH closes 5:00 p.m. ET.
- Always use the 1-minute chart to take exact gap open/close prices (new week or new day).
- Label gaps by the trading day (Monday's opening range gap high/low), not the date of the data; relabel if price crosses to the other side before 9:30.
- No-news days: draw on liquidity = session highs/lows (Asia, London 2:00–5:00 ET, NY AM, NY PM; plus previous day's AM/PM session highs/lows).
- Midnight NY time = true day open; London killzone 2:00–5:00 a.m. ET.
- Discount opening range gap: bullish 9:30–10:00 ET until 50% of the gap is traded; "70% likelihood"; never short just because you open lower.
- New trader daily objective: 5 handles ES / 10 handles NQ; progress to 10–15 ES / 15–20 NQ; stop once achieved.
- Use the first presented FVG as the entry framework; win and you're done; lose and you do not trade again that day.
- NQ levels quoted in captions (20,494.25 gap high; 20,484.25–20,496.25 NWOG; hypothetical open "408"/"20,480"; pre-market ~20,39x) are unreliable; use for structure only.

## Process, risk & psychology
- [0:15:00](https://youtu.be/CQk-5lAirn0?t=900) — do not trade all four sessions "hog wild"; tape reading all of them builds skill.
- [0:18:14](https://youtu.be/CQk-5lAirn0?t=1094) — modest daily handle objectives; discipline over frequency.
- [0:32:46](https://youtu.be/CQk-5lAirn0?t=1966) — retail impulse: chasing shorts because price is lower than yesterday's close.
- [0:37:32](https://youtu.be/CQk-5lAirn0?t=2252) — his stated mentoring goal: for students to become independent and stop needing his videos or anyone's courses; this one rule (gap lower, look for half-gap higher) "could be your entire model."
- [0:40:42](https://youtu.be/CQk-5lAirn0?t=2442) — rules for Caleb: use any FVG (first presented FVG) as the model for the morning; "if it wins you be done with it, if you lose you don't do it again, you sit still."
- Personal: he normally sleeps about 4 hours in two sessions plus naps (slept 8 hours that night); not a trading lesson.

## Glossary candidates
`Opening range gap (ORG)` — gap between previous RTH settlement (4:14 ET last 1m candle) and the 9:30 first print.
`Discount gap` — open at 9:30 below the previous settlement; bullish until 50% of the gap is traded.
`New Week Opening Gap (NWOG)` — Friday ETH settlement (5 p.m. ET) to Sunday 6 p.m. ET first print.
`Session highs/lows` — Asian, London, NY AM, NY PM highs/lows used as default draws on liquidity.
`Overnight dealing range` — London-session range (midnight true day open; 2–5 a.m. ET killzone) used to frame pre-market targets.
`Price delivery continuum` — price moves PD array to PD array, timeframe to timeframe.
`Rough-cut sentiment` — ICT's description of the opening price: bait for impulsive traders.
