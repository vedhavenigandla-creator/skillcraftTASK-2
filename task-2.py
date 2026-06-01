# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
import os

# Upload CSV file
uploaded = files.upload()

# Get uploaded file name automatically
file_name = list(uploaded.keys())[0]

# Read CSV file
df = pd.read_csv(file_name)

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age values with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill missing Embarked values with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Drop Cabin column
df.drop("Cabin", axis=1, inplace=True)

# -------------------------------
# 1. Survival Count Graph
# -------------------------------

plt.figure(figsize=(6,4))

df["Survived"].value_counts().plot(
    kind="bar",
    edgecolor='black'
)

plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")

plt.show()