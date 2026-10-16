# M22-002 — 2022 ICT Mentorship Episode 2
ID: tmeCWULSTHc · URL: https://www.youtube.com/watch?v=tmeCWULSTHc · Duration: 49:36
Content type: lecture (built around his own live NQ trade)
Teaching density: high

## Summary
The first real teaching episode, "elements to a trade setup". Using his live thinkorswim NQ executions, ICT walks top-down from the weekly candle (bias: will this week's candle expand higher or lower?) to the daily chart (where the liquidity and draw sit), the hourly and 15m (consolidation, relative equal highs, a sell-side "sucker" run first), then the 2m chart for the entry: buy stops run, a break in market structure lower, and a sell into the fair value gap created by the displacement. Target is taken by splitting the day's range at 50% (premium/discount) and aiming for the nearest sell stops/imbalance in discount ("low-hanging fruit"). This is the core skeleton of the 2022 mentorship model and the homework is to find and log these setups (handles available) in old intraday data.

## Concepts
### Weekly bias — "will the weekly candle expand higher or lower?"
- **Kind:** rule
- **What ICT says:** Before each new trading week (preferably on the weekend), decide whether the next weekly candle is more likely to go higher or lower. You are NOT trying to predict the weekly close; only which side the weekly range expands toward. This sets your initial bias for the week.
- **How to identify:** Look at the weekly chart and the prior weekly candle; consider where price is drawing (an old low/high not yet broken) plus context: seasonality, macro news (Fed rate hikes), earnings season, and the "underlying tone" seen on the daily chart.
- **How to use:** If expecting lower, look only for setups that sell (buy stops run first). The move may happen in the first half of the week or a single day; if you get your setup in that, "you're done" for the week.
- **Example in this video:** NQ March 2022 contract (TradingView symbol NQH2022), weekly chart: bearish expectation for reasons of seasonal tendency to decline at that time of year, Fed expected to raise rates, earnings-season volatility, and a heavy tone; drawing toward an unbroken old weekly/daily low expected to be targeted on Sunday's open into Monday.
- **Timestamps:** [0:12:22](https://youtu.be/tmeCWULSTHc?t=742) — read the next weekly candle before the week; [0:13:11](https://youtu.be/tmeCWULSTHc?t=791) — reasons: seasonality, Fed, earnings; [0:15:32](https://youtu.be/tmeCWULSTHc?t=932) — the weekly expansion may be one day; don't trade every session; [0:16:20](https://youtu.be/tmeCWULSTHc?t=980) — weekly candle sets the initial bias.
- **Nuance / caveats / changes:** He did not expect the whole range delivered in one week; what matters is the direction of expansion.

### Draw on liquidity (DOL)  (aliases ICT uses: "where it's drawing to", "paperclip and magnet")
- **Kind:** definition
- **What ICT says:** Price is like a paperclip; price levels and seasonality act like a magnet pulling it toward certain levels. Price draws to one of two things: stops (liquidity) or an imbalance. Above old highs = buy stops; below old lows = sell stops. Speed and magnitude of the move to a level is learned by experience ("a feel"), not transferable.
- **How to identify:** On the daily chart, mark swing highs/lows (where liquidity sits) and imbalances. Most of the draw on liquidity "is predominantly found on" the daily timeframe, so most analysis should be linked to it.
- **How to use:** Define the weekly direction, then use the daily chart to see where you are within the weekly range expansion and which short-term lows/highs (stops) are the next draw.
- **Example in this video:** NQ daily: in a weak market, each short-term low has sell stops beneath it; the old daily low is the larger objective.
- **Timestamps:** [0:14:45](https://youtu.be/tmeCWULSTHc?t=885) — paperclip/magnet analogy; [0:16:20](https://youtu.be/tmeCWULSTHc?t=980) — daily chart: swing highs/lows, draw on liquidity found mostly on daily; [0:17:08](https://youtu.be/tmeCWULSTHc?t=1028) — draws to stops or an imbalance.
- **Nuance / caveats / changes:** He explicitly says this is not auction theory and his boxes are not supply and demand.

### Buy-side / sell-side liquidity and the stop hunt before a big move  (aliases ICT uses: "buy stops", "sell stops", "sucker play", "engineered liquidity", "inducing shorts")
- **Kind:** rule
- **What ICT says:** Before any significant price move lower, always anticipate some measure of a stop hunt on buy stops / a short-term high taken out; when expecting higher prices, generally a short-term low and its sell stops get taken before a pronounced rally. Says this occurs almost daily. When buy stops are run, they become market orders flooding in, giving smart money (who want to sell high) willing buyers as counterparty.
- **How to identify:** Consolidation forming a short-term high and short-term low; relative equal highs (retail "resistance" with stops above); traders who were short trail stops just above the recent high.
- **How to use:** In a bearish week, wait for the run above the old high (buy stops), then look for the entry signature on lower timeframes. Do not sell simply because highs were taken.
- **Example in this video:** NQ hourly/15m, Friday (last day of the week): bearish all week, sell-off Thursday, overnight consolidation. Friday: price first trades down below the consolidation low (sell stops), inducing breakout shorts ("sucker play"), then runs up through relative equal highs/old highs (buy stops above where shorts trailed their stops). That run is the setup context.
- **Timestamps:** [0:20:19](https://youtu.be/tmeCWULSTHc?t=1219) — consolidation; sell stops taken first to induce shorts; [0:22:01](https://youtu.be/tmeCWULSTHc?t=1321) — buy stops as counterparty for smart money; note: anticipate a stop hunt before a significant move; [0:23:39](https://youtu.be/tmeCWULSTHc?t=1419) — relative equal highs, retail resistance; [0:25:18](https://youtu.be/tmeCWULSTHc?t=1518) — larger pool above in sync with downtrend.
- **Nuance / caveats / changes:** He says "algorithms" attack the buy-stop pool; he rejects the buying/selling pressure explanation in favor of liquidity.

### Relative equal highs/lows  (aliases ICT uses: "cleanly delivered", "relative equal highs")
- **Kind:** definition (applied)
- **What ICT says:** Two highs at basically the same level are seen by retail as resistance; textbooks say place a buy stop just above clear resistance when short. These levels hold briefly, but most of the time the market runs them before a meaningful move.
- **How to identify:** Two or more highs (or lows) at nearly the same price.
- **How to use:** Treat as an engineered liquidity pool and a likely target before the real move.
- **Example in this video:** NQ 15m Friday: high right before the drop matches an earlier high; price runs through them.
- **Timestamps:** [0:23:39](https://youtu.be/tmeCWULSTHc?t=1419); [0:24:29](https://youtu.be/tmeCWULSTHc?t=1469).
- **Nuance / caveats / changes:** none.

### Market Structure Shift / break in market structure  (aliases ICT uses: "break in market structure", "market structure break", "short-term low being broken")
- **Kind:** definition / rule
- **What ICT says:** After the buy stops are run, look for a short-term swing low to be broken. A swing low = a candle with a higher low on its left and a higher low on its right (three-candle swing low). A break below it is "key" and is the specific signature that tips the market's hand. Says it forms almost every day, many times per week, in one direction or the other.
- **How to identify:** On the lower timeframe (1–3m for indices), after the stop run, mark the short-term low that formed on the way up; wait for price to break below it.
- **How to use:** Only after the MSS do you look for the imbalance (FVG) to sell into.
- **Example in this video:** NQ 2m, Friday: after running the old/relative equal highs, price creates short-term lows then breaks below them with a large down candle.
- **Timestamps:** [0:27:43](https://youtu.be/tmeCWULSTHc?t=1663) — break in market structure; [0:28:31](https://youtu.be/tmeCWULSTHc?t=1711) — don't rush in after the high is taken, wait for the signature; [0:42:59](https://youtu.be/tmeCWULSTHc?t=2579) — swing low definition.
- **Nuance / caveats / changes:** He points to other YouTube lessons on market structure breaks.

### Fair Value Gap (FVG) / imbalance  (aliases ICT uses: "imbalance", "buy-side imbalance", "fair value gap")
- **Kind:** definition / entry model
- **What ICT says:** An imbalance is where one candle moves in one direction only and the candle before's high and candle after's low don't overlap (for an up candle); price only went one way there and nothing offset it, so it has to be "efficiently delivered" on the opposite side (the algorithm must deliver equal price in the other direction to book it). He introduced "fair value gap" in 2016. Mark the first candle's low and third candle's high (for a bearish gap) as the FVG.
- **How to identify:** Three candles; the middle candle's range is not overlapped by candle 1's wick and candle 3's wick. Bearish FVG: candle 1 low above candle 3 high.
- **How to use:** After the MSS, when price trades back up into the FVG, sell short. If you can't get it on that timeframe, drop to a lower one (e.g., from 3m to 1m, or from 5m to 1m) and find an FVG there. A bullish (buy-side) imbalance below in discount is also a target, because price wants to rebalance it.
- **Example in this video:** NQ 2m, Friday: the big displacement candle breaking the short-term low leaves an FVG between that candle sequence; the next candle opens, trades higher and stops right in the gap: sell entry. The downside target was a buy-side imbalance (one up candle, prior candle high vs next candle low) located just below the 50% of the day's range near old lows; price traded down into it and "completely closed" it with down-closing price.
- **Timestamps:** [0:17:56](https://youtu.be/tmeCWULSTHc?t=1076) — imbalance defined; [0:29:18](https://youtu.be/tmeCWULSTHc?t=1758) — price goes up into the area: sell; scale down timeframes; [0:30:04](https://youtu.be/tmeCWULSTHc?t=1804) — "fair value gap", introduced 2016; [0:38:04](https://youtu.be/tmeCWULSTHc?t=2284) — buy-side imbalance as target, closed in.
- **Nuance / caveats / changes:** He says 1m, 2m, 3m charts are best for finding imbalances in indices because HFT algorithms operate at timeframes up to about 3 minutes (often 15s/30s/45s/60s intervals).

### Displacement entry, stop placement, and chasing  (aliases ICT uses: "sell into the gap", "don't chase")
- **Kind:** rule
- **What ICT says:** Enter as price trades up into the FVG; it feels scary to sell while price is rising, but that is what you want (retail wants "confirmation" and comes in late). If price has started moving lower you can still get in near the FVG, but once a short-term low is taken out you are chasing; market orders there risk slippage and larger risk. Stop: above the swing high (the stop-run high) or above the FVG-forming candle's high, whichever fits your risk parameters. Alternative: a sell stop order in the gap candle to trip you in, with stop above that candle's high (may be too wide).
- **How to identify:** n/a.
- **How to use:** Use micros while learning: full contract leverage on NQ can "burn you" if price moves 100 points quickly.
- **Example in this video:** NQ 2m short "at 14,800" (he abbreviates "798"), covered at "675" (about 14,675) as price hit the top of the target imbalance range, about 120-130 handles.
- **Timestamps:** [0:32:26](https://youtu.be/tmeCWULSTHc?t=1946) — entry and stop options; [0:33:13](https://youtu.be/tmeCWULSTHc?t=1993) — can still get in near the area; [0:34:02](https://youtu.be/tmeCWULSTHc?t=2042) — chasing, slippage; sell when the candle is going up; [0:43:47](https://youtu.be/tmeCWULSTHc?t=2627) — sell stop entry alternative.
- **Nuance / caveats / changes:** none.

### Premium / discount / equilibrium (dealing range split at 50%)  (aliases ICT uses: "split the range", "50 level", "liquidity matrix")
- **Kind:** definition / rule
- **What ICT says:** Take the current range (low of day to high of day so far) and split it with a Fibonacci 50% level. Above 50% is a premium (expensive, "algorithmic stance"); below 50% is a discount. Markets can stay in premium a while. When short, check where you are in the range: selling an FVG in premium, the algorithm will seek discount; it reprices lower regardless of buyers (buyers get "squeezed"; "bear squeeze/bull squeeze" are excuses for not understanding the algorithm).
- **How to identify:** Fib from high to low (or low to high) of the day's range; 50% level.
- **How to use:** Sell in premium, target liquidity/imbalance in discount (below 50%) — sell stops below an old low and nearby imbalances.
- **Example in this video:** NQ 2m Friday: FVG short formed in the premium of the day's range; price drove below the 50% level, raided sell stops under a low and filled the buy-side imbalance there.
- **Timestamps:** [0:34:49](https://youtu.be/tmeCWULSTHc?t=2089) — liquidity matrix; range low/high of day; [0:35:36](https://youtu.be/tmeCWULSTHc?t=2136) — 50% Fib, premium vs discount; [0:36:26](https://youtu.be/tmeCWULSTHc?t=2186) — algorithm in a sell program reprices lower; [0:37:17](https://youtu.be/tmeCWULSTHc?t=2237) — sell stops below 50% as counterparty to cover.
- **Nuance / caveats / changes:** The day's range here is "low of the day and high of the day thus far".

### Targets: low-hanging fruit  (aliases ICT uses: "closest target", "opposing high or low")
- **Kind:** rule
- **What ICT says:** Aim for the closest target: an old low or an imbalance (when short). Don't get fancy targeting the lowest low; the market can deny it. Take the easiest target and let the market go further without you. When covering a short you need willing sellers at a low price — they sit with sell stops below lows.
- **How to identify:** Nearest old low / imbalance in discount.
- **How to use:** Exit at the first logical draw; he exited as price hit the top of the target imbalance.
- **Example in this video:** He held the old daily low as a bigger objective but didn't expect it that day, so he stopped trading after the first target; in hindsight wishes he had left a small runner.
- **Timestamps:** [0:38:54](https://youtu.be/tmeCWULSTHc?t=2334) — efficient delivery, didn't participate rest of day; [0:47:49](https://youtu.be/tmeCWULSTHc?t=2869) — low-hanging fruit.
- **Nuance / caveats / changes:** Accept leaving money on the table.

### Time window: 8:30–11:00 ET  (aliases ICT uses: "sweet little spot in the morning")
- **Kind:** rule
- **What ICT says:** He likes watching index futures around 8:30 AM to 11:00 AM New York time; usually there's a setup he can find in there.
- **How to identify:** n/a.
- **How to use:** Focus study/live watching on this window; if you can't watch live, use TradingView replay (limited: candles don't paint fully, can't practice entries).
- **Example in this video:** n/a (the trade was during the morning).
- **Timestamps:** [0:42:09](https://youtu.be/tmeCWULSTHc?t=2529).
- **Nuance / caveats / changes:** Killzones not yet formally introduced.

### Top-down timeframe sequence (this episode's version)
- **Kind:** rule
- **What ICT says:** Weekly (bias) → daily (liquidity/draw; transpose daily levels down) → hourly (week framed from Monday midnight NY to Friday) → 15m (stop run levels marked with short line segments) → 2m (1–3m) for MSS and FVG entry. Intraday = anything below daily (4H, 1H, 5m, 3m, 2m, 1m).
- **How to identify:** n/a.
- **How to use:** While developing, draw liquidity levels on your chart to keep your bearings; he himself watches a naked chart.
- **Example in this video:** The NQ walk-through above.
- **Timestamps:** [0:18:43](https://youtu.be/tmeCWULSTHc?t=1123) — hourly framework, week from Monday midnight NY; [0:22:51](https://youtu.be/tmeCWULSTHc?t=1371) — 15m line segments; draw levels while learning; [0:26:05](https://youtu.be/tmeCWULSTHc?t=1565) — why 2m chart.
- **Nuance / caveats / changes:** none.

## Rules, checklists & numbers stated
- Setup checklist (bearish; reverse for bullish): (1) weekly bias expecting lower; (2) a run above an old high / buy stops (opposing direction of weekly expectation); (3) a break in market structure on a lower timeframe (short-term low broken); (4) the imbalance/FVG left by that move is the trigger — sell when price trades up into it; (5) split the range at 50% and target an old low or imbalance in discount — the closest one.
- Before any significant move lower, anticipate a buy-stop raid; before a significant rally, a sell-stop raid.
- 1m/2m/3m charts best for index imbalances; HFT algorithms work at ≤3m intervals.
- Watching window: 8:30–11:00 AM New York time.
- NQ: $20 per handle; ES: $50 per handle ($12.50/tick, 4 ticks/handle). Margin for one full NQ contract is captioned as "$177,000" (caption unclear; likely about $17,700) and about $12,500 for one ES contract; micros need a fraction of that (smaller tick multiplier).
- His live NQ 1m executions that day (abbreviated prices): short ~740 → long ~720 (20 handles); long 720 → out 732 (12); long 756 → out 784.5; short 798 (~14,798) → cover 675 (~14,675). The last is the setup taught.
- Don't trade every session/day.
- Stop: above the stop-run swing high or above the FVG candle high.
- Homework: on e-mini (ES, NQ, YM) intraday charts, find MSS after a liquidity run against the weekly expected direction, mark the FVG, find the opposing high/low target, and log the number of handles available (backtest log).

## Process, risk & psychology
- Don't trade every session; expecting daily profits leads to the "loser cycle" after the first loss ([0:15:32](https://youtu.be/tmeCWULSTHc?t=932)).
- He doesn't hunt 3–5 handle scalps; focus on finding a nice intraday price leg ([0:10:45](https://youtu.be/tmeCWULSTHc?t=645), [0:11:34](https://youtu.be/tmeCWULSTHc?t=694)).
- Independence: no black box, no signal service; only the chart ([0:09:09](https://youtu.be/tmeCWULSTHc?t=549)).
- Weeks/months of backtesting required before acting; don't trade it the first time you see it ([0:30:51](https://youtu.be/tmeCWULSTHc?t=1851), [0:31:40](https://youtu.be/tmeCWULSTHc?t=1900)).
- Use micros; full-size leverage via discount brokers can burn you if you lack skill ([0:32:26](https://youtu.be/tmeCWULSTHc?t=1946), [0:33:13](https://youtu.be/tmeCWULSTHc?t=1993)).
- You'll never be right about everything (too early, held too long, size); don't beat yourself up ([0:39:41](https://youtu.be/tmeCWULSTHc?t=2381)).
- Study old moves; TradingView replay is the next best thing to live ([0:41:20](https://youtu.be/tmeCWULSTHc?t=2480)).
- Live executions shown on thinkorswim (green = live; orange = paper) ([0:44:35](https://youtu.be/tmeCWULSTHc?t=2675)).

## Glossary candidates
`Handle` — one full index point (4 ticks); NQ $20, ES $50.
`Imbalance` — one-directional price leg where adjacent candle wicks don't overlap; must be rebalanced by delivery in the opposite direction.
`Buy-side imbalance` — an FVG created by an up candle (later "BISI"); a downside target when bearish.
`Efficiently delivered` — when price has traded both directions through a range, balancing it.
`Sucker play` — an initial move that trips breakout traders into the wrong side before the real run.
`Low-hanging fruit` — the closest, easiest target.
`Premium / discount` — above / below 50% of the current range.
