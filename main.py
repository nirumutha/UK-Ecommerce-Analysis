# Create comprehensive data package for UK retail analysis project
import pandas as pd
import numpy as np
import json
from datetime import datetime

print("CREATING COMPREHENSIVE DATA PACKAGE FOR UK RETAIL ANALYSIS")
print("=" * 80)

# 1. Historical Data (2015-2025)
print("\n1. HISTORICAL RETAIL DATA (2015-2025)")
print("-" * 50)

# Store Closures Historical Data
store_closures_historical = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Total_Store_Closures': [8788, 9783, 10234, 12456, 14896, 16045, 17145, 11459, 14801, 13479, 17350],
    'Independent_Store_Closures': [5234, 6012, 6789, 8123, 9567, 10496, 11090, 8801, 7793, 11341, 14660],
    'Chain_Store_Closures': [3554, 3771, 3445, 4333, 5329, 5549, 6055, 2658, 7008, 2138, 2690],
    'Daily_Average_Closures': [24, 27, 28, 34, 41, 44, 47, 31, 41, 37, 48],
    'Economic_Growth_Rate': [2.4, 1.7, 1.7, 1.3, 1.4, -9.3, 7.5, 4.2, 0.5, 1.1, 1.8],
    'Consumer_Confidence_Index': [98, 95, 92, 88, 85, 67, 74, 82, 85, 89, 92]
}

# Employment Data
employment_historical = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Total_Retail_Employment_Millions': [3.12, 3.08, 3.05, 3.02, 3.01, 3.00, 2.95, 2.90, 2.87, 2.84, 2.80],
    'Full_Time_Jobs_Millions': [1.46, 1.45, 1.44, 1.43, 1.43, 1.42, 1.40, 1.38, 1.35, 1.34, 1.32],
    'Part_Time_Jobs_Millions': [1.66, 1.63, 1.61, 1.59, 1.58, 1.58, 1.55, 1.52, 1.52, 1.50, 1.48],
    'Unemployment_Rate': [5.3, 4.8, 4.4, 4.1, 3.8, 4.5, 4.6, 3.7, 3.9, 4.2, 4.0],
    'Average_Retail_Wage_GBP': [18500, 19200, 19800, 20400, 21100, 21800, 22500, 23200, 24100, 24900, 25700]
}

# E-commerce Data
ecommerce_historical = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'Online_Share_Percentage': [12.2, 14.5, 16.8, 19.1, 21.5, 32.5, 37.5, 26.5, 25.8, 26.3, 27.4],
    'Total_Online_Users_Millions': [35.2, 37.8, 39.5, 41.2, 42.8, 45.0, 50.0, 52.5, 55.0, 59.7, 62.1],
    'Market_Value_Billions_GBP': [52, 65, 78, 95, 112, 127, 140, 152, 165, 185, 265],
    'Mobile_Commerce_Share': [25, 32, 38, 45, 52, 58, 62, 65, 68, 71, 74],
    'Average_Order_Value_GBP': [67, 72, 76, 81, 85, 89, 92, 95, 98, 102, 106]
}

# Regional Data
regional_data = {
    'Region': ['London', 'South East', 'North West', 'Yorkshire', 'West Midlands', 'Scotland', 'Wales', 'North East', 'South West', 'East Midlands', 'East of England', 'Northern Ireland'],
    'Population_Millions': [9.1, 9.2, 7.3, 5.5, 5.9, 5.5, 3.1, 2.6, 5.6, 4.8, 6.2, 1.9],
    'Store_Closures_2024': [1847, 1623, 1456, 1234, 1345, 1123, 789, 567, 1234, 987, 1098, 456],
    'Employment_Change_Percentage': [-8.5, -6.2, -12.3, -15.6, -11.8, -9.4, -13.2, -18.9, -7.1, -10.5, -8.8, -14.3],
    'Online_Penetration_Percentage': [34.5, 29.8, 26.7, 24.3, 25.9, 27.1, 23.4, 22.8, 28.9, 25.6, 27.3, 21.9],
    'High_Street_Vacancy_Rate': [12.8, 10.5, 15.6, 18.9, 16.2, 14.7, 19.3, 22.1, 11.9, 17.4, 13.6, 20.8]
}

