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
> [!question] The command `cv2.resize(img, (200, 300))` will resize the image to a height of 200 pixels and a width of 300 pixels.
>> [!success]- Answer
>> False

> [!question] The code `img[100, 50] = [255, 0, 0]` sets the pixel at row 100, column 50 to pure red in OpenCV's BGR color space.
>> [!success]- Answer
>> False

> [!question] In Matplotlib, the command `plt.subplot(2, 3, 1)` activates the first plot in a grid with 2 rows and 3 columns.
>> [!success]- Answer
>> True

> [!question] The `ksize` parameter in `cv2.medianBlur(src, ksize)` must be a tuple like `(5, 5)`.
>> [!success]- Answer
>> False

> [!question] The slicing syntax `my_array[::-1]` can be used to reverse a 1D NumPy array.
>> [!success]- Answer
>> True

> [!question] To ensure arithmetic operations on an image array do not cause overflow issues, it's a good practice to first convert it using `.astype(np.float32)`.
>> [!success]- Answer
>> True

> [!question] The function `cv2.getRotationMatrix2D(center, angle, scale)` expects the `angle` to be in radians.
>> [!success]- Answer
>> False

> [!question] The code `gray_img = cv2.imread('path.jpg', 0)` is a valid shortcut for loading an image in grayscale.
>> [!success]- Answer
>> True

> [!question] If `img` is a color image, `pixel = img[50, 100]` will assign a single integer value to the `pixel` variable.
>> [!success]- Answer
>> False

> [!question] The code `output = np.zeros_like(image)` creates a new black image with the same dimensions and data type as the source `image`.
>> [!success]- Answer
>> True

> [!question] Which line of code correctly unpacks the dimensions from a color image's shape attribute?
> a) `height, width = img.shape`
> b) `height, width, channels = img.shape`
> c) `dimensions = (height, width, channels).img.shape`
> d) `h, w, c = img.size`
>> [!success]- Answer
>> b) `height, width, channels = img.shape`

> [!question] How do you correctly crop a 100x50 region (100 pixels wide, 50 pixels high) starting from the top-left corner (0,0)?
> a) `cropped = img[0:100, 0:50]`
> b) `cropped = img[0:50, 0:100]`
> c) `cropped = cv2.crop(img, (0, 0, 100, 50))`
> d) `cropped = img.slice(0, 50, 0, 100)`
>> [!success]- Answer
>> b) `cropped = img[0:50, 0:100]`

> [!question] To convert a color image `img_bgr` for correct display in Matplotlib, which command should you use?
> a) `img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2BGR)`
> b) `img_rgb = cv2.convert(img_bgr, 'RGB')`
> c) `img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)`
> d) `img_rgb = plt.convert_color(img_bgr)`
>> [!success]- Answer
>> c) `img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)`

> [!question] Which code correctly applies a 7x7 Mean Filter to an image named `im`?
> a) `filtered = cv2.meanFilter(im, 7)`
> b) `filtered = cv2.blur(im, 7)`
> c) `filtered = cv2.blur(im, (7, 7))`
> d) `filtered = cv2.mean(im, ksize=7)`
>> [!success]- Answer
>> c) `filtered = cv2.blur(im, (7, 7))`

> [!question] What is the output of the following code? `np.clip(np.array([-50, 150, 350]), 0, 255)`
> a) `array([-50, 150, 350])`
> b) `array([0, 150, 255])`
> c) `array([50, 150, 255])`
> d) It will produce an error.
>> [!success]- Answer
>> b) `array([0, 150, 255])`

> [!question] To create a 5x5 elliptical structuring element for morphological operations, you would use:
> a) `kernel = cv2.createKernel(cv2.MORPH_ELLIPSE, 5)`
> b) `kernel = np.ellipse(5, 5)`
> c) `kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))`
> d) `kernel = cv2.structuringElement('ellipse', 5)`
>> [!success]- Answer
>> c) `kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))`

> [!question] Which function applies a transformation matrix (e.g., for rotation) to an image?
> a) `cv2.applyTransform()`
> b) `cv2.transform()`
> c) `cv2.warpAffine()`
> d) `cv2.rotateImage()`
>> [!success]- Answer
>> c) `cv2.warpAffine()`

> [!question] What is the correct way to display a grayscale image `gray_img` with Matplotlib?
> a) `plt.imshow(gray_img)`
> b) `plt.imshow(gray_img, color='gray')`
> c) `plt.imshow(gray_img, cmap='gray')`
> d) `plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB))`
>> [!success]- Answer
>> c) `plt.imshow(gray_img, cmap='gray')`

