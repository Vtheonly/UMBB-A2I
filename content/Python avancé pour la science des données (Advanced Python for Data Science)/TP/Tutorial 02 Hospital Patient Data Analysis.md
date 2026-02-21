
# Lab Solution: Hospital Patient Data Analysis

## Phase 1: Environment & Project Setup

### Step 1: Create the Project Directory
**Command:**
```bash
mkdir HospitalDataAnalysis
cd HospitalDataAnalysis
```
**Reasoning (Course File 9):** 
Organization is critical. We create a dedicated root folder to contain all files related to this specific analysis, keeping our file system clean.

### Step 2: Create a Virtual Environment
**Command (Terminal):**
```bash
# Windows
python -m venv env

# macOS/Linux
python3 -m venv env
```
**Reasoning (Course File 5):** 
We create a **Virtual Environment** (`env`) to isolate this project. As explained in File 5, this prevents "Dependency Hell." If this project needs `pandas` v1.0 and another project on your computer needs `pandas` v2.0, a global installation would cause a conflict. The virtual environment ensures this project has its own standalone Python installation.

### Step 3: Activate and Install Libraries
**Command:**
```bash
# Activate - Windows
.\env\Scripts\activate

# Activate - macOS/Linux
source env/bin/activate

# Install
pip install numpy pandas matplotlib
```
*(Note: You will see `(env)` appear in your terminal prompt indicating activation.)*

**Reasoning (Course File 6 & 7):**
*   **Activation:** Tells the terminal to use the Python interpreter inside our `env` folder, not the system-wide one.
*   **Installation:** We install the standard Data Science stack (File 7):
    *   `pandas` for data manipulation (DataFrames).
    *   `numpy` for the underlying math.
    *   `matplotlib` is required for the plotting step in the PDF (Step 5).

### Step 4: Create Project Structure
**Action:** Create the following folders and files manually or via command line.
```text
HospitalDataAnalysis/
├── env/                (Created in Step 2)
├── data/               (Create this folder)
├── notebooks/          (Create this folder)
├── scripts/            (Create this folder)
├── .gitignore          (Create empty file)
└── README.md           (Create empty file)
```

**Reasoning (Course File 4):**
This adheres to the "Standard Directory Tree" for professional data science:
*   **`data/`**: Separates data from code. This prevents accidental deletion or corruption of raw data files.
*   **`notebooks/`**: Keeps experimental `.ipynb` files separate from production scripts.
*   **`env/`**: Contains the heavy library binaries.

---

## Phase 2: Data Analysis & Visualization (The Notebook)

**Action:** Create a CSV file named `patients.csv` inside the `data/` folder with the following dummy content:
```csv
PatientID,Age,Sex,BloodPressure,Cholesterol,Diagnosis
1,45,Male,120,200,Healthy
2,50,Female,130,240,High Risk
3,60,Male,140,260,High Risk
4,30,Female,110,180,Healthy
5,70,Male,150,280,High Risk
```

**Action:** Create a Jupyter Notebook inside `notebooks/` (e.g., `analysis.ipynb`) and run the following cells.

### Cell 1: Loading Data
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
# We use '..' to go up one level from 'notebooks/' then into 'data/'
df = pd.read_csv('../data/patients.csv')

# Display first few rows
df.head()
```
**Reasoning (Course File 7):** 
We use **Pandas** to read the CSV into a DataFrame. A DataFrame acts like a programmable Excel sheet, allowing us to manipulate rows and columns programmatically.

### Cell 2: Descriptive Statistics
```python
# Numerical statistics
print(df.describe())

# Categorical counts
print(df['Sex'].value_counts())
print(df['Diagnosis'].value_counts())
```
**Reasoning:**
*   `describe()` gives us the distribution (mean, max, min) to sanity-check the data (e.g., ensuring no one has an age of 200).
*   `value_counts()` is essential for categorical data to check for dataset imbalance (e.g., do we have enough "High Risk" patients to analyze?).

### Cell 3: Visualization
```python
# Scatter Plot: Age vs Cholesterol
plt.figure(figsize=(8, 5))

# We use 'o' for dots and linestyle='none' to avoid connecting lines
plt.plot(df['Age'], df['Cholesterol'], marker='o', linestyle='none', color='blue')

plt.title('Cholesterol Levels by Age')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.grid(True)
plt.show()
```
**Reasoning (Course File 7):**
We use **Matplotlib**. As noted in the provided solution text, `linestyle='none'` is crucial. By default, `plt.plot` draws a line chart (connecting point A to B). Since Patient A and Patient B are unrelated individuals, a line implies a sequence that doesn't exist. We remove the line to create a **Scatter Plot**.

---

## Phase 3: Version Control (Git)

### Step 5 (Git): Initialize and Configure
**Command:**
```bash
git init
```

**Action:** Open the `.gitignore` file and add the following lines:
```text
env/
__pycache__/
*.pyc
.ipynb_checkpoints/
```

**Reasoning (Course File 8 & 9):**
*   **`git init`**: Starts tracking the folder.
*   **`.gitignore`**: This is vital. The `env/` folder contains thousands of small files (the libraries). We **never** push the environment to GitHub because it is large and OS-specific. We only want to push our source code.

### Step 6: Commit and Push
**Command:**
```bash
git add .
git commit -m "Initial project setup with patient analysis"
# (Optional: Link to GitHub if you have a repo URL)
# git remote add origin <URL>
# git push -u origin main
```

---

## Phase 4: Sharing the Environment

### Step 7: Freeze Dependencies
**Command:**
```bash
pip freeze > requirements.txt
```

**Reasoning (Course File 6):**
Since we ignored the `env/` folder in Git, how does a colleague run our code?
We generate `requirements.txt`. This text file lists the names and exact versions of the libraries we used (e.g., `pandas==2.0.3`).
A colleague can clone our code and simply run `pip install -r requirements.txt` to reconstruct the exact environment on their machine.

---

## Summary of Concepts (Why did we do this?)

1.  **Isolation (Virtual Env):** We ensured our medical analysis project doesn't break if we update Python for a different project later.
2.  **Reproducibility (requirements.txt):** We made sure that anyone, anywhere, can run this analysis and get the same results by listing our exact dependencies.
3.  **Scalability (Directory Structure):** By separating `data` (raw material) from `notebooks` (lab/experimentation), we prevent errors and make it easier to add new data later without rewriting code.