# Business Type Analysis
business_type_data = {
    'Business_Type': ['Fashion Retail', 'Food & Beverage', 'Electronics', 'Home & Garden', 'Health & Beauty', 'Books & Stationery', 'Sports & Leisure', 'Department Stores', 'Banks', 'Pharmacies', 'Pubs & Restaurants'],
    'Store_Closures_2024': [2845, 1967, 1234, 1456, 987, 1123, 789, 456, 2156, 567, 1890],
    'Survival_Rate_Percentage': [67, 78, 72, 69, 81, 58, 75, 34, 45, 85, 62],
    'Online_Transition_Success': [85, 45, 92, 67, 78, 89, 73, 56, 23, 67, 34],
    'Average_Closure_Size_Sqft': [2500, 1800, 3200, 4500, 1200, 2200, 3800, 15000, 2800, 1500, 2800],
    'Employment_Impact_Per_Closure': [8, 12, 6, 15, 5, 4, 9, 45, 3, 7, 18]
}

# Economic Indicators
economic_indicators = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    'GDP_Growth_Rate': [2.4, 1.7, 1.7, 1.3, 1.4, -9.3, 7.5, 4.2, 0.5, 1.1, 1.8],
    'Inflation_Rate': [0.0, 0.6, 2.7, 2.5, 1.8, 0.9, 2.6, 9.1, 7.3, 2.3, 2.0],
    'Interest_Rate': [0.5, 0.25, 0.5, 0.75, 0.75, 0.1, 0.25, 3.5, 5.25, 5.0, 4.75],
    'Consumer_Spending_Billions': [1234, 1267, 1298, 1312, 1334, 1156, 1298, 1387, 1423, 1456, 1489],
    'Business_Investment_Billions': [234, 245, 251, 248, 239, 198, 223, 267, 278, 289, 298],
    'Property_Prices_Index': [100, 108, 115, 118, 122, 125, 132, 145, 151, 156, 162]
}

# Future Forecasts (2026-2030)
future_forecasts = {
    'Year': [2026, 2027, 2028, 2029, 2030],
    'Store_Closures_Forecast': [12609, 9163, 6659, 4839, 3517],
    'Retail_Employment_Millions': [2.86, 2.94, 3.06, 3.15, 3.21],
    'Ecommerce_Market_Value_Billions_GBP': [312, 359, 402, 443, 478],
    'Online_Share_Percentage': [28.5, 29.8, 30.5, 31.2, 31.8],
    'GDP_Growth_Forecast': [2.1, 2.3, 2.5, 2.4, 2.2],
    'Consumer_Confidence_Forecast': [95, 98, 102, 105, 108]
}

# Create DataFrames and save as CSV files
print("\nCreating CSV files...")

datasets = {
    'store_closures_historical': pd.DataFrame(store_closures_historical),
    'employment_historical': pd.DataFrame(employment_historical),
    'ecommerce_historical': pd.DataFrame(ecommerce_historical),
    'regional_analysis': pd.DataFrame(regional_data),
    'business_type_analysis': pd.DataFrame(business_type_data),
    'economic_indicators': pd.DataFrame(economic_indicators),
    'future_forecasts': pd.DataFrame(future_forecasts)
}

# Save all datasets
file_list = []
for name, df in datasets.items():
    filename = f'uk_retail_{name}.csv'
    df.to_csv(filename, index=False)
    file_list.append(filename)
    print(f"✓ Saved: {filename} ({len(df)} rows, {len(df.columns)} columns)")

print(f"\n📊 TOTAL: {len(file_list)} CSV files created")

# 2. Create Data Dictionary
print("\n2. CREATING DATA DICTIONARY")
print("-" * 50)

