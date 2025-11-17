

## Exercise 08: Network Connectivity and Gateway

> **Problem:**
> - User A: IP `143.27.102.101`, Mask `255.255.192.0`
> - User B: IP `143.27.172.101`, Mask `255.255.192.0`
> 1. Find the network and broadcast addresses for User A.
> 2. Are User A and User B on the same subnet?
> 3. Can User B use User A's default gateway (`143.27.105.1`)?

### 1. Solution According to the Notes

The notes for `Exo(08)` follow a very logical path.
1.  **User A's Subnet:** The mask `/18` (`255.255.192.0`) is identified. The note performs a bitwise AND on the third octet (`102 & 192 = 64`) to correctly find User A's subnet address: **`143.27.64.0/18`**. The broadcast address is correctly identified as `143.27.127.255`.
2.  **User B's Subnet:** The same AND operation is performed for User B (`172 & 192 = 128`), correctly finding User B's subnet: **`143.27.128.0/18`**.
3.  **Comparison:** Since `64.0` is not equal to `128.0`, the conclusion is that **they are not on the same subnet**.
4.  **Gateway Issue:** The note correctly states that since B is not on the same subnet as A, it cannot use A's gateway. The final remark is crucial: *"La passerelle doit être dans même SR que l'hôte qui l'utilise"* (The gateway must be in the same subnet as the host that uses it).

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
-   To determine if two devices can communicate directly on a LAN, they must be on the **same subnet**.
-   We find a device's subnet by performing a **bitwise AND** between its IP and its subnet mask.
-   A **Default Gateway** is a router interface that a host uses to send traffic to other networks. A host can only use a gateway that is on its own local subnet. A host cannot "jump" to a gateway on a different subnet.

#### Step-by-Step Analysis

**1. Analyze User A's Subnet:**
-   IP: `143.27.102.101`
-   Mask: `255.255.192.0` (which is `/18`)
-   We perform `143.27.102.101 AND 255.255.192.0`. The key is the third octet:
    -   `102` (decimal) = `01100110` (binary)
    -   `192` (decimal) = `11000000` (binary)
    -   `01100110 & 11000000 = 01000000` -> `64` (decimal)
-   **User A's Subnet Address: `143.27.64.0/18`**.
-   The `/18` mask gives a block size of 64 in the third octet. So the range is `143.27.64.0` to `143.27.127.255`.
-   **User A's Broadcast Address: `143.27.127.255`**.

**2. Analyze User B's Subnet and Compare:**
-   IP: `143.27.172.101`
-   Mask: `255.255.192.0` (`/18`)
-   Third octet calculation:
    -   `172` (decimal) = `10101100` (binary)
    -   `192` (decimal) = `11000000` (binary)
    -   `10101100 & 11000000 = 10000000` -> `128` (decimal)
-   **User B's Subnet Address: `143.27.128.0/18`**.
-   **Comparison:** `143.27.64.0` is not the same as `143.27.128.0`.
-   **Conclusion:** User A and User B are on **different subnets**.

**3. Analyze the Gateway:**
-   User A's Gateway: `143.27.105.1`. Let's check which subnet it's on using the same `/18` mask.
    -   Third octet: `105 & 192 = 64`.
    -   The gateway `143.27.105.1` is on subnet **`143.27.64.0/18`**, which is User A's subnet. This is a valid configuration for User A.
-   Can User B use it?
    -   User B is on subnet `143.27.128.0/18`.
    -   The gateway is on subnet `143.27.64.0/18`.
    -   Since the gateway is not on User B's local subnet, User B **cannot reach it directly** and therefore cannot use it as a default gateway.

#### Final Answer
1.  User A is on subnet `143.27.64.0/18` with broadcast `143.27.127.255`.
2.  No, they are on different subnets.
3.  No, User B cannot use User A's gateway because the gateway is not on User B's subnet.

---