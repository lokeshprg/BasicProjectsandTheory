import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Create & Load Dataset
data = {
    'Size_sqft':[1500, 1800, 2400, np.nan, 3000, 1200, 2100, 1900, 2800, 1600],
    'Bedrooms': [3, 4, 3, 4, 5, 2, 3, 3, 4, 3],
    'Price_USD':[300000, 360000, 470000, 410000, 590000, 240000, 400000, 380000, 540000, 320000]
}

df = pd.DataFrame(data)
print("---Raw Dataset---")
print(df.head(), '\n')

# Step 2: Data Cleaning
print("Missing values per column:\n", df.isnull().sum())
df['Size_sqft'] = df['Size_sqft'].fillna(df['Size_sqft'].mean())
print("Cleaned Data")
print(df.head(), '\n')

# Step 3: Exploratory Data Analysis (EDA)
print("---Summary Statistics---")
print(df.describe(), "\n")

# Step 4: Data Visualization
plt.scatter(df['Size_sqft'], df['Price_USD'], color='blue', label='Data Points')
plt.title("House Price vs Size")
plt.xlabel('Size(sqft)')
plt.ylabel('Price($)')
plt.grid(True)
plt.show()

X = df[['Size_sqft', 'Bedrooms']]
y= df['Price_USD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state = 42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predicitons using the test data
predictions = model.predict(X_test)

# Evaluate model performance using Mean Squred Error
mse = mean_squared_error(y_test, predictions)
print(f"Model training complete.")
print(f"Mean Squared error on Test Set: {mse:.2f}")

# Predict the price of a new house (2000 sqft, 3 bedrooms)
new_house = pd.DataFrame([[2000, 3]], columns=['Size_sqft', 'Bedrooms'])
predicted_price = model.predict(new_house)
print(f"Predicted price for 2000 sqft 3-bed house : ${predicted_price[0]:,.2f}")

