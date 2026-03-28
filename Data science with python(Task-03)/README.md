# 📊 Household Data Analysis & Visualization

## 📌 Project Overview

This project analyzes household data using Python and visualizes patterns using different plots like scatter, line, bar, and histogram.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📂 Dataset

* **File Name:** `householdtask3.csv`
* Columns:

  * `year` → Year data
  * `own` → Ownership values
  * `income` → Income data

---

## ⚙️ Code Explanation (Line by Line)

### 🔹 Import Libraries

```python
import pandas as pd
```

➡️ Imports **Pandas** library to work with datasets (tables, CSV files).

```python
import numpy as np
```

➡️ Imports **NumPy** for numerical operations (arrays, calculations).

```python
import matplotlib.pyplot as plt
```

➡️ Imports **Matplotlib** for creating graphs and plots.

```python
import seaborn as sns
```

➡️ Imports **Seaborn** for advanced and attractive visualizations.

```python
from datetime import datetime
```

➡️ Imports **datetime** module to work with date and time (not used in this code but useful).

---

### 🔹 Load Dataset

```python
data = pd.read_csv('C:\\Users\\Ishwarya\\Downloads\\householdtask3.csv')
```

➡️ Reads the CSV file and stores it in a DataFrame named `data`.

---

### 🔹 Display Data

```python
display(data.head(10))
```

➡️ Shows the first 10 rows of the dataset to understand structure and values.

---

### 🔹 Scatter Plot

```python
plt.scatter(data['year'], data['own'])
```

➡️ Creates a scatter plot showing relationship between **year and ownership**.

```python
plt.title("scatter plot")
```

➡️ Adds title to the graph.

```python
plt.xlabel('year')
```

➡️ Labels x-axis as "year".

```python
plt.ylabel('own')
```

➡️ Labels y-axis as "own".

```python
plt.show()
```

➡️ Displays the plot.

---

### 🔹 Line Chart

```python
plt.plot(data['year'])
```

➡️ Plots values of `year`.

```python
plt.plot(data['own'])
```

➡️ Plots values of `own` on same graph.

```python
plt.title("Line chart")
```

➡️ Adds title.

```python
plt.xlabel('year')
```

➡️ Labels x-axis.

```python
plt.ylabel('own')
```

➡️ Labels y-axis.

```python
plt.show()
```

➡️ Displays the chart.

---

### 🔹 Bar Plot

```python
plt.bar(data['year'], data['own'])
```

➡️ Creates a bar chart comparing ownership across years.

```python
plt.title("Bar plot")
```

➡️ Adds title.

```python
plt.xlabel('year')
```

➡️ Labels x-axis.

```python
plt.ylabel('own')
```

➡️ Labels y-axis.

```python
plt.show()
```

➡️ Displays the plot.

---

### 🔹 Histogram

```python
plt.hist(data['income'])
```

➡️ Creates histogram to show distribution of income values.

```python
plt.title("Histogram")
```

➡️ Adds title.

```python
plt.show()
```

➡️ Displays histogram.

---

## 📊 Key Insights

* Scatter plot shows relationship between variables
* Line chart shows trends over time
* Bar chart compares values across years
* Histogram shows income distribution

---

## 🚀 Future Improvements

* Data cleaning and preprocessing
* Add correlation analysis
* Build machine learning model
* Create dashboard using Power BI / Tableau

---

## 🙌 Author

**Ishwarya Kunduru**

---
