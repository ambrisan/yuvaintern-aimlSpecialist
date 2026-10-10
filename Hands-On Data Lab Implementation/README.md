# Hands-On Data Lab Implementation

Yuva Intern – Task 2 (Data Science). A complete, reproducible data-analysis lab using Python, Jupyter, NumPy, Pandas, Matplotlib, Seaborn and Scikit-learn.

## Contents
| File | Purpose |
|---|---|
| `Data_Lab_Implementation.ipynb` | Main notebook (code + outputs + visualizations + insights) |
| `data/sales_raw.csv` | Raw dataset with intentional quality problems |
| `data/sales_clean.csv` | Cleaned dataset |
| `images/` | Saved charts (7) |
| `requirements.txt` | Library list |

## What is covered
1. Environment setup and version check
2. Selection, filtering, sorting, grouping, aggregation, pivot tables and merging (Pandas); statistics and z-scores (NumPy)
3. Cleaning: duplicates, missing values, inconsistent text, wrong dtypes, impossible values, outlier check (IQR)
4. Visualizations: bar, line, histogram, scatter, box, heatmap, count plot
5. Descriptive statistics, skewness, correlation and regression slope
6. Written observations and insights

## Run it
```bash
python -m venv venv
venv\Scripts\activate        # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
jupyter notebook Data_Lab_Implementation.ipynb   # Kernel -> Restart & Run All
```
The dataset is generated with `numpy` seed 42, so results are identical on every run.

## Key findings
- Laptops produce ~40% of revenue; online channel ~59%.
- Discount vs rating shows a weak negative correlation (r ≈ -0.10).
- Revenue is right-skewed (skew ≈ 2.6) because of high-ticket items.
