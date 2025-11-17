
## Exercise 04: FLSM, Aggregation, and VLSM Redesign

> **Problem:**
> An enterprise is given `172.17.0.0/19`.
> 1.  Divide the network into 5 equal-sized subnets. What is the new mask?
> 2.  For IPs `172.17.6.210`, `172.17.18.1`, etc., find their subnet addresses.
> 3.  Aggregate the last two *unassigned* subnets from the FLSM plan.
> 4.  Use the aggregated block from step 3 to create a new VLSM plan for 5 new subnets (A-E) with new requirements.

### 1. Solution According to the Notes

The notes for this multi-part problem are very insightful.

**Part 1 (FLSM):**
-   To get 5 subnets, the notes correctly determine we must borrow **3 bits** (`2^3 = 8` subnets, which is the smallest power of 2 >= 5).
-   The new mask is `/19 + 3 = /22`.
-   The `/22` mask gives a block size of 4 in the third octet. The notes then list the first 5 subnets: `172.17.0.0`, `172.17.4.0`, `172.17.8.0`, `172.17.12.0`, `172.17.16.0`.

**Part 3 (Aggregation):**
-   The notes correctly identify the full 8 subnets created by the `/22` mask. The last two are `172.17.28.0/22` and `172.17.24.0/22`.
-   The aggregation is shown in binary. The addresses `172.17.000110`00 and `172.17.000111`00 only differ in the 3rd borrowed bit. By removing this bit from the mask (going from `/22` to `/21`), they can be summarized.
-   The resulting aggregated address is correctly identified as **`172.17.24.0/21`**.

**Part 4 (New VLSM Plan):**
-   The new requirements (A:62, B:2, C:200, D:30, E:128) are ordered by size: C, E, A, D, B.
-   Using the `172.17.24.0/21` block, the notes create a perfect VLSM allocation plan, which is summarized in the final table.

### 2. Formal, Detailed Solution

#### Step 1: FLSM Decomposition
1.  **Starting Block:** `172.17.0.0/19`. A `/19` mask is `255.255.224.0`.
2.  **Requirement:** 5 equal-sized subnets.
3.  **Bits to Borrow:** We need `2^n >= 5`. The smallest `n` is **3 bits**. This will create `2^3 = 8` subnets in total.
4.  **New FLSM Mask:** `/19 + 3 = /22`. In decimal, this is `255.255.252.0`.
5.  **Subnet Ranges:** A `/22` mask has a block size of 4 in the 3rd octet. The first 5 subnets are:
    -   S1: `172.17.0.0/22`
    -   S2: `172.17.4.0/22`
    -   S3: `172.17.8.0/22`
    -   S4: `172.17.12.0/22`
    -   S5: `172.17.16.0/22`

#### Step 2: Identify Subnet for Given IPs
To find the subnet for an IP, we perform a bitwise AND with the `/22` mask (`255.255.252.0`).
-   `172.17.6.210`: `6 & 252 = 4`. Belongs to subnet **`172.17.4.0/22`**.
-   `172.17.18.1`: `18 & 252 = 16`. Belongs to subnet **`172.17.16.0/22`**.
-   `172.17.12.25`: `12 & 252 = 12`. Belongs to subnet **`172.17.12.0/22`**.

#### Step 3: Route Aggregation (Supernetting)
1.  **Identify Unused Subnets:** From our FLSM plan, we created 8 subnets. The last two are:
    -   S7: `172.17.24.0/22`
    -   S8: `172.17.28.0/22`
2.  **Analyze in Binary:** Let's look at the third octet. The `/19` mask ends at `172.17.000|xxxxx`. The `/22` mask uses 3 more bits: `172.17.000xx|xxx`.
    -   `24` is `00011000`. The subnet bits are `110`.
    -   `28` is `00011100`. The subnet bits are `111`.
    -   `172.17.000110|00...`
    -   `172.17.000111|00...`
3.  **Find the Common Prefix:** These two subnets share the common prefix `172.17.00011`. This prefix is 21 bits long (`16` from the first two octets + `5` from the third).
4.  **Resulting Aggregated Network:** The aggregated network address is **`172.17.24.0/21`**. This single route summary now covers the entire range from `172.17.24.0` to `172.17.31.255`.

#### Step 4: New VLSM Plan from Aggregated Block
1.  **Starting Block:** `172.17.24.0/21`.
2.  **New Requirements:**
    -   C: 200 hosts -> `2^8-2=254`. Needs `h=8` bits -> **/24 mask**.
    -   E: 128 hosts -> `2^8-2=254`. Needs `h=8` bits -> **/24 mask**.
    -   A: 62 hosts -> `2^6-2=62`. Needs `h=6` bits -> **/26 mask**.
    -   D: 30 hosts -> `2^5-2=30`. Needs `h=5` bits -> **/27 mask**.
    -   B: 2 hosts -> `2^2-2=2`. Needs `h=2` bits -> **/30 mask**.
3.  **Final VLSM Addressing Table:**

| Subnet | Hosts Req. | Mask | Network Address | Usable IP Range | Broadcast |
|:---:|:---:|:---:|:---|:---|:---|
| **C** | 200 | **/24** | `172.17.24.0` | `172.17.24.1 - 172.17.24.254` | `172.17.24.255` |
| **E** | 128 | **/24** | `172.17.25.0` | `172.17.25.1 - 172.17.25.254` | `172.17.25.255` |
| **A** | 62 | **/26** | `172.17.26.0` | `172.17.26.1 - 172.17.26.62` | `172.17.26.63` |
| **D** | 30 | **/27** | `172.17.26.64`| `172.17.26.65 - 172.17.26.94` | `172.17.26.95` |
| **B** | 2 | **/30** | `172.17.26.96`| `172.17.26.97 - 172.17.26.98` | `172.17.26.99` |

This detailed plan exactly matches the final table in your handwritten notes.

---
