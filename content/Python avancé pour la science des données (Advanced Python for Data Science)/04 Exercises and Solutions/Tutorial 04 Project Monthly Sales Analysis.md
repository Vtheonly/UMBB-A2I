
## 1. Overview
This project represents a complete Data Science workflow: **Simulation -> Analysis -> Reporting**.
We simulate monthly sales data for four products (A, B, C, D) and perform a deep dive to find trends, growth rates, and seasonal patterns.

## 2. Methodology

### Step 1: Data Generation (NumPy)
Since we have no database, we used `numpy.random.randint` to generate realistic integer sales figures.
*   **Time Index:** Created using `pd.date_range(freq='M')` to generate exactly 12 month-end dates. This is essential for Time Series plotting.

### Step 2: Feature Engineering
We added columns that did not exist in the raw data:
*   **`MoM_Growth`**: `df.pct_change()`. This calculates the percentage jump from Jan to Feb, Feb to March, etc. Positive means growth; negative means decline.
*   **`Max_Sales_Product`**: `df.idxmax(axis=1)`.
    *   *Logic:* `max()` gives the number (e.g., 100). `idxmax()` gives the **label** (e.g., "Product_A"). This helps us answer: "Who won this month?"

### Step 3: Visualization (Seaborn/Matplotlib)
*   **Line Chart:** Shows the "Story" over time (ups and downs).
*   **Stacked Bar:** Shows the "Volume". It lets us see the total monthly revenue while still seeing the contribution of each product.
*   **Heatmap:** The most dense info. Darker colors = Higher sales. Good for spotting seasonality (e.g., a dark vertical stripe in July means a good summer).
*   **Boxplot:** Shows stability.
    *   *Small Box:* Consistent sales (Reliable).
    *   *Large Box/Whiskers:* Volatile sales (Risky).

## 3. Key Findings
*   **Product A** is the market leader with the highest median sales.
*   **Product D** struggles to compete and has the lowest variance and lowest total.
*   **Seasonality:** (Depends on the random seed, but generally observable in the Heatmap).

## 4. How to Run
1.  Ensure you have the libraries installed: `pip install pandas numpy matplotlib seaborn`
2.  Open **Tutorial 04 Project - Monthly Sales Analysis.ipynb**.
3.  Run all cells. The script will automatically create a `data/` folder and save the CSV reports (`initial.csv`, `final.csv`, `output.csv`) there.