# Final Data Science Capstone – Drivers of High Income and a Fairness Audit

Yuva Intern – Task 6 (AI/ML Research Specialist Internship)

**Dataset:** UCI Adult (Census Income), 48,842 records from the 1994 US Census; target = income above $50,000.

**Problem:** Which factors are associated with high income, how strongly, can a model support group-level programme planning, and is that model fair enough to use?

## Contents
| File | Purpose |
|---|---|
| `Capstone_Income_Analysis.ipynb` | Full executed analysis: problem definition, data audit, feature engineering, statistics with context, models, limitations and fairness audit, visualisations, recommendations |
| `Capstone_Presentation.pptx` | 14-slide presentation |
| `data/adult_raw.csv`, `adult_clean.csv` | Raw and cleaned data |
| `data/metrics.json` | Every number quoted in the report and slides |
| `images/` | Charts incl. `00_dashboard.png` |
| `requirements.txt` | Libraries |

## Method
1. Data audit (52 duplicates, non-random missing values, top-coded fields) and feature engineering
2. Statistics with effect sizes: two-proportion z-test, chi-square with Holm correction and Cramer's V, Welch t-test and Mann-Whitney, logistic regression odds ratios, bootstrap intervals
3. Models: logistic regression, random forest, gradient boosting (tuned), threshold chosen from out-of-fold predictions
4. Model limitations: calibration, learning curve, subgroup performance, fairness metrics, proxy test, group-threshold trade-off, error analysis

## Headline results
- 23.9% earn above $50K; men 30.4% vs women 10.9% (gap 19.5 pp); observed factors account for ~86% of the log-odds gap, an adjusted odds ratio of 0.84 remains
- Each extra year of education: adjusted odds ratio 1.31
- Final model test ROC-AUC 0.928 (95% CI 0.922-0.932), PR-AUC 0.827, Brier 0.089, ECE 0.012
- Fairness audit: female/male selection ratio 0.29, recall gap 13.4 pp; sex can be predicted from the "unaware" features with AUC 0.936, so removing sex does not remove its influence

## Responsible use
The model is suitable only for aggregate planning, not for decisions about individuals. See Section 8 of the report for biases and limitations.

## Run
```bash
pip install -r requirements.txt
jupyter notebook Capstone_Income_Analysis.ipynb   # Kernel -> Restart & Run All (about 5 minutes)
```
Random seed 42 throughout.
