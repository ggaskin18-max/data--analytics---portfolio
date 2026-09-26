from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "Data" / "employee_attrition - Cleaned(employee_attrition) (1).csv"

df = pd.read_csv(csv_path)

# Display the first 5 rows of the dataset
print(df.head())

# Display the number of rows and columns
print(df.shape)

# Display column names
print(df.columns)

# Display dataset information
df.info()

# Check for missing values
print(df.isnull().sum())

# Analyse employee attrition
attrition_counts = df["Attrition"].value_counts()

print("\nEmployee Attrition:")
print(attrition_counts)


