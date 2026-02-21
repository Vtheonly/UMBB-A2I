
# Exercise 01: Medical Dataset (Cleaning & Visualization)

### Step 1: Create and Clean the Dataset

We will first recreate the dataset from the screenshot, then apply the cleaning strategies found in **File 2 (Data Consistency)** and **File 1 (Missing Data Handling)**.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Recreating the dataset from the screenshot
data = {
    'PatientID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008', 'P009', 'P010'],
    'Age': [25, np.nan, 65, 50, 80, 120, 45, 38, np.nan, 55],
    'BloodPressure': [120, 130, np.nan, 110, 200, 95, 125, 118, 122, 210],
    'Cholesterol': [200, 180, 250, 190, 300, 180, np.nan, 210, 220, 350],
    'Gender': ['Female', 'male', 'Male', 'female', 'MALE', 'None', 'Female', 'female', 'FEMALE', 'Male'],
    'Diagnosis': ['Diabetes', 'Healthy', 'Diabetes', 'Healthy', 'Hypertension', 'Healthy', 'Diabetes', 'Healthy', 'None', 'Hypertension']
}
df = pd.DataFrame(data)

# --- CLEANING STEPS ---

# 1. Text Normalization (File 2 & File 4)
# Problem: 'Male', 'male', 'MALE' are treated as different categories.
# Solution: Lowercase and strip whitespace.
cols_to_fix = ['Gender', 'Diagnosis']
for col in cols_to_fix:
    # Convert to string first to handle non-string types safely
    df[col] = df[col].astype(str).str.lower().str.strip()
    
# Replace literal string "none" or "nan" with actual NumPy NaN for proper processing
df.replace(['none', 'nan'], np.nan, inplace=True)

# 2. Fill Missing Categorical Values (File 1)
# Strategy: Impute with Mode (Most Frequent)
# Gender mode is likely 'female' or 'male' based on counts.
for col in ['Gender', 'Diagnosis']:
    mode_val = df[col].mode()[0]
    df[col] = df[col].fillna(mode_val)

# 3. Fill Missing Numeric Values (File 1)
# Strategy: Use Median.
# Reasoning: Age and BP can have outliers (skewed data). File 1 suggests Median is safer than Mean.
for col in ['Age', 'BloodPressure', 'Cholesterol']:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)

# 4. Remove Extreme Outliers (File 3)
# Detection: IQR Method.
# Note: Patient P006 has Age 120. This is likely an error.
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Filtering: Keep only rows within bounds
df_clean = df[(df['Age'] >= lower) & (df['Age'] <= upper)].copy()

print("Cleaned Data Sample:")
print(df_clean)

# 5. Encoding Categorical Variables (File 5)
# Strategy: Label Encoding (Assigning numbers to categories).
# Note: For 'Gender', One-Hot is usually better, but for this specific exercise asking for "numeric format", LabelEncoder is efficient.
le = LabelEncoder()
df_clean['Gender_Code'] = le.fit_transform(df_clean['Gender'])
df_clean['Diagnosis_Code'] = le.fit_transform(df_clean['Diagnosis'])

# 6. Feature Scaling (File 6)
# Strategy: StandardScaler (Z-Score).
# Why? Cholesterol (200-350) is much larger than Age (25-80). 
scaler = StandardScaler()
df_clean[['Age_Scaled', 'BP_Scaled', 'Chol_Scaled']] = scaler.fit_transform(df_clean[['Age', 'BloodPressure', 'Cholesterol']])
```

### Step 2: Visualize the Data

We use `seaborn` as recommended in **File 1 (EDA Intro)** and **File 5/6/7 (Analysis)**.

```python
# Set style (File 1 recommendation)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

# 1. Relationship between Age and BloodPressure, distinguishing Gender
# Analysis Type: Multivariate (Num vs Num vs Cat)
plt.subplot(2, 2, 1)
sns.scatterplot(data=df_clean, x='Age', y='BloodPressure', hue='Gender', s=100)
plt.title('Age vs Blood Pressure (by Gender)')

# 2. Distribution of Cholesterol by Diagnosis
# Analysis Type: Bivariate (Num vs Cat) - Boxplot is best here (File 5)
plt.subplot(2, 2, 2)
sns.boxplot(data=df_clean, x='Diagnosis', y='Cholesterol')
plt.title('Cholesterol Distribution by Diagnosis')

