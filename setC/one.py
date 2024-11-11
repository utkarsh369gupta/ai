import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Size': [1500, 2000, 2500, 1800, 2200, 1700, 2100, 1600, 2400, 1900],
    'Bedrooms': [3, 4, 4, 3, 4, 3, 4, 3, 5, 3],
    'Price': [300000, 400000, 500000, 350000, 450000, 325000, 420000, 310000, 490000, 370000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file
# df.to_excel('housing_prices.xlsx', index=False)

# # Read the Excel file (to demonstrate loading)
# df = pd.read_excel('housing_prices.xlsx')

# Prepare features (X) and target variable (y)
X = df[['Size', 'Bedrooms']]
y = df['Price']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate Mean Squared Error
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

# Print model coefficients and error metrics
print("\nModel Coefficients:")
print(f"Intercept: ${model.intercept_:.2f}")
print(f"Size coefficient: ${model.coef_[0]:.2f} per sq ft")
print(f"Bedrooms coefficient: ${model.coef_[1]:.2f} per bedroom")
print(f"\nRoot Mean Squared Error: ${rmse:.2f}")

# Create scatter plot of actual vs predicted prices
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, color='blue', label='Data points')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='Perfect prediction')
plt.xlabel('Actual Price ($)')
plt.ylabel('Predicted Price ($)')
plt.title('Actual vs Predicted Housing Prices')
plt.legend()
plt.grid(True)
plt.show()

# Optional: Print the R-squared score
r2_score = model.score(X, y)
print(f"\nR-squared Score: {r2_score:.4f}")

# Example prediction for a new house
new_house = np.array([[2000, 4]])  # 2000 sq ft, 4 bedrooms
predicted_price = model.predict(new_house)[0]
print(f"\nPredicted price for a 2000 sq ft, 4-bedroom house: ${predicted_price:,.2f}")