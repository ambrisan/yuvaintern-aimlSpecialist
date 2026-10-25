# Data Science Tool Mastery Project – Diamond Price Analysis & Prediction

Yuva Intern – Task 4 (AI/ML Research Specialist Internship)

A portfolio project that demonstrates the core data-science toolkit on a **53,940-row real-world dataset** (diamonds, seaborn-data repository).

| Tool | Demonstrated |
|---|---|
| NumPy | Vectorisation benchmark (~40x faster than a loop), broadcasting, masks, least squares from scratch |
| Pandas | Cleaning, ordered categoricals, groupby, pivot, merge, transform, qcut, melt |
| SQL (SQLite) | Aggregation, HAVING, CTE, window functions, verified against Pandas |
| SciPy / Statsmodels | Normality, Pearson/Spearman, CI, bootstrap, Welch t-test, ANOVA + Tukey, chi-square, Bayes, OLS |
| Matplotlib / Seaborn | 10 charts |
| Scikit-learn | Pipelines, 5 models, 5-fold CV, GridSearchCV, permutation importance, error analysis |

## Files
- `Data_Science_Tool_Mastery.ipynb` – full executed notebook
- `data/` – raw and cleaned data, `metrics.json` (every key number)
- `images/` – saved charts
- `requirements.txt`

## Highlights
- 53,940 rows -> 53,772 after removing 146 duplicates and 22 impossible stones
- Confounding example: raw mean price Ideal $3,462 < Fair $4,341 because Fair stones are heavier (1.04 vs 0.70 carat); controlling for weight, colour and clarity, Ideal is ~17.6% more expensive
- Cut explains 1.8% of log-price variance; carat bands explain 87%
- Gradient boosting: test RMSE ~$525, R2 0.982, 79.6% of stones predicted within 10%

## Run
```bash
pip install -r requirements.txt
jupyter notebook Data_Science_Tool_Mastery.ipynb   # Kernel -> Restart & Run All
```
Random seed 42 is used throughout. Runtime is a few minutes.
