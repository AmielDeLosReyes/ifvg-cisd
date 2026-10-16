# M24-003 — ICT 2024 Mentorship \ Lecture #3 (August 7, 2024)
ID: ZkLc4-adodg · URL: https://www.youtube.com/watch?v=ZkLc4-adodg · Duration: 2:22:58
Content type: mixed (lecture + recap of a demo trade + long mindset section)
Teaching density: high for 0:14–0:58 and 1:08–1:59; the rest (about 40%) is a rant about critics, motivation and mindset

## Summary
This lecture covers the "afternoon protocol" plus the main underlying narrative for the 2024 mentorship: the **New Day Opening Gap (NDOG)** and **New Week Opening Gap (NWOG)** as the larger draws ("black holes") on price. ICT explains exactly how to mark them on index futures (the 5:00 PM close to 6:00 PM open), how long they stay valid (5 trading days / 5 weeks), how to grade them (high, low, CE and quarter levels) and how a cluster of them gives you a directional filter. They let you anticipate where relative equal highs/lows will be engineered. He then gives a rule: when the morning has no medium- or high-impact news, skip the morning and trade the afternoon. Today's afternoon driver was the 1:00 PM ET bond auction. He walks through his NQ 1-minute demo short on Aug 7, 2024. The entry was a bearish order block built from a SIBI whose CE price could not reach, and the trade pyramided 6+4 contracts down to the London lows for over 100 handles. He also gives his first answer on how to hold trades longer, his size categories for price runs (scout <50, intermediate 50+, larger 100+ handles), and Caleb's three-month study plan.

## Concepts

### New Day Opening Gap (NDOG)  (aliases: new day opening gap, NDOG; label "ND" + date)
- **Kind:** definition + rule
- **What ICT says:**
  - Applies to the **index futures** in this teaching. Every day except Friday, the market stops at **5:00 PM ET**, pauses for one hour and reopens at **6:00 PM ET**.
  - On a **1-minute chart**, take the close of the **4:59 PM candle** (the last print before the stop) and the **opening price of the first 6:00 PM 1m candle**. The space between those two prices is the NDOG. You do not need live data for this, and the effect on price lasts for weeks.
  - **Three levels:** the gap high (whichever is higher of the 5 PM close and the 6 PM open), the gap low (whichever is lower), and **consequent encroachment (CE)**, the midpoint. He also adds the **0.25 and 0.75 levels** with a Fib, which splits the gap into equal quarters ("quadrants").
  - Draw each level with a **horizontal ray** that extends right forever. Put the label in the middle/right and **always include the date**, because the date tells you how old (and how important) the level is.
  - **Dating convention:** a gap that forms Tuesday evening at 6 PM is **Wednesday's** NDOG, because it is the reference for Wednesday's trading.
  - **Life cycle: 5 trading days** (not calendar days). If there is a holiday, skip it and add a day. Example: a gap formed Tuesday for Wednesday is valid Wed (day 1), Thu (2), Fri (3), Mon (4), Tue (5), so it is good "until Wednesday next week". Keep **five** NDOGs on the chart. This is a starting rule, not a hard cutoff: he still uses gaps that are **9 months old** when they fit the narrative.
  - Filling the gap does **not** make it stale. He contrasts this with retail "gap fill, done" thinking and with supply/demand "fresh zone" logic. Price keeps coming back to these levels.
  - Price is especially sensitive to an NDOG it has **touched only once**. It is still "hot" and price will very likely be drawn back to it ("just a guarantee", one of the very few guarantees in trading, he says).
- **How to identify:** 1m chart → 4:59 PM close vs. 6:00 PM first open → mark high, low, CE (and quarters) → label with date → keep the last 5.
- **How to use:**
  - It is the **underlying narrative / draw on liquidity** behind the intraday REH/REL objectives. An intraday target is "linked to" an NDOG and/or NWOG.
  - **Clustering filter:** look only at the last 5. If most of them sit above the current price (maybe one at or below), expect price to gravitate up, and the reverse when they cluster below. If you are anticipating a short but the gaps cluster above, give the first 30 minutes after 7:00/8:00/9:00 a chance to spike up into them in a thin price run. Then wait for a market structure shift or breaker and/or an **inversion FVG** before shorting.
  - Clustering is a **filter, not a hard rule**. A cluster below doesn't mean "short only". If he wants a long, he first waits to see whether they drop price toward the gaps.
  - The trade does not need to reach the NDOG that day to be profitable. If it hadn't traded there during the day, he would have looked for it to happen in **London that night**.
