
# Pandas Data Analysis

Pandas is built on NumPy and introduces **Labels** (Indices and Column Names), making it capable of handling tabular data (DataFrames).

## 1. Selection: `loc` vs `iloc`
This is the most common source of bugs.

| Method | Definition | Input Logic | Slicing Rule |
| :--- | :--- | :--- | :--- |
| **`.iloc[]`** | **Integer** Location | Purely position-based (0, 1, 2...) | Stop index is **exclusive** (like Python lists). |
| **`.loc[]`** | **Label** Location | Name-based ('Age', 'City'...) | Stop index is **INCLUSIVE**. |

> [!EXAMPLE]
> `df.iloc[0:3]` returns rows 0, 1, 2.
> `df.loc[0:3]` returns rows labeled 0, 1, 2, **AND** 3.

## 2. The `groupby` Operation
Follows the **Split-Apply-Combine** strategy.

1.  **Split:** Data is divided into groups based on a key (e.g., 'City').
2.  **Apply:** A function (sum, mean, count) is applied to each group independently.
3.  **Combine:** Results are merged back into a result object.

```python
# Group by City, take the mean of Sales
df.groupby('City')['Sales'].mean()
```

## 3. Data Cleaning Tools
*   **`isnull().sum()`**: Counts missing values in each column.
*   **`fillna(value)`**: Fills missing values (e.g., with the mean or median).
*   **`dropna()`**: Removes rows with missing data.
*   **`pd.cut`**: Bins continuous data into categories (e.g., Age 0-18 -> "Child").
    *   *Note:* `right=False` means intervals are `[start, end)`.

## 4. Reshaping: Pivot vs Melt
*   **`pivot_table`**: Turns rows into columns (Wide format). Good for summary reports.
    *   *Analogy:* Creating an Excel Pivot Table.
*   **`melt`**: Turns columns into rows (Long format). Good for visualization libraries like Seaborn.
    *   *Analogy:* Un-pivoting.

## 5. Merging Data
*   **`pd.concat`**: Stacking dataframes (usually vertical).
*   **`pd.merge`**: Database-style joining (Inner, Outer, Left, Right) on a specific key (column).


---


### The Sample Data

```python
import pandas as pd
import numpy as np

# Creating the Main DataFrame
data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', 
                            '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-06', '2023-01-07']),
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West', 'South', 'North', 'West'],
    'Product': ['Laptop', 'T-Shirt', 'Mouse', 'Blender', 'Jeans', 'Desk', 'Monitor', 'Shoes', 'Lamp', 'Headphones'],
    'Sales': [1200, 40, 25, 80, 60, 150, 300, 90, 45, 100],
    'Rating': [5.0, 4.0, np.nan, 3.0, 5.0, np.nan, 4.0, 2.0, 4.5, np.nan] # Contains Missing Values!
}

df = pd.DataFrame(data)

# For the 'loc' examples, let's make a version where the Index is text
df_labeled = df.set_index('Product')
```

---

### 1. Selection: `loc` vs `iloc`
**Concept:** This is about how you grab specific rows and columns.
*   `iloc` = "Integer Location" (Position 0, 1, 2...)
*   `loc` = "Label Location" (Names like 'Laptop', 'South'...)

#### Example 1: `iloc` (Standard Slicing)
We want the first 3 rows.
```python
# Like standard Python lists, the stop index (3) is NOT included.
# This gives us rows at index 0, 1, and 2.
subset = df.iloc[0:3] 
```

#### Example 2: `loc` (Inclusive Slicing)
We want rows from 'Laptop' down to 'Mouse' using the `df_labeled` dataframe.
```python
# WARNING: Unlike Python lists, 'loc' INCLUDES the last item.
# This returns Laptop, T-Shirt, AND Mouse.
subset = df_labeled.loc['Laptop':'Mouse'] 
```

#### Example 3: `loc` with Column Names
We want to see the specific 'Sales' and 'Region' for the 'Jeans' row.
```python
# Format: [Row_Label, Column_Label]
# We cannot use numbers (0, 1) here because we are using .loc
info = df_labeled.loc['Jeans', ['Sales', 'Region']]
```

#### Example 4: `iloc` for specific cells by position
We want the value in the 4th row and the 2nd column, regardless of what they are named.
```python
# Row index 3 (4th row), Column index 1 (2nd column)
# This is purely coordinate based.
specific_cell = df.iloc[3, 1] 
```

---

### 2. The `groupby` Operation
**Concept:** We are squashing rows together based on a shared category (Split), doing math on them (Apply), and looking at the result (Combine).

#### Example 1: Simple Mean
We want to know: *On average, how much money do we make per transaction in each Region?*
```python
# 1. Group by 'Region'
# 2. Select the 'Sales' column
# 3. Calculate the Mean
avg_sales = df.groupby('Region')['Sales'].mean()
# Result: East: 115, North: 423, etc.
```

#### Example 2: Multiple Aggregations (agg)
We want to know the Total Sales AND the Average Rating for each Region.
```python
# We pass a dictionary to .agg()
# Key = Column Name, Value = Function
stats = df.groupby('Region').agg({
    'Sales': 'sum',    # Total money made
    'Rating': 'mean'   # Average customer happiness
})
```

#### Example 3: Counting Frequency
We want to know: *How many orders did we get from each Region?*
```python
# .size() counts the number of rows in each group
# .count() counts the number of NON-NULL values
order_counts = df.groupby('Region').size()
```

