# PROJECT 2 :- Youtube Shorts Analytics Dashboard -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================================================================
# STEP 1 :- Loading and Cleaning the Data
# ================================================================

df = pd.read_csv(r"C:/Users/Rehan/Downloads/project4_youtube_shorts_analytics.csv")
print("=" * 140)
print("                    MILESTONE 1 : Loading the Data")
print("=" * 140)
print('Shape of the Data :- ', df.shape)
print('\nColumns :- ')
print(df.columns)


# ================================================================
# STEP 2 :- Creating the Dashboard Grid (2 Rows x 2 Columns)
# ================================================================

# ----------------------------------------------------------------
# 1. Topic-wise Total views bar chart
# ----------------------------------------------------------------
df["Upload_Date"] = pd.to_datetime(df['Upload_Date'])
topic_views = df.groupby('Topic')['Views']

plt.bar(df['Topic'], df['Views'], color='red', edgecolor='black', width=0.5)
plt.title('Topic-wise views line chart', fontsize= 12, fontweight= 'bold')
plt.xlabel('Topics', labelpad=10)
plt.ylabel('Views')

# ----------------------------------------------------------------
# 2. Topic-wise Average views bar chart
# ----------------------------------------------------------------
avg_topic_views = df.groupby('Topic')['Views'].mean().reset_index()
plt.figure(figsize=(8, 5))

plt.bar(avg_topic_views['Topic'], avg_topic_views['Views'], color='royalblue', edgecolor='black', width=0.5)
plt.title('Topic-wise views line chart', fontsize= 12, fontweight= 'bold')
plt.xlabel('Topics', labelpad=10)
plt.ylabel('Average Views')

plt.show()

# ----------------------------------------------------------------
# 3. Views vs Likes ka scatter plot
# ----------------------------------------------------------------
plt.scatter(df['Like_Rate'], df['Views'], color='green', alpha=0.4)
plt.title('Views vs Likes Rate', fontsize=12, fontweight='bold')
plt.xlabel('Likes Rate')
plt.ylabel('Views')
plt.grid(True, linestyle=':', alpha=0.6, color='gray')

plt.show()

# ----------------------------------------------------------------
# 4. Views distribution ka histogram
# ----------------------------------------------------------------
plt.hist(df['Views'], bins= 10, edgecolor= 'black', alpha= 0.9)
plt.title('Views distribution histogram')
plt.xlabel('Views')
plt.ylabel('Videos')

plt.show()

# ----------------------------------------------------------------
# 5. Topic-wise views ka pie chart
# ----------------------------------------------------------------
pie_chart = df.groupby('Topic')['Views'].sum()

plt.pie(pie_chart, labels= pie_chart.index, autopct='%1.1f%%', startangle=140)
plt.title('Topic-wise views pie chart')

plt.show()

# ----------------------------------------------------------------
# 6. Engagement Rate vs Views ka scatter plot
# ----------------------------------------------------------------
plt.scatter(df['Engagement_Rate'], df['Views'], color='green', alpha=0.4)
plt.title('Engagement Rate vs Views')
plt.xlabel('Engagement_Rate')
plt.ylabel('Views')
plt.grid(True, linestyle=':', alpha=0.6, color='gray')

plt.show()

# ----------------------------------------------------------------
# 7. Top 10 videos by views ka bar chart
# ----------------------------------------------------------------
largest_10 = df.nlargest(10, 'Views')
plt.figure(figsize=(8, 5))

plt.bar(largest_10['Video_No'].astype(str), largest_10['Views'], color='royalblue', edgecolor='black')
plt.title('Top 10 videos by views bar chart', fontsize= 12, fontweight= 'bold')
plt.xlabel('Videos', labelpad=10)
plt.ylabel('Views')
plt.grid(True, linestyle=':', alpha=0.6, color='gray')

plt.show()

# ----------------------------------------------------------------
# 8. Highest-view video ko chart mein annotate karo
# ----------------------------------------------------------------
top_10_videos = df.nlargest(10, 'Views').reset_index(drop=True)

plt.figure(figsize=(10, 5))

plt.bar(top_10_videos['Video_No'].astype(str), top_10_videos['Views'], color='royalblue', edgecolor='black')

highest_views = top_10_videos.loc[0, 'Views']

plt.text(0, highest_views + (highest_views * 0.02), f"⭐ Highest: {highest_views:,}", 
         ha='center', fontweight='bold', color='red', fontsize=11)

plt.title('Top 10 videos by views', fontsize=12, fontweight='bold')
plt.xlabel('Video Number')
plt.ylabel('Views')
plt.ylim(0, highest_views * 1.15) 

plt.show()

