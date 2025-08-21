import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_dir = '/Users/nirajmutha/Downloads/Ecommerce'  # Update as needed
region_file = 'uk_retail_regional_analysis.csv'
region_path = os.path.join(data_dir, region_file)

df = pd.read_csv(region_path)

print(df.info())
print(df.head())

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Online_Penetration_Percentage', y='Store_Closures_2024', hue='Region', palette='viridis', s=100)
plt.title('E-commerce Penetration vs Store Closures by Region')
plt.xlabel('Online Penetration (%)')
plt.ylabel('Store Closures in 2024')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



