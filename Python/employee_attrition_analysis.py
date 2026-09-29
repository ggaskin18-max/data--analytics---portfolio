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

department_summary = (
    df.assign(Left=df["Attrition"].eq("Yes").astype(int))
      .groupby("Department")
      .agg(
          Total_Employees=("Attrition", "size"),
          Employees_Left=("Left", "sum")
      )
)

department_summary["Attrition_Rate_Percentage"] = (
    department_summary["Employees_Left"]
    / department_summary["Total_Employees"]
    * 100
).round(2)

department_summary = department_summary.sort_values(
    "Attrition_Rate_Percentage",
    ascending=False
)

print("\nDepartment Attrition:")
print(department_summary)

print("\nAttrition by job role — employee counts")
print(pd.crosstab(df["JobRole"], df["Attrition"]))

print("\nAttrition by job role — percentages within each role")
print(pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
).mul(100).round(2))
print("\nRecords analysed:", len(df))


