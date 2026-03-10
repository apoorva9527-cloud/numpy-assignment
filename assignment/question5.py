import pandas as pd
import numpy as np

# 🔹 Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("\n===== Original Dataset =====")
print(df)

# 🔹 Detect missing values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# 🔹 Fill missing salary with mean
salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

print("\n===== Dataset After Filling Missing Salaries =====")
print(df)

# 🔹 Drop Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])

print("\n===== After Dropping Temporary_Notes =====")
print(df)

# 🔹 Rename Salary column
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\n===== After Renaming Column =====")
print(df)

# 🔹 Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n===== Department Salary Summary =====")
print(summary)