import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
df1 = pd.read_csv("Unemployment in India.csv")
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Clean column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Clean text columns
for df in [df1, df2]:
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

# Convert date columns
df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)
df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)

# Convert numerical columns
df1["Estimated Unemployment Rate (%)"] = pd.to_numeric(
    df1["Estimated Unemployment Rate (%)"], errors="coerce"
)

df2["Estimated Unemployment Rate (%)"] = pd.to_numeric(
    df2["Estimated Unemployment Rate (%)"], errors="coerce"
)

df2["Estimated Labour Participation Rate (%)"] = pd.to_numeric(
    df2["Estimated Labour Participation Rate (%)"], errors="coerce"
)

# Remove missing values
df1 = df1.dropna(subset=["Estimated Unemployment Rate (%)"])
df2 = df2.dropna(subset=[
    "Estimated Unemployment Rate (%)",
    "Estimated Labour Participation Rate (%)"
])

# Sort data by date
df1 = df1.sort_values("Date")
df2 = df2.sort_values("Date")

# Display basic statistics
print("\n--- Dataset 1 Statistics ---")
print(df1["Estimated Unemployment Rate (%)"].describe())

print("\n--- Dataset 2 Statistics ---")
print(df2[[
    "Estimated Unemployment Rate (%)",
    "Estimated Labour Participation Rate (%)"
]].describe())

# Average unemployment rate by state
state_unemployment = (
    df2.groupby("Region")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
)

print("\n--- Average Unemployment Rate by Region ---")
print(state_unemployment)

# Average unemployment rate by area
area_unemployment = (
    df1.groupby("Area")["Estimated Unemployment Rate (%)"]
    .mean()
)

print("\n--- Average Unemployment Rate by Area ---")
print(area_unemployment)

# Create graphs folder
import os
os.makedirs("graphs", exist_ok=True)

# 1. Unemployment rate over time
monthly_unemployment = (
    df2.groupby("Date")["Estimated Unemployment Rate (%)"]
    .mean()
)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker="o"
)
plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/unemployment_trend.png")
plt.show()


# 2. Average unemployment rate by region
top_regions = state_unemployment.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_regions.index[::-1],
    top_regions.values[::-1]
)
plt.title("Top 10 Regions by Average Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("graphs/state_unemployment.png")
plt.show()


# 3. Rural vs Urban unemployment
plt.figure(figsize=(7, 5))
plt.bar(
    area_unemployment.index,
    area_unemployment.values
)
plt.title("Average Unemployment Rate: Rural vs Urban")
plt.xlabel("Area")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("graphs/unemployment_by_area.png")
plt.show()


# 4. Labour participation rate over time
monthly_participation = (
    df2.groupby("Date")["Estimated Labour Participation Rate (%)"]
    .mean()
)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_participation.index,
    monthly_participation.values,
    marker="o"
)
plt.title("Average Labour Participation Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Labour Participation Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/labour_participation.png")
plt.show()

print("\nAnalysis completed successfully!")
print("Graphs saved in the 'graphs' folder.")

# COVID-19 Impact Analysis

print("\n--- COVID-19 Impact Analysis ---")

# Pre-COVID period: before March 2020
pre_covid = df2[df2["Date"] < "2020-03-01"]

# COVID period: March 2020 onwards
covid_period = df2[df2["Date"] >= "2020-03-01"]

pre_covid_avg = pre_covid["Estimated Unemployment Rate (%)"].mean()
covid_avg = covid_period["Estimated Unemployment Rate (%)"].mean()

print(f"Average unemployment rate before COVID-19: {pre_covid_avg:.2f}%")
print(f"Average unemployment rate during COVID-19: {covid_avg:.2f}%")

change = covid_avg - pre_covid_avg
print(f"Change in average unemployment rate: {change:.2f} percentage points")

# Highest and lowest unemployment observations
highest = df2.loc[
    df2["Estimated Unemployment Rate (%)"].idxmax()
]

lowest = df2.loc[
    df2["Estimated Unemployment Rate (%)"].idxmin()
]

print("\n--- Key Patterns ---")
print(
    f"Highest recorded unemployment rate: "
    f"{highest['Estimated Unemployment Rate (%)']:.2f}% "
    f"in {highest['Region']} on {highest['Date'].strftime('%d-%m-%Y')}"
)

print(
    f"Lowest recorded unemployment rate: "
    f"{lowest['Estimated Unemployment Rate (%)']:.2f}% "
    f"in {lowest['Region']} on {lowest['Date'].strftime('%d-%m-%Y')}"
)

# Monthly average unemployment rate
monthly_rate = (
    df2.groupby(df2["Date"].dt.to_period("M"))
    ["Estimated Unemployment Rate (%)"]
    .mean()
)

print("\n--- Monthly Average Unemployment Rate ---")
print(monthly_rate)

# COVID-19 comparison graph
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_rate.index.astype(str),
    monthly_rate.values,
    marker="o"
)

plt.axvline(
    x="2020-03",
    linestyle="--",
    label="COVID-19 period begins"
)

plt.title("Unemployment Trend and COVID-19 Impact")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("graphs/covid_impact.png")
plt.show()

print("\nCOVID-19 analysis completed.")