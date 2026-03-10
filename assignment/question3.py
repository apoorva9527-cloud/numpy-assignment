import pandas as pd

# Load dataset
df = pd.read_csv("assignment/dataset.csv")

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Last 5 Rows =====")
print(df.tail())

print("\n===== Dataset Info =====")
print(df.info())

print("\n===== Summary Statistics =====")
print(df.describe())

# Select single column
print("\n===== Single Column (Age) =====")
age_column = df["Age"]
print(age_column)

# Select multiple columns
print("\n===== Multiple Columns (Name and Score) =====")
selected_columns = df[["Name", "Score"]]
print(selected_columns)

# Filter rows where Score > 80
print("\n===== Filtered Rows (Score > 80) =====")
filtered_rows = df[df["Score"] > 80]
print(filtered_rows)