> [!question] Which code snippet creates a list of squared numbers from 0 to 9?
> a) `[x*x for x in range(10)]`
> b) `(x**2 if x in list(10))`
> c) `list(x^2 for x in 1..10)`
> d) `[x^2 in range(10)]`
>> [!success]- Answer
>> a) `[x*x for x in range(10)]`

> [!question] To draw a horizontal red line across the middle of an image `img` of `width` and `height`, which code is correct?
> a) `img[int(height/2), :] = [0, 0, 255]`
> b) `img[:, int(width/2)] = [255, 0, 0]`
> c) `img[int(height/2), :] = [255, 0, 0]`
> d) `img[:, int(width/2)] = [0, 0, 255]`
>> [!success]- Answer
>> a) `img[int(height/2), :] = [0, 0, 255]`

> [!question] Match the code for creating an array to its description.
>> [!example] Group A
>> a) `np.copy(image)`
>> b) `np.zeros_like(image)`
>> c) `np.random.normal(0, 1, image.shape)`
>> d) `np.clip(image, 0, 255)`
>
>> [!example] Group B
>> n) Creates an array of the same size as `image` filled with values from a Gaussian distribution.
>> o) Creates a new array filled with zeros, with the same dimensions and type as `image`.
>> p) Limits the values in `image` to be within the 0-255 range.
>> q) Creates a true, independent duplicate of the `image` array.
>
>> [!success]- Answer
>> a) -> q)
>> b) -> o)
>> c) -> n)
>> d) -> p)

> [!question] Match the filtering function to its required `ksize` (kernel size) parameter type.
>> [!example] Group A
>> a) `cv2.blur()`
>> b) `cv2.medianBlur()`
>
>> [!example] Group B
>> n) An integer (e.g., `5`).
>> o) A tuple (e.g., `(5, 5)`).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the image transformation function with the key parameter it requires.
>> [!example] Group A
>> a) `cv2.resize()`
>> b) `cv2.getRotationMatrix2D()`
>> c) `cv2.warpAffine()`
>
>> [!example] Group B
>> n) The `M` transformation matrix.
>> o) The `center` point of the operation.
>> p) The `dsize` tuple as `(width, height)`.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the code snippet to the color value it represents in OpenCV's BGR format.
>> [!example] Group A
>> a) `[0, 0, 0]`
>> b) `[255, 255, 255]`
>> c) `[255, 0, 0]`
>> d) `[0, 0, 255]`
>
>> [!example] Group B
>> n) White
>> o) Red
>> p) Black
>> q) Blue
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] Match the `cv2.morphologyEx` operation constant with its name.
>> [!example] Group A
>> a) `cv2.MORPH_OPEN`
>> b) `cv2.MORPH_CLOSE`
>
>> [!example] Group B
>> n) Dilation followed by Erosion.
>> o) Erosion followed by Dilation.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the Python variable assignment to its outcome.
>> [!example] Group A
>> a) `new_image = source_image`
>> b) `new_image = np.copy(source_image)`
>
>> [!example] Group B
>> n) Creates a new, independent copy of the image data in memory.
>> o) Creates a new reference; both variables point to the same image data.
>
>> [!success]-Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the `cv2.imread()` flag with the resulting array shape.
>> [!example] Group A
>> a) `cv2.imread('img.png', cv2.IMREAD_COLOR)`
>> b) `cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)`
>
>> [!example] Group B
>> n) `(height, width)`
>> o) `(height, width, 3)`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the standard plotting workflow command to its description.
>> [!example] Group A
>> a) `plt.figure()`
>> b) `plt.imshow(img)`
>> c) `plt.title('My Image')`
>> d) `plt.show()`
>
>> [!example] Group B
>> n) Renders the actual image data onto the active subplot.
>> o) Adds a text title to the active subplot.
>> p) Displays the complete figure window to the user.
>> q) Creates the main container for all plots.
>
>> [!success]- Answer
>> a) -> q)
>> b) -> n)
>> c) -> o)
>> d) -> p)

> [!question] Match the slicing operation with its result on the list `L = [10, 20, 30, 40, 50]`.
>> [!example] Group A
>> a) `L[1:4]`
>> b) `L[:3]`
>> c) `L[::2]`
>
>> [!example] Group B
>> n) `[10, 30, 50]`
>> o) `[20, 30, 40]`
>> p) `[10, 20, 30]`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Python code to the data type it primarily handles or returns.
>> [!example] Group A
>> a) `img.shape`
>> b) `img.dtype`
>> c) `cv2.imread('color.png')`
>
>> [!example] Group B
>> n) Returns a NumPy `ndarray` object.
>> o) Returns a `tuple`.
>> p) Returns a `dtype` object (e.g., `uint8`).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)