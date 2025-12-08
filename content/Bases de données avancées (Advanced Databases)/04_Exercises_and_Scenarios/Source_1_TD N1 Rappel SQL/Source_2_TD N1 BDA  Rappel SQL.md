Here is the second batch of 5 exercises, continuing with **TD N° 1 BDA : Rappel SQL** (The Car Dealership Database).

---

### Exercise 6: Dealers With No Deliveries

**Source:** TD N° 1 BDA : Rappel SQL - Question 6
**Question:** "Quels sont les noms des revendeurs pour lesquels aucune voiture n’est fournie ?" (What are the names of the dealers to whom no car is supplied?)

#### 1. Solution
```sql
SELECT NomR 
FROM REVEND 
WHERE NR NOT IN (SELECT DISTINCT NR FROM FVR);
```
*Alternative (Using NOT EXISTS):*
```sql
SELECT NomR 
FROM REVEND R
WHERE NOT EXISTS (SELECT 1 FROM FVR F WHERE F.NR = R.NR);
```

#### 2. Reasoning
We need to find dealers present in the `REVEND` table but *missing* from the `FVR` (supply) table. This is a classic "set difference" problem (A - B).

#### 3. Detailed Explanation
*   **`NOT IN` Logic**:
    *   The subquery `SELECT DISTINCT NR FROM FVR` generates the list of all "active" dealers (those who have received at least one car).
    *   The outer query selects dealers whose ID is NOT in that list.
*   **Potential Pitfall (NULLs)**: If the column `FVR.NR` allowed NULL values, `NOT IN` would fail (it would return an empty set because `val != NULL` is unknown). Since `NR` is part of a primary key in `REVEND`, it is implicitly not null, but `NOT EXISTS` is generally safer and often more performant in modern optimizers.
*   **`NOT EXISTS` Logic**: For every dealer in `REVEND`, the database checks the `FVR` table. If it finds *no* rows linking to that dealer, the condition is true.

---

### Exercise 7: Suppliers for Both R1 and R2

**Source:** TD N° 1 BDA : Rappel SQL - Question 7
**Question:** "Quels sont les numéros des fournisseurs qui fournissent chacun simultanément des voitures pour les revendeurs R1 et R2 ?" (Which supplier numbers supply cars to BOTH dealer R1 and dealer R2?)

#### 1. Solution
```sql
SELECT NF 
FROM FVR 
WHERE NR = 'R1'
INTERSECT
SELECT NF 
FROM FVR 
WHERE NR = 'R2';
```
*Alternative (SQL Standard - Self Join):*
```sql
SELECT DISTINCT T1.NF 
FROM FVR T1 
JOIN FVR T2 ON T1.NF = T2.NF 
WHERE T1.NR = 'R1' AND T2.NR = 'R2';
```

#### 2. Reasoning
This requires an intersection of two sets:
1.  Set A: Suppliers who supply R1.
2.  Set B: Suppliers who supply R2.
We need suppliers found in *both* A and B.

#### 3. Detailed Explanation
*   **`INTERSECT`**: This set operator explicitly returns values common to both result sets. It is clean and mathematically precise.
*   **Self-Join approach**:
    *   We look at the table `FVR` twice (aliased as T1 and T2).
    *   We join T1 and T2 on the Supplier Number (`NF`), meaning "we are talking about the same supplier".
    *   We apply the condition: In instance T1, the dealer is R1. In instance T2, the dealer is R2.
    *   This proves that supplier `NF` exists in both contexts.

---

### Exercise 8: Suppliers of Red Cars to R1

**Source:** TD N° 1 BDA : Rappel SQL - Question 8
**Question:** "Quels sont les numéros des fournisseurs qui fournissent au moins une voiture rouge au revendeur R1 ?" (Which supplier numbers supply at least one red car to dealer R1?)

#### 1. Solution
```sql
SELECT DISTINCT F.NF 
FROM FVR F
JOIN VOITURE V ON F.NV = V.NV
WHERE F.NR = 'R1' 
  AND V.Couleur = 'ROUGE';
```

#### 2. Reasoning
We need to link the supply chain (`FVR`) with product details (`VOITURE`). The filtering criteria apply to both tables: the dealer (`FVR.NR`) and the car attribute (`VOITURE.Couleur`).

#### 3. Detailed Explanation
*   **Join Operation**: `FVR` connects suppliers to cars (`NV`). `VOITURE` connects cars to colors. By joining `F.NV = V.NV`, we associate the color "Red" with the transaction.
*   **Composite Condition**: The `WHERE` clause acts as a double filter. We only care about rows where *both* the recipient is R1 *and* the object received is Red.
*   **Optimization**: The database optimizer will likely filter `NR='R1'` first (using an index on FVR) and then look up the car color, rather than checking all red cars first, as R1 transactions are likely fewer than total red cars in the database.

