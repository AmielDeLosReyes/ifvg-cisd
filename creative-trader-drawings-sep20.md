# What his drawings define — the six open items (2026-09-20)

Follow-up to `reports/creative-trader-research-sep18.md`, which listed six things he never states in words. This file
answers them from **his own screens** (frames from his videos) and, where his charts can be matched to data, from
**bar-by-bar measurement** of the same minutes on NAS100ft 1-minute data (a close proxy for the NQ contract he trades:
on 10 Jun his CISD line, entry close, sweep low and session levels all reproduce to within ~1 point).

Tools: `research/ytlab/creative/measure_lib.py` (bars, session levels, CISD run, gap interaction),
`verify.py`, `aggregate.py`. Reviewed frames are in `research/ytlab/creative/review/frames/`, one JSON record per
video/short in `research/ytlab/creative/review/`.

Two kinds of statement are kept apart below:
- **His numbers** — read off his settings panel or his own drawn labels.
- **Measured** — what the data says about the same bars. Measurement describes what he did; it is not a rule he stated.

---

## 1. How big a swing must be to count as liquidity

**Mostly a non-question: he sweeps levels his indicator draws from fixed clock times, not from a swing-size rule.**

**His numbers** (indicator settings panel, `frames/crop_walk_392.png`, walkthrough 24 Mar):
- Timezone America/New_York; **Asia session 19:00–03:00, London 03:00–09:30, New York 09:30–16:00**; previous-day
  high/low on as well (dashed).
- News tool (`frames/crop_walk_1125.png`): **Fractal Threshold 2 points, Detection Wick Size 2 points**, "Delete on
  Mitigation" ticked — that is how DATA.H / DATA.L (news-candle swings) are found.
- SMT tool (`frames/crop_walk_530.png`): compares with **CME_MINI:ES**, **maximum candles for SMT = 200**.

**Measured:** rebuilding those sessions from the minute data reproduces his on-screen labels exactly, e.g. 10 Jun 2026:
Asia high 29,166.75, London high 28,999.13, London low 28,609.38, previous-day low 28,227.25 — all match the AH / LH /
LL / PDL lines on his chart. 22 Jun: London low 30,686.38 = his "LL" line.

What is left over: the lines he draws by hand ("$$$", "External Liquidity", "Buyside Liquidity"). In most reviewed
examples the originating swing is off the left edge of the replay window, so no count is possible. The two cases where
the swing was fully on screen point in different directions:
- 3 Aug short (`4QhVyExltpo`): the swept London low is a single spike-down candle with **8+ candles higher on its left
  and 1 candle before the reversal on its right** (`review/frames/4QhVyExltpo_0000_llcount2_crop.png`).
- 19 Aug (`vopCxsZYUf0`, ex. 4): the swept low (29,373.00) is the **tail of an unbroken run of 8+ candles each making a
  new low** — no left-side pivot at all (`review/frames/vopCxsZYUf0_sweep_count.png`).
- 20 Jul short (`YzUWvZkwUCM`): the swept high he marks "$$$" has about **14 lower candles on each side** on the
  1-minute chart (counted on a time-axis-aligned crop, ~08:31 to ~08:59).
So there is no "N bars each side" rule visible in his work — the same model is traded off a 14-bar pivot, an 8-bar
pivot and a low with no left shoulder at all. What makes a level tradeable for him is the label it carries
(session / previous day / data / an obvious high-low on the leg he is describing), not the shape of the swing.

## 2. What makes a higher-timeframe gap "holding / respected"

**His rule, in his tool:** a gap box stays on the chart until it is filled ("Delete boxes after fill" ticked, max FVG
size 3 x daily ATR, hide gaps below the chart timeframe) and an **inversion needs a candle body to close beyond the far
edge** — a close on the edge does not count (he shows this on 25 Mar, `notes.md`).

**Measured** — how deep price actually was inside the gaps he called "delivering from", before his entry:

| date | gap he named | depth reached | candle closed beyond far edge? |
|---|---|---|---|
| 10 Jun | 15m 28,753.94–28,824.19 | 73% | no |
| 10 Jun | 30m 28,753.94–28,821.13 | 72% | no |
| 24 Jun | 30m 29,883.63–29,920.88 | 82% | no |
| 7 Aug | 4H 29,555.00–29,590.75 | 78% | no |

So in the measured cases "respected" = price traded 70–85% of the way through the gap and **no candle body closed past
it**. (Depth is measured from the near edge: 1.0 = the far edge.)

