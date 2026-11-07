# Unemployment Analysis

## About the Project

This project analyzes unemployment data in India using Python. The main aim is to understand unemployment trends, compare different regions and areas, and study the effect of COVID-19 on unemployment.

## Objectives

- Analyze unemployment rate data.
- Clean and explore the data using Python.
- Visualize unemployment trends.
- Compare unemployment rates across regions.
- Compare rural and urban unemployment.
- Study the impact of COVID-19 on unemployment.
- Identify important patterns and trends.
- Understand how the findings can be useful for economic and social policies.

## Dataset

This project uses two datasets:

- `Unemployment in India.csv`
- `Unemployment_Rate_upto_11_2020.csv`

The datasets contain information about unemployment rates, labour participation, regions, areas, and dates.

## Technologies Used

- Python
- Pandas
- Matplotlib

## Data Cleaning

The data was cleaned using Python by:

- Removing extra spaces from column names and text.
- Converting dates into the correct format.
- Converting numerical columns into numeric values.
- Removing missing values from important columns.
- Sorting the data according to date.

## Analysis Performed

### 1. Unemployment Trend

The average unemployment rate was analyzed over time to understand how it changed during the given period.

### 2. Regional Analysis

The average unemployment rate was calculated for different regions to compare unemployment levels.

### 3. Rural and Urban Analysis

The unemployment rates of rural and urban areas were compared.

### 4. Labour Participation

The labour participation rate was analyzed over time.

### 5. COVID-19 Impact

Unemployment rates before March 2020 were compared with rates from March 2020 onwards to study the impact of COVID-19.

### 6. Key Patterns

The analysis identifies:

- Highest unemployment rate
- Lowest unemployment rate
- Monthly unemployment trends
- Regional differences
- Rural and urban differences

## Visualizations

The project contains the following graphs:

- Unemployment Rate Over Time
- Top 10 Regions by Average Unemployment Rate
- Rural vs Urban Unemployment
- Labour Participation Rate Over Time
- COVID-19 Impact on Unemployment

## Key Insights

The analysis shows how unemployment changed over time and how unemployment levels differed across regions and between rural and urban areas.

The COVID-19 period can also be compared with the period before March 2020 to understand changes in unemployment.

## Policy Relevance

The findings can be useful for understanding areas where employment support, skill development, regional planning, and economic support may be needed.

## Project Structure

```text
Unemployment_Analysis/
│
├── graphs/
│   ├── unemployment_trend.png
│   ├── state_unemployment.png
│   ├── unemployment_by_area.png
│   ├── labour_participation.png
│   └── covid_impact.png
│
├── Unemployment in India.csv
├── Unemployment_Rate_upto_11_2020.csv
├── unemployment_analysis.py
├── requirements.txt
└── README.md
```