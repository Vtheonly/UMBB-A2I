# Tutorial 04: NumPy Mastery 🧮

## 1. Overview
This tutorial focuses on **NumPy (Numerical Python)**, the library that underpins almost all Data Science tools in Python (including Pandas, Scikit-Learn, and Matplotlib). 

Unlike standard Python lists, NumPy uses **C-based arrays**, which are:
*   **Faster:** Operations run in optimized C code.
*   **Memory Efficient:** Stores data in contiguous memory blocks.
*   **Vectorized:** Allows math on whole arrays without writing `for` loops.

## 2. Exercise 1: Temperature Analysis 🌡️
*File: Tutorial 04: Essential Python Libraries - NumPy.ipynb*

We manipulate a small dataset representing temperatures for 3 cities over 7 days.

### Key Concepts Used:
*   **Axes:** This is the most common point of confusion.
    *   `axis=0`: Acts on columns (Downward direction). Used to find max temp for *each city*.
    *   `axis=1`: Acts on rows (Horizontal direction). Used to find max temp for *each day*.
*   **Coordinate Retrieval:** `np.argmax(T)` gives a flat index (e.g., 15th element). We used `np.unravel_index` to convert that back to (Row, Col) format to find the exact Day and City.
*   **Broadcasting/Comparison:**
    *   `np.maximum(Array1, Array2)` compares two arrays element-by-element and creates a new array with the "winners".
*   **Boolean Masking:**
    *   We filtered days using logic: `(Annaba > Alger) & (Annaba > Oran)`.
    *   *Note:* In NumPy, use `&` for AND, `|` for OR. Standard Python `and/or` will cause a crash.

## 3. Exercise 2: Student Grades 🎓
*File: Tutorial 04: Essential Python Libraries - NumPy.ipynb*

We simulated a grade sheet for 100 students across 5 modules using Random Number Generation.

### Key Concepts Used:
1.  **Reproducibility:** `np.random.seed(101)` ensures that every time we run the code, we get the exact same "random" numbers. This is crucial for debugging.
2.  **Statistics:**
    *   Calculated `mean`, `median`, `var`, `std`.
    *   Used `np.percentile` to analyze grade distribution (25th vs 75th percentile).
3.  **Advanced Sorting:**
    *   `np.argsort()`: Instead of sorting the values, it returns the **indices** that would sort the array.
    *   We used this to find the IDs of the Top 5 students without losing their original ID numbers.
4.  **Matplotlib Integration:**
    *   NumPy arrays feed directly into `plt.bar` and `plt.boxplot`.
    *   Boxplots are excellent for detecting skewness (e.g., was the exam too hard? Are there outliers who scored 0 or 20?).

## 4. How to Run
Since this tutorial generates its own dummy data, you do not need any CSV files in the `data/` folder.

1.  Activate your environment: `source .venv/bin/activate` (or Windows equivalent).
2.  Open **Tutorial 04...ipynb**.
3.  Run all cells.