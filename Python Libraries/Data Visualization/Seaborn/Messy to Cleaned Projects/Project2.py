
# ================================================================
# PROJECT 2 :- NETFLIX DATA CLEANING AND VISUALIZATION DASHBOARD
# Libraries: NumPy, Pandas, Matplotlib, Seaborn
# Dataset: netflix_messy_12180_rows.csv
# Total Charts: 8 (2 Pages, 4 Charts Each)
# ================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ================================================================
# STEP 1 :- LOADING AND INSPECTING THE DATA
# ================================================================

df = pd.read_csv(
    r"C:/Users/Rehan/Downloads/netflix_messy_12180_rows.csv"
)

print("=" * 100)
print("MILESTONE 1 : LOADING THE DATA")
print("=" * 100)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include='all'))

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ================================================================
# STEP 2 :- REMOVING DUPLICATES
# ================================================================

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print("\nShape After Removing Duplicates:")
print(df.shape)


# ================================================================
# STEP 3 :- CLEANING TEXT COLUMNS
# ================================================================

# 1. Title
df['title'] = df['title'].str.strip().str.title()

# 2. Type
df['type'] = df['type'].str.strip().str.title()

# Standardize content type categories
df['type'] = df['type'].replace({
    'Movie': 'Movie',
    'Tv Show': 'TV Show',
    'Tv show': 'TV Show'
})

# 3. Director
df['director'] = (
    df['director']
    .fillna('Not Mentioned')
    .str.strip()
    .str.title()
)

# 4. Country
df['country'] = (
    df['country']
    .fillna('Not Mentioned')
    .str.strip()
    .str.title()
)

# 5. Genre
df['genre'] = (
    df['genre']
    .fillna('Not Mentioned')
    .str.strip()
    .str.title()
)

# 6. Rating
df['rating'] = (
    df['rating']
    .fillna('Not Given')
    .str.strip()
    .replace('', 'Not Given')
)


# ================================================================
# STEP 4 :- CLEANING DATE COLUMN
# ================================================================

# Parse mixed date formats
df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='mixed',
    errors='coerce'
)

# Count invalid or missing dates before dropping
print("\nInvalid/Missing Dates:")
print(df['date_added'].isna().sum())

# Remove rows where date is unavailable
df.dropna(subset=['date_added'], inplace=True)

# Extract year for time-based analysis
df['date_added_year'] = df['date_added'].dt.year


# ================================================================
# STEP 5 :- CLEANING RELEASE YEAR
# ================================================================

df['release_year'] = pd.to_numeric(
    df['release_year'],
    errors='coerce'
)

# Treat impossible years as missing
invalid_year = ~df['release_year'].between(1900, 2026)

df.loc[invalid_year, 'release_year'] = np.nan

# Fill invalid years with median
year_median = df['release_year'].median()

df['release_year'] = df['release_year'].fillna(
    year_median
).round().astype(int)


# ================================================================
# STEP 6 :- CLEANING DURATION
# ================================================================

# Extract numerical duration
df['duration'] = pd.to_numeric(
    df['duration']
    .astype('string')
    .str.extract(r'(\d+)', expand=False),
    errors='coerce'
)

# Invalid/non-positive duration values
df.loc[df['duration'] <= 0, 'duration'] = np.nan

# Fill missing duration using median for each content type
df['duration'] = df.groupby('type')['duration'].transform(
    lambda series: series.fillna(series.median())
)

# Fallback in case a group has no valid duration
df['duration'] = df['duration'].fillna(
    df['duration'].median()
)


# ================================================================
# STEP 7 :- CLEANING VOTES AND SCORE
# ================================================================

# 1. Votes
df['votes'] = pd.to_numeric(
    df['votes'],
    errors='coerce'
)

df.loc[df['votes'] <= 0, 'votes'] = np.nan

df['votes'] = df['votes'].fillna(
    df['votes'].median()
).round().astype('int64')


# 2. Score
df['score'] = pd.to_numeric(
    df['score'],
    errors='coerce'
)

# Valid scores are between 1 and 10
df.loc[
    ~df['score'].between(1, 10),
    'score'
] = np.nan

df['score'] = df['score'].fillna(
    df['score'].median()
)


# ================================================================
# STEP 8 :- FINAL DATA QUALITY CHECK
# ================================================================

print("\n" + "=" * 100)
print("MILESTONE 2 : CLEANED DATA")
print("=" * 100)

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nRemaining Missing Values:")
print(df.isna().sum())

print("\nRemaining Duplicate Rows:")
print(df.duplicated().sum())

print("\nCleaned Data Types:")
print(df.dtypes)

print("\nCleaned Data Preview:")
print(df.head())


# Save cleaned dataset
df.to_csv(
    r"C:/Users/Rehan/Downloads/netflix_cleaned.csv",
    index=False
)

print("\nCleaned CSV saved successfully!")


# ================================================================
# STEP 9 :- AGGREGATIONS FOR CHARTS
# ================================================================

# 1. Movies vs TV Shows
type_counts = df['type'].value_counts()

# 2. Top 10 Countries
top_10_countries = (
    df[df['country'] != 'Not Mentioned']['country']
    .value_counts()
    .head(10)
)

# 3. Top 10 Genres
top_10_genres = (
    df[df['genre'] != 'Not Mentioned']['genre']
    .value_counts()
    .head(10)
)

# 4. Rating Distribution
rating_counts = df['rating'].value_counts()

# 5. Movie Duration
movie_df = df[df['type'] == 'Movie'].copy()

# 6. Genre vs Content Type
top_genres = top_10_genres.index

genre_vs_type = pd.crosstab(
    df[df['genre'].isin(top_genres)]['genre'],
    df[df['genre'].isin(top_genres)]['type']
)

