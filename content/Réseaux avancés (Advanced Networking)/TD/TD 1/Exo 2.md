
## Exercise 02: Ethernet Frame Analysis

> **Problem:** Analyze the given Ethernet frame data (preamble/FCS removed) to identify its main components and determine the type of the destination MAC address.
> **Frame Data:** `ffff ffff ffff 09ab 14d8 0548 0806 0001 ...`

### 1. Solution According to the Notes

Your notes show a diagram of an Ethernet frame, correctly laying out the fields: `Destination @Mac`, `Source @Mac`, `Type`, and `Donnée (Data)`. The analysis then correctly applies this structure to the given hex string:
-   **Destination:** `ffff ffff ffff`
-   **Source:** `09ab 14d8 0548`
-   **Type:** `0806`, which is correctly identified as the protocol for **ARP**.
-   **Data:** The rest of the payload.

The notes then conclude that the destination MAC type is **Broadcast**. This is entirely correct.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge
An **Ethernet II frame** is the standard container for sending data over a local Ethernet network. Its structure is as follows:

```mermaid
graph LR
    A[Destination MAC<br>6 bytes] --> B[Source MAC<br>6 bytes];
    B --> C[EtherType<br>2 bytes];
    C --> D[Payload (Data)<br>46-1500 bytes];
```
-   **Destination MAC Address:** The Layer 2 address of the intended recipient(s).
-   **Source MAC Address:** The Layer 2 address of the sender.
-   **EtherType:** A two-byte code that tells the receiving device what kind of protocol is inside the payload (e.g., IPv4, ARP, IPv6). This allows the network stack to hand the data to the correct process.
-   **Payload:** The actual data being transported, typically an IP packet or, in this case, an ARP message.

#### Step-by-Step Analysis

We will dissect the hexadecimal string according to the frame structure.

1.  **Destination MAC Address (First 6 bytes):**
    -   Hex: `ffff ffff ffff`
    -   Formatted Address: **`FF:FF:FF:FF:FF:FF`**
    -   This is a special, reserved MAC address.

2.  **Source MAC Address (Next 6 bytes):**
    -   Hex: `09ab 14d8 0548`
    -   Formatted Address: **`09:AB:14:D8:05:48`**

3.  **EtherType (Next 2 bytes):**
    -   Hex: `0806`
    -   The value `0x0806` is the standardized identifier for **ARP (Address Resolution Protocol)**. ARP is used by a device to ask "Who on this network has IP address X? Please tell me your MAC address."

4.  **Data/Payload (Remaining bytes):**
    -   The rest of the string is the payload. Since the EtherType is ARP, this payload contains a structured ARP request message.

#### Final Answer

-   **Destination MAC:** `FF:FF:FF:FF:FF:FF`. The type of this address is **Broadcast**. A broadcast frame is sent to every single device on the local network segment. This makes sense for an ARP request, as the sender is shouting its question to everyone.
-   **Source MAC:** `09:AB:14:D8:05:48`
-   **Protocol Type:** ARP (`0x0806`)

---