- **Example in this video:** NQ 1m. On Tue Aug 6, the 5 PM close was **above** the 6 PM open, so it was a **down gap**. That made it Wednesday Aug 7's NDOG. After the open, price traded up into the gap and stopped exactly at a quadrant level, **18,049.50** (caption "18, 04950"), which he calls perfect. It hovered around the **upper quadrant**, dropped to CE, then to the **lower quadrant**, and took a low there. It did not touch the actual gap low before rallying away. At 7:00, 8:00 and 9:00, price was far above the gap. In the afternoon (during the stream), price fell back and closed into it.
- **Timestamps:** [0:17:21](https://youtu.be/ZkLc4-adodg?t=1041) definition starts · [0:18:58](https://youtu.be/ZkLc4-adodg?t=1138) the 4:59 close and 6:00 first print · [0:27:53](https://youtu.be/ZkLc4-adodg?t=1673) dated for the next day, 5 trading days · [0:31:52](https://youtu.be/ZkLc4-adodg?t=1912) quarters, stop at 18,049.50
- **Nuance / caveats / changes:** He first introduced NDOGs in Twitter Spaces. He says "it's 2024" and that he is now showing his hand: the journal routine, the clustering filter, the 150-handle proximity rule and "touched once = hot". If the exchange ever went to 24-hour trading and the NDOG disappeared, he says you would still have NWOGs and REH/REL.

### New Week Opening Gap (NWOG)  (aliases: new week opening gap, NWOG; label "NW" + date)
- **Kind:** definition + rule
- **What ICT says:** The NWOG is the range between **Friday's 5:00 PM close** and **Sunday's 6:00 PM open**. Mark it the same way as the NDOG (high, low, CE) but label it NW. **Life cycle: 5 weeks**, so keep five of them. Like NDOGs, they work 6–9 months later because they are real places where the market didn't trade efficiently. There is only one NWOG per week against five NDOGs. **For a swing trade the NWOG has more impact**, because the market makers have had the whole weekend to digest information before setting that opening price.
- **How to identify:** 1m chart, Fri 4:59 PM close vs. Sun 6:00 PM first print.
- **How to use:** It is the higher-tier "black hole" draw. Use it together with NDOG clusters for the directional filter and as targets for holding longer.
- **Example in this video:** none specific. He points to price dipping into a gap and calls that the first and second time it passed into it.
- **Timestamps:** [0:28:41](https://youtu.be/ZkLc4-adodg?t=1721) definition and 5-week cycle · [0:45:19](https://youtu.be/ZkLc4-adodg?t=2719) NWOG vs NDOG for swing trades
- **Nuance / caveats / changes:** Keep the full history on a separate TradingView layout if you want to track older gaps. You must also keep count of how many times each has been referred to.

### Opening-gap housekeeping (journal + layouts)
- **Kind:** process
- **What ICT says:** He keeps a **spiral notebook** with one column per market (usually S&P, Nasdaq, sometimes the bond market). For every NDOG he writes the high, low, CE and the date/week it formed. He personally looks at any of them when price is **within 150 handles**. On TradingView, build separate **layouts**: one with only NWOGs and one with only NDOGs for your market. You pull them up at session start and keep your execution chart clean (he teaches as if from one laptop).
- **Timestamps:** [0:26:16](https://youtu.be/ZkLc4-adodg?t=1576) journal, 150 handles · [0:29:30](https://youtu.be/ZkLc4-adodg?t=1770) layouts

### Consequent Encroachment (CE) vs. Equilibrium; gap quadrants  (aliases: midpoint, "consequent encroachment")
- **Kind:** definition + refinement
- **What ICT says:**
  - **CE is the midpoint of any gap or inefficiency.** It is not called equilibrium. **Equilibrium** belongs to a *range* that has been delivered up and down (a trading range). A gap is not a range: no trades printed between the 5 PM stop and the 6 PM restart.
  - Grade the gap with 0.25 / 0.5 / 0.75 to get equal quarters. Price respects the upper and lower quadrants to the tick.
  - **SIBI (down-close FVG):** the best shorts form in the **lower half**, and you want the upper half left open. **BISI (up-close FVG):** the best longs fill in the **upper half**, leaving the lower half open. When price can't fill that half and runs, it is a **breakaway gap**. That tells you the algorithm will move quickly, so anticipate large range expansion.
- **How to use:** CE serves as an entry level and as a **strength/weakness gauge** (see the order block concept below).
- **Timestamps:** [0:31:04](https://youtu.be/ZkLc4-adodg?t=1864) CE vs equilibrium · [0:33:25](https://youtu.be/ZkLc4-adodg?t=2005) CE rules for SIBI/BISI, breakaway gap

### Sell-side / buy-side delivery vs. liquidity; inefficiency vs. BPR  (aliases: one-sided delivery, "liquidity void" critique)
- **Kind:** definition / refinement
- **What ICT says:**
  - **Liquidity** means real resting orders, the buy stops above highs and sell stops below lows. He calls it the "lifeblood"/"heartbeat" of the market.
  - An **inefficiency** (FVG, gap) has had **one-sided delivery**. A down move is *sell-side delivery*, and what it lacks is *buy-side delivery*, and vice versa. So "sell-side delivery" and "sell-side liquidity" are not the same thing.
  - Chris Lori's "liquidity void" is a misnomer, ICT says: there was buying (or selling) in it, and what's missing is the opposite side of delivery.
  - Price merely trading back into an FVG does not balance it. It must trade there **and leave**, and then it becomes a **balanced price range**.
  - **Hierarchy of draws:** NDOG/NWOG and relative equal highs/lows rank above inefficiencies (FVGs). Inefficiencies are "subordinate and less important" because the algorithm places more weight on the former. Real opening gaps outrank everything because no trades took place there.
- **Timestamps:** [0:22:10](https://youtu.be/ZkLc4-adodg?t=1330) what the gap lacks (sell-side delivery) · [1:53:37](https://youtu.be/ZkLc4-adodg?t=6817) hierarchy of draws · [1:55:15](https://youtu.be/ZkLc4-adodg?t=6915) delivery vs liquidity · [1:57:39](https://youtu.be/ZkLc4-adodg?t=7059) BPR and the Lori critique

### Engineering liquidity (predicting REH/REL before they form)  (aliases: engineered liquidity, design of liquidity)
- **Kind:** rule / refinement
- **What ICT says:**
  - Midnight NY is the start of the "true day". The algorithm refers back to midnight and everything after it for liquidity and inefficiencies, and beyond that to NDOG/NWOG.
  - Starting at **7:00 AM** (then 8:00, 9:00), look for relative equal highs/lows or "smooth" price that forms after the session changeover. In the **30 minutes after each top of hour**, anticipate a move in the opposing direction (this continues from Lecture 2).
  - Because a known NDOG/NWOG draw gives you a "magnetized reference point", you can predict **where relative equal highs/lows will be built before they form**. That, he says, is exactly what engineering liquidity means.
  - Example rule: with an NDOG below and REH forming after 7:00, **never short right away** on the first drop. Let price run those highs first (a **Judas swing**), and don't chase.
- **How to identify / REH-REL quality filter:** Two swings close together, and the right-hand swing must sit inside the left one. For relative equal **lows**, the right low has to be **higher** than the previous low. Then it is a high-probability REL to draw to. The NDOG below acts as "rocket fuel" on top of that.
- **Example in this video:** NQ, Aug 7 2024. In the 7:00 and 8:00 hours, price built REH and REL. The NDOG sat far south, so he expected the highs to run first. Price dropped, and retail chased it short. After 9:00, it rallied and pumped above the highs (one, two, three relative equal highs), made another REH, then broke down. He calls that a Judas swing into 9:00 that chops traders up all morning.
- **Timestamps:** [0:14:57](https://youtu.be/ZkLc4-adodg?t=897) NDOG as underlying narrative; 7/8/9 intervals · [0:50:57](https://youtu.be/ZkLc4-adodg?t=3057) predict REH/REL before they form · [0:52:31](https://youtu.be/ZkLc4-adodg?t=3151) don't chase; Judas swing · [1:28:40](https://youtu.be/ZkLc4-adodg?t=5320) REL right-side rule
- **Nuance:** Once the real draw is lower, the REH above can simply be left alone ("they can stay in play"). He doesn't need them taken before shorting the afternoon.

### Afternoon session protocol on no-news mornings (bond auction setup)  (aliases: PM session, 1:00 bond auction)
- **Kind:** rule / narrative filter
- **What ICT says:**
  - Check the economic calendar (ForexFactory, Econoday). When the **morning has no medium- or high-impact news**, the morning tends to be lackluster and rangy: false breakouts, pulls back into the previous day's range, or reverses an attempt higher. It "demands a lot more experience" because you get caught offside.
  - Morning drivers usually come at **8:30 ET**, sometimes 10:00, with crude oil inventories at 10:30. Today had none, which is why he booked his eye appointment for the morning.
  - **Rule (write it down):** no medium/high-impact data in the morning → trade the afternoon, because the cleaner price action comes after New York lunch.
  - On such a day, a **bond auction at 1:00 PM ET** (a medium-impact driver, not very volatile) is the afternoon catalyst. He says he has never taught this before. **Condition:** it only counts as this clean setup when there is **no morning news**. With morning drivers, it doesn't hold.
  - Afternoon timing: he wants to be at the charts by **1:30 PM**. Moves can start a bit before 1:30, which is fine. The **1:30–2:30** window usually holds a "sweet spot". If nothing forms 1:30–2:00, use the **2:00–3:00 Silver Bullet**. If that is missed or sideways, use the **3:00 hour to the close**.
  - If you miss the move, use Lecture 2's technique: a **sub-1-minute chart** to get in sync with a run already unfolding on the 1m/5m.
- **How to use:** Set the narrative before 1:00. The draw is below (SSL plus NDOG), so you are looking to short into the auction release and treat the release as fuel for the run.
- **Timestamps:** [0:04:29](https://youtu.be/ZkLc4-adodg?t=269) no-news mornings are rangy · [1:09:22](https://youtu.be/ZkLc4-adodg?t=4162) bond-auction condition · [1:19:49](https://youtu.be/ZkLc4-adodg?t=4789) rule: trade the afternoon, 1:30–2:30 · [1:26:15](https://youtu.be/ZkLc4-adodg?t=5175) 1:30, 2:00 Silver Bullet, 3:00 hour
- **Nuance:** Caleb's own focus is the **7:00–11:00 AM NY** window: start at 7 or 8, or just wait for the 9:30 bell and use **9:00–11:00**. The afternoon rules are given "for completeness". He says he will also show London later.

### Trading ahead of a news release (pre-1:00 logic)
- **Kind:** rule / example
- **What ICT says:** People ask how he knows direction before news. His answer: if price has already rounded over, left an FVG whose **candle bodies respect it**, and started **displacing lower** before the release, the likelihood is that it will explore below the nearby lows, because that's where liquidity is. Buying and selling after the release does not cause the move. The market is already running before the number comes out.
- **Example in this video:** NQ 1m. At **12:42 ET**, price trades up and rolls over, leaving an FVG ("one of the 81 PD arrays") with bodies respecting it, then displaces lower going into the 1:00 auction. He lists the draws below:
  - (1) a short-term low, the day-session low since 7:00, with minor SSL
  - (2) the London session low, a relative equal low that passes the right-side-higher rule
  - (3) the NDOG further down as the "black hole"
- **Timestamps:** [1:34:20](https://youtu.be/ZkLc4-adodg?t=5660) 12:42 FVG roll-over · [1:36:44](https://youtu.be/ZkLc4-adodg?t=5804) the logic before news · [1:39:12](https://youtu.be/ZkLc4-adodg?t=5952) three draws below

### Bearish order block from an FVG that failed to reach CE (strength/weakness signature)
- **Kind:** entry model / refinement
- **What ICT says:**
  - When a retracement runs up into a SIBI and **can't even touch its CE** (it comes close and falls short), that is an "algorithmic signature" of weakness. He then treats that up candle as a **bearish order block**. Once the candle closes, he needs price to move away and come back up into the **bottom of that candle**, and he sells there.
  - **Conditional rule:** if the retrace *had* touched the CE, he would not take the trade. He would wait for another attempt a little above CE and short in the upper part of the gap.
  - PD arrays are fixed levels to enter and exit on, but he also uses them to **measure strength and weakness**.
  - **Two stacked SIBIs:** expect price might go up into the higher one. If it fails at the **lower one's CE** and a news driver is coming, he is happy to be short. If it had touched the lower one's CE, he would expect a run into the higher gap, and the stop would then have to go above that (higher) gap's CE. Which gap he means is slightly unclear in the caption.
- **How to identify:** a SIBI in a bearish narrative → a retrace whose wick stays below CE → treat that candle as a bearish OB → the next candle trades up into its body/low without passing CE or the candle high → enter short.
- **Example in this video:** NQ 1m, Aug 7, shortly before 1:00 PM. A candle runs into the SIBI, misses CE and closes. The market displaces below that bearish OB. The next candle opens, trades up, touches it, and he shorts. The candle low was **18,320.25** and his fill was **18,321.25** (6 contracts).
- **Timestamps:** [1:43:59](https://youtu.be/ZkLc4-adodg?t=6239) fails to touch CE · [1:44:47](https://youtu.be/ZkLc4-adodg?t=6287) bearish OB rule, what he'd do otherwise · [1:45:37](https://youtu.be/ZkLc4-adodg?t=6337) PD arrays as a strength gauge · [1:47:12](https://youtu.be/ZkLc4-adodg?t=6432) fill price, two FVGs

### Live/demo trade recap: NQ 1m, Aug 7 2024 bond-auction short  (example only)
- **Kind:** example (demo account, shown to his youngest son, not Caleb)
- **Sequence (diagrammable):**
  1. Narrative: the morning had no news, and the 1:00 PM bond auction was the driver. The NDOG was below, SSL sat at the day-session low and the London REL, and the morning REH were already engineered and run.
  2. 12:42: price rolls over, leaving an FVG and displacing lower.
  3. Price retraces into a SIBI, falls short of CE, and that candle becomes a bearish OB. He shorts **6 contracts at 18,321.25**.
  4. A big down-close candle is followed by an **immediate rebalance** (price trades back up into it). He adds **4 contracts at 18,291.25** (a pyramid). There is some heat on the add, but because the 6 larger contracts are at the better price, the combined position stays about **$1,700** in profit.
  5. The retrace goes up to an FVG level but **does not touch its CE** before the swing high. He **moves the stop to the first entry minus 2 ticks** and "just relaxes".
  6. **1:00 PM:** the auction candle pumps up (an up-close 1m candle) and then dumps. A small SIBI forms, and there is a slight **mohawk** overshoot of its boundary that doesn't take the high. The next retrace stops right at the FVG's edge: candle high **18,283.75** vs. FVG candle low **18,283.50**.
  7. After that retracement he points out a **2022 model** and an **OTE** on the chart.
  8. Price trades through the London lows. His **limit order just below the London low** fills. He takes off all **10 contracts** at about 18,2xx (caption "18,23…", unclear). That is **over 100 handles** on the 6-contract portion.
  9. Later in the session, price continues down and closes into the NDOG.
- **Lesson he draws:** 1-minute traders saw the 1:00 pump as a failure swing or iFVG going for the REH. They "lost the plot", because the draw was the London lows and the NDOG.
- **Timestamps:** [1:46:24](https://youtu.be/ZkLc4-adodg?t=6384) executions shown · [1:50:23](https://youtu.be/ZkLc4-adodg?t=6623) six-and-four, heat explained · [1:51:12](https://youtu.be/ZkLc4-adodg?t=6672) stop to entry minus 2 ticks; 1:00 pump and dump · [1:59:17](https://youtu.be/ZkLc4-adodg?t=7157) fills, over 100 handles

### Immediate rebalance & Mohawk  (example only / refinement)
- **Kind:** refinement (both referenced from Lecture 2)
- **What ICT says:** **Immediate rebalance:** after a big displacement candle, price trades right back up into it and then continues. He used it as the add-on area here. **Mohawk:** price overshoots an FVG boundary by a little ("coloring outside the lines"). It doesn't change the read as long as the swing high isn't taken. In a bearish narrative, judge how price treats **every SIBI** on the way down.
- **Timestamps:** [1:49:36](https://youtu.be/ZkLc4-adodg?t=6576) immediate rebalance · [1:52:01](https://youtu.be/ZkLc4-adodg?t=6721) mohawk, how price treats each SIBI

### Six-and-four position building / pyramiding  (aliases: "my model six and four")
- **Kind:** rule (trade management)
- **What ICT says:** He puts the larger piece (**6 contracts**) on at the best price and adds a smaller piece (**4 contracts**) later. The bigger, better-priced first entry absorbs heat on the add, so a retrace above the second entry can't put the whole position underwater. Building larger positions this way comes from years of experience, he says. How much you can take out of a run depends on how high in its range (premium vs equilibrium) you get in.
- **Timestamps:** [1:50:23](https://youtu.be/ZkLc4-adodg?t=6623) · [2:17:30](https://youtu.be/ZkLc4-adodg?t=8250) "how much you can yield" depends on where in the range you enter

### Holding trades longer / price-run sizes  (aliases: scout trade, intermediate-term run)
- **Kind:** rule + process
- **What ICT says:**
  - **Prerequisite:** you must first be able to consistently get **5 handles in ES or 10 handles in NQ**. Holding longer does not fix an inability to do that.
  - **NQ price-run grades:** under **50 handles** is a "scout" (small intraday). **50+** is an intermediate-term run (what he means by swinging intraday volatility). **100+** is a larger swing. He has no grades beyond that. Most of his content aims for roughly 20 pips / 25 handles / 50 handles.
  - **Rule of excess range:** to take 10 handles, the setup must offer **15–20**. To hold longer, there must be a draw outside your normal range, such as an NDOG/NWOG, that justifies more than a 1m chart's range.
  - **Graduation drill:** aim the trade at the near target (the short-term low or REL), take a partial or close there, then **tape-read the rest**. Screenshot and note every impulse or doubt ("I have doubts it drops here") and review it afterwards. This exposure desensitizes you to needing to be right. Use demo or tape-reading for the extended part until you trust it.
  - Holding for longer runs increases the chance of being stopped out prematurely, because early on every retracement feels like the bottom. Watching price gravitate to NDOG/NWOG over weeks and months is what builds that patience. You can't fast-track it.
- **Timestamps:** [1:10:58](https://youtu.be/ZkLc4-adodg?t=4258) 5 ES / 10 NQ prerequisite · [1:11:47](https://youtu.be/ZkLc4-adodg?t=4307) 50/100-handle grades · [1:25:26](https://youtu.be/ZkLc4-adodg?t=5126) 15–20 to get 10 · [1:40:48](https://youtu.be/ZkLc4-adodg?t=6048) partial + tape-read the rest + journal doubts

### Algorithmic reference points (why gaps repeat)  (IPDA framing)
- **Kind:** definition (narrative)
- **What ICT says:** The algorithm works like a recipe. It must refer back to old information: the **date, day of week, week of month, month, quarter, the price, and the time** it was trading there. Levels hold because of these time-and-price references, not because buyers or sellers ran out or because of how many times a level was hit. This is why gaps that filled weeks ago still matter.
- **Timestamps:** [0:49:17](https://youtu.be/ZkLc4-adodg?t=2957) why would it care about an old gap · [1:06:57](https://youtu.be/ZkLc4-adodg?t=4017) recipe and reference points

### 81 PD arrays; iFVG mention
- **Kind:** definition (claim)
- **What ICT says:** He has **81** specific PD arrays (not 84), and each one works as an entry, partial and take-profit mechanism. Counting inversions would technically double that. You need **only one**, plus the patience to wait for it inside a narrative. All of them appear every day on some timeframe. An **inversion FVG** is distinct from an FVG and is "one of the bangers". If you wait patiently for it, it gives excellent runners. No trend analysis, moving averages or daily chart were used today. He used only time of day, time and price, liquidity, and the calendar narrative.
- **Timestamps:** [0:10:59](https://youtu.be/ZkLc4-adodg?t=659) 81 PD arrays · [0:42:57](https://youtu.be/ZkLc4-adodg?t=2577) iFVG as a "banger" · [1:17:23](https://youtu.be/ZkLc4-adodg?t=4643) you only need one · [1:18:12](https://youtu.be/ZkLc4-adodg?t=4692) no trend analysis or daily chart

### Street money vs. smart money (sentiment)
- **Kind:** refinement (context)
- **What ICT says:** "Street money" means people who openly share their ideas online, or uninformed people suddenly interested in a market. His example is his wife asking about Bitcoin near $20k, after which he called the top. When the social-media herd is loudly bearish ("crash") against what these principles show, he leans the other way, because the odds favor the opposite side.
- **Timestamps:** [1:00:36](https://youtu.be/ZkLc4-adodg?t=3636) · [1:01:25](https://youtu.be/ZkLc4-adodg?t=3685)

## Rules, checklists & numbers stated
- Caleb's main window is **7:00–11:00 AM NY**, either starting at 7/8 or waiting for the **9:30** bell and using **9:00–11:00**.
- **Midnight NY** is the start of the "true day". The algorithm references liquidity and inefficiencies from midnight onward.
- At **7:00, 8:00 and 9:00**, use the following 30 minutes to anticipate a move against your direction first. Look for REH/REL or smooth price after 7:00.
- **NDOG:** index futures, every day except Friday, 4:59 PM close vs 6:00 PM first 1m open. Mark the high, low and CE (plus 0.25/0.75). It is dated for the next trading day. It is valid **5 trading days** (holidays add a day). Keep **5** on the chart.
- **NWOG:** Fri 5:00 PM close vs Sun 6:00 PM open. It is valid **5 weeks**. Keep **5**. It has more weight than an NDOG for swing trades.
- Gaps can still work **6–9 months** later. Old gaps matter when price is **within 150 handles** (his personal rule).
- **Clustering:** of the last 5 gaps, more above price means expect it to gravitate up, and more below means expect it to gravitate down. Treat this as a filter, not a hard rule.
- A gap/array touched only **once** is still "hot" and price will very likely revisit it.
- **Hierarchy of draws:** NDOG/NWOG and REH/REL rank above FVGs and other inefficiencies.
- **REL quality:** the right-side low must be higher than the previous low. REH is the mirror.
- **SIBI:** best shorts in the lower half, upper half left open. **BISI:** best longs in the upper half, lower half left open. An unfilled half that runs away is a breakaway gap, so expect range expansion.
- If the retrace **fails to touch CE**, short the bottom of that candle (bearish OB). If it **touches CE**, wait for a higher entry in the upper part, with the stop above the higher gap's CE.
- **No medium/high-impact morning news → trade the afternoon.** Typical morning releases are 8:30 (sometimes 10:00) and crude at 10:30.
- **Bond auction at 1:00 PM ET** (medium impact) is a clean afternoon catalyst **only** when there is no morning news.
- Afternoon: be at the charts by **1:30**. The sweet spot is usually **1:30–2:30**. Then the **2:00–3:00 Silver Bullet**, then the **3:00 hour to the close**.
- **Prerequisite** for holding: consistent **5 handles ES / 10 handles NQ**.
- **NQ run grades:** <50 handles is a scout, **50+** is intermediate, **100+** is a larger swing.
- To reliably take X handles, the setup must offer about 1.5–2X (10 → 15–20).
- **Six-and-four:** 6 contracts at the first, better entry and 4 on the add.
- After confirmation (a retrace fails at CE), **move the stop to first entry minus 2 ticks**.
- **81** PD arrays, and you need one.

## Process, risk & psychology
- **The first development stage** is being able to predict where the market will gravitate. That is not profitable trading, precise entries, tight stops or low-risk management. It comes first, and the hardest part is learning where price is going, not the entry. ([0:46:06](https://youtu.be/ZkLc4-adodg?t=2766), [1:16:35](https://youtu.be/ZkLc4-adodg?t=4595))
- **Observe and record:** relax, watch price and take screenshots even when price is near nothing important. You don't need to know what it will do right now. Repetition at the right times of day builds the read by default. ([0:15:45](https://youtu.be/ZkLc4-adodg?t=945), [0:13:23](https://youtu.be/ZkLc4-adodg?t=803))
- **Systematic entries + small risk + no overtrading** leads to potential profitability by default. Don't rename or "spray-paint" his rules into your own model. Don't embellish them; use them as given. ([0:59:49](https://youtu.be/ZkLc4-adodg?t=3589))
- **Process → practice → proficiency**, in that order. Your dopamine should come from following the rules, not from gambling. You can't shortcut the time it takes. ([1:15:47](https://youtu.be/ZkLc4-adodg?t=4547))
- **Losses:** treat them like the "dough repair kit" joke at Domino's: flatten it out and move on. If you anticipated instead of waiting, get out, wait for the real setup and re-enter. He has re-entered after stop-outs and reversed when offside. Every loss is the operator's fault ("I did it wrong"), which lets you release it. Don't turn losses or wins into a social-media conversation. ([1:31:01](https://youtu.be/ZkLc4-adodg?t=5461), [1:47:59](https://youtu.be/ZkLc4-adodg?t=6479), [2:11:09](https://youtu.be/ZkLc4-adodg?t=7869))
- **Don't copy live streamers or signal services.** He calls that "the epitome of weakness". Put that faith in yourself. ([1:13:22](https://youtu.be/ZkLc4-adodg?t=4402))
- **"Should have held longer" thinking is toxic.** You will miss big runs while learning. ([1:42:25](https://youtu.be/ZkLc4-adodg?t=6145))
- **Demo/paper trading is "your best friend"** while learning. There are no taxes or realized losses, and nobody grades you, so you can focus purely on price. Trading real money or funded accounts early adds toxic thinking right before you push the button. Being anxious at +$1,500 shows you haven't tape-read enough. Ask whether there's an actual reason to exit other than "I've never made this much". ([2:07:59](https://youtu.be/ZkLc4-adodg?t=7679), [2:08:46](https://youtu.be/ZkLc4-adodg?t=7726))
- **Your journal of past wins is your "counselor"** when a setup eventually fails in your hands. ([2:10:22](https://youtu.be/ZkLc4-adodg?t=7822))
- **Caleb's study plan:** in month 1, backtest and journal old data and pick out in hindsight what price did. He watches nothing live. In month 2, tape-read live during the streams while ICT calls things in advance. In month 3, learn to push the button and get over the fear of entering. ICT says he got the "just take lots of trades to desensitize" idea from Larry Williams. ([2:15:55](https://youtu.be/ZkLc4-adodg?t=8155), [2:16:43](https://youtu.be/ZkLc4-adodg?t=8203))
- He trades demo in front of students on purpose: "if it doesn't work here it won't work anywhere else". ([1:59:17](https://youtu.be/ZkLc4-adodg?t=7157))

## Glossary candidates
`NDOG` — New Day Opening Gap. In index futures, the range between the 4:59 PM ET close and the 6:00 PM ET reopen. It is dated to the next trading day and valid for 5 trading days.
`NWOG` — New Week Opening Gap. The range between Friday's 5:00 PM close and Sunday's 6:00 PM open. It is valid for 5 weeks and carries more weight for swings.
`Consequent encroachment (CE)` — the midpoint of a gap or inefficiency. ICT keeps it distinct from "equilibrium", which refers to a delivered trading range.
`Gap quadrants` — the 0.25 / 0.5 / 0.75 grades of an opening gap. Price reacts at them to the tick.
`True day` — the trading day counted from midnight NY local time, the algorithm's daily reference start.
`Sell-side / buy-side delivery` — one-directional price delivery through a range. This is different from sell-side/buy-side *liquidity*, which means resting stops.
`Engineering liquidity` — the market deliberately building relative equal highs/lows (smooth price) to run later. You can anticipate it from the larger draw (NDOG/NWOG).
`Black hole` — ICT's image for an NDOG/NWOG as the dominant gravitational draw on price.
`Breakaway gap` — an FVG whose far half is never filled before price runs. It signals fast delivery and range expansion.
`Immediate rebalance` — price trading straight back into a just-formed displacement candle before continuing.
`Mohawk` — a small overshoot of an FVG boundary ("coloring outside the lines") that doesn't invalidate it.
`Six and four` — ICT's position-building pattern: 6 contracts on the first entry and 4 on a pyramid add.
`Scout trade` — ICT's term for a small intraday run under 50 NQ handles. 50+ is intermediate and 100+ is a larger swing.
`Street money` — the herd and uninformed public sentiment, especially ideas aired openly online. It is the counterpart to smart money.
