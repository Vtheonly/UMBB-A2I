
### Exercise 11: Cars from Local Suppliers

**Source:** TD N° 1 BDA : Rappel SQL - Question 11
**Question:** "Quels sont les numéros des voitures dont les fournisseurs habitent la ville où est situé le revendeur auquel ces voitures sont destinées ?" (Which car numbers are supplied by suppliers who live in the same city as the dealer receiving the car?)

#### 1. Solution
```sql
SELECT DISTINCT FVR.NV
FROM FVR
JOIN FOURN F ON FVR.NF = F.NF
JOIN REVEND R ON FVR.NR = R.NR
WHERE F.VilleF = R.VilleR;
```

#### 2. Reasoning
This query requires comparing attributes from two different entities (`FOURN` and `REVEND`) that are linked by a transaction (`FVR`). We need to check if `Supplier.City` equals `Dealer.City`.

#### 3. Detailed Explanation
*   **Data Path**:
    1.  Start with the transaction table `FVR`.
    2.  Join `FOURN` to get the supplier's city (`VilleF`).
    3.  Join `REVEND` to get the dealer's city (`VilleR`).
*   **Condition**: The `WHERE` clause `F.VilleF = R.VilleR` enforces the "local supply" constraint.
*   **`DISTINCT`**: A specific car model (e.g., 'V1') might be supplied locally in Paris (F1->R1) and non-locally in London (F4->R5). If it is supplied locally at least once, it appears in the result. `DISTINCT` prevents duplicate car numbers if multiple local transactions occur for the same car type.

---

### Exercise 12: Dealers with Non-Local Suppliers

