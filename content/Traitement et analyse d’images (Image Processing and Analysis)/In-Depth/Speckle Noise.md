
### **1. Definition**

**Speckle noise** is a type of **multiplicative noise** that commonly appears in **coherent imaging systems** such as:

- **Radar (SAR)** – Synthetic Aperture Radar
    
- **Ultrasound imaging**
    
- **Laser and sonar imaging**
    

Unlike Gaussian or salt-and-pepper noise (which _add_ random values to pixels), **speckle noise multiplies** the original pixel values by random variations.  
This means the noise intensity **depends on the brightness** of the original pixel.

---

### **2. Mathematical Model**

If the clean image is denoted by $I(x, y)$, and the speckle noise by $n(x, y)$,  
the observed (noisy) image $I'(x, y)$ is given by:

$$
I'(x, y) = I(x, y) + I(x, y) \cdot n(x, y)
$$

or equivalently:

$$
I'(x, y) = I(x, y) \cdot [1 + n(x, y)]
$$

- $n(x, y)$ is typically modeled as a random variable following a **uniform**, **gamma**, or **Rayleigh distribution**.
    
- Because it’s **multiplicative**, bright regions appear more strongly corrupted than dark ones.
    

---

### **3. Visual Appearance**

Speckle noise looks like **grainy or patchy texture**, similar to sand or tiny dots randomly scattered over the image surface.

- In **ultrasound images**, it appears as granular texture.
    
- In **radar images**, it looks like random interference patterns.
    

---

### **4. Effects on the Image**

- Reduces **contrast**
    
- Degrades **edge and detail visibility**
    
- Makes **segmentation and object recognition** harder
    
- Alters the **statistical properties** of the image
    

---

### **5. Common Denoising Techniques**

Since speckle noise is _multiplicative_, **additive filters (like Gaussian blur)** are not very effective.  
Instead, these specialized filters are often used:

|**Filter Type**|**Description**|**Advantages**|**Disadvantages**|
|---|---|---|---|
|**Lee Filter**|Uses local statistics (mean and variance) to smooth areas while preserving edges|Good for radar and ultrasound images|Can blur small details|
|**Frost Filter**|Similar to Lee but uses exponential weighting|Preserves edges better|Computationally heavier|
|**Kuan Filter**|Approximates multiplicative noise as additive|Works well with multiplicative models|Slight loss of contrast|
|**Wavelet-based Filters**|Removes noise in the frequency domain|Good control of frequency details|Requires tuning|
|**Anisotropic Diffusion**|Reduces noise while maintaining edges using differential equations|Very effective in medical imaging|Computationally intensive|

---

### **6. Comparison with Other Noise Types**

|**Noise Type**|**Model**|**Common Sources**|**Appearance**|**Filtering Approach**|
|---|---|---|---|---|
|**Gaussian Noise**|Additive|Sensors, thermal effects|Smooth grain|Mean / Gaussian filter|
|**Salt & Pepper Noise**|Additive (impulsive)|Transmission errors, dust|Black and white dots|Median filter|
|**Speckle Noise**|Multiplicative|Coherent imaging (radar, ultrasound)|Granular texture|Lee, Frost, or Kuan filter|

---

### **7. Example Scenario**

Suppose an ultrasound image has speckle noise modeled by:

$$
n(x, y) \sim \mathcal{N}(0, 0.1)
$$
and  
$$
I'(x, y) = I(x, y) \times (1 + n(x, y))
$$

- For a pixel $I(x, y) = 150$:  
    $I'(x, y) = 150 \times (1 + 0.1) = 165$
    
- For a darker pixel $I(x, y) = 50$:  
    $I'(x, y) = 50 \times (1 + 0.1) = 55$
    

The bright region changes _more noticeably_, showing how **speckle noise depends on intensity**.

---

### **8. Key Takeaways**

- Speckle noise is **multiplicative**, not additive.
    
- It mostly affects **coherent imaging systems** (radar, ultrasound).
    
- It causes a **grainy appearance** that reduces clarity and contrast.
    
- Effective filters include **Lee, Frost, and Kuan filters**.
    
- Gaussian or median filters are usually **not effective** for speckle noise.
    

---

Would you like me to include a **Mermaid diagram** showing how different noise types relate (additive vs multiplicative) and which filters work for each?