---

### Exercise 9: Cars Supplied to All London Dealers

**Source:** TD N° 1 BDA : Rappel SQL - Question 9
**Question:** "Donnez les numéros des voitures fournies pour tous les revendeurs de Londres ?" (Give the car numbers supplied to ALL dealers in London?)

#### 1. Solution
*(This is a classic Relational Division problem)*

```sql
SELECT V.NV
FROM VOITURE V
WHERE NOT EXISTS (
    -- Find a London dealer...
    SELECT R.NR 
    FROM REVEND R 
    WHERE R.VilleR = 'LONDRES'
    AND NOT EXISTS (
        -- ...to whom this car (V.NV) has NOT been supplied.
        SELECT 1 
        FROM FVR F 
        WHERE F.NR = R.NR 
          AND F.NV = V.NV
    )
);
```

#### 2. Reasoning
The query asks for cars where the set of "London Dealers supplied with this car" contains the set of "All London Dealers".
In SQL, we rephrase "All X are Y" as "There is no X that is NOT Y".
*Translation:* Find cars such that there does not exist a London dealer who has *not* received this car.

#### 3. Detailed Explanation
*   **Outer Query**: Iterates through every car `V.NV`.
*   **Middle Query**: Finds all dealers in London.
*   **Inner Query**: Checks if there is a supply record (`FVR`) linking the current car (`V.NV`) to the current London dealer (`R.NR`).
*   **Logic Flow**:
    1.  Pick a car.
    2.  Look for a "Counter-Example": A London dealer who *didn't* get this car.
    3.  If no counter-example is found (`NOT EXISTS` returns true), then the car was supplied to everyone.

---

### Exercise 10: Suppliers of Red Cars to Paris or London

**Source:** TD N° 1 BDA : Rappel SQL - Question 10
**Question:** "Quels sont les numéros des fournisseurs qui fournissent des voitures rouges pour des revendeurs situés à Paris et Londres ?" (Which supplier numbers supply red cars to dealers located in Paris AND London?)
*(Note: The French phrasing "Paris et Londres" implies the set of target cities is {Paris, London}, but usually in SQL contexts, we interpret this as supplying to a dealer in Paris OR a dealer in London, OR supplying to BOTH distinct locations. Given typical exam patterns, let's assume the question implies suppliers active in this **zone** (Union of cities). However, if it implies "Suppliers who have clients in Paris AND clients in London", that is an Intersection problem).*

**Interpretation A (Union - Most likely simple filter):** "Suppliers supplying red cars to dealers in Paris or London".
**Interpretation B (Intersection - Strict):** "Suppliers who supply at least one red car to Paris AND at least one red car to London".

#### 1. Solution (Interpretation A - Union/List)
```sql
SELECT DISTINCT F.NF 
FROM FVR F
JOIN REVEND R ON F.NR = R.NR
JOIN VOITURE V ON F.NV = V.NV
WHERE V.Couleur = 'ROUGE'
  AND R.VilleR IN ('PARIS', 'LONDRES');
```

#### 1. Solution (Interpretation B - Intersection)
```sql
SELECT NF FROM FVR F, REVEND R, VOITURE V 
WHERE F.NR=R.NR AND F.NV=V.NV AND V.Couleur='ROUGE' AND R.VilleR='PARIS'
INTERSECT
SELECT NF FROM FVR F, REVEND R, VOITURE V 
WHERE F.NR=R.NR AND F.NV=V.NV AND V.Couleur='ROUGE' AND R.VilleR='LONDRES';
```

#### 2. Reasoning
We need three tables: `FVR` (Link), `REVEND` (City), `VOITURE` (Color).
*   **Interpretation A**: Simply filters rows where City is Paris OR London.
*   **Interpretation B**: Ensures the supplier appears in the "Paris Red Car" dataset AND the "London Red Car" dataset.

#### 3. Detailed Explanation
*   **Triple Join**: We join `FVR` to `REVEND` to check the city, and to `VOITURE` to check the color.
*   **`IN` Operator**: `R.VilleR IN ('PARIS', 'LONDRES')` is shorthand for `R.VilleR = 'PARIS' OR R.VilleR = 'LONDRES'`.
*   This effectively finds any transaction matching the criteria. If a supplier sends a Red car to Paris, they are selected. If they send one to London, they are selected.