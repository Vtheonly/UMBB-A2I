Here is the first batch of 5 exercises, focusing on **TD N° 1 BDA : Rappel SQL** (The Car Dealership Database).

**Context Schema:**
*   `FOURN (NF, NomF, Code, VilleF)`
*   `REVEND (NR, NomR, VilleR)`
*   `VOITURE (NV, NomV, Couleur, Prix)`
*   `FVR (NF, NV, NR, Qté)` - *Association Table (Supplier-Car-Dealer)*

---

### Exercise 1: Information on All Dealers

**Source:** TD N° 1 BDA : Rappel SQL - Question 1
**Question:** "Donnez tous les renseignements sur tous les revendeurs." (Give all details about all dealers.)

#### 1. Solution
```sql
SELECT * 
FROM REVEND;
```

#### 2. Reasoning
The request asks for "all details" (all columns) and "all dealers" (all rows) without any specific filtering condition. In SQL, the wildcard `*` selects every column defined in the table schema.

#### 3. Detailed Explanation
*   **`SELECT *`**: This tells the database engine to retrieve data from every column (`NR`, `NomR`, `VilleR`) available in the table. It is equivalent to writing `SELECT NR, NomR, VilleR`.
*   **`FROM REVEND`**: Specifies the target table.
*   **Note:** While `SELECT *` is convenient for ad-hoc queries, in production applications (like Java or PHP apps), it is often better to list specific columns explicitly. This prevents the application from breaking if a new column is added to the database later.

---

### Exercise 2: Dealers in London

**Source:** TD N° 1 BDA : Rappel SQL - Question 2
**Question:** "Donnez tous les renseignements sur les revendeurs habitant Londres." (Give all details about dealers living in London.)

#### 1. Solution
```sql
SELECT * 
FROM REVEND 
WHERE VilleR = 'LONDRES';
```

#### 2. Reasoning
We need to filter the rows based on a specific attribute value. The condition corresponds to the column `VilleR`. Since "LONDRES" is a string literal, it must be enclosed in single quotes.

#### 3. Detailed Explanation
*   **`WHERE` Clause**: This clause acts as a filter. The database engine scans the `REVEND` table and evaluates the condition `VilleR = 'LONDRES'` for each row.
*   **String Sensitivity**: In standard SQL, string comparisons can be case-sensitive depending on the collation of the database. If 'Londres' is stored as 'London' or 'LONDRES', the query must match exactly unless a function like `UPPER()` is used.
*   **Result**: Only the tuples (rows) where the city matches exactly are returned in the result set.

---

### Exercise 3: Suppliers for Dealer R1

**Source:** TD N° 1 BDA : Rappel SQL - Question 3
**Question:** "Quels sont les numéros des fournisseurs fournissant des voitures au revendeur R1 ?" (Which supplier numbers supply cars to dealer R1?)

#### 1. Solution
```sql
SELECT DISTINCT NF 
FROM FVR 
WHERE NR = 'R1';
```

#### 2. Reasoning
The relationship between suppliers and dealers is stored in the association table `FVR`. We do not need the names of the suppliers, only their numbers (`NF`), so we do not need to join with the `FOURN` table. A dealer might receive multiple deliveries from the same supplier, so `DISTINCT` is required to remove duplicates.

#### 3. Detailed Explanation
*   **Target Table**: `FVR` contains the links between `NF` (Supplier), `NV` (Car), and `NR` (Dealer).
*   **Condition**: `NR = 'R1'` filters entries specifically for dealer R1.
*   **`DISTINCT`**: If Supplier F1 supplied a car to R1 on Monday and another car on Tuesday, F1 appears twice in the `FVR` table for R1. The question asks "Which suppliers", implying a set of unique identifiers. `DISTINCT` ensures F1 is listed only once.

---

### Exercise 4: Suppliers of Car V1 to Dealer R1

**Source:** TD N° 1 BDA : Rappel SQL - Question 4
**Question:** "Quels sont les numéros des fournisseurs qui fournissent des voitures V1 au revendeur R1 ?" (Which supplier numbers supply car V1 to dealer R1?)

#### 1. Solution
```sql
SELECT DISTINCT NF 
FROM FVR 
WHERE NR = 'R1' 
  AND NV = 'V1';
```

#### 2. Reasoning
This is a refinement of the previous query. We now have two conditions that must be true simultaneously: the dealer must be 'R1' AND the car product must be 'V1'.

#### 3. Detailed Explanation
*   **`AND` Operator**: Logical operators combine conditions. Both `NR='R1'` and `NV='V1'` must be satisfied for a row to be selected.
*   **Index Usage**: In a real-world scenario, a composite index on `(NR, NV)` would make this query extremely fast because the database could jump directly to the relevant pointers without scanning the whole table.
*   **Data Integrity**: This query assumes 'V1' and 'R1' exist. If they don't, the result is simply an empty set (no error).

---

### Exercise 5: Names of Dealers Supplied by F1

**Source:** TD N° 1 BDA : Rappel SQL - Question 5
**Question:** "Quels sont les noms des revendeurs dont l’un des fournisseurs est F1 ?" (What are the names of the dealers where one of the suppliers is F1?)

#### 1. Solution
**Option A (Using Join):**
```sql
SELECT DISTINCT R.NomR 
FROM REVEND R
JOIN FVR L ON R.NR = L.NR
WHERE L.NF = 'F1';
```

**Option B (Using Subquery):**
```sql
SELECT NomR 
FROM REVEND 
WHERE NR IN (SELECT NR FROM FVR WHERE NF = 'F1');
```

#### 2. Reasoning
The information is split across two tables:
1.  `REVEND` contains the names (`NomR`).
2.  `FVR` contains the supply logic (`NF` -> `NR`).
We must link these tables using the common key `NR` (Dealer Number).

#### 3. Detailed Explanation
*   **Join Logic (Option A)**:
    *   We create a Cartesian product of `REVEND` and `FVR`.
    *   We filter to keep only rows where the Dealer Numbers match (`R.NR = L.NR`).
    *   We filter again to keep only rows where the supplier is 'F1'.
    *   `DISTINCT` is crucial here because if F1 made 10 deliveries to the same dealer, the join would produce the dealer's name 10 times.
*   **Subquery Logic (Option B)**:
    *   The inner query `(SELECT NR FROM FVR WHERE NF = 'F1')` builds a list of IDs (e.g., 'R1', 'R2').
    *   The outer query selects the names of dealers whose ID is inside that list.
    *   This approach is often more readable for "set membership" questions ("Is this dealer in the set of F1's clients?").