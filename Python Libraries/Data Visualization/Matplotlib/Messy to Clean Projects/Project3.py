# PROJECT 3 :- SALES DASHBOARD -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================
df = pd.read_csv(r"C:/Users/Rehan/Downloads/project3_messy_sales_500_rows.csv")
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
# 1. Removing Duplicate Rows -
df.drop_duplicates(inplace=True)

# 2. Customer_Name Column -
df['Customer_Name'] = df['Customer_Name'].str.strip()
df['Customer_Name'] = df['Customer_Name'].fillna('Not Mentioned')
df['Customer_Name'] = df['Customer_Name'].str.title()

# 3. City Column -
df['City'] = df['City'].str.strip()
df['City'] = df['City'].fillna('Not Mentioned')
df['City'] = df['City'].str.title()

# 4. Category Column -
df['Category'] = df['Category'].str.strip()
df['Category'] = df['Category'].fillna('Unknown')
df['Category'] = df['Category'].str.title()

# 5. Product Column -
df['Product'] = df['Product'].str.strip()
df['Product'] = df[ 'Product'].fillna('Unknown')
df['Product'] = df['Product'].str.title()


# ================================================================
# STEP 2 :- Fixing Missing (NaN) Values for Numeric Columns
# ================================================================
# 1. Date Column -
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset= ['Date'], inplace=True)

# 2. Quantity Column -
df['Quantity'] = df['Quantity'].replace('unknown', np.nan)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df.loc[df['Quantity'] < 0, 'Quantity'] = np.nan

df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['Quantity'] = df['Quantity'].astype(int)

# 3. Price Column -
df['Price'] = df['Price'].replace('unknown', np.nan)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df.loc[df['Price'] < 0, 'Price'] = np.nan

df['Price'] = df['Price'].fillna(df['Price'].median())
df['Price'] = df['Price'].astype(int)

# 3. Discount Column -
df['Discount'] = (
    df['Discount']
    .astype(str)
    .str.strip()
)


def fix_mixed_discount(val):

    if pd.isna(val):
        return 0.0

    val = str(val).strip()

    if val.lower() in [
        'nan',
        'null',
        'none',
        ''
    ]:
        return 0.0

    # Percentage values
    if '%' in val:

        val_cleaned = float(
            val.replace('%', '')
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


df['Discount'] = df['Discount'].apply(
    fix_mixed_discount
)

df['Discount'] = df['Discount'].astype(float)
print(df.isna().sum())


# ================================================================
# STEP 3 :- FEATURE ENGINEERING
# ================================================================
df['Total_Sales'] = df['Price'] * df['Quantity'] * (1-df['Discount'])

# ================================================================
# STEP 5 :- ANALYSIS
# ================================================================
category_wise_sales = df.groupby('Category')['Total_Sales'].sum()

city_wise_sales = df.groupby('City')['Total_Sales'].sum()

date_wise_sales = df.groupby('Date')['Total_Sales'].sum()
# ================================================================
# 📄 CREATING DASHBOARD : 4 CHARTS (Grid: 2 Rows, 2 Columns)
# ================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

plt.subplots_adjust(wspace=0.4, hspace=0.4)

# --- CHART 1: Category-wise Sales ---
axes[0,0].bar(category_wise_sales.index, category_wise_sales.values, color='royalblue', edgecolor='black', width=0.5)

axes[0,0].set_title('1. Category-wise Sales', color='black', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Category')
axes[0,0].set_ylabel('Total Sales')

axes[0,0].grid(True, linestyle=':', alpha=0.9, color='gray')

# --- CHART 2: City-wise Sales ---
axes[0,1].bar(city_wise_sales.index, city_wise_sales.values, color='orange', edgecolor='black', width=0.5)

axes[0,1].set_title('2. City-wise Sales', color='black', fontweight='bold', fontsize=12)
axes[0,1].set_xlabel('City')
axes[0,1].set_ylabel('Total Sales')

axes[0,1].grid(True, linestyle=':', alpha=0.9, color='gray')

# --- CHART 3: Date-wise Sales ---
axes[1,0].plot(date_wise_sales.index, date_wise_sales.values, color='green', linewidth=1.5)

axes[1,0].set_title('2. Date-wise Sales', color='black', fontweight='bold', fontsize=12)
axes[1,0].set_xlabel('Dates')
axes[1,0].set_ylabel('Total_Sales')

axes[1,0].grid(True, linestyle=':', alpha=0.9, color='gray')

axes[1,0].tick_params(axis='x', rotation=30)

# --- CHART 4: Quantity vs Total Sales ---
axes[1,1].scatter(df['Quantity'], df['Total_Sales'], color='red', alpha=0.4)

axes[1,1].set_title('3. Quantity vs Total Sales', color='black', fontweight='bold', fontsize=12)
axes[1,1].set_xlabel('Quantity')
axes[1,1].set_ylabel('Total Sales')

axes[1,1].grid(True, linestyle=':', alpha=0.9, color='gray')


# ================================================================
# STEP 6 :- Saving the Charts
# ================================================================
plt.savefig('Project3_Chart.png')
plt.show()


# ================================================================
# STEP 7 :- Saving the Data
# ================================================================
print("\n" + "=" * 140)
print("              MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv("Project3_fully_cleaned_data.csv",index=False)

print("\nAll Data has Successfully Saved !!")

print("\nFile Name :- Project3_fully_cleaned_data.csv")