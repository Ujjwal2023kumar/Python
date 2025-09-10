import pandas as pd
import numpy as np

# From dictionary
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [25, 30, 22],
    "Score": [85, 90, 88]
})

# From list
s = pd.Series([10, 20, 30], name="Numbers")

# From numpy
df2 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])

df.head()       # First 5 rows
df.tail()       # Last 5 rows
df.info()       # Metadata
df.describe()   # Summary stats
df.shape        # (rows, cols)
df.dtypes       # Data types
df.columns      # Column names
df.index        # Index


df["Name"]             # Select column
df[["Name", "Score"]]  # Multiple columns
df.iloc[0]             # Row by position
df.loc[0, "Age"]       # Row by label
df[df["Age"] > 25]     # Boolean filter


df["Grade"] = ["A", "B", "A"]   # New column
df.at[0, "Age"] = 26            # Update single value
df.drop("Score", axis=1, inplace=True)  # Drop column
df.drop(1, axis=0)              # Drop row


df["Age"].mean()
df["Age"].sum()
df["Age"].min()
df["Age"].max()
df["Age"].std()
df["Age"].var()
df.corr()
df.cov()


df.sort_values("Age")
df.sort_index()


df.groupby("Grade")["Age"].mean()
df.groupby("Grade").agg({"Age": "mean", "Score": "max"})
df1 = pd.DataFrame({"ID": [1,2], "Name": ["X", "Y"]})
df2 = pd.DataFrame({"ID": [1,2], "Score": [100, 200]})

pd.merge(df1, df2, on="ID")
pd.concat([df1, df2], axis=0)  # Stack rows
pd.concat([df1, df2], axis=1)  # Stack columns

df.isna()
df.fillna(0)
df.dropna()

df.pivot(index="Name", columns="Grade", values="Age")
df.melt(id_vars="Name", value_vars=["Age", "Score"])
df.stack()
df.unstack()

df["Age"].rolling(2).mean()
df["Age"].expanding().sum()

df["Date"] = pd.to_datetime(["2021-01-01", "2021-01-02", "2021-01-03"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month


df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")
