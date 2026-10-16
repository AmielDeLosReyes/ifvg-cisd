# L26-047 — Chain Of Custody Of Price With RTH ORG
ID: V5crdCw0AsY · URL: https://www.youtube.com/watch?v=V5crdCw0AsY · Duration: 14:24
Content type: mixed (concept explanation + annotated 1-minute walk-through of one RTH session)
Teaching density: high (defines "chain of custody", defines the RTH opening range gap precisely, shows how to grade it and how to pick high-probability FVGs inside it)

## Summary
ICT answers viewer confusion about "chain of custody for price": how price travels from one key PD array to the next, and what makes a PD array "key" or high probability, without retail support/resistance or supply/demand. He says markets are algorithmic ("autonomous delivery") and that the answer is visual and mathematical: grade every inefficiency (daily/weekly suspension block, or the RTH opening range gap) into octant/quadrant levels, then only trust PD arrays whose middle candle sits on those graded levels when time and bias/draw on liquidity agree. He then walks through Monday's RTH ORG on the 1-minute chart (bearish, draw = full gap closure down), showing the first presented FVG, an inversion FVG, a "suspension" test on FVGs, a breakaway gap at the gap's CE, and a SIBI that stalls at its CE. Takeaway: the RTH ORG alone is enough to give a draw and entries; daily levels are added when price leaves the scope of the ORG, and the more things that agree on one side, the higher the probability.

## Concepts

### Chain of custody of price  (aliases ICT uses: chain of custody for price, key PD array to key PD array, autonomous delivery)
- **Kind:** new coinage / definition
- **What ICT says:**
  - The question: how does price move from one key PD array to the next, and what makes a PD array key or high probability?
  - The answer must not rely on "archaic mythology" such as retail support/resistance or supply and demand; it should be "so visual and mathematic." Markets are algorithmic: delivery is autonomous, no one is babysitting it; when it suits them they disrupt it briefly and it returns to autonomous delivery.
  - He says you may keep your own religion about buying/selling pressure, but this is what he means by chain of custody.
  - Operationally (as shown): price is handed from one graded level/PD array to the next - the range gap gives the draw, the graded octant/quadrant levels give the anchor points, and PD arrays that sit on those levels carry price from stop to stop.
- **How to identify:** a sequence of PD arrays each connected to a gradient level of the same range, all consistent with the draw on liquidity.
- **How to use:** build the day's path as a chain: a draw (e.g. full RTH gap closure), graded levels inside it, and the FVGs/iFVGs/breakaway gaps that touch those levels.
- **Example in this video:** Monday's RTH ORG (see below): first presented FVG -> iFVG at upper octant -> gap at the CE -> gap on lower quadrant -> imbalance on the gap low (Friday's last print), each a link in the chain.
- **Timestamps:** [0:00:00](https://youtu.be/V5crdCw0AsY?t=0) — the question; [0:00:47](https://youtu.be/V5crdCw0AsY?t=47) — "visual and mathematic", algorithmic autonomous delivery
- **Nuance / caveats / changes:** He does not give a formal checklist titled "chain of custody"; the rules below are my compilation of what he demonstrates (the term is first defined here by use). Part of a multi-video thread (he refers to previous videos and an X post from the day before).

### Suspension block (bullish BISI with volume imbalance at both ends), and checking FVGs for a volume imbalance  (aliases ICT uses: buy-side imbalance sell-side inefficiency "BISI", suspension block, volume imbalance)
- **Kind:** definition / refinement
- **What ICT says:**
  - The daily chart pattern from the previous video: a bullish BISI that is a "suspension block" because there is a volume imbalance at the top end and the low end ("very, very small, but it's there"). He had removed the small dark-purple volume-imbalance shading earlier so the whole block could be seen.
  - Correction: in the previous video he was fatigued and could not see why a level was not "green"; he suspected the fib was anchored wrong and now says to anchor the fib on the higher price of the candle's open (per the captions the candle's open is about 28,020 with body edges near 28,009.25 and 28,007.75; numbers caption-unclear), because that is the price it reaches down for.
  - On the 1-minute RTH chart he tests individual gaps the same way: compare candle open/close values; if the gap's candle edges do not overlap, there is a volume imbalance. One SIBI had none ("not a suspension block"); another had a small one (close 5xx04.5 vs open 5xx04.25, caption-unclear digits) and he calls that the high-probability gap.
