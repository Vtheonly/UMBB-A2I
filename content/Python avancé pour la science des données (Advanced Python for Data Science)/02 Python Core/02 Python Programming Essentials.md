
# Python Programming Essentials

## 1. Data Structures

### Lists (`[]`)
*   **Ordered** and **Mutable** (Changeable).
*   **Slicing:** `list[start:stop:step]`
    *   `my_list[::-1]` reverses the list.
    *   `my_list[0:3]` takes index 0, 1, 2 (Stop index is **exclusive**).

### Tuples (`()`)
*   **Ordered** and **Immutable** (Cannot change once created).
*   **Use Case:** Coordinates, return values from functions, data that shouldn't change.
*   *Tip:* Accessing tuples is slightly faster than lists.

### Dictionaries (`{key: value}`)
*   Key-Value pairs. Keys must be unique and immutable.
*   **Access:** `my_dict['key']` (Crashes if key missing) vs `my_dict.get('key')` (Returns None if missing - **Safer**).

### Sets (`{}`)
*   Unordered collection of **unique** elements.
*   **Use Case:** Removing duplicates instantly: `list(set(my_list))`.
*   **Operations:** Union (`|`), Intersection (`&`), Difference (`-`).

## 2. Advanced Control Flow

### List Comprehensions
A concise way to create lists. Pythonic and often faster than loops.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Traditional Loop
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# List Comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
```

### `zip()` and `enumerate()`
*   **`enumerate(list)`**: Returns `(index, item)` pairs. Essential when you need the index inside a loop.
*   **`zip(list_a, list_b)`**: Pairs elements from two lists together like a zipper.

## 3. Functions and Modules

### Lambda Functions
Anonymous, one-line functions.
*   *Syntax:* `lambda arguments: expression`
*   *Usage:* Often used inside `map()`, `filter()`, or Pandas `apply()`.
    ```python
    df['Price'].apply(lambda x: x * 1.2) # Increases price by 20%
    ```

### Modular Code (`if __name__ == "__main__":`)
This block is crucial for professional scripts.
*   Code inside this block **only runs if the file is executed directly** (e.g., `python script.py`).
*   It **does not run** if the file is imported as a module (`import script`).
*   *Why?* It allows you to write functions in a file that can be reused by others without triggering the main script logic immediately.

## 4. File I/O (Context Managers)
Always use the `with` statement.

```python
# Best Practice
with open("data.txt", "r") as f:
    content = f.read()
# File closes automatically here, even if an error occurs.
```

*   `strip()`: Removes hidden characters like `\n` (newline) from read lines. Essential for data cleaning.

