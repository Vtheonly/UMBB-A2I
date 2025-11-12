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
> [!question] A digital image is inherently discrete, with both its spatial coordinates and its intensity values quantized into finite numbers.
>> [!success]- Answer
>> True

> [!question] What is the smallest individual component of a digital image called?
> a) Dot
> b) Element
> c) Pixel
> d) Voxel
>> [!success]- Answer
>> c) Pixel

> [!question] Scaling a vector image to a larger size typically results in a loss of quality and pixelation.
>> [!success]- Answer
>> False

> [!question] Which of the following is an example of a vector image format?
> a) JPEG
> b) PNG
> c) BMP
> d) SVG
>> [!success]- Answer
>> d) SVG

> [!question] Match the term with its correct definition regarding image representation.
>> [!example] Group A
>> a) Bitmap Image
>> b) Vector Image
>> c) Resolution Dependent
>
>> [!example] Group B
>> n) Quality is tied to the number of pixels; scaling up causes blurriness.
>> o) Composed of mathematical objects like points, lines, and curves.
>> p) Composed of a grid of individual pixels, ideal for photorealism.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Spatial resolution refers to the number of distinct colors that can be represented for each pixel.
>> [!success]- Answer
>> False

> [!question] A 24-bit "True Color" image uses 8 bits for each of the three color channels (Red, Green, and Blue).
>> [!success]- Answer
>> True

> [!question] What does a color depth of 1-bit represent?
> a) A grayscale image with 256 shades
> b) A "True Color" image
> c) A binary image with only two colors (e.g., black and white)
> d) A high dynamic range image
>> [!success]- Answer
>> c) A binary image with only two colors (e.g., black and white)

> [!question] In the RGB color model, the value `(0, 0, 0)` corresponds to which color?
> a) White
> b) Red
> c) Gray
> d) Black
>> [!success]- Answer
>> d) Black

> [!question] Match the component of the HSL color space with its description.
>> [!example] Group A
>> a) Hue
>> b) Saturation
>> c) Lightness
>
>> [!example] Group B
>> n) The "purity" or intensity of the color.
>> o) The brightness of the color.
>> p) The type of color (e.g., red, green, blue).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] PNG is a lossy compression format, which is why it's ideal for photographs.
>> [!success]- Answer
>> False

> [!question] A histogram clustered to the left side of the x-axis indicates a very bright image.
>> [!success]- Answer
>> False

> [!question] Which image format uses lossy compression and is the most common choice for photographs on the web?
> a) PNG
> b) TIFF
> c) JPEG
> d) BMP
>> [!success]- Answer
>> c) JPEG

> [!question] A narrow image histogram that occupies only a small portion of the intensity range suggests what about the image?
> a) It has high contrast.
> b) It has low contrast.
> c) It is a vector image.
> d) It has salt-and-pepper noise.
>> [!success]- Answer
>> b) It has low contrast.

> [!question] The N4 neighborhood of a pixel includes its diagonal neighbors.
>> [!success]- Answer
>> False

> [!question] Which specialized format is the standard for storing and transmitting medical images like MRIs and CT scans?
> a) RAW
> b) TIFF
> c) DICOM
> d) EPS
>> [!success]- Answer
>> c) DICOM

> [!question] Match the distance metric with its common name.
>> [!example] Group A
>> a) d₁
>> b) d₂
>> c) d_inf
>
>> [!example] Group B
>> n) Euclidean Distance
>> o) Chessboard Distance
>> p) City-Block / Manhattan Distance
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] The Chebyshev distance between two pixels is always less than or equal to the Euclidean distance between them.
>> [!success]- Answer
>> True

> [!question] What are the two primary attributes of a pixel?
> a) Size and Shape
> b) Position and Value
> c) Hue and Saturation
> d) Resolution and Depth
>> [!success]- Answer
>> b) Position and Value

> [!question] What is the primary advantage of the HSL color space over RGB for color manipulation tasks?
> a) It has smaller file sizes.
> b) It is more aligned with human perception, making it easier to change one aspect like color type (Hue) independently.
> c) It is a device-independent color space.
> d) It supports a wider range of colors than RGB.
>> [!success]- Answer
>> b) It is more aligned with human perception, making it easier to change one aspect like color type (Hue) independently.