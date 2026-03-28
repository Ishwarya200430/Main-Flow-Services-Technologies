# 📊 YouTube Trending Videos Data Analysis

## 📌 Project Overview

This project analyzes the **US YouTube Trending Videos dataset** to uncover insights such as:

* Video publishing trends
* Category-wise performance
* Views, likes, and engagement patterns

The analysis is performed using **Python, Pandas, Matplotlib, and Seaborn**.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📂 Dataset

* **File Name:** `USvideos.csv`
* Contains:

  * `video_id`, `title`, `views`, `likes`
  * `category_id`, `publish_time`, `trending_date`
  * and more...

---

## ⚙️ Code Explanation (Line by Line)

### 🔹 Import Libraries

```python
import pandas as pd
```

➡️ Used for data manipulation and analysis.

```python
import numpy as np
```

➡️ Used for numerical operations.

```python
import matplotlib.pyplot as plt
```

➡️ Used for plotting graphs.

```python
import seaborn as sns
```

➡️ Used for advanced visualizations.

```python
from datetime import datetime
```

➡️ Used for date-time operations.

---

### 🔹 Load Dataset

```python
df = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\USvideos.csv')
```

➡️ Loads CSV file into DataFrame `df`.

---

### 🔹 View Data

```python
df.head()
```

➡️ Displays first 5 rows.

```python
df.shape
```

➡️ Shows number of rows and columns.

---

### 🔹 Remove Duplicates

```python
df = df.drop_duplicates()
```

➡️ Removes duplicate rows.

```python
df.shape
```

➡️ Checks updated shape after removing duplicates.

---

### 🔹 Statistical Summary

```python
df.describe()
```

➡️ Provides summary statistics (mean, min, max, etc.).

---

### 🔹 Data Info

```python
df.info()
```

➡️ Shows column names, data types, and null values.

---

### 🔹 Drop Unnecessary Columns

```python
columns_to_remove = ['thumbnail_link','description']
```

➡️ List of columns to remove.

```python
df = df.drop(columns=columns_to_remove)
```

➡️ Removes unwanted columns.

```python
df.info()
```

➡️ Confirms updated structure.

---

### 🔹 Date Conversion

```python
import datetime
```

➡️ Imports datetime module again.

```python
df["trending_date"] = df["trending_date"].apply(lambda x: datetime.datetime.strptime(x, '%y.%d.%m'))
```

➡️ Converts `trending_date` string into datetime format.

```python
df.head(3)
```

➡️ Displays first 3 rows.

---

```python
df['publish_time'] = pd.to_datetime(df['publish_time'])
```

➡️ Converts publish_time into datetime.

```python
df.head(2)
```

➡️ Displays updated data.

---

### 🔹 Extract Date Features

```python
df['publish_month'] = df['publish_time'].dt.month
```

➡️ Extracts month.

```python
df['publish_day'] = df['publish_time'].dt.day
```

➡️ Extracts day.

```python
df['publish_hour'] = df['publish_time'].dt.hour
```

➡️ Extracts hour.

---

### 🔹 Category Mapping

```python
df['category_name'] = np.nan
```

➡️ Creates empty column.

```python
df.loc[(df["category_id"] == 1), "category_name"] = 'Film and Animation'
```

➡️ Maps category_id to name.

➡️ Similar mapping is done for all category IDs.

---

### 🔹 Yearly Video Count

```python
df['year'] = df['publish_time'].dt.year
```

➡️ Extracts year.

```python
yearly_counts = df.groupby('year')['video_id'].count()
```

➡️ Counts videos per year.

```python
yearly_counts.plot(kind='bar', xlabel='year', ylabel='total Publish count', title='Total publish video per year')
```

➡️ Creates bar chart.

```python
plt.show()
```

➡️ Displays plot.

---

### 🔹 Yearly Views

```python
yearly_views = df.groupby('year')['views'].sum()
```

➡️ Calculates total views per year.

```python
yearly_views.plot(kind='bar', xlabel='year', ylabel='Total views', title='Total views per year')
```

➡️ Bar chart for views.

---

### 🔹 Top Categories

```python
category_views = df.groupby('category_name')['views'].sum().reset_index()
```

➡️ Total views per category.

```python
top_categories = category_views.sort_values(by='views', ascending=False).head(5)
```

➡️ Selects top 5 categories.

```python
plt.bar(top_categories['category_name'], top_categories['views'])
```

➡️ Plots bar chart.

---

### 🔹 Category Count

```python
sns.countplot(x='category_name', data=df)
```

➡️ Counts videos per category.

---

### 🔹 Videos per Hour

```python
videos_per_hour = df['publish_hour'].value_counts().sort_index()
```

➡️ Counts videos per hour.

```python
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values)
```

➡️ Plots hourly distribution.

---

### 🔹 Videos Over Time

```python
df['publish_date'] = df['publish_time'].dt.date
```

➡️ Extracts date.

```python
video_count_by_date = df.groupby('publish_date').size()
```

➡️ Counts videos per day.

```python
sns.lineplot(data=video_count_by_date)
```

➡️ Plots time trend.

---

### 🔹 Views vs Likes

```python
sns.scatterplot(data=df, x='views', y='likes')
```

➡️ Shows relationship between views and likes.

---

### 🔹 Disabled Features Analysis

```python
sns.countplot(x='comments_disabled', data=df)
```

➡️ Counts videos with comments disabled.

```python
sns.countplot(x='ratings_disabled', data=df)
```

➡️ Counts videos with ratings disabled.

```python
sns.countplot(x='video_error_or_removed', data=df)
```

➡️ Counts removed/error videos.

---

### 🔹 Correlation

```python
corr_matrix = df['views'].corr(df['likes'])
```

➡️ Calculates correlation between views and likes.

```python
corr_matrix
```

➡️ Displays correlation value.

---

## 📊 Key Insights

* Most videos are published in specific peak hours
* Certain categories dominate trending (e.g., Entertainment, Music)
* Strong positive correlation between views and likes
* Engagement features (comments, ratings) impact visibility

---

## 🚀 Future Improvements

* Add sentiment analysis on titles/descriptions
* Build ML model to predict trending videos
* Dashboard using Power BI / Tableau

---

## 🙌 Author

**Ishwarya Kunduru**

---
