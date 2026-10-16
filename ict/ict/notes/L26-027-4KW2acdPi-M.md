# L26-027 — Friday Review On NQ & PreMarket Session Rules Revisited
ID: 4KW2acdPi-M · URL: https://www.youtube.com/watch?v=4KW2acdPi-M · Duration: 33:40
Content type: market review (recorded Saturday Aug 29, 2026, 7:15 pm ET; reviews Thursday Aug 27 and Friday Aug 28 on NQ), plus a closing segment (~0:24:39 onward) demonstrating live feed vs TradingView market replay
Teaching density: medium (the 7:00–9:00 rule is taught clearly, then a lot of persona/credibility talk and the replay demo)

## Summary
The video restates and demonstrates ICT's 7:00–9:00 am ET pre-market rule: the behavior of that two-hour window (trending vs consolidating) tells you how the AM session after 9:30 will trade, and a session in consolidation is followed by a session that moves. He grades Thursday's 7–9 range (trending) and shows its levels (a SIBI at the upper end, the CE, octants) still acting as references on Friday, where the new day opening gap (NDOG) CE and the graded levels steered Asia and London. Friday's own 7–9 window was a tight block with equal highs at 29,539, so he expected a trending (bearish) AM session; he shows the bodies failing to reach CE, a validated iFVG, and the sweep of the August 6 low. He then gives a "nothing burger profile" coinage and the principle that the algorithm refers to time first, price second. The last third is a demo (live feed vs market replay) to answer accusations that his executions are replays.

## Concepts

### 7:00–9:00 am ET dealing range: trending vs consolidating predicts the AM session  (aliases: 7-9 rule, pre-market dealing range)
- **Kind:** rule
- **What ICT says:**
  - Look at the range between 7:00 am and 9:00 am ET (a "small little two-hour window"); the highs and lows of that window are the bookends. When a report is due at 8:30, use 7:00 to 8:30 instead of 9:00 (he mentioned this for a CPI or PPI day).
  - Determine how price books: trending ("allowed to protract", moving) versus consolidating (a block, a swatch of price that cannot even get to the CE of an earlier wick with bodies).
  - If 7–9 is a trend, the AM session is "a block, up and down, up and down" (choppy, harder to trade for an average student; he can trade it but it is not for those who do not understand this algorithmic phenomenon).
  - If 7–9 is consolidation, the AM session after 9:00/9:30 should trend. Friday: "Consolidation between 7:00 and 9:00 on Friday tells us what is likely to occur in the AM session... We're going to get trending environments."
  - General statement of the logic: "If the previous session is in consolidation, the next session's going to move. The next session after that expected to be in consolidation, but be prepared in the event that it is trending in the 24-hour cycle." The algorithm compresses into holding patterns, lulls traders into thinking nothing is happening, then makes a big move.
  - Grade the 7–9 range: draw the high-to-low fib; keep the 50% (equilibrium) line a different color; above it is premium, at or below is discount (his words: "anything at that price or higher... premium. Anything less than this level or at that level is considered discount").
  - The levels carry forward across sessions: "my levels don't have an expiration date"; Thursday's 7–9 levels were still in use on Friday. Looking back "the last three sessions" supplies all the information needed; you "don't even need a daily chart".
  - Source claim: no Wyckoff book teaches looking at the 7–9 range to predict how the AM session trades; he repeats that the premium/discount concept is also not in Wyckoff.
