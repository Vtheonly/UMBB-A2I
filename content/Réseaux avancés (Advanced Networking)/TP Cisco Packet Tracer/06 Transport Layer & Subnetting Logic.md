


## 📦 TP05: TCP Protocol Analysis
TCP (Transmission Control Protocol) is connection-oriented. It makes sure data arrives correctly.

### The 3-Way Handshake
Before sending data (like a Telnet command), TCP establishes a connection.
1.  **SYN (Synchronize):** PC sends to Server. "Let's talk. My sequence number is X."
2.  **SYN-ACK:** Server sends to PC. "Okay. I acknowledge X. My sequence number is Y."
3.  **ACK:** PC sends to Server. "I acknowledge Y. Connection open."

### Lab: Wireshark / Packet Tracer Simulation
1.  Connect two PCs.
2.  Start **Simulation Mode**.
3.  Edit Filters: Show only **TCP** (uncheck everything else).
4.  On PC1, Telnet to PC2.
5.  Watch the colored boxes (PDUs).
    *   **First Packet:** Look at "Outbound PDU Details". The flag **SYN** is set to 1.
    *   **Second Packet:** The flag **SYN** and **ACK** are set to 1.
    *   **Third Packet:** The flag **ACK** is set to 1.

> **Why Telnet?** We use Telnet in the lab because it uses TCP port 23, making it easy to generate this specific traffic.

---

## ➗ TP03 Part I: Subnetting Workshop
**The Task:** You have network `172.16.0.0/16`. You need 5 subnets (Departments).
*   Dept 1-4: 25 hosts.
*   Dept 5: 29 hosts.

### The Calculation Logic (VLSM)
We need to fit the largest department first (29 hosts).
Formula: **2^n - 2 >= Hosts**.
*   We need 29 hosts.
*   2^5 = 32. 32 - 2 = 30. This is enough.
*   So we need **5 host bits**.
*   New CIDR: /32 - 5 = **/27**.
*   Subnet Mask: 255.255.255.224.

### The Plan
1.  **Subnet 1:** 172.16.1.0 /27
    *   Range: .1 to .30
    *   Broadcast: .31
2.  **Subnet 2:** 172.16.1.32 /27
    *   Range: .33 to .62
    *   Broadcast: .63
3.  **Subnet 3:** 172.16.1.64 /27
    *   Range: .65 to .94
    *   Broadcast: .95
*(And so on for Dept 4 and 5)*.

### 🧪 Implementing in Packet Tracer
When assigning IPs to PCs in Dept 3:
*   **IP:** 172.16.1.65 (First usable)
*   **Mask:** 255.255.255.224 (NOT .0)
*   **Gateway:** 172.16.1.94 (Last usable - typically assigned to the Router interface).
