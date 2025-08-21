import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

# Update this path to your data folder
data_dir = '/Users/nirajmutha/Downloads/Ecommerce'

# Load datasets
store_closures = pd.read_csv(os.path.join(data_dir, 'uk_retail_store_closures_historical.csv'))
economic_indicators = pd.read_csv(os.path.join(data_dir, 'uk_retail_economic_indicators.csv'))

# Merge datasets on Year
data = pd.merge(store_closures, economic_indicators, on='Year')

# Use Year, Economic_Growth_Rate, Consumer_Confidence_Index as features
X = data[['Year', 'Economic_Growth_Rate', 'Consumer_Confidence_Index']]
y = data['Total_Store_Closures']

# Create and train linear regression model
model = LinearRegression()
model.fit(X, y)

# Predictions on historical data
y_pred = model.predict(X)

# Model evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'Model Mean Squared Error: {mse:.2f}')
print(f'Model R2 Score: {r2:.3f}')

# Visualize actual vs predicted
plt.figure(figsize=(10,6))
plt.plot(data['Year'], y, label='Actual Closures', marker='o')
plt.plot(data['Year'], y_pred, label='Predicted Closures', marker='x')
plt.title('Actual vs Predicted Store Closures')
plt.xlabel('Year')
plt.ylabel('Total Store Closures')
plt.legend()
plt.tight_layout()
plt.show()

# Forecast for next 5 years
future_years = pd.DataFrame({
    'Year': np.arange(data['Year'].max() + 1, data['Year'].max() + 6),
    'Economic_Growth_Rate': data['Economic_Growth_Rate'].iloc[-1],  # Assuming last known growth rate
    'Consumer_Confidence_Index': data['Consumer_Confidence_Index'].iloc[-1]  # Assuming last known confidence
})

future_pred = model.predict(future_years)

# Show forecasted closures
forecast_df = future_years.copy()
forecast_df['Predicted_Store_Closures'] = future_pred.astype(int)
print("\nForecasted Store Closures for next 5 years:")
print(forecast_df)

# Plot forecast with historical data
plt.figure(figsize=(10,6))
plt.plot(data['Year'], y, label='Historical Actual', marker='o')
plt.plot(data['Year'], y_pred, label='Historical Predicted', marker='x')
plt.plot(forecast_df['Year'], forecast_df['Predicted_Store_Closures'], label='Forecasted', marker='s', linestyle='--')
plt.title('Store Closure Forecast')
plt.xlabel('Year')
plt.ylabel('Total Store Closures')
plt.legend()
plt.tight_layout()
plt.show()
