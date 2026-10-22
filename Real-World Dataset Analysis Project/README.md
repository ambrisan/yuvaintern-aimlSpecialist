# Real-World Dataset Analysis Project – Titanic Survival Patterns

Yuva Intern – Task 3 (AI/ML Research Specialist Internship)

**Dataset:** Titanic passenger data (891 rows, 12 columns), public dataset from the Data Science Dojo repository (originally Kaggle). A local copy is in `data/titanic_raw.csv`.

**Question:** Which passenger characteristics were associated with survival?

## Files
| File | Purpose |
|---|---|
| `Real_World_Dataset_Analysis.ipynb` | Full analysis: context, exploration, cleaning, EDA, 7 visualizations, insights |
| `data/titanic_raw.csv` / `titanic_clean.csv` | Raw and cleaned data |
| `data/metrics.json` | Key metrics exported from the notebook |
| `images/` | Saved charts |

## Method
1. Selection and context • 2. Exploration (structure, types, missing, duplicates) • 3. Cleaning (title standardisation, group-wise Age imputation, Embarked mode, Cabin→Deck, dtype fixes, IQR outlier review) • 4. EDA with Pandas/NumPy, chi-square and Mann-Whitney tests • 5. Visualization with Matplotlib/Seaborn • 6. Insights, limitations, recommendations

## Key findings
- Overall survival 38.4%; women 74% vs men 19%.
- Class: 63% (1st), 47% (2nd), 24% (3rd). First/second-class women survived at 97%/92%.
- Children 0-12 survived at 57%; travelling alone 30% vs 51% with family.
- Sex, class, port and travelling alone are all statistically significant (chi-square, p < 0.05).

## Run
```bash
pip install -r requirements.txt
jupyter notebook Real_World_Dataset_Analysis.ipynb   # Kernel -> Restart & Run All
```
