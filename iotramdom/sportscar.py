import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Readig data
data = pd.read_csv(r"C:\Users\lokes\OneDrive\Desktop\RandomElecTheory\iotramdom\Sport car price.csv")
print(data.columns, '\n')
data = data.head()

# Changing the str to numeric
data['Engine Size (L)'] = pd.to_numeric(
    data['Engine Size (L)'],
    errors='coerce'
)

data['Torque (lb-ft)'] = pd.to_numeric(
    data['Torque (lb-ft)'], 
    errors='coerce'
)
# Cleaning data
print("----Unfiltered Data----\n")
print(data.isnull().sum())
data['Engine Size (L)'] =data['Engine Size (L)'].fillna(data['Engine Size (L)'].mean())
data['Torque (lb-ft)'] =data['Torque (lb-ft)'].fillna(data['Torque (lb-ft)'].mean())
print("----Filtered Data----\n")
print(data.isnull().sum())

# Applying EDA
print("---After Applying EDA---\n")
print(data.describe())

# Visulaizing Data
plt.scatter(data['Engine Size (L)'], data['Torque (lb-ft)'], color='blue', label='Data Points')
plt.title("Engine Size v/s Tourque")
plt.xlabel("Engine Size")
plt.ylabel("Tourque")
plt.grid(True)
plt.show()
plt.bar(data['Engine Size (L)'], data['Torque (lb-ft)'])
plt.title("Engine Size v/s Tourque")
plt.xlabel("Engine Size")
plt.ylabel("Tourque")
plt.grid(True)
plt.show()

sns.countplot(data=data, x="Engine Size (L)")
plt.show()
sns.boxplot(x=data["Engine Size (L)"], y=data['Torque (lb-ft)'])
plt.show()
sns.violinplot(x =data['Engine Size (L)'], y =data['Torque (lb-ft)'], data = data)
plt.show()
sns.barplot(data=data, x='Engine Size (L)')
plt.show()