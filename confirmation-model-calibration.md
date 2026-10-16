# "Confirmation Model" calibration — The Creative Trader reel

**Date:** 2026-08-31 · **Harness:** `research/confirm/replay_confirm.py` · **Data:** XAUUSD.s (PU Prime)

## The model as stated in the reel

1. **Liquidity sweep** — price takes out a major high/low. No sweep, no trade.
2. **HTF FVG delivery** — 15M/1H delivering from a higher-TF fair value gap; body-closed-through ("chopped") gaps disqualify.
3. **LTF iFVG** — drop to the 1-minute; price displaces and closes through a FVG (inversion).
4. **CISD** — candle close above/below the opens of the last candle series that led into the sweep.

Entry = market on the confirming close. Stop = beyond the CISD candle series (incl. sweep wick).
Target = opposing liquidity. His own screen shows **RR 1.16**. Claim: "two red days in the past month."

## Replay implementation

- Major levels = PDH/PDL, PWH/PWL, Asia/London/NY session extremes, confirmed 1H swings.
- HTF gaps die on HTF body close through the far edge ("respected vs chopped"); delivery = tap within 2h.
- iFVG + CISD close within a 2h post-sweep window (4h "loose" variant = robustness check).
- Spread $0.27 charged both legs; ties inside a bar counted as losses (conservative);
  geometry invariants asserted (stop on losing side, target on winning side, risk ∈ [3 spreads, 5 ATR]).
- **Statistic:** P(target before stop) vs per-trade gambler's-ruin null 1/(1+k) → Poisson-binomial z.
  Non-overlapping primary series, side-split, select-2025 / verify-2026.

## Results (base windows, non-overlapping)

### M1 literal (his spec) — May 15 → Aug 26 2026, 108 trades

| | n | WR | null | z | pips/trade |
|---|---|---|---|---|---|
| All | 108 | 34.3% | 33.1% | **+0.28** | −5.5 |
| Buys | 61 | 29.5% | 33.2% | −0.66 | −12.8 |
| Sells | 47 | 40.4% | 32.9% | +1.16 | +4.0 |

Barrier grid (+0.5R/+1R/+1.16R/+2R): z = +1.02 / +0.19 / +0.19 / −0.41. **Dead on chance, negative after spread.**

### M5 proxy — Apr 2025 → Aug 2026, 456 trades

| | n | WR | null | z | pips/trade |
|---|---|---|---|---|---|
| 2025 all | 245 | 49.4% | 45.3% | +1.40 | +6.4 |
| 2026 all | 211 | 48.3% | 45.3% | +0.96 | +37.2 |
| Pooled | 456 | 48.9% | 45.3% | **+1.68** | +20.6 |

- No barrier rung clears |z| 1.5 pooled. The only z>2 cells are **2026 sells** (+2.26/+2.30 at 1.16R/2R)
  — the known 2026 sell-side regime (gold's Aug slide), mirrored by 2026 buys running *negative*
  (−1.79 at 0.5R). Sides flip between years (2025 buys were the good side) = beta, not model skill.
  Same pattern CWS1 showed; not adoptable.
- Loose windows: same picture (pooled z +1.80; M1 +0.12).

### The "two red days a month" claim

Honest daily accounting of the replay: **M1 literal = 9.8 red days/month (66% of trading days)**;
M5 = 7.9 red days/month (49%). Arithmetic makes his claim impossible at his own RR: at RR 1.16 the
chance win rate is 46.3%; even a real 55% winner has ~45% red days taking ~1 trade/day. "2 red
days/month" ≈ 90% green days — reachable only via partial-banking accounting (count any trade that
banked TP1 as green), not counting no-trade days, or selective memory. Same accounting we unmasked in
the ICC (90% claims = checkpoint banking) and TOP1 (81% = no-SL) audits.

## Verdict

**Not worth building a Pine script for edge.** The 4-confirmation stack measures at chance on the
literal M1 spec (z +0.28, negative expectancy after spread) and indistinguishable-from-chance on 17
months of M5 (z +1.68 pooled, nothing survives the barrier grid or the year split). This is the
**fifth** independent measurement of this confluence family in the repo (CWS1 S2, donnydropout
market-entry, Oliver 4-step, smc_alerts M1) and every one lands at chance — the finder is consistent.

If an alert tool is still wanted: CWS1 already implements sweep gate + 1H POI + iFVG trigger; the only
missing element is a CISD-close gate, a ~20-line toggle — cheaper than a new script, same expected edge (none).

Caveats: my proxy choices (level pool, 2h windows) are one reasonable reading of a 60-second reel;
M1 sample is 3.4 months (n=108, can't detect edges under ~10pts of WR); PU Prime feed.
