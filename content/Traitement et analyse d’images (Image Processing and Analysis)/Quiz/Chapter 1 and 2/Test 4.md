---
sources:
  - "[[1.0 What is a Digital Image]]"
  - "[[1.1 Image Representation (Bitmap vs Vector)]]"
  - "[[1.2 Resolution and Color Depth]]"
  - "[[1.3 Color Spaces (RGB, Grayscale, HSL)]]"
  - "[[1.4 Image Formats (JPG, PNG, DICOM)]]"
  - "[[1.5 The Image Histogram]]"
  - "[[1.6 Pixel Relationships and Distance]]"
---
---
sources:
  - "[[TP1 - Setup and Basic Image Manipulation]]"
  - "[[TP2 - Noise Generation and Filtering]]"
  - "[[1.1 Image Representation (Bitmap vs Vector)]]"
  - "[[1.5 The Image Histogram]]"
  - "[[1.6 Pixel Relationships and Distance]]"
  - "[[2.0 Image Noise and Degradation]]"
  - "[[Mathematical Morphology]]"
  - "[[Convolution The Definition and Core Formula]]"
---
> [!question] The `cv2.IMREAD_GRAYSCALE` flag can be used with `cv2.cvtColor()` to convert a color image to grayscale.
>> [!success]- Answer
>> False

> [!question] In Matplotlib, `plt.imshow()` will correctly display the colors of an image loaded with OpenCV (in BGR format) without any conversion.
>> [!success]- Answer
>> False

> [!question] The morphological operation of Erosion can cause small holes inside a foreground object to become larger.
>> [!success]- Answer
>> True

> [!question] A high MSE (Mean Squared Error) between an original and a filtered image corresponds to a high PSNR value.
>> [!success]- Answer
>> False

> [!question] A key limitation of the image histogram is that it completely discards the spatial information of pixels.
>> [!success]- Answer
>> True

> [!question] The Nagao filter calculates the new pixel value by taking the *median* of the sub-region with the lowest variance.
>> [!success]- Answer
>> False

> [!question] Vector images are composed of a grid of individual pixels, which allows them to be scaled infinitely without losing quality.
>> [!success]- Answer
>> False

> [!question] The commutativity property of convolution means that `f * h` is equivalent to `h * f`.
>> [!success]- Answer
>> True

> [!question] Speckle noise, often found in radar imagery, is an example of a multiplicative noise model.
>> [!success]- Answer
>> True

> [!question] The NumPy data type `np.uint8` can represent negative integer values.
>> [!success]- Answer
>> False

> [!question] In the lab setup instructions, what is the primary purpose of creating a virtual environment?
> a) To make the Python code run faster.
> b) To isolate the project's library dependencies and prevent version conflicts.
> c) To automatically back up the project files.
> d) To provide a graphical user interface for the code.
>> [!success]- Answer
>> b) To isolate the project's library dependencies and prevent version conflicts.

> [!question] In the `sp_noise` function from the lab, the `prob` parameter represents:
> a) The variance of the noise.
> b) The size of the noise kernel.
> c) The probability of a pixel being corrupted (the noise density).
> d) The maximum intensity value of the noise.
>> [!success]- Answer
>> c) The probability of a pixel being corrupted (the noise density).

> [!question] For any two pixels P and Q, which inequality correctly describes the relationship between the distance metrics?
> a) d₂(P,Q) ≤ d_inf(P,Q) ≤ d₁(P,Q)
> b) d₁(P,Q) ≤ d₂(P,Q) ≤ d_inf(P,Q)
> c) d_inf(P,Q) ≤ d₂(P,Q) ≤ d₁(P,Q)
> d) d_inf(P,Q) ≤ d₁(P,Q) ≤ d₂(P,Q)
>> [!success]- Answer
>> c) d_inf(P,Q) ≤ d₂(P,Q) ≤ d₁(P,Q)

> [!question] The function `cv2.getStructuringElement()` is used to create which component for morphological operations?
> a) The input binary image.
> b) The histogram of the image.
> c) The structuring element (kernel).
> d) The output image mask.
>> [!success]- Answer
>> c) The structuring element (kernel).

> [!question] If the sum of the elements in a low-pass (blurring) convolution kernel is greater than 1, what will be the effect on the output image?
> a) The image will become darker.
> b) The image will become sharper.
> c) The image brightness will be unchanged.
> d) The image will become brighter.
>> [!success]- Answer
>> d) The image will become brighter.

> [!question] Which conversion code is used in `cv2.cvtColor()` to change a BGR image to grayscale?
> a) `cv2.COLOR_GRAY2BGR`
> b) `cv2.COLOR_BGR2GRAY`
> c) `cv2.COLOR_BGR2HSL`
> d) `cv2.IMREAD_GRAYSCALE`
>> [!success]- Answer
>> b) `cv2.COLOR_BGR2GRAY`

