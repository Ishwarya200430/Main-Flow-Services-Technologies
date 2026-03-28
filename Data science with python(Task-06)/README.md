# 🎬 Disney+ Titles Data Analysis

## 📌 Project Overview

This project analyzes the **Disney+ titles dataset** to understand:

* Content ratings distribution
* Country-wise availability
* Movie vs TV show trends
* Release year patterns
* Duration and content growth

The analysis is performed using **Python, Pandas, Matplotlib, and Seaborn**.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

## 📂 Dataset

* **File Name:** `disney_plus_titles.csv`
* Contains:

  * `show_id` → Unique ID
  * `type` → Movie / TV Show
  * `title`, `country`, `release_year`
  * `rating`, `duration`, `date_added`, `listed_in`

---

## ⚙️ Code Explanation (Line by Line)

### 🔹 Import Libraries

```python id="x1k7po"
import numpy as np
```

➡️ Used for numerical operations.

```python id="z8v2lm"
import pandas as pd
```

➡️ Used for data handling and analysis.

```python id="h3s9qw"
import matplotlib.pyplot as plt
```

➡️ Used for plotting graphs.

```python id="p7d2ye"
import seaborn as sns
```

➡️ Used for advanced visualizations.

```python id="k9r5fa"
get_ipython().run_line_magic('matplotlib', 'inline')
```

➡️ Ensures plots display inside Jupyter Notebook.

---

### 🔹 Load Dataset

```python id="m2a8vn"
df = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\disney_plus_titles.csv')
```

➡️ Loads dataset into DataFrame `df`.

---

### 🔹 View Data

```python id="q4y7bc"
df.head()
```

➡️ Displays first 5 rows.

```python id="d1f6zx"
df.tail()
```

➡️ Displays last 5 rows.

---

### 🔹 Check Missing Values

```python id="r6j2ls"
df.isna().sum()
```

➡️ Checks null values in each column.

---

### 🔹 Dataset Info

```python id="b8k3po"
df.info()
```

➡️ Shows column names, data types, and non-null values.

---

### 🔹 Statistical Summary

```python id="u5v9mn"
df.describe()
```

➡️ Provides statistical details of numerical columns.

---

### 🔹 Data Type Check

```python id="c7w2ha"
type(df)
```

➡️ Confirms dataset is a DataFrame.

---

### 🔹 Remove Duplicates

```python id="y2e8tn"
df = df.drop_duplicates()
```

➡️ Removes duplicate rows.

```python id="n9k3qe"
df
```

➡️ Displays cleaned dataset.

---

### 🔹 Column Names

```python id="g3u8as"
df.columns
```

➡️ Lists all column names.

---

### 🔹 Histogram

```python id="f6p2lo"
df.hist(bins=50, grid=False, figsize=(20,15));
```

➡️ Shows distribution of numerical columns.

---

### 🔹 Questions

```python id="s5z7qd"
questions = [...]
```

➡️ Defines analysis questions.

---

### 🔹 Rating Analysis

```python id="t2y9bx"
df.rating.value_counts()
```

➡️ Counts different ratings.

```python id="a7w4cl"
df.rating.value_counts().plot(kind='bar')
```

➡️ Bar chart of ratings.

```python id="m8k1js"
df.rating.value_counts().plot(kind='pie')
```

➡️ Pie chart of ratings.

---

### 🔹 Listed Categories

```python id="p3x8vn"
df.listed_in.value_counts().plot(kind='bar')
```

➡️ Shows content categories distribution.

---

### 🔹 Country Analysis

```python id="v7r2op"
df.country.value_counts().plot(kind='bar')
```

➡️ Displays number of titles per country.

---

### 🔹 Release Year Analysis

```python id="j4c9we"
sns.displot(x='release_year', data=df, bins=10, kde=True)
```

➡️ Shows trend of release years.

```python id="l8m2qa"
sns.displot(x='release_year', data=df, bins=10, kde=False)
```

➡️ Same plot without density curve.

---

### 🔹 Duration Analysis

```python id="n5f7kt"
sns.displot(x='duration', data=df, bins=30, kde=True)
```

➡️ Shows distribution of duration.

---

### 🔹 Movie vs TV Show

```python id="w3h9pl"
df.type.value_counts().plot(kind='pie')
```

➡️ Compares number of Movies vs TV Shows.

---

### 🔹 Date Added Analysis

```python id="k8t1xa"
sns.displot(x='date_added', data=df, bins=10, kde=True)
```

➡️ Shows trend of content added over time.

---

### 🔹 Show ID Analysis

```python id="q1z6mn"
sns.displot(x='show_id', data=df, bins=10, kde=True)
```

➡️ Analyzes distribution of show IDs.

---

## 📊 Key Insights

* Certain ratings dominate Disney+ content
* Movies are more common than TV shows (or vice versa depending on dataset)
* Content is concentrated in specific countries
* Release years show growth trend in recent years
* Duration varies significantly across content

---

## 🚀 Future Improvements

* Clean and preprocess missing data
* Perform sentiment analysis on titles/descriptions
* Build recommendation system
* Create dashboard (Power BI / Tableau)

---

## 🙌 Author

**Ishwarya Kunduru**

---
