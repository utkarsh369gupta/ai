import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Hardcoded dataset
data = pd.DataFrame({
    'Date': ['01-09-2024', '02-09-2024', '03-09-2024', '04-09-2024', '05-09-2024'],
    'Temperature (°C)': [22, 24, 23, 25, 26],
    'Humidity (%)': [60, 55, 58, 50, 52],
    'Energy Consumption (kWh)': [30, 32, 31, 29, 34]
})

# Preprocess the data
# Drop the Date column as it is not needed for prediction
data = data.drop('Date', axis=1)

# Split the data into features and target
X = data[['Temperature (°C)', 'Humidity (%)']]
y = data['Energy Consumption (kWh)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model's performance
r2 = r2_score(y_test, y_pred)
print("R^2 Score:", r2)

# Optionally, plot actual vs predicted values
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', color='red')
plt.xlabel('Actual Energy Consumption (kWh)')
plt.ylabel('Predicted Energy Consumption (kWh)')
plt.title('Actual vs Predicted Energy Consumption')
plt.show()
