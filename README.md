# Unemployment Analysis

## Overview

This project analyzes unemployment data in India to understand unemployment trends, regional differences, rural and urban unemployment, labour participation, and the impact of the COVID-19 period.

## Objectives

- Analyze unemployment rate data in India.
- Clean and explore the datasets using Python.
- Visualize unemployment trends over time.
- Compare unemployment rates across regions.
- Compare rural and urban unemployment.
- Analyze labour participation rates.
- Investigate the impact of COVID-19 on unemployment.
- Identify important patterns and trends.
- Present insights that can support economic and social policy discussions.

## Datasets

The project uses two datasets:

1. `Unemployment in India.csv`
2. `Unemployment_Rate_upto_11_2020.csv`

The datasets contain information about unemployment rate, labour participation rate, employment estimates, area, region, and date.

## Technologies Used

- Python
- Pandas
- Matplotlib

## Data Cleaning and Exploration

The following preprocessing steps were performed:

- Removed extra spaces from column names.
- Cleaned text values.
- Converted date columns into proper date format.
- Converted numerical columns into numeric values.
- Removed missing values from important analysis columns.
- Sorted the data chronologically.
- Calculated descriptive statistics and regional averages.

## Analysis Performed

### 1. Unemployment Rate Over Time

The project analyzes how the average unemployment rate changed over the available period.

### 2. Regional Unemployment

Average unemployment rates were calculated for different regions to identify areas with relatively higher and lower unemployment levels.

### 3. Rural vs Urban Unemployment

The analysis compares average unemployment rates between rural and urban areas.

### 4. Labour Participation Rate

The project studies changes in the average labour participation rate over time.

### 5. COVID-19 Impact

The unemployment rate before March 2020 was compared with the unemployment rate from March 2020 onwards to examine changes during the COVID-19 period.

The analysis calculates the change in average unemployment rate and visualizes the unemployment trend during this period.

### 6. Key Patterns

The project identifies:

- Highest recorded unemployment rate.
- Lowest recorded unemployment rate.
- Monthly changes in unemployment.
- Differences in unemployment across regions.
- Differences between rural and urban unemployment.

## Visualizations

The following graphs are generated:

- Unemployment rate over time
- Top 10 regions by average unemployment rate
- Rural vs Urban unemployment
- Labour participation rate over time
- COVID-19 impact on unemployment

## Key Insights

The analysis helps identify changes in unemployment over time and differences between regions and areas. The COVID-19 period can be compared with the pre-COVID period to understand how unemployment conditions changed.

These findings can help highlight the importance of employment-support programs, regional employment opportunities, skill development, and targeted economic support during periods of increased unemployment.

## Policy Relevance

The analysis can provide useful information for:

- Employment generation programs
- Skill development and training initiatives
- Regional employment planning
- Rural and urban employment policies
- Economic support during major disruptions such as pandemics

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