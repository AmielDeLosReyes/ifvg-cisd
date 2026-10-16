# M24-016 — ICT 2024 Mentorship \ Lecture #16 (August 24, 2024)
ID: kuURDD1ajdQ · URL: https://www.youtube.com/watch?v=kuURDD1ajdQ · Duration: 46:29
Content type: market review (annotated replay of Friday Aug 23, 2024 NQ session, framed as a chart-logging exercise for his son Caleb)
Teaching density: high (new coinage Event Horizon, first-presentation FVG rule, balanced price range / high resistance liquidity, ORG 70% midpoint, and a complete top-down short walkthrough)

## Summary
This is a post-mortem of Friday Aug 23, 2024 (NQ, Powell speaking at 10:00 ET) used to show how to annotate and log a session: mark the higher-timeframe PD arrays given in advance on Aug 13, the new day/week opening gaps, the opening range gap, and the first-presented fair value gap, then record how price used each. ICT walks the daily chart (volume imbalance, bearish order block mean threshold, daily SIBI), explains why price should not trade into the upper half of the volume imbalance, defines a balanced price range with high resistance liquidity above it, and then replays the 1-minute action: a 9:30-10:00 opening range raid of buy side, turtle soup, CISD, a short with pyramiding, an inversion FVG, and a drop of 200+ handles toward nested opening gaps, with an "Event Horizon" zone capping the last pump. Two new/clarified rules matter most: the first-presentation FVG cannot be formed by an imbalance candle earlier than 9:31 (it must exist in both ETH and RTH views), and the Event Horizon is the area between nested NDOG/NWOG levels, limited by a 60-day look-back. The final hour low formed at 3:45 at the bottom of the first-presentation FVG, which ICT cites as proof the day was time-and-price coded.

## Concepts

### Session logging / chart annotation routine  (aliases: "daily meditation", journaling charts)
- **Kind:** rule (process)
- **What ICT says:**
  - For each session, capture screenshots of your own charts (not his, though viewers who cannot watch live may use his to catch up) in PowerPoint or a notes tool, and type annotations in the open areas of the chart.
  - Record what levels mattered, how price traded to them, the highest high and lowest low, and how price worked with the levels given in advance. Do it every single day, not only on good technical days.
  - Expect it to feel monotonous and useless early; he says it is the routine that taught him to anticipate and repeat setups. Journals get more specific over time and drop the unimportant items.
  - What to log (his "number one, go-to" list): time of day; new day opening gaps and new week opening gaps; the opening range gap; the first-presentation fair value gap; plus other order blocks and FVGs you notice. Don't be afraid to annotate things that later prove unimportant.
  - His focus for Caleb: "what creates the high and low of the day."
