
## 1. Overview
This exercise tackles a messy, realistic dataset. Real-world data is rarely clean; it contains typos, missing values, and nonsense outliers. This tutorial builds a **Preprocessing Pipeline** to fix these issues before analysis.

## 2. The Data Problems
We identified four major issues in the raw `data/messy_medical.csv`:
1.  **Inconsistent Strings:** `Female`, `female`, `FEMALE`.
2.  **Missing Values (NaN):** Gaps in Age, BloodPressure, and Cholesterol.
3.  **Typos/Outliers:** A patient aged 120.
4.  **Format:** Computers cannot do math on text ("Diabetes"), so we need numbers.

## 3. The Cleaning Pipeline

### Step 1: Standardization
```python
df['Gender'].str.lower().str.strip()
```
*   **Why?** Grouping by `Gender` would create 3 separate groups for women if we didn't fix the capitalization. This merges them into one clean `female` category.

### Step 2: Imputation (Filling NaNs)
*   **Categorical Data:** Filled with the **Mode** (Most common value).
*   **Numerical Data:** Filled with the **Median**.
*   **Critical Thinking:** Why Median and not Mean? The dataset has an outlier (Age 120). The *Mean* is sensitive to outliers (it would be pulled higher). The *Median* is robust and represents the "middle" patient better.

### Step 3: Outlier Removal
We removed patients with `Age > 100`. In a medical context, unless studying centenarians specifically, an age of 120 usually indicates a data entry error.

### Step 4: Encoding & Scaling
*   **Label Encoding:** Converts `Healthy`, `Diabetes` -> `0`, `1`.
*   **MinMax Scaling:** Transforms `Age` (0-100) and `BP` (100-200) to a common scale (0-1).
    *   *Why?* Some Machine Learning algorithms (like K-Nearest Neighbors) behave poorly if one variable has huge numbers (BP) and another has small numbers (Age). Scaling makes them equal in importance.

## 4. Visualization Insights
*   **Scatter Plot:** Showed how Blood Pressure correlates with Age.
*   **Box Plot:** Showed that patients with `Hypertension` generally had higher Cholesterol ranges than `Healthy` patients.
*   **Heatmap:** Provided a quick summary grid showing that Males with Hypertension had the highest average Blood Pressure in the cohort.
