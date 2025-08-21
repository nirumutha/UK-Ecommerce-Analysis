import pandas as pd
import os

data_dir = '/Users/nirajmutha/Downloads/Ecommerce'  # Update this to the folder with your CSVs

csv_files = [
    'uk_retail_store_closures_historical.csv',
    'uk_retail_employment_historical.csv',
    'uk_retail_ecommerce_historical.csv',
    'uk_retail_regional_analysis.csv',
    'uk_retail_business_type_analysis.csv',
    'uk_retail_economic_indicators.csv',
    'uk_retail_future_forecasts.csv'
]

def load_data(data_folder, files):
    datasets = {}
    for file in files:
        path = os.path.join(data_folder, file)
        df = pd.read_csv(path)
        datasets[file.replace('.csv', '')] = df
        print(f"Loaded {file}: {df.shape[0]} rows, {df.shape[1]} columns")
    return datasets

data = load_data(data_dir, csv_files)

print("\nSample Data Exploration on Store Closures Historical Data")
store_closures = data['uk_retail_store_closures_historical']
print(store_closures.info())
print(store_closures.head())
