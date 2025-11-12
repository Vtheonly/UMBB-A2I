

## **Purpose of Quality Metrics**

In image processing, filtering operations aim to improve an image (e.g., by removing noise), but they can also introduce artifacts (e.g., blurring). Visual inspection is subjective. **Objective metrics** provide a quantitative, reproducible way to measure the fidelity of a result and compare the performance of different algorithms.

---

## **Mean Squared Error (MSE)**

MSE measures the cumulative squared error between two images. It represents the average of the squares of the differences between the pixel intensity values of the original and processed images.

### **Calculation**

For two grayscale images, $Im$ (original) and $Imf$ (filtered), of size $H \times W$:

$$
MSE = \frac{1}{H \cdot W} \sum_{i=0}^{H-1} \sum_{j=0}^{W-1} \big(Im[i,j] - Imf[i,j]\big)^2
$$

### **Interpretation**

- A lower MSE value indicates a smaller difference between the images, meaning higher fidelity.  
- An MSE of 0 means the images are identical.  
- **Insight:** The squaring of the difference term means that large errors are penalized much more heavily than small errors.

---

## **Peak Signal-to-Noise Ratio (PSNR)**

PSNR is a more common metric that builds upon MSE. It measures the ratio between the maximum possible power of a signal (the image) and the power of the corrupting noise that affects its fidelity.

### **Calculation**

PSNR is defined on a logarithmic scale (decibels, dB):

$$
PSNR = 10 \cdot \log_{10} \left( \frac{R^2}{MSE} \right)
$$

Where:

- $R$ is the maximum possible pixel value of the image. For an 8-bit grayscale image, $R = 255$.  
- $MSE$ is the Mean Squared Error calculated previously.

### **Interpretation**

- A **higher PSNR** value indicates a better quality reconstruction or a more effective filtering result.  
- Because of the logarithmic scale, PSNR aligns better with human perception of quality than MSE does.  
- Typical values for image processing range from 20 dB (poor) to over 40 dB (excellent).  
- An infinite PSNR occurs only if $MSE = 0$ (identical images).

---

## **Insights and Practical Notes**

1. **MSE vs PSNR**:  
   - MSE provides an absolute error measure (smaller is better).  
   - PSNR expresses the error in relation to the signal power on a logarithmic scale, making it more interpretable for human perception.

2. **Sensitivity to Outliers**:  
   - MSE is highly sensitive to large deviations due to squaring.  
   - PSNR inherits this sensitivity indirectly but compresses the scale logarithmically.

3. **Usage in Filtering**:  
   - When testing denoising or compression algorithms, compute both MSE and PSNR for objective comparison.  
   - Example: Comparing Gaussian filter vs median filter on the same noisy image. The algorithm with **lower MSE and higher PSNR** preserves more image fidelity.

4. **Relationship with Human Perception**:  
   - PSNR tends to correlate better with visual quality than MSE.  
   - However, very small visual artifacts may not significantly change PSNR but could be noticeable.

---

## **Summary Formulas**

$$
\text{MSE} = \frac{1}{H \cdot W} \sum_{i=0}^{H-1} \sum_{j=0}^{W-1} (Im[i,j] - Imf[i,j])^2
$$

$$
\text{PSNR} = 10 \cdot \log_{10} \left( \frac{R^2}{\text{MSE}} \right)
$$

Where $H \times W$ is the image size, $Im$ is the original image, $Imf$ is the filtered or processed image, and $R$ is the maximum pixel value.

---

## **Key Takeaways**

- **Lower MSE** → higher fidelity, fewer errors.  
- **Higher PSNR** → better visual quality and reconstruction.  
- Always use **both metrics** for quantitative comparison in image processing tasks.


# **Practical Scenarios for MSE and PSNR**

Below are several example scenarios comparing an original image $Im$ to a processed image $Imf$, showing MSE and PSNR values and their interpretations.

---

## **Scenario 1: Minimal Noise / Excellent Filtering**

- **Description:** Original image processed with a mild Gaussian filter.  
- **Calculated metrics:**  
  - $MSE = 10$  
  - $R = 255$  
  - $PSNR = 10 \cdot \log_{10} \frac{255^2}{10} \approx 38.1 \text{ dB}$

**Interpretation:**  
- Very low error → image is almost identical to original.  
- High PSNR (>35 dB) indicates excellent visual quality.  
- Only minor differences are perceptible, mostly imperceptible to the human eye.

---

## **Scenario 2: Moderate Noise / Reasonable Filtering**

- **Description:** Image corrupted by moderate Gaussian noise and filtered with a mean filter.  
- **Calculated metrics:**  
  - $MSE = 200$  
  - $R = 255$  
  - $PSNR = 10 \cdot \log_{10} \frac{255^2}{200} \approx 25.1 \text{ dB}$

**Interpretation:**  
- Moderate error → noticeable differences compared to original.  
- PSNR ~25 dB indicates acceptable quality but artifacts or blurring are noticeable.  
- Good filtering reduces noise but cannot fully restore original details.

---

## **Scenario 3: Severe Noise / Poor Filtering**

- **Description:** Image with salt-and-pepper noise processed with a linear mean filter.  
- **Calculated metrics:**  
  - $MSE = 1200$  
  - $R = 255$  
  - $PSNR = 10 \cdot \log_{10} \frac{255^2}{1200} \approx 17.3 \text{ dB}$

**Interpretation:**  
- High error → many pixel differences remain.  
- PSNR <20 dB indicates poor reconstruction.  
- Linear filter failed to remove impulse noise effectively; edges and details are strongly affected.

---

## **Scenario 4: Identical Images**

- **Description:** No processing; original image compared to itself.  
- **Calculated metrics:**  
  - $MSE = 0$  
  - $PSNR = \infty$ (division by zero in formula)

**Interpretation:**  
- No difference between images → perfect fidelity.  
- PSNR is infinite by definition.  
- Useful as a reference maximum quality.

---

## **Scenario 5: Different Types of Filters**

| Scenario | Filter | MSE | PSNR (dB) | Interpretation |
|----------|--------|-----|------------|----------------|
| Low Gaussian noise | Gaussian filter | 15 | 36.3 | Very good quality, small smoothing |
| Salt & Pepper noise | Median filter | 50 | 30.1 | Removes noise effectively, edges preserved |
| Salt & Pepper noise | Mean filter | 600 | 20.4 | Poor performance; edges blurred, noise persists |
| Motion blur | Wiener filter | 120 | 27.3 | Restores edges moderately, some artifacts remain |

---

## **Key Takeaways**

1. **Lower MSE** always indicates better fidelity.  
2. **Higher PSNR** correlates with visually better quality.  
3. For **impulse noise**, non-linear filters (like median) perform much better than linear filters, reflected in both lower MSE and higher PSNR.  
4. PSNR is more interpretable than MSE for humans because it scales the error relative to signal power.  
5. Infinite PSNR corresponds to perfect identity between original and processed images.

---

### **Formulas Recap**

$$
MSE = \frac{1}{H \cdot W} \sum_{i=0}^{H-1} \sum_{j=0}^{W-1} (Im[i,j] - Imf[i,j])^2
$$

$$
PSNR = 10 \cdot \log_{10} \frac{R^2}{MSE}
$$
