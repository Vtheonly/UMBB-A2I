
# 08 - Exercise Solution: TP3 Subnetting (VLSM)

## 📌 The Scenario (from TP3 PDF)
**Context:** We need to deploy an addressing plan for the Faculty of Sciences (5 Departments).
**Network Given:** `172.16.1.0` with Mask `255.255.255.0` (/24).
**Requirements:**
*   **Dept 5:** Needs 29 addresses (PCs + Servers).
*   **Dept 1, 2, 3, 4:** Need 25 addresses each.
*   **Router:** Needs 1 interface address per department (Gateway).

---

## 🧠 Step-by-Step Logic

### 1. Determine the Block Size
To subnet efficiently, we look at the **biggest** requirement first.
*   **Largest Dept (Dept 5):** 29 Hosts.
*   **Overhead:** We always need +1 for Network ID, +1 for Broadcast IP, and +1 for the Router Gateway.
*   **Total IP needed:** $29 + 3 = 32$.

**Math:**
Find the power of 2 that is $\ge 32$.
$$2^5 = 32$$
So, we need **5 host bits**.

### 2. Calculate the Mask
*   Current Mask: /24 (24 network bits).
*   Total bits in IPv4: 32.
*   **New Prefix (CIDR):** $32 - 5 \text{ (host bits)} = /27$.
*   **Subnet Mask:**
    *   /27 means $11111111.11111111.11111111.11100000$
    *   Binary `11100000` = $128 + 64 + 32 = 224$.
    *   **Final Mask:** `255.255.255.224`.

### 3. Assigning the Subnets
The "Magic Number" (Block Size) is **32**. We count by 32s.

| Department | Subnet ID (Network Address) | Host Range (Usable IPs) | Broadcast Address | Gateway IP (Last Usable) |
| :--- | :--- | :--- | :--- | :--- |
| **Dept 5** | **172.16.1.0** /27 | .1 to .30 | 172.16.1.31 | **172.16.1.30** |
| **Dept 1** | **172.16.1.32** /27 | .33 to .62 | 172.16.1.63 | **172.16.1.62** |
| **Dept 2** | **172.16.1.64** /27 | .65 to .94 | 172.16.1.95 | **172.16.1.94** |
| **Dept 3** | **172.16.1.96** /27 | .97 to .126 | 172.16.1.127 | **172.16.1.126** |
| **Dept 4** | **172.16.1.128** /27 | .129 to .158 | 172.16.1.159 | **172.16.1.158** |

> ⚠️ **Critical Exam Tip:** The PDF instructions say *"Passerelle devrait être la dernière adresse"* (Gateway should be the last address).
> Many students put `.1` as the gateway by habit. In this lab, for Dept 5, the gateway is `.30`, NOT `.1`.

---

## 🛠️ Packet Tracer Configuration (Dept 3 Example)

**For the PC (PC5 in Dept 3):**
*   **IP Address:** `172.16.1.65` (First usable IP in Dept 3 range)
*   **Subnet Mask:** `255.255.255.224` (Crucial! Do not use .0)
*   **Default Gateway:** `172.16.1.94` (The router IP calculated above)

**For the Router Interface (connected to Dept 3):**
```cisco
Router> enable
Router# config t
Router(config)# interface fastEthernet 0/2   <-- Verify port number in your topology
Router(config-if)# ip address 172.16.1.94 255.255.255.224
Router(config-if)# no shutdown
```

---

## ❓ Common Mistakes to Avoid
1.  **Overlapping Subnets:** If you try to assign `172.16.1.35` to Dept 1 and `172.16.1.35` to Dept 2, the Router will reject it saying "Overlap".
2.  **Wrong Gateway on PC:** If PC5 has Gateway `172.16.1.1` (which belongs to Dept 5), it will never reach the internet because it is looking for a router that isn't in its room.

