# solution.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
import os

# --- Helper Functions ---

def ensure_dir(directory):
    """Ensure that a directory exists, creating it if it doesn't."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def sp_noise(image, prob):
    """
    Adds salt and pepper noise to an image.
    Args:
        image: The input image (numpy array).
        prob: The probability of a pixel being affected (e.g., 0.1 for 10%).
    Returns:
        The noisy image.
    """
    output = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0  # Pepper
            elif rdn > thres:
                output[i][j] = 255 # Salt
    return output

def calculate_psnr(img1, img2):
    """
    Calculates the Peak Signal-to-Noise Ratio between two images.
    """
    mse = np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

# --- Exercise Solutions ---

def exercise_1():
    """Solution for Exercise 1: Image Noise"""
    print("=========================================")
    print("Executing Exercise 1: Image Noise")
    print("=========================================")

    # Task 1: Read the image
    try:
        im1 = cv2.imread('Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)
        if im1 is None: raise FileNotFoundError
    except FileNotFoundError:
        print("Error: 'Images/cameraman.bmp' not found. Please ensure the image exists.")
        return

    # Task 2: Apply Gaussian noise
    mean = 0
    variance = 100
    sigma = variance ** 0.5
    gaussian_noise = np.random.normal(mean, sigma, im1.shape)
    im2 = im1 + gaussian_noise
    im2 = np.clip(im2, 0, 255).astype(np.uint8) # Clip values to be in [0, 255]
    cv2.imwrite('Images/cameraman_bruit_gauss_sig100.bmp', im2)
    print("Task 2: Gaussian noise added and saved.")

    # Task 3: Apply Salt & Pepper noise
    p = 0.1
    im3 = sp_noise(im1, p)
    cv2.imwrite('Images/cameraman_bruit_sel_poivre_p_10.bmp', im3)
    print("Task 3: Salt & Pepper noise added and saved.")
    
    # Task 4: Display and compare
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1), plt.imshow(im1, cmap='gray'), plt.title('Original (im1)'), plt.axis('off')
    plt.subplot(1, 3, 2), plt.imshow(im2, cmap='gray'), plt.title(f'Gaussian Noise σ²={variance} (im2)'), plt.axis('off')
    plt.subplot(1, 3, 3), plt.imshow(im3, cmap='gray'), plt.title(f'Salt & Pepper p={p*100}% (im3)'), plt.axis('off')
    plt.suptitle("Exercise 1: Noise Comparison")
    plt.show()

def exercise_2():
    """Solution for Exercise 2: Spatial Domain Filtering"""
    print("\n=========================================")
    print("Executing Exercise 2: Filtering")
    print("=========================================")
    
    # Task 1: Load images
    try:
        im1 = cv2.imread('Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread('Images/cameraman_bruit_gauss_sig100.bmp', cv2.IMREAD_GRAYSCALE)
        im3 = cv2.imread('Images/cameraman_bruit_sel_poivre_p_10.bmp', cv2.IMREAD_GRAYSCALE)
        if im1 is None or im2 is None or im3 is None: raise FileNotFoundError
    except FileNotFoundError:
        print("Error: Could not load images for Exercise 2. Please run Exercise 1 first.")
        return
        
    # Task 2: Mean Filter on Gaussian noise
    imf2 = cv2.blur(im2, (3, 3))
    print("Task 2: Mean filter (3x3) applied to Gaussian noisy image.")
    print(f"PSNR(Original, Gaussian Noise): {calculate_psnr(im1, im2):.2f} dB")
    print(f"PSNR(Original, Mean Filtered): {calculate_psnr(im1, imf2):.2f} dB -> Quality improved.")
    
    # Task 3: Median Filter on Salt & Pepper noise
    imf3 = cv2.medianBlur(im3, 3)
    imfm2 = cv2.medianBlur(im2, 3)
    print("\nTask 3: Median filter (3x3) applied.")
    print(f"PSNR(Original, S&P Noise): {calculate_psnr(im1, im3):.2f} dB")
    print(f"PSNR(Original, Median Filtered S&P): {calculate_psnr(im1, imf3):.2f} dB -> Quality significantly improved.")
    print(f"PSNR(Original, Median Filtered Gaussian): {calculate_psnr(im1, imfm2):.2f} dB")
    
    # Display results
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes[0, 0].imshow(im1, cmap='gray'), axes[0, 0].set_title('Original')
    axes[0, 1].imshow(im2, cmap='gray'), axes[0, 1].set_title('Gaussian Noise')
    axes[0, 2].imshow(imf2, cmap='gray'), axes[0, 2].set_title('Mean Filtered')
    axes[1, 0].imshow(im1, cmap='gray'), axes[1, 0].set_title('Original')
    axes[1, 1].imshow(im3, cmap='gray'), axes[1, 1].set_title('Salt & Pepper Noise')
    axes[1, 2].imshow(imf3, cmap='gray'), axes[1, 2].set_title('Median Filtered')
    for ax in axes.flat: ax.axis('off')
    plt.tight_layout()
    plt.show()

    # Task 5: Test various filters
    print("\nTask 5: Testing filter performances...")
    results = []
    
    # Filters to test: (Name, function, parameters)
    filters = [
        ("Mean 3x3", lambda img: cv2.blur(img, (3, 3))),
        ("Mean 5x5", lambda img: cv2.blur(img, (5, 5))),
        ("Mean 7x7", lambda img: cv2.blur(img, (7, 7))),
        ("Gaussian 3x3 s=2", lambda img: cv2.GaussianBlur(img, (3, 3), 2)),
        ("Gaussian 5x5 s=1.5", lambda img: cv2.GaussianBlur(img, (5, 5), 1.5)),
        ("Median 3x3", lambda img: cv2.medianBlur(img, 3)),
        ("Median 5x5", lambda img: cv2.medianBlur(img, 5)),
        ("Median 7x7", lambda img: cv2.medianBlur(img, 7)),
        ("Bilateral d=7", lambda img: cv2.bilateralFilter(img, 7, 40, 40)),
    ]

    for name, func in filters:
        for img_name, noisy_img in [("im2 (Gaussian)", im2), ("im3 (S&P)", im3)]:
            start_time = time.time()
            filtered_img = func(noisy_img)
            end_time = time.time()
            
            psnr = calculate_psnr(im1, filtered_img)
            duration = (end_time - start_time) * 1000  # in ms
            results.append((name, img_name, psnr, duration))

    print("-" * 60)
    print(f"{'Filter':<20} | {'Image':<15} | {'PSNR (dB)':<12} | {'Time (ms)':<10}")
    print("-" * 60)
    for name, img_name, psnr, duration in results:
        print(f"{name:<20} | {img_name:<15} | {psnr:<12.2f} | {duration:<10.2f}")
    print("-" * 60)

def exercise_3():
    """Solution for Exercise 3: Nagao Filter"""
    print("\n=========================================")
    print("Executing Exercise 3: Nagao Filter")
    print("=========================================")
    
    def nagao_filter(image, size=5):
        h, w = image.shape
        pad = size // 2
        img_padded = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
        output_img = np.zeros_like(image)

        # Define 9 subregions (masks) for a 5x5 window
        sub_regions = [
            # 3x3 center
            np.array([[0,0,0,0,0], [0,1,1,1,0], [0,1,1,1,0], [0,1,1,1,0], [0,0,0,0,0]], dtype=bool),
            # 4 corners and 4 edges
            np.array([[1,1,1,0,0], [1,1,1,0,0], [1,1,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], dtype=bool),
            np.array([[0,0,1,1,1], [0,0,1,1,1], [0,0,0,1,1], [0,0,0,0,0], [0,0,0,0,0]], dtype=bool),
            np.array([[0,0,0,0,0], [0,0,0,0,0], [1,1,0,0,0], [1,1,1,0,0], [1,1,1,0,0]], dtype=bool),
            np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,1,1], [0,0,1,1,1], [0,0,1,1,1]], dtype=bool),
            np.array([[1,1,0,0,0], [1,1,0,0,0], [1,1,0,0,0], [1,1,0,0,0], [1,1,0,0,0]], dtype=bool),
            np.array([[0,0,0,1,1], [0,0,0,1,1], [0,0,0,1,1], [0,0,0,1,1], [0,0,0,1,1]], dtype=bool),
            np.array([[1,1,1,1,1], [1,1,1,1,1], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], dtype=bool),
            np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [1,1,1,1,1], [1,1,1,1,1]], dtype=bool),
        ]

        for y in range(h):
            for x in range(w):
                window = img_padded[y:y+size, x:x+size]
                min_var = float('inf')
                best_mean = 0
                
                for region_mask in sub_regions:
                    if window.shape != region_mask.shape: continue
                    sub_window = window[region_mask]
                    if sub_window.size == 0: continue
                    
                    var = np.var(sub_window)
                    if var < min_var:
                        min_var = var
                        best_mean = np.mean(sub_window)
                
                output_img[y, x] = best_mean

        return output_img.astype(np.uint8)

    # Load images
    im1 = cv2.imread('Images/cameraman.bmp', cv2.IMREAD_GRAYSCALE)
    im2 = cv2.imread('Images/cameraman_bruit_gauss_sig100.bmp', cv2.IMREAD_GRAYSCALE)
    im3 = cv2.imread('Images/caman_bruit_sel_poivre_p_10.bmp', cv2.IMREAD_GRAYSCALE)

    print("Applying Nagao filter (5x5)... This may take a moment.")
    nagao_im2 = nagao_filter(im2, 5)
    nagao_im3 = nagao_filter(im3, 5)
    
    print("Nagao Filter Results:")
    print(f"PSNR(Original, Nagao on Gaussian): {calculate_psnr(im1, nagao_im2):.2f} dB")
    print(f"PSNR(Original, Nagao on S&P): {calculate_psnr(im1, nagao_im3):.2f} dB")
    
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1), plt.imshow(im2, cmap='gray'), plt.title('Gaussian Noise'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(nagao_im2, cmap='gray'), plt.title('Nagao Filtered'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(im3, cmap='gray'), plt.title('S&P Noise'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(nagao_im3, cmap='gray'), plt.title('Nagao Filtered'), plt.axis('off')
    plt.show()

def exercise_4():
    """Solution for Exercise 4: Mathematical Morphology"""
    print("\n=========================================")
    print("Executing Exercise 4: Morphology")
    print("=========================================")
    
    # Load and binarize the image
    try:
        im1 = cv2.imread('Images/Globules_rouges.jpg', cv2.IMREAD_GRAYSCALE)
        if im1 is None: raise FileNotFoundError
    except FileNotFoundError:
        print("Error: 'Images/Globules_rouges.jpg' not found.")
        return
        
    # Binarize using Otsu's method - finds the optimal threshold automatically
    _, imb1 = cv2.threshold(im1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Task 1: Basic morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    
    erosion = cv2.erode(imb1, kernel, iterations=1)
    dilation = cv2.dilate(imb1, kernel, iterations=1)
    opening = cv2.morphologyEx(imb1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(imb1, cv2.MORPH_CLOSE, kernel)
    
    print("Task 1: Morphological operations applied.")
    
    # Display morphology results
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 3, 1), plt.imshow(im1, cmap='gray'), plt.title('Original'), plt.axis('off')
    plt.subplot(2, 3, 2), plt.imshow(imb1, cmap='gray'), plt.title('Binarized (Otsu)'), plt.axis('off')
    plt.subplot(2, 3, 3), plt.imshow(erosion, cmap='gray'), plt.title('Erosion'), plt.axis('off')
    plt.subplot(2, 3, 4), plt.imshow(dilation, cmap='gray'), plt.title('Dilation'), plt.axis('off')
    plt.subplot(2, 3, 5), plt.imshow(opening, cmap='gray'), plt.title('Opening'), plt.axis('off')
    plt.subplot(2, 3, 6), plt.imshow(closing, cmap='gray'), plt.title('Closing'), plt.axis('off')
    plt.show()
    
    # Task 2: Separate and count red blood cells
    # Use opening to remove small noise and separate weakly connected cells
    sure_bg = cv2.dilate(opening, kernel, iterations=2)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1 # Add one to all labels so that sure background is not 0, but 1
    markers[unknown == 255] = 0 # Mark the region of unknown with zero
    
    # Apply watershed
    im1_color = cv2.cvtColor(im1, cv2.COLOR_GRAY2BGR)
    markers = cv2.watershed(im1_color, markers)
    im1_color[markers == -1] = [255, 0, 0] # Mark boundaries in red
    
    num_cells = len(np.unique(markers)) - 2 # Subtract background and boundary markers
    print(f"Task 2: Separated and counted cells. Estimated count: {num_cells}")
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1), plt.imshow(opening, cmap='gray'), plt.title('Cleaned Image (Opening)'), plt.axis('off')
    plt.subplot(1, 2, 2), plt.imshow(im1_color), plt.title(f'Watershed Segmentation ({num_cells} cells)'), plt.axis('off')
    plt.show()

    # Task 3: Skeletonization
    # Note: cv2.ximgproc.thinning expects a binary image with white foreground
    skeleton = cv2.ximgproc.thinning(imb1, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
    print("Task 3: Skeletonization applied.")
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1), plt.imshow(imb1, cmap='gray'), plt.title('Binarized'), plt.axis('off')
    plt.subplot(1, 2, 2), plt.imshow(skeleton, cmap='gray'), plt.title('Skeleton (Zhang-Suen)'), plt.axis('off')
    plt.show()

# --- Main Execution ---
if __name__ == '__main__':
    # Ensure the output directory exists
    ensure_dir('Images')
    
    exercise_1()
    exercise_2()
    # exercise_3() # This is slow, uncomment to run
    exercise_4()