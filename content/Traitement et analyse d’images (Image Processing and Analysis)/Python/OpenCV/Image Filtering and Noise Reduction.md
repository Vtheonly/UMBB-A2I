---
title: Image Filtering and Noise Reduction
---

Image filtering is a process where a **kernel** (a small matrix) is applied to an image to modify its pixels. This is used for blurring, sharpening, edge detection, and noise reduction. The `Lab_solution.py` script for **Exercise 2** focuses on using filters to reduce noise.

# Keywords
`#OpenCV` `#Filtering` `#NoiseReduction` `#Blur` `#MedianFilter` `#PSNR`

---

## The Concept of a Kernel

A kernel is a small matrix of numbers. The filter works by sliding this kernel over every pixel of the input image. At each position, a new value for the center pixel is calculated based on the values of its neighbors covered by thekernel.

![Kernel Operation](https://i.imgur.com/hY8tJg8.png)
*Fig: A 3x3 kernel sliding over an image.*

---

## Types of Noise

The lab introduces two common types of image noise:

1.  **Gaussian Noise:**
    - Appears as small, random variations in brightness across the entire image.
    - Looks like fine grain.
    - Caused by sensor noise, poor lighting.
    - **Best treated with:** Mean or Gaussian filters.

2.  **Salt and Pepper Noise:**
    - Appears as random black (`pepper`) and white (`salt`) pixels scattered across the image.
    - Caused by transmission errors or faulty sensor elements.
    - **Best treated with:** Median filters.

---

## Filtering Functions from the Lab

### 1. Mean Filter (`cv2.blur()`)

This is the simplest type of blur filter. It replaces each pixel's value with the **average (mean)** of all the pixel values in the kernel window.

- **Effect:** It smooths the image and is effective at reducing Gaussian noise.
- **Drawback:** It blurs edges along with the noise.

#### Example from Lab (`exercise_2`)
```python
# im2 is the image with Gaussian noise
# (3, 3) is the kernel size
imf2 = cv2.blur(im2, (3, 3))
```
A larger kernel size (e.g., `(5, 5)`) will produce a more blurred result.

### 2. Median Filter (`cv2.medianBlur()`)

This filter replaces each pixel's value with the **median** of all the pixel values in the kernel window.

- **How it works:** It sorts all the pixel values in the kernel window and picks the middle value.
- **Effect:** It is extremely effective at removing salt and pepper noise. Because the random black (0) and white (255) pixels are outliers, they rarely become the median value.
- **Advantage:** It is much better at preserving edges than the mean filter.

#### Example from Lab (`exercise_2`)
```python
# im3 is the image with Salt & Pepper noise
# 3 is the kernel size (for a square 3x3 kernel)
imf3 = cv2.medianBlur(im3, 3)
```

### 3. Gaussian Filter (`cv2.GaussianBlur()`)
This is similar to the mean filter, but it uses a weighted average. Pixels closer to the center of the kernel are given more importance (weight).

- **Effect:** Produces a smoother, more natural-looking blur than the simple mean filter and is very effective against Gaussian noise.

### 4. Bilateral Filter (`cv2.bilateralFilter()`)
This is an advanced filter that is highly effective at noise reduction while keeping edges sharp. It considers both the spatial distance of pixels (like the Gaussian filter) and the difference in pixel intensity.

---

## Measuring Filter Performance: PSNR

How do we know if a filter "improved" an image? The lab uses **Peak Signal-to-Noise Ratio (PSNR)**.

- **What it is:** A metric that measures the quality of a reconstructed or modified image compared to its original, clean version.
- **How to interpret it:**
    - **Higher PSNR = Better Quality.** A higher value means the filtered image is more similar to the original.
    - It is measured in decibels (dB).

The `calculate_psnr` function in the lab implements this formula. By comparing the PSNR before and after filtering, you can objectively measure the filter's effectiveness.

#### Example from Lab (`exercise_2`)
```python
# PSNR before filtering
psnr_before = calculate_psnr(im1, im2) # (Original vs. Noisy)
# PSNR after filtering
psnr_after = calculate_psnr(im1, imf2) # (Original vs. Filtered)

# If psnr_after > psnr_before, the filter improved the image quality.
print(f"PSNR(Original, Gaussian Noise): {psnr_before:.2f} dB")
print(f"PSNR(Original, Mean Filtered): {psnr_after:.2f} dB -> Quality improved.")
```

The table generated at the end of `exercise_2` is a perfect summary, showing which filters perform best (highest PSNR) for each type of noise.