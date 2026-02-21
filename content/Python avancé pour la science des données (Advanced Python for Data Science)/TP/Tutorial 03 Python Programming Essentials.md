This guide walks you through the solution for **Tutorial 03: Python Programming Essentials**.

Based on the provided course notes and the lab PDF, this project aims to teach you **Modular Programming** (breaking code into separate files) and **Data Processing Pipelines**.

Here is the step-by-step implementation and the reasoning behind each part.

---

### 0. Project Setup (Folder Structure)
Before writing code, you must create the folder structure shown in the PDF (Exercise 6 screenshot). This structure makes Python treat your folders as "packages" so you can import files from one to another.

```text
Sales_project/
├── data/
│   └── raw/
│       └── data.txt       <-- Create this file manually
├── scripts/
│   └── create_products.py
├── utils/
│   ├── __init__.py        <-- Create empty file (Crucial!)
│   ├── helpers.py
│   └── product.py
└── notebooks/
    └── analysis.ipynb
```

**Reasoning:** As explained in *Course Note 3 (Functions and Modular Code)*, separating scripts from modules makes code reusable and organized. The `__init__.py` file tells Python "Treat the `utils` folder as a library so I can import from it."

---

### 1. `utils/helpers.py` (Exercises 1 & 2)

This file contains the "tools" for cleaning raw text.

**Code:**
```python
# utils/helpers.py

def clean_lines(lines):
    """
    Exercise 1: Removes empty lines and trims extra spaces using List Comprehensions.
    """
    # Logic: Loop through lines, strip whitespace. Keep only if the line is not empty.
    cleaned = [line.strip() for line in lines if line.strip()]
    return cleaned

def parse_products(lines):
    """
    Exercise 2: Converts string lines into tuples (name, price, quantity).
    Includes Error Handling for robustness.
    """
    parsed_list = []
    
    for line in lines:
        try:
            # Split "Laptop,1000,3" into ["Laptop", "1000", "3"]
            parts = line.split(',')
            
            # Unpack and convert types (Casting)
            name = parts[0].strip()
            price = float(parts[1])  # Convert string "1000" to float 1000.0
            quantity = int(parts[2]) # Convert string "3" to int 3
            
            parsed_list.append((name, price, quantity))
            
        except (ValueError, IndexError):
            # As per Course Note 5 (Exceptions): catch specific errors.
            # If a line is "BadData,Free", conversion fails. We skip it instead of crashing.
            print(f"Warning: Skipping malformed line: '{line}'")
            continue
            
    return parsed_list
```

**Reasoning:**
*   **`clean_lines`:** Uses `.strip()` to remove invisible characters (newline `\n`) and List Comprehensions (Course Note 2) for efficiency.
*   **`parse_products`:** Real-world data is dirty. We use `try...except` (Course Note 5) to prevent the whole program from crashing just because one line in the text file is formatted incorrectly.

---

### 2. `utils/product.py` (Exercise 3)

This defines the Blueprint for a Product using Object-Oriented Programming.

**Code:**
```python
# utils/product.py

class Product:
    def __init__(self, name, price, quantity):
        """Constructor: Initializes attributes."""
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        """Method: Encapsulates the calculation logic."""
        return self.price * self.quantity
    
    def __repr__(self):
        """
        Optional but recommended: Makes printing the object readable.
        Without this, print(p) shows <Product object at 0x...>
        """
        return f"Product({self.name}, Total={self.total_value()})"
```

**Reasoning:**
*   As per *Course Note 4 (OOP)*, creating a Class allows us to bundle data (`price`, `quantity`) with logic (`total_value`).
*   `self` ensures that when we calculate total value, it uses the specific numbers for *that specific instance* of the product.

---

### 3. Create the Data File
Create a file at `data/raw/data.txt` and paste this content:
```text
Laptop,1000,3

Phone,500,5
Tablet,700,2
Monitor,300,4
Camera,400,1
```

---

### 4. `scripts/create_products.py` (Exercise 4)

This script ties everything together.

**Code:**
```python
# scripts/create_products.py
import sys
import os

# Ensure Python can find the 'utils' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import clean_lines, parse_products
from utils.product import Product

def main():
    # 1. Define file path (using os.path is safer than hardcoding strings)
    file_path = os.path.join("data", "raw", "data.txt")
    
    # 2. Read File (Course Note 3: Using 'with open')
    with open(file_path, "r") as f:
        raw_lines = f.readlines()
        
    # 3. Use Utils to clean and parse
    cleaned = clean_lines(raw_lines)
    parsed_data = parse_products(cleaned)
    
    # 4. Create Objects
    products = []
    total_sales = 0.0
    
    print("--- Individual Product Sales ---")
    for item in parsed_data:
        # Create instance: Product("Laptop", 1000.0, 3)
        p = Product(item[0], item[1], item[2]) 
        products.append(p)
        
        # Calculate totals
        val = p.total_value()
        total_sales += val
        
        print(f"{p.name}: {val}")
        
    print("\n--- Final Report ---")
    print(f"Total Sales: {total_sales}")

if __name__ == "__main__":
    main()
```

**Expected Output:**
```text
--- Individual Product Sales ---
Laptop: 3000.0
Phone: 2500.0
Tablet: 1400.0
Monitor: 1200.0
Camera: 400.0

--- Final Report ---
Total Sales: 8500.0
```

---

### 5. `notebooks/analysis.ipynb` (Exercise 5)

This assumes you are running this inside a Jupyter Notebook or VS Code.

**Code:**
```python
# Cell 1: Imports
import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath('..')) # Add parent directory to path

from utils.helpers import clean_lines, parse_products
from utils.product import Product

# Cell 2: Load Data
with open("../data/raw/data.txt", "r") as f:
    lines = clean_lines(f.readlines())
    data = parse_products(lines)

# Create objects
products = [Product(n, p, q) for n, p, q in data]

# Cell 3: Visualization
names = [p.name for p in products]
sales = [p.total_value() for p in products]

plt.figure(figsize=(10, 5))
plt.bar(names, sales, color='skyblue')
plt.xlabel("Product Name")
plt.ylabel("Total Sales ($)")
plt.title("Sales by Product")
plt.show()
```

---

### 6. The "One Million Products" Solution (Exercise 6)

**The Problem:** In Exercise 4, we used `f.readlines()`. This loads the *entire* file into a Python List. If the file has 1 million lines, your computer runs out of RAM (Memory) and crashes.

**The Solution:** Use a **Generator** (Course Note 5). A generator processes one line at a time, "yields" the result, and then forgets that line to free up memory.

**Add this code to `utils/helpers.py`:**

```python
def process_large_file(file_path):
    """
    Exercise 6 Solution: A Generator for Big Data.
    Instead of returning a list, it yields one Product at a time.
    """
    with open(file_path, 'r') as f:
        for line in f:
            # Clean logic inside the loop
            line = line.strip()
            if not line:
                continue
            
            try:
                parts = line.split(',')
                name = parts[0].strip()
                price = float(parts[1])
                quantity = int(parts[2])
                
                # Create object and hand it over immediately
                # Python pauses here until the next loop iteration is requested
                yield Product(name, price, quantity) 
                
            except ValueError:
                continue
```

**How to use it (optimized script):**
```python
# This uses almost 0 RAM, even with 1 million lines
total_sales = 0

# The generator gives us one product at a time
for product in process_large_file("data/raw/data.txt"):
    total_sales += product.total_value()
    # After this line, 'product' is discarded from memory

print(f"Total Sales: {total_sales}")
```