> [!question] According to the notes, what is a primary cause of Gaussian noise in digital sensors?
> a) Errors in data transmission.
> b) Dead or stuck pixels.
> c) Thermal noise and poor illumination.
> d) Scratches on a camera lens.
>> [!success]- Answer
>> c) Thermal noise and poor illumination.

> [!question] When a high-pass filter is applied to a completely uniform (flat) region of an image, the resulting pixel values in that region will be:
> a) Close to 255 (white).
> b) Close to 127 (mid-gray).
> c) Close to 0 (black).
> d) The same as the original values.
>> [!success]- Answer
>> c) Close to 0 (black).

> [!question] A digital image is fundamentally a discrete representation, where both its spatial coordinates and intensity values are...
> a) Continuous
> b) Analog
> c) Infinite
> d) Quantized
>> [!success]- Answer
>> d) Quantized

> [!question] Which morphological operation is most effective for breaking thin connections between two touching objects?
> a) Dilation
> b) Closing
> c) Erosion
> d) Thresholding
>> [!success]- Answer
>> c) Erosion

> [!question] Match the image problem with the most appropriate filtering solution from the labs.
>> [!example] Group A
>> a) Salt-and-Pepper noise
>> b) Gaussian noise
>> c) Separating touching cells
>
>> [!example] Group B
>> n) Mean Filter (`cv2.blur`)
>> o) Watershed algorithm after morphological opening
>> p) Median Filter (`cv2.medianBlur`)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Python slicing syntax with its result on the list `x = [0, 1, 2, 3, 4, 5]`.
>> [[example] Group A
>> a) `x[1:4]`
>> b) `x[::2]`
>> c) `x[3:]`
>
>> [!example] Group B
>> n) `[0, 2, 4]`
>> o) `[3, 4, 5]`
>> p) `[1, 2, 3]`
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the `cv2.morphologyEx` operation flag with the sequence of fundamental operations it performs.
>> [!example] Group A
>> a) `cv2.MORPH_OPEN`
>> b) `cv2.MORPH_CLOSE`
>
>> [!example] Group B
>> n) 1st: Dilation, 2nd: Erosion
>> o) 1st: Erosion, 2nd: Dilation
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the color space to its primary advantage or use case.
>> [!example] Group A
>> a) RGB
>> b) HSL
>> c) LAB
>
>> [!example] Group B
>> n) Standard for digital displays and image file storage.
>> o) Perceptually uniform, excellent for measuring color differences.
>> p) Intuitive for color manipulation tasks like changing hue independently of brightness.
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] Match the filter name to its category.
>> [!example] Group A
>> a) Mean Filter
>> b) Median Filter
>> c) Nagao Filter
>
>> [!example] Group B
>> n) Non-Linear (Order-Statistic)
>> o) Non-Linear (Adaptive)
>> p) Linear
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the image degradation type with its visual appearance.
>> [!example] Group A
>> a) Gaussian Noise
>> b) Salt-and-Pepper Noise
>> c) Motion Blur
>
>> [!example] Group B
>> n) Streaked or smeared edges and details.
>> o) A fine, grain-like texture across the entire image.
>> p) Sparse black and white dots scattered randomly.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the histogram shape to the general characteristic of the image.
>> [!example] Group A
>> a) Clustered on the left
>> b) Spread across the full range
>> c) Clustered on the right
>
>> [!example] Group B
>> n) Bright image
>> o) High contrast image
>> p) Dark image
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the NumPy array attribute with what it represents for a loaded image.
>> [!example] Group A
>> a) `.shape`
>> b) `.dtype`
>
>> [!example] Group B
>> n) The data type of the pixel values (e.g., `uint8`).
>> o) A tuple representing the dimensions (height, width, channels).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the OpenCV function with the data type of its key size parameter.
>> [!example] Group A
>> a) `cv2.blur()`
>> b) `cv2.medianBlur()`
>> c) `cv2.getRotationMatrix2D()`
>
>> [!example] Group B
>> n) `ksize` is an `int` (e.g., 3).
>> o) `angle` is a `float`.
>> p) `ksize` is a `tuple` (e.g., (3, 3)).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the border handling strategy for convolution with its description.
>> [!example] Group A
>> a) `BORDER_CONSTANT`
>> b) `BORDER_REPLICATE`
>> c) `BORDER_REFLECT`
>
>> [!example] Group B
>> n) Mirrors the pixel values at the boundary.
>> o) Pads the image with a fixed value (e.g., zero).
>> p) Repeats the last row/column of pixels.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)