- **How to identify:** (1) an FVG/BISI/SIBI; (2) check the open/close relationship of the adjacent candles for a volume imbalance at the top end and at the low end; if both ends have one it is a suspension block.
- **How to use:** a suspension block (or an FVG with volume imbalance) is the higher-probability version of the gap, to be combined with the graded levels below.
- **Example in this video:** daily NQ(?) chart: the blue shaded block is a bullish BISI with octants/quadrants; on the 1m chart a SIBI at ~28,5xx fails the test (no volume imbalance), a later one passes.
- **Timestamps:** [0:01:34](https://youtu.be/V5crdCw0AsY?t=94) — suspension block explained and fib correction; [0:10:26](https://youtu.be/V5crdCw0AsY?t=626) — this SIBI is not a suspension block; [0:11:14](https://youtu.be/V5crdCw0AsY?t=674) — this one has a volume imbalance
- **Nuance / caveats / changes:** Price digits in the captions are unreliable for this passage. Compare with L26-045 where the same term was introduced.

### Grading inefficiencies (octants, quadrants, CE as gradient levels)  (aliases ICT uses: graded out, gradient levels, octant and quadrant levels, grade it)
- **Kind:** rule / refinement
- **What ICT says:**
  - "All inefficiencies need to be graded." If you are trading inside a daily or weekly inefficiency it is "very, very important" to consider these levels.
  - Graded set: high, low, octants, quadrants, midpoint (CE).
  - When time and price agree at these levels - and bias plus draw on liquidity agree - then any FVG, order block, breaker, volume imbalance, wick, consequent encroachment, i.e. any ICT PD array forming around those levels carries high probability.
  - He took the gradient levels off the chart in the video to reduce confusion; the details of where "those key PD arrays overlapped with these levels" are in his earlier video.
- **How to identify:** draw a fib/grid over the full inefficiency (e.g. the daily suspension block or the RTH ORG) and mark octants (eighths) and quadrants (quarters) plus the 50%.
- **How to use:** (1) establish bias and draw on liquidity; (2) grade the relevant range; (3) look for PD arrays whose key candle touches graded levels; (4) take those that agree with time of day.
- **Example in this video:** the blue daily block ("octants, quadrants, high and low, BISI/SIBI in the form of a suspension block"), then the RTH ORG graded in the same way.
- **Timestamps:** [0:02:25](https://youtu.be/V5crdCw0AsY?t=145) — graded blue area; [0:03:13](https://youtu.be/V5crdCw0AsY?t=193) — "all inefficiencies need to be graded", PDA + time + bias
- **Nuance / caveats / changes:** No exact octant percentages given in this video (octant = eighth, quadrant = quarter; assumed from standard usage).

### RTH Opening Range Gap (RTH ORG)  (aliases ICT uses: regular trading hours opening range gap, opening range gap, Monday's RTH opening range gap)
- **Kind:** definition / rule
- **What ICT says:**
  - The RTH ORG for a given day is bounded by two prices: the 9:30 opening price of regular trading hours (the open of the 9:30 candle) and the last print of the prior RTH session (Friday's last print at 4:14 p.m. ET for Monday's gap; the candle's close is used - he dropped the fib on the higher value, the close at 28,291.25 vs open 28,290.75, per captions).
  - "Those are the only two reference points you really need" when looking at regular trading hours; the CME website offers other data, "it's not a big deal."
  - On Monday the high of the gap was the 9:30 opening price and the low was Friday's last print; the blue box's low is "all the way down there."
  - If price gaps up and you are bearish, full gap closure is the draw.
  - Some students argued about using 4:14; he insists the 9:30 open to the final printed RTH price is correct.
- **How to identify:** switch to the RTH (regular hours) chart; mark the 9:30 candle open and the prior session's last print (4:14 p.m. ET candle close); box between them.
- **How to use:** (1) the box edges and midpoint define a dealing range; (2) grade it into octants/quadrants; (3) trade PD arrays that form on those levels in the direction of the draw (full gap closure).
- **Example in this video:** Monday RTH: last print Friday 4:14 p.m. ET about 28,291; Monday 9:30 open higher (about 28,5xx; implied by 9:3x prices near 28,521-28,536). Bearish bias; draw = fill of the entire gap down to Friday's last print.
- **Timestamps:** [0:04:01](https://youtu.be/V5crdCw0AsY?t=241) — RTH ORG introduced for Monday; [0:04:52](https://youtu.be/V5crdCw0AsY?t=292) — only two reference points (9:30 open and last RTH print); [0:06:28](https://youtu.be/V5crdCw0AsY?t=388) — high = 9:30 open, low = Friday 4:14 last print
- **Nuance / caveats / changes:** He mentions that the RTH ORG is separate from the daily suspension block (previous video's levels): you can use it alone and don't need to confer with the daily BISI to find the draw. Instrument not named (NQ implied).

### Choosing high-probability FVGs inside a graded range: candle two touches the graded level  (aliases ICT uses: first presented fair value gap, candlestick number two, key PD arrays on octant and quadrant levels)
- **Kind:** rule / refinement
- **What ICT says:**
  - In a three-candle FVG, "candlestick number two" - the candle that creates the inefficiency - must be connected to an octant/gradient level of a range that is your analysis leading to a draw on liquidity. That is what makes the gap valid.
  - A middle candle touching two levels (here upper quadrant and lower octant) signals significant contraction in the trend direction ("fall out of bed") if bias is bearish.
  - The first presented FVG (here at the 9:3x candles): a BISI with a volume imbalance; using it as a short requires waiting for price to trade down through it and close below (inversion), then selling at that point ("there's your short if you're using the octant").
  - Illustrated with the question-bait "which gaps do you use? These never work when I try them" -> "because you don't know what you're doing": use graded levels only.
- **How to identify:** (1) range with a known draw; (2) graded levels; (3) three-candle gap where the middle candle overlaps at least one graded level, ideally two; (4) volume imbalance present.
- **How to use:** short in a bearish draw once price closes below the BISI (iFVG) or retraces to a SIBI at a graded level; expect strong delivery if two levels are touched.
- **Example in this video:** RTH ORG: BISI at 9:35 / first presented gap; then a SIBI whose middle candle touches the upper quadrant and a lower octant: he expected a quick fall but price retraced more than he thought and needed more participation lower.
- **Timestamps:** [0:07:17](https://youtu.be/V5crdCw0AsY?t=437) — first presented BISI at 9:35; [0:08:50](https://youtu.be/V5crdCw0AsY?t=530) — candle two must connect to a gradient level; [0:11:14](https://youtu.be/V5crdCw0AsY?t=674) — touches two levels -> significant contraction
- **Nuance / caveats / changes:** Candle times are caption-garbled (9:32 "CB", 9:35). The retracement above his expectation shows touching two levels is a probability tilt, not a guarantee.

### Inversion FVG at an octant (reverse the logic of the first utilization)  (aliases ICT uses: iFVG, inversion fair value gap)
- **Kind:** entry model / example
- **What ICT says:**
  - An FVG's first utilization is in the direction of the delivery that created it (a BISI is made by an up-close/buy-side delivery). When bearish, if price trades down below it (closing through), it can become an inversion FVG and be used with reversed logic (as bearish resistance).
  - When annotating he draws it as reversed to remind students that the logic of first use is inverted.
  - Example: the iFVG formed from the 9:3x BISI; price traded right up into the upper octant of the gap and then "falls out of bed".
- **How to use:** short on the retrace into the iFVG at an octant level in a bearish range-gap draw.
- **Example in this video:** RTH ORG: BISI at ~28,536.5-28,536.75 (caption values); price closes below it; retraces up to the upper octant; then drops sharply.
- **Timestamps:** [0:09:37](https://youtu.be/V5crdCw0AsY?t=577) — iFVG logic reversed; [0:10:26](https://youtu.be/V5crdCw0AsY?t=626) — trades to the upper octant and falls
- **Nuance / caveats / changes:** Consistent with other iFVG notes; the new bit is tying the iFVG to octant levels of the RTH ORG.

### Breakaway gap at the CE of the RTH ORG  (aliases ICT uses: breakaway gap, gap at the midpoint, unrealized dealing range)
- **Kind:** definition / example
- **What ICT says:**
  - A gap that forms exactly at the midpoint (CE) of your range-gap analysis, in the direction of the draw (down), signals a likely continuation toward the unrealized end of the dealing range.
  - It is a breakaway gap if price does not trade back into it or overlap and close it; "Would you want to see it traded back into ... No."
  - A second SIBI forms on the lower quadrant, price trades up into it, then breaks lower; another inefficiency lies right on the low of the range gap (Friday's settlement/last print), validating the SIBI.
- **How to identify:** gap formed at the 50% of the RTH ORG during a one-directional run; subsequent candles never trade back to its far boundary.
- **How to use:** if price stays away from the breakaway gap, hold toward the unrealized range end (full gap closure).
- **Example in this video:** RTH ORG Monday: gap touching the CE of the box; price never returns, trades to the lower-quadrant SIBI, then to the gap low where another gap forms; that SIBI goes to its CE and "stops dead in its tracks" with bodies staying below.
- **Timestamps:** [0:12:01](https://youtu.be/V5crdCw0AsY?t=721) — gap at CE = breakaway gap; [0:12:48](https://youtu.be/V5crdCw0AsY?t=768) — lower-quadrant gap, lower gap on Friday's last print; [0:13:35](https://youtu.be/V5crdCw0AsY?t=815) — SIBI to CE, bodies stay below
- **Nuance / caveats / changes:** "Settlement price for previous Friday at 4:14 pm ET" is how he words the low of the RTH ORG here.

### Layering the daily bias and daily inefficiency with the RTH ORG  (aliases ICT uses: "ring in" the daily levels, what takes precedence)
- **Kind:** rule
- **What ICT says:**
  - Answer to "what takes precedence": the RTH ORG framework alone is sufficient when the draw is full gap closure; you "don't need to confer with the daily BISI/suspension block."
  - When price starts doing things beyond the scope of the opening range gap, then bring in the daily bias levels and the daily balance-outside-of-efficiency (blue block) from earlier videos.
  - "The more things that agree on one side of the market, the less likely it is to go the other direction" - that is how he defines high probability.
- **Timestamps:** [0:04:01](https://youtu.be/V5crdCw0AsY?t=241) — precedence question; [0:13:35](https://youtu.be/V5crdCw0AsY?t=815) — ring in the daily levels; high probability = more agreement
- **Nuance / caveats / changes:** Re-affirms confluence, but with a clear hierarchy: RTH ORG first, daily second when price leaves the ORG's scope.

## Rules, checklists & numbers stated
- RTH ORG = 9:30 opening price (high of box for a gap up) to the prior session's last printed RTH price (4:14 p.m. ET candle close, Friday for Monday); only these two reference points are needed.
- Grade every inefficiency (daily/weekly/RTH ORG): high, low, octants, quadrants, CE.
- PD arrays count only when connected to a graded level, agree with time and with bias/DOL.
- FVG candle two must touch a gradient level; touching two levels = expect significant contraction.
- An FVG used for first utilization must be reversed (inverted) if price trades through it against bias.
- A gap at the CE of the range gap that is never retraced = breakaway gap.
- Fib should be anchored on the correct (higher) value of the candle open/close as he specifies; wrong anchoring makes levels not line up.
- Numbers (caption-only, possibly garbled): daily candle open ~28,020; RTH last print candle open 28,290.75, close 28,291.25; 9:3x BISI ~28,521.5 open / 28,522 close; a gap candle at 28,536.5/28,536.75; another at ~28,504.25/504.5.

## Process, risk & psychology
- Don't rely on retail concepts; be willing to accept visual, mathematical rules. He dismisses "chasing phantoms" and people arguing over the 4:14 print.
- He admits error when tired (fib anchored wrong) and publicly corrects it.
- "If the levels are good and the PD arrays are good, the concepts agree"; use agreement to define high probability, not opinion.

## Glossary candidates
`CHAIN OF CUSTODY (OF PRICE)` — how price is handed from one key PD array to the next along graded levels toward a draw.
`RTH ORG` — regular-trading-hours opening range gap: 9:30 open vs previous RTH last print (4:14 p.m. ET).
`GRADING` — marking octant/quadrant/CE levels across an inefficiency or range gap.
`OCTANT / QUADRANT` — eighth / quarter slices of the range used as gradient levels.
`SUSPENSION BLOCK` — a BISI/SIBI with a volume imbalance at both its top and low ends.
`BREAKAWAY GAP` — a gap at the CE of the range that price never trades back into, then continues in the draw's direction.
`FIRST PRESENTED FVG` — the first gap formed after the 9:30 open inside the RTH ORG.