#### Example 4: Grouping by Multiple Columns
We want detailed stats: *How did each Region perform on specific Dates?*
```python
# We pass a list of columns to groupby
# The result will have a Multi-Index (Two layers of labels)
daily_region_sales = df.groupby(['Region', 'Date'])['Sales'].sum()
```

---

### 3. Data Cleaning Tools
**Concept:** Real-world data is messy. It has holes (`NaN`) or needs to be categorized.

#### Example 1: Detecting Missing Data (`isnull`)
We want to know how many Ratings are missing.
```python
# isnull() returns True/False for every cell.
# .sum() adds up the "Trues" (1s).
missing_count = df.isnull().sum()
# Output for Rating will be 3 (because we have 3 np.nan values)
```

#### Example 2: Filling Missing Data (`fillna`)
We don't want empty cells. Let's assume missing ratings are average (3.0).
```python
# This replaces every 'NaN' in the Rating column with 3.0
# inplace=True means it updates the dataframe directly without making a copy
df['Rating'].fillna(3.0, inplace=True)
```

#### Example 3: Dropping Missing Data (`dropna`)
Alternatively, if a row has missing data, we might consider it "corrupt" and want to delete it entirely.
```python
# If any column in a row has NaN, delete the whole row.
clean_df = df.dropna()
```

#### Example 4: Binning Continuous Data (`cut`)
We want to categorize Sales into "Low", "Medium", and "High".
*   Low: 0-50
*   Medium: 50-150
*   High: 150-2000
```python
bins = [0, 50, 150, 2000]
labels = ['Low Value', 'Mid Value', 'High Value']

# Creates a new column with these text labels
df['Sales_Category'] = pd.cut(df['Sales'], bins=bins, labels=labels)
```

---

### 4. Reshaping: Pivot vs Melt
**Concept:** changing the *shape* of the table without changing the *data*.
*   **Pivot:** Makes the table wider (good for reading).
*   **Melt:** Makes the table longer (good for plotting/graphs).

#### Example 1: `pivot_table` (The Excel Style)
We want a matrix where **Regions are Rows** and **Dates are Columns**, showing Sales in the middle.
```python
# This creates a grid purely for Sales figures
wide_view = df.pivot_table(index='Region', columns='Date', values='Sales', aggfunc='sum')
# Any Region/Date combo with no sales will show as NaN
```

#### Example 2: `pivot_table` with Fill Value
Same as above, but we want to replace the ugly `NaN`s with 0.
```python
wide_view_clean = df.pivot_table(index='Region', columns='Date', values='Sales', fill_value=0)
```

#### Example 3: `melt` (Un-pivoting)
Imagine we have that `wide_view` from Example 1, but we want to turn it back into a long list for a visualization library.
```python
# We assume 'wide_view' is our current dataframe.
# reset_index() is usually needed first to make Region a normal column again.
long_view = wide_view.reset_index().melt(
    id_vars='Region',     # Keep this column as an identifier
    var_name='Date',      # What to call the old column headers
    value_name='Revenue'  # What to call the values
)
```

#### Example 4: `melt` on the Original DataFrame
We want to stack 'Sales' and 'Rating' into a single column called "Metric_Value".
```python
# This makes the dataframe twice as long.
# One row for Sales, one row for Rating, for every order.
super_long = df.melt(
    id_vars=['OrderID', 'Product'], 
    value_vars=['Sales', 'Rating'],
    var_name='Metric_Type',
    value_name='Metric_Value'
)
```

---

### 5. Merging Data
**Concept:** Combining two different DataFrames. We need a second dataframe to demonstrate this.

```python
# New DataFrame: Returns information
returns_data = {
    'OrderID': [102, 105, 110],
    'Reason': ['Wrong Size', 'Defect', 'Changed Mind']
}
df_returns = pd.DataFrame(returns_data)
```

#### Example 1: `pd.merge` (Inner Join)
We want to see **only** the orders that were returned and their details.
```python
# This keeps ONLY rows where OrderID exists in BOTH tables.
# Orders that weren't returned disappear.
returned_orders = pd.merge(df, df_returns, on='OrderID', how='inner')
```

#### Example 2: `pd.merge` (Left Join)
We want a master list of **all** sales, attaching return info if it exists.
```python
# Keep EVERYTHING from 'df' (left).
# If there is no match in 'df_returns', put NaN in the 'Reason' column.
all_orders_status = pd.merge(df, df_returns, on='OrderID', how='left')
```

#### Example 3: `pd.concat` (Vertical Stacking)
We just got new data for the next day. We want to add it to the bottom of our list.
```python
new_sales = pd.DataFrame({
    'OrderID': [111],
    'Product': ['Keyboard'],
    'Sales': [50]
})

# Stacks new_sales below df.
# ignore_index=True resets the row numbers so they don't repeat.
combined_df = pd.concat([df, new_sales], ignore_index=True)
```

#### Example 4: `pd.concat` (Horizontal Stacking)
We have two dataframes with the exact same number of rows and we want to glue them side-by-side.
```python
# Let's say we have a dataframe of Shipping Costs calculated separately
shipping_costs = pd.DataFrame({'Shipping': [5, 5, 5, 10, 5, 10, 15, 5, 5, 15]})

# axis=1 means "Columns" (Side by Side)
# axis=0 means "Rows" (Top to Bottom)
df_with_shipping = pd.concat([df, shipping_costs], axis=1)
```