# ❤️ Heart Disease Data Analysis

## 📌 Project Overview

This project analyzes a **heart disease dataset** to identify patterns and answer key questions like:

* How many people have heart disease?
* Which gender is more affected?
* How chest pain relates to heart disease

The analysis is done using **Python, Pandas, Matplotlib, and Seaborn**.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

## 📂 Dataset

* **File Name:** `heart.csv`
* Key Columns:

  * `age` → Age of patient
  * `sex` → Gender (1 = Male, 0 = Female)
  * `cp` → Chest pain type
  * `thalach` → Maximum heart rate
  * `target` → Heart disease (1 = Yes, 0 = No)

---

## ⚙️ Code Explanation (Line by Line)

### 🔹 Import Libraries

```python id="k3s8bz"
import numpy as np
```

➡️ Used for numerical operations.

```python id="0q0tbo"
import pandas as pd
```

➡️ Used for data handling and analysis.

```python id="r9dkg3"
import matplotlib.pyplot as plt
```

➡️ Used for creating plots.

```python id="5ry8lo"
import seaborn as sns
```

➡️ Used for advanced visualizations.

```python id="9ch87y"
get_ipython().run_line_magic('matplotlib', 'inline')
```

➡️ Displays plots inside Jupyter Notebook.

---

### 🔹 Load Dataset

```python id="m5l8fx"
df = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\heart.csv')
```

➡️ Loads dataset into DataFrame `df`.

---

### 🔹 View Data

```python id="t9a8yb"
df.head()
```

➡️ Displays first 5 rows.

```python id="3k7w0s"
df.tail()
```

➡️ Displays last 5 rows.

```python id="z8m8p7"
df.columns.values
```

➡️ Shows all column names.

---

### 🔹 Check Missing Values

```python id="4hjhvk"
df.isna().sum()
```

➡️ Checks for null values in each column.

---

### 🔹 Dataset Info

```python id="y8kqru"
df.info()
```

➡️ Shows data types and non-null counts.

---

### 🔹 Histogram

```python id="h8nqv4"
df.hist(bins=50, grid=False, figsize=(20,15));
```

➡️ Displays distribution of all numerical columns.

---

### 🔹 Statistical Summary

```python id="l3k8zp"
df.describe()
```

➡️ Shows mean, min, max, etc.

---

### 🔹 Questions

```python id="w2f6jk"
questions = [...]
```

➡️ Lists analysis questions.

---

### 🔹 Target Variable Analysis

```python id="v9g1qa"
df.target.value_counts()
```

➡️ Counts people with/without heart disease.

```python id="o6l3fs"
df.target.value_counts().plot(kind='bar', color=["orchid","salmon"])
```

➡️ Bar chart of heart disease count.

```python id="9sb1hv"
df.target.value_counts().plot(kind='pie', figsize=(8,6))
```

➡️ Pie chart representation.

---

### 🔹 Gender Analysis

```python id="c4d7hj"
df.sex.value_counts()
```

➡️ Counts male and female.

```python id="m2x7fa"
df.sex.value_counts().plot(kind='pie')
```

➡️ Pie chart of gender distribution.

---

### 🔹 Target vs Gender

```python id="9v2n7l"
pd.crosstab(df.target, df.sex)
```

➡️ Shows relationship between gender and disease.

---

### 🔹 Chest Pain Analysis

```python id="f6y9ke"
df.cp.value_counts()
```

➡️ Counts chest pain types.

```python id="r1w8kx"
df.cp.value_counts().plot(kind='bar')
```

➡️ Bar chart of chest pain types.

---

### 🔹 Gender vs Chest Pain

```python id="u3n6b2"
pd.crosstab(df.sex, df.cp)
```

➡️ Shows chest pain distribution by gender.

```python id="p4k8zs"
pd.crosstab(df.sex, df.cp).plot(kind='bar')
```

➡️ Visualizes above data.

---

### 🔹 Chest Pain vs Heart Disease

```python id="d8f1tm"
pd.crosstab(df.cp, df.target)
```

➡️ Shows which chest pain leads to disease.

```python id="g7j3qa"
sns.countplot(x='cp', data=df, hue='target')
```

➡️ Visual comparison.

---

### 🔹 Age Distribution

```python id="w9n2xr"
sns.displot(x='age', data=df, bins=30, kde=True)
```

➡️ Shows age distribution.

---

### 🔹 Max Heart Rate Distribution

```python id="q6h8pl"
sns.displot(x='thalach', data=df, bins=30, kde=True)
```

➡️ Shows heart rate distribution.

---

## 📊 Key Insights

* Significant number of people have heart disease
* Gender plays a role in disease distribution
* Certain chest pain types are strongly linked to heart disease
* Age and heart rate show important patterns

---

## 🚀 Future Improvements

* Apply machine learning models (Logistic Regression, Decision Tree)
* Build prediction system
* Create dashboard (Power BI / Tableau)

---

## 🙌 Author

**Ishwarya Kunduru**

---
