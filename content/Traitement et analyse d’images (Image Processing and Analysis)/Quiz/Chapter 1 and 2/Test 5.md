---
sources:
  - "[[1.1 Image Representation (Bitmap vs Vector)]]"
  - "[[1.3 Color Spaces (RGB, Grayscale, HSL)]]"
  - "[[1.6 Pixel Relationships and Distance]]"
  - "[[2.1 Spatial Domain vs Frequency Domain]]"
  - "[[2.2 Linear Spatial Filters (Mean, Gaussian)]]"
  - "[[2.3 Non-Linear Spatial Filters (Median, Nagao)]]"
  - "[[Mathematical Morphology]]"
  - "[[Convolution The Definition and Core Formula]]"
---
> [!question] The RGB color model is considered a subtractive model, where colors are created by removing light.
>> [!success]- Answer
>> False

> [!question] In the frequency domain representation of an image, high frequencies correspond to the smooth, slowly changing areas.
>> [!success]- Answer
>> False

> [!question] The Mean filter is generally more effective at preserving sharp edges than the Median filter.
>> [!success]- Answer
>> False

> [!question] A morphological Closing operation can be used to separate two objects that are connected by a thin bridge.
>> [!success]- Answer
>> False

> [!question] 4-connectivity considers diagonally adjacent pixels to be neighbors.
>> [!success]- Answer
>> False

> [!question] A key advantage of vector graphics is that they are resolution-independent.
>> [!success]- Answer
>> True

> [!question] The Nagao filter is an adaptive filter that modifies its behavior based on the local statistical properties of the image.
>> [!success]- Answer
>> True

> [!question] The process of converting a continuous range of values into a finite set of discrete values is known as quantization.
>> [!success]- Answer
>> True

> [!question] Applying two spatial filters to an image one after the other can be optimized by first convolving the two filter kernels together.
>> [!success]- Answer
>> True

> [!question] The PNG image format typically uses a lossy compression algorithm.
>> [!success]- Answer
>> False

> [!question] Which term describes the process of estimating new pixel values when resizing a bitmap image?
> a) Quantization
> b) Interpolation
> c) Thresholding
> d) Convolution
>> [!success]- Answer
>> b) Interpolation

> [!question] The "alpha channel" in an image format like PNG is used to store what information?
> a) Color depth
> b) Image resolution
> c) Transparency
> d) Copyright metadata
>> [!success]- Answer
>> c) Transparency

> [!question] A linear spatial filter is one where the output pixel's value is calculated as a...
> a) Median of the input neighborhood.
> b) Weighted sum of the input neighborhood.
> c) Minimum value of the input neighborhood.
> d) Variance of the input neighborhood.
>> [!success]- Answer
>> b) Weighted sum of the input neighborhood.

> [!question] What is the primary reason for using the Fourier Transform in image filtering?
> a) It converts color images to grayscale.
> b) It allows computationally expensive convolution to be replaced by simple multiplication.
> c) It corrects geometric distortions in an image.
> d) It increases the spatial resolution of an image.
>> [!success]- Answer
>> b) It allows computationally expensive convolution to be replaced by simple multiplication.

> [!question] What does the "Saturation" component represent in the HSL color space?
> a) The overall brightness of the color.
> b) The type of color (e.g., red or blue).
> c) The "purity" or intensity of the color.
> d) The dominant wavelength of the color.
>> [!success]- Answer
>> c) The "purity" or intensity of the color.

> [!question] What is the small template or shape used to probe an image in morphological operations called?
> a) A pixel grid
> b) A feature vector
> c) A structuring element
> d) A binarization mask
>> [!success]- Answer
>> c) A structuring element

> [!question] Which of the following is an example of an "order-statistic" filter?
> a) Mean filter
> b) Gaussian filter
> c) Median filter
> d) Laplacian filter
>> [!success]- Answer
>> c) Median filter

