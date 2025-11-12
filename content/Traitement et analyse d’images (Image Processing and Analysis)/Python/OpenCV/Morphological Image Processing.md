---
title: Morphological Image Processing
---

Mathematical Morphology is a set of techniques used to process images based on their shapes. These operations are typically performed on **binary** (black and white) images. They use a **structuring element** (similar to a kernel in filtering) to probe the image and modify it.

**Exercise 4** in `Lab_solution.py` uses these techniques to isolate and count red blood cells in an image.

# Keywords
`#OpenCV` `#Morphology` `#Erosion` `#Dilation` `#Opening` `#Closing` `#Watershed`

---

## Binarization: The First Step

Morphological operations require a binary image. The lab uses **Otsu's Binarization** (`cv2.THRESH_OTSU`) to automatically find the optimal threshold value to convert a grayscale image to black and white.

```python
# im1 is the grayscale image of red blood cells
# cv2.THRESH_BINARY_INV inverts the colors (cells become white, background black)
_, imb1 = cv2.threshold(im1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
```

---

## The Structuring Element

This is a shape (like a square, circle, or cross) that we use to interact with the image. The lab uses an elliptical (oval) structuring element, which is good for the roundish shape of the cells.

```python
# Creates a 5x5 elliptical structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
```

---

## Fundamental Operations

### 1. Erosion (`cv2.erode()`)

Erosion **erodes away** the boundaries of the foreground objects (the white parts).

- **Effect:** It makes objects smaller. It is useful for removing small white noise and for separating two connected objects.
- **How it works:** A pixel in the output image is set to white (1) only if **all** pixels under the structuring element are white in the input image. Otherwise, it is set to black (0).

![Erosion](https://i.imgur.com/sT0mJcW.png)

### 2. Dilation (`cv2.dilate()`)

Dilation is the opposite of erosion. It **expands** the area of the foreground objects.

- **Effect:** It makes objects larger. It is useful for filling small holes or gaps in objects.
- **How it works:** A pixel in the output image is set to white (1) if **at least one** pixel under the structuring element is white in the input image.

![Dilation](https://i.imgur.com/u5I4b2h.png)

---

## Compound Operations

Erosion and dilation are often used in sequence.

### 3. Opening (`cv2.morphologyEx(..., cv2.MORPH_OPEN, ...)`

Opening is **Erosion followed by Dilation**.

- **Effect:** It is useful for **removing small noise "islands"** in the background (salt noise). It can also separate objects that are weakly connected.
- **Why it works:** The initial erosion removes the small noise spots. The subsequent dilation restores the size of the remaining larger objects without bringing back the noise.

### 4. Closing (`cv2.morphologyEx(..., cv2.MORPH_CLOSE, ...)`

Closing is **Dilation followed by Erosion**.

- **Effect:** It is useful for **filling small holes** inside foreground objects (pepper noise).
- **Why it works:** The initial dilation fills the holes. The subsequent erosion reduces the object size back to its approximate original size.

In `exercise_4`, **Opening** is chosen because the goal is to remove small artifacts and separate the touching blood cells.

---

## Application: Counting Cells with Watershed

The ultimate goal of `exercise_4` is to count the cells. This is a **segmentation** task. The lab uses the Watershed algorithm, a powerful but complex method.

Here's a simplified breakdown of the steps used in the lab:

1.  **Clean the Image:** An **Opening** operation is performed to remove noise and separate cells.
2.  **Identify "Sure Foreground":** The code finds areas that are definitely part of a cell. It does this by eroding the cleaned image, which shrinks the cells, leaving only their cores. This is achieved with `cv2.distanceTransform` and `cv2.threshold`.
3.  **Identify "Sure Background":** The code finds areas that are definitely not cells. This is done by dilating the cleaned image, which expands the cells, and the remaining black area is the sure background.
4.  **Identify the "Unknown" Region:** The region between the sure foreground and sure background is the unknown area—these are the boundaries of the cells that the algorithm needs to find.
5.  **Apply Watershed (`cv2.watershed()`):** The algorithm treats the image like a topographic map, "flooding" it from the "sure foreground" markers until the "dams" (watershed lines) that separate the different regions are found. These dams are the cell boundaries.
6.  **Count the Objects:** The final `markers` array contains a unique label for each identified cell. By counting the number of unique labels (and subtracting the background label), we get the cell count.

This is a classic and effective method for segmenting touching objects.