**His own captions** (`review/frames/0NcYFJIHePE_0052_full.png`, reel "the one difference between FVGs that work and
ones that trap you"): one chart, two boxes side by side — the lower one captioned **"RESPECT"** (a single long wick
reaches into it, down to its dashed mid-line, then price rallies away; he puts an anchor icon on it) and the upper one
captioned **"DISRESPECT"** (candles chop back and forth inside it with bodies closing through). A slide from his own
guide (`review/frames/ozxSFGtPcCc_0116_full.png`, "Page 8 of 14") shows the same pair labelled *"Rejecting 15m FVG"*
(two touches, no body through) versus *"Disrespecting FVGs"* (one candle body closing through two stacked 5-minute
boxes).

On-screen corroboration from the reviewers: the 15m gap in the 7 Aug teaching replay is **tapped once and stays drawn
and intact** through the entry (`review/frames/NVhyZrJpoTc_0941_fvgbox.png`); the 1H box on 31 Jul is only **wick-tapped**,
no candle body enters it (`review/frames/EBUmil-juAM_0000_1hbox_crop.png`); and on 13 Aug a three-candle run plunges
straight through a 15m/30m box pair without either box disappearing or a body closing past the far edge
(`review/frames/x2TGuW3lxtY_0030_plungecount_crop.png`) — his tool's "delete after fill" did not fire there.

## 3. Which leg the OTE fibonacci is drawn on

**His numbers:** the fib shows only **0.5, 0.62, 0.79** between 0 and 1 (frames: flagship 9 Dec 1H example,
24 Jun, 19 Aug). His TradingView Fib Retracement settings dialog is on screen in one reel
(`review/frames/j6h6qXyOwA4_0128_full.png`): only 0, 0.5, 0.618 (labelled "0.62") and 0.79 are ticked.

**Measured anchors:**
- 22 Jun (`frames/xsby9NyXIHc_0335_smt.png`): "1" on the London low, "0" on the post-open high — exactly his verbal rule
  ("London low to where price was"). Data: 30,686.38 → 30,924.88; the pullback low 30,762.25 = **68% retracement**,
  i.e. inside 0.62–0.79.
- 10 Jun (frame `p_130.png`, 15-minute chart): "1" on the previous-day low, "0" on the high that leg made. Data:
  28,227.25 (11:40 on 9 Jun) → 29,193.63 (15:04). His three lines then compute to 28,710 / 28,594 / 28,430 — but the
  low his setup formed at was 28,772.63, a **44% retracement**, above his own 0.5 line, while he called it "in OTE".
- 4 Jun: he calls it "OTE of this huge range" with the fib spanning a multi-day range (reviewer read "0" at the
  previous-day high ~30,805, "1" at a swing low ~29,750). On that leg his entry area is ~50%; on the small leg of that
  morning (London low 30,163.13 → pre-open high 30,328.88) the same low is a **72% retracement**.

- 18 Jun (`h81_IIYPLi8`): "0" sits exactly on the swing labelled **LH**, "1" on an unlabelled low (not the AL line)
  (`review/frames/h81_IIYPLi8_0530_full.png`); his entry is tagged 30,469.00 with the stop ~69 points under, near the
  0.79 line.
- 31 Aug (`whyAN8viVx8`, re-entry): a small fib, "1" ≈ 29,482, "0" ≈ 29,415, price rejecting the **0.79** line on the
  retest leg immediately before he re-enters (`review/frames/whyAN8viVx8_0837_full.png`).

**So:** the anchors are always a swing low and a swing high of a leg he points at, and the levels are always
0.5 / 0.62 / 0.79 — but **which leg** is a judgement call, and the reviewed examples show the small session leg, the
day's own leg and a multi-day range all being called "the range". The same pullback can sit at 44%, 50% or 72%
depending on that choice.

A refinement from the August–September recaps: in the recap shorts where the fib labels were legible, the anchors sat
on **session extremes** — "0" on a PDL/LL and the far end on an AH/LH — rather than on a small intraday leg
(`review/frames/400pgx6S16w_0028_full.png`, `review/frames/to5Hx5nRurE_0020_full.png`). Since those levels are defined
by his session clock, the anchors themselves are objective; what varies is **which pair** he picks.

