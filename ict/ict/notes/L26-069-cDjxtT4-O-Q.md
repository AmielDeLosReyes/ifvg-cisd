# L26-069 — Weekend US Holiday Volume Protocol
ID: cDjxtT4-O-Q · URL: https://www.youtube.com/watch?v=cDjxtT4-O-Q · Duration: 28:10
Content type: live trade (live NQ trade on the Monday after a weekend US holiday, with a closing lecture on why such days are trashy)
Teaching density: medium-high (a clear "stand aside on post-holiday Mondays" protocol plus a worked example of closing a failing short, reversing long, and the SIBI-fails-to-close-below-CE tell)

## Summary
On the Monday after a US holiday that fell on a Saturday (inferred to be the July 4 weekend, so Monday July 6, 2026; not stated), ICT warns that the day will be "trashy" with false signals because participation is light. He trades NQ (September 2026 contract, NQU2026) live: a first short from the CE of the first presented FVG/inversion FVG into the 10:00 news fails to follow through; he closes it, reverses long on a standard bullish FVG, targets an "event horizon" between a 15-minute FVG CE and an old high, takes partials, and ends with a small net gain after having had a larger initial loss. The lesson is the protocol: the day after a weekend holiday you should usually not trade at all; light volume means the algorithm does not need to deliver big ranges or precise levels, which also undermines the buying/selling-pressure idea.

## Concepts

### Holiday volume protocol (Monday after a weekend US holiday)  (aliases ICT uses: holiday volume, trashy conditions, failures to launch, false signals)
- **Kind:** rule (day-type filter)
- **What ICT says:**
  - The holiday fell on Saturday; "usually Mondays after that, it's very, very trashy. It means you're going to have a whole lot of false signals."
  - "I've lost more money trading after holidays like this than in any other thing. Always holiday volume."
  - Price is "lethargic," gives "failures to launch," is "ugly price action"; "technicals don't give you that real pristine precision."
  - Why: volume will be light - people are away (summer months, hungover, vacation); participation is thin so "there's no need for them to make the ranges big" and they "don't need to have the market to be that precise." He says "he [the algorithm/market maker] won't be able to engineer participation because there's a vacuum of interest."
  - It "slaps in the face the buying and selling pressure myth": a big range wouldn't be justified without participation.
  - Response: "knowing these things going in helps you preserve capital... not go on tilt... Enough is not trading at all on a day like today. That's the right answer."
  - He had posted on X before the open that people shouldn't trade live funds and to be careful, "these days can be rather fickle."
  - Contrast with low-resistance liquidity-run days where "price moves around really freely" and technicals are clean.
  - Rebuttal to foreign traders ("why does a US holiday matter?"): it's participation, not nationality.
