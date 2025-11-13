---
sources:
  - "[[1. Core Concepts.md]]"
  - "[[2. Basic Image IO.md]]"
  - "[[3. Grayscale Conversion.md]]"
  - "[[4. Pixel Manipulation.md]]"
  - "[[5. Image Transformations.md]]"
  - "[[6. Image Filtering.md]]"
  - "[[7. Morphological Operations.md]]"
  - "[[1. The ndarray for Images.md]]"
  - "[[2. Array Operations.md]]"
  - "[[1. Plotting Workflow.md]]"
  - "[[2. Displaying Images.md]]"
  - "[[TP1 - Setup and Basic Image Manipulation.md]]"
  - "[[TP2 - Noise Generation and Filtering.md]]"
  - "[[TP3 - Nagao Filter and Performance.md]]"
  - "[[TP4 - Mathematical Morphology.md]]"
---

> [!question] In OpenCV, the origin of the coordinate system (0, 0) is located at the bottom-left corner of the image.
>> [!success]- Answer
>> False

> [!question] A higher Peak Signal-to-Noise Ratio (PSNR) value indicates that the image quality is worse and further from the original.
>> [!success]- Answer
>> False

> [!question] The Median filter is highly effective against Gaussian noise.
>> [!success]- Answer
>> False

> [!question] Morphological Opening is defined as a dilation operation followed by an erosion operation.
>> [!success]- Answer
>> False

> [!question] When using Matplotlib's `plt.imshow()`, you must convert an image loaded by OpenCV from BGR to RGB to display colors correctly.
>> [!success]- Answer
>> True

> [!question] The NumPy data type `uint8` can represent negative values.
>> [!success]- Answer
>> False

> [!question] The `cv2.waitKey(0)` function call will pause the program indefinitely until a key is pressed.
>> [!success]- Answer
>> True

> [!question] In NumPy array slicing `[startY:endY, startX:endX]`, the `endY` and `endX` indices are inclusive.
>> [!success]- Answer
>> False

> [!question] The Nagao filter preserves edges by finding the sub-region with the highest variance to calculate the new pixel value.
>> [!success]- Answer
>> False

> [!question] Assigning an array with `new_img = old_img` creates a completely independent copy of the image data in memory.
>> [!success]- Answer
>> False

> [!question] Which function is used to load an image from a file in OpenCV?
> a) `cv2.show()`
> b) `cv2.load_image()`
> c) `cv2.imread()`
> d) `cv2.capture()`
>> [!success]- Answer
>> c) `cv2.imread()`

> [!question] What attribute of a NumPy array gives you its dimensions (height, width, channels)?
> a) `.size`
> b) `.dim`
> c) `.dtype`
> d) `.shape`
>> [!success]- Answer
>> d) `.shape`

> [!question] Which type of noise is characterized by random black and white pixels and is best removed with a Median filter?
> a) Gaussian Noise
> b) Salt & Pepper Noise
> c) Poisson Noise
> d) Speckle Noise
>> [!success]- Answer
>> b) Salt & Pepper Noise

> [!question] What is the correct color conversion code to change a BGR image to grayscale?
> a) `cv2.COLOR_RGB2GRAY`
> b) `cv2.COLOR_BGR2GRAY`
> c) `cv2.IMREAD_GRAYSCALE`
> d) `cv2.COLOR_GRAY2BGR`
>> [!success]- Answer
>> b) `cv2.COLOR_BGR2GRAY`

> [!question] Which NumPy function is essential for forcing pixel values to stay within the valid [0, 255] range after an operation like adding noise?
> a) `np.mean()`
> b) `np.copy()`
> c) `np.clip()`
> d) `np.random.normal()`
>> [!success]- Answer
>> c) `np.clip()`

> [!question] In Matplotlib, what parameter must be set in `plt.imshow()` to correctly display a 2D grayscale array without false color?
> a) `color='gray'`
> b) `mode='grayscale'`
> c) `cmap='gray'`
> d) `channel=1`
>> [!success]- Answer
>> c) `cmap='gray'`

> [!question] A kernel is a small matrix that slides over an image to calculate new pixel values. This process is called:
> a) Convolution
> b) Transformation
> c) Binarization
> d) Interpolation
>> [!success]- Answer
>> a) Convolution