> [!question] A larger kernel size in a mean (averaging) filter will result in:
> a) A sharper image.
> b) Less blurring.
> c) More aggressive blurring.
> d) An increase in image contrast.
>> [!success]- Answer
>> c) More aggressive blurring.

> [!question] Impulsive noise, such as salt-and-pepper, is often caused by:
> a) Thermal fluctuations in the sensor.
> b) Slow shutter speed.
> c) Coherent imaging systems like radar.
> d) Data transmission errors or sensor defects.
>> [!success]- Answer
>> d) Data transmission errors or sensor defects.

> [!question] The standard reference color space based on human perception, often used as a connection point between other spaces, is:
> a) RGB
> b) HSL
> c) XYZ
> d) CMYK
>> [!success]- Answer
>> c) XYZ

> [!question] Match the morphological operation with its primary visual effect.
>> [!example] Group A
>> a) Erosion
>> b) Dilation
>> c) Opening
>> d) Closing
>
>> [!example] Group B
>> n) Fills small holes within foreground objects.
>> o) Shrinks or thins foreground objects.
>> p) Removes small, isolated foreground objects.
>> q) Expands or thickens foreground objects.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> q)
>> c) -> p)
>> d) -> n)

> [!question] Match the filter type to its fundamental principle.
>> [!example] Group A
>> a) Mean Filter
>> b) Gaussian Filter
>> c) Median Filter
>
>> [!example] Group B
>> n) Replaces a pixel with the middle value from a sorted list of its neighbors.
>> o) Replaces a pixel with a weighted average where closer neighbors have more influence.
>> p) Replaces a pixel with the unweighted average of all its neighbors.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the domain to the information it primarily represents.
>> [!example] Group A
>> a) Spatial Domain
>> b) Frequency Domain
>
>> [!example] Group B
>> n) Represents the rate of change of pixel values across the image.
>> o) Represents the intensity or color value at specific (x,y) coordinates.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the distance metric with its common analogy or name.
>> [!example] Group A
>> a) Euclidean
>> b) Manhattan
>> c) Chebyshev
>
>> [!example] Group B
>> n) City-Block Distance
>> o) Chessboard Distance
>> p) Straight-Line Distance
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the noise model with its mathematical category.
>> [!example] Group A
>> a) Gaussian Noise
>> b) Salt-and-Pepper Noise
>> c) Speckle Noise
>
>> [!example] Group B
>> n) Impulsive
>> o) Multiplicative
>> p) Additive
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the term with its correct definition.
>> [!example] Group A
>> a) Pixel
>> b) Resolution
>> c) Color Depth
>
>> [!example] Group B
>> n) The smallest individual element of a digital image.
>> o) The number of distinct colors that can be represented per pixel.
>> p) The number of pixels an image contains, often given as width x height.
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] Match the image format with its primary compression type.
>> [!example] Group A
>> a) JPEG
>> b) PNG
>> c) BMP
>
>> [!example] Group B
>> n) Typically uncompressed.
>> o) Lossy compression.
>> p) Lossless compression.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the image quality metric to its interpretation.
>> [!example] Group A
>> a) MSE (Lower is better)
>> b) PSNR (Higher is better)
>
>> [!example] Group B
>> n) A logarithmic measure of reconstruction quality relative to the signal peak.
>> o) A direct measure of the average squared difference between pixel values.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the frequency filter with its primary purpose.
>> [!example] Group A
>> a) Low-Pass
>> b) High-Pass
>> c) Band-Reject
>
>> [!example] Group B
>> n) Sharpening and edge detection.
>> o) Removing specific periodic noise.
>> p) Smoothing and noise reduction.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the connectivity rule to the type of adjacency it defines.
>> [!example] Group A
>> a) 4-Connectivity
>> b) 8-Connectivity
>
>> [!example] Group B
>> n) Considers pixels sharing an edge or a corner as neighbors.
>> o) Considers only pixels sharing an edge as neighbors.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)