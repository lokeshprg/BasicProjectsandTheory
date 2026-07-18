import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(r"C:\Users\lokes\OneDrive\Desktop\RandomElecTheory\iotramdom\soccer_salaries.csv")

# Data Cleaning
data = data.dropna().head(10)

# Convert salary to numeric (if needed)
data["Yearly Salary"] = pd.to_numeric(
    data["Yearly Salary"].astype(str).str.replace(",", ""),
    errors="coerce"
)

print(data)


plt.scatter(data["Age"], data["Yearly Salary"])
plt.title("Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Yearly Salary")
plt.grid(True)
plt.show()


plt.plot(data["Age"], data["Yearly Salary"], marker='o')
plt.title("Line Plot")
plt.xlabel("Age")
plt.ylabel("Yearly Salary")
plt.grid(True)
plt.show()


plt.bar(data["Age"], data["Yearly Salary"])
plt.title("Bar Plot")
plt.xlabel("Age")
plt.ylabel("Yearly Salary")
plt.show()


plt.hist(data["Yearly Salary"], bins=5)
plt.title("Histogram")
plt.xlabel("Yearly Salary")
plt.ylabel("Frequency")
plt.show()


plt.boxplot(data["Yearly Salary"])
plt.title("Box Plot")
plt.show()


sns.violinplot(y=data["Yearly Salary"])
plt.title("Violin Plot")
plt.show()


sns.heatmap(data.corr(numeric_only=True))
plt.title("Heatmap")
plt.show()


sns.countplot(x="Age", data=data)
plt.title("Count Plot")
plt.show()


plt.pie(
    data["Yearly Salary"],
    labels=data["Age"],
    autopct="%1.1f%%"
)
plt.title("Pie Chart")
plt.show()


sns.stripplot(
    x="Age",
    y="Yearly Salary",
    data=data
)
plt.title("Strip Plot")
plt.show()


plt.stem(data["Age"], data["Yearly Salary"])
plt.title("Stem Plot")
plt.show()


plt.barh(data["Age"], data["Yearly Salary"])
plt.title("Horizontal Bar Graph")
plt.show()


plt.figure(figsize=(8,3))
plt.axis("off")

table = plt.table(
    cellText=data.values,
    colLabels=data.columns,
    loc="center"
)


plt.show()

sns.pairplot(data)
plt.show()