import pandas as pd
df = pd.read_csv("Tracker.csv")

#print(df.Amount)

print (df.head())
print (df.info())

total_spend_per_category = df.groupby('Category')['Amount'].sum()
print (total_spend_per_category)

average_spend_per_category = df.groupby('Category')['Amount'].mean()
print(average_spend_per_category)

summary = df.groupby('Category')['Amount'].agg(['sum','mean'])
print (summary)
# .agg() = "aggregate" — run multiple calculations at once, per group.
# Same idea as SQL's SELECT Category, SUM(Amount), AVG(Amount) ... GROUP BY Category

highest_expenses = df.sort_values('Amount', ascending= False)
print (highest_expenses)