# PROJECT 3 :- Messy Sales Data with Dashboard -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================
df = pd.read_csv(r"C:/Users/Rehan/Downloads/project1_messy_sales.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)
print('Shape of the Data :- ', df.shape)
print('\nColumns :- ')
print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.info())
print(df.describe())


# ================================================================
# STEP 2 :- Fixing Missing (NaN) Values for Text Columns
# ================================================================
# 1. Customer_Name Column -
df['Customer_Name'] = df['Customer_Name'].fillna('Not Mentioned')
df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()

# 2. City Column -
df['City'] = df['City'].fillna('Not Mentioned')
df['City'] = df['City'].str.strip().str.title()

# 3. Category Column -
df['Category'] = df['Category'].fillna('Unknown')
df['Category'] = df['Category'].str.strip().str.title()

# 4. Product Column -
df['Product'] = df['Product'].fillna('Unknown')
df['Product'] = df['Product'].str.strip().str.title()

# ================================================================
# STEP 3 :- Fixing Missing (NaN) Values for Date Columns
# ================================================================
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
df.dropna(subset= ['Date'], inplace= True)

# ================================================================
# STEP 4 :- Fixing Missing (NaN) Values for Numeric Columns
# ================================================================
# 1. Quantity Column -
df['Quantity'] = df['Quantity'].replace('unknown', np.nan)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df.loc[df['Quantity'] < 0, 'Quantity'] = np.nan

df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median()) 
df['Quantity'] = df['Quantity'].astype(int)

# # 2. Price Column -
df['Price'] = pd.to_numeric(df['Price'])

df.loc[df['Price'] < 0, 'Price'] = np.nan

df['Price'] = df['Price'].fillna(df['Price'].median())

df['Price']= df['Price'].astype(int)

# 3. Discount Column -
df["Discount"] = (
    df["Discount"]
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


df["Discount"] = df["Discount"].apply(
    fix_mixed_discount
)

df["Discount"] = df["Discount"].astype(float)

# # ================================================================
# # STEP 5 :- FEATURE ENGINEERING
# # ================================================================
df['Total Sales'] = df['Quantity'] * df['Price'] * (1-df['Discount'])

# # ================================================================
# # STEP 6 :- ANALYSIS
# # ================================================================
city_sales = df.groupby('City')['Total Sales'].sum()

category_sales = df.groupby('Category')['Total Sales'].sum()

date_sales = df.groupby('Date')['Total Sales'].sum().sort_index()

product_sales = df.groupby('Product')['Total Sales'].sum()


# ================================================================
# 📄 PAGE 1 : FIRST 4 CHARTS (Grid: 2 Rows, 2 Columns)
# ================================================================
fig1, axes1 = plt.subplots(2, 2, figsize=(16, 12))

# --- CHART 1: Category-wise Sales ---
axes1[0, 0].bar(category_sales.index, category_sales.values, edgecolor='black', width=0.5)
axes1[0, 0].set_title('Category-wise Sales', fontsize=12, fontweight='bold')
axes1[0, 0].set_xlabel('Category', labelpad=10)
axes1[0, 0].set_ylabel('Total Sales')

# --- CHART 2: City-wise Sales ---
axes1[0, 1].bar(city_sales.index, city_sales.values, color='yellow', edgecolor='black', width=0.5)
axes1[0, 1].set_title('City-wise Sales', fontsize=12, fontweight='bold')
axes1[0, 1].set_xlabel('City', labelpad=10)
axes1[0, 1].set_ylabel('Total Sales')
axes1[0, 1].grid(True, linestyle=':', alpha=0.9, color='gray')

# --- CHART 3: Date-wise Sales ---
axes1[1, 0].plot(date_sales.index, date_sales.values, color='green', linewidth=1.5)
axes1[1, 0].set_title('Date-wise Sales', fontsize=12, fontweight='bold')
axes1[1, 0].set_xlabel('Date', labelpad=10)
axes1[1, 0].set_ylabel('Sales')
axes1[1, 0].grid(True, linestyle=':', alpha=0.9, color='gray')

# --- CHART 4: Category Sales distribution ---
axes1[1, 1].pie(category_sales.values, labels=category_sales.index, startangle=140, autopct='%1.1f%%')
axes1[1, 1].set_title('Category Sales distribution', fontsize=12, fontweight='bold')

plt.tight_layout()

plt.savefig('Project1_1st Page')

plt.show()


# ================================================================
# 📄 PAGE 2 : REMAINING 3 CHARTS (Grid: 2 Rows, 2 Columns)
# ================================================================
fig2, axes2 = plt.subplots(2, 2, figsize=(16, 12))

# --- CHART 5: Quantity vs Total Sales ---
axes2[0, 0].scatter(df['Quantity'], df['Total Sales'], color='green', alpha=0.4)
axes2[0, 0].set_title('Quantity vs Total Sales', fontsize=12, fontweight='bold')
axes2[0, 0].set_xlabel('Quantity')
axes2[0, 0].set_ylabel('Total Sales')
axes2[0, 0].grid(True, linestyle=':', alpha=0.6, color='gray')

# --- CHART 6: Sales distribution → histogram ---
axes2[0, 1].hist(df['Total Sales'], bins=10, edgecolor='black', alpha=0.9)
axes2[0, 1].set_title('Sales distribution → histogram', fontsize=12, fontweight='bold')
axes2[0, 1].set_xlabel('Total Sales Amount')
axes2[0, 1].set_ylabel('Frequency')
axes2[0, 1].grid(True, linestyle=':', alpha=0.9, color='gray')

# --- CHART 7: Top 5 products → bar chart ---
top_5 = product_sales.nlargest(5)
axes2[1, 0].bar(top_5.index.astype(str), top_5.values, color='royalblue', edgecolor='black')
axes2[1, 0].set_title('Top 5 products by sales bar chart', fontsize=12, fontweight='bold')
axes2[1, 0].set_xlabel('Product', labelpad=10)
axes2[1, 0].set_ylabel('Sales')
axes2[1, 0].grid(True, linestyle=':', alpha=0.9, color='gray')

axes2[1, 1].axis('off')

plt.tight_layout()

plt.savefig('Project1_2nd Page')

plt.show()  


# # ================================================================
# # STEP 7 :- Saving the Data
# # ================================================================
print("\n" + "=" * 140)
print("              MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv("Project1_fully_cleaned_data.csv",index=False)

print("\nAll Data has Successfully Saved !!")

print("File Name :- Project3_fully_cleaned_data.csv")

