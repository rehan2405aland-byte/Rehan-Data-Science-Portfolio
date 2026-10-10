# ==========================================
# PROJECT 3: ADVANCED SALES DATA CLEANING
# ==========================================

import pandas as pd
import numpy as np


# STEP 1 :- Import Data File
df = pd.read_csv(
    r"C:/Users/Rehan/Downloads/sales_data_dirty.txt"
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


# 1. Missing Values
miss_values = df.isna().sum()

print("\nMissing Values Found :-")
print(miss_values)

print("\nStep 1: Missing Values Found !!")


# 2. Duplicate Rows
print("\n" + "-" * 140)

dup_rows = df.duplicated().sum()

print("\nDuplicate Rows Found :- ", dup_rows)

df.drop_duplicates(inplace=True)

df.reset_index(
    drop=True,
    inplace=True
)

print("\nStep 2: Duplicate rows dropped & index reset successfully !!")


# 3. Category Column
print("\n" + "-" * 140)
print("For Category Column -")

print("\nBefore Cleaning Category Column:")
print(df["category"].head())

df["category"] = df["category"].fillna("Unknown")

df["category"] = (
    df["category"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nAfter Cleaning Category Column:")
print(df["category"].head())

print("\nStep 3: 'category' column standardized !!")


# 4. Quantity Column
print("\n" + "-" * 140)
print("For Quantity Column -")

print("\nBefore Cleaning Quantity Column:")
print(df["quantity"].head())

# Fix known text value
df["quantity"] = df["quantity"].replace(
    "ten",
    10
)

# Convert to numeric
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
df["quantity"] = df["quantity"].fillna(1)

# Convert to integer
df["quantity"] = df["quantity"].astype(int)

print("\nAfter Cleaning Quantity Column:")
print(df["quantity"].head())

print("\nStep 4: 'quantity' column cleaned successfully !!")


# 5. Price Column
print("\n" + "-" * 140)
print("For Price Column -")

print("\nBefore Cleaning Price Column:")
print(df["price"].head())

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

df["price"] = df["price"].fillna(0.0)

print("\nAfter Cleaning Price Column:")
print(df["price"].head())

print("\nStep 5: 'price' column cleaned successfully !!")


# 6. Discount Column
print("\n" + "-" * 140)
print("For Discount Column -")

print("\nBefore Cleaning Discount Column:")
print(df["discount"].head())


df["discount"] = (
    df["discount"]
    .astype(str)
    .str.strip()
)


def fix_mixed_discount(val):

    if pd.isna(val):
        return 0.0

    val = str(val).strip()

    if val.lower() in [
        "nan",
        "null",
        "none",
        ""
    ]:
        return 0.0

    # Percentage values
    if "%" in val:

        val_cleaned = float(
            val.replace("%", "")
        )

        if val_cleaned > 100:
            return 0.0

        if val_cleaned < 0:
            return 0.0

        return val_cleaned / 100

    # Decimal or numeric values
    try:

        float_val = float(val)

        if float_val < 0:
            return 0.0

        if float_val > 100:
            return 0.0

        if float_val > 1:
            return float_val / 100

        return float_val

    except ValueError:

        return 0.0


df["discount"] = df["discount"].apply(
    fix_mixed_discount
)

df["discount"] = df["discount"].astype(float)


print("\nAfter Cleaning Discount Column:")
print(df["discount"].head())

print(
    "\nStep 6: 'discount' column standardized "
    "to decimal scale (0.0 - 1.0) !!"
)


# 7. Order Date Column
print("\n" + "-" * 140)
print("For Order_Date Column -")

print("\nBefore Cleaning Order_Date Column:")
print(df["order_date"].head())

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce",
    format="mixed"
)

print("\nAfter Cleaning Order_Date Column:")
print(df["order_date"].head())

print(
    "\nMissing / Invalid Dates :- ",
    df["order_date"].isna().sum()
)

print(
    "\nStep 7: 'order_date' successfully "
    "converted to datetime format !!"
)


# 8. Payment Method
print("\n" + "-" * 140)
print("For Payment_Method Column -")

print("\nBefore Cleaning Payment_Method Column:")
print(df["payment_method"].head())

df["payment_method"] = df["payment_method"].fillna(
    "Unknown"
)

df["payment_method"] = (
    df["payment_method"]
    .astype(str)
    .str.strip()
    .str.title()
)

df["payment_method"] = df[
    "payment_method"
].replace(
    "Upi",
    "UPI"
)

print("\nAfter Cleaning Payment_Method Column:")
print(df["payment_method"].head())

print(
    "\nStep 8: 'payment_method' values unified !!"
)


# 9. Creating Total Amount Column
print("\n" + "-" * 140)

df["total_amount"] = (
    df["quantity"]
    * df["price"]
    * (1 - df["discount"])
)

print("\nTotal Amount:")
print(df["total_amount"].head())

print(
    "\nStep 9: New 'total_amount' column "
    "created successfully !!"
)


# STEP 3 :- Final Analysis
print("\n" + "=" * 140)
print("              MILESTONE 3 : Final Analysis (Reporting)")
print("=" * 140)


# 1. Total Sales
total_sales = df["total_amount"].sum()

print(
    "\nTotal Sales :- ",
    round(total_sales, 2)
)


# 2. Average Order Value
total_orders = len(df)

avg_order_val = (
    total_sales / total_orders
)

print(
    "\nAverage Order Value :- ",
    round(avg_order_val, 2)
)


# 3. Best-Selling Product
products = (
    df.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

best_product = products.head(1)

print("\nBest-Selling Product :-")
print(best_product)


# 4. Highest Revenue Product
rev_products = (
    df.groupby("product")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

high_rev_product = rev_products.head(1)

print("\nHighest Revenue Product :-")
print(high_rev_product)


# 5. Category-wise Revenue
category_wise_products = (
    df.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Revenue :-")
print(category_wise_products)


# 6. Payment-method-wise Sales
payment_method_sales = (
    df.groupby("payment_method")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPayment-method-wise Sales :-")
print(payment_method_sales)


# 7. Monthly Sales
month = df["order_date"].dt.to_period("M")

monthly_sales = (
    df.groupby(month)["total_amount"]
    .sum()
)

print("\nMonthly Sales :-")
print(monthly_sales)


print(
    "\nFinal Analysis (Reporting) "
    "is Successfully Done !!"
)


# STEP 4 :- Final Data Check
print("\n" + "=" * 140)
print("              MILESTONE 4 : Final Data Check")
print("=" * 140)

print("\nFinal Shape :-")
print(df.shape)

print("\nRemaining Missing Values :-")
print(df.isna().sum())

print("\nRemaining Duplicate Rows :-")
print(df.duplicated().sum())

print("\nData Types :-")
print(df.dtypes)


# STEP 5 :- Saving the Data
print("\n" + "=" * 140)
print("              MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv(
    "Project3_fully_cleaned_data.csv",
    index=False
)

print(
    "\nAll Data has Successfully Saved !!"
)

print(
    "File Name :- Project3_fully_cleaned_data.csv"
)