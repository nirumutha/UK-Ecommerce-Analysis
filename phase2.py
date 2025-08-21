import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Update this to your CSV files folder
data_dir = '/Users/nirajmutha/Downloads/Ecommerce'

# Load datasets
store_closures = pd.read_csv(os.path.join(data_dir, 'uk_retail_store_closures_historical.csv'))
economic_indicators = pd.read_csv(os.path.join(data_dir, 'uk_retail_economic_indicators.csv'))

# Merge on Year
merged = pd.merge(store_closures, economic_indicators, on='Year', how='inner')

# Calculate correlation matrix for key columns
correlation = merged[['Total_Store_Closures', 'Economic_Growth_Rate', 'Consumer_Confidence_Index']].corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation between Store Closures and Economic Indicators')
plt.tight_layout()
plt.show()
