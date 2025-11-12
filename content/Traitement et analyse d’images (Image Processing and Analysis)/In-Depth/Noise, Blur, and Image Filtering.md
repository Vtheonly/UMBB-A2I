
## **1. Introduction**

Digital images are rarely perfect: they often contain **noise** or are affected by **blur**.  
Image processing uses **filters** to enhance quality and extract meaningful information.  

**Objectives:**  

1. Identify the type of noise or blur.  
2. Choose the appropriate filter.  
3. Understand the effect of filtering on the image.

---

## **2. Types of Noise**

| Noise Type | Description | Characteristics | Example |
|------------|------------|----------------|---------|
| **Gaussian Noise (additive)** | Smooth, random variations in intensity | Known mean and standard deviation; spread across the image | CCD sensors, image transmission |
| **Impulse Noise (Salt & Pepper)** | Isolated very dark or very bright pixels | Extreme values (0 or 255) | Dead pixels or transmission errors |
| **Photon / Poisson Noise** | Proportional to light intensity | Follows Poisson distribution | Scientific imaging |
| **Thermal / Electronic Noise** | Weak, random disturbances | Random, low amplitude | Electronic cameras |

---

## **3. Types of Blur**

| Blur Type | Cause | Visual Effect | Typical Solution |
|-----------|-------|--------------|----------------|
| **Motion Blur** | Object or camera movement | Stretched edges, loss of detail | Deconvolution, Wiener filter |
| **Optical Blur** | Out-of-focus or diffraction | Soft edges, smooth contours | Sharpening, high-pass filtering |
| **Gaussian Blur** | Intentional smoothing or diffusion | Softens image, reduces noise | Inverse filtering, high-pass filter |
| **Average / Mean Blur** | Local averaging (spatial filter) | Loss of texture and fine detail | Adaptive or nonlinear filtering |

---

## **4. Filters: Spatial and Frequency Domains**

### **4.1 Spatial Domain**

- Applied directly on pixels.
- **Linear filters (convolution)**: mean, Gaussian.  
- **Non-linear filters**: median, Nagao, max/min.

#### **Formulas**

**Linear filter (convolution):**

\[
g(x,y) = \sum_i \sum_j f(x-i, y-j) \cdot h(i,j)
\]

- \(h(i,j)\) = filter kernel (e.g., mean, Gaussian)

**Median filter (non-linear):**  

\[
g(x,y) = \text{median}\{ f(x+i, y+j), \forall (i,j) \in \text{neighborhood} \}
\]

---

### **4.2 Frequency Domain (DFT / FFT)**

- Transform the image to **frequency space**: \(F(u,v) = \text{FFT}[f(x,y)]\)
- Apply the filter (low-pass, high-pass, band-pass)
- Transform back to spatial domain: \(f(x,y) = \text{FFT}^{-1}[F(u,v) \cdot H(u,v)]\)

| Frequency Filter | Purpose | Effect |
|-----------------|---------|--------|
| Low-pass | Smoothing, high-frequency noise removal | General blur |
| High-pass | Edge detection | Enhances edges |
| Band-pass | Remove or select a specific frequency range | Suppresses texture or selects patterns |
| Gabor | Select specific frequency zones | Pattern and texture detection |

---

## **5. Choosing Filters Based on Noise or Blur**

| Problem / Artifact | Recommended Filter | Type | Expected Effect | Limitation |
|------------------|-----------------|------|----------------|------------|
| Gaussian noise | Mean, Gaussian | Linear | Smooths gently | Slight edge blurring |
| Impulse noise | Median, Nagao | Non-linear | Removes extreme pixels | Ineffective for continuous noise |
| Motion blur | Wiener (deconvolution) | Adaptive linear | Restores edges | Requires blur estimation |
| Edge loss | High-pass, Laplacian | Linear | Enhances details | Amplifies noise |
| Preserve edges | Bilateral, Anisotropic Diffusion | Non-linear | Adaptive smoothing | More computationally expensive |
| Small unwanted objects | Erosion / Opening | Non-linear | Removes isolated noise | Can remove nearby small objects |
| Small holes | Dilation / Closing | Non-linear | Fills gaps | Can expand unwanted regions |

---

## **6. Quick Reference Guide**

1. **Identify the artifact**: noise or blur.
2. **Analyze the cause**: Gaussian, impulse, motion, optical.
3. **Choose the domain**:
   - Spatial → fast and intuitive.
   - Frequency → targeted on frequency bands.
4. **Select the filter**:
   - Linear → general smoothing, edge enhancement.
   - Non-linear → impulse noise removal, edge preservation.
5. **Check results** and adjust kernel size or parameters.

---

### **7. Conceptual Visualization**

| Artifact | Filter Type | Result |
|----------|------------|-------|
| Soft noise (Gaussian) | Linear (mean / Gaussian) | Smooths uniformly, edges slightly blurred |
| Impulse noise (Salt & Pepper) | Non-linear (median) | Removes extreme pixels, edges preserved |
| Optical / Motion blur | Adaptive linear / Wiener | Restores edges |
| Specific texture | Band-pass / Gabor | Removes or selects frequency range |

---

### **8. Conclusion**

- **Noise and blur** affect images differently: noise → isolated pixels or continuous variation, blur → loss of detail and soft edges.
- **Linear filters**: effective for continuous noise and mild blur.
- **Non-linear filters**: essential for impulse noise and preserving details.
- **Filter choice** depends on the artifact, processing domain (spatial/frequency), and desired output.
