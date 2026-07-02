Create Python analysis script

import pandas as pd

# Load the dataset
df = pd.read_csv("../Dataset/Sample_Superstore.csv", encoding="latin1")

# Display the first five rows
print("First 5 Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())
