
# **Low-Pass vs High-Pass Filters**

### **1. Low-Pass Filter (LPF)**

**Purpose:**

- Smooths an image and reduces high-frequency components.
    
- Used to **remove noise or blur fine details**.
    

**How it works:**

- Replaces each pixel with the **average of its neighbors**.
    
- Effectively **removes rapid intensity changes** while preserving low-frequency regions.
    

**Example: 3×3 Mean Filter (LPF)**

$$  
\text{Kernel} = \frac{1}{9}  
\begin{bmatrix}  
1 & 1 & 1 \  
1 & 1 & 1 \  
1 & 1 & 1  
\end{bmatrix}  
$$

**Effect:**

- Smooths edges slightly.
    
- Reduces noise.
    

---

### **2. High-Pass Filter (HPF)**

**Purpose:**

- Enhances **edges and fine details** by emphasizing high-frequency components.
    
- Used for **edge detection or sharpening**.
    

**How it works:**

- Measures **difference between a pixel and its neighbors**.
    
- Rapid intensity changes (edges) remain, smooth regions go toward zero.
    

**Calculation of HPF Kernel:**

- A common way is **subtracting the low-pass kernel from the identity**:
    

$$  
\text{HPF Kernel} = \text{Delta Function} - \text{LPF Kernel}  
$$

- For a 3×3 filter:
    

1. **Start with LPF kernel (mean):**
    

$$  
LPF =  
\frac{1}{9}  
\begin{bmatrix}  
1 & 1 & 1 \  
1 & 1 & 1 \  
1 & 1 & 1 \
\end{bmatrix}  
$$

2. **Subtract from identity (center = 1, others = 0) or multiply appropriately:**
    

A simple **3×3 high-pass kernel**:

$$  
HPF =  
\begin{bmatrix}  
-1 & -1 & -1 \  
-1 & 8 & -1 \  
-1 & -1 & -1  
\end{bmatrix}  
$$

**Explanation:**

- The **center value (8)** minus the sum of the neighbors (-1 each) ensures the sum of the kernel = 0.
    
- Zero-sum kernel → smooth areas → 0, edges → non-zero → highlighted.
    

---

### **3. Applying High-Pass Filter**

- Convolve the HPF matrix with the image:
    

$$  
I_{HP} = I \ast HPF  
$$

Where $\ast$ denotes convolution.

**Effect:**

- Flat areas → near zero intensity.
    
- Edges and rapid changes → high intensity → emphasized.
    

**Visual Example (conceptual 3×3 patch)**

```
Original:
100 102 101
103 105 104
101 103 102

After HPF:
  0   2   0
  3  10   3
  0   2   0
```

- Bright values correspond to edges; flat regions → 0 or small values.
    

---

### **4. Summary Table**

|Property|Low-Pass Filter|High-Pass Filter|
|---|---|---|
|Purpose|Smoothing, noise removal|Edge detection, sharpening|
|Kernel Sum|1 (averaging)|0 (zero-sum)|
|Frequency|Preserves low frequencies|Preserves high frequencies|
|Effect on Image|Blurs details|Highlights edges|
|Example Kernel|$\frac{1}{9}\begin{bmatrix}1 & 1 & 1\1 & 1 & 1\1 & 1 & 1\end{bmatrix}$|$\begin{bmatrix}-1 & -1 & -1\-1 & 8 & -1\-1 & -1 & -1\end{bmatrix}$|

---
