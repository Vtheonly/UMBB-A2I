

## Exercise 06: Subnet Mask Calculation

> **Problem:** For each given Network ID and required number of subnets (SR), find the correct subnet mask and the number of usable machines per subnet.

### 1. Solution According to the Notes

The note for `Exo(06)` presents the final answers in a table. It also shows a separate calculation for one case (`184.25.0.0` needing 37 SR), demonstrating the correct logic:
1.  **Find bits to borrow (n):** For 37 subnets, `n` must satisfy `2^n >= 37`. The note shows `n=6` (`2^6=64`).
2.  **Calculate Final Mask:** It starts with the default bits (16 for Class B) and adds the borrowed bits: `16 + 6 = 22`. This is a `/22` mask.
3.  **Convert to Decimal:** A `/22` mask is `255.255.252.0`, which is correctly calculated.
This logic is sound and can be applied to all items in the table.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
This exercise is the reverse of subnet identification. We are given the requirements and must design the subnet mask.
1.  **Determine Class:** Identify the class of the Network ID to find the default number of host bits.
2.  **Calculate Bits to Borrow (n):** Find the smallest integer `n` such that `2^n` is greater than or equal to the required number of subnets (SR).
3.  **Calculate the New Mask:** The new mask length will be `(default mask length) + n`.
4.  **Calculate Hosts per Subnet:** Find the remaining host bits `h = (default host bits) - n`. The number of usable hosts is `2^h - 2`.

#### Step-by-Step Analysis

| NetID | Required SR | Class / Default Host Bits | Bits to Borrow (n) `(2^n ≥ SR)` | New Mask Length | Final Mask (Decimal) | Machines/SR `(h = def - n)`, `(2^h - 2)` |
|:--- |:---|:--- |:--- |:--- |:---|:---|
| `148.25.0.0` | 37 | **B** / 16 | `2^6=64` -> **n=6** | `/16 + 6 = /22` | `255.255.252.0` | `h=10`, `1022` |
| `198.63.24.0`| 2 | **C** / 8 | `2^1=2` -> **n=1** | `/24 + 1 = /25` | `255.255.255.128`| `h=7`, `126` |
| `110.0.0.0` | 1000 | **A** / 24 | `2^10=1024` -> **n=10**| `/8 + 10 = /18` | `255.255.192.0` | `h=14`, `16382` |
| `175.23.0.0` | 550 | **B** / 16 | `2^10=1024` -> **n=10**| `/16 + 10 = /26` | `255.255.255.192`| `h=6`, `62` |
| `209.206.202.0`| 60 | **C** / 8 | `2^6=64` -> **n=6** | `/24 + 6 = /30` | `255.255.255.252`| `h=2`, `2` |

---
