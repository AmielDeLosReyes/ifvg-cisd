# M22-041 — 2022 ICT Mentorship Episode 41 & Final
ID: 2XhDi5GoNUI · URL: https://www.youtube.com/watch?v=2XhDi5GoNUI · Duration: 50:08
Content type: mixed (ES review + final lecture on risk management, drawdown control, and stop management)
Teaching density: high

## Summary
This is the final lesson of the 2022 mentorship model. ICT reviews ES (Sept 2022) on 23 June 2022, a day with Fed Chair Powell speaking at 10:00 AM. His morning target of 3805 failed; a long was stopped out at +2 points. He explains why he then stood aside: an FVG that formed without displacement below the low was not a valid short, and he would not hold anything new into lunch. The lunch-hour stop run made the session low at about 1:00 PM. The 1:30 PM setup was a 15m FVG plus order block plus OTE, which he calls the "gold standard" of the channel's pattern, and it ran to 3805. He then completes the model with static rules:
- position sizing from a 1% risk on $10,000 (ES vs micro);
- R-multiples and compounding (1% a day is about 22% a month);
- a two-order version for 2% risk;
- drawdown control by halving risk after each loss (1%, then 0.5%, then 0.25%), earning back 50% of the loss before returning to full size;
- mandatory hard stops;
- a systematic stop-trailing rule: trim the stop 25% at 50% of the target range, and breakeven at 75%.

## Concepts

### Failed expectation around a news event: when to walk away
- **Kind:** rule / example
- **What ICT says:**
  - When a high-impact event (here Fed Chair Powell at 10:00) does not pan out as expected, in his experience it is better to step away, close the computer, and come back later. He then looks at the lunch hour and the post-lunch 1:30 window.
  - The NY index AM session (killzone) is 8:30–11:00. He can trade after 11, but he sticks to the rules to show that following them sometimes means missing opportunities, "and it's fine".
  - Being wrong publicly costs nothing when risk is controlled.