# 3. Pivot Table / Heatmap (Average BP by Diagnosis and Gender)
# Analysis Type: Multivariate aggregation (File 7)
plt.subplot(2, 2, 3)
pivot_table = df_clean.pivot_table(values='BloodPressure', index='Diagnosis', columns='Gender', aggfunc='mean')
sns.heatmap(pivot_table, annot=True, cmap='Blues', fmt=".1f")
plt.title('Avg Blood Pressure Heatmap')

# 4. Combined Comparative Plot (Pairplot)
# Analysis Type: Multivariate (File 7)
# Note: Pairplot creates its own figure, so we usually run it separately, 
# but here is the code to generate it.
plt.tight_layout()
plt.show()

# Generating Pairplot separately
sns.pairplot(df_clean, vars=['Age', 'BloodPressure', 'Cholesterol'], hue='Diagnosis', height=2.5)
plt.show()
```

---

# Project 02: Titanic Data Preprocessing & Modeling

This section builds a full pipeline. Note that `sns.load_dataset('titanic')` is a cleaned version that lacks the 'Name' column required for title extraction. I will address this in the Feature Engineering section.

### 1. Initial Exploration & Cleaning

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Data
df_titanic = sns.load_dataset('titanic')

# EDA Check (File 2)
# print(df_titanic.info())
# print(df_titanic.isnull().sum())

# --- CLEANING (File 1 & 3) ---

# 1. Missing Values
# Age: Skewed distribution -> Use Median (File 1)
df_titanic['age'] = df_titanic['age'].fillna(df_titanic['age'].median())

# Embarked: Categorical -> Use Mode (File 1)
df_titanic['embarked'] = df_titanic['embarked'].fillna(df_titanic['embarked'].mode()[0])
df_titanic['embark_town'] = df_titanic['embark_town'].fillna(df_titanic['embark_town'].mode()[0])

# Deck: Too many missing (>70%) -> Drop Column (File 1 Strategy 1)
df_titanic.drop(columns=['deck'], inplace=True)

# 2. Drop Redundant Columns
# 'who' overlaps with sex/age. 'alive' overlaps with survived. 'class' overlaps with pclass.
cols_to_drop = ['who', 'alive', 'adult_male', 'class', 'embark_town']
df_titanic.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# 3. Duplicates (File 2)
df_titanic.drop_duplicates(inplace=True)
```

### 2. Feature Engineering

```python
# 1. Family Size
df_titanic['FamilySize'] = df_titanic['sibsp'] + df_titanic['parch'] + 1

# 2. IsAlone (Binary feature)
df_titanic['IsAlone'] = 1
df_titanic['IsAlone'].loc[df_titanic['FamilySize'] > 1] = 0

# 3. Title Extraction
# NOTE: sns.load_dataset('titanic') does NOT contain names. 
# If using a CSV from Kaggle, the code would be:
# df_titanic['Title'] = df_titanic['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
# Since we don't have it, we skip this specific step for this dataset source.
```

### 3. Encoding & Outlier Handling

```python
# --- CATEGORICAL ENCODING (File 5) ---

# Sex: Nominal (Binary) -> Label Encoding or Map
df_titanic['sex'] = df_titanic['sex'].map({'male': 0, 'female': 1})

# Embarked: Nominal -> One-Hot Encoding
# We use get_dummies with drop_first=True to avoid multicollinearity
df_titanic = pd.get_dummies(df_titanic, columns=['embarked'], drop_first=True)

# --- OUTLIER HANDLING (File 3) ---

# Fare is notoriously right-skewed (File 4 - Skewness).
# We apply Log Transformation to compress the range.
# Adding +1 to avoid log(0) errors.
df_titanic['fare'] = np.log1p(df_titanic['fare'])
```

### 4. Scaling, Split, and Modeling

```python
# Define Features (X) and Target (y)
X = df_titanic.drop('survived', axis=1)
y = df_titanic['survived']

# --- SCALING (File 6) ---
# Algorithms like KNN use Euclidean distance, so Scaling is MANDATORY.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# --- MODELING ---

# Model 1: Logistic Regression
log_reg = LogisticRegression(max_iter=500)
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

# Model 2: K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# --- EVALUATION ---

print("--- Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

print("\n--- KNN Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))
```

### Comparison & Justification
*   **Logistic Regression:** Likely performed well because the relationships between class, age, sex, and survival are somewhat linear (e.g., higher class = higher survival). It is also interpretable.
*   **KNN:** Might struggle if the dataset dimensionality is high or if the optimal `k` wasn't tuned. However, with proper scaling (which we did), it should provide competitive results.
*   **Selection:** If Accuracy is similar, **Logistic Regression** is preferred here because it provides coefficients telling us *which* factors (Sex, Class) were most important, whereas KNN is a "black box" based purely on distance.