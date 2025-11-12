---
title: Core Python Concepts for Data Science
---

Beyond specific libraries like OpenCV and NumPy, a strong grasp of some core Python features is crucial for writing clean and efficient code in the labs. This note focuses on concepts you specifically asked about: array/list slicing, tuple unpacking (destructuring), and list comprehensions.

# Keywords
`#Python` `#Slicing` `#ListComprehension` `#Destructuring` `#DataManipulation`

---

## 1. Slicing in Python (Lists and NumPy Arrays)

Slicing is a powerful feature for accessing sub-parts of sequences like lists, tuples, or NumPy arrays. The syntax is `variable[start:stop:step]`.

- `start`: The index of the first item to include (default is 0).
- `stop`: The index of the first item to **exclude** (default is the end of the sequence).
- `step`: The amount to increment by (default is 1).

### Slicing 1D Arrays/Lists

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 up to (but not including) index 7
# -> [2, 3, 4, 5, 6]
print(f"Slice 1: {my_list[2:7]}")

# Get every second element from the whole list
# -> [0, 2, 4, 6, 8]
print(f"Slice 2: {my_list[::2]}")

# Get elements from index 1 to 8, in steps of 3
# -> [1, 4, 7]
print(f"Slice 3: {my_list[1:8:3]}")

# A common trick to reverse a sequence
# -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Slice 4: {my_list[::-1]}") 
```

### Slicing 2D NumPy Arrays (Images)
This is how we crop images. The slicing is applied to each dimension, separated by a comma: `image[y_slice, x_slice]`.

#### Example from Lab (`Lab_tp4.py`)
Let's break down the image cropping example.

```python
# cropped_image = imgOG[y : y+h, x : x+w]
# Let's assume y=30, h=120, x=200, w=200

# The slice for the Y-axis (rows) is `30:150`
# This selects all rows from 30 up to 149.

# The slice for the X-axis (columns) is `200:400`
# This selects all columns from 200 up to 399.

# The result is a new 2D array (the cropped image) containing only the
# pixels within that rectangular region.
```

---

## 2. Tuple Unpacking (Destructuring)

This is the process of assigning the elements of a tuple (or list) to multiple variables in a single line. It makes code cleaner and more readable.

### Basic Example
```python
# A tuple of coordinates
point = (10, 20)

# The "long" way
# x = point[0]
# y = point[1]

# The "Pythonic" way using unpacking
x, y = point

print(f"x = {x}, y = {y}") # -> x = 10, y = 20
```

### Example from Lab (Image Shape)
The `.shape` attribute of a NumPy array returns a tuple. We use unpacking to assign its values directly to variables.

```python
import cv2
img = cv2.imread('Images/pepper.bmp') # A color image

# The shape attribute returns a tuple, e.g., (512, 512, 3)
shape_tuple = img.shape 

# Unpack the tuple into three variables
height, width, channels = shape_tuple

print(f"Height: {height}, Width: {width}, Channels: {channels}")
```
This is far more readable than accessing them by index: `height = img.shape[0]`, `width = img.shape[1]`, etc.

---

## 3. List Comprehensions

A list comprehension offers a concise way to create lists. It consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.

**Structure:** `[expression for item in iterable if condition]`

### Example 1: Simple Transformation
Let's create a list of squared numbers.

```python
# The traditional for-loop way
squares = []
for i in range(10):
    squares.append(i * i)
print(f"Loop result: {squares}")

# The list comprehension way
squares_comp = [i * i for i in range(10)]
print(f"Comprehension result: {squares_comp}")
```

### Example 2: With a Condition
Let's get the squares of only the even numbers.

```python
# The traditional for-loop way
even_squares = []
for i in range(10):
    if i % 2 == 0:
        even_squares.append(i * i)
print(f"Loop result: {even_squares}")

# The list comprehension way
even_squares_comp = [i * i for i in range(10) if i % 2 == 0]
print(f"Comprehension result: {even_squares_comp}")
```

### Relevance to Lab Material
While not explicitly used in the provided lab files, list comprehensions are extremely common in data science and image processing for tasks like:
- Generating lists of file paths.
- Filtering data points based on a condition.
- Applying a simple function to each element in a list.

For instance, the filter testing loop in `exercise_2` could be partially rewritten to use comprehensions to build the results list, though the current `for` loop is perfectly clear for that multi-step task.