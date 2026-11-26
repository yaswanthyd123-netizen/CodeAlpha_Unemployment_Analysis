from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "unemployment.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["unemployment_rate"] = pd.to_numeric(df["unemployment_rate"], errors="coerce")
df = df.dropna(subset=["date", "unemployment_rate"]).drop_duplicates().sort_values("date")

print("Dataset overview")
print(df.describe())
print(f"Missing values after cleaning: {int(df.isna().sum().sum())}")
print(f"Highest month: {df.loc[df.unemployment_rate.idxmax(), 'date'].date()} "
      f"({df.unemployment_rate.max():.2f}%)")
print(f"Lowest month: {df.loc[df.unemployment_rate.idxmin(), 'date'].date()} "
      f"({df.unemployment_rate.min():.2f}%)")

df["year"] = df["date"].dt.year
yearly = df.groupby("year", as_index=False)["unemployment_rate"].mean()
print("\nAnnual average unemployment rate (%)")
print(yearly.to_string(index=False, formatters={"unemployment_rate": "{:.2f}".format}))

out = ROOT / "outputs"
out.mkdir(exist_ok=True)
plt.figure(figsize=(11, 5))
plt.plot(df["date"], df["unemployment_rate"], linewidth=1.8)
plt.axvspan(pd.Timestamp("2020-03-01"), pd.Timestamp("2020-12-31"), alpha=0.15,
            label="Illustrative 2020 interval")
plt.title("Monthly Unemployment Rate (Demonstration Data)")
plt.xlabel("Month")
plt.ylabel("Unemployment rate (%)")
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(out / "unemployment_trend.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 4))
plt.bar(yearly["year"].astype(str), yearly["unemployment_rate"])
plt.title("Annual Average Unemployment Rate")
plt.xlabel("Year")
plt.ylabel("Average rate (%)")
plt.tight_layout()
plt.savefig(out / "annual_average.png", dpi=150)
yearly.to_csv(out / "yearly_summary.csv", index=False)
print(f"\nOutputs saved in: {out}")