# 7. Content Added Over Time
yearly_content = (
    df.groupby('date_added_year')
    .size()
    .sort_index()
)

# 8. Score Distribution
valid_scores = df['score'].dropna()


# ================================================================
# STEP 10 :- DASHBOARD PAGE 1
# Charts 1, 2, 3, 4
# ================================================================

sns.set_theme(style='whitegrid')

fig, axes = plt.subplots(
    2, 2,
    figsize=(18, 12)
)

fig.suptitle(
    'NETFLIX DATA ANALYSIS DASHBOARD - PAGE 1',
    fontsize=18,
    fontweight='bold'
)


# CHART 1 :- Movies vs TV Shows (Count Plot)

sns.countplot(
    data=df,
    x='type',
    order=['Movie', 'TV Show'],
    hue='type',
    legend=False,
    ax=axes[0, 0]
)

axes[0, 0].set_title(
    '1. Movies vs TV Shows',
    fontweight='bold'
)

axes[0, 0].set_xlabel('Content Type')
axes[0, 0].set_ylabel('Number of Titles')


# CHART 2 :- Top 10 Countries (Horizontal Bar Chart)

sns.barplot(
    x=top_10_countries.values,
    y=top_10_countries.index,
    hue=top_10_countries.index,
    legend=False,
    ax=axes[0, 1]
)

axes[0, 1].set_title(
    '2. Top 10 Countries',
    fontweight='bold'
)

axes[0, 1].set_xlabel('Number of Titles')
axes[0, 1].set_ylabel('Country')


# CHART 3 :- Top 10 Genres (Horizontal Bar Chart)

sns.barplot(
    x=top_10_genres.values,
    y=top_10_genres.index,
    hue=top_10_genres.index,
    legend=False,
    ax=axes[1, 0]
)

axes[1, 0].set_title(
    '3. Top 10 Genres',
    fontweight='bold'
)

axes[1, 0].set_xlabel('Number of Titles')
axes[1, 0].set_ylabel('Genre')


# CHART 4 :- Rating Distribution (Count Plot)

sns.countplot(
    data=df,
    y='rating',
    order=df['rating'].value_counts().index,
    hue='rating',
    legend=False,
    ax=axes[1, 1]
)

axes[1, 1].set_title(
    '4. Rating Distribution',
    fontweight='bold'
)

axes[1, 1].set_xlabel('Number of Titles')
axes[1, 1].set_ylabel('Rating')


plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig('Project2_Chart_Page1')

# ================================================================
# STEP 11 :- DASHBOARD PAGE 2
# Charts 5, 6, 7, 8
# ================================================================

fig, axes = plt.subplots(
    2, 2,
    figsize=(18, 12)
)

fig.suptitle(
    'NETFLIX DATA ANALYSIS DASHBOARD - PAGE 2',
    fontsize=18,
    fontweight='bold'
)


# CHART 5 :- Movie Duration Distribution (Histogram + KDE)

sns.histplot(
    data=movie_df,
    x='duration',
    bins=25,
    kde=True,
    ax=axes[0, 0]
)

axes[0, 0].set_title(
    '5. Movie Duration Distribution',
    fontweight='bold'
)

axes[0, 0].set_xlabel('Duration (Minutes)')
axes[0, 0].set_ylabel('Number of Movies')


# CHART 6 :- Genre vs Content Type (Heatmap)

sns.heatmap(
    data=genre_vs_type,
    annot=True,
    fmt='d',
    cmap='coolwarm',
    linewidths=0.5,
    ax=axes[0, 1]
)

axes[0, 1].set_title(
    '6. Genre vs Content Type',
    fontweight='bold'
)

axes[0, 1].set_xlabel('Content Type')
axes[0, 1].set_ylabel('Genre')


# CHART 7 :- Content Added Over Time (Line Chart)

sns.lineplot(
    x=yearly_content.index,
    y=yearly_content.values,
    marker='o',
    ax=axes[1, 0]
)

axes[1, 0].set_title(
    '7. Content Added Over Time',
    fontweight='bold'
)

axes[1, 0].set_xlabel('Year Added')
axes[1, 0].set_ylabel('Number of Titles')

axes[1, 0].tick_params(
    axis='x',
    rotation=45
)


# CHART 8 :- Content Score Distribution (Histogram + KDE)

sns.histplot(
    x=valid_scores,
    bins=20,
    kde=True,
    ax=axes[1, 1]
)

axes[1, 1].set_title(
    '8. Content Score Distribution',
    fontweight='bold'
)

axes[1, 1].set_xlabel('Score (1 to 10)')
axes[1, 1].set_ylabel('Frequency')


plt.tight_layout(pad=3.0)

plt.savefig('Project2_Chart_Page2')

plt.show()


# ================================================================
# STEP 12 :- Saving the Data
# ================================================================
print("\n" + "=" * 140)
print("              MILESTONE 12 : Saving the Data")
print("=" * 140)

df.to_csv("Project2_fully_cleaned_data.csv",index=False)

print("\nAll Data has Successfully Saved !!")

print("File Name :- Project2_fully_cleaned_data.csv")
# ================================================================
# PROJECT COMPLETED
# ================================================================

print("\n" + "=" * 100)
print("PROJECT 2 COMPLETED SUCCESSFULLY")
print("=" * 100)

print("1. Dataset loaded")
print("2. Duplicate rows removed")
print("3. Text columns cleaned")
print("4. Dates and numerical columns cleaned")
print("5. Cleaned CSV exported")
print("6. Dashboard Page 1 created")
print("7. Dashboard Page 2 created")
print("8. Total charts created: 8")
