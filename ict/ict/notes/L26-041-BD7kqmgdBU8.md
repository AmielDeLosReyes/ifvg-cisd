# L26-041 — Part 2 High Precision Secrets To Intraday Price Action
ID: BD7kqmgdBU8 · URL: https://www.youtube.com/watch?v=BD7kqmgdBU8 · Duration: 51:48
Content type: market review (Saturday recap of the prior Friday on index futures, with a hypothetical short and a scale-out framework; opens mid-lecture, continuing Part 1)
Teaching density: high

Context: recorded on a Saturday after the Friday session being reviewed. This is the second half of the same lecture as L26-042 (Part 1), whose Friday is July 31, 2026 (ICT's 8:14 am ET tweet that day); so the reviewed session is most likely Friday July 31, 2026 (inferred, not spoken in this video). Instrument is never named; prices are around 28,300–28,600 and the Part 1 video says "Nasdaq", so presumably NQ. The first ~8 minutes are the tail of Part 1 (measuring a defined range to project the daily low) plus personal remarks.

## Summary
ICT shows how one graded range, the RTH opening range gap (previous day's 4:14 pm ET final print up to the 9:30 ET open), predicted both the PD arrays that formed during Friday and where price delivered, including the low of the day. He grades the gap in eighths (octants/quadrants), watches which levels the candle bodies respect, and shows how gaps in the premium half become "breakaway" gaps and old gaps become inversion FVGs. He then presents a beginner-friendly shortcut: short the retest of the 9:30 open with a tiny FVG entry, with a stop above the wick's CE, and take profit in tiers at half gap, full gap and then fib extensions of the gap (-0.2, -0.5, -1.0). The second theme is scaling: learn to hold runners by taking 75-80% off at the first target and stretching your comfort in small steps. Third theme: journal how highs and lows form in sessions, studying the daily chart one day a week.

## Concepts

### RTH opening range gap (ORG): definition, grading and the 70% / 10:00 statistic  (aliases: opening range gap, "regular trading hours opening range gap", half gap)
- **Kind:** definition / rule
- **What ICT says:**
  - The ORG runs from the 9:30 ET opening price to the previous session's regular-trading-hours final print/settlement at 4:14 pm ET. On this day: high = 9:30 open at 28,576.75, low = Thursday's 4:14 pm print at 28,324.75 (a gap up).
  - Add the levels in the data window to confirm both prices are exact (he toggles RTH and then back to electronic hours to read the prices).
  - Grade the gap: high, upper octant, upper quadrant, consequent encroachment (CE, the half gap), lower quadrant/octant, low. Above the CE is premium, below is discount.
  - Half gap (CE) "70% of the time" gets traded to by 10:00 am ET. Here it traded to the CE at 9:43.
  - The time dimension: 9:30 open is the "tethered" level, so horizontal levels are price relative to time. He also draws a first-hour dealing range (9:30–10:30 high and low) as a second time-based range.
- **How to identify:** gap between prior RTH close (4:14 final print) and 9:30 open; confirm with RTH/ETH toggle.
- **How to use:** the graded levels tell you where PD arrays should form and which levels they should react from; then check where the bodies (not wicks) are relative to those levels.
- **Example in this video:** NQ-like prices, Friday: price returns to the 9:30 open, trades below and up again, falls short of it, then opens lower and trades right into it; a gap in premium acts as a breakaway; it trades down through the CE at 9:43 and fills the gap to the low at 28,324.75, closes beyond it after hours.
- **Timestamps:** [0:09:39](https://youtu.be/BD7kqmgdBU8?t=579) setting the 9:30 high and the RTH low · [0:11:12](https://youtu.be/BD7kqmgdBU8?t=672) CE and the 70% by 10:00 statistic · [0:12:01](https://youtu.be/BD7kqmgdBU8?t=721) first-hour dealing range
- **Nuance / caveats:** he has used two "last price" references over the years: the high of the 4:00 candle (if it is higher than the close) from his 1990s S&P days, and the 4:14 final print; see the shortcut model below.

### Octants and quadrants: grading a range and reading body location
- **Kind:** rule / refinement
- **What ICT says:**
  - Take the highest of a set of levels to the lowest and measure it, then grade it. Upper octant, upper quadrant, CE, lower quadrant, lower octant are the grading levels.
  - What matters is where the bodies end up, not wicks: if price wicks through a level but the body comes back and closes inside, the range is respected.
  - Example logic: bodies trade down through the upper octant and the upper quadrant but fail to touch the next octant, then are rejected back up = bullish, especially if no body can return to the range that was used to project the daily low.
  - "Where are the bodies?" is his repeated question: bodies below the upper quadrant of the ORG = bearish context.
  - This measurement work is "very specific" to him: "an absolution, not a guesstimate". Don't be put off by the number of measurements: practise on old days.
- **How to use:** a candle touching two graded PD arrays at once (an old gap and the upper octant) is a significant reaction point.
- **Timestamps:** [0:03:59](https://youtu.be/BD7kqmgdBU8?t=239) measure highest to lowest · [0:05:43](https://youtu.be/BD7kqmgdBU8?t=343) body location, bullish or bearish · [0:15:32](https://youtu.be/BD7kqmgdBU8?t=932) upper octant touching two PD arrays
- **Nuance / caveats:** octant (1/8) vs quadrant (1/4) wording is his; the exact percentage is not spoken (assumed 12.5% and 25%).

### Breakaway gap in the premium half of the ORG
- **Kind:** new coinage / refinement
- **What ICT says:** if a gap forms after leaving a consolidation (one or two candles working inside a range between two PD arrays) and then price displaces lower, and that gap sits above the CE of the opening range gap (premium), you want it to act as a breakaway gap: price should not trade back up into it.
- **How to identify:** consolidation between two PD arrays, displacement away, gap formed above the ORG CE (for shorts).
- **How to use:** a candle laying on the CE with a bearish close and no return into the gap confirms the move; bodies stay below.
- **Example in this video:** gap at the upper quadrant of the ORG forms after a two-candle consolidation between two PD arrays, then displacement lower.
- **Timestamps:** [0:16:20](https://youtu.be/BD7kqmgdBU8?t=980) breakaway gap defined
- **Nuance / caveats:** "breakaway gap" is his label here; not a canonical earlier term in our list.

### First utilization of a gap: BISI/SIBI delivery and inversion
- **Kind:** rule / refinement
- **What ICT says:**
  - The first utilization of a BISI is buy-side delivery: if price is above it and trades down into it, it should send price higher. The first utilization of an old gap that is a SIBI is sell-side delivery: when bearish, it is a premium PD array to send price lower.
  - If, after the first utilization, price trades through the BISI and the market is now bearish, the BISI acts as an inversion fair value gap (iFVG): "see how the logic is very simple".
  - Price wicking into the gap, leaving no candle bodies in it, and coming back down = bearish.
  - Rule on the PM short: the gap that matters is the one prior to relative equal highs being taken out. After the equal highs are taken, price breaks lower and that gap becomes a bearish iFVG; internet teachers say "go long when it comes back into the fair value gap" but he is interested in it for a different reason (as a bearish iFVG).
  - To measure the iFVG, include the candle that carries the volume imbalance and anchor to the wick low.
- **How to identify:** a gap with a VI; price returns, wicks in, bodies do not close in it.
- **How to use:** short the iFVG after the equal highs are taken, with price closing below the midpoint.
- **Example in this video:** Friday morning: a BISI formed at about 9:01 (caption unclear), first-utilized as buy-side delivery, then price trades below it and it becomes an iFVG; objective tweeted at 28,400. In the PM: BISI prior to the relative equal highs being taken, price rallies out to the highs, bodies stop below the upper quadrant of the ORG, then big displacement lower closing below the midpoint.
- **Timestamps:** [0:17:07](https://youtu.be/BD7kqmgdBU8?t=1027) first utilization = buy-side delivery · [0:17:54](https://youtu.be/BD7kqmgdBU8?t=1074) becomes an iFVG · [0:22:46](https://youtu.be/BD7kqmgdBU8?t=1366) PM gap prior to the equal highs
- **Nuance / caveats:** he claims other "smart money" teachers do not know the "real" fair value gaps; the transferable point is the sequence of context (equal highs taken, then the prior gap inverts).

### Immediate rebalance
- **Kind:** definition (as taught here, caption unclear)
- **What ICT says:** after a candle closes, the very next candle can come right back to it and rebalance it immediately. If the following candle did not touch the first candle's low, it would have to be the very immediate next candle for this to count. Here both candles do it, and neither puts a body above the midpoint of the inversion FVG.
- **How to use:** supports staying short in the iFVG (bodies below the midpoint).
- **Timestamps:** [0:24:23](https://youtu.be/BD7kqmgdBU8?t=1463)
- **Nuance / caveats:** caption is rough; which candle low is touched is unclear.

### Bearish order block at the lower octant
- **Kind:** example only
- **What ICT says:** an up-close candle sitting directly on the lower octant (just under the CE of the ORG) is a bearish order block: price opens, trades up into it, and sells off. The drift then carries down to the ORG low, fills the gap, and breaks beyond it. A wick sell-side liquidity pool tweeted earlier was cleared first.
- **Timestamps:** [0:20:18](https://youtu.be/BD7kqmgdBU8?t=1218)
- **Nuance / caveats:** no stop rule stated for this one.

### Opening range gap extensions: -0.2, -0.5, -1.0 (standard deviation)
- **Kind:** rule / projection
- **What ICT says:**
  - Measure from the 9:30 open (gap high) down to the previous settlement (gap low), then use negative fib extensions below the gap low: -0.2 ("negative 20", a very low threshold just outside the gap), -0.5 (the "50" level), and -1.0 (one standard deviation). He says he taught this "a couple of years" ago.
  - The market came "real close" to the -1 projection, and the -0.5 level created a small FVG that price traded up into and then sold off from.
  - Measurements do not need to be perfect ("I ain't got time for that").
- **How to use:** these are the exit levels for the runners (see scale-out below). The -0.2 level is a place to take a partial because price can dip below the gap low and then rip back up.
- **Timestamps:** [0:21:07](https://youtu.be/BD7kqmgdBU8?t=1267) -50 and -1 projections · [0:46:37](https://youtu.be/BD7kqmgdBU8?t=2797) -0.2, -0.5 and -1 revisited
- **Nuance / caveats:** the earlier segment mentions a "negative 50" retraction level and "negative one", while the later one adds the -0.2; whether he is using the extension in percent or in range multiples is not spelled out.

### Fulcrum point (door and hinge)  (aliases: fulcrum, "climax reversal high")
- **Kind:** new coinage / projection
- **What ICT says:** when there is a climax reversal high (the zenith turning point), drag the fib from that high to the low where the rally started. That low is a fulcrum point, like a hinge: imagine the rally is a door; if the door swung round past the hinge, it would swing equally far below it. So the price target below equals the size of the rally, projected from the hinge. On this day that level was close to where the market had a turning point, which "gives a rich tapestry" to anticipate a significant run the other way, or at least a settled day. The low of the day formed around these levels.
- **How to use:** a measured-move/symmetry projection to confirm a reversal objective alongside ORG levels.
- **Example in this video:** Friday: rally off a low to a climax high; fib dragged from high to the hinge low; the projected equal-distance level sat close to where price eventually made the day's low.
- **Timestamps:** [0:26:47](https://youtu.be/BD7kqmgdBU8?t=1607) fulcrum explained
- **Nuance / caveats:** caption is ambiguous about which low is the hinge; the "equal swing" reading is my best interpretation.

### Gap-based shortcut model: short the 9:30 retest with a tiny gap entry  (aliases: "low-hanging fruit", easy objective)
- **Kind:** entry model
- **What ICT says:**
  - Do not try to predict the high or short the exact high. Use the gap: the 9:30 open versus where it settled the previous day at 4:14 pm ET (the last print).
  - If you are more comfortable, look at whether the close created a short-term high in close proximity (e.g. the high of the 4:00 candle). If the 4:00 candle's high is above the 4:14 close it gives a nearer gap-fill target; two reference points (4:00 candle high, 4:14 final print) plus the 9:30 open.
  - Low-hanging fruit: the easiest objective is the nearer, higher level; the next one is the "classic" half gap of the 4:14 gap. Both were hit within the same one-minute candle here.
  - Entry: price trades back into the range, retests the 9:30 opening price, and a small FVG forms there. The entry is inside that FVG. "Efficient entry": there is a small volume imbalance between bodies at the gap's high; the candle's wick high has no VI (its close was lower than the open); you start shorting at the wick as soon as the midpoint of that wick is breached ("above midpoint of this wick", upper quadrant), one contract.
  - The full sell-side-imbalance/buy-side-inefficiency range is measured from the VI high down to the wick high; entry starts at the upper quadrant.
  - Second order: wait to see if price gets between the two wicks; as soon as price gets above 9:30 open, try to nail another around the 9:30 level (may or may not fill).
  - Pyramiding: if it keeps going higher and enters the lower portion of the wick, at the wick low and just above, add more. Some prop firms do not allow adding to a losing position; if so, don't trade this way. ICT says he has never traded in a prop firm.
  - Stop: just above the CE of the wick (above the upper-quadrant entry region). On a high-volatility day that stop is wide; "that's why you should be trading micros."
  - Stop trail: once price leaves the area and takes out the low of that candle's body on a closing basis, tighten stop to the CE of the FVG, then to just above the high, where it stays until the target (half gap) is reached.
- **How to identify:** gap up (9:30 open above prior 4:14 print), market is bearish, price returns to the 9:30 open, small FVG with a wick high, a body-based VI.
- **How to use:** targets in order: half gap, then the 4:00-candle-high level / full gap, then extensions (see scale-out).
- **Example in this video:** Friday: after trading back into the range, retest of the 9:30 open forms a small gap; short at its upper part, price drops into the half gap and the full gap near the same minute.
- **Timestamps:** [0:34:44](https://youtu.be/BD7kqmgdBU8?t=2084) "shortcut version" · [0:37:03](https://youtu.be/BD7kqmgdBU8?t=2223) two reference points · [0:37:50](https://youtu.be/BD7kqmgdBU8?t=2270) the short at the 9:30 retest · [0:39:24](https://youtu.be/BD7kqmgdBU8?t=2364) entry at upper quadrant, stop above wick CE · [0:42:38](https://youtu.be/BD7kqmgdBU8?t=2558) stop trail
- **Nuance / caveats:** this was walked as hypothetical ("I'll toss in a single contract right there"); "may or may not have been filled". The phrase "SIBI/BISI" for the wick range is ICT's; captions garble which is which.

### Scale-out ladder for a gap short  (aliases: low-threshold trading, "give yourself the cookie")
- **Kind:** rule / trade management
- **What ICT says:**
  - New traders should trade a low threshold: easy targets, short time in the trade. Holding longer is built by practice, like the gym.
  - Always expect full gap closure, but take something out along the way: partial at the first target; at standard CE of the ORG you are done with 75-80% of the position off.
  - Graduating: wait for full gap closure and close the rest, or take a partial at full gap closure plus a little for spread (example he gives: don't try to catch 28,367 exactly, aim for about 28,370), and leave one runner to see if the gap overlaps and price continues lower.
  - Extension ladder: something off at half gap; the bulk off at full gap closure; then a partial at -0.2 (price could pierce the gap low and rip up); a partial at -0.5; and leave something to reach one standard deviation (-1.0). Beyond that "who cares".
  - Roll the stop to cover costs once the first partials are in; at full gap closure keep three micro contracts for the extensions.
  - These levels are action points: "do something with it", take it off or roll the stop right above and be willing to be stopped. If price then closes back between those levels the stop will likely be hit, and you risk the final partial you could have taken at the level; that cost is part of trading.
- **How to use:** one practical stretch rule: if you are a 100-point trader aiming at 250–500 point runs, take most off at 100 and leave a runner with no concern for what it does. Even if it comes back and you made nothing extra it is progress: you widened your comfort zone.
- **Timestamps:** [0:43:27](https://youtu.be/BD7kqmgdBU8?t=2607) low threshold · [0:45:03](https://youtu.be/BD7kqmgdBU8?t=2703) 75–80% off at CE · [0:47:25](https://youtu.be/BD7kqmgdBU8?t=2845) bulk at full gap closure · [0:48:11](https://youtu.be/BD7kqmgdBU8?t=2891) -0.2, -0.5, -1.0 · [0:49:48](https://youtu.be/BD7kqmgdBU8?t=2988) consequences of holding the last piece
- **Nuance / caveats:** "28,367" vs ORG low "28,324.75": the 28,367 figure is probably the nearer gap-fill level of the shortcut (caption unclear), so do not treat it as the ORG low.

### Journaling highs and lows; study the daily chart
- **Kind:** rule / process
- **What ICT says:** after 34 years (this coming November) he is still studying how the highs and lows form: session highs/lows (the AM session, the 7:00–9:00 am two-hour window), daily and weekly extremes. Log and journal the mechanism of how the market "books price", not just "ICT is good at picking FVGs". Repeating phenomena are not random but you will not see them until you look at wicks the way he teaches. Backtest and log. Pick one day a week, ~30 minutes, put on music, and study old moves on the daily chart. The daily chart is where the information comes from (not weekly, not 4-hour, nothing lower), because it caps the daily high and low.
- **Timestamps:** [0:00:00](https://youtu.be/BD7kqmgdBU8?t=0) · [0:06:31](https://youtu.be/BD7kqmgdBU8?t=391) the one-day-a-week routine · [0:07:18](https://youtu.be/BD7kqmgdBU8?t=438) daily chart caps the high and low
- **Nuance / caveats:** "daily ranges are defined by a daily chart" is stated flatly; it is context for the ORG and PD-array work above, which uses the lower timeframe only for entries.

## Rules, checklists & numbers stated
- ORG: 9:30 ET open to previous day's RTH final print at 4:14 pm ET; check prices with RTH vs ETH toggling.
- Half gap gets traded to by 10:00 ET about 70% of the time.
- Example numbers: ORG high 28,576.75; ORG low 28,324.75; tweeted objective 28,400; CE traded at 9:43.
- First-hour dealing range = 9:30–10:30 ET.
- Extensions of the gap: -0.2, -0.5, -1.0 (std dev).
- Scale: 75–80% off at CE (half gap); bulk at full gap; partials at -0.2 and -0.5; runner to -1.0; three micros left at full gap closure.
- Entry on a gap short: upper quadrant of the wick, above its midpoint; stop just above the wick CE; use micros on volatile days.
- Gap fill: add a little for spread (e.g., aim ~28,370 rather than 28,367).
- Bodies, not wicks, decide whether a graded level held.

## Process, risk & psychology
- Study one day a week for ~30 minutes, calmly, on the daily chart [0:06:31].
- Start the day with an idea of where the market is likely to go and what you need to see; know the risks, what could turn against you and why [0:33:09–0:33:56].
- Be systematic about stretching your comfort zone: take most off at a reliable level, leave a small runner and don't care what it does [0:44:15].
- You will never be right in this business (he cites Larry Williams); aim for precision, follow process, don't beat yourself up [0:50:36].
- Do not use a shortened or "cliff notes" version of his teaching: the "why" is what makes it work [0:29:11–0:30:00].
- Dismisses trendlines, head and shoulders, bull flags and moving average crossovers as "religion"; his work is "time and price, split up and graded" [0:32:21].
- Personal: he says he will reduce engagement over the next two years (empty nester in June 2028) but keep a weekly session [0:07:18–0:08:52]. Pyramiding in drawdown is not for every prop-firm rule set [0:41:02].

## Glossary candidates
`OPENING RANGE GAP (ORG)` — 9:30 open versus the previous RTH 4:14 pm final print.
`HALF GAP` — consequent encroachment of the ORG; reached by 10:00 about 70% of the time.
`OCTANT / QUADRANT` — 1/8 and 1/4 grading divisions of a range.
`BREAKAWAY GAP` — a premium-side gap after consolidation and displacement that price should not return into.
`FULCRUM POINT` — hinge low at the base of a rally; projecting the rally equally past it.
`LOW-HANGING FRUIT / LOW THRESHOLD` — nearest, easiest objective for newer traders.
`FIRST UTILIZATION` — the first time price reacts from a gap, which sets whether it delivers buy-side or sell-side.
`IMMEDIATE REBALANCE` — the next candle revisits the prior candle's area right away.
`TETHERED LEVEL` — a PD array anchored to the 9:30 open or CE.
