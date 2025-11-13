---
sources:
  - "[[2.0 Image Noise and Degradation]]"
  - "[[2.2 Linear Spatial Filters (Mean, Gaussian)]]"
  - "[[2.3 Non-Linear Spatial Filters (Median, Nagao)]]"
  - "[[TP2 - Noise Generation and Filtering]]"
  - "[[TP4 - Mathematical Morphology]]"
  - "[[The Spatial and Frequency Domains]]"
  - "[[Image Quality Metrics (MSE and PSNR)]]"
  - "[[1.3 Color Spaces (RGB, Grayscale, HSL)]]"
---
> [!question] The `cv2.waitKey(0)` function in OpenCV will wait indefinitely until any key is pressed.
>> [!success]- Answer
>> True

> [!question] Dilation is a morphological operation that can be used to fill small holes within a foreground object.
>> [!success]- Answer
>> True

> [!question] The HSL color space is generally considered less intuitive for human perception than the RGB color space.
>> [!success]- Answer
>> False

> [!question] An MSE (Mean Squared Error) of 0 between two images corresponds to a PSNR value of 0 dB.
>> [!success]- Answer
>> False

> [!question] Unlike impulse noise, Gaussian noise typically affects every single pixel in an image.
>> [!success]- Answer
>> True

> [!question] A separable 2D filter can be decomposed into two 1D filters, which is computationally slower than performing the full 2D convolution.
>> [!success]- Answer
>> False

> [!question] The NumPy function `np.clip()` is used to ensure pixel values remain within a valid range, such as [0, 255].
>> [!success]- Answer
>> True

> [!question] A high-pass filter in the frequency domain works by attenuating (removing) the high-frequency components of an image.
>> [!success]- Answer
>> False

> [!question] The `cv2.watershed` algorithm is a common technique used for blurring images to reduce noise.
>> [!success]- Answer
>> False

> [!question] In a color image represented as a NumPy array with shape (height, width, 3), the 'width' corresponds to the number of pixel rows.
>> [!success]- Answer
>> False

> [!question] The Nagao filter determines the smoothest sub-region by finding the one with the...
> a) Maximum mean
> b) Minimum variance
> c) Maximum standard deviation
> d) Minimum median
>> [!success]- Answer
>> b) Minimum variance

> [!question] The mathematical operation used to apply a linear spatial filter to an image is called:
> a) Correlation
> b) Fourier Transform
> c) Convolution
> d) Inversion
>> [!success]- Answer
>> c) Convolution

> [!question] In an 8-bit grayscale image, how many distinct intensity levels can be represented?
> a) 8
> b) 16
> c) 256
> d) 24
>> [!success]- Answer
>> c) 256

> [!question] What is the most significant disadvantage of using a Mean filter for noise reduction?
> a) It is computationally very slow.
> b) It only works on color images.
> c) It blurs edges and fine details.
> d) It tends to amplify existing noise.
>> [!success]- Answer
>> c) It blurs edges and fine details.

> [!question] The formula `|x_p - x_q| + |y_p - y_q|` defines which distance metric?
> a) Euclidean
> b) Manhattan (City-Block)
> c) Chebyshev
> d) Hamming
>> [!success]- Answer
>> b) Manhattan (City-Block)

> [!question] What is the purpose of the `cv2.THRESH_OTSU` flag when performing a thresholding operation?
> a) It sets the threshold value to a fixed number, 127.
> b) It automatically finds an optimal threshold value based on the image's histogram.
> c) It inverts the resulting binary image (black becomes white and vice-versa).
> d) It creates a multi-level threshold instead of a binary one.
>> [!success]- Answer
>> b) It automatically finds an optimal threshold value based on the image's histogram.

> [!question] A Gabor filter is particularly effective for which of the following tasks?
> a) Color correction
> b) Removing salt-and-pepper noise
> c) Image compression
> d) Texture analysis and feature extraction
>> [!success]- Answer
>> d) Texture analysis and feature extraction

> [!question] A morphological 'Opening' operation is especially useful for which task?
> a) Filling large holes inside objects
> b) Making objects significantly larger
> c) Sharpening the edges of objects
> d) Removing small, isolated foreground noise (salt-like noise)
>> [!success]- Answer
>> d) Removing small, isolated foreground noise (salt-like noise)

> [!question] What is the output of the `img.shape` attribute for a color image loaded by OpenCV?
> a) (width, height)
> b) (width, height, channels)
> c) (height, width, channels)
> d) (channels, height, width)
>> [!success]- Answer
>> c) (height, width, channels)

> [!question] In Python, the expression `my_list[2:5]` will extract which elements from `my_list`?
> a) Elements at index 2, 3, 4, and 5
> b) Elements at index 2, 3, and 4
> c) Elements at index 3, 4, and 5
> d) Only the element at index 2 and index 5
>> [!success]- Answer
>> b) Elements at index 2, 3, and 4

> [!question] Match the image format with its primary characteristic or use case.
>> [!example] Group A
>> a) JPEG
>> b) PNG
>> c) DICOM
>
>> [!example] Group B
>> n) A lossless format that supports transparency, ideal for web graphics.
>> o) The standard for medical images, containing both pixel data and rich metadata.
>> p) A lossy format that offers a great balance between quality and file size for photographs.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the noise type with the filter best suited to remove it.
>> [!example] Group A
>> a) Gaussian Noise
>> b) Salt-and-Pepper Noise
>
>> [!example] Group B
>> n) Median Filter
>> o) Mean or Gaussian Filter
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the color space to its constituent components.
>> [!example] Group A
>> a) RGB
>> b) HSL
>> c) LAB
>
>> [!example] Group B
>> n) Hue, Saturation, Lightness
>> o) Luminance, a-channel (green-red), b-channel (blue-yellow)
>> p) Red, Green, Blue
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the term to its correct definition.
>> [!example] Group A
>> a) Spatial Resolution
>> b) Color Depth
>
>> [!example] Group B
>> n) The number of bits used to represent the color of a single pixel.
>> o) The number of pixels in an image, typically expressed as width x height.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the morphological operation to its effect on a white object on a black background.
>> [!example] Group A
>> a) Erosion
>> b) Dilation
>
>> [!example] Group B
>> n) Expands or thickens the object.
>> o) Shrinks or thins the object.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the NumPy function from the labs with its purpose.
>> [!example] Group A
>> a) `np.random.normal()`
>> b) `np.clip()`
>> c) `np.var()`
>
>> [!example] Group B
>> n) To limit the values in an array to a specified min-max range.
>> o) To calculate the variance of a set of values, used in the Nagao filter.
>> p) To generate an array of random numbers from a Gaussian distribution.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)