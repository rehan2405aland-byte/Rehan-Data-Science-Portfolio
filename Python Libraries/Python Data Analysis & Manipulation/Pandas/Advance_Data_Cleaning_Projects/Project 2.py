# PROJECT 2 : CUSTOMER DATA CLEANING

import pandas as pd
import numpy as np


# STEP 1 :- Loading the Data
df = pd.read_csv(r"C:/Users/Rehan/Downloads/customer_data_dirty.txt")

print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)

print("Shape of Data :- ", df.shape)


# STEP 2 :- Cleaning the Data
print("\n" + "=" * 140)
print("                    MILESTONE 2 : Cleaning the Data")
print("=" * 140)


# 1. Identifying Missing Values
miss_values = df.isna().sum()

print("\nMissing Values :-")
print(miss_values)


# 2. Duplicate Rows
dup_rows = df.duplicated().sum()

print("\nDuplicate Rows :- ", dup_rows)


# 3. Filling / Fixing Missing Values


# A. Name Column
print("\n" + "=" * 140)
print("FOR NAME COLUMN")
print("=" * 140)

print("\nBefore Cleaning Name Column:")
print(df["name"].head())

df["name"] = df["name"].fillna("Unknown")
df["name"] = df["name"].str.strip().str.title()

print("\nAfter Cleaning Name Column:")
print(df["name"].head())


# ----------------------------------------------------------------------------


# B. Phone Column
print("\n" + "=" * 140)
print("FOR PHONE COLUMN")
print("=" * 140)

print("\nBefore Cleaning Phone Column:")
print(df["phone"].head())

df["phone"] = df["phone"].fillna("Unknown")
df["phone"] = df["phone"].astype(str).str.replace(
    " ", "", regex=False
)

print("\nAfter Cleaning Phone Column:")
print(df["phone"].head())


# ----------------------------------------------------------------------------


# C. Age Column
print("\n" + "=" * 140)
print("FOR AGE COLUMN")
print("=" * 140)

print("\nBefore Fixing Age Column:")
print(df["age"].head())

# Fix known text value
df["age"] = df["age"].replace("twenty eight", 28)

# Convert age into numeric
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

# Convert to integer
df["age"] = df["age"].astype(int)

print("\nAfter Fixing Age Column:")
print(df["age"].head())


# ----------------------------------------------------------------------------


# D. Email Column
print("\n" + "=" * 140)
print("FOR EMAIL COLUMN")
print("=" * 140)

print("\nBefore Fixing Email Column:")
print(df["email"].tail())

df["email"] = df["email"].fillna("Unknown Email")

df["email"] = df["email"].str.strip()

print("\nAfter Fixing Email Column:")
print(df["email"].tail())


# ----------------------------------------------------------------------------


# E. Gender Column
print("\n" + "=" * 140)
print("FOR GENDER COLUMN")
print("=" * 140)

print("\nBefore Fixing Gender Column:")
print(df["gender"].head())

df["gender"] = df["gender"].fillna("Unknown")

df["gender"] = df["gender"].str.strip().str.title()

df["gender"] = df["gender"].replace(
    {
        "M": "Male",
        "F": "Female"
    }
)

print("\nAfter Fixing Gender Column:")
print(df["gender"].head())


# ----------------------------------------------------------------------------


# F. Signup_Date Column
print("\n" + "=" * 140)
print("FOR SIGNUP_DATE COLUMN")
print("=" * 140)

print("\nBefore Fixing Signup_Date Column:")
print(df["signup_date"].head())

df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce",
    format="mixed"
)

print("\nAfter Fixing Signup_Date Column:")
print(df["signup_date"].head())

print(
    "\nMissing / Invalid Dates :-",
    df["signup_date"].isna().sum()
)


# ----------------------------------------------------------------------------


# G. Purchase_Amount Column
print("\n" + "=" * 140)
print("FOR PURCHASE_AMOUNT COLUMN")
print("=" * 140)

print("\nBefore Fixing Purchase_Amount Column:")
print(df["purchase_amount"].head())

# Convert different missing-value strings into NaN
df["purchase_amount"] = df["purchase_amount"].replace(
    ["nan", "NaN", " ", "null", "None"],
    np.nan
)

# Convert to numeric
df["purchase_amount"] = pd.to_numeric(
    df["purchase_amount"],
    errors="coerce"
)

# Fill missing values with median
df["purchase_amount"] = df["purchase_amount"].fillna(
    df["purchase_amount"].median()
)

print("\nAfter Fixing Purchase_Amount Column:")
print(df["purchase_amount"].head())


# ----------------------------------------------------------------------------


# H. City Column
print("\n" + "=" * 140)
print("FOR CITY COLUMN")
print("=" * 140)

print("\nBefore Fixing City Column:")
print(df["city"].head())

df["city"] = df["city"].fillna("Unknown")

df["city"] = df["city"].str.strip().str.title()

print("\nAfter Fixing City Column:")
print(df["city"].head())


# STEP 3 :- Final Analysis
print("\n" + "=" * 140)
print("                    MILESTONE 3 : Final Analysis")
print("=" * 140)


# 1. Average Customer Age
avg_age = df["age"].mean()

print(
    "\nAverage Customer Age :- ",
    round(avg_age, 2)
)


# 2. Total Purchase Amount
total_amt = df["purchase_amount"].sum()

print(
    "\nTotal Purchase Amount :- ",
    round(total_amt, 2)
)


# 3. City-wise Number of Customers
city_customers = (
    df.groupby("city")["name"]
    .count()
    .sort_values(ascending=False)
)

print("\nCity-wise Number of Customers :-")
print(city_customers)


# 4. Top 3 Customers by Purchase Amount
customers_purchase = (
    df.groupby("name")["purchase_amount"]
    .sum()
    .sort_values(ascending=False)
)

top_customers = customers_purchase.head(3)

print("\nTop 3 Customers by Purchase Amount :-")
print(top_customers)


# STEP 4 :- Final Data Check
print("\n" + "=" * 140)
print("                    MILESTONE 4 : Final Data Check")
print("=" * 140)

print("\nFinal Shape :-")
print(df.shape)

print("\nRemaining Missing Values :-")
print(df.isna().sum())

print("\nDuplicate Rows :-")
print(df.duplicated().sum())

print("\nData Types :-")
print(df.dtypes)


# STEP 5 :- Saving the Data
print("\n" + "=" * 140)
print("                    MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv(
    "Project2_fully_cleaned_data.csv",
    index=False
)

print("\nAll Data Has Been Saved Successfully !!")
print("File Name :- Project2_fully_cleaned_data.csv")