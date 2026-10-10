# PROJECT 1 :- Sales Analytics Dashboard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/project1_sales_dashboard.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)
print('Shape of the Data :- ', df.shape)
print('\nColumns :- ')
print(df.columns)

# Data Cleaning & Feature Engineering
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Calculate Total Sales
df['Total Sales'] = df['Quantity'] * df['Price'] * (1 - df['Discount'])

# Aggregations for Charts
weekly_sales = df.set_index('Date').resample('W')['Total Sales'].sum().reset_index()
category_sales = df.groupby('Category')['Total Sales'].sum().reset_index()
city_sales = df.groupby('City')['Total Sales'].sum().reset_index()


# ================================================================
# STEP 2 :- Creating the Dashboard Grid (2 Rows x 2 Columns)
# ================================================================

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 20))
fig.suptitle('Project 1: Comprehensive Sales Dashboard (2026)', fontsize=18, fontweight='bold', y=0.98)

# ----------------------------------------------------------------
# 1. Weekly Sales Line Chart (Top-Left)
# ----------------------------------------------------------------
axes[2, 0].plot(weekly_sales['Date'], weekly_sales['Total Sales'], marker='o', color='purple', linestyle='-', linewidth=2)
axes[2, 0].set_title('Weekly Sales Trend', fontsize=12, fontweight='bold')
axes[2, 0].set_xlabel('Week Ending Date', labelpad=10)
axes[2, 0].set_ylabel('Total Sales ($)')
axes[2, 0].grid(True, linestyle='--', alpha=0.5)

# X-axis ke labels har 2 hafte baad dikhane aur ghumane ke liye
axes[2, 0].set_xticks(weekly_sales['Date'][::2])
axes[2, 0].tick_params(axis='x', rotation=30)


# ----------------------------------------------------------------
# 2. Category-wise Sales Bar Chart (Top-Right)
# ----------------------------------------------------------------
axes[0, 1].bar(category_sales['Category'], category_sales['Total Sales'], color='royalblue', edgecolor='black', width=0.5)
axes[0, 1].set_title('Category Sales Trend', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Total Sales ($)')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)


# ----------------------------------------------------------------
# 3. City-wise Sales Bar Chart (Bottom-Left)
# ----------------------------------------------------------------
axes[1, 1].bar(city_sales['City'], city_sales['Total Sales'], color='yellow', edgecolor='black', width=0.5) # Yellow color set
axes[1, 1].set_title('City Sales Trend', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('City')
axes[1, 1].set_ylabel('Total Sales ($)')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5) 


# ----------------------------------------------------------------
# 4. Category Sales Distribution Pie Chart (Bottom-Right)
# ----------------------------------------------------------------
# Fixed: labels parameter add kiya taaki categories ke naam pie me dikhein
axes[1,0].pie(category_sales['Total Sales'], labels=category_sales['Category'], autopct='%1.1f%%', startangle=140)
axes[1,0].set_title('Category Sales Distribution', fontsize=12, fontweight='bold')


# ----------------------------------------------------------------
# 5. Quantity vs Total Sales ka scatter plot (Bottom-Right)
# ----------------------------------------------------------------
axes[0, 0].scatter(df['Quantity'], df['Total Sales'], color='green', alpha=0.4)
axes[0, 0].set_title('Quantity vs Total Sales', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Quantity')
axes[0, 0].set_ylabel('Total Sales')
axes[0, 0].grid(True, linestyle=':', alpha=0.6, color='gray')

axes[2, 1].axis('off')

# ================================================================
# STEP 3 :- Layout Adjustment & Display
# ================================================================
plt.subplots_adjust(
    left=0.08,     
    right=0.95,    
    top=0.90,      
    bottom=0.05,   
    wspace=0.25,   
    hspace=0.40    
)
# Saving the Charts-
plt.savefig('Sales Analytics Dashboard')

plt.show()
