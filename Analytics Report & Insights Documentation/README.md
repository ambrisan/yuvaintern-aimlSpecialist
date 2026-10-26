# Analytics Report & Insights – Customer Churn at a Telecom Provider

Yuva Intern – Task 5 (AI/ML Research Specialist Internship)

**Dataset:** IBM Telco Customer Churn sample dataset (7,043 customers, 21 columns). It is a simulated sample dataset, so results illustrate the method rather than a real company.

**Business question:** Who churns, why, what does it cost, and what should be done?

## Contents
| File | Purpose |
|---|---|
| `Analytics_Report_Insights.ipynb` | Full executed analysis: objectives, KPIs, segments, 8 statistical tests, regression, risk model, dashboard, insights, recommendations |
| `data/telco_raw.csv`, `telco_clean.csv` | Raw and cleaned data |
| `data/metrics.json` | Every number quoted in the report |
| `images/` | Charts incl. `00_dashboard.png` (executive dashboard) |
| `requirements.txt` | Libraries |

## Headline results
- Churn rate 26.5% (1,869 of 7,043); MRR lost $139,131/month (30.5% of MRR), about $1.67M a year
- Month-to-month churn 42.7% vs two-year 2.8% (15x relative risk); chi-square = 1,184.6, Cramér's V = 0.41
- Fibre 41.9% vs DSL 19.0% churn (difference 22.9 pp, 95% CI 20.6-25.3)
- Tenure: churned 18.0 vs retained 37.6 months (Welch t = -34.8, Cohen's d = -0.85)
- Logistic regression: two-year contract OR 0.26, fibre OR 1.66, electronic check OR 1.47, tech support OR 0.68
- Risk model AUC 0.844; top decile churns at 72.9% (2.75x lift); top 20% captures 50.7% of churners
- Pilot design: 1,509 customers per group to detect a 5-point churn reduction (80% power)

## Run
```bash
pip install -r requirements.txt
jupyter notebook Analytics_Report_Insights.ipynb   # Kernel -> Restart & Run All
```
Random seed 42 throughout.
