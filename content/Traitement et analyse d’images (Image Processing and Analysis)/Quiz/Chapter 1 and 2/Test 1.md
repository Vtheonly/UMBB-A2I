---
sources:
  - "[[1.0 What is a Digital Image]]"
  - "[[1.3 Color Spaces (RGB, Grayscale, HSL)]]"
  - "[[1.5 The Image Histogram]]"
  - "[[1.6 Pixel Relationships and Distance]]"
  - "[[2.0 Image Noise and Degradation]]"
  - "[[2.2 Linear Spatial Filters (Mean, Gaussian)]]"
  - "[[2.3 Non-Linear Spatial Filters (Median, Nagao)]]"
  - "[[Convolution The Definition and Core Formula]]"
  - "[[Image Quality Metrics (MSE and PSNR)]]"
  - "[[Mathematical Morphology]]"
---
> [!question] The Mean filter is a non-linear filter because it averages pixel values.
>> [!success]- Answer
>> False

> [!question] A higher PSNR (Peak Signal-to-Noise Ratio) value generally indicates better image quality.
>> [!success]- Answer
>> True

> [!question] The Nagao filter is considered a linear spatial filter.
>> [!success]- Answer
>> False

> [!question] Convolution in the spatial domain is equivalent to element-wise multiplication in the frequency domain.
>> [!success]- Answer
>> True

> [!question] The Median filter is particularly effective against Gaussian noise.
>> [!success]- Answer
>> False

> [!question] In the RGB color model, the value (255, 255, 255) represents black.
>> [!success]- Answer
>> False

> [!question] A low-pass filter in the frequency domain is primarily used for sharpening and edge detection.
>> [!success]- Answer
>> False

> [!question] Morphological Opening is defined as an erosion followed by a dilation.
>> [!success]- Answer
>> True

> [!question] A bitmap (or raster) image can be scaled to any size without any loss of quality.
>> [!success]- Answer
>> False

> [!question] The kernel of a Gaussian filter gives more weight to pixels that are closer to the center.
>> [!success]- Answer
>> True

> [!question] Which of the following filters is most effective at removing "salt-and-pepper" noise?
> a) Mean filter
> b) Gaussian filter
> c) Median filter
> d) Laplacian filter
>> [!success]- Answer
>> c) Median filter

> [!question] What does the `sigma` parameter control in a Gaussian filter?
> a) The kernel size
> b) The extent of the blurring
> c) The number of iterations
> d) The image contrast
>> [!success]- Answer
>> b) The extent of the blurring

> [!question] In OpenCV, what is the default color channel order for images loaded by `cv2.imread()`?
> a) RGB
> b) HSL
> c) BGR
> d) YUV
>> [!success]- Answer
>> c) BGR

> [!question] Which morphological operation is best suited for filling small holes inside a foreground object?
> a) Erosion
> b) Opening
> c) Closing
> d) Dilation
>> [!success]- Answer
>> c) Closing

> [!question] The Chebyshev distance (d_inf) between two pixels is also commonly known as the:
> a) Euclidean distance
> b) City-Block distance
> c) Manhattan distance
> d) Chessboard distance
>> [!success]- Answer
>> d) Chessboard distance

> [!question] A narrow image histogram that is concentrated in a small portion of the intensity range indicates what about the image?
> a) High contrast
> b) Low contrast
> c) It is a vector image
> d) It contains speckle noise
>> [!success]- Answer
>> b) Low contrast

> [!question] In the HSL color model, what does 'Hue' represent?
> a) The brightness or intensity of the color
> b) The "purity" of the color
> c) The type of color (e.g., red, green, blue)
> d) The alpha channel
>> [!success]- Answer
>> c) The type of color (e.g., red, green, blue)

> [!question] What is the primary purpose of a high-pass filter?
> a) To blur the image and reduce noise
> b) To increase the overall brightness of an image
> c) To enhance edges and fine details
> d) To convert an image to grayscale
>> [!success]- Answer
>> c) To enhance edges and fine details

