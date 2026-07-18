import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import  accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

dta = pd.read_csv(r"C:\Users\lokes\OneDrive\Desktop\RandomElecTheory\iotramdom\country_wise_latest.csv")
print("\n Data Frame is: \n", dta)
print("\n Columns of DataFrame: \n", dta.columns)
print("\n Informations of DataFrame: \n", dta.info)

dta["Confirmed"] = dta["Confirmed"].isnull().sum()
dta["Deaths"] = dta["Deaths"].isnull().sum()