- **Timestamps:** [0:01:57](https://youtu.be/kuURDD1ajdQ?t=117) daily routine, will feel monotonous · [0:04:21](https://youtu.be/kuURDD1ajdQ?t=261) typed annotations in blank areas · [0:44:42](https://youtu.be/kuURDD1ajdQ?t=2682) focus on what creates the high and low of the day · [0:45:29](https://youtu.be/kuURDD1ajdQ?t=2729) the baseline list to log every day
- **Nuance / caveats:** he says the replay is meaningless unless you also watch the Aug 23 live stream (about an hour and 15 minutes) because the nuance is in the narration.

### Volume imbalance (precise definition)  (aliases: VI)
- **Kind:** definition
- **What ICT says:** a volume imbalance is any pair of adjacent candles whose bodies do not touch or overlap; you measure the separation between the previous candle's body (open or close) and the next candle's body. There is no difference whether the candles are up- or down-closed. The wicks may travel and even open above the previous candle's low; that does not negate it. He adds that even a single tick of separation counts (captions on that last sentence are garbled).
- **How to use:** measure the gap, take its consequent encroachment, divide into halves/quadrants. When bearish, the upper (premium) half should not be traded back into if the algorithm "respects" the array.
- **Timestamps:** [0:09:11](https://youtu.be/kuURDD1ajdQ?t=551) definition
- **Nuance / caveats:** consistent with M24-013 (where he treats the wick bridge as a gap and measures between bodies).

### Daily volume imbalance + bearish order block mean threshold (higher-timeframe map)  (aliases: daily levels from Aug 13, "premium half should not trade")
- **Kind:** rule + example
- **What ICT says:**
  - Levels were given in advance on the Aug 13 live stream (end of stream) when price was lower and he expected higher prices. They were worked one level at a time: a small remaining portion of a daily SIBI; the daily SIBI high of Jul 23 (caption "CBI"); the big down-close candle of Jul 24 as a SIBI; the rejection block; the wick's consequent encroachment; the volume imbalance; and the bearish order block (the Jul 22 up-close candle) with its mean threshold.
  - Price hammered into the rejection block, fell just short of the wick CE (which he reads as underlying weakness), had a big smash down on Thursday (Aug 22), and on Friday worked into the mean threshold of the bearish order block (the halfway point), where he looked for rejection.
  - Rule: if you expect weakness and the HTF PD array is a volume imbalance that price already traded through, the best sign of algorithm respect is that price does not trade into its upper half. The upper (premium) half was shaded pink, and the NDOG of Aug 22 plus the daily SIBI high sat there; price had already gone through it three times and broke through.
  - The up-close candle at that area, once broken, becomes a bearish order block to use for intraday shorts.
  - Levels quoted: CE of the daily volume imbalance high = 19,943 (he thinks it respected the Friday high); mean threshold of the bearish order block = 19,881.75.
- **How to use:** short inside the range from the bearish OB with the expectation that the upper half of the volume imbalance stays unfilled.
- **Timestamps:** [0:05:59](https://youtu.be/kuURDD1ajdQ?t=359) bearish OB mean threshold, rejection block, wick, volume imbalance · [0:07:33](https://youtu.be/kuURDD1ajdQ?t=453) Jul 24 SIBI, smash Thursday, Powell at 10:00 Friday · [0:10:48](https://youtu.be/kuURDD1ajdQ?t=648) should not trade into the upper half · [0:12:24](https://youtu.be/kuURDD1ajdQ?t=744) MT 19,881.75
- **Nuance / caveats:** captions garble the candle dates (July 22/23/24); treat the above as approximate. He says he was reluctant to go long all day and instead shorted.

### Balanced Price Range (BPR) and high resistance liquidity  (aliases: balanced price range, "guarded by the algorithm", manual intervention)
- **Kind:** definition / refinement (his usage differs from the common overlapping-FVG BPR definition)
- **What ICT says:**
  - On the 1-minute chart he labels a segment a balanced price range: a small SIBI exists between one candle's low and another's high; price trades up into it (a small wick above is fine), breaks lower to a low, comes back up and overlaps the whole prior run, breaks lower again, retraces to the "propulsion block" again, then finally leaves the range below the low.
  - Why "balanced": price delivered both ways, back and forth (down, up, down, up), offering efficient delivery both higher and lower inside a clear trading range, and then leaves it. It is not enough to go up, down and leave.
  - Balanced price ranges are very difficult to get through. Buy-side stops above the high are "high resistance liquidity": it takes something very significant to reach them, in this case manual intervention (the algorithm is overridden), as around Fed, payroll, CPI and PPI.
  - Therefore if price does return to the BPR low and reaches into it, nothing is wrong with the logic; but if price reaches the high it signals manual intervention; he would not chase long and would "cut the interest in the day and be done."
  - Always trade after those news drivers; you do not know what they will do at the time of delivery.
  - Extend the BPR through the day. He kept the levels on a notepad (the chart gets busy); he recommends putting them on the chart while learning.
- **How to identify:** (1) a mapped range with a small SIBI inside; (2) price trades both directions inside it; (3) price leaves it with displacement; (4) the range's high holds as resistance.
- **Example in this video:** NQ 1m, Aug 23 before the open: the range sits above, price displaces below its low; ICT says he is not interested in longs "because of the factors on the daily chart." The shaded BPR high-low extended through 9:30.
- **Timestamps:** [0:13:11](https://youtu.be/kuURDD1ajdQ?t=791) BPR introduced · [0:14:47](https://youtu.be/kuURDD1ajdQ?t=887) back and forth then leaves · [0:16:28](https://youtu.be/kuURDD1ajdQ?t=988) high resistance liquidity and manual intervention · [0:18:03](https://youtu.be/kuURDD1ajdQ?t=1083) displacement leaves, return to BPR is guarded
- **Nuance / caveats:** this does not mention the usual "two opposing FVGs overlapping" definition. Record this as ICT's wording here.

### Propulsion block and order block "accelerator" (as used here)
- **Kind:** example only
- **What ICT says:** after a bearish order block changes the state of delivery (price crosses over it), an up-closed candle that sits there is another order block; he calls it a propulsion block, "like an accelerator" that pushes price lower. Price retests this propulsion block twice, sells off to a lower low, retraces into it again, then "gives up the ghost" and breaks lower out of the range.
- **Timestamps:** [0:13:59](https://youtu.be/kuURDD1ajdQ?t=839) propulsion block and accelerator
- **Nuance / caveats:** brief, descriptive only; no entry or stop rules given.

### First-Presentation Fair Value Gap (9:31-10:00 ET)  (aliases: first presented FVG, first presentation FVG, "your real first fair value gap")
- **Kind:** new coinage / rule
- **What ICT says:**
  - The first FVG that forms inside the 9:30-10:00 opening range. The candle that creates the imbalance (the middle candle) cannot be earlier than 9:31: toggle TradingView from electronic trading hours (ETH) to regular trading hours (RTH) and a 9:30-created gap disappears. A real first-presentation gap must exist in both ETH and RTH views.
  - Do not use gaps that start at 9:30, or 9:30 to 9:32 (caption wording), for this purpose; the earliest valid imbalance candle is 9:31.
  - Project it forward through the whole day and log how it behaves later. He calls this a school of thought he taught in Twitter Spaces in 2023, not in older books, and says it is the "number one go-to."
  - Carry it until 3:45 ET (end of the 3:15-3:45 macro), because the final-hour algorithm can reference it.
  - All times are New York time.
- **How to identify:** (1) set the chart to RTH; (2) find the first 3-candle FVG after the open whose middle candle is 9:31 or later; (3) check it also appears on ETH; (4) the gap must form between 9:31 and 10:00.
- **Example in this video:** NQ, Aug 23. The first presented FVG formed on the early rally; during the lunch hour price worked below it and sold off to fill the undelivered part of the opening range gap; later price rallied, rolled through and overlapped it; then in the last hour the day's low formed at 3:45 right at the bottom of that gap, and price rallied back to a previous NDOG, swiped above a short-term high, and closed.
- **Timestamps:** [0:19:40](https://youtu.be/kuURDD1ajdQ?t=1180) opening range 9:30-10:00 and the first FVG · [0:20:29](https://youtu.be/kuURDD1ajdQ?t=1229) RTH vs ETH toggle · [0:38:16](https://youtu.be/kuURDD1ajdQ?t=2296) imbalance candle cannot form before 9:31 · [0:42:14](https://youtu.be/kuURDD1ajdQ?t=2534) carry it through 3:45 · [0:43:05](https://youtu.be/kuURDD1ajdQ?t=2585) low of day at 3:45 at the bottom of the FVG
- **Nuance / caveats:** likely reason (my reading, not stated): a gap whose middle candle is 9:30 needs a pre-9:30 candle that RTH does not show. He says viewers' comments asking why he did not use an earlier gap are answered in the live stream.

### Opening Range and the "first one taken" rule  (aliases: opening range, 9:30 high, buy side vs sell side clean equals)
- **Kind:** rule
- **What ICT says:** the opening range is the 30 minutes from 9:30 to 10:00. If both the buy side (relative equal highs, including the 9:30 high) and the sell side (relative equal lows) are obvious and clean, wait for the first one to be taken; the side that is taken first is the fake run. On Aug 23 the buy side was taken, so "all of this is a fake run"; had price gone down first and then reversed, he would have treated that FVG as an inversion FVG.
- **Timestamps:** [0:21:19](https://youtu.be/kuURDD1ajdQ?t=1279) opening range, REH and REL, wait for the first one to be taken
- **Nuance / caveats:** ties to 2024 mentorship lesson on relative equal highs/lows; he refers to it as what he taught going into the 2024 mentorship.

### Aug 23 top-down short walkthrough (turtle soup, CISD, pyramid, accumulation test, iFVG)
- **Kind:** entry model (example); contains several rules
- **What ICT says:**
  - Accumulation test: after a run, a small BISI/SIBI forms; if price does not build multiple candles at its consequent encroachment ("I don't want to see it accumulate"), it will quickly run again, so expect another drive above the high. It drops, reverses out, and pumps higher; no accumulation at the CE means a higher high.
  - Sequence on Aug 23 (NQ 1m): opening buy-side raid creating relative equal highs; price hits the daily SIBI high from Jul 23, sweeps above the NDOG, runs to the mean threshold of the bearish order block (daily, Jul 22) and leaves relative equal highs; then drops without accumulating at the CE; a higher low forms; it rallies; a small gap forms, price rallies above and treats it as support; it runs just above the relative equal highs (turtle soup) and falls back through the bearish order block.
  - Failure signal: price could not reach the NDOG of Aug 22; he calls that weakness. When a candle swept below the opening price, that is the change in the state of delivery.
  - Short zone: any price between the opening price and the mean threshold of the Jul 22 bearish OB is a short; he calls the turtle soup the validation of the bearish order block, and says you can add/pyramid anywhere between those levels.
  - Price then breaks down through the Aug 20 NDOG, rallies one candle to touch the daily SIBI high (Jul 23) again, and breaks lower; he wanted it to go below the gap, come back into the lower half, and not trade the upper half; it drops to the next NDOG and rejects sharply, leaving the upper half unfilled.
  - Targets: relative equal lows (minor sell side), then the opening-range sell side that had not been tagged; the 10:00 move while Powell spoke was Judas swing / manual intervention knocking out shorts.
  - Inversion FVG: price makes relative equal highs again, does not accumulate in the BISI, runs a new high; the gap formed after the run is passed and becomes an inversion FVG. With buy side swept, the market should be in a sell model: consolidation, rally (manipulation), break lower (smart money reversal) = a low-risk sell. Price breaks below the old NDOG and below the FVG, acts as an iFVG, upper half stays open.
  - Final target: the NDOG of Aug 23 sitting inside the old NWOG of Aug 18 (see Event Horizon).
- **How to use:** he did it live ("I'm expecting this before it even happens"); shorts were between the open and the order-block MT; add as it works; hold for the nested-gap draw.
- **Example in this video:** NQ, Fri Aug 23, 2024, 9:30 to the afternoon; moved over 200 handles. Prices not stated in captions beyond the daily levels above.
- **Timestamps:** [0:22:08](https://youtu.be/kuURDD1ajdQ?t=1328) no accumulation at CE, drop-reverse-pump · [0:23:47](https://youtu.be/kuURDD1ajdQ?t=1427) turtle soup, back below bearish OB · [0:24:34](https://youtu.be/kuURDD1ajdQ?t=1474) CISD, short zone, add/pyramid · [0:27:46](https://youtu.be/kuURDD1ajdQ?t=1666) iFVG and sell model, low-risk sell
- **Nuance / caveats:** the captions in this stretch are rough; the order of touches (daily SIBI, NDOGs) is approximate. A passing line says every FVG should not be viewed as a future iFVG; first presentation is its own idea.

### Event Horizon  (aliases: "my event horizon", gray pool / dark pool / "black hole")
- **Kind:** new coinage (PD array)
- **What ICT says:**
  - When there is a new day or new week opening gap above and another below where price is expected to draw, measure from one to the other with a fib and put quadrants on it: upper quadrant, midpoint, lower quadrant. That zone is the Event Horizon. The algorithm will reprice into it "like a black hole" and draw price in.
  - It can be NDOG with NDOG, NDOG with NWOG, or NWOG with NWOG; there is no preference or added strength for one pairing; what matters is that they are close to one another.
  - Look-back: use the IPDA data range, no older than 60 days (about three months) for the gaps; if a NWOG is older than 60 days he is not generally interested, especially for the Event Horizon (the algorithm can use any of them; this is his maximum).
  - He calls this kind of PD array a gray pool (dark pool) and says retail cannot see it in the candles; he has others similar, will not teach all of them, and may share one more in the mentorship (no promises). He shares the Event Horizon with private students and mentioned it in passing in a Twitter Space.
  - Nesting: the Aug 23 NDOG sat inside the high-low of the NWOG of Aug 18; "when they nest like that" it is a huge black hole, easy to anticipate where it will be drawn.
- **How to identify:** two nearby NDOG/NWOG ranges (each within 60 days), measure between them, mark quadrants, and watch whether the candle bodies stay inside the zone and fail to go above the upper quadrant.
- **How to use:** treat the zone as a place price is drawn into; judge it by the candle bodies, which should stay inside it (not above the upper quadrant) when it caps a move. He also asks how far price can go below sell-side liquidity even without the extra opening gaps.
- **Example in this video:** NQ, Aug 23: the pink Event Horizon zone (between two NDOGs, per the captions) sat where price built relative equal highs and pumped one more time; the bodies stayed inside it and never went above the upper quadrant. Price then dropped through sell-side liquidity toward the NDOG of Aug 23 nested inside the NWOG of Aug 18 (his stated destination from the start of the stream). Which exact gaps bound the zone is not fully clear in captions.
- **Timestamps:** [0:28:36](https://youtu.be/kuURDD1ajdQ?t=1716) NDOG nested in NWOG · [0:29:24](https://youtu.be/kuURDD1ajdQ?t=1764) "my event horizon" · [0:30:14](https://youtu.be/kuURDD1ajdQ?t=1814) fib and quadrants, bodies stay inside · [0:31:50](https://youtu.be/kuURDD1ajdQ?t=1910) combinations allowed, 60-day cap
- **Nuance / caveats:** earlier in M24-013 he used a 5-week lookback for Caleb's NWOGs and said older ones don't go stale; here the stated hard maximum is 60 days. He says it is "outside the spectrum of a candlestick."

### Opening Range Gap (RTH) and its 70% midpoint tendency  (aliases: ORG, premium/discount opening range gap)
- **Kind:** rule
- **What ICT says:**
  - ORG = previous regular-trading-hours close (4:15 PM ET close; he cites the 4:14 candle) to the 9:30 open the next trading day. If it opens above, that is a premium ORG; below is a discount ORG.
  - He says he taught this year that 70% of the time the midpoint (CE) of that gap gets traded to. Measure it on the first tick, then add quadrants; the midpoint matters most.
  - Track the undelivered portion (from previous settlement to the day's low, if it hasn't fully closed) and project it forward.
- **Example in this video:** NQ, Aug 23: he wanted to see price drop to the ORG CE but would only act at premium levels. Price dropped into the undelivered portion during the lunch hour; the candle bodies respected the Aug 18 NWOG, and the gap delivered.
- **Timestamps:** [0:34:12](https://youtu.be/kuURDD1ajdQ?t=2052) ORG definition and 70% CE · [0:34:59](https://youtu.be/kuURDD1ajdQ?t=2099) undelivered portion · [0:35:46](https://youtu.be/kuURDD1ajdQ?t=2146) lunch-hour delivery respects the NWOG
- **Nuance / caveats:** "70%" is his statement; adds a number to M24-013's "very high probability" language.

### Manual intervention around Fed speakers  (aliases: Judas swing at 10:00, news drivers)
- **Kind:** rule
- **What ICT says:** manual intervention (human override of the algorithm) is most likely when a Fed chair speaks; the initial reaction is usually fake ("a mess, you're going to get hurt chasing it"). Powell spoke at 10:00 ET on Aug 23, so the early rally in the opening range was a Judas move that knocked out shorts; he did not go long and said if it keeps going up it goes without him. Trade after the news.
- **Timestamps:** [0:26:11](https://youtu.be/kuURDD1ajdQ?t=1571) 10:00 Powell, manual intervention · [0:41:26](https://youtu.be/kuURDD1ajdQ?t=2486) initial reaction is fake
- **Nuance / caveats:** relates to the high-resistance-liquidity idea above.

### Last-hour macro (3:15-3:45) and the first FVG
- **Kind:** refinement
- **What ICT says:** between 3:00 and 4:00 there is a 3:15-3:45 macro; carry the first-presentation FVG to 3:45. On Aug 23 the day's low formed at 3:45 at the bottom of that FVG; he says that is "coded logic based on time and price," not buying and selling pressure.
- **Timestamps:** [0:42:14](https://youtu.be/kuURDD1ajdQ?t=2534) 3:15-3:45 macro · [0:43:05](https://youtu.be/kuURDD1ajdQ?t=2585) low at 3:45 at the bottom of the first FVG
- **Nuance / caveats:** the lunch macro is described similarly to M24-012: price comes back against resting buy orders trailed by shorts ([0:40:39](https://youtu.be/kuURDD1ajdQ?t=2439)).

## Rules, checklists & numbers stated
- Opening range = 9:30-10:00 ET; first-presentation FVG imbalance candle >= 9:31 and must exist in both ETH and RTH.
- Carry the first-presentation FVG to 3:45 ET; last-hour macro 3:15-3:45.
- ORG: RTH close 4:15 PM ET (4:14 candle) to 9:30; midpoint reached about 70% of the time (his statement); opens above = premium, below = discount.
- Event Horizon: any NDOG/NWOG pair close together; quadrants; look-back no older than 60 days.
- Volume imbalance: bodies of adjacent candles do not overlap; up/down irrelevant; wicks do not negate.
- When bearish and price has traded through a volume imbalance, the upper half should not be revisited.
- If buy-side and sell-side clean equals both exist in the opening range, wait for the first one to be taken.
- Levels: CE of daily volume imbalance 19,943; bearish OB MT 19,881.75.
- Short zone: between the 9:30 opening price and the bearish OB MT; add (pyramid) within it.
- Trade after high-impact news (Fed, payroll, CPI, PPI); expect fake first moves at Fed chair speeches.

## Process, risk & psychology
- Log every day and every session on your own charts; it will feel pointless at first and then build pattern recognition ([0:02:44](https://youtu.be/kuURDD1ajdQ?t=164)).
- Do not just take the screenshot; go and watch the live stream for the nuance ([0:04:21](https://youtu.be/kuURDD1ajdQ?t=261), [0:18:51](https://youtu.be/kuURDD1ajdQ?t=1131)).
- Note the times in New York time and annotate afterward when you can ([0:43:53](https://youtu.be/kuURDD1ajdQ?t=2633)).
- Don't worry about annotating things that later prove unimportant; that is progress ([0:45:29](https://youtu.be/kuURDD1ajdQ?t=2729)).
- Advice: don't chase longs against the daily picture; if the BPR high is reached it signals manual intervention and he would be done for the day ([0:18:51](https://youtu.be/kuURDD1ajdQ?t=1131)).
- Pyramid into the short between the opening price and the OB mean threshold ([0:24:34](https://youtu.be/kuURDD1ajdQ?t=1474)).
- Claims 200+ handles of range called in advance on live YouTube in front of about 177,000 viewers; he says he was trading behind the scenes ([0:41:26](https://youtu.be/kuURDD1ajdQ?t=2486), [0:44:42](https://youtu.be/kuURDD1ajdQ?t=2682)).

## Glossary candidates
`Event Horizon` — zone between nearby NDOG/NWOG levels (quadrants) that draws price in like a black hole; max 60-day look-back.
`First presentation FVG` — first FVG in 9:30-10:00 with imbalance candle at 9:31 or later; exists in ETH and RTH; carried to 3:45.
`Gray pool / dark pool` — his name for hidden PD arrays like the Event Horizon.
`ETH / RTH` — electronic vs regular trading hours chart setting (TradingView).
`High resistance liquidity` — buy/sell stops behind a balanced price range that take manual intervention to reach.
`Manual intervention` — a human override of the algorithm, typically around Fed or other news.
`Propulsion block` — here, an up-closed order block after a bearish OB's CISD that accelerates price lower.
`BPR (as used here)` — a range price delivered through both ways, then left; high of it acts as resistance.
`Undelivered portion` — the unfilled part of an opening range gap.
`Nesting` — one opening gap sitting inside another, which intensifies the draw.
`Premium / discount ORG` — opening range gap that opens above / below the previous RTH close.
`Pyramid` — adding to a winning short within the valid zone.
