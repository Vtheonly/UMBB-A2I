--- 
title: Image Manipulation and Transformations
---

Once an image is loaded as a NumPy array, you can perform a wide range of manipulations. These include accessing/modifying individual pixels, resizing, rotating, cropping, and applying filters. These operations are fundamental to the lab exercises.

# Keywords
`#OpenCV` `#NumPy` `#ImageManipulation` `#Transformation` `#Pixel` `#Resize` `#Rotate` `#Crop` `#Blur`

---

## 1. Accessing and Modifying Pixels

Since an image is a NumPy array, you can access pixel values using array indexing. The coordinate system is `(y, x)` or `(row, column)`.

### Accessing a Pixel
- **Grayscale Image:** `pixel_value = img[100, 150]` (at row 100, column 150)
- **Color Image:** `bgr_value = img[100, 150]` (returns a list `[Blue, Green, Red]`)

### Modifying a Pixel
You can change a pixel's value by assigning a new one.

#### Example from Lab (`Lab_tp4.py`)
The code changes the color of the pixels in the middle row to red.

```python
import cv2
import numpy as np

img = cv2.imread('Images/pepper.bmp')
height, width, _ = img.shape

# The center row index
center_row = int(height / 2)

# Loop through each column (pixel) in the center row
for i in range(width):
    # Assign the color red to the pixel at (center_row, i)
    # OpenCV uses BGR format, so red is [0, 0, 255]
    img[center_row, i] = [0, 0, 255]

cv2.imshow('Red Line Added', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
**Note:** This `for` loop is illustrative but slow for large images. NumPy provides much faster ways to perform such operations, which we will cover later.

---

## 2. Cropping Images (Slicing)

Cropping is simply selecting a rectangular region of the image. In NumPy, this is done via **array slicing**. This is a critical concept you asked about.

### NumPy Slicing Syntax
The syntax for slicing a 2D array is: `array[startY:endY, startX:endX]`

- `startY:endY`: The range of rows to select (Y-axis).
- `startX:endX`: The range of columns to select (X-axis).
- **Important:** The `end` index is **exclusive**. `0:100` includes indices 0 through 99.

#### Example from Lab (`Lab_tp4.py`)
This code crops a `120x200` region from the image.

```python
import cv2

imgOG = cv2.imread('Images/pepper.bmp')

# Define the top-left corner of the crop
y = 30
x = 200
# Define the height and width of the crop
h = 120
w = 200

# Perform the slice
# Rows from y to y+h
# Columns from x to x+w
cropped_image = imgOG[y : y+h, x : x+w]

cv2.imshow('Original Image', imgOG)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
This is the most efficient way to crop an image.

---

## 3. Resizing Images

`cv2.resize()` changes the dimensions of an image.

| Parameter |
| :--- |
| `src` |
| `dsize` |
| `interpolation`|

| Description |
| :--- |
| The source image. |
| The desired new size as a tuple `(width, height)`. |
| (Optional) The method used to fill in pixel values. `cv2.INTER_AREA` is good for shrinking, `cv2.INTER_CUBIC` or `cv2.INTER_LINEAR` for enlarging. |

| Example from Lab |
| :--- |
| `imgOG` |
| `(new_width, new_height)` |
| (Not specified, uses default) |

#### Example from Lab (`Lab_tp4.py`)
This code resizes the image to half its original height.

```python
import cv2

imgOG = cv2.imread('Images/pepper.bmp')
h, w, _ = imgOG.shape

# Define the new dimensions
new_width = w       # Keep original width
new_height = h // 2 # Half the original height (integer division)

# Resize the image
resized_image = cv2.resize(imgOG, (new_width, new_height))

print(f"Original shape: {imgOG.shape}")
print(f"Resized shape: {resized_image.shape}")

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 4. Rotating Images

Rotation is a more complex transformation that involves two steps:
1.  **`cv2.getRotationMatrix2D()`**: Creates a `2x3` transformation matrix.
2.  **`cv2.warpAffine()`**: Applies the transformation matrix to the image.

#### Example from Lab (`Lab_tp4.py`)

```python
import cv2

imgOG = cv2.imread('Images/pepper.bmp')
h, w, _ = imgOG.shape

# 1. Define the center of rotation
center_point = (w // 2, h // 2)
# 2. Define the angle of rotation (in degrees)
angle = 90
# 3. Define the scale factor (1.0 means no scaling)
scale = 1.0

# 4. Get the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center_point, angle, scale)
print("Rotation Matrix:\n", rotation_matrix)

# 5. Apply the affine transformation
# The third argument is the output image size (width, height)
rotated_image = cv2.warpAffine(imgOG, rotation_matrix, (w, h))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 5. Blurring (Filtering)

Blurring, or smoothing, is a common operation to reduce image noise. It's a form of low-pass filtering. `Lab_solution.py` and `Lab_tp4.py` use several types.

### Gaussian Blur (`cv2.GaussianBlur`)
This is one of the most common blurring methods. It uses a Gaussian kernel.

| Parameter |
| :--- |
| `src` |
| `ksize` |
| `sigmaX` |

| Description |
| :--- |
| The source image. |
| The kernel size as `(width, height)`. Must be **positive and odd**. |
| The standard deviation in the X direction. `0` means it's calculated from kernel size. |

| Example from Lab |
| :--- |
| `imgOG` |
| `(15, 15)` |
| `0` |

A larger kernel size or a larger sigma value results in a more blurred image.

#### Example from Lab (`Lab_tp4.py`)
```python
import cv2

imgOG = cv2.imread('Images/pepper.bmp')

# Apply a 15x15 Gaussian blur
blurred_image = cv2.GaussianBlur(imgOG, (15, 15), 0)

cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Other blurring functions seen in `Lab_solution.py` include:
- **`cv2.blur()`**: A simple mean filter.
- **`cv2.medianBlur()`**: Excellent for removing "salt and pepper" noise.
- **`cv2.bilateralFilter()`**: A more advanced filter that blurs while preserving edges.
