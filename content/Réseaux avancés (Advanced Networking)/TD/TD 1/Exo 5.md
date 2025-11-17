


## Exercise 05: Subnet Identification

> **Problem:** A machine M has IP `184.65.94.20`.
> 1.  What is its class and default network address?
> 2.  If the network uses the mask `255.255.240.0`, how many subnets and hosts per subnet are possible?
> 3.  What is the address of the subnet hosting M?
> 4.  Which other machines belong to the same subnet?

### 1. Solution According to the Notes

The notes for `Exo(05)` are spread across two pages and are very thorough.
1.  **Class & Network:** Correctly identifies the address as **Class B** and the default network as `184.65.0.0`.
2.  **Subnets/Hosts:** The mask `255.255.240.0` is analyzed. The third octet `240` (`11110000`) shows **4 bits** have been borrowed. This leads to the correct calculation of `2^4 = 16` subnets and `2^12 - 2 = 4094` hosts.
3.  **Subnet of M:** The note performs the bitwise AND operation on the third octet: `94 AND 240`. The binary calculation `01011110 AND 11110000 = 01010000` is shown, which correctly yields `80`. The subnet address is `184.65.80.0`.
4.  **Other Machines:** The notes correctly perform the AND operation for the other machines and identify `M3`, `M5`, and `M6` as belonging to the same subnet.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
**Subnetting** divides a single large network into smaller logical networks (subnets). A **subnet mask** defines which part of the IP is the network/subnet and which is the host. To find the subnet a host belongs to, you perform a **bitwise AND** operation between the IP address and the subnet mask.

#### Step-by-Step Analysis

**1. Class and Default Network:**
-   IP Address: `184.65.94.20`.
-   The first octet (`184`) is in the Class B range (128-191).
-   **Class: B**.
-   The default network part for Class B is the first two octets.
-   **Default Network Address: `184.65.0.0`**.

**2. Calculating Subnets and Hosts with Custom Mask:**
-   Default Class B mask: `/16` or `255.255.0.0`. This leaves `32 - 16 = 16` bits for hosts.
-   Custom Subnet Mask: `255.255.240.0`. Let's convert this to binary:
    `11111111.11111111.11110000.00000000`
-   This mask has `8 + 8 + 4 = 20` ones. It is a `/20` mask.
-   **Bits Borrowed (n):** `n = (Custom mask bits) - (Default mask bits) = 20 - 16 = 4` bits.
-   **Number of Subnets:** `2^n = 2^4 = **16 subnets**`.
-   **Host Bits Remaining (h):** `h = (Total bits) - (Custom mask bits) = 32 - 20 = 12` bits.
-   **Usable Hosts per Subnet:** `2^h - 2 = 2^12 - 2 = 4096 - 2 = **4094 hosts**`.

**3. Subnet Address of Machine M:**
-   We perform `184.65.94.20 AND 255.255.240.0`. The only challenging part is the third octet.
-   `94` (decimal) = `01011110` (binary)
-   `240` (decimal) = `11110000` (binary)
-   Performing the AND:
    ```
      01011110
    & 11110000
    -----------
      01010000  -> This is 64 + 16 = 80 (decimal)
    ```
-   The resulting IP is `184.65.80.0`.
-   **Subnet Address for M: `184.65.80.0`**.

**4. Identifying Machines on the Same Subnet:**
A machine is on the same subnet if its IP `AND` the subnet mask also results in `184.65.80.0`. We only need to test the third octet.
-   M3 (`184.65.90.1`): `90 & 240 = 80`. **Match.**
-   M5 (`184.65.87.1`): `87 & 240 = 80`. **Match.**
-   M6 (`184.65.94.1`): `94 & 240 = 80`. **Match.**

#### Final Answer
The machines belonging to the same subnet as M (`184.65.80.0`) are **M3, M5, and M6**.

---
*(This detailed, structured approach will be continued for all remaining exercises to provide a complete and easy-to-understand reference.)*

---