Across the 16 fib drawings the reviewers could read, the leg length ranges from about **110 points** (13 Aug:
"1" on the London low ~29,812, "0" on the high ~29,920) to **2,500 points** (9 Jul, on the 1-hour chart: "1" = 28,500.00,
"0" = 31,000.00) and a multi-week range on 24 Jul (28,409.75 → 30,056.25). The anchors usually sit on a labelled level
(LL, LH, AH, PDH, "External Liquidity") but not always — several sit on unlabelled swings.

## 4. The CISD run: how many candles, and how long after the sweep

**Measured, from his drawn CISD line vs the data:**

| date | his line | what that price is in the data | strict unbroken colour run | candles sweep → close through |
|---|---|---|---|---|
| 10 Jun | 28,918.38 | open of 08:31, first of **4** consecutive down candles into the low | same | 1 |
| 7 Aug (teaching replay) | 29,635.25 | open of 09:11, first of **2** consecutive down candles | same | 4 |
| 20 Jul | (line not read; entry 29,117.25) | his entry = the close of the candle that closed through the line built on the **5** consecutive up candles 08:40–08:44, line 29,123.88; data close 29,115.63 = his 29,117.25 within the feed offset | same | 4 |
| 24 Jun | 29,798–29,802.75 | open of 09:56, the **start of the whole up-leg** (an opposite candle sits inside it) | would have been 29,882.75 (1 candle) | — |

So on two of three he anchors at the first candle of the unbroken run that made the sweep; on the third he anchors at
the start of the impulse leg, ~80 points lower, with a contrary candle inside the "series". Reviewers looking at other
examples report the same thing in words: at the CISD line the candles "alternate colour" / "one white candle mixed in" /
"a small doji in the middle" — it is often not a clean single-colour run.
**His phrase "the series of candles that led into the sweep" is not one mechanical definition.**

**His own graphic** (`review/frames/HOR8xm0p22Q_0056_full.png`): a short example where the run is **shaded green and
contains exactly 4 up-close candles**, the "CISD" line is drawn at the bottom (origin) of that shaded run, the "SWEEP"
line sits above it, the inverted gap is boxed and labelled "iFVG", the position tool's entry line sits **on** the CISD
line, the stop box extends **above the swept high**, and the tool prints RR **1.77**. His on-screen text there calls the
shaded run "the last series of up-close candles leading into the liquidity sweep".

Counts that were legible on his teaching charts, sweep-extreme candle to the candle that closes through:
**5** (`5Mx1JiaQ5as`), **~5–6** (`4rs6QzZqz7Q`), **~6** (`2ewnMLYG4Sc`), **1** and **~4** (`BGubksIUasc`), versus the
measured 1 (10 Jun) and 4 (7 Aug). On a 15-minute CISD the run is small: 2 up-candles into an equal high that the next
candle sweeps (`r4aCT7kViVo`). Two separate CISD lines on one chart (an HTF one and the LTF entry one) are common
(`75jFwekG97I`, `sMymuU8HKl4`, `uVwzg_xfNo0`: "CISD" and "CISD (15)" ~29,044–29,088).

## 5. Where the stop actually sits

**What he teaches:** "above the high that was swept for shorts or below the low that was swept for longs. Not one tick
above ... above the actual sweep" (#25/#250).

**Read off his position tool, with the swept extreme measured in the data** (only dates where his contract and the data
contract agree — the feed rolls June→September on the evening of 18 Jun, a ~307-point step, so 16–18 Jun prices are not
comparable):

| date | direction | his stop | what it sits beyond | distance from the swept wick |
|---|---|---|---|---|
| 20 Jul | short | 29,192.25 (entry 29,117.25, risk 75) | the swept high (29,190.63 at 08:45) | **+1.6 points** |
| 5 Aug | short | 30,073.00 | the swept high (30,072.38 at 08:45) | **+0.6 points** |
| 7 Aug (teaching) | long | 29,565.75 | the second, higher low of the sweep (29,566.88) | 2.75 **inside** the deepest wick (29,563.00) |
| 10 Jun | long | ~28,864 (reviewer) / ~28,845 (mine) | the 1-minute gap left by the reversal candle (28,837.63–28,870.75) | 70–90 points **inside** |
| 4 Jun | long | ~30,246 | the inverted 1m/2m gap stack | 37 points **inside** |
| 24 Jul | short | ~28,568 | the order block ("my stop above the order block") | ~52 points **inside** |
| 31 Aug | short | not read; **57 points** (his words) | an order block, explicitly instead of the sweep stop: *"traditionally, your stop would be all the way up here. That's a 106 point stop. That's way too much for me"* | ~49 points **inside** |
| 31 Aug (re-entry) | short | 29,431.50 | just above the CISD line / turtle-soup high; entry 29,408 | 23.5 points of risk |
| 2 Sep | long | ~29,050 | below the 1m CISD line (entry ~29,083.75) | ~34 points of risk |
| 9 Jul | long | position tool caption **"Stop: 26.50"** | below the 30-second gap he entered on | 26.5 points of risk |
| 4 Sep | short | ~29,652.75 (entry ~29,606.50) | the order block he waited for after the CISD | 36.75 points **inside** the session high (29,689.50), 46 points of risk |

