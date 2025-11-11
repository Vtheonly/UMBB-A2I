
### Slide 1: The Definition and Core Formula

This first slide introduces convolution as a fundamental concept and presents its mathematical formula.

> **Slide's Message:** "Image Convolution: a very common operation in image processing... It consists of recalculating the value of a pixel by associating the values of its neighboring pixels."

This tells us that convolution is a **local operation**. The new value of a pixel depends not just on its old value, but also on the values of the pixels immediately surrounding it.

#### The Formula: An Ingredient-by-Ingredient Breakdown

The slide presents two formulas. The first is a high-level representation:

$$
g(x,y) = f(x,y) \otimes \text{filtre}(x,y)
$$

This says the **output image $g(x,y)$** is the result of convolving the **input image $f(x,y)$** with a **kernel $\text{filtre}(x,y)$**. The symbol $\otimes$ represents the convolution operation.

The second formula is the one that tells us *how* to actually compute it:

$$
g(x,y) = \sum_{i} \sum_{j} f(x+i, y+j) \cdot \text{filtre}(i,j)
$$

Let's break this down piece by piece, as illustrated on the slide:

1.  **The Output: $g(x,y)$**
    *   **What it is:** This represents a single pixel value in the new, output image. The coordinates $(x,y)$ are the location of the pixel we are trying to calculate.
    *   **From the slide:** This is labeled "Niveau de gris après convolution" (Grayscale level after convolution). It is the final result of our calculation for one point.

2.  **The Input Neighborhood: $f(x+i, y+j)$**
    *   **What it is:** This represents the pixel values from the **original input image**. The coordinates are a combination of the anchor point $(x,y)$ and an offset $(i,j)$.
    *   **What it does:** This term selects a specific neighbor. For a 3x3 kernel, the offsets $i$ and $j$ range from -1 to 1. For example, if we are calculating the output for pixel $(10, 20)$:
        *   When $(i,j) = (0,0)$, this term is $f(10,20)$, the center pixel.
        *   When $(i,j) = (-1,-1)$, this term is $f(9,19)$, the top-left neighbor.
    *   **From the slide:** This is labeled "Niveaux de gris initiaux" (Initial grayscale levels). It is the collection of pixel values that will be used in the calculation.

3.  **The Kernel's Weight: $\text{filtre}(i,j)$**
    *   **What it is:** This represents a single value from the kernel (or "mask"). The coordinates $(i,j)$ correspond directly to the offsets used for the input neighborhood.
    *   **What it does:** It assigns a weight, or a level of importance, to each neighbor. This is the "recipe" of the filter.
    *   **From the slide:** This is labeled "opérateur de convolution (noyau de convolution)" (convolution operator / convolution kernel).

4.  **The Core Operation and Aggregation: $\sum_{i} \sum_{j} (\dots \cdot \dots)$**
    *   The multiplication `·` calculates the **weighted influence** of a single neighbor.
    *   The double summation $\sum_{i} \sum_{j}$ instructs us to **sum up all these weighted influences** from every pixel in the neighborhood. This final sum becomes the value of our output pixel, $g(x,y)$.

### Slide 2: A Practical 3x3 Example

This slide makes the abstract formula concrete by "unrolling" it for a 3x3 kernel.

> **Slide's Message:** "A pixel $f(x,y)$ is replaced by a weighted sum of itself and its neighboring pixels."

Here, the kernel is represented by a matrix of weights, $W$:
$$
\begin{bmatrix}
W_1 & W_2 & W_3 \\
W_4 & W_5 & W_6 \\
W_7 & W_8 & W_9
\end{bmatrix}
$$
These weights correspond to the `filtre(i,j)` values. For example, $W_1$ corresponds to the weight for the top-left neighbor, where $(i,j) = (-1, -1)$. $W_5$ is the weight for the center pixel, where $(i,j) = (0,0)$.

The slide then shows the summation formula expanded explicitly:
$$
\begin{aligned}
g(x,y) = \quad & f(x-1, y-1) \cdot W_1 + f(x-1, y) \cdot W_2 + f(x-1, y+1) \cdot W_3 + \\
& f(x, y-1) \cdot W_4 + f(x, y) \cdot W_5 + f(x, y+1) \cdot W_6 + \\
& f(x+1, y-1) \cdot W_7 + f(x+1, y) \cdot W_8 + f(x+1, y+1) \cdot W_9
\end{aligned}
$$
This is the **exact same calculation** as the $\sum\sum$ formula from the first slide, but written out term by term for a 3x3 case. It clearly shows the process of multiplying each pixel in the neighborhood by its corresponding weight and adding them all up.

### Slide 3: Key Mathematical Properties

This slide explains the "rules" of convolution, which are critical for understanding how filters can be combined and optimized. The asterisk $*$ is used here as a shorthand for the convolution operator $\otimes$.

1.  **Additivity / Distributivity: $f * (h_1 + h_2) = (f * h_1) + (f * h_2)$**
    *   **What it means:** Convolving an image with a single kernel that is the sum of two other kernels gives the same result as convolving the image with each kernel separately and then adding the two resulting images together.
    *   **Why it's useful:** This property allows for the decomposition of complex filters into simpler parts.

2.  **Commutativity: $h_1 * h_2 = h_2 * h_1$**
    *   **What it means:** The order of convolution does not matter. The property also applies to the image and kernel: $f * h = h * f$.
    *   **Why it's useful:** It provides flexibility in how convolution operations are designed and implemented in software.

3.  **Associativity: $(f * h_1) * h_2 = f * (h_1 * h_2)$**
    *   **What it means:** Applying two filters to an image one after the other is equivalent to first convolving the two filters together to create a single new filter, and then applying that new filter to the image.
    *   **Why it's useful:** This is a powerful optimization. If you need to apply the same two filters repeatedly, you can pre-calculate their combined kernel ($h_{new} = h_1 * h_2$) once and then perform only one convolution on the image, saving significant computation time.

4.  **Separability: $h(x,y) = h_x(x) \cdot h_y(y)$**
    *   **What it means:** A 2D kernel $h(x,y)$ is "separable" if it can be expressed as the product of a 1D column vector $h_y(y)$ and a 1D row vector $h_x(x)$. The Gaussian kernel is a famous example.
    *   **Why it's so important:** This is the **most significant optimization property** for convolution. Instead of performing one computationally expensive 2D convolution, you can perform two much faster 1D convolutions:
        1.  First, convolve the image with the 1D row vector (as indicated by "Traitement selon x"). This processes all the rows.
        2.  Then, convolve the result of that operation with the 1D column vector ("Traitement selon y"). This processes all the columns.
    *   For an $N \times N$ kernel, a 2D convolution takes roughly $N^2$ multiplications per pixel. A separable convolution takes only $N+N = 2N$ multiplications per pixel. For a $7 \times 7$ kernel, this is a difference between 49 and 14 operations per pixel—a massive speed increase.