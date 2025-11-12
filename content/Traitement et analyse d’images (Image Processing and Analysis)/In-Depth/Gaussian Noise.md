Gaussian noise is one of the most fundamental concepts in image processing, and understanding it in detail is key.

Here is a comprehensive note on "Bruit gaussien (additif)" or Additive Gaussian Noise, synthesizing the information from both your lecture slides and your lab (TP2) document into a single, detailed explanation.

---

### In-Depth: Additive Gaussian Noise

**Objective:** To explain the concept of additive Gaussian noise, covering its mathematical foundation, its key characteristics, its visual appearance, and its specific role as a common image degradation model in this course.

## 1. Core Concept: What is Additive Gaussian Noise?

Additive Gaussian Noise is a type of image degradation where each pixel in the original image is corrupted by the addition of a random value. The "additive" part of the name refers to the mathematical operation used: a simple addition.

As defined in the course slides, the relationship between the original image, the noise, and the final noisy image is:

$$
I_{\text{noisy}}(i,j) = I_{\text{original}}(i,j) + N(i,j)
$$

-   $I_{\text{noisy}}(i,j)$ is the intensity of the pixel at position $(i,j)$ in the final, corrupted image.
-   $I_{\text{original}}(i,j)$ is the intensity of the pixel in the clean, original image.
-   $N(i,j)$ is the random noise value added to that specific pixel.

The "Gaussian" part of the name describes the statistical nature of the noise values $N$. These values are not just any random numbers; they are drawn from a **Gaussian (or Normal) distribution**.

## 2. The Mathematical Foundation: The Gaussian Distribution

The values of the noise $N$ follow a bell-shaped curve defined by the Gaussian Probability Density Function (PDF). This function describes the likelihood of a random noise value occurring.

$$
p(z) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(z-\mu)^2}{2\sigma^2}}
$$

Let's break down the ingredients of this formula:

-   $z$: Represents the intensity of the noise value itself (the value being added to the pixel).
-   $\mu$ (mu, "moyenne"): The **mean** of the distribution. This is the average value of the noise. In image processing, this is almost always set to **$\mu = 0$**.
    -   **Insight:** A zero-mean noise is critical because it means the noise does not systematically brighten or darken the image. On average, the added positive and negative noise values cancel each other out, preserving the image's overall brightness.
-   $\sigma$ (sigma, "écart type"): The **standard deviation** of the distribution. This parameter is the most important for controlling the noise's appearance.
-   $\sigma^2$: The **variance**. This is simply the square of the standard deviation.

**The Role of Standard Deviation ($\sigma$):**
The standard deviation $\sigma$ controls the "spread" of the bell curve.
-   A **small $\sigma$** results in a narrow curve, meaning most noise values will be very close to the mean (0). This produces subtle, fine-grained noise.
-   A **large $\sigma$** results in a wide curve, meaning the noise values can be much larger (both positive and negative). As stated in the lab document, *"plus σ est élevée, plus l'image est bruitée"* (the higher σ is, the noisier the image). This produces strong, very visible noise. The lab's example uses a variance of $\sigma^2=100$, which corresponds to a standard deviation of $\sigma=10$.

## 3. Key Characteristics (Synthesized from Slides and Labs)

-   **Additive:** The noise is added to the original pixel values.
-   **Affects Every Pixel:** Unlike other noise types (like salt & pepper), Gaussian noise modifies the value of **every single pixel** in the image, even if the modification is very small for some pixels.
-   **Zero-Mean:** The average of the noise is zero, so the overall image brightness is not changed.
-   **Statistically Independent:** The noise value at one pixel does not depend on the value of its neighbors. This is what is meant by "white noise" in the lab document.
-   **Controlled by Variance ($\sigma^2$):** The intensity of the noise is directly controlled by its variance. This is the main parameter you would change to simulate different levels of noise.

## 4. Visual Appearance and Its Effect on Frequencies

Visually, Gaussian noise appears as a fine, grainy, "static-like" texture spread across the entire image. It makes the image look like it was taken in low light conditions with a high ISO setting on a digital camera.

The lab document makes a crucial point: Gaussian noise *"affecte les basses et les hautes fréquences dans une image"* (affects the low and high frequencies in an image).
-   **High Frequencies:** The rapid, random, pixel-to-pixel variations introduce a significant amount of high-frequency content. This is the visible "graininess."
-   **Low Frequencies:** The overall "haze" and slight, large-scale variations in brightness caused by the noise also impact the low-frequency components of the image.

## 5. Simulation and Relevance in This Course

**Why is it important?**
Gaussian noise is studied so thoroughly because it is an excellent mathematical model for many types of real-world noise, particularly **sensor noise** in digital cameras and scanners that arises from electronic fluctuations and poor illumination.

**How is it simulated (as per TP2)?**
1.  Start with a clean image, $I_{original}$.
2.  Generate a matrix of random numbers the same size as the image, where the numbers are drawn from a Gaussian distribution with a mean of 0 and a specified variance (e.g., $\sigma^2=100$).
3.  Add this noise matrix to the original image's matrix.
4.  Clip the resulting values to ensure they remain within the valid pixel range (e.g., [0, 255]).

**How is it combatted in this course?**
The primary way to reduce additive Gaussian noise is through **averaging**. The random positive and negative values tend to cancel each other out when averaged. Therefore, **low-pass filters** like the **Mean Filter (Filtre Moyenneur)** and the **Gaussian Filter** are the most effective tools for its removal. This is a central theme of the preprocessing chapter.