- **Example in this video:** ES 1h, 23 June 2022. SSL was taken, then a rally to BSL. His target was 3805, above an old high to the left. If it had hit, he would have watched for a short there. Price went just above a short-term high, "gave up the ghost", and went lower. His long was stopped out at +2 points ("just covering expenses").
- **Timestamps:** [0:01:41](https://youtu.be/2XhDi5GoNUI?t=101) — 3805 target, stopped out +2; [0:03:16](https://youtu.be/2XhDi5GoNUI?t=196) — AM session 8:30–11, sticking to rules; [0:04:50](https://youtu.be/2XhDi5GoNUI?t=290) — walk away after a failed news-driven expectation.

### No displacement, no valid FVG
- **Kind:** rule
- **What ICT says:**
  - After his long was stopped out, price dropped back down but did not take out the short-term low with displacement. So the FVG that formed was "not one that I would have taken". It was not an FVG he would participate in, because there was no meaningful move below that low.
  - Had a candle displaced below the low and then retraced up into the FVG, he "may have" shorted, aimed for that low, and closed it at noon if not reached.
- **Example in this video:** ES 5m and 2m in the morning. He went long from a 2-minute FVG, and the BSL above was taken with a bold bullish candle. Price came back for a complete closure of the FVG, rallied away, then dropped again and stopped him out, because he had rolled his stop up rather than weather a deeper retracement. The subsequent drop lacked displacement through the short-term low, so he stood aside.
- **Timestamps:** [0:09:36](https://youtu.be/2XhDi5GoNUI?t=576) — 2-minute FVG long toward 3805; [0:11:12](https://youtu.be/2XhDi5GoNUI?t=672) — stopped out after rolling stop; complete closure of the FVG; [0:11:59](https://youtu.be/2XhDi5GoNUI?t=719) — FVG without displacement, not taken.

### Price overrunning a smaller FVG to reach a larger one
- **Kind:** refinement / example
- **What ICT says:** Price ran over a smaller 15m FVG because a larger one sat beneath it. The top of a candle marked the low end of one gap and also the high end of the other, so price was likely to go over the top of the smaller FVG and run into the larger one.
- **Example in this video:** ES 15m. After running BSL, price drew down, took SSL, and overran the smaller FVG into the larger 15m FVG. Going into the noon lunch hour until 1:00, it made the session low after closing in that FVG.
- **Timestamps:** [0:05:37](https://youtu.be/2XhDi5GoNUI?t=337) — overrunning one FVG into the larger one.

### NY lunch: don't initiate into lunch; prefer the lunch stop run; wait for 1:30
- **Kind:** rule
- **What ICT says:**
  - Once price broke lower going into lunch, he did not want to short, because it might consolidate and "take forever". He does not hold anything new into lunch.
  - He prefers to see a stop run during the lunch hour. Here price ran below the lows into an FVG in a deep discount (of the low–high range) during lunch, and made the session low at about 1:00 when lunch ended.
  - The NY index PM session is 1:30–4:00 PM NY. He likes to wait until 1:30 because the price action is cleaner.
- **Timestamps:** [0:06:23](https://youtu.be/2XhDi5GoNUI?t=383) — 1:30–4:00 PM session; [0:07:10](https://youtu.be/2XhDi5GoNUI?t=430) — no new trades into lunch; prefer the lunch stop run; [0:07:59](https://youtu.be/2XhDi5GoNUI?t=479) — wait until 1:30, cleaner price action.

### "Gold standard" ICT pattern: FVG + order block + OTE after an MSS
- **Kind:** entry model
- **What ICT says:** A fair value gap with an order block at optimal trade entry is "the gold standard" and the flagship pattern of the channel. His checklist:
  1. Price traded down into an HTF FVG (15m) and shows willingness to go higher.
  2. A short-term market structure shift.
  3. A gap (FVG).
  4. A down-closed candle (bullish order block) to the left of it.
  5. The retrace into the OB lies at the OTE: the 62–79% retracement (caption says "62 to 70"), below equilibrium of the swing.
- **How to use:** Place a buy limit order. Stop under the swing low. First target is the first "low-hanging fruit": the nearest imbalance or premium level. Further targets are the BSL pools above.
- **Example in this video:** ES 2m and 5m PM session. Price hit the low in the 1:00 hour and rallied, giving a short-term MSS. At about 1:30 it traded back down into the last down-closed candle (OB), inside a 15m FVG (caption says "50 minute"), at OTE. It then ran to the short-term high, then through an FVG and up to 3805. Hypothetical demo entry: limit buy at 3754.75 (he says a quarter point below a candle's low). Stop 3745.75 (the swing low), which is 9 points of risk. First target 3780.25, the high of the imbalance candle in the premium of the high–low range. That is 25.5 points, better than 2.5R.
- **Timestamps:** [0:15:55](https://youtu.be/2XhDi5GoNUI?t=955) — 1:30 MSS, OB, 15m FVG, OTE = gold standard; [0:16:44](https://youtu.be/2XhDi5GoNUI?t=1004) — targets: imbalance, BSL, 3805; [0:18:18](https://youtu.be/2XhDi5GoNUI?t=1098) — checklist, limit 3754.75; [0:19:06](https://youtu.be/2XhDi5GoNUI?t=1146) — stop 3745.75 (9 pts); target 3780.25 (25.5 pts).
- **Nuance / caveats / changes:** He traded this PM long live and shows the account briefly (a "1 975" figure; caption unclear).

### Position sizing (risk per trade) — worked example
- **Kind:** rule
- **What ICT says:**
  - Use free lot-size calculators (search for them): enter account size, risk %, and stop size.
  - Worked example:
    1. $10,000 account at 1% risk means $100.
    2. Stop is 9 points, so $100 / 9 is about $11 per point.
    3. One ES mini is $50/point, which is too big, so you cannot trade a mini at 1%.
    4. One micro (MES) is $5/point. $11 / $5 means 2 micros ($10/point).
    5. Actual risk: 9 × $10 = $90, which is under 1%.
    6. Target 25.5 points × $10 = $255. He calls this "basically 2¼%" (the arithmetic gives 2.55%).
  - He does not factor commissions, fees, or spread into the sizing. "Costs are like taxes, you just eat it." Beginners who want to be strict about risk can include them.
- **Timestamps:** [0:20:43](https://youtu.be/2XhDi5GoNUI?t=1243) — lot-size calculators; [0:22:18](https://youtu.be/2XhDi5GoNUI?t=1338) — $10k × 1% = $100, 9-point stop; [0:23:08](https://youtu.be/2XhDi5GoNUI?t=1388) — mini too big, micros; [0:24:46](https://youtu.be/2XhDi5GoNUI?t=1486) — no commissions in math; $90 risk, $255 target.

### Compounding and realistic return targets
- **Kind:** rule / numbers
- **What ICT says:**
  - 1% a day, Monday–Friday, over about four weeks compounds to about 22% a month, not 20%.
  - Fund managers consider 12–15% a year stellar and 20%+ a blockbuster year.
  - 1% every single day is unrealistic for a new trader. For a seasoned trader, a 1% average per day is "really easy". It is an average: one 5% trade in a week equals 1% a day for that week.
  - He does not sit at the charts every day for 1%.
  - With 2% risk you can use two orders on the same setup: order 1 at the same limit and stop, targeting 3780.25 (about +2.25%); order 2 targeting the short-term high or 3805.50 (about +4.5% more). That is about 6.75% in one day from one trade idea.
- **Timestamps:** [0:26:21](https://youtu.be/2XhDi5GoNUI?t=1581) — 1% a day compounds to 22% a month; [0:27:55](https://youtu.be/2XhDi5GoNUI?t=1675) — 1% average; one 5% trade a week; [0:28:43](https://youtu.be/2XhDi5GoNUI?t=1723) — two orders for 2% risk, 3805.50 target; [0:29:33](https://youtu.be/2XhDi5GoNUI?t=1773) — about 6.75% in a day.

### Funded account challenges
- **Kind:** rule
- **What ICT says:**
  - If you lack capital, learn the skill set and use funded-account challenges or partners: "it doesn't have to be your money."
  - Their 10%-type targets are achievable if you know what you are doing and can handle drawdown.
  - Once funded, trade soberly: aim for 10–15% a month after the split, then stop. Do not try to get rich quickly.
- **Timestamps:** [0:30:20](https://youtu.be/2XhDi5GoNUI?t=1820) — funded challenges, drawdown; [0:32:42](https://youtu.be/2XhDi5GoNUI?t=1962) — small accounts, other people's money; [0:33:29](https://youtu.be/2XhDi5GoNUI?t=2009) — 10–15% a month after split.

### Drawdown control: halve risk after each loss
- **Kind:** rule
- **What ICT says:**
  - After a loss at 1% risk, the next trade risks 0.5%. Reasons: emotions, revenge, the urge to over-leverage, and impatience (the "loser's cycle, gambler's mentality").
  - You must make back 50% of what you lost before returning to full 1% risk. For example, lose about $100 (with commission), then earn $50 back.
  - If the 0.5% trade also loses, the next is 0.25%, the lowest you go.
  - Three straight losses then total only 1.75% drawdown (1 + 0.5 + 0.25). Compare doubling up: 1% then 2% is already 3%, and spiralling to 3–4% risk, removing or widening stops, leads easily to 10% drawdown and shame.
  - Same logic at 2% risk: after a full 2% loss, the next trade can risk only 1%. For example, 4 micros ($20/point) at 2% become 2 micros at 1% on the same 9-point stop.
  - Stops are not static. This trade needed 9 points, while others may need 5, 10, or 12. Recalculate size each time. Deep drawdown can leave you unable to trade even one micro.
- **Timestamps:** [0:31:07](https://youtu.be/2XhDi5GoNUI?t=1867) — after a loss risk half; [0:31:54](https://youtu.be/2XhDi5GoNUI?t=1914) — make back 50%, then 0.25% floor; [0:34:17](https://youtu.be/2XhDi5GoNUI?t=2057) — 1.75% vs doubling-up spiral; [0:41:25](https://youtu.be/2XhDi5GoNUI?t=2485) — 2% loss means the next is 1% (4 micros to 2).
- **Nuance / caveats / changes:** Professionals "are not allowed to touch their account when they're highly charged or emotional." Risk management is a psychological game as well as numbers.

### Hard stop is mandatory
- **Kind:** rule
- **What ICT says:**
  - If you do not put in a hard stop, you are not respecting the risk. You are saying "I'll figure out where I'm wrong when it gets there."
  - "I don't really use a hard stop but I know when I want to get out" tells him that trader does not have it together.
  - With this model the stop location is defined, so the hard stop must be placed, period. If it gets hit, it has done you a favor. Then your job is to manage the next trade with less risk to come out of drawdown incrementally.
  - Focus on whether price keeps showing the expected institutional order flow, not on fear of the stop being tripped. "You pay it well" to do its job.
- **Timestamps:** [0:14:21](https://youtu.be/2XhDi5GoNUI?t=861) — stop does its job; watch order flow instead; [0:15:08](https://youtu.be/2XhDi5GoNUI?t=908) — no hard stop means not respecting risk; [0:40:34](https://youtu.be/2XhDi5GoNUI?t=2434) — "I know when I want to get out" criticised; hard stop period.

### Systematic stop management (25% at 50% of the target range; breakeven at 75%)
- **Kind:** rule
- **What ICT says:**
  - Define the expected range from entry to target. Example: 3754.75 to 3780.25, 25.5 points.
  - When price has moved 50% of that range in your favor (about 12.75, rounded to 12.5 points), the stop can be moved up by 25% of the stop-to-entry distance, trimming risk a little. This is not jamming it to breakeven. (Caption is ambiguous between "trim by 25%" and "to 25%"; he describes it as "moving a little bit".)
  - When price has moved 75% of the entry-to-target range, move the stop to breakeven, "period".
  - Meanwhile, judge whether you are still on the right side:
    - Is price still reaching for the objective?
    - Do down-closed candles keep supporting price?
    - Does it run short-term lows (sell stops) and rally with energy?
    - Does it drop into FVGs, re-accumulate, and send another leg higher?
    
    If those hold, together or individually, keep holding for the target.
  - For multiple positions at "competition level leverage" (3%–4.5% risk), use a static partial rule, for example always take something off at +15 or +20 points.
  - These are foundations, not ironclad rules. Adapt them to your personality and model.
- **Timestamps:** [0:45:21](https://youtu.be/2XhDi5GoNUI?t=2721) — stop management: define entry-to-target range; [0:46:10](https://youtu.be/2XhDi5GoNUI?t=2770) — at 50% of range, trim stop 25%; [0:46:57](https://youtu.be/2XhDi5GoNUI?t=2817) — at 75%, breakeven; what to watch; [0:47:46](https://youtu.be/2XhDi5GoNUI?t=2866) — competition leverage 3–4.5%, static partials at 15–20 points.
- **Nuance / caveats / changes:** He says that in many shown trades he takes partials without rushing his stop up. This rule is meant to build trust in partials and reduce fear of being stopped out.

## Rules, checklists & numbers stated
- NY index AM session: 8:30–11:00 AM. NY lunch: 12:00–1:00 PM. NY index PM session: 1:30–4:00 PM (he prefers to start at 1:30).
- Do not initiate new trades into lunch. Look for the lunch-hour stop run instead.
- After a failed high-impact-news expectation, walk away and reassess at lunch or 1:30.
- An FVG without displacement through the short-term low is not a valid entry.
- Gold-standard entry: MSS, then FVG, then down-closed candle (OB), then OTE (62–79%, below equilibrium), inside an HTF (15m) FVG.
- Example trade: limit 3754.75, stop 3745.75 (9 pts), target 1 at 3780.25 (25.5 pts, better than 2.5R), target 2 at 3805.50.
- Sizing: risk $ = equity × risk %. Per-point value = risk $ / stop points. Divide by contract multiplier (ES $50/pt, MES $5/pt).
- $10k at 1% with a 9-point stop gives 2 MES ($90 risk). At 2% it gives 4 MES ($20/pt).
- 1% a day compounds to about 22% a month. Fund managers' 12–15% a year is stellar.
- Funded accounts: target 10–15% a month after the split, then stop.
- After a loss: next risk is half (1%, then 0.5%, then 0.25% floor). Recover 50% of the loss before returning to full risk. After a 2% loss, the next is 1%.
- Stop trail: at 50% of the entry-to-target distance, trim the stop by 25%. At 75%, move to breakeven.
- Competition-level leverage: 3–4.5% risk. Take a static partial (for example +15/+20 points).
- Learning timeline: in 6 months you will see things you never saw; by 1 year "you'll have it".

## Process, risk & psychology
- Being wrong publicly is fine: "wrong isn't going to ruin me". Use demo, not live, when following his Twitter commentary. ([0:11:12](https://youtu.be/2XhDi5GoNUI?t=672), [0:12:46](https://youtu.be/2XhDi5GoNUI?t=766))
- Revenge trading and doubling up after a loss is "infantile". A loss is like a toy taken away that you want back right away. ([0:35:51](https://youtu.be/2XhDi5GoNUI?t=2151))
- Treat drawdown like a bank loan you will collect interest on. Take a long-term view: your career is not your last 5 trades, weeks, or months. ([0:36:38](https://youtu.be/2XhDi5GoNUI?t=2198), [0:37:26](https://youtu.be/2XhDi5GoNUI?t=2246))
- Losing trades are a "tax on success" that every speculator pays (the "ferryman" metaphor). You control how bad it is by doing the math and sticking to it. ([0:39:46](https://youtu.be/2XhDi5GoNUI?t=2386), [0:44:33](https://youtu.be/2XhDi5GoNUI?t=2673))
- Do not escalate risk after an easy win (3% risk at 5R, "every session plus London", "quit my job next Sunday"). Use low-threshold objectives and work up. Longevity and impeccable risk management are what make you consistently profitable. ([0:43:46](https://youtu.be/2XhDi5GoNUI?t=2626))
- People who announce they are quitting are usually asking for encouragement. Real quitters just disappear. ([0:38:12](https://youtu.be/2XhDi5GoNUI?t=2292))
- You will not trade every day or know the bias every day, and you will have losers. Mastery means having faith that the model repeats more often than it fails. Test that claim yourself. ([0:49:23](https://youtu.be/2XhDi5GoNUI?t=2963))
- Answer basic questions (lot size and similar) yourself with free tools. Do the legwork. ([0:20:43](https://youtu.be/2XhDi5GoNUI?t=1243))

## Glossary candidates
`Gold standard (ICT pattern)` — an FVG plus an order block at OTE after an MSS, the flagship entry of the 2022 YouTube model.
`Competition level leverage` — ICT's term for 3–4.5% risk per trade, used with static partials.
`Tax on success` — ICT's framing of losing trades as an unavoidable cost of trading.
`Drawdown as a loan` — viewing equity drawdown as money lent to the market that will be repaid "with interest" over time.
`Low-hanging fruit objective` — the first, nearest target (for example the nearest imbalance or premium level), used for the first exit or R calculation.
`NY index PM session` — 1:30–4:00 PM ET for index futures.
