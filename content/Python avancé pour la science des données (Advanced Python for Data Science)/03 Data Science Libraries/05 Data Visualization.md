# Data Visualization (Matplotlib & Seaborn)

## 1. Matplotlib: The Two Interfaces
Matplotlib is confusing because there are two ways to use it. Always prefer the **Object-Oriented (OO)** approach for control.

1.  **Functional (Pyplot):** `plt.plot()`. Quick, easy, but hard to customize complex plots.
2.  **Object-Oriented:** Explicitly creating Figure and Axes objects.

```python
# OO Approach
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)
ax.set_title("Title")
```

*   **Figure:** The physical window/canvas.
*   **Axes:** The actual plot (x/y region) inside the figure.

## 2. Choosing the Right Plot

| Chart Type | Purpose | Matplotlib Func | Seaborn Func |
| :--- | :--- | :--- | :--- |
| **Histogram** | Distribution of 1 variable | `ax.hist()` | `sns.histplot()` |
| **Box/Violin** | Distribution + Outliers | `ax.boxplot()` | `sns.boxplot()` / `sns.violinplot()` |
| **Scatter** | Relationship between 2 vars | `ax.scatter()` | `sns.scatterplot()` |
| **Bar** | Comparison of Categories | `ax.bar()` | `sns.barplot()` |
| **Heatmap** | Correlation Matrix | N/A | `sns.heatmap()` |

## 3. Seaborn Features
Seaborn is built on top of Matplotlib. It makes complex statistical plots easy.
*   **`hue` parameter:** Adds a 3rd dimension using color (e.g., Color points by 'Gender').
*   **`pairplot`:** Automatically plots pairwise relationships for an entire dataset.
*   **Integration:** Works directly with Pandas DataFrames.

## 4. Interactive Plots (Plotly)
Unlike Matplotlib (static images), Plotly generates HTML/JS plots.
*   Features: Zoom, Pan, Hover tooltips.
*   `import plotly.express as px`

## 5. Basemap / Cartopy
Used for Geospatial data.
*   **Warning:** Basemap is deprecated. `Cartopy` is the modern standard, though legacy tutorials often use Basemap.
*   Allows drawing coastlines, countries, and projecting lat/long coordinates onto a map.