**Source:** TD N° 1 BDA : Rappel SQL - Question 12
**Question:** "Donnez les numéros des revendeurs dont un fournisseur au moins n’habite pas la ville où est situé ce revendeur." (Give the numbers of dealers who have at least one supplier not living in the dealer's city.)

#### 1. Solution
```sql
SELECT DISTINCT FVR.NR
FROM FVR
JOIN FOURN F ON FVR.NF = F.NF
JOIN REVEND R ON FVR.NR = R.NR
WHERE F.VilleF <> R.VilleR;
```

#### 2. Reasoning
This is the inverse logic of the previous exercise, but focused on dealers (`NR`) instead of cars (`NV`). We look for the existence of *any* transaction where the cities do not match.

#### 3. Detailed Explanation
*   **Inequality Operator**: The symbol `<>` (or `!=` in some SQL dialects) checks for inequality.
*   **Logic**:
    *   If Dealer R1 is in Paris.
    *   Supplier F1 is in London.
    *   Transaction F1 -> R1 exists.
    *   Since 'Paris' <> 'London', R1 is selected.
*   **Note**: A dealer might have 10 local suppliers and 1 non-local supplier. They will still be selected because the question asks for "at least one".

---

### Exercise 13: Dealers with No Red Cars from London Suppliers

**Source:** TD N° 1 BDA : Rappel SQL - Question 13
**Question:** "Quels sont les numéros des revendeurs pour lesquels aucune voiture rouge n’est fournie par un fournisseur habitant Londres ?" (Which dealer numbers have NO red cars supplied by a supplier living in London?)

#### 1. Solution
```sql
SELECT NR 
FROM REVEND
EXCEPT -- (or MINUS in Oracle)
SELECT FVR.NR
FROM FVR
JOIN FOURN F ON FVR.NF = F.NF
JOIN VOITURE V ON FVR.NV = V.NV
WHERE F.VilleF = 'LONDRES' 
  AND V.Couleur = 'ROUGE';
```
*Alternative using `NOT IN`:*
```sql
SELECT NR 
FROM REVEND
WHERE NR NOT IN (
    SELECT FVR.NR
    FROM FVR
    JOIN FOURN F ON FVR.NF = F.NF
    JOIN VOITURE V ON FVR.NV = V.NV
    WHERE F.VilleF = 'LONDRES' 
      AND V.Couleur = 'ROUGE'
);
```

#### 2. Reasoning
This is a "exclusion" query.
1.  Identify the "Forbidden Set": Transactions involving a **Red Car** coming from a **London Supplier**.
2.  Subtract the dealers involved in that set from the list of all dealers.

#### 3. Detailed Explanation
*   **The Subquery (The "Bad" List)**:
    *   Joins `FVR`, `FOURN`, and `VOITURE`.
    *   Filters for `VilleF='LONDRES'` AND `Couleur='ROUGE'`.
    *   Returns the list of dealers who *did* receive such a car.
*   **The Outer Query**: `NOT IN` removes anyone found in the bad list. The remaining dealers either received red cars from non-London suppliers, or non-red cars from London, or nothing at all. All these cases satisfy the condition "No red car from London".

---

### Exercise 14: Suppliers Matching Paris Code but Not in Paris

**Source:** TD N° 1 BDA : Rappel SQL - Question 14
**Question:** "Quels sont les numéros des fournisseurs n’habitant pas Paris mais dont le code est égal à celui d’un fournisseur habitant Paris ?" (Which supplier numbers do not live in Paris but have a code equal to that of a supplier living in Paris?)

#### 1. Solution
```sql
SELECT F1.NF
FROM FOURN F1
WHERE F1.VilleF <> 'PARIS'
  AND F1.Code IN (
      SELECT F2.Code 
      FROM FOURN F2 
      WHERE F2.VilleF = 'PARIS'
  );
```

#### 2. Reasoning
We are comparing suppliers to other suppliers.
1.  Find the set of codes belonging to suppliers in Paris.
2.  Find suppliers *not* in Paris whose code belongs to that set.

#### 3. Detailed Explanation
*   **Subquery**: `SELECT Code FROM FOURN WHERE VilleF = 'PARIS'` extracts the target codes (e.g., 10, 20).
*   **Main Query**: Scans the `FOURN` table.
    *   Row 1: F4, London, Code 20.
    *   Check 1: Is City <> Paris? Yes (London).
    *   Check 2: Is Code (20) in the Paris-list? Yes.
    *   Result: Keep F4.

---

### Exercise 15: Cars Supplied to ALL London Dealers

**Source:** TD N° 1 BDA : Rappel SQL - Question 15
**Question:** "Donnez les numéros des voitures fournies chacune à tous les revendeurs de Londres." (Give the car numbers supplied to ALL dealers in London.)

#### 1. Solution
*(Another Relational Division problem)*

```sql
SELECT V.NV
FROM VOITURE V
WHERE NOT EXISTS (
    -- Find a dealer in London...
    SELECT R.NR
    FROM REVEND R
    WHERE R.VilleR = 'LONDRES'
    AND NOT EXISTS (
        -- ...who has NOT received this car.
        SELECT 1
        FROM FVR F
        WHERE F.NR = R.NR
          AND F.NV = V.NV
    )
);
```

#### 2. Reasoning
This is mathematically identical to Exercise 9, but the "subject" is different.
*   Exercise 9: Cars supplied to all London Dealers? (Wait, looking back at Ex 9, it was the same question. Let me double check the provided context).
*   *Correction*: Exercise 9 asked for "cars supplied *for* all dealers". Exercise 15 asks "cars supplied *to* all dealers". In French "pour" vs "à". In the context of this schema, they mean the exact same thing (Relational Division).
*   **Verification**: Let's look at the correction provided in the image for Question 15.
    *   Image snippet says: `select nv from fvr x where not exists (select * from revend where ville='LONDRES' and not exists (select * from fvr where nr=revend.nr and nv=x.nv));`
    *   This confirms it is indeed the exact same logic.

#### 3. Detailed Explanation
*   **Double Negation**: "Find cars where there is NO London dealer who does NOT have the car."
*   **Step 1**: `SELECT R.NR ... WHERE VilleR = 'LONDRES'` gets the list of target dealers (the denominator of the division).
*   **Step 2**: The inner `NOT EXISTS` checks the link.
*   **Step 3**: The outer `NOT EXISTS` confirms that the set of "missing links" is empty for that specific car.

---

### Exercises 16 & 17 (Bonus from the image)

Although you asked for batches of 5, the image provided (Screenshot 2/3 from TD1 correction) contains Questions 16 and 17. I will include them briefly here to complete the TD1 set before moving to TD2 in the next batch.

**Exercise 16:** "Dealers with identical stock to F1"
*   **Query**: Find dealers where their set of cars is exactly equal to the set of cars supplied by F1.
*   **Logic**: (Cars of R contains Cars of F1) AND (Cars of F1 contains Cars of R).

**Exercise 17:** "Dealers offering *only* cars available from F1"
*   **Query**: Find dealers where `NOT EXISTS` a car they sell that is `NOT IN` F1's catalog.
*   **Logic**: Set Inclusion (Cars of R $\subseteq$ Cars of F1).

*End of TD 1.*