
## **Connectivity and Neighbors in Digital Images**

---

### **Clarifying the Question**

We want to understand:

1. Why we need to define _neighbors_ in digital images.
    
2. What happens when we use **4-connectivity** versus **8-connectivity**, and how a thin diagonal line can appear disconnected in one but continuous in the other.
    

---

### **Why We Need Neighbors**

Digital images are made of **discrete pixels**, not continuous ink.  
When we analyze or segment an image, we must define what it means for pixels to be **connected** — for example, when identifying shapes, regions, or object boundaries.

We do this by defining a **neighborhood system** (4-neighbors or 8-neighbors) which determines:

- Which pixels belong to the same region.
    
- How to traverse or label connected components.
    
- How to detect object boundaries or connectivity in binary images.
    

Without a neighborhood definition, the concept of “connectedness” would not exist — pixels would just be isolated points.

---

### **4-Connectivity and 8-Connectivity**

Let $P(x, y)$ be a pixel.

---

#### **1. 4-Connectivity $N_4(P)$ **

The **4-neighbors** of ( P ) are its immediate **horizontal and vertical** neighbors:

$$  
N_4(P) = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}  
$$

That means each pixel is connected only to the ones directly above, below, left, or right.

**Visual (conceptual):**

```
          (x, y-1)
             ↑
(x-1,y) ← P(x,y) → (x+1,y)
             ↓
          (x, y+1)
```

This uses the **Manhattan distance** rule:

$$  
|x_1 - x_2| + |y_1 - y_2| = 1  
$$

---

#### **2. 8-Connectivity $N_8(P)$ **

The **8-neighbors** of ( P ) include both the 4 direct neighbors **and** the 4 diagonal ones:

$$  
N_8(P) = {(x+i, y+j) \mid i, j \in {-1, 0, 1}, (i, j) \neq (0,0)}  
$$

**Visual (conceptual):**

```
(x-1,y-1)       (x, y-1)     (x+1,y-1)
      \            ↑          /
     (x-1,y)  ← P(x,y) → (x+1,y)
      /            ↓          \
(x-1,y+1)       (x, y+1)     (x+1,y+1)
```

This uses the **Chessboard distance** rule:

$$  
\max(|x_1 - x_2|, |y_1 - y_2|) = 1  
$$

---

### **Why Connectivity Matters**

Connectivity defines how algorithms interpret **continuous structures** in binary images.  
For example, in image segmentation, edge detection, or connected-component labeling, we use connectivity to determine whether pixels form one object or multiple.

---

### **Example: A Diagonal Line**

Below are two **7×7 binary matrices**, where `1` represents a white (object) pixel and `0` represents background.

#### **Matrix Representation**

$$
\begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

#### **Interpretation**

- **Under 4-Connectivity:**
    
    - Each `1` touches the next **only diagonally**, not vertically or horizontally.
        
    - Therefore, they are **not connected**.
        
    - The algorithm would detect **7 separate components**.
        
- **Under 8-Connectivity:**
    
    - Diagonal adjacency **counts as a connection**.
        
    - The same diagonal line is seen as **one continuous object**.
        
    - The algorithm detects **1 connected component**.
        

---

### **Visual Concept**

Under **4-Connectivity**, the connection can only move like a city grid — up, down, left, or right.

Under **8-Connectivity**, it can move like a **king in chess** — in any direction, including diagonals.

---

### **Example: Mixed Region**

$$
\begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$$

- **With 4-Connectivity:**  
    The chain appears **broken** into separate clusters.
    
- **With 8-Connectivity:**  
    The pixels form **one continuous diagonal region**.
    

---

### **Summary Table**

|Property|4-Connectivity|8-Connectivity|
|---|---|---|
|Neighbor Type|Horizontal + Vertical|Adds 4 Diagonals|
|Distance Metric|Manhattan|Chessboard|
|Number of Neighbors|4|8|
|Diagonal Connection|Not connected|Connected|
|Thin Diagonal Line|Appears broken|Continuous|
|Use Case|Preserving separate regions|Ensuring smooth connectivity|

---

### **Final Insight**

The choice between 4- and 8-connectivity determines **how an algorithm perceives structure**.  
When analyzing thin or diagonal shapes, **4-connectivity may break continuity**, while **8-connectivity preserves it**.

In practice:

- Use **4-connectivity** when you want strict, grid-based separation (to avoid diagonal merging).
    
- Use **8-connectivity** when you want natural visual continuity, especially for edges or thin lines.