> [!question] To create a grid of plots within a single Matplotlib figure, which function should you use?
> a) `plt.figure()`
> b) `plt.subplot()`
> c) `plt.show()`
> d) `plt.imshow()`
>> [!success]- Answer
>> b) `plt.subplot()`

> [!question] Which morphological operation is used to fill small holes inside foreground objects?
> a) Erosion
> b) Opening
> c) Dilation
> d) Closing
>> [!success]- Answer
>> d) Closing

> [!question] What is the correct syntax for accessing the pixel at row 100, column 50 of an image array named `img`?
> a) `img(50, 100)`
> b) `img(100, 50)`
> c) `img[50, 100]`
> d) `img[100, 50]`
>> [!success]- Answer
>> d) `img[100, 50]`

> [!question] Match the OpenCV I/O function to its primary purpose.
>> [!example] Group A
>> a) `cv2.imread()`
>> b) `cv2.imshow()`
>> c) `cv2.waitKey()`
>> d) `cv2.destroyAllWindows()`
>
>> [!example] Group B
>> n) Pauses script execution and waits for a key press.
>> o) Closes all windows created by OpenCV.
>> p) Displays an image in a window.
>> q) Reads an image from a file into a NumPy array.
>
>> [!success]- Answer
>> a) -> q)
>> b) -> p)
>> c) -> n)
>> d) -> o)

> [!question] Match the noise type with the filter best suited to remove it.
>> [!example] Group A
>> a) Gaussian Noise
>> b) Salt & Pepper Noise
>
>> [!example] Group B
>> n) Median Filter
>> o) Mean Filter
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the morphological operation with its definition.
>> [!example] Group A
>> a) Opening
>> b) Closing
>> c) Erosion
>> d) Dilation
>
>> [!example] Group B
>> n) Shrinks the boundaries of foreground objects.
>> o) An erosion followed by a dilation.
>> p) A dilation followed by an erosion.
>> q) Expands the boundaries of foreground objects.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)
>> d) -> q)

> [!question] Match the NumPy array attribute to its description.
>> [!example] Group A
>> a) `.shape`
>> b) `.dtype`
>
>> [!example] Group B
>> n) The data type of the elements in the array (e.g., uint8).
>> o) A tuple representing the dimensions of the array.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the image representation with its corresponding NumPy array shape.
>> [!example] Group A
>> a) Grayscale Image
>> b) Color Image (BGR)
>
>> [!example] Group B
>> n) `(height, width, 3)`
>> o) `(height, width)`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the image transformation operation with its primary OpenCV/NumPy method.
>> [!example] Group A
>> a) Cropping
>> b) Resizing
>> c) Rotating
>
>> [!example] Group B
>> n) `cv2.resize()`
>> o) NumPy array slicing
>> p) `cv2.warpAffine()`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] Match the term with its correct definition regarding color image handling between OpenCV and Matplotlib.
>> [!example] Group A
>> a) OpenCV's default channel order
>> b) Matplotlib's expected channel order
>> c) The function to convert between them
>
>> [!example] Group B
>> n) `cv2.cvtColor()`
>> o) BGR (Blue, Green, Red)
>> p) RGB (Red, Green, Blue)
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Python concept to its description.
>> [!example] Group A
>> a) Slicing
>> b) Tuple Unpacking
>> c) List Comprehension
>
>> [!example] Group B
>> n) Assigning elements of a sequence to multiple variables (e.g., `h, w = shape`).
>> o) A concise way to create a list (e.g., `[x*x for x in range(5)]`).
>> p) Accessing a sub-part of a sequence using `[start:stop:step]` notation.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the core steps of the Nagao filter to their purpose.
>> [!example] Group A
>> a) Calculate Variance
>> b) Identify Smoothest Sub-Region
>> c) Calculate Mean
>
>> [!example] Group B
>> n) To find the average pixel value of only the winning sub-region.
>> o) To measure how spread out the pixel values are in each sub-region.
>> p) To find the sub-region with the minimum variance.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Matplotlib plotting function to its role.
>> [!example] Group A
>> a) `plt.figure()`
>> b) `plt.subplot()`
>> c) `plt.imshow()`
>> d) `plt.show()`
>
>> [!example] Group B
>> n) Renders the NumPy array data as an image.
>> o) Displays the final figure with all its subplots.
>> p) Creates a new figure, the main container window.
>> q) Activates a specific cell in a grid layout for plotting.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> q)
>> c) -> n)
>> d) -> o)