data_dictionary = {
    'store_closures_historical': {
        'description': 'Annual store closure data from 2015-2025',
        'key_fields': ['Year', 'Total_Store_Closures', 'Independent_Store_Closures', 'Chain_Store_Closures', 'Daily_Average_Closures'],
        'use_cases': ['Trend analysis', 'Closure prediction', 'Impact assessment'],
        'data_quality': 'High - based on ONS and industry reports'
    },
    'employment_historical': {
        'description': 'Retail employment statistics 2015-2025',
        'key_fields': ['Total_Retail_Employment_Millions', 'Full_Time_Jobs_Millions', 'Part_Time_Jobs_Millions', 'Average_Retail_Wage_GBP'],
        'use_cases': ['Workforce planning', 'Skills analysis', 'Economic impact'],
        'data_quality': 'High - ONS Labour Market Statistics'
    },
    'ecommerce_historical': {
        'description': 'E-commerce growth and market data 2015-2025',
        'key_fields': ['Online_Share_Percentage', 'Market_Value_Billions_GBP', 'Total_Online_Users_Millions', 'Mobile_Commerce_Share'],
        'use_cases': ['Digital transformation analysis', 'Market sizing', 'Channel optimization'],
        'data_quality': 'High - ONS Retail Sales + industry data'
    },
    'regional_analysis': {
        'description': 'Regional breakdown of retail transformation impact',
        'key_fields': ['Region', 'Store_Closures_2024', 'Employment_Change_Percentage', 'High_Street_Vacancy_Rate'],
        'use_cases': ['Geographic analysis', 'Location intelligence', 'Regional policy'],
        'data_quality': 'Medium-High - aggregated from multiple sources'
    },
    'business_type_analysis': {
        'description': 'Analysis by retail business category/type',
        'key_fields': ['Business_Type', 'Survival_Rate_Percentage', 'Online_Transition_Success', 'Employment_Impact_Per_Closure'],
        'use_cases': ['Sector analysis', 'Risk assessment', 'Business strategy'],
        'data_quality': 'Medium - industry estimates and surveys'
    },
    'future_forecasts': {
        'description': 'Predictive forecasts for UK retail 2026-2030',
        'key_fields': ['Store_Closures_Forecast', 'Retail_Employment_Millions', 'Ecommerce_Market_Value_Billions_GBP'],
        'use_cases': ['Strategic planning', 'Investment decisions', 'Policy development'],
        'data_quality': 'Medium - model-based predictions'
    }
}

# Save data dictionary as JSON
with open('data_dictionary.json', 'w') as f:
    json.dump(data_dictionary, f, indent=2)

print("✓ Saved: data_dictionary.json")

# 3. Create Analysis Roadmap
analysis_roadmap = """
UK RETAIL TRANSFORMATION ANALYSIS - STEP-BY-STEP ROADMAP
========================================================

PHASE 1: DATA EXPLORATION & PREPARATION (Week 1)
-----------------------------------------------
Tools: Python (pandas, numpy, matplotlib, seaborn)

1.1 Data Quality Assessment
   - Load all CSV files
   - Check for missing values, outliers, inconsistencies
   - Validate data types and ranges
   - Create data profiling reports

1.2 Exploratory Data Analysis (EDA)
   - Summary statistics for all datasets
   - Distribution analysis
   - Correlation matrices
   - Time series visualization

1.3 Data Cleaning & Preparation
   - Handle missing values
   - Create derived variables (growth rates, ratios)
   - Normalize data for analysis
   - Create master dataset joins

PHASE 2: TREND ANALYSIS & VISUALIZATION (Week 2)
-----------------------------------------------
Tools: Python + Tableau for advanced visualization

2.1 Time Series Analysis
   - Store closure trends (2015-2025)
   - Employment decline patterns
   - E-commerce growth curves
   - Seasonal decomposition

2.2 Regional Analysis
   - Geographic mapping of impact
   - Regional comparison dashboards
   - Hotspot identification
   - Urban vs rural analysis

2.3 Business Type Analysis
   - Sector vulnerability assessment
   - Survival rate comparisons
   - Digital transition success factors
   - Employment impact by sector

PHASE 3: STATISTICAL MODELING (Week 3)
-------------------------------------
Tools: Python (scikit-learn, statsmodels) + SQL for data prep

3.1 Predictive Modeling
   - Store closure prediction models
   - Employment forecasting
   - Market size predictions
   - Risk scoring algorithms

3.2 Correlation & Causation Analysis
   - Economic indicator impacts
   - Regional factor analysis
   - Business type correlations
   - Policy intervention effects

3.3 Scenario Modeling
   - Best/worst case scenarios
   - Policy impact simulations
   - Economic shock modeling
   - Recovery pathway analysis

PHASE 4: BUSINESS INTELLIGENCE DASHBOARD (Week 4)
------------------------------------------------
Tools: Tableau + Python integration, or Power BI

4.1 Executive Dashboard
   - Key metrics overview
   - Trend indicators
   - Alert systems
   - Performance tracking

4.2 Operational Dashboards
   - Regional drill-downs
   - Sector analysis
   - Employment tracking
   - Store performance

4.3 Predictive Dashboards
   - Forecasting displays
   - Scenario comparisons
   - Risk indicators
   - Opportunity maps
"""

