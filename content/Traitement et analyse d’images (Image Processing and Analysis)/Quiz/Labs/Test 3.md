---
sources:
  - "[[1. Core Concepts.md]]"
  - "[[2. Basic Image IO.md]]"
  - "[[5. Image Transformations.md]]"
  - "[[6. Image Filtering.md]]"
  - "[[1. Plotting Workflow.md]]"
  - "[[3. Grayscale Conversion.md]]"
  - "[[1. Advanced Python Techniques.md]]"
  - "[[1. The ndarray for Images.md]]"
  - "[[2. Array Operations.md]]"
  - "[[4. Pixel Manipulation.md]]"
  - "[[7. Morphological Operations.md]]"
---
---
sources:
  - "[[1. Core Concepts.md]]"
  - "[[2. Basic Image IO.md]]"
  - "[[4. Pixel Manipulation.md]]"
  - "[[5. Image Transformations.md]]"
  - "[[6. Image Filtering.md]]"
  - "[[7. Morphological Operations.md]]"
  - "[[1. The ndarray for Images.md]]"
  - "[[2. Array Operations.md]]"
  - "[[1. Plotting Workflow.md]]"
  - "[[2. Displaying Images.md]]"
  - "[[1. Advanced Python Techniques.md]]"
---

> [!question] In the `for` loop `for i in range(0, width - 1):`, the code inside the loop will execute `width` number of times.
>> [!success]- Answer
>> False

> [!question] The code `pixel_value = 5; new_value = pixel_value - 10` where `pixel_value` is of type `np.uint8` will result in `new_value` being `-5`.
>> [!success]- Answer
>> False

> [!question] The function `plt.suptitle("My Figure")` is used to add a title to a single subplot within a figure.
>> [!success]- Answer
>> False

> [!question] When applying a morphological operation, the `iterations` parameter specifies how many times the operation is applied. For example, `iterations=2` means the operation runs twice.
>> [!success]- Answer
>> True

> [!question] If a script displays an image using `cv2.imshow()` but omits `cv2.waitKey()`, the image will be displayed for a fraction of a second and the window may appear frozen.
>> [!success]- Answer
>> True

> [!question] The `dsize` parameter in `cv2.warpAffine(src, M, dsize)` determines the dimensions of the output image.
>> [!success]- Answer
>> True

> [!question] The code `im2 = im1 + gaussian_noise` is likely to produce an image array with a data type of `float64`, not `uint8`.
>> [!success]- Answer
>> True

> [!question] A list comprehension is always more computationally efficient than a standard `for` loop.
>> [!success]- Answer
>> False

> [!question] In the `cv2.resize(src, dsize)` function, `dsize` is specified as `(height, width)`.
>> [!success]- Answer
>> False

> [!question] Using `plt.axis('off')` will remove the image content from the plot, leaving only the axes.
>> [!success]- Answer
>> False

> [!question] What is the primary purpose of the line `output = np.copy(image)` at the beginning of a function that modifies an image?
> a) To convert the image to grayscale.
> b) To create a faster, read-only version of the image.
> c) To ensure the original input image is not modified by the function.
> d) To reserve more memory for the image.
>> [!success]- Answer
>> c) To ensure the original input image is not modified by the function.

> [!question] If `img` is a 512x512 color image, what will `img.shape` return?
> a) `(512, 512)`
> b) `[512, 512, 3]`
> c) `(512, 512, 3)`
> d) `512, 512, 3`
>> [!success]- Answer
>> c) `(512, 512, 3)`

> [!question] Given `shape = (480, 640, 3)`, what does the line `h, w, _ = shape` accomplish?
> a) It will cause a syntax error.
> b) It assigns 480 to `h`, 640 to `w`, and 3 to `_`.
> c) It assigns 480 to `h` and 640 to `w`, and the underscore indicates an error.
> d) It assigns 480 to `h`, 640 to `w`, and effectively discards the channel value.
>> [!success]- Answer
>> d) It assigns 480 to `h`, 640 to `w`, and effectively discards the channel value.

> [!question] In the context of the Nagao filter, `np.var()` is used on sub-regions to:
> a) Find the brightest sub-region.
> b) Find the sub-region with the smoothest texture.
> c) Find the average intensity of the sub-region.
> d) Find the darkest sub-region.
>> [!success]- Answer
>> b) Find the sub-region with the smoothest texture.

> [!question] To apply a morphological "Closing" operation to a binary image `bin_img`, which code is correct?
> a) `closed = cv2.morphologyEx(bin_img, cv2.MORPH_ERODE, kernel)`
> b) `closed = cv2.dilate(cv2.erode(bin_img, kernel), kernel)`
> c) `closed = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel)`
> d) `closed = cv2.close(bin_img, kernel)`
>> [!success]- Answer
>> c) `closed = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel)`

> [!question] What is the result of increasing the `ksize` parameter in `cv2.blur()` from `(3, 3)` to `(11, 11)`?
> a) The image becomes sharper.
> b) The amount of blurring increases.
> c) The amount of blurring decreases.
> d) The processing time decreases.
>> [!success]- Answer
>> b) The amount of blurring increases.

> [!question] Which of the following commands correctly loads an image and immediately converts it to a 2D grayscale NumPy array?
> a) `img = cv2.imread('path.jpg', cv2.IMREAD_GRAYSCALE)`
> b) `img = cv2.imread('path.jpg'); img = cv2.to_gray(img)`
> c) `img = cv2.loadGray('path.jpg')`
> d) `img = cv2.imread('path.jpg'); img.shape = (h, w)`
>> [!success]- Answer
>> a) `img = cv2.imread('path.jpg', cv2.IMREAD_GRAYSCALE)`

