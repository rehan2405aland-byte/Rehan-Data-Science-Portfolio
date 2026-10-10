# PROJECT 2 :- 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/seaborn_project2_clean_students.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())


# ================================================================
# STEP 2 :- Aggregations for Charts
# ================================================================

# 1. Department-wise average Exam Score
department_average = df.groupby('Department')['Exam_Score'].mean().reset_index()

# 2. Average Exam Score According to Study Hours
average_exam_study_hours = df.groupby('Study_Hours')['Exam_Score'].mean().reset_index()

# 3. Numerical columns ka correlation
columns_to_create = ['Study_Hours', 'Attendance', 'Assignments_Completed', 'Exam_Score']
numeric_col =  df[columns_to_create].corr()


# ================================================================
# STEP 3 :- Creating the Dashboard Grid (2 Rows x 3 Columns)
# ================================================================

fig, axes = plt.subplots(2,3, figsize=(17,10))

# 1. ---Bar Plot--- 
sns.barplot(data=department_average, x='Department', y='Exam_Score', ax=axes[0,0], palette='muted')

axes[0,0].set_title('1. Department-wise average Exam Score', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Department')
axes[0,0].set_ylabel('Average Exam Score')

axes[0,0].ticklabel_format(style='plain', axis='y')

# 2. ---Box Plot---
sns.boxplot(data=df, x='Department', y='Exam_Score', palette='Blues_r',
             hue='Department', legend=False, ax=axes[0,1])

axes[0,1].set_title('2.Department-wise Exam Score distribution', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Department')
axes[0,1].set_ylabel('Exam_Score')

axes[0,1].ticklabel_format(style='plain', axis='y')  

# 3. ---Scatter Plot---
sns.scatterplot(data=df, x='Study_Hours', y='Exam_Score', alpha=0.7, ax=axes[0,2], hue='Department')

axes[0,2].set_title('3. Study_Hours vs Exam_Score', fontsize=12, fontweight='bold')
axes[0,2].set_xlabel('Study_Hours')
axes[0,2].set_ylabel('Exam Score')

axes[0,2].ticklabel_format(style='plain', axis='y')

# 4. ---Line Plot---
sns.lineplot(data=average_exam_study_hours, x='Study_Hours', y='Exam_Score', ax=axes[1,0], color='red')

axes[1,0].set_title('4. Average Exam Score According to Study Hours', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Study Hours')
axes[1,0].set_ylabel('Exam Score')

# 5. ---Count Plot---
sns.countplot(data=df, x='Placement_Eligible', palette='Set2', ax=axes[1,1])

axes[1,1].set_title('5. Placement Eligible distribution', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Placement Eligible')
axes[1,1].set_ylabel('No. of Students')

# 6. ---Heatmap---
sns.heatmap(data=numeric_col, annot=True, cmap='coolwarm', ax=axes[1,2], fmt=".2f", linewidths=0.5)

axes[1,2].set_title('Correlation of Numerical columns', fontsize=12, fontweight='bold')

axes[1,2].tick_params(axis='x', labelsize=10)
axes[1,2].tick_params(axis='y', labelsize=10)


# ================================================================
# STEP 4 :- Layout Adjustment & Display
# ================================================================
plt.tight_layout(pad=3.0)
plt.savefig('Project2_Chart')
plt.show()
