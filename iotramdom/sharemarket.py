import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(r"C:\Users\lokes\OneDrive\Desktop\RandomElecTheory\iotramdom\Top vendors market share (2022 Q1).csv")

print("Columns:\n")
print(data.columns)

print("\nMissing Values:\n")
print(data.isnull().sum())

data = data.dropna()


data["Market share"] = pd.to_numeric(
    data["Market share"],
    errors="coerce"
)

data = data.dropna()

print("\nCleaned Data\n")
print(data.head())

print("\nStatistics\n")
print(data.describe())


plt.figure(figsize=(8,5))

plt.scatter(data["Manufacturer"],data["Market share"],color="green")

plt.title("Manufacturer vs Market Share")
plt.xlabel("Manufacturer")
plt.ylabel("Market Share")
plt.grid(True)

plt.show()


plt.figure(figsize=(8,5))

plt.plot(data["Manufacturer"],data["Market share"],marker='o',color='red')

plt.title("Manufacturer vs Market Share")
plt.xlabel("Manufacturer")
plt.ylabel("Market Share")
plt.grid(True)

plt.show()


plt.figure(figsize=(8,5))

plt.bar(data["Manufacturer"],data["Market share"],color="skyblue")

plt.title("Manufacturer vs Market Share")
plt.xlabel("Manufacturer")
plt.ylabel("Market Share")
plt.show()


plt.figure(figsize=(8,5))

plt.barh(data["Manufacturer"],data["Market share"],color="orange")

plt.title("Horizontal Bar Graph")

plt.show()

plt.figure(figsize=(7,5))

plt.hist(data["Market share"],bins=6,color="purple")

plt.title("Histogram")
plt.xlabel("Market Share")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(5,6))

plt.boxplot(data["Market share"])

plt.title("Box Plot")
plt.ylabel("Market Share")

plt.show()


plt.figure(figsize=(5,6))

sns.violinplot(y=data["Market share"],color="lightgreen")

plt.title("Violin Plot")

plt.show()

plt.figure(figsize=(8,5))

sns.stripplot(x="Manufacturer",y="Market share",data=data,jitter=True)

plt.title("Strip Plot")

plt.show()

plt.figure(figsize=(8,5))

sns.swarmplot(x="Manufacturer",y="Market share",data=data)

plt.title("Swarm Plot")

plt.show()


plt.figure(figsize=(7,7))

plt.pie(data["Market share"],labels=data["Manufacturer"],autopct="%1.1f%%",startangle=90)

plt.title("Market Share Distribution")

plt.show()


plt.figure(figsize=(8,5))

plt.fill_between(data["Manufacturer"],
    data["Market share"],
    alpha=0.5,
    color="cyan"
)

plt.plot(
    data["Manufacturer"],
    data["Market share"],
    color="blue"
)

plt.title("Area Plot")

plt.show()

plt.figure(figsize=(8,5))

plt.stem(
    range(len(data)),
    data["Market share"]
)

plt.xticks(
    range(len(data)),
    data["Manufacturer"],
    rotation=45
)

plt.title("Stem Plot")

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(
    x="Manufacturer",
    data=data,
    hue="Manufacturer",
    legend=False
)

plt.title("Count Plot")

plt.show()

plt.figure(figsize=(5,4))

sns.heatmap(
    data.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Heatmap")

plt.show()

plt.figure(figsize=(10,4))

plt.axis("off")

table = plt.table(
    cellText=data.values,
    colLabels=data.columns,
    cellLoc="center",
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2,1.5)

plt.title("Dataset Table")

plt.show()


numeric_columns = data.select_dtypes(include="number")

if numeric_columns.shape[1] >= 2:
    sns.pairplot(numeric_columns)

    plt.suptitle("Pair Plot", y=1.02)

    plt.show()
else:
    print("Pair Plot skipped (requires at least two numeric columns).")