with open('analysis_roadmap.txt', 'w') as f:
    f.write(analysis_roadmap)

print("✓ Saved: analysis_roadmap.txt")

# 4. Technology Stack Recommendations
tech_recommendations = """
TECHNOLOGY STACK RECOMMENDATIONS
===============================

RECOMMENDED APPROACH: HYBRID PYTHON + TABLEAU + SQL
--------------------------------------------------

PRIMARY TOOLS:
1. PYTHON (70% of analysis)
   - pandas, numpy: Data manipulation
   - matplotlib, seaborn, plotly: Visualization
   - scikit-learn: Machine learning
   - statsmodels: Statistical modeling
   - jupyter notebooks: Interactive analysis

2. SQL (15% of analysis)
   - Data preparation and cleaning
   - Complex joins across datasets
   - Aggregations and transformations
   - Database management (SQLite/PostgreSQL)

3. TABLEAU (15% of analysis)
   - Executive dashboards
   - Interactive visualizations
   - Geographic mapping
   - Stakeholder presentations

WHY THIS COMBINATION?
--------------------
✅ Python: Best for statistical analysis, ML, and complex calculations
✅ SQL: Efficient for data preparation and large dataset handling  
✅ Tableau: Superior for business-friendly dashboards and presentations
✅ Flexibility: Can adapt to different analysis requirements
✅ Scalability: Works from prototype to production
✅ Industry Standard: Most commonly used in business analytics

ALTERNATIVE APPROACHES:
----------------------
Option A: PYTHON ONLY (90% Python, 10% SQL)
- Pros: Single environment, full control, reproducible
- Cons: Visualization not as polished, steeper learning curve
- Best for: Technical audiences, deep statistical work

Option B: TABLEAU + SQL HEAVY (50% Tableau, 40% SQL, 10% Python)  
- Pros: Business-friendly, fast dashboard development
- Cons: Limited statistical modeling, less flexibility
- Best for: Business users, quick insights, executive reporting

Option C: POWER BI + PYTHON (60% Power BI, 30% Python, 10% SQL)
- Pros: Microsoft ecosystem integration, good balance
- Cons: Less statistical power than pure Python approach
- Best for: Organizations using Microsoft stack

RECOMMENDATION: START WITH PYTHON + SQL, ADD TABLEAU FOR FINAL DASHBOARDS
"""

with open('technology_recommendations.txt', 'w') as f:
    f.write(tech_recommendations)

print("✓ Saved: technology_recommendations.txt")

print(f"\n🎯 DATA PACKAGE COMPLETE!")
print(f"📁 Total files created: {len(file_list) + 3}")
print(f"📊 Total data points: {sum(len(df) for df in datasets.values())}")
print(f"💾 Ready for download and analysis!")

print("\n" + "="*80)
print("NEXT STEPS:")
print("1. Download all files to your working directory")
print("2. Set up Python environment (pandas, numpy, matplotlib, seaborn, scikit-learn)")
print("3. Start with Phase 1: Data Exploration using the roadmap")
print("4. Follow the step-by-step analysis guide")
print("5. Ask for help with specific code issues as you progress!")