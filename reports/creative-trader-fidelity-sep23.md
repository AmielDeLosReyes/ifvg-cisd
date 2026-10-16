# Creative Trader replica — fidelity audit (2026-09-23)

The operator's challenge: *"26% winrate, 8/30 this month. There's no way it is this bad. I don't
feel we have truly replicated his strat."* He is right. This is the evidence.

Tools: `research/ytlab/creative/{fidelity.py, calibrate.py, find_positions.py}`. The replica is
`pinescripts/CreativeTrader_ConfirmationModel_v1.0.pine` with `mirror.py` as its Python twin.

---

## 1. Two of his four confirmations were not enforced

| his confirmation | in the replica |
|---|---|
| 1. liquidity sweep | approximated: **any new 20-candle extreme** counts (my stand-in for his hand-drawn "$$$"), plus session levels |
| 2. delivering from a higher-timeframe FVG | **OFF by default** (`i_reqHtf`): the strict version rejects *all eight* of his dated trades on our feed |
| 3. lower-timeframe FVG inverted by a body close | **MIS-CODED**: the test asked that no opposing 1m gap was still *alive*, instead of requiring one to have been *inverted*. Fixed 2026-09-23. |
| 4. CISD close | correct |

`CISD_MODE` was dead code (declared, never read), which is why "run" and "leg" scored identically.
Removed. Pre-fix copy: `mirror.py.bak-inv`.

## 2. Fidelity against his eight dated entries

Recall = how many of his trades the replica catches (±12 min, same direction). Extra = signals it
takes on those same days that he did not. Precision = hits / (hits + extra).

| sweeps | confirmation 3 | his 8 | extra | precision |
|---|---|---|---|---|
| 20-candle + levels | not required (shipped) | **4** | 10 | 29% |
| 20-candle + levels | required | 3 | 7 | 30% |
| his levels only | required | 2 | 7 | 22% |
| his levels only | not required | 3 | 8 | 27% |

No configuration passes ~30% precision: **the replica takes 2–3 trades for every one of his.**
Where it does catch him the match is tight (0.0–0.2 min, ~2 points), so the mechanics are right and
**selection** is the gap. Enforcing his own taught rule #3 *costs* one of his own trades, so either
our gap definition differs from his or he does not always wait for it.

Note: an earlier claim in this repo that entries matched "to the tick" (20 Jul 29,115.63; 7 Aug
29,652.63) came from an OLDER mirror build and no longer holds. `calibrate.py` also printed the
break-even stop, producing a bogus "risk 0.0"; it now prints the entry stop.

## 3. The larger problem: he does not trade one model

25 videos in `notes.md` show a trade with a date. Classified from his own words:

| what he actually did | count |
|---|---|
| 30-second chart entries | 4 (15 Jan, 21 May, 18 Jun, 9 Jul) |
| 15-minute chart entries | 3 (12 Feb, 24 Feb, 17 Jun) |
| 4-minute chart | 1 (9 Apr) |
| 3-minute order block | 1 (18 May) |
| 1-minute order block | 2 (25 Jun, 29 Jun) |
| 1-minute FVG-inversion close, no CISD | 1 (25 Mar) |
| pullback to the CISD rather than the CISD close | 4+ (18 Mar, 22 Apr, 24 Jun, 16 Jul) |
| outside his own 09:30–11:00 window | 1 (24 Jun, 11:09 ET) |
| **1-minute chart, entry at the CISD close — the replica's model** | **~4–5 of 25 (~20%)** |

The replica implements one entry model on one timeframe. Roughly a fifth of his shown trades are
that. No amount of parameter tuning closes that gap.

## 4. What his position tool shows (read from frames)

`find_positions.py` samples every video every 10s and scores each frame for his pastel position
tool (pink risk slab against a mint/blue target slab; calibrated on known frames — the earlier
colour thresholds found nothing because his charts are nearly monochrome).

| date | dir | entry | stop | target | RR | chart |
|---|---|---|---|---|---|---|
| 13 Mar | long | 24,677.75 | 24,610.75 (67.00) | 24,738.00 (60.25) | 0.90 | 1m |
| 18 Mar | short | 24,719.25 | 24,781.25 (62.00) | 24,647.00 (72.25) | 1.17 | 1m |
| 9 Apr | short | 25,037.25 | ~25,103.50 (66.25) | 24,952.50 (84.75) | 1.28 | **4m** |
| 22 Apr | long | 26,880.25 | 26,848.50 (31.75) | 26,902.75 (22.50) | 0.71 | 1m |
| 24 Jun | short | 29,801.00 | 29,906.50 (105.50) | 29,520.50 (280.50) | 2.66 | 1m |
| 20 Jul | short | 29,119.00 | 29,194.00 (75.00) | ~28,997.00 (122.00) | 1.63 | 1m |

Most of his risk-to-reward sits near 1:1, matching his stated habit. **Caution:** not every
position box on screen is an executed trade — the 16 Jul frame shows a *long* at 2.33 RR while his
narrated trade that day was a short at the CISD close. Boxes must be tied to the narration.

Also visible on his 20 Jul chart: a band labelled **"1-30-15"** — his indicator merging the 1m, 30m
and 15m gaps into one band. That is confirmation #2 as he actually uses it, and it is the one thing
we have never implemented. His own words: *"connect all of the fair value gaps and make it one big
fair value gap because you're going to need to inverse all of them"*, and *"delivering from HTF"* =
the HTF gap was **tapped**, not inverted.

## Verdict

The replica is not his strategy. It enforces two of his four confirmations, models one of the
several entry types he uses, and takes two to three trades for every one of his. **Its 26% win rate
is a fact about its own trade population and says nothing about his results.** The number should be
retired rather than held against him — and equally, nothing here verifies his ~78–80% claim, which
a previous replay of his "two red days in a month" put closer to ten red days.

To go further, the order is: (1) implement the merged multi-timeframe gap band so confirmation #2
can be on, (2) add his other entry types (pullback to CISD, order-block close, inversion close) and
timeframes, (3) harvest 15–25 more dated trades so there is something left to validate on after
fitting. Each step is real work and none removes the discretionary selection at the centre of it.
