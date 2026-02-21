
# Part 1: Monthly Sales Analysis Project

This project combines NumPy (generation), Pandas (manipulation), and Matplotlib/Seaborn (visualization).

### 1. `utils.py` (Data Generation)
*Reasoning:* As per **Section 1.3.2** of your notes, we use `np.random.randint` for random integer generation.

```python
# utils.py
import numpy as np

def generate_random_sales(min_val, max_val, size):
    """
    Generates a random NumPy array of integers.
    """
    return np.random.randint(min_val, max_val + 1, size)
```

### 2. `notebook.ipynb` (Analysis Logic)

#### Step 1 & 2: Data Generation & DataFrame Build
*Reasoning:*
*   We use `pd.date_range` for time series generation.
*   We use standard dictionary construction for the DataFrame (**Section 2.1.2**).
*   `axis=1` is used for summing across columns (**Section 1.6.1** logic applied to Pandas).
*   `idxmax(axis=1)` is the Pandas equivalent of finding the index (column name) of the max value.

```python
import pandas as pd
import numpy as np
from utils import generate_random_sales

# --- 1. Data Generation ---
dates = pd.date_range(start='2025-01-01', periods=12, freq='MS') # MS = Month Start

data = {
    'Date': dates,
    'Product_A': generate_random_sales(50, 100, 12),
    'Product_B': generate_random_sales(30, 80, 12),
    'Product_C': generate_random_sales(20, 60, 12),
    'Product_D': generate_random_sales(10, 50, 12)
}

df = pd.DataFrame(data)
df.to_csv('initial.csv', index=False)

# --- 2. Build DataFrame & Metrics ---
# Extract Month name
df['Month'] = df['Date'].dt.strftime('%b') # Jan, Feb...

# Total & Average Sales (Axis=1 acts on rows)
product_cols = ['Product_A', 'Product_B', 'Product_C', 'Product_D']
df['Total_Sales'] = df[product_cols].sum(axis=1)
df['Average_Sales'] = df[product_cols].mean(axis=1)

# Growth (pct_change calculates change vs previous row)
df['Month_over_Month_Growth'] = df['Total_Sales'].pct_change() * 100

# Assign Quarters
df['Quarter'] = df['Date'].dt.quarter.map({1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})

# Max/Min Product per month (idxmax returns the column label of the max value)
df['Max_Sales_Product'] = df[product_cols].idxmax(axis=1)
df['Min_Sales_Product'] = df[product_cols].idxmin(axis=1)

df.to_csv('final.csv', index=False)
print(df.head())
```

#### Step 3: Pivot Tables
*Reasoning:* As per **Section 2.9.1**, Pivot tables allow us to aggregate data (Long to Wide).

```python
# --- 3. Summaries ---
# Average sales per quarter for each product
pivot_avg = df.pivot_table(index='Quarter', values=product_cols, aggfunc='mean')

# Total sales per quarter
pivot_total = df.pivot_table(index='Quarter', values='Total_Sales', aggfunc='sum')

# Save (using an Excel writer or appending to CSV, here we just show logic)
pivot_avg.to_csv('output.csv') 
```

#### Step 4: Key Insights (Code to find them)
*Reasoning:* We use sorting (`sort_values`) and accessing the top row (`iloc[0]`) to find "bests".

```python
# Best Month
best_month = df.sort_values('Total_Sales', ascending=False).iloc[0]['Month']

# Best Product (Summing columns then finding max)
best_product = df[product_cols].sum().idxmax()

# Best Quarter
best_quarter = pivot_total['Total_Sales'].idxmax()

print(f"Best Month: {best_month}, Best Product: {best_product}, Best Quarter: {best_quarter}")
```

#### Step 5: Visualization
*Reasoning:*
*   **Line Chart:** Used for trends over time (**Section 3.3**).
*   **Stacked Bar:** Good for comparing composition (products) within categories (months).
*   **Heatmap:** Used for correlation or data density (**Section 4.3.3**).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line Chart
plt.figure(figsize=(10, 6))
for prod in product_cols:
    plt.plot(df['Month'], df[prod], marker='o', label=prod)
plt.title("Product Sales Trends")
plt.legend()
plt.show()

# 2. Stacked Bar
df.set_index('Month')[product_cols].plot(kind='bar', stacked=True, figsize=(10,6))
plt.title(f"Monthly Sales (Best Month: {best_month})")
plt.ylabel("Sales")
plt.show()

# 3. Seaborn Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[product_cols], annot=True, cmap="YlGnBu", yticklabels=df['Month'])
plt.title("Monthly Sales Heatmap")
plt.show()

