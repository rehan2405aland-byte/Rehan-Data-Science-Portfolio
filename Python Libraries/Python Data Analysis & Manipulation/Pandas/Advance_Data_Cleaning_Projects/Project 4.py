# ===================================================
# PROJECT 4: ADVANCED SALES DATA CLEANING (1530 Rows)
# ===================================================

import pandas as pd
import numpy as np


# STEP 1 :- Import Data File
df = pd.read_csv(
    r"C:/Users/Rehan/Downloads/large_dirty_dataset_1530_rows.csv"
)

print("=" * 140)
print("              MILESTONE 1 : Import Data File")
print("=" * 140)

print("Shape of Data :- ", df.shape)
print("Data has been Successfully Loaded !!")


# STEP 2 :- Cleaning The Data
print("\n" + "=" * 140)
print("              MILESTONE 2 : Cleaning The Data")
print("=" * 140)


# 1. Duplicate Rows
dup_rows = df.duplicated().sum()

print("\nDuplicate Rows Found :- ", dup_rows)

df.drop_duplicates(
    inplace=True
)

df.reset_index(
    drop=True,
    inplace=True
)

print(
    "\nDuplicate rows dropped & index reset successfully !!"
)


# ----------------------------------------------------------------------------
# 2. Missing Values

print("\n" + "-" * 140)

miss_values = df.isna().sum()

print("Missing Values :-")
print(miss_values)

print("\nMissing Values Identified !!")


# ----------------------------------------------------------------------------
# 3. Name Column

df["name"] = df["name"].fillna("Unknown")

df["name"] = (
    df["name"]
    .astype(str)
    .str.strip()
    .str.title()
)


# ----------------------------------------------------------------------------
# 4. Email Column

df["email"] = df["email"].fillna("Unknown")

df["email"] = (
    df["email"]
    .astype(str)
    .str.strip()
)


# ----------------------------------------------------------------------------
# 5. Phone Column

df["phone"] = pd.to_numeric(
    df["phone"],
    errors="coerce"
).astype("Int64")

df["phone"] = (
    df["phone"]
    .astype("string")
    .fillna("Unknown")
)


# ----------------------------------------------------------------------------
# 6. Age Column

df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

# Remove unrealistic ages
df.loc[
    (df["age"] < 18) | (df["age"] > 100),
    "age"
] = np.nan

# Fill missing age with median
df["age"] = df["age"].fillna(
    df["age"].median()
)

df["age"] = df["age"].astype(int)


# ----------------------------------------------------------------------------
# 7. City Column

df["city"] = df["city"].fillna("Unknown")

df["city"] = (
    df["city"]
    .astype(str)
    .str.strip()
    .str.title()
)


# ----------------------------------------------------------------------------
# 8. Department Column

df["department"] = df["department"].fillna("Unknown")

df["department"] = (
    df["department"]
    .astype(str)
    .str.strip()
    .str.title()
)


# ----------------------------------------------------------------------------
# 9. Salary Column

df["salary"] = df["salary"].replace(
    [
        "unknown",
        "not available",
        " ",
        "",
        "null",
        "None"
    ],
    np.nan
)

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

sal_med = df["salary"].median()

df["salary"] = df["salary"].fillna(
    sal_med
)


# ----------------------------------------------------------------------------
# 10. Customer ID Column

df["customer_id"] = pd.to_numeric(
    df["customer_id"],
    errors="coerce"
)

df["customer_id"] = df["customer_id"].astype("Int64")


# ----------------------------------------------------------------------------
# 11. Join Date Column

df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce",
    format="mixed"
)

# Missing/invalid dates are kept as NaT
# because filling them with another customer's date
# could create incorrect information.


# ----------------------------------------------------------------------------
# 12. Status Column

df["status"] = df["status"].fillna(
    "Unknown"
)

df["status"] = (
    df["status"]
    .astype(str)
    .str.strip()
    .str.title()
)


# ----------------------------------------------------------------------------
# 13. Product Column

df["product"] = df["product"].fillna(
    "Unknown Product"
)

df["product"] = (
    df["product"]
    .astype(str)
    .str.strip()
    .str.title()
)


# ----------------------------------------------------------------------------
# 14. Quantity Column

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

# Remove invalid quantities
df.loc[
    df["quantity"] <= 0,
    "quantity"
] = np.nan

# Fill missing quantity
df["quantity"] = df["quantity"].fillna(
    1
)

df["quantity"] = df["quantity"].astype(int)


# ----------------------------------------------------------------------------
# 15. Price Column

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(
        r"[^\d.]",
        "",
        regex=True
    )
)

df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)

# Remove negative/invalid prices
df.loc[
    df["price"] < 0,
    "price"
] = np.nan

price_med = df["price"].median()

df["price"] = df["price"].fillna(
    price_med
)


# ----------------------------------------------------------------------------
# 16. Discount Column

df["discount"] = pd.to_numeric(
    df["discount"],
    errors="coerce"
)

df["discount"] = df["discount"].fillna(
    0.0
)

# Keep discount between 0 and 1
df.loc[
    (df["discount"] < 0) |
    (df["discount"] > 1),
    "discount"
] = 0.0


# ----------------------------------------------------------------------------
# 17. Final Missing Values Check

print("\n" + "-" * 140)

miss_values = df.isna().sum()

print("Remaining Missing Values :-")
print(miss_values)


# STEP 3 :- Inserting New Column
print("\n" + "=" * 140)
print("              MILESTONE 3 : Inserting New Column")
print("=" * 140)


df["total_amount"] = (
    df["quantity"]
    * df["price"]
    * (1 - df["discount"])
)

print("\nTotal Amount Column Created Successfully !!")

print(
    df[
        [
            "customer_id",
            "product",
            "quantity",
            "price",
            "discount",
            "total_amount"
        ]
    ].head(10)
)


# STEP 4 :- Final Analysis
print("\n" + "=" * 140)
print("              MILESTONE 4 : Final Analysis (Reporting)")
print("=" * 140)


# Top 10 rows by Total Amount

top_10_transactions = df.nlargest(
    10,
    "total_amount"
)

print("\nTop 10 Rows by Total Amount :-")
print(top_10_transactions)


# Total Sales

total_sales = df["total_amount"].sum()

print(
    "\nOverall Total Sales :- ",
    round(total_sales, 2)
)


# Average Sales

average_sales = df["total_amount"].mean()

print(
    "\nAverage Sales Per Row :- ",
    round(average_sales, 2)
)


# Product-wise Sales

product_sales = (
    df.groupby("product")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProduct-wise Total Sales :-")
print(product_sales)


# Department-wise Sales

department_sales = (
    df.groupby("department")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nDepartment-wise Total Sales :-")
print(department_sales)


# City-wise Sales

city_sales = (
    df.groupby("city")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCity-wise Total Sales :-")
print(city_sales)


# STEP 5 :- Final Data Check
print("\n" + "=" * 140)
print("              MILESTONE 5 : Final Data Check")
print("=" * 140)

print("\nFinal Shape :-")
print(df.shape)

print("\nRemaining Missing Values :-")
print(df.isna().sum())

print("\nRemaining Duplicate Rows :-")
print(df.duplicated().sum())

print("\nData Types :-")
print(df.dtypes)


# STEP 6 :- Saving the Data
print("\n" + "=" * 140)
print("              MILESTONE 6 : Saving the Data")
print("=" * 140)


df.to_csv(
    "Project4_fully_cleaned_data.csv",
    index=False
)

print(
    "\nAll Data has Successfully Saved !!"
)

print(
    "File Name :- Project4_fully_cleaned_data.csv"
)