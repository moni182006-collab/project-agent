import pandas as pd

# Load dataset
df = pd.read_excel("data/online_retail.xlsx")

# Convert date safely
df.loc[:, "InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df.loc[:, "date"] = df["InvoiceDate"].dt.date

# Aggregate daily metrics
daily = (
    df.groupby("date")
    .agg(
        orders=("InvoiceNo", "nunique"),
        revenue=("TotalPrice", "sum"),
        traffic=("CustomerID", "nunique"),
    )
    .reset_index()
)

# Conversion rate (safe assignment)
daily.loc[:, "conversion_rate"] = daily["orders"] / daily["traffic"]

# Rename for pipeline compatibility
daily.rename(columns={"date": "timestamp"}, inplace=True)

# Save processed dataset
daily.to_csv("data/sales.csv", index=False)

print("✅ Processed dataset saved as data/sales.csv")
