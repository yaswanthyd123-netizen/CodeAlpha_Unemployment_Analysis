# Task 2 — Unemployment Analysis with Python

Exploratory time-series analysis of monthly unemployment rates.

## Included data — please read
`unemployment.csv` is a **synthetic demonstration dataset**, not official government statistics. It contains illustrative monthly values from January 2019 to December 2024, including a simulated temporary shock around 2020. It is included so the project runs immediately. For a formal internship submission, replace it with the assigned/downloaded official dataset and keep the same columns: `date`, `unemployment_rate`.

## What it does
- Cleans dates and numeric values, checks missing values and duplicates.
- Summarizes the rate and identifies the highest/lowest months.
- Compares annual averages and visualizes the monthly trend.
- Highlights the 2020 period as a contextual interval, not as a causal analysis.

## Run
```bash
python -m pip install -r requirements.txt
python main.py
```
Charts and a yearly summary are saved in `outputs/`.
