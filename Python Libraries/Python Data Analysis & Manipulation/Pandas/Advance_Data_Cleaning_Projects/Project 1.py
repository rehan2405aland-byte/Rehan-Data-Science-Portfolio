# PROJECT 1 : MESSY SALES DATA CLEANING

import pandas as pd
import numpy as np


# ================================================================
# STEP 1 :- Loading the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/pandas_messy_sales.csv")

print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)

print("Shape of Data :- ", df.shape)
print("\nColumns :-")
print(df.columns)


# ================================================================
# STEP 2 :- Fixing Missing (NaN) Values for Text Columns
# ================================================================

print("\n" + "=" * 140)
print("          MILESTONE 2 : Fixing Missing (NaN) Values for Text Columns")
print("=" * 140)


# 1. Customer_Name
print("\nFOR CUSTOMER_NAME COLUMN :-")

print("\nBefore Cleaning:")
print(df[df["Customer_Name"].isna()].head())

df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")

print("\nAfter Cleaning:")
print(df[df["Customer_Name"] == "Unknown"].head())


# 2. Product
print("\n" + "-" * 140)
print("FOR PRODUCT COLUMN :-")

print("\nMissing Product Values Before Cleaning:")
print(df["Product"].isna().sum())

# Product missing hone par Unknown rakhenge
df["Product"] = df["Product"].fillna("Unknown")

print("\nMissing Product Values After Cleaning:")
print(df["Product"].isna().sum())


# ================================================================
# STEP 3 :- Dirty Numeric Columns
# ================================================================

print("\n" + "=" * 140)
print("          MILESTONE 3 : Dirty Numeric Columns")
print("=" * 140)


# 1. Quantity
print("\nFOR QUANTITY COLUMN :-")

print("\nBefore Fixing:")
print(df["Quantity"].head(10))

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan

df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)

df["Quantity"] = df["Quantity"].astype(int)

print("\nAfter Fixing:")
print(df["Quantity"].head(10))


# 2. Price_Per_Unit
print("\n" + "-" * 140)
print("FOR PRICE_PER_UNIT COLUMN :-")

print("\nBefore Fixing:")
print(df["Price_Per_Unit"].head(10))

df["Price_Per_Unit"] = (
    df["Price_Per_Unit"]
    .astype(str)
    .str.replace("$", "", regex=False)
)

df["Price_Per_Unit"] = df["Price_Per_Unit"].replace(
    "FREE",
    "0"
)

df["Price_Per_Unit"] = pd.to_numeric(
    df["Price_Per_Unit"],
    errors="coerce"
)

df["Price_Per_Unit"] = df["Price_Per_Unit"].fillna(
    df["Price_Per_Unit"].median()
)

print("\nAfter Fixing:")
print(df["Price_Per_Unit"].head(10))


# ================================================================
# STEP 4 :- Fixing Mixed Date Formats
# ================================================================

print("\n" + "=" * 140)
print("          MILESTONE 4 : Fixing Mixed Date Formats")
print("=" * 140)

print("\nFOR ORDER_DATE COLUMN :-")

print("\nBefore Fixing:")
print(df["Order_Date"].head(10))

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    format="mixed"
)

print("\nAfter Fixing:")
print(df["Order_Date"].head(10))

print("\nMissing/Invalid Dates:", df["Order_Date"].isna().sum())


# ================================================================
# STEP 5 :- Handling NaN Values of Payment_Status
# ================================================================

print("\n" + "=" * 140)
print("          MILESTONE 5 : Handling NaN Values of Payment_Status")
print("=" * 140)

print("\nFOR PAYMENT_STATUS COLUMN :-")

print("\nBefore Fixing:")
print(df["Payment_Status"].head(10))

df["Payment_Status"] = df["Payment_Status"].replace(
    ["nan", "NaN", "null", "None", ""],
    np.nan
)

df["Payment_Status"] = df["Payment_Status"].fillna(
    "Unknown"
)

print("\nAfter Fixing:")
print(df["Payment_Status"].head(10))


# ================================================================
# STEP 6 :- Final Analysis / Reporting
# ================================================================

print("\n" + "=" * 140)
print("                    MILESTONE 6 : Final Analysis")
print("=" * 140)


# 1. Total Sales Column

df["Total_Sales"] = (
    df["Quantity"] *
    df["Price_Per_Unit"]
)

print("\n--- Total_Sales Column Created ---")
print(
    df[
        [
            "Product",
            "Quantity",
            "Price_Per_Unit",
            "Total_Sales"
        ]
    ].head(10)
)


# 2. Product-wise Total Sales

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Product-wise Total Sales ---")
print(product_sales)


# 3. Overall Company Total Sales

overall_total_sales = df["Total_Sales"].sum()

print("\nOverall Company Total Sales :-",
      overall_total_sales)


# 4. Average Sales

average_sales = df["Total_Sales"].mean()

print("\nAverage Sales Per Transaction :-",
      average_sales)


# 5. Highest Sale

highest_sale = df["Total_Sales"].max()

print("\nHighest Single Sale :-",
      highest_sale)


# 6. Product With Highest Sales

best_product = product_sales.idxmax()

print("\nProduct With Highest Total Sales :-",
      best_product)


# ================================================================
# STEP 7 :- Final Data Check
# ================================================================

print("\n" + "=" * 140)
print("                    MILESTONE 7 : Final Data Check")
print("=" * 140)


print("\nFinal Shape :-",
      df.shape)

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)


# ================================================================
# STEP 8 :- Saving the Cleaned Data
# ================================================================

print("\n" + "=" * 140)
print("                    MILESTONE 8 : Saving the Data")
print("=" * 140)

df.to_csv(
    "Project1_fully_cleaned_data.csv",
    index=False
)

print("\nAll Data Has Been Saved Successfully !!")
print("File Name :- Project1_fully_cleaned_data.csv")