> [!question] What does the `cv2.waitKey(25)` function typically do inside a video processing loop?
> a) It pauses the program for exactly 25 seconds.
> b) It saves the current frame as an image file.
> c) It checks for a key press for 25 milliseconds, allowing the image window to refresh.
> d) It closes the window after 25 frames have been processed.
>> [!success]- Answer
>> c) It checks for a key press for 25 milliseconds, allowing the image window to refresh.

> [!question] In the PSNR calculation, `mse = np.mean((img1 - img2) ** 2)`, what mathematical operation does `** 2` represent?
> a) Square root.
> b) Element-wise multiplication.
> c) Matrix multiplication.
> d) Element-wise squaring.
>> [!success]- Answer
>> d) Element-wise squaring.

> [!question] To create a 3x3 rectangular structuring element, which code is correct?
> a) `cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))`
> b) `cv2.createKernel(cv2.RECT, 3)`
> c) `np.ones((3,3))`
> d) `cv2.structuringElement(cv2.MORPH_SQUARE, 3)`
>> [!success]- Answer
>> a) `cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))`

> [!question] Match the code for generating noise to its description.
>> [!example] Group A
>> a) `gaussian = np.random.normal(0, 25, img.shape)`
>> b) `noisy_img = img.astype(np.float64) + gaussian`
>> c) `final_img = np.clip(noisy_img, 0, 255).astype(np.uint8)`
>
>> [!example] Group B
>> n) Adds the generated noise matrix to the source image matrix.
>> o) Creates a valid `uint8` image by ensuring all pixel values are in the correct range.
>> p) Creates a matrix of random numbers from a normal distribution.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Python `range()` function call with the sequence it generates.
>> [!example] Group A
>> a) `range(4)`
>> b) `range(1, 5)`
>> c) `range(0, 6, 2)`
>
>> [!example] Group B
>> n) `1, 2, 3, 4`
>> o) `0, 2, 4`
>> p) `0, 1, 2, 3`
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the code to the type of array manipulation it performs.
>> [!example] Group A
>> a) `height, width, _ = img.shape`
>> b) `cropped = img[50:100, 20:80]`
>> c) `red_channel = img[:, :, 2]`
>
>> [!example] Group B
>> n) Slicing to extract a Region of Interest (ROI).
>> o) Slicing to isolate a single color channel (in BGR).
>> p) Tuple unpacking to assign dimensions to variables.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Matplotlib function with its specific purpose in the workflow.
>> [!example] Group A
>> a) `plt.figure(figsize=(10, 5))`
>> b) `plt.subplot(1, 2, 1)`
>> c) `plt.tight_layout()`
>> d) `plt.axis('off')`
>
>> [!example] Group B
>> n) Activates the first cell of a 1x2 grid for plotting.
>> o) Creates a new figure window with a specific size in inches.
>> p) Hides the coordinate system ticks and labels.
>> q) Adjusts subplot spacing to prevent labels from overlapping.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> q)
>> d) -> p)

> [!question] Match the morphological operation's code constant to its primary use case.
>> [!example] Group A
>> a) `cv2.MORPH_OPEN`
>> b) `cv2.MORPH_CLOSE`
>
>> [!example] Group B
>> n) Filling small holes or gaps within an object ("pepper" noise).
>> o) Removing small, isolated noise specks from the background ("salt" noise).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the code for rotating an image to the step it performs.
>> [!example] Group A
>> a) `center = (w // 2, h // 2)`
>> b) `M = cv2.getRotationMatrix2D(center, 90, 1.0)`
>> c) `rotated = cv2.warpAffine(img, M, (w, h))`
>
>> [!example] Group B
>> n) Applies the calculated transformation to the image.
>> o) Defines the point around which the rotation will occur.
>> p) Creates the 2x3 transformation matrix that describes the rotation.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the NumPy statistical function to its role in the provided lab context.
>> [!example] Group A
>> a) `np.mean()`
>> b) `np.var()`
>> c) `np.unique()`
>
>> [!example] Group B
>> n) Used by the Nagao filter to find the smoothest sub-region.
>> o) Used to count the number of segmented cells after the watershed algorithm.
>> p) Used to calculate the Mean Squared Error for PSNR.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the variable assignment with the data type of the result.
>> [!example] Group A
>> a) `pixel = color_img[y, x]`
>> b) `shape = color_img.shape`
>> c) `value = gray_img[y, x]`
>
>> [!example] Group B
>> n) a `tuple`
>> o) a `np.uint8` scalar (or similar integer type)
>> p) a `NumPy array` of 3 elements
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the code snippet for pixel modification with the visual result.
>> [!example] Group A
>> a) `img[y, x] = [0, 255, 0]`
>> b) `img[y, x] = 0` (on a grayscale image)
>> c) `img[y, x] = [0, 0, 255]`
>
>> [!example] Group B
>> n) Sets the pixel to pure green.
>> o) Sets the pixel to pure red.
>> p) Sets the pixel to black.
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] Match the fundamental OpenCV functions to their typical sequence in a simple script.
>> [!example] Group A
>> a) Step 1
>> b) Step 2
>> c) Step 3
>> d) Step 4
>
>> [!example] Group B
>> n) `cv2.imshow('Window', img)`
>> o) `cv2.destroyAllWindows()`
>> p) `cv2.imread('image.png')`
>> q) `cv2.waitKey(0)`
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)