# PROJECT 3 :- Messy Data of Students Performance -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================
df = pd.read_csv(r"C:/Users/Rehan/Downloads/project2_messy_student_performance.csv")
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

# 2. Student_Name Column -
df['Student_Name'] = df['Student_Name'].fillna('Not Mentioned')
df['Student_Name'] = df['Student_Name'].str.strip().str.title()

# 3. Gender Column -
df.dropna(subset=['Gender'], inplace=True)
df['Gender'] = df['Gender'].str.strip().str.title()
df['Gender'] = df['Gender'].replace('F','Female')
df['Gender'] = df['Gender'].replace('M','Male')
df['Gender'] = df['Gender'].str.title()

# 4. Course Column -
df.dropna(subset=['Course'], inplace=True)
df['Course'] = df['Course'].str.upper()

# ================================================================
# STEP 3 :- Fixing Missing (NaN) Values for Numeric Columns
# ================================================================
# 1. Study_Hours Column -
df['Study_Hours'] = pd.to_numeric(df['Study_Hours'], errors='coerce')

df.loc[df['Study_Hours'] < 0, 'Study_Hours'] = np.nan

df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].median())

df['Study_Hours'] = df['Study_Hours'].round().astype(int)

# 2. Attendance Column -
df['Attendance'] = df['Attendance'].astype(str).str.replace('%', '')
df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')

df.loc[(df['Attendance'] > 100) | (df['Attendance'] < 0), 'Attendance'] = np.nan
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())

df['Attendance'] = df['Attendance'].round().astype(int)

# 3. Marks Columns -

# Maths Column -
df['Maths'] = pd.to_numeric(df['Maths'], errors='coerce')

df.loc[(df['Maths'] > 100) | (df['Maths'] < 0), 'Maths'] = np.nan
df['Maths'] = df['Maths'].fillna(df['Maths'].median())

df['Maths'] = df['Maths'].round().astype(int)

# Programming Column -
df['Programming'] = pd.to_numeric(df['Programming'], errors='coerce')

df.loc[(df['Programming'] > 100) | (df['Programming'] < 0), 'Programming'] = np.nan
df['Programming'] = df['Programming'].fillna(df['Programming'].median())

df['Programming'] = df['Programming'].round().astype(int)

# Database Column -
df['Database'] = pd.to_numeric(df['Database'], errors='coerce')

df.loc[(df['Database'] > 100) | (df['Database'] < 0), 'Database'] = np.nan
df['Database'] = df['Database'].fillna(df['Database'].median())

df['Database'] = df['Database'].round().astype(int)

# English Column -
df['English'] = pd.to_numeric(df['English'], errors='coerce')

df.loc[(df['English'] > 100) | (df['English'] < 0), 'English'] = np.nan
df['English'] = df['English'].fillna(df['English'].median())

df['English'] = df['English'].round().astype(int)
#print(df.isnull().sum())

# ================================================================
# STEP 4 :- Inserting New Columns
# ================================================================

# 1. Total Column -
df['Total Marks'] = df['Maths'] + df['Programming'] + df['Database'] + df['English']

# 2. Percentage Column -
df['Percentage'] = (df['Maths'] + df['Programming'] + df['Database'] + df['English']) / 400 * 100
df['Percentage'] = df['Percentage'].round(2)

# 3. Performance Column -
bins = [0, 50, 75, 90, 100]
labels = ['Needs Improvement', 'Average', 'Good', 'Excellent']
df['Performance'] = pd.cut(df['Percentage'], bins=bins, labels=labels, include_lowest=True)


# ================================================================
# STEP 4 :- ANALYSIS
# ================================================================
weights = np.ones_like(df['Percentage']) * 100 / len(df['Percentage'])

course_wise_avg = df.groupby('Course')['Percentage'].mean()

subjects_list = ['Maths', 'Programming', 'Database', 'English']
subject_wise_avg = df[subjects_list].mean()

gender_wise_avg =  df.groupby('Gender')['Percentage'].mean()

course_wise = df['Course'].value_counts()

