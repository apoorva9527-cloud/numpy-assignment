import pandas as pd

# Create sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 92, 78, 88, 67, 91],
    "Passed": [True, True, False, True, False, True],
    "Category": ["A", "A", "B", "B", "C", "A"]
}

df = pd.DataFrame(data)

print("\n===== Original Dataset =====")
print(df)

# 1. Select single column
print("\n===== Single Column (Score) =====")
print(df["Score"])

# 2. Select multiple columns
print("\n===== Multiple Columns (Name and Score) =====")
selected_df = df[["Name", "Score"]]
print(selected_df)

# 3. Use iloc to retrieve first 3 rows
print("\n===== First 3 Rows using iloc =====")
print(df.iloc[0:3])

# 4. Use loc after setting index
df_indexed = df.set_index("Name")

print("\n===== Using loc (Row for Alice) =====")
print(df_indexed.loc["Alice"])

# 5. Filter rows where Score > 85
print("\n===== Score > 85 =====")
high_score = df[df["Score"] > 85]
print(high_score)

# 6. Filter rows where Score > 85 and Passed = True
print("\n===== Score > 85 AND Passed =====")
filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(filtered)

# 7. Sort filtered result descending by Score
print("\n===== Sorted High Performers (Descending Score) =====")
sorted_df = filtered.sort_values(by="Score", ascending=False)
print(sorted_df)

# 8. Chained filtering + sorting
print("\n===== Chained Filtering and Sorting =====")
result = df[(df["Score"] > 85) & (df["Passed"])].sort_values(by="Score", ascending=False)
print(result)