# PROJECT 1 :- 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/seaborn_fitness_lifestyle_12000.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())


# ================================================================
# STEP 2 :- Fixing Missing (NaN) Values for Numeric Columns
# ================================================================

# 1. Date Column-
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Date'] = df['Date'].dt.date

# 2. Mood Column-
df['Mood'] = df['Mood'].fillna('Good')


# ================================================================
# STEP 3 :- Fixing Missing (NaN) Values for Numeric Columns
# ================================================================

# 1. Sleep_Hours Column-
df = df.dropna(subset=['Sleep_Hours'])

# 2. Water_Intake_L Column-
df['Water_Intake_L'] = df['Water_Intake_L'].fillna(df['Water_Intake_L'].median())

# 3. Heart_Rate_Avg Column-
df = df.dropna(subset=['Heart_Rate_Avg'])

# 4. Workout_Intensity Column-
df = df.dropna(subset=['Workout_Intensity'])


# ================================================================
# STEP 2 :- Aggregations for Charts
# ================================================================

# 1. Distribution of Calories_Burned per Mood -
calories_burned_mood = df.groupby('Mood')['Calories_Burned'].sum().reset_index()

# 2. Date-wise Stress Level Distribution -
date_wise_stress = df.groupby('Date')['Stress_Level'].sum().reset_index()

# 3. Correlation of Health Matrix -
num_corr = ['Age', 'Workout_Duration_Min', 'Steps', 'Calories_Burned', 'Sleep_Hours', 'Water_Intake_L', 'Heart_Rate_Avg', 'Stress_Level']
health_matrix = df[num_corr].corr()

columns_to_plot = ['Age', 'Workout_Duration_Min', 'Steps', 'Calories_Burned', 'Sleep_Hours']


# ================================================================
# STEP 4 :- Creating the Dashboard Grid (2 Rows x 2 Columns)
#                     Page 1
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(17,10))

# 1. Histplot(Steps wise Distribution) -
sns.histplot(data=df, x='Steps', color='teal', ax=axes[0,0], edgecolor='white', kde=True)

axes[0,0].set_title('1. Steps wise Distribution', fontweight='bold', fontsize=12)
axes[0,0].set_xlabel('Steps')

# 2. Boxplot(City wise Workout_Duration_Min Distribution) -
sns.boxplot(data=df, x='City', y='Workout_Duration_Min', palette='Blues_r', hue='City', legend=False, ax=axes[0,1])

axes[0,1].set_title('2. City wise Workout_Duration_Min Distribution', fontweight='bold', fontsize=12)
axes[0,1].set_xlabel('City')
axes[0,1].set_ylabel('Workout Duration Min')

# 3. Countplot(Activity_Type Distribution)
sns.countplot(data=df, x='Activity_Type', palette='Set2', ax=axes[1,0])

axes[1,0].set_title('3. Activity_Type Distribution', fontweight='bold', fontsize=12)
axes[1,0].set_xlabel('Activity_Type')
axes[1,0].set_ylabel('No. of Peoples')

# 4. Barplot(Distribution of Calories Burned per Mood)
sns.barplot(data=calories_burned_mood, x='Mood', y='Calories_Burned', ax=axes[1,1], palette='muted')

axes[1,1].set_title('4. Distribution of Calories Burned per Mood', fontweight='bold', fontsize=12)
axes[1,1].set_xlabel('Mood')
axes[1,1].set_ylabel('Calories Burned')

plt.savefig('Project1_Chart_Page1')


# ================================================================
# STEP 4 :- Creating the Dashboard Grid (2 Rows x 3 Columns)
#                     Page 2
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(17,10))

# 1. Scatterplot(Workout_Duration_Min vs Calories_Burned)
sns.scatterplot(data=df, x='Workout_Duration_Min', y='Calories_Burned', hue='Activity_Type', alpha=0.5, ax=axes[0,0], palette='viridis')

axes[0,0].set_title('1. Workout_Duration_Min vs Calories_Burned', fontweight='bold', fontsize=12)
axes[0,0].set_xlabel('Workout Duration Min')
axes[0,0].set_ylabel('Calories Burned')

# 2. Lineplot(Date-wise Stress Level Distribution)
sns.lineplot(data=date_wise_stress, x='Date', y='Stress_Level', ax=axes[0,1], color='red')

axes[0,1].set_title('2. Date-wise Stress Level Distribution', fontweight='bold', fontsize=12)
axes[0,1].set_xlabel('Date')
axes[0,1].set_ylabel('Stress Level')

# 3. Heatmap(Correlation of Health Matrix)
sns.heatmap(data=health_matrix, annot=True, cmap='coolwarm', ax=axes[1,0], fmt=".2f", linewidths=0.5)

axes[1,0].set_title('3. Correlation of Health Matrix', fontsize=12, fontweight='bold')

axes[1,0].tick_params(axis='x', labelsize=10)
axes[1,0].tick_params(axis='y', labelsize=10)

plt.tight_layout(pad=3.0)
plt.savefig('Project1_Chart_Page2')
plt.show()


# ================================================================
# STEP 5 :- Creating the Standalone Pairplot 
#                     Page 3 (Final Plot)
# ================================================================
# 4. Pairplot -
sns.pairplot(data=df[columns_to_plot + ['Gender']], hue='Gender', palette='coolwarm', diag_kind='kde')

plt.savefig('Project1_Chart_Page3')
plt.show()


# ================================================================
# STEP 7 :- Saving the Data
# ================================================================
print("\n" + "=" * 140)
print("              MILESTONE 5 : Saving the Data")
print("=" * 140)

df.to_csv("Project1_fully_cleaned_data.csv",index=False)

print("\nAll Data has Successfully Saved !!")

print("File Name :- Project1_fully_cleaned_data.csv")