# 4. Boxplot
plt.figure(figsize=(10, 6))
# We need to melt data for seaborn boxplot (Wide to Long as per Section 2.9.2)
melted_df = df.melt(id_vars=['Month'], value_vars=product_cols, var_name='Product', value_name='Sales')
sns.boxplot(data=melted_df, x='Product', y='Sales')
plt.title("Sales Distribution per Product")
plt.show()
```

---

# Part 2: Exercises

## Exercise 01: Temperature Analysis with NumPy

**Reasoning:** This tests array creation, slicing, and aggregation axes (**Section 1.6.1**). `axis=0` calculates down the column (per city), `axis=1` across the row (per day).

```python
import numpy as np

# 1. Create Array
data = np.array([
    [22, 25, 20],
    [24, 27, 21],
    [19, 20, 22],
    [25, 29, 28],
    [26, 30, 27],
    [21, 21, 23],
    [20, 26, 25]
])

# 2. Compute Maxima
max_per_city = np.max(data, axis=0)  # Down columns
max_per_day = np.max(data, axis=1)   # Across rows
overall_max = np.max(data)

print("Max per city:", max_per_city)
print("Max per day:", max_per_day)

# 3. Find Day and City of overall max
# argmax returns flat index, unravel_index converts to (row, col)
max_pos = np.unravel_index(np.argmax(data), data.shape)
cities = ['Alger', 'Annaba', 'Oran']
print(f"Overall Max occurred on Day {max_pos[0]+1} in {cities[max_pos[1]]}")

# 4. Higher temp between Alger (col 0) and Oran (col 2)
# np.maximum compares element-wise
alger = data[:, 0]
oran = data[:, 2]
comparison = np.maximum(alger, oran)
print("Higher (Alger vs Oran):", comparison)

# 5. Add Average Row
avg_temps = np.mean(data, axis=0) # Average per city
# Stack vertical (Section 1.7)
data_with_avg = np.vstack([data, avg_temps])

# 6. Days where Annaba (col 1) was hottest (vs Alger AND Oran)
annaba = data[:, 1]
# Boolean mask
mask = (annaba > alger) & (annaba > oran)
# np.where returns indices where mask is true
days_annaba_hottest = np.where(mask)[0] + 1 
print("Days Annaba was hottest:", days_annaba_hottest)
```

---

## Exercise 02: Student Grades with NumPy

**Reasoning:** Focuses on statistical functions (`mean`, `std`, `percentile`) and boolean masking (**Section 1.4.2**).

```python
import numpy as np
import matplotlib.pyplot as plt

# 1-3. Initialization
np.random.seed(101) # Reproducibility
grades = np.random.randint(0, 21, size=(100, 5)) # 100 students, 5 modules
modules = np.array(['THL', 'DSS', 'DB', 'SE', 'RE'])

# --- Basic Statistics ---
# 1. Mean per student (axis 1)
mean_per_student = np.mean(grades, axis=1)

# 2. Mean per module (axis 0)
mean_per_module = np.mean(grades, axis=0)

# 4. Variance and Std Dev per module
var_modules = np.var(grades, axis=0)
std_modules = np.std(grades, axis=0)

# 6. Percentiles for THL (Index 0)
thl_grades = grades[:, 0]
p25, p50, p75 = np.percentile(thl_grades, [25, 50, 75])
print(f"THL Percentiles: 25th={p25}, 50th={p50}, 75th={p75}")

# --- Boolean Masking ---
# 1. Mask for 10 <= grade <= 15
mask_10_15 = (grades >= 10) & (grades <= 15)
# 2. Count
count_10_15 = np.sum(mask_10_15)
# 3. Extract values
grades_10_15 = grades[mask_10_15]

# --- Visualization ---
# 1. Bar Plot (Mean grades)
plt.bar(modules, mean_per_module, color='skyblue')
plt.title("Average Grades per Module")
plt.show()

# --- Extra Practice ---
# 1. All grades > 15
# np.all checks if ALL elements in the axis satisfy the condition
excellent_students_mask = np.all(grades > 15, axis=1)
print(f"Students with all grades > 15: {np.where(excellent_students_mask)[0]}")

# 2. Top 5 Students
# argsort sorts ascending, so we take slice form end [::-1]
top_5_indices = np.argsort(mean_per_student)[-5:][::-1]
print("Top 5 Student Indices:", top_5_indices)
```

---

## Exercise 03: Hospital Data with Pandas

**Reasoning:** Covers the full Pandas lifecycle: Creation -> Transformation -> Cleaning -> Ranking -> Aggregation. Key notes used: **Section 2.5 (Filtering)**, **Section 2.9 (Pivot)**, and vectorized math.

```python
import pandas as pd
import numpy as np

