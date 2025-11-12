---
title: Introduction to Matplotlib for Image Display
---

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. In the context of our image processing labs, we use it to display multiple images in a single window for comparison, add titles, and control their appearance.

While `cv2.imshow()` is great for quickly displaying a single image, Matplotlib offers far more control and is better for creating figures for reports and analysis.

# Keywords
`#Matplotlib` `#Plotting` `#Visualization` `#imshow` `#subplot`

---

## The Core Workflow for Displaying Images

The `Lab_solution.py` script follows a standard pattern for displaying multiple images:

1.  **`plt.figure()`**: Create a new figure (the window that holds the plots).
2.  **`plt.subplot()`**: Define a grid layout and select which subplot to draw on.
3.  **`plt.imshow()`**: Display the image data on the selected subplot.
4.  **`plt.title()`**: Add a title to the current subplot.
5.  **`plt.axis('off')`**: Hide the x and y axes for a cleaner look.
6.  **`plt.show()`**: Display the figure.

Let's break down each function.

### `plt.figure(figsize=(width, height))`
Creates a figure object. The `figsize` argument is optional but very useful. It's a tuple specifying the width and height of the figure in inches.

#### Example from Lab (`exercise_1`)
```python
# Creates a figure that is 15 inches wide and 5 inches tall.
plt.figure(figsize=(15, 5)) 
```

### `plt.subplot(rows, cols, index)`
This is the key to displaying multiple images. It divides the figure into a grid of `rows` and `cols` and selects the plot at `index` (which starts at 1).

#### Example from Lab (`exercise_1`)
The lab displays three images side-by-side. This means 1 row and 3 columns.

```python
# --- First Image ---
# Select the 1st plot in a 1x3 grid
plt.subplot(1, 3, 1) 
plt.imshow(im1, cmap='gray')
plt.title('Original (im1)')

# --- Second Image ---
# Select the 2nd plot in a 1x3 grid
plt.subplot(1, 3, 2)
plt.imshow(im2, cmap='gray')
plt.title('Gaussian Noise')

# --- Third Image ---
# Select the 3rd plot in a 1x3 grid
plt.subplot(1, 3, 3)
plt.imshow(im3, cmap='gray')
plt.title('Salt & Pepper')
```

### `plt.imshow(image, cmap='gray')`
This is the function that actually draws the image data.

- **`image`**: The image data, as a NumPy array.
- **`cmap='gray'`**: This is **critical** for grayscale images. `cmap` stands for "color map". If you display a 2D (grayscale) array without specifying `cmap='gray'`, Matplotlib will use a default color map (like 'viridis'), resulting in a false-color image (often shades of purple and yellow). You must tell it to use a gray color map to see the image correctly.

**BGR vs. RGB:**
A major difference between OpenCV and Matplotlib is the channel order for color images.
- **OpenCV:** BGR (Blue, Green, Red)
- **Matplotlib:** RGB (Red, Green, Blue)

If you display a color image loaded with `cv2.imread()` directly in `plt.imshow()`, the colors will be wrong (e.g., blue and red will be swapped).

**Correct Way to Display a CV2 Color Image in Matplotlib:**
```python
import cv2
import matplotlib.pyplot as plt

# Load image with OpenCV (it's in BGR order)
img_bgr = cv2.imread('Images/pepper.bmp')

# Convert it from BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Correct Colors")
plt.show()
```

### `plt.title()`, `plt.axis()`, `plt.show()`
- **`plt.title('My Title')`**: Sets the title for the *currently active* subplot.
- **`plt.axis('off')`**: Hides the numbered axes, which are generally not needed when just displaying images.
- **`plt.show()`**: Renders the complete figure with all its subplots and displays it. The script execution will pause here until the Matplotlib window is closed.

### Other Useful Functions from the Lab
- **`plt.suptitle("My Main Title")`**: Adds a centered title for the entire figure, above all subplots.
- **`plt.tight_layout()`**: Automatically adjusts subplot params so that the subplots fit into the figure area. It's great for preventing titles and labels from overlapping.