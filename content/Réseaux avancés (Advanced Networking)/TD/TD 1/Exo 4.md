
## Exercise 04: Broadcast Communication

> **Problem:** Machine M1 with IP `192.175.60.3` wants to send a global message (broadcast) on its network. What is the destination IP address, and which listed machines will respond?

### 1. Solution According to the Notes

The note for `Exo(04)` is clear and correct:
1.  It identifies `192.175.60.3` as **Class C**.
2.  It deduces the network address as `192.175.60.0`.
3.  It calculates the broadcast address by setting the host part to all `1`s, resulting in **`192.175.60.255`**.
4.  It concludes that only machines on the same network (`192.175.60.0`) will respond, correctly listing `M2`, `M4`, and `M5`.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
A **broadcast** is a message sent to all devices on a specific network segment. To do this, a device sends a packet to the network's broadcast address. A device will only receive and process a broadcast if the broadcast address corresponds to the network it is currently on.

#### Step-by-Step Analysis

1.  **Identify the Sender's Network:**
    -   Sender's IP: `192.175.60.3`.
    -   The first octet (`192`) falls in the Class C range (192-223).
    -   In a Class C network, the first three octets define the network.
    -   Therefore, the network address is **`192.175.60.0`**.

2.  **Calculate the Broadcast Address:**
    -   The network part is `192.175.60`.
    -   The host part is the last octet. To create the broadcast address, we set all host bits to `1`.
    -   An octet of all `1`s (`11111111`) is `255` in decimal.
    -   The destination IP for the broadcast is **`192.175.60.255`**.

3.  **Identify Machines on the Same Network:**
    We must check which of the other machines have a network portion of `192.175.60`.
    -   M2 (`192.175.60.4`): Network is `192.175.60`. **Match.**
    -   M3 (`192.176.60.3`): Network is `192.176.60`. No match.
    -   M4 (`192.175.60.5`): Network is `192.175.60`. **Match.**
    -   M5 (`192.175.60.38`): Network is `192.175.60`. **Match.**

#### Final Answer
-   The broadcast destination address is **`192.175.60.255`**.
-   The machines that will receive and can respond to this broadcast are **M2, M4, and M5**.

---