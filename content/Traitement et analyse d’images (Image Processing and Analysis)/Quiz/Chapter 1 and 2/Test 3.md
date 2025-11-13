---
sources:
  - "[[1.3 Color Spaces (RGB, Grayscale, HSL)]]"
  - "[[1.5 The Image Histogram]]"
  - "[[1.6 Pixel Relationships and Distance]]"
  - "[[2.0 Image Noise and Degradation]]"
  - "[[2.3 Non-Linear Spatial Filters (Median, Nagao)]]"
  - "[[2.4 Frequency Domain Filtering]]"
  - "[[Convolution The Definition and Core Formula]]"
  - "[[Mathematical Morphology]]"
  - "[[TP1 - Setup and Basic Image Manipulation]]"
---
> [!question] The associativity property of convolution states that the order of convolution does not matter (e.g., `f * h = h * f`).
>> [!success]- Answer
>> False

> [!question] When converting an RGB image to grayscale using a weighted average, the Green channel is typically given the highest weight.
>> [!success]- Answer
>> True

> [!question] A histogram provides detailed information about the spatial arrangement of pixels in an image.
>> [!success]- Answer
>> False

> [!question] The Nagao filter replaces the value of a central pixel with the *mean* of the local sub-region that has the minimum variance.
>> [!success]- Answer
>> True

> [!question] Salt-and-pepper noise is a type of multiplicative noise.
>> [!success]- Answer
>> False

> [!question] A Structuring Element (SE) used in morphological operations must always be a square.
>> [_!success]- Answer
>> False

> [!question] Periodic noise in an image (like a repeating line pattern) appears as distinct, bright spikes in its frequency spectrum.
>> [!success]- Answer
>> True

> [!question] For any two pixels, the Chebyshev distance will always be greater than or equal to the Euclidean distance.
>> [!success]- Answer
>> False

> [!question] The sum of all elements in a standard low-pass blurring kernel (like a mean filter) should be 1 to preserve image brightness.
>> [!success]- Answer
>> True

> [!question] The Python library primarily used for its powerful n-dimensional array object and numerical operations is Matplotlib.
>> [!success]- Answer
>> False

> [!question] What does a bimodal histogram (a histogram with two distinct peaks) often indicate?
> a) The image has very low contrast.
> b) The image contains a large amount of Gaussian noise.
> c) The image contains a distinct foreground object on a distinct background.
> d) The image is a color image.
>> [!success]- Answer
>> c) The image contains a distinct foreground object on a distinct background.

> [!question] Which property allows a 2D convolution kernel to be decomposed into two 1D convolutions for a significant speed increase?
> a) Associativity
> b) Commutativity
> c) Linearity
> d) Separability
>> [!success]- Answer
>> d) Separability

> [!question] What is the `ksize` parameter in the `cv2.medianBlur()` function?
> a) A float representing the standard deviation.
> b) An odd integer representing the size of the kernel aperture (e.g., 3 for a 3x3 kernel).
> c) The number of times to apply the filter.
> d) The constant value used for border padding.
>> [!success]- Answer
>> b) An odd integer representing the size of the kernel aperture (e.g., 3 for a 3x3 kernel).

> [!question] Which type of filter is specifically designed to remove a specific band of frequencies, making it ideal for eliminating periodic noise?
> a) Low-pass filter
> b) Band-reject filter
> c) Gabor filter
> d) High-pass filter
>> [!success]- Answer
>> b) Band-reject filter

> [!question] The Median filter is classified as which type of filter?
> a) A linear spatial filter
> b) A frequency domain filter
> c) An order-statistic filter
> d) An additive filter
>> [!success]- Answer
>> c) An order-statistic filter

> [!question] What is the primary advantage of the CIELAB (L*a*b*) color space in image analysis?
> a) It is device-dependent, matching monitor colors exactly.
> b) It requires less memory than RGB.
> c) It is perceptually uniform, meaning numerical changes correspond better to visual changes.
> d) It is an additive color model.
>> [!success]- Answer
>> c) It is perceptually uniform, meaning numerical changes correspond better to visual changes.

> [!question] A 24-bit "True Color" image can represent approximately how many distinct colors?
> a) 256
> b) 65,536
> c) 16.7 million
> d) 4.2 billion
>> [!success]- Answer
>> c) 16.7 million

