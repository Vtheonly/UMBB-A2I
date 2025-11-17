
## Exercise 01: FLSM vs. VLSM Efficiency

> **Problem:**
> Given the network `204.15.5.0/24`, design an addressing plan for 5 subnets (A, B, C, D, E) with the following host requirements:
> -   Subnet A: 14 equipment
> -   Subnet B: 28 equipment
> -   Subnet C: 2 equipment
> -   Subnet D: 7 equipment
> -   Subnet E: 28 equipment
> 1.  Propose a plan using **FLSM (Fixed Length Subnet Masking)**.
> 2.  Calculate the address utilization rate for each subnet in the FLSM plan.
> 3.  What can you conclude?
> 4.  Propose an optimal addressing plan using **VLSM (Variable Length Subnet Masking)**.

### 1. Solution According to the Notes

Your notes correctly identify the core logic for both FLSM and VLSM.

**For the FLSM plan:**
-   The largest requirement is for 28 hosts (Subnets B and E).
-   To satisfy 28 hosts, the calculation `2^h - 2 >= 28` is performed. This correctly yields `h=5` host bits (`2^5 - 2 = 30` hosts).
-   Since the base network is `/24` (8 host bits), `8 - 5 = 3` bits must be borrowed for subnets.
-   This leads to a new, fixed mask of `/24 + 3 = /27` for all subnets. The notes correctly identify this mask as `255.255.255.224`.

**For the VLSM plan:**
-   The notes correctly re-order the subnets by size, from largest to smallest: B(28), E(28), A(14), D(7), C(2).
-   For each subnet, the appropriately sized mask is calculated:
    -   B & E (28 hosts) need `h=5` bits -> **/27 mask**.
    -   A (14 hosts) needs `h=4` bits (`2^4-2=14`) -> **/28 mask**.
    -   D (7 hosts) needs `h=4` bits -> **/28 mask**.
    -   C (2 hosts, a point-to-point link) needs `h=2` bits (`2^2-2=2`) -> **/30 mask**.
-   The final addressing plan allocates these variable-sized blocks sequentially.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
-   **FLSM (Fixed Length Subnet Masking):** A traditional subnetting method where all subnets have the same size and the same number of available host addresses. The size is determined by the largest subnet's requirement, which often leads to significant address waste in smaller subnets.
-   **VLSM (Variable Length Subnet Masking):** A modern, efficient method where each subnet is sized precisely according to its specific host requirements. This minimizes wasted addresses. The key is to start allocating addresses for the largest subnets first.

#### Step 1: FLSM Plan
1.  **Identify the Largest Requirement:** Subnets B and E both need 28 hosts.
2.  **Calculate Required Host Bits (h):** We need `2^h - 2 >= 28`.
    -   If h=4, `2^4 - 2 = 14`. Not enough.
    -   If h=5, `2^5 - 2 = 30`. Sufficient. We need **5 host bits**.
3.  **Calculate the FLSM Subnet Mask:**
    -   The base network `204.15.5.0/24` has 8 host bits.
    -   To leave 5 bits for hosts, we must use `32 - 5 = 27` bits for the mask.
    -   The fixed mask for all subnets is **/27** (`255.255.255.224`).
4.  **Allocate the Subnets:** A `/27` mask has a block size of `256 - 224 = 32`.
    -   Subnet A: `204.15.5.0/27`
    -   Subnet B: `204.15.5.32/27`
    -   Subnet C: `204.15.5.64/27`
    -   Subnet D: `204.15.5.96/27`
    -   Subnet E: `204.15.5.128/27`

#### Step 2: Calculate FLSM Utilization
Each subnet is given 30 usable addresses.
-   **Subnet A (14 hosts):** `14 / 30 = 46.7%` utilization. (16 addresses wasted)
-   **Subnet B (28 hosts):** `28 / 30 = 93.3%` utilization. (2 addresses wasted)
-   **Subnet C (2 hosts):** `2 / 30 = 6.7%` utilization. (28 addresses wasted)
-   **Subnet D (7 hosts):** `7 / 30 = 23.3%` utilization. (23 addresses wasted)
-   **Subnet E (28 hosts):** `28 / 30 = 93.3%` utilization. (2 addresses wasted)

#### Step 3: Conclusion
The utilization rates are very low for subnets C and D. FLSM is simple but extremely wasteful, allocating far more addresses than needed for the smaller subnets.

#### Step 4: Optimal VLSM Plan
1.  **Order Subnets by Size:** Largest to smallest.
    -   Subnet B (28 hosts)
    -   Subnet E (28 hosts)
    -   Subnet A (14 hosts)
    -   Subnet D (7 hosts)
    -   Subnet C (2 hosts)
2.  **Calculate the Optimal Mask for Each:**
    -   **B & E (28 hosts):** Need `h=5` bits. Mask is **/27**. Block size is 32.
    -   **A (14 hosts):** Need `h=4` bits (`2^4-2=14`). Mask is **/28**. Block size is 16.
    -   **D (7 hosts):** Need `h=4` bits. Mask is **/28**. Block size is 16.
    -   **C (2 hosts):** Need `h=2` bits (`2^2-2=2`). Mask is **/30**. Block size is 4.
3.  **Allocate Addresses Sequentially:**

| Subnet | Hosts Req. | Mask | Network Address | Usable IP Range | Broadcast |
|:---:|:---:|:---:|:---|:---|:---|
| **B** | 28 | **/27** | `204.15.5.0` | `204.15.5.1 - 204.15.5.30` | `204.15.5.31` |
| **E** | 28 | **/27** | `204.15.5.32`| `204.15.5.33 - 204.15.5.62` | `204.15.5.63` |
| **A** | 14 | **/28** | `204.15.5.64`| `204.15.5.65 - 204.15.5.78` | `204.15.5.79` |
| **D** | 7 | **/28** | `204.15.5.80`| `204.15.5.81 - 204.15.5.94` | `204.15.5.95` |
| **C** | 2 | **/30** | `204.15.5.96`| `204.15.5.97 - 204.15.5.98` | `204.15.5.99` |

**Conclusion:** This VLSM plan is far more efficient. The next available address is `204.15.5.100`, leaving a large portion of the original `/24` block free for future use.

---