**In his teaching graphics** the position tool is left on screen with its captions, all in points:
46.75 / 91.00 (RR 1.95), 38.50 / 66.25 (RR 1.72), 7.75 / 26.25 (RR 3.39), 75.50 / 205.25 (RR 2.72),
17.50 / 23.50 (labelled RR 1.56 — the arithmetic does not match, flagged by the reviewer), and 1.77 on the CISD graphic
above. So the risk he draws in teaching examples runs from **7.75 to 75.5 points**.

So: when he does take the wick stop, the buffer is **under 2 points** (a few ticks). But in most of the measured trades
the stop sits beyond the **entry-side structure** — the inverted gap, an order block, the CISD line — at 23–75 points,
which is what keeps his risk inside his "I don't like over 100 points" limit. Both versions are his: the reels teach
the wick stop, the trade recaps mostly show the tighter structural one, and on 31 Aug he says out loud why he switched.

## 6. "Chop", "staircase", "narrative"

Frames were captured at every moment he uses these words (48 entries across the reviewed set). What is on screen:
- **"chop" / "barcoding"** — always a cluster of small, overlapping, alternating-colour candles, usually right before a
  displacement move (`review/frames/xsby9NyXIHc_0723_barcode.png`, he circles them by hand;
  `review/frames/FNZkkYsJhx4_*` price oscillating in a ~20-point band under the CISD line).
- **"staircase" / "market maker buy/sell model" / "path of least resistance"** — a hand-drawn red curved arc over the
  price path (`review/frames/h81_IIYPLi8_0400_full.png`, `review/frames/vopCxsZYUf0_0333_full.png`,
  `review/frames/Kz60TT2sZb8_0048_liq.png`). The arc is drawn freehand; nothing is measured.
- **"narrative"** — spoken over a general higher-timeframe chart (4H/1H boxes, session lines) with **nothing pointed
  at** in most cases; it refers to his own directional read, not to a chart object.
- The **grandma staircase** has one dedicated drawing (`review/frames/qN-6HY9kjeE_0108_full.png`): a red-marker sketch
  of a zigzag staircase "grandma can walk down" beside a single sheer diagonal drop. It is a sketch, not a chart, and
  carries no measurement; the same reel shows a real chart (NQU, 29,175–29,600, a DATA.L line) as the day he did not
  trade because of chop.

No numeric definition appears on screen in any reviewed example. These stay descriptions of what he sees.

---

## One example that matches the taught model end to end (20 Jul 2026, short)

Worth keeping as the reference case, because every piece is both drawn by him and reproducible in data:
- London high (29,107.00 by his session definition) taken at 08:32 Chicago; the high of the push = 29,190.63 at 08:45.
- The run into that high = 5 consecutive up candles, 08:40–08:44; its first candle's open = **29,123.88** = the CISD line.
- First candle to close below that line = 08:49 (close 29,115.63 in data); **his entry 29,117.25**.
- **His stop 29,192.25** = 1.6 points above the swept high; risk 75 points; he holds to a 15m order-block level.

## What this changes for a Pine build

Now defined well enough to code from his own settings/drawings: the liquidity levels (session clock times), the OTE
levels (0.5/0.62/0.79) once a leg is chosen, the inversion test (body close beyond), the "respected gap" test
(no body close beyond the far edge; his examples ran 70–85% deep), the stop variants and their sizes, and the
standard-deviation targets.

Still a judgement call, and the reviewed examples show him doing it differently on different days: **which leg the OTE
fib spans**, **which candles count as the "series" the CISD line is drawn from**, and **which stop model he uses on a
given trade**. Any Pine version has to pick one option for each of those three, and the choice materially changes the
signal (e.g. on 24 Jun the two CISD readings sit ~80 points apart).