> [!question] In the frequency domain representation of an image, where are the lowest frequencies typically located after an FFT shift operation?
> a) At the corners of the spectrum
> b) At the center of the spectrum
> c) Along the top edge of the spectrum
> d) Randomly distributed
>> [!success]- Answer
>> b) At the center of the spectrum

> [!question] Which image format is known for being lossless and supporting an alpha channel for transparency, making it ideal for web graphics?
> a) JPEG
> b) BMP
> c) PNG
> d) GIF
>> [!success]- Answer
>> c) PNG

> [!question] Match the noise type to its description.
>> [!example] Group A
>> a) Gaussian Noise
>> b) Salt-and-Pepper Noise
>> c) Speckle Noise
>
>> [!example] Group B
>> n) Multiplicative noise common in radar and ultrasound images.
>> o) Additive noise where values are drawn from a normal distribution.
>> p) Impulsive noise characterized by sparse black and white pixels.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the spatial filter to its primary function.
>> [!example] Group A
>> a) Mean Filter
>> b) Median Filter
>> c) Nagao Filter
>
>> [!example] Group B
>> n) Edge-preserving smoothing that analyzes the variance of local sub-regions.
>> o) Simple blurring achieved by averaging all pixel values in a neighborhood.
>> p) Removes impulse noise by selecting the middle value from a sorted list of neighbors.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the distance metric with its corresponding formula.
>> [!example] Group A
>> a) Euclidean
>> b) Manhattan
>> c) Chebyshev
>
>> [!example] Group B
>> n) |x_p - x_q| + |y_p - y_q|
>> o) max(|x_p - x_q|, |y_p - y_q|)
>> p) √((x_p - x_q)² + (y_p - y_q)²)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the morphological operation to its definition.
>> [!example] Group A
>> a) Opening
>> b) Closing
>
>> [!example] Group B
>> n) A dilation operation followed by an erosion operation.
>> o) An erosion operation followed by a dilation operation.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the component of the HSL color space with its description.
>> [!example] Group A
>> a) Hue
>> b) Saturation
>> c) Lightness
>
>> [!example] Group B
>> n) The brightness of the color.
>> o) The "purity" or intensity of the color.
>> p) The type of color (e.g., red, green).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the image representation type to its key characteristic.
>> [!example] Group A
>> a) Bitmap (Raster)
>> b) Vector
>
>> [!example] Group B
>> n) Is resolution independent and can be scaled to any size without quality loss.
>> o) Is resolution dependent and will appear pixelated when enlarged significantly.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the frequency domain filter to its primary effect on an image.
>> [!example] Group A
>> a) Low-Pass Filter
>> b) High-Pass Filter
>
>> [!example] Group B
>> n) Enhances sharp details and edges.
>> o) Blurs the image and reduces high-frequency noise.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the convolution property to its mathematical description.
>> [!example] Group A
>> a) Associativity
>> b) Commutativity
>
>> [!example] Group B
>> n) The order of operation does not matter: f * h = h * f.
>> o) Applying filters sequentially is the same as applying their combined filter: (f * h1) * h2 = f * (h1 * h2).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the image quality metric to its interpretation.
>> [!example] Group A
>> a) MSE (Mean Squared Error)
>> b) PSNR (Peak Signal-to-Noise Ratio)
>
>> [!example] Group B
>> n) A logarithmic metric where a higher value is better.
>> o) An absolute error metric where a lower value is better.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the pixel neighborhood definition to its components.
>> [!example] Group A
>> a) 4-Neighbors (N4)
>> b) 8-Neighbors (N8)
>
>> [!example] Group B
>> n) Includes the neighbors that are adjacent horizontally, vertically, and diagonally.
>> o) Includes only the neighbors that are adjacent horizontally and vertically.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)