- **How to identify:** mark the high and low of 7–9 (e.g., Thursday: high at the 7:00 candle, low at 8:36 am); ask if bodies rotate in a tight block (consolidation, exact equal highs) or progress (trend).
- **How to use:** consolidation → expect trending AM session; trend → expect block/chop AM. Direction of the trend comes from higher-timeframe narrative and where the bodies fail (see below).
- **Example in this video:** Thursday Aug 27 7–9: clear trend; high at 7:00, low at 8:36; AM session was chopping ("block", seek and destroy; see [[L26-021]]). Friday Aug 28 7–9: a block whose two highs were the same price, 29,539, with bodies unable to touch the CE of Thursday's range wick; AM session then trended down.
- **Timestamps:** [0:00:51](https://youtu.be/4KW2acdPi-M?t=51) no Wyckoff source · [0:01:39](https://youtu.be/4KW2acdPi-M?t=99) rules and window, 8:30 caveat · [0:03:15](https://youtu.be/4KW2acdPi-M?t=195) Thursday is a trend · [0:04:03](https://youtu.be/4KW2acdPi-M?t=243) trend means AM session is a block · [0:11:56](https://youtu.be/4KW2acdPi-M?t=716) Friday is a block · [0:12:48](https://youtu.be/4KW2acdPi-M?t=768) previous session consolidation → next moves · [0:14:23](https://youtu.be/4KW2acdPi-M?t=863) consolidation 7–9 → trend after 9
- **Nuance / caveats:** Extends the Monday review in [[L26-026]] (bodies not wicks; pop vs trend). The "8:30 report" exception is new here. On Thursday the low printed at 8:36, after 8:30, so he evidently still used the full window that day (caption does not say why).

### Anchoring FVGs to key levels ("salient"): only trade gaps tied to a graded level  (aliases: salient FVG, tethered FVG)
- **Kind:** rule
- **What ICT says:**
  - On Thursday's graded range he points out one SIBI sitting in the premium side near the 0.875 level (captioned "optimal at 8.75") and ignores the other FVGs: "Why? Because it's not salient. And it has to be anchored to a key level. Period."
  - On Friday the iFVG is valid because it sits on the upper quadrant, 0.25, of the graded 7–9 range: "Isn't that what you would expect if the market wasn't algorithmic?"
  - "We don't trade supply and demand. We supply the demand": no indiscriminate "buy in a zone"; entries come at discount PD arrays like the NDOG CE.
- **Timestamps:** [0:05:40](https://youtu.be/4KW2acdPi-M?t=340) · [0:06:27](https://youtu.be/4KW2acdPi-M?t=387) · [0:17:32](https://youtu.be/4KW2acdPi-M?t=1052) · [0:10:24](https://youtu.be/4KW2acdPi-M?t=624) NDOG CE as a discount PD array
- **Nuance / caveats:** Same logic as the "tethered to an octant" validation in [[L26-026]].

### New Day Opening Gap (NDOG): definition, CE and persistence  (aliases: NDOG)
- **Kind:** definition / rule
- **What ICT says:**
  - NDOG = the difference between the 5:00 pm ET settlement and the 6:00 pm restart for futures.
  - Extend the NDOG line to the right continuously: because price traded up to it once it is "not one and done", it is not thrown out. His levels persist.
  - Friday Asia: price used the CE (midpoint) of the NDOG as support and rallied; for an Asian trader looking for short targets (and for those watching the midnight opening price), the NDOG CE is a clean discount PD array target.
  - Later (London/NY): price came down to the NDOG, fluttered through it, and traded back up into it where it acted as a premium PD array, then dropped lower to take the August 6 low. Another idea: during the first hour's dealing range (9:30–10:30) wait for price to trade above and up into the NDOG.
  - On extended trading hours for Nasdaq futures: he is not worried; it will make his methods better.
- **Timestamps:** [0:07:15](https://youtu.be/4KW2acdPi-M?t=435) definition · [0:08:49](https://youtu.be/4KW2acdPi-M?t=529) extend continuously, no expiration · [0:09:37](https://youtu.be/4KW2acdPi-M?t=577) price uses CE of NDOG in Asia · [0:19:06](https://youtu.be/4KW2acdPi-M?t=1146) premium PD array later
- **Nuance / caveats:** The caption for the midnight-open remark is unclear; I read it as a reference to the midnight opening price as a premium/discount split.

### Bodies failing to reach CE as a bearish order-flow read; relative equal highs with the bodies  (aliases: wicks do the damage, run on relative equal highs)
- **Kind:** rule / refinement
- **What ICT says:**
  - On Friday the highest body of a swing high and a later set of bodies slightly higher create "relatively equal highs with the bodies" (the wicks are "allowed to do the damage"); that is a run on relative equal highs.
  - The bodies cannot touch the CE of Thursday's 7–9 gap (SIBI), even though two wicks poke above ("I can't do it"). Interpreted per his order-flow teaching using candlesticks and PD arrays: bearish.
  - Then price gives up; a close below validates a potential inversion fair value gap; price trades up to it, breaks lower, takes the short-term low, rips back up to a gap sitting on a graded level.
- **How to use:** if bodies can't reach the CE of a premium array that anchors the reference range, expect lower prices; confirm with a close through the next structure, then use the iFVG on the retest.
- **Example in this video:** NQ 1m, Fri Aug 28: equal body highs at 29,539 (7–9 window), failure at Thursday's SIBI CE, break lower, retrace into the iFVG sitting on the 0.25 line, then continuation to the August 6 low.
- **Timestamps:** [0:14:23](https://youtu.be/4KW2acdPi-M?t=863) · [0:15:11](https://youtu.be/4KW2acdPi-M?t=911) bodies and relative equal highs · [0:15:59](https://youtu.be/4KW2acdPi-M?t=959) bodies can't reach CE, bearish · [0:16:45](https://youtu.be/4KW2acdPi-M?t=1005) close validates iFVG
- **Nuance / caveats:** Caption jumbled in places; the exact candle references are described only relatively.

### Inversion FVG retest and "premium sensitivity" at the octant  (aliases: iFVG, premium sensitivity, unfinished business)
- **Kind:** example / rule
- **What ICT says:**
  - After the close below that validated the iFVG, price traded up into it "beautifully", worked the low, broke through, and accelerated lower to the short-term low; then ripped back up to a gap on the graded level and tapped the iFVG one more time before "ripping all the way through".
  - Premium sensitivity on the 7–9 range: sensitivity from the midpoint to the low of the range; price went to the octant line (measured from the range low to high) "and one more tick" and then fell.
  - "Unfinished business at the August 6th low": he had tweeted that price would go there and it did, taking out the August 6 low (after flutters through the NDOG).
- **Timestamps:** [0:16:45](https://youtu.be/4KW2acdPi-M?t=1005) · [0:18:19](https://youtu.be/4KW2acdPi-M?t=1099) why it goes there, premium sensitivity · [0:19:54](https://youtu.be/4KW2acdPi-M?t=1194) takes out Aug 6 low
- **Nuance / caveats:** The exact octant is not named in the captions (the iFVG sits on "0.25").

### First hour's dealing range (9:30–10:30), equilibrium and the "nothing burger profile"  (aliases: first hour dealing range, new coinage: nothing burger profile)
- **Kind:** refinement / new coinage
- **What ICT says:**
  - At about 10:30 the range between 9:30 and 10:30 forms (the first hour's dealing range): "draw that out on your chart, find equilibrium on that, and then wait for price to get above and trade up into the NDOG." Stops sit right above that high.
  - He then calls the consolidating chop after the move a "nothing burger profile" ("I'm coining the term. Don't use it"): price hammers down into consolidation and does nothing.
  - Time-first principle: "the algorithm is going to refer back to time first. Time is more important than the actual price right now." Before the reference time price was trending; now consolidating, so the next bit of business is trending. Direction: bearish, because price left the highs and cannot reach CE; it gave a wonderful entry.
  - Retracing back up into the 9:30–10:30 dealing range and bumping its high; "because it's Friday, this is consolidate rest of the day and kill everybody".
- **Timestamps:** [0:19:54](https://youtu.be/4KW2acdPi-M?t=1194) first hour's range and NDOG · [0:20:41](https://youtu.be/4KW2acdPi-M?t=1241) nothing burger, time first · [0:21:28](https://youtu.be/4KW2acdPi-M?t=1288) bearish direction and Friday behaviour
- **Nuance / caveats:** "Friday consolidates the rest of the day" is a stated tendency in this clip.

### Session structure he cites (24-hour cycle and NY subdivisions)  (aliases: fractals of the day)
- **Kind:** definition
- **What ICT says:** Asia, London, New York in that order; New York subdivides into pre-market session, AM session, first hour's dealing range, the two-hour lunch, PM session, then market on close / last hour. How the previous session traded indicates what to expect, because the algorithm cycles compression and expansion.
- **Timestamps:** [0:13:35](https://youtu.be/4KW2acdPi-M?t=815)

## Rules, checklists & numbers stated
- 7:00–9:00 am ET window (or 7:00–8:30 when an 8:30 report is due) determines AM session behavior: trend → chop; consolidation → trend.
- A consolidating session is followed by a moving session; the session after that is expected to consolidate again but stay alert.
- Grade the range with a different-colored 50% line; premium above, discount at or below.
- FVGs only matter when anchored to a key level (e.g., graded 0.25/0.875 lines); otherwise "not salient".
- Levels do not expire; extend NDOG and previous 7–9 levels to the right.
- NDOG = 5:00 pm settlement to 6:00 pm restart (ET).
- Price levels: Friday 7–9 equal highs 29,539; Thursday range low at 8:36 am; unfinished business at the Aug 6 low.
- First hour's dealing range: 9:30–10:30.

## Process, risk & psychology
- "How not to be surprised by the market": the quiet, choppy session precedes the big move, so don't switch off or lose focus ([0:14:23](https://youtu.be/4KW2acdPi-M?t=863)).
- Casual listeners miss the free, public rules (7–9, premium/discount); watch the lecture videos and the trader round-ups ([0:03:15](https://youtu.be/4KW2acdPi-M?t=195)).
- Live vs replay credibility segment ([0:24:39](https://youtu.be/4KW2acdPi-M?t=1479) to the end): when recording executions his screen shows the live market-open countdown (upper left), a countdown to candle close on the price axis, no replay toolbar; replay mode shows blue controls, a different banner, and candles that complete at once. He posts screenshots to a tweet thread while the video renders, and offers a $1M challenge to anyone who can fake it. This is mainly credibility material, not a trading lesson.
- Expect to be stopped sometimes; he posts "when I get stopped out because it's happened a few times" ([0:31:53](https://youtu.be/4KW2acdPi-M?t=1913)).

## Glossary candidates
`7–9 rule` — 7:00–9:00 am ET trending/consolidating read that previews the AM session.
`Nothing burger profile` — his one-off coinage for a consolidating chop session.
`Salient (FVG)` — an FVG anchored to a key/graded level and therefore worth using.
`NDOG` — new day opening gap: 5 pm settlement to 6 pm reopen.
`Run on relative equal highs with the bodies` — equal body highs taken, wicks ignored.
