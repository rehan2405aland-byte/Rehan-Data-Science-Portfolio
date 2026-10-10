# PROJECT 1 :- 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/seaborn_project1_clean_sales.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())


# ================================================================
# STEP 2 :- Feature Engennering & Inserting New Column
# ================================================================

#--- Date Column --- 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# --- Inserting New Column (Total Sales) ---
df['Total Sales'] = df['Sales'] * df['Quantity']
print(';Total Sales', df['Total Sales'])


# ================================================================
# STEP 3 :- Aggregations for Charts
# ================================================================

# 1. Product-wise total Sales :-
product_wise_sales = df.groupby('Product')['Total Sales'].sum().reset_index()

# 2. City-wise number of sales :-
city_wise_sales = df.groupby('City').size().reset_index(name='Number of Sales')

# 3. Correlation of Numerical columns :-
columns_to_create = ['Sales', 'Profit', 'Customer_Rating', 'Quantity']
numeric_corr = df[columns_to_create].corr()


# ================================================================
# STEP 4 :- Creating the Dashboard Grid (2 Rows x 3 Columns)
# ================================================================

fig, axes = plt.subplots(2, 3, figsize=(17,10)) 

# 1. Product-wise total Sales :-
sns.barplot(data=product_wise_sales, x='Product', y='Total Sales', ax=axes[0,0], palette='muted')

axes[0,0].set_title('Product-wise total Sales', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Products')
axes[0,0].set_ylabel('Total Sales')

axes[0,0].ticklabel_format(style='plain', axis='y')
axes[0,0].tick_params(axis='x', rotation=30)

# 2. City-wise number of sales :-
sns.barplot(data=city_wise_sales, x='City', y='Number of Sales', palette='viridis', ax=axes[0,1])

axes[0,1].set_title('City-wise number of sales', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Cities')
axes[0,1].set_ylabel('Number of Sales')

axes[0,1].ticklabel_format(style='plain', axis='y')
axes[0,1].tick_params(axis='x', rotation=30)

# 3. Product-wise Profit distribution :-
sns.boxplot(data=df, x='Product', y='Profit', palette='Blues_r', hue='Product', legend=False, ax=axes[0,2])

axes[0,2].set_title('Product-wise Profit distribution', fontsize=12, fontweight='bold')
axes[0,2].set_xlabel('Product')
axes[0,2].set_ylabel('Profit')

axes[0,2].tick_params(axis='x', rotation=45)
axes[0,2].ticklabel_format(style='plain', axis='y')

# 4. Customer Rating distribution :-
sns.histplot(data=df, x='Customer_Rating', color='teal', ax=axes[1,0], edgecolor='white', kde=True)

axes[1,0].set_title('Customer Rating distribution', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Customer Rating')

# 5. Sales vs Profit :-
sns.scatterplot(data=df, x='Sales', y='Profit', alpha=0.7, ax=axes[1,1])

axes[1,1].set_title('Sales vs Profit', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Sales')
axes[1,1].set_ylabel('Profit')

axes[1,1].ticklabel_format(style='plain', axis='y')

# 6. Correlation of Numerical columns :-
sns.heatmap(data=numeric_corr, annot=True, cmap='coolwarm', ax=axes[1,2], fmt=".2f", linewidths=0.5)

axes[1,2].set_title('Correlation of Numerical columns', fontsize=12, fontweight='bold')

axes[1,2].tick_params(axis='x', labelsize=10)
axes[1,2].tick_params(axis='y', labelsize=10)


# ================================================================
# STEP 3 :- Layout Adjustment & Display
# ================================================================
plt.savefig('Project1_Chart')
plt.tight_layout(pad=3.0)
plt.show()