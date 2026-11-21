
"""CleanAir India - Beginner Data Analytics Project
IMPORTANT: The included CSV contains illustrative demo values only.
Replace it with verified CPCB / data.gov.in data before making real-world claims.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "air_quality_demo.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA_FILE)

# 2. Basic data checks and cleaning
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
df = df.dropna(subset=["City", "Month", "AQI"])
df = df[df["AQI"] >= 0]

print("\n--- DATA PREVIEW ---")
print(df.head(10))

print("\n--- DATA SUMMARY ---")
print(df.describe())

# 3. City-wise average AQI
city_avg = (
    df.groupby("City", as_index=False)["AQI"]
      .mean()
      .sort_values("AQI", ascending=False)
)
print("\n--- CITY-WISE AVERAGE AQI ---")
print(city_avg.round(1).to_string(index=False))
city_avg.to_csv(OUTPUT_DIR / "city_average_aqi.csv", index=False)

# 4. Find the highest average AQI city
highest_city = city_avg.iloc[0]
print(
    f"\nHighest average AQI in this dataset: "
    f"{highest_city['City']} ({highest_city['AQI']:.1f})"
)

# 5. Month-wise average AQI across all cities
month_avg = (
    df.groupby(["Month_Number", "Month"], as_index=False)["AQI"]
      .mean()
      .sort_values("Month_Number")
)
print("\n--- MONTH-WISE AVERAGE AQI ---")
print(month_avg[["Month", "AQI"]].round(1).to_string(index=False))
month_avg.to_csv(OUTPUT_DIR / "month_average_aqi.csv", index=False)

# 6. Create city comparison chart
plt.figure(figsize=(9, 5))
plt.bar(city_avg["City"], city_avg["AQI"])
plt.title("Average AQI by City (Illustrative Demo Data)")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "city_comparison.png", dpi=150)
plt.show()

# 7. Create monthly trend chart
plt.figure(figsize=(9, 5))
plt.plot(month_avg["Month"], month_avg["AQI"], marker="o")
plt.title("Monthly Average AQI Across Selected Cities (Demo Data)")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_trend.png", dpi=150)
plt.show()

print(f"\nCharts and summary CSV files saved in: {OUTPUT_DIR}")
print("\nReminder: Demo data is not official or suitable for factual conclusions.")