---
title: Introduction to NumPy for Image Processing
---

NumPy is the foundational library for numerical computing in Python. In our labs, it's essential because **images are represented as NumPy arrays**. Understanding NumPy is key to understanding image manipulation.

# Keywords
`#NumPy` `#Array` `#ImageProcessing` `#DataManipulation`

---

## The NumPy Array (`ndarray`)

A NumPy array, or `ndarray`, is a grid of values, all of the same type.

### Key Attributes
- **`shape`**: A tuple representing the dimensions of the array. For an image, this is `(height, width)` or `(height, width, channels)`.
- **`dtype`**: The data type of the elements in the array. For images, this is usually `np.uint8`.

### `np.uint8` - The Standard Image Data Type
- **`uint8`** stands for "unsigned 8-bit integer".
- **Unsigned:** The values cannot be negative.
- **8-bit:** The values can hold 2⁸ = 256 different values.
- **Range:** This means each pixel value must be in the range **[0, 255]**.

This is why `np.uint8` is perfect for representing grayscale and standard color images.

---

## Array Creation and Manipulation

The lab exercises use several functions to create and modify arrays.

### `np.copy()`
Creates a full copy of an array. This is crucial when you want to modify an image without altering the original.

#### Example from Lab (`Lab_solution.py`)
In the `sp_noise` function, a copy of the input image is created before noise is added.

```python
import numpy as np

# output = np.copy(image)
# This ensures that the original 'image' is not modified. 
# Any changes made to 'output' will not affect 'image'.
```
**Assignment vs. Copy:**
- `new_image = old_image` **does not** create a copy. It just makes another variable name point to the same data.
- `new_image = np.copy(old_image)` creates a completely independent duplicate.

### `np.random.normal()`
Generates an array of random numbers from a normal (Gaussian) distribution. This is used in `exercise_1` to create Gaussian noise.

| Parameter | Description | Example from Lab |
| :--- | :--- | :--- |
| `loc` | The mean ("center") of the distribution. | `mean = 0` |
| `scale` | The standard deviation of the distribution. | `sigma = variance ** 0.5` |
| `size` | The shape of the output array. | `im1.shape` (to match the image) |

#### Example
```python
import numpy as np

# Create a 3x3 array of random numbers with mean=0, std_dev=10
noise = np.random.normal(0, 10, (3, 3))
print(noise)
# Output will be a 3x3 array of floats, some negative.
```

### Adding Noise to an Image
When you add this `noise` array to an image array, the operation is performed **element-wise**. Each noise value is added to the corresponding pixel value.

```python
# From exercise_1:
# gaussian_noise = np.random.normal(mean, sigma, im1.shape)
# im2 = im1 + gaussian_noise 
```
The result `im2` is now a floating-point array, and its values can be outside the `[0, 255]` range. This leads to our next function.

### `np.clip()`
Clips (limits) the values in an array to be within a specified range. This is essential after operations like adding noise, which can create values outside the valid `[0, 255]` range for an image.

| Parameter | Description | Example from Lab |
| :--- | :--- | :--- |
| `a` | The input array. | `im2` |
| `a_min` | The minimum value. Anything less becomes this. | `0` |
| `a_max` | The maximum value. Anything more becomes this. | `255` |

#### Example from Lab (`exercise_1`)
```python
# im2 = np.clip(im2, 0, 255).astype(np.uint8)
```
This line is doing two things:
1.  **`np.clip(im2, 0, 255)`**: Any pixel value in `im2` that is less than 0 becomes 0. Any value greater than 255 becomes 255.
2.  **`.astype(np.uint8)`**: The array's data type is converted from float back to `uint8`, which is required for saving or displaying it as an image with OpenCV.

---

## Mathematical and Statistical Functions

NumPy provides fast functions for calculations.

### `np.mean()`
Calculates the average of the array elements. Used in `calculate_psnr`.

```python
# mse = np.mean((img1 - img2) ** 2)
# This calculates the Mean Squared Error (MSE) between two images.
# 1. (img1 - img2): Element-wise subtraction.
# 2. (...) ** 2: Element-wise square.
# 3. np.mean(...): Average of all the resulting values.
```

### `np.var()`
Calculates the variance of the array elements. Used in the `nagao_filter` to find the sub-window with the most uniform brightness. A low variance means the pixels in that region have similar values (i.e., it's a smooth area).

### `np.zeros_like()`
Creates a new array with the same shape and type as a given array, but filled with zeros.

```python
# output_img = np.zeros_like(image)
# If 'image' has shape (512, 512) and dtype uint8,
# 'output_img' will also be a 512x512 uint8 array, but all black.
```

### `np.unique()`
Finds the unique elements in an array. In `exercise_4`, it's used to count the number of cells identified by the watershed algorithm. Each cell is given a unique integer label, so counting the unique labels gives the cell count.