> [!question] What does the 'R' value represent in the PSNR formula: `10 * log10(R² / MSE)`?
> a) The resolution of the image.
> b) The radius of the filter kernel.
> c) The ratio of red pixels.
> d) The maximum possible pixel value (e.g., 255 for an 8-bit image).
>> [!success]- Answer
>> d) The maximum possible pixel value (e.g., 255 for an 8-bit image).

> [!question] Which image format category contains minimally processed data directly from a digital camera's sensor, offering maximum post-processing flexibility?
> a) TIFF
> b) PNG
> c) RAW
> d) JPEG
>> [!success]- Answer
>> c) RAW

> [!question] The concise Python syntax `[x**2 for x in my_list]` is an example of what?
> a) A tuple unpacking
> b) A lambda function
> c) A for-loop
> d) A list comprehension
>> [!success]- Answer
>> d) A list comprehension

> [!question] Match the Python library with its primary role in the labs.
>> [!example] Group A
>> a) OpenCV
>> b) NumPy
>> c) Matplotlib
>
>> [!example] Group B
>> n) Used for creating plots and displaying multiple images in a single figure.
>> o) The core library for computer vision tasks like filtering and transformations.
>> p) Provides the fundamental `ndarray` object for representing images and fast numerical operations.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the convolution property with its mathematical formula.
>> [!example] Group A
>> a) Distributivity
>> b) Commutativity
>> c) Associativity
>
>> [!example] Group B
>> n) `(f * h1) * h2 = f * (h1 * h2)`
>> o) `f * (h1 + h2) = (f * h1) + (f * h2)`
>> p) `f * h1 = h1 * f`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the morphological operation to its primary purpose.
>> [!example] Group A
>> a) Opening
>> b) Closing
>> c) Dilation
>
>> [!example] Group B
>> n) To fill small holes and gaps within an object.
>> o) To connect separate objects or thicken object boundaries.
>> p) To remove small, isolated noise objects from the background.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the noise model to its mathematical representation.
>> [!example] Group A
>> a) Additive
>> b) Multiplicative
>> c) Impulsive
>
>> [!example] Group B
>> n) The noisy pixel value is proportional to the original pixel value (`IB = IP * B`).
>> o) The noisy pixel value is independent of the original pixel value and replaces it completely (`IB = B`).
>> p) The noise value is simply added to the original pixel value (`IB = IP + B`).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the image color representation with its typical bit depth.
>> [!example] Group A
>> a) Binary Image
>> b) Grayscale Image
>> c) True Color Image
>
>> [!example] Group B
>> n) 24 bits per pixel
>> o) 1 bit per pixel
>> p) 8 bits per pixel
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the frequency domain concept to its corresponding image feature.
>> [!example] Group A
>> a) Low Frequencies
>> b) High Frequencies
>> c) Fourier Transform
>
>> [!example] Group B
>> n) The mathematical tool used to convert from the spatial domain to the frequency domain.
>> o) Corresponds to edges, fine textures, and noise.
>> p) Corresponds to smooth, slowly changing areas like walls or sky.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the OpenCV function to its purpose.
>> [!example] Group A
>> a) `cv2.imread()`
>> b) `cv2.imshow()`
>> c) `cv2.cvtColor()`
>
>> [!example] Group B
>> n) Displays an image in a window.
>> o) Converts an image from one color space to another.
>> p) Reads an image file from disk and returns it as a NumPy array.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the filter type to its fundamental mechanism.
>> [!example] Group A
>> a) Linear Spatial Filter
>> b) Non-Linear Spatial Filter
>> c) Frequency Domain Filter
>
>> [!example] Group B
>> n) Operates by modifying coefficients in the Fourier spectrum of an image.
>> o) Operates directly on pixel neighborhoods using rules based on ordering or selection (e.g., median).
>> p) Operates directly on pixel neighborhoods using a weighted sum (convolution).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the concept from the labs to its Python implementation detail.
>> [!example] Group A
>> a) Pixel Access
>> b) Image Cropping
>> c) Shape Unpacking
>
>> [!example] Group B
>> n) `cropped_img = img[startY:endY, startX:endX]`
>> o) `height, width, channels = img.shape`
>> p) `pixel_value = img[row, column]`
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Nagao filter's main steps to their correct order.
>> [!example] Group A
>> a) Step 1
>> b) Step 2
>> c) Step 3
>
>> [!example] Group B
>> n) Identify the sub-region with the minimum variance.
>> o) For each sub-region in the neighborhood, calculate its variance.
>> p) Replace the center pixel's value with the mean of the minimum-variance sub-region.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)```