# 1. Create DataFrame
data = {
    'City': ['Alger', 'Annaba', 'Oran', 'Alger', 'Oran', 'Annaba', 'Alger', 'Oran'],
    'Department': ['Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology'],
    'Age': [45, 60, 30, 50, 40, 70, 35, 55],
    'DaysAdmitted': [5, 8, 3, 7, 4, 6, 2, 9],
    'DailyCost': [200, 300, 150, 220, 280, 160, 210, 290],
    'Satisfaction': [4.5, 3.8, 4.2, 4.0, 4.1, 3.5, 4.7, 3.9],
    'Readmitted': [0, 1, 0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# 2. Add Columns
df['TotalCost'] = df['DaysAdmitted'] * df['DailyCost']

# Age Group (using cut is cleaner than multiple if statements)
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 50, 150], labels=['Young', 'Middle', 'Senior'], right=True)

# 3. Add/Rename/Delete
df['Bonus'] = df['DailyCost'] * 0.10
df.rename(columns={'DailyCost': 'DailyFee'}, inplace=True)
df.drop(columns=['Bonus'], inplace=True)

# 4. Data Transformation (np.where is efficient for Yes/No logic)
df['HighCost'] = np.where(df['TotalCost'] > 60000, 'Yes', 'No') # Note: Costs in data are small, so all will be "No"

def categorize_satisfaction(s):
    if s >= 8: return 'Excellent' # Note: Data is 1-5 scale, instructions imply 1-10 scale.
    elif s >= 5: return 'Average'
    else: return 'Poor'

df['SatisfactionLevel'] = df['Satisfaction'].apply(categorize_satisfaction)

# 5. Ranking
df['Rank'] = df['TotalCost'].rank(ascending=False)

# 7. Risk Score Calculation (Before cleaning/mapping to keep math valid)
# Formula: (Days * 0.4) + (Age * 0.3) + (100 - Sat * 10) * 0.3
df['RiskScore'] = (df['DaysAdmitted'] * 0.4) + (df['Age'] * 0.3) + ((100 - df['Satisfaction'] * 10) * 0.3)

# Risk Category
df['RiskCategory'] = pd.cut(df['RiskScore'], bins=[-np.inf, 40, 60, np.inf], labels=['Low', 'Medium', 'High'])

# 9. Data Cleaning & Mapping
# Mapping Readmitted 0->No, 1->Yes
df['Readmitted'] = df['Readmitted'].map({0: 'No', 1: 'Yes'})
# Mapping Cities (Example logic)
df['City'] = df['City'].map({'Alger': 'DZ-16', 'Oran': 'DZ-31', 'Annaba': 'DZ-23'})

# 10. Pivot Analysis
pivot_summary = df.pivot_table(index=['City', 'Department'], values=['TotalCost', 'Satisfaction'], aggfunc='mean')
print(pivot_summary)

# 11. Export
df.to_csv('hospital_risk.csv', index=False)
```

---

## Exercise 04: Visualization (Matplotlib vs Seaborn)

**Reasoning:** Compares the **OO-Matplotlib** approach (**Section 3.1.2**) vs the high-level **Seaborn** approach (**Section 4.1**).

### Matplotlib Section (Manual Control)

```python
import matplotlib.pyplot as plt

# 1. Total Cost per City (Bar)
city_costs = df.groupby('City')['TotalCost'].sum()
plt.bar(city_costs.index, city_costs.values, color='orange')
plt.title("Total Cost per City")
# Annotation loop
for i, v in enumerate(city_costs.values):
    plt.text(i, v, str(v), ha='center')
plt.show()

# 2. Satisfaction Distribution (Hist)
plt.hist(df['Satisfaction'], bins=5, color='green', alpha=0.7)
plt.axvline(df['Satisfaction'].mean(), color='red', linestyle='dashed', label='Mean')
plt.title("Satisfaction Distribution")
plt.legend()
plt.show()

# 3. Scatter Plot
# Use boolean masking to color HighCost points differently
plt.scatter(df['TotalCost'], df['Satisfaction'], c='blue')
plt.xlabel("Total Cost")
plt.ylabel("Satisfaction")
plt.title("Cost vs Satisfaction")
plt.show()
```

### Seaborn Section (Statistical & Theme-based)

```python
import seaborn as sns

# 1. Barplot with Hue
sns.barplot(data=df, x='City', y='TotalCost', hue='Department')
plt.title("Cost by City and Dept")
plt.show()

# 2. Boxplot
sns.boxplot(data=df, x='City', y='RiskScore')
plt.title("Risk Score Distribution")
plt.show()

# 3. Correlation Heatmap
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 5. Combined Dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Hospital Risk and Satisfaction Overview")

# Subplot 1
sns.barplot(data=df, x='City', y='Satisfaction', ax=axes[0,0])
# Subplot 2
sns.boxplot(data=df, x='RiskCategory', y='RiskScore', ax=axes[0,1])
# Subplot 3
sns.heatmap(numeric_df.corr(), annot=True, ax=axes[1,0])
# Subplot 4
sns.countplot(data=df, x='City', hue='Readmitted', ax=axes[1,1])

plt.tight_layout()
plt.show()
```