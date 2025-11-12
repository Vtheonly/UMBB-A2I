---
title: Introduction to OpenCV
---

OpenCV (Open Source Computer Vision Library) is a powerful library used for image and video analysis. In our labs, we use it to perform fundamental operations like reading, displaying, and manipulating images.

# Keywords
`#OpenCV` `#ComputerVision` `#ImageProcessing`

---

## How OpenCV Represents Images

The most crucial concept to understand is that **OpenCV treats images as NumPy arrays**.

- **NumPy Array:** Think of a NumPy array as a grid of numbers. For an image, these numbers represent pixel intensity or color.
- **Coordinates:** In OpenCV, image coordinates are specified as `(y, x)`, which corresponds to `(row, column)`. The origin `(0, 0)` is at the **top-left corner**.

### Image Types

1.  **Grayscale Image:**
    - A 2-dimensional NumPy array.
    - Each element in the array is a single value (typically from 0 to 255) representing the pixel's intensity.
    - `0` = Black, `255` = White.
    - **Shape:** `(height, width)`

2.  **Color Image (BGR):**
    - A 3-dimensional NumPy array.
    - For each pixel, there are three values representing the color channels.
    - **Important:** OpenCV loads color images in **BGR (Blue, Green, Red)** order by default, not the more common RGB.
    - **Shape:** `(height, width, 3)`

### Example: Understanding Image Shape

The `.shape` attribute of a NumPy array is essential. It tells you the dimensions of the image.

```python
import cv2
import numpy as np

# Load a color image
img_color = cv2.imread('Images/BoatsColor.bmp') 
# Create a dummy grayscale image for demonstration
img_gray = np.zeros((100, 150), dtype=np.uint8) # 100 rows, 150 columns

# Destructuring the shape tuple
height, width, channels = img_color.shape
print(f"Color Image - Height: {height}, Width: {width}, Channels: {channels}")
# Expected Output: Color Image - Height: 512, Width: 512, Channels: 3

h_gray, w_gray = img_gray.shape
print(f"Grayscale Image - Height: {h_gray}, Width: {w_gray}")
# Expected Output: Grayscale Image - Height: 100, Width: 150
```
This demonstrates **tuple unpacking** (or destructuring), where we assign the elements of the `shape` tuple directly to variables like `height`, `width`, and `channels`.

---
## Core Functions

Here are some of the first functions you'll encounter in the labs.

### `cv2.imread()`
This function reads an image from a file.

| Parameter | Description | Example from Lab |
| :--- | :--- | :--- |
| `filename` | The path to the image file. | `'Images/BoatsColor.bmp'` |
| `flag` | (Optional) Specifies how the image should be read. | `cv2.IMREAD_GRAYSCALE` |

**Default Behavior:** If the `flag` is omitted, the image is loaded as a 3-channel BGR color image.

### `cv2.imshow()`
Displays an image in a window. The window automatically fits to the image size.

| Parameter | Description | Example from Lab |
| :--- | :--- | :--- |
| `winname` | The name of the window. | `'Input Image'` |
| `mat` | The image (NumPy array) to be shown. | `img` |

### `cv2.waitKey()`
Waits for a specified time (in milliseconds) for a key press.

- **`cv2.waitKey(0)`:** This is a special case that waits **indefinitely** until any key is pressed. This is useful for keeping an image window open until you are ready to close it.
- **`cv2.waitKey(25)`:** This would wait for 25ms. It's often used in loops for displaying video frames.

### `cv2.destroyAllWindows()`
Closes all the windows created by `cv2.imshow()`. It's good practice to call this at the end of your script to clean up.