- **How to identify:** the first trading day after a US market holiday (weekend or Friday/Monday holiday), summer especially; look for price repeatedly failing at levels, jagged moves on the upside, price stuck in the middle of a range.
- **How to use:** do not trade live money; if you trade, expect failures, use tiny size and fast protection of stops; watch rather than engage. Seek low-resistance days instead.
- **Example in this video:** NQ 15m/1m, morning: price middles in a 15-minute range, sharp upside jaggedness, failure to launch both ways; the 10:00 news only moves price a little.
- **Timestamps:** [0:00:47](https://youtu.be/cDjxtT4-O-Q?t=47) — holiday on Saturday, Mondays after are trashy, false signals; [0:05:55](https://youtu.be/cDjxtT4-O-Q?t=355) — "lost more money after holidays"; [0:21:04](https://youtu.be/cDjxtT4-O-Q?t=1264) — fickle, lethargic, failures to launch; [0:26:37](https://youtu.be/cDjxtT4-O-Q?t=1597) — participation explanation; [0:27:24](https://youtu.be/cDjxtT4-O-Q?t=1644) — enough is not trading at all
- **Nuance / caveats / changes:** Related to L26-064's Monday guidance (avoid unless NFP week) and the holiday-protocol theme in this series. The explanation overtly rejects "buying and selling pressure" logic.

### Wait for the 10:00 news before committing  (aliases ICT uses: 10:00 news, intel/bias)
- **Kind:** rule
- **What ICT says:** He had posted on X that he would look to the 10:00 news to give "a little bit more intel or bias." Before the news he would not short; "if the 10:00 news had already happened and this was 10:01, I would be shorting right there." He wants them to "use the news to send it lower and attack the sell side resting below today's intraday low." After 10:00, price took the low but did not touch the first significant FVG.
- **How to use:** hold off on direction until the scheduled 10:00 release; then trade the reaction toward the liquidity.
- **Timestamps:** [0:02:23](https://youtu.be/cDjxtT4-O-Q?t=143) — 10:00 news as intel; [0:04:17](https://youtu.be/cDjxtT4-O-Q?t=257) — wants news to attack sell side below intraday low; [0:05:04](https://youtu.be/cDjxtT4-O-Q?t=304) — low taken, didn't touch the first FVG
- **Nuance / caveats / changes:** Mirrors his approach in L26-062 (trade after the 10:00 speaker).

### First presented FVG as inversion FVG; stop above the candle that went through it  (aliases ICT uses: first presented fair value gap, inversion fair value gap, consequent encroachment)
- **Kind:** entry model
- **What ICT says:** The first presented FVG of the session (formed in the first 30 minutes) "is going to act as an inversion FVG" given what price has done; he watches the candlestick's halfway (CE) and, once the candle closes, uses the high of the candle that went completely through the iFVG as his risk; he wants price to take the sell side below today's intraday low. A small gap sits inside the iFVG; needs "a heaviness campaign to lower"; any more consolidation sends price up to the high. Stop is placed above that candle's high and later lowered to a nearby candle's high.
- **How to use:** short from the CE of the iFVG with the stop above the high of the candle that traded through; require heaviness quickly; otherwise get out.
- **Example in this video:** NQ 1m, ~9:55-10:05: short at the CE of the first presented FVG after the first 30 minutes; target intraday low sell-side; stop above the high of the candle that went through the gap.
- **Timestamps:** [0:03:12](https://youtu.be/cDjxtT4-O-Q?t=192) — first presented FVG acts as iFVG; [0:04:17](https://youtu.be/cDjxtT4-O-Q?t=257) — risk is the high of the candle that traded through; [0:06:51](https://youtu.be/cDjxtT4-O-Q?t=411) — needs to get heavy on this or the next candle
- **Nuance / caveats / changes:** Entry price and exact levels are not stated in the captions.

### Wick CE rule: a close below the wick's midpoint usually means the low will be revisited  (aliases ICT uses: consequent encroachment of a wick, protect the high, "tip off")
- **Kind:** rule / observation
- **What ICT says:**
  - Normal procedure: if a wick like that closes below its halfway point, it is more likely price comes back for the low (or the high that protected it).
  - Today (holiday volume) the sequence was: 9:30 open dropped, closed higher, then dropped without taking the low; price closed below the CE of a wick "usually" a clue, which "could be not true today because of the holiday volume."
  - The market could not even bump the old high; "they didn't have enough interest to send it there... buyers can't buy it to make it go higher, they can't short it to make it go lower." The level drawn on the 15m (the 30,011.25 level) was not reached.
  - Price was in the dead center of a 15-minute range, either side could be explored; i.e. low conviction.
- **Timestamps:** [0:08:29](https://youtu.be/cDjxtT4-O-Q?t=509) — middle of a 15-minute range, closing below the CE; [0:09:17](https://youtu.be/cDjxtT4-O-Q?t=557) — normal procedure vs holiday sloppiness; [0:10:04](https://youtu.be/cDjxtT4-O-Q?t=604) — couldn't bump the high, no interest
- **Nuance / caveats / changes:** Shows the rule is probabilistic and degrades in holiday conditions.

### SIBI that fails to close below its CE is not bearish: close the short and reverse long  (aliases ICT uses: initial utilization, standard bullish fair value gap, reclaimed, volume imbalance)
- **Kind:** entry model / rule
- **What ICT says:**
  - The sell-side imbalance buy-side inefficiency (with a volume imbalance) is usually bearish, "but look what it did: it failed to take out that low. It failed to trade and close below its consequent encroachment." He measures with a fib: price did not close below the halfway point, "indicating this is not going to be bearish."
  - So he bailed on the short ("protected the stop loss that would clearly have gotten a larger stop out"), "saved the stop loss, reversed," and treated the area as the initial utilization of a standard bullish FVG that was reclaimed after going below.
  - The long: stop one tick below the open of the key candle; target = event horizon between the 15-minute FVG's CE and the old high (the midpoint of those two reference points).
  - Rule for the retest: the long FVG/iFVG may be traded down into on a wick only, not leaving a body; if it wicks and the next candle opens above the range up to the candle's high, it should draw higher; stay in the upper half of the gap.
  - Partial plan: peel one off at the CE-ish level, another halfway between levels, run the balance.
- **How to identify:** a bearish gap (SIBI) that does not close below its own midpoint, and failed to take out the low.
- **How to use:** exit shorts; flip long into the next bullish FVG, stay long while price stays in the upper half; stop one tick under the open of the key candle.
- **Example in this video:** NQ 1m ~10:05-10:15: short from the iFVG CE; the SIBI fails to close below its CE; he closes (loss ~$1,800 per his words), reverses long; price makes a wick into the bullish FVG and closes above; first target hit, second partial.
- **Timestamps:** [0:11:42](https://youtu.be/cDjxtT4-O-Q?t=702) — closes the trade, reverses; [0:13:25](https://youtu.be/cDjxtT4-O-Q?t=805) — SIBI fails to close below its CE; [0:14:12](https://youtu.be/cDjxtT4-O-Q?t=852) — fib shows no close below the halfway point; [0:14:59](https://youtu.be/cDjxtT4-O-Q?t=899) — wick only, partial plan
- **Nuance / caveats / changes:** An explicit instance of "a gap that fails to reach/close beyond its CE flips the bias," as with the earlier iFVG CE failure notes (L26-002).

### Event horizon between a 15-minute FVG CE and an old high; confirmed at 30,037.5  (aliases ICT uses: event horizon, halfway point, grade the range with octants and quadrants)
- **Kind:** target / verification
- **What ICT says:**
  - Target for the long: the halfway between the CE of a 15-minute FVG he had shown on the 15m time frame and an old high. He drew it by hand; price struggled there ("see how reluctant it is to continue").
  - After the session he grades the 15m range (high to low) into octants and quadrants and zooms to the 1m: the loosely hand-drawn event horizon matched a level at 30,037.5 where the body stops and rolls over ("look at the precision"). He notes the halfway point to its low is the lower quadrant.
  - "Nobody else talks about that kind of stuff - Gann, Wyckoff, supply and demand."
- **Example in this video:** NQ 1m: price runs about 15 handles above the high of the session, stalls near the event horizon; body stops at 30,037.5; retraces.
- **Timestamps:** [0:12:28](https://youtu.be/cDjxtT4-O-Q?t=748) — event horizon target; [0:15:45](https://youtu.be/cDjxtT4-O-Q?t=945) — reluctance at the halfway point; [0:25:51](https://youtu.be/cDjxtT4-O-Q?t=1551) — precision of 30,037.5
- **Nuance / caveats / changes:** Event horizon used here as a target; in L26-002 it was an entry level.

### Management: limited room, lingering above a level, take two off, stop under wick low, final contract on the stop  (aliases ICT uses: peel risk off, runner, strangle with the stop loss)
- **Kind:** rule (trade management)
- **What ICT says:**
  - After taking the long: if price spends 1, 2, then a third minute just above the high without running ("three times we have spent 1 minute here, 2 minutes, more than a third minute above this high"), it needs to "find legs"; he takes two contracts off and rolls the stop under the wick low.
  - One contract remains (a runner); with one contract he can't scale so he manages with the stop and lets it be the "best case scenario exit"; rolls the stop below the wick as price gets above.
  - "If I'm stopped out, it's fine. The loss I had on the initial position is completely mitigated already." He cites an initial loss of about $1,800, then +$220, then another +$1,000 (caption figures).
  - Warning signs: too much wanting to fold and roll over above a high.
- **How to use:** protect the remaining position by rolling stops under the latest wick low; take partials when price stalls; the final contract managed by the stop.
- **Timestamps:** [0:15:45](https://youtu.be/cDjxtT4-O-Q?t=945) — peel some risk off; [0:17:41](https://youtu.be/cDjxtT4-O-Q?t=1061) — three minutes above the high, take two off; [0:19:30](https://youtu.be/cDjxtT4-O-Q?t=1170) — last contract on the stop; [0:24:12](https://youtu.be/cDjxtT4-O-Q?t=1452) — loss mitigated, P&L recap
- **Nuance / caveats / changes:** Same family as L26-062 (don't strangle, but here he strangles with the stop out of necessity).

### Index coupling across NQ, ES, YM as confirmation  (aliases ICT uses: coupling between the three averages, continuous contract vs delivery month)
- **Kind:** refinement
- **What ICT says:** He checks Dow, ES, and NQ: the Dow "is falling out of bed," ES mixed, NQ chopping. "If they were all moving higher it's a no-brainer" that the bullish FVG sends prices higher. He also notes that the front chart is the continuous contract and he switches to the September 2026 delivery contracts (NQU2026, ESU2026, YMU2026) for analysis.
- **How to use:** require the three indexes to agree before trusting a gap to deliver (a mild SMT-style check).
- **Timestamps:** [0:00:00](https://youtu.be/cDjxtT4-O-Q?t=0) — quick pass through Dow/ES/NQ and contract month; [0:01:35](https://youtu.be/cDjxtT4-O-Q?t=95) — coupling between the three averages
- **Nuance / caveats / changes:** Informal; no divergence-vs-correlation rule specified.

## Rules, checklists & numbers stated
- After a weekend US holiday: expect trashy, false-signal price action; the right answer is often not to trade at all; do not trade live funds.
- Wait for the 10:00 news before committing; after the news, trade the reaction.
- If a SIBI does not close below its CE (and fails to take the low), it is not bearish - exit shorts; flip to the bullish FVG.
- Retest of a bullish FVG: wick only, no body inside; the next candle should open in the upper range.
- Stop for the long one tick below the open of the key candle; partials: one at the CE-ish level, one at half between levels; runner on the stop.
- Candle lingering above a level for 3 minutes without running: reduce.
- Levels (captions): old high drawn ~30,011.25; event horizon precision at 30,037.5; run about 15 handles above the session high.
- Contract: NQU2026 (Sept 2026), ES/YM September contracts.
- Dollar P&L (captions): initial loss ~$1,800; mitigated; +$220; +$1,000.

## Process, risk & psychology
- Preserve capital and avoid tilt: skipping a bad-condition day is the right trade ([0:27:24](https://youtu.be/cDjxtT4-O-Q?t=1644)).
- Admit when you may be wrong and exit: "I know I'm possibly wrong, so I'm going to close the trade, save the stop loss, reverse" ([0:11:42](https://youtu.be/cDjxtT4-O-Q?t=702)).
- Show losses honestly: trading in crummy conditions is a good scenario to show a failure; people asked "show us where it doesn't work" ([0:23:24](https://youtu.be/cDjxtT4-O-Q?t=1404)).
- A loss on the initial position was mitigated by the reversal; you can fix a bad entry by acting quickly ([0:21:51](https://youtu.be/cDjxtT4-O-Q?t=1311)).
- "You generally don't want to be taking any trades on a day like today" ([0:13:25](https://youtu.be/cDjxtT4-O-Q?t=805)).
- Platform/execution delays on a paper-trading platform are a risk to evaluate before going live ([0:07:38](https://youtu.be/cDjxtT4-O-Q?t=458)).

## Glossary candidates
`HOLIDAY VOLUME` — thin participation after a holiday producing trashy, false-signal price action.
`FAILURE TO LAUNCH` — a level/array that doesn't produce the expected follow-through quickly.
`INITIAL UTILIZATION` — the first (original) use of a gap, e.g. a bullish FVG's original bullish role.
`RUNNER` — the last contract left on after partials, managed with the stop.
`LOW-RESISTANCE LIQUIDITY RUN` — a clean day where price moves freely to a draw (contrast with holiday days).