performance_category = df.groupby('Performance')['Percentage'].sum()
# ================================================================
# 📄 PAGE 1 : FIRST 4 CHARTS (Grid: 2 Rows, 2 Columns)
# ================================================================
fig1, axes = plt.subplots(2, 2, figsize=(16, 12))

plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.tight_layout()

#--- CHART 1: Percentage distribution Histogram ---
axes[0,0].hist(df['Total Marks'], bins=10, weights=weights, edgecolor='black', alpha=0.9)

axes[0,0].set_title('1. Percentage distribution', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Total Marks (out of 400)')
axes[0,0].set_ylabel('Percentage of Students (%)')

axes[0,0].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 2: Course-wise average percentage Bar Chart ---
axes[0,1].bar(course_wise_avg.index, course_wise_avg.values, color='yellow', edgecolor='black', width=0.5)

axes[0,1].set_title('2. Course-wise average percentage', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Course')
axes[0,1].set_ylabel('Percentage')
axes[0,1].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 3: Study Hours vs Percentage Scatter plot ---
axes[1,0].scatter(df['Study_Hours'], df['Percentage'], color='green', alpha=0.4)

axes[1,0].set_title('3. Study Hours vs Percentage Scatter Plot', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Study Hours')
axes[1,0].set_ylabel('Percentage')
axes[1, 0].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 4: Attendance vs Percentage Scatter plot ---
axes[1,1].scatter(df['Attendance'], df['Percentage'], color='red', alpha=0.4)

axes[1,1].set_title('4. Attendance vs Percentage Scatter Plot', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Attendance')
axes[1,1].set_ylabel('Percentage')
axes[1,1].grid(True, linestyle=':', alpha=0.9, color='gray')

plt.tight_layout()

# Saving the Chart :-
plt.savefig('Project2_1st Page')
plt.show()

# ================================================================
# 📄 PAGE 2 : FIRST 4 CHARTS (Grid: 2 Rows, 2 Columns)
# ================================================================
fig1, axes = plt.subplots(2, 2, figsize=(16, 12))

plt.subplots_adjust(wspace=0.4, hspace=0.4)

#--- CHART 1: Subject-wise average marks Bar Chart ---
axes[0,0].bar(subject_wise_avg.index, subject_wise_avg.values, color='purple', edgecolor='black', width=0.5)

axes[0,0].set_title('1. Subject-wise average percentage', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Subject')
axes[0,0].set_ylabel('Percentage')
axes[0,0].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 2: Gender-wise average percentage Bar Chart ---
axes[0,1].bar(gender_wise_avg.index, gender_wise_avg.values, color='orange', edgecolor='black', width=0.5)

axes[0,1].set_title('2. Gender-wise average percentage Bar Chart', color='black', fontweight='bold', fontsize=12)
axes[0,1].set_xlabel('Gender')
axes[0,1].set_ylabel('Percentage')
axes[0,1].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 3: Course-wise student count Bar Chart ---
axes[1,0].bar(course_wise.index, course_wise.values, color='teal', edgecolor='black', width=0.5)

axes[1,0].set_title('3. Course-wise student count Bar Chart', color='black', fontweight='bold', fontsize=12)
axes[1,0].set_xlabel('Course')
axes[1,0].set_ylabel('No. of Students')
axes[1,0].grid(True, linestyle=':', alpha=0.9, color='gray')

#--- CHART 4: Performance category distribution Pie Chart ---
axes[1,1].pie(performance_category.values, labels=performance_category.index, startangle=140, autopct='%1.1f%%')
axes[1,1].set_title('4. Performance category distribution', fontsize=12, fontweight='bold')

# Saving the Chart :-
plt.tight_layout()

plt.savefig('Project2_2nd Page')
plt.show()

# ================================================================
# STEP 5 :- Saving the Data
# ================================================================
print("\n" + "=" * 140)
print("              MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv("Project2_fully_cleaned_data.csv",index=False)

print("\nAll Data has Successfully Saved !!")

print("File Name :- Project2_fully_cleaned_data.csv")