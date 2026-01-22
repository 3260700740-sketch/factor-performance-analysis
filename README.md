# factor-performance-analysis

## Overview

This project studies the empirical behavior of common equity factors using historical data.  
Rather than focusing on trading strategies or return forecasting, the analysis aims to understand:

- How factor returns evolve over long horizons
- Whether factors exhibit stable cross-sectional predictive power
- To what extent factor behavior may be explained by industry exposure

The project is structured as a descriptive and diagnostic analysis of factor performance.

---

## Data

The analysis uses monthly Fama–French factor data obtained from the official Kenneth R. French data library.

- Frequency: Monthly
- Factors analyzed: Market (Mkt-RF), SMB, HML
- Sample start: 2000

All returns are converted from percentages to decimal form prior to analysis.

---

## Methodology

Three complementary analyses are conducted:

1. **Cumulative return analysis**  
   Monthly factor returns are compounded to visualize long-term performance paths and compared against a market benchmark.

2. **Information Coefficient (IC) analysis**  
   The predictive ability of a factor is measured using the Spearman rank correlation between factor values and future market returns.

3. **Sector exposure analysis**  
   Asset-level weights are aggregated by sector to examine whether factor behavior may be driven by structural industry tilts.

---

## Results

### Factor Cumulative Returns

The cumulative return curves illustrate substantial differences in long-term behavior across factors.

- The market benchmark exhibits strong long-term growth with pronounced drawdowns.
- SMB displays relatively flat cumulative performance over the sample period.
- HML shows strong early performance followed by extended periods of underperformance, indicating regime dependence.

These observations motivate further investigation into the stability of factor predictive power.

---

### Information Coefficient and IC Decay

Information Coefficients are computed for prediction horizons ranging from 1 to 12 months.

The results show that:
- The factor exhibits mildly positive IC values at very short horizons.
- Predictive strength fluctuates substantially across horizons.
- IC values tend to decay toward zero as the prediction horizon increases.

Overall, the factor’s predictive ability appears short-lived and time-varying rather than persistent.

---

### Sector Exposure

Sector-level aggregation of asset weights reveals a pronounced concentration in specific industries.

In the illustrative example:
- Information Technology accounts for the majority of exposure.
- Financials and Energy represent smaller but non-negligible components.

This suggests that part of the observed factor behavior may be attributable to underlying sector tilts rather than pure factor effects.

---

## Discussion

Taken together, the results indicate that:

- Long-term factor performance alone does not imply stable predictive power.
- Information Coefficient analysis provides additional insight into the temporal stability of factor signals.
- Sector exposure analysis highlights the importance of disentangling factor effects from structural industry biases.

These findings emphasize the need for caution when interpreting factor performance based solely on historical returns.

---

## Notes and Limitations

- The analysis is descriptive and does not constitute a trading strategy.
- Transaction costs, portfolio construction rules, and risk constraints are not considered.
- Sector exposure analysis is based on a simplified illustrative universe and can be extended to broader asset sets.