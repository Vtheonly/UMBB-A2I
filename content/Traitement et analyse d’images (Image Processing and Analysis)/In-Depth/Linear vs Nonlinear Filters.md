
## **1. Purpose**

Filtering helps modify an image by combining information from a pixel’s **neighborhood** — used for tasks like noise reduction, blurring, sharpening, or edge detection.

The key distinction is **how** the new pixel value is computed:

- **Linear filter:** uses **weighted sums** (convolution).
- **Nonlinear filter:** uses **nonlinear operations** (e.g., median, min, max).

---

## **2. Linear Filters**

A **linear filter** satisfies:

1. **Additivity:**  
   $F(a + b) = F(a) + F(b)$

2. **Homogeneity:**  
   $F(k \cdot a) = k \cdot F(a)$

That means the filter’s output is directly proportional to its input — it behaves like a linear system.

---

### **2.1 Mathematical Form**

For an image $I(x, y)$ and a kernel $h(i, j)$:

$$
I'(x, y) = \sum_i \sum_j h(i, j) \cdot I(x - i, y - j)
$$

This is a **convolution** operation.

---

### **2.2 Example: Mean (Average) Filter**

The 3×3 mean filter averages the 9 neighboring pixels:

$$
h(i,j) = \frac{1}{9}
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$

Let’s apply it to the neighborhood:

$$
\begin{bmatrix}
20 & 22 & 23 \\
19 & 255 & 24 \\
18 & 21 & 20
\end{bmatrix}
$$

Compute the mean:

$$
\text{Mean} = \frac{20 + 22 + 23 + 19 + 255 + 24 + 18 + 21 + 20}{9} = 46.89
$$

So, the new center pixel becomes **46.89**.

---

### **2.3 Interpretation**

- The high value **255** (a noisy outlier) strongly influences the result.  
- The output is **blurred** and affected by noise.  
- The operation is **linear** because it’s a weighted sum.

---

## **3. Nonlinear Filters**

A **nonlinear filter** doesn’t satisfy the linearity conditions.  
It uses nonlinear logic (e.g., sorting, thresholding, or min/max operations) to choose the new pixel value.

---

### **3.1 Example: Median Filter**

For the same 3×3 patch:

$$
\begin{bmatrix}
20 & 22 & 23 \\
19 & 255 & 24 \\
18 & 21 & 20
\end{bmatrix}
$$

Flatten the neighborhood:

$$
[20, 22, 23, 19, 255, 24, 18, 21, 20]
$$

Sort them:

$$
[18, 19, 20, 20, 21, 22, 23, 24, 255]
$$

The **median** (middle value) is **21**.

So, the new center pixel becomes **21**.

---

### **3.2 Interpretation**

- The extreme outlier (255) is **ignored**.  
- The output preserves the **true neighborhood intensity**.  
- The result is **nonlinear** because it’s not a weighted sum — sorting is involved.

---

## **4. Visual Comparison**

| Filter Type | Operation | Result (Center Pixel) | Effect |
|--------------|------------|-----------------------|--------|
| **Mean Filter** | Weighted average | 46.89 | Blurred; noise spreads |
| **Median Filter** | Median of values | 21 | Sharp; noise removed |

---

### **Visual Intuition**

| Concept | Illustration |
|----------|---------------|
| **Linear Filter** | Averages all neighbors equally — even extreme noise affects the result. |
| **Nonlinear Filter** | Chooses representative (median) value — robust to isolated noise pixels. |

---

## **5. Summary Table**

| Property               | **Linear Filter**          | **Nonlinear Filter**               |
| ---------------------- | -------------------------- | ---------------------------------- |
| Mathematical Operation | Weighted sum (convolution) | Nonlinear rule (median, min, etc.) |
| Example                | Mean, Gaussian, Sobel      | Median, Bilateral, Morphological   |
| Edge Handling          | Blurs edges                | Preserves edges                    |
| Behavior with Outliers | Sensitive                  | Robust                             |
| Speed                  | Typically faster           | Slightly slower                    |
| Used For               | Smoothing, edge detection  | Denoising without blur             |

---

## **6. Key Insight**

- **Linear filters** are efficient but blur details.  
- **Nonlinear filters** protect structural information and remove impulsive noise effectively.

---

### **Analogy**

| Type | Analogy |
|------|----------|
| Linear | Taking the **average** of everyone’s opinions — smooth but influenced by outliers. |
| Nonlinear | Taking the **median** opinion — ignores extremes and reflects the central tendency. |
