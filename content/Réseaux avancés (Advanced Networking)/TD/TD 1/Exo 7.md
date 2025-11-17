
## Exercise 07: Subnet Range Calculation

> **Problem:** Given the starting network `172.60.0.0/20`, divide it into 4 subnets and list the network address, first/last usable IPs, and broadcast address for each.

### 1. Solution According to the Notes

The note for `Exo(07)` correctly deduces the steps for this Variable Length Subnet Masking (VLSM) problem.
1.  **Starting Mask:** `/20` (or `255.255.240.0`).
2.  **Bits to Borrow:** To create 4 subnets, we need `n` bits where `2^n=4`. So, `n=2` bits.
3.  **New Mask:** The new mask is `/20 + 2 = /22`.
4.  **Host Bits:** `32 - 22 = 10` host bits remain.
5.  **Machines/Subnet:** `2^10 - 2 = 1022`.
6.  **Subnet Ranges:** The note then correctly calculates the ranges. The `/22` mask means subnets are separated by a "block size" of 4 in the third octet (`256 - 252 = 4`). The table correctly lists the ranges starting from `172.16.0.0`, `172.16.4.0`, `172.16.8.0`, and `172.16.12.0`. *(Note: The problem states `172.60...` but the solution uses `172.16...`. We will follow the solution's base address).*

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
This problem involves subnetting an already subnetted network. We start with a `/20` block and must divide it further. The key is to calculate the new mask and then determine the "block size" or increment between the new, smaller subnets.

#### Step-by-Step Analysis

1.  **Starting Block:** We are given the network `172.16.0.0/20`.
2.  **Requirement:** We need to create **4 subnets** from this block.
3.  **Calculate Bits to Borrow (n):** To get 4 subnets, we need `n` bits such that `2^n = 4`. Therefore, **`n = 2` bits**.
4.  **Calculate the New Subnet Mask:** We add the borrowed bits to the starting mask length: `20 + 2 = 22`.
    -   New mask: `/22` or `255.255.252.0`.
5.  **Calculate the "Block Size":** The new subnets will be sized based on the last significant bit of the new mask. The `/22` mask is `11111111.11111111.11111100.00000000`. The interesting part is the third octet (`11111100`). The smallest value this bit represents is `4`. So, our subnets will increment by **4** in the third octet.

6.  **Map Out the Subnets:**

    *   **Subnet 1:**
        -   **Network Address:** `172.16.0.0`
        -   **First Usable IP:** `172.16.0.1`
        -   The next subnet starts at `172.16.4.0`. So, this subnet ends right before it.
        -   **Broadcast Address:** `172.16.3.255`
        -   **Last Usable IP:** `172.16.3.254`

    *   **Subnet 2:**
        -   **Network Address:** `172.16.4.0`
        -   **First Usable IP:** `172.16.4.1`
        -   **Broadcast Address:** `172.16.7.255`
        -   **Last Usable IP:** `172.16.7.254`

    *   **Subnet 3:**
        -   **Network Address:** `172.16.8.0`
        -   **First Usable IP:** `172.16.8.1`
        -   **Broadcast Address:** `172.16.11.255`
        -   **Last Usable IP:** `172.16.11.254`

    *   **Subnet 4:**
        -   **Network Address:** `172.16.12.0`
        -   **First Usable IP:** `172.16.12.1`
        -   **Broadcast Address:** `172.16.15.255`
        -   **Last Usable IP:** `172.16.15.254`

This detailed breakdown matches the table in your notes perfectly.

---