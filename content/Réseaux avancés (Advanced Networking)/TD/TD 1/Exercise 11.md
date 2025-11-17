## Exercise 11: IP Fragmentation

> [!Note] An IP datagram of 3820 bytes (20-byte header, 3800 bytes data) must cross a network with an MTU of 1500 bytes. Describe the resulting fragments.

### 1. Solution According to the Notes

The note for `Exo(11)` is a perfect, concise solution.

1.  **Max Data per Fragment:** Correctly calculated as `MTU - Header Length = 1500 - 20 = 1480 bytes`.
2.  **Number of Fragments:** `3800 / 1480` is calculated as `2.56...`, correctly leading to the conclusion that **3 fragments** are needed.
3.  **Fragment Details:**
    - A clear diagram shows F1 and F2 with 1480B of data and F3 with the remainder (`3800 - (1480*2) = 860B`). _Correction: the note says 840B for F3, which is 3800-2960. My initial math was slightly off. The note is correct!_
    - **Offset:** The note correctly calculates the offsets in 8-byte blocks:
      - F1: `offset = 0`
      - F2: `offset = 1480 / 8 = 185`
      - F3: `offset = (1480+1480) / 8 = 2960 / 8 = 370`
    - **MF Flag:** The note correctly sets `MF=1` for F1 and F2, and `MF=0` for F3, indicating it's the last fragment.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge

- **MTU (Maximum Transmission Unit):** The largest packet size (in bytes) that a specific network medium can carry. For standard Ethernet, this is 1500 bytes.
- **Fragmentation:** If a router receives an IP packet larger than the MTU of the outgoing link, it must break it into smaller pieces (fragments).
- **Fragmentation Fields in IP Header:**
  - **Identification:** All fragments of the same original packet share the same ID.
  - **MF (More Fragments) Flag:** A bit that is set to `1` for all fragments except the last one.
  - **Fragment Offset:** A field that indicates where in the original datagram's payload this fragment belongs. This value is not in bytes, but in **8-byte blocks**. Therefore, the data payload of every fragment (except the last) must be a multiple of 8.

#### Step-by-Step Analysis

1.  **Determine Maximum Payload per Fragment:**
    - MTU = 1500 bytes.
    - Each fragment will have its own 20-byte IP header.
    - Max data payload = `MTU - IP Header Size = 1500 - 20 = 1480 bytes`.
    - Check if 1480 is a multiple of 8: `1480 / 8 = 185`. Yes, it is. This is our maximum data size for the first fragments.

2.  **Calculate Fragment Sizes and Payloads:**
    - Total data to transmit = 3800 bytes.
    - **Fragment 1:** Will carry the maximum possible data: **1480 bytes**.
      - Remaining data: `3800 - 1480 = 2320 bytes`.
    - **Fragment 2:** Will also carry the maximum: **1480 bytes**.
      - Remaining data: `2320 - 1480 = 840 bytes`.
    - **Fragment 3:** Will carry all the remaining data: **840 bytes**.

3.  **Detail Each Fragment's Header Information:**

| Fragment   | Total Size | Header Size | Data Size | Data Bytes  | Offset (in 8-byte blocks) | MF Flag                  |
| :--------- | :--------- | :---------- | :-------- | :---------- | :------------------------ | :----------------------- |
| **Frag 1** | 1500 B     | 20 B        | 1480 B    | 0 - 1479    | `0 / 8 = 0`               | **1** (More follow)      |
| **Frag 2** | 1500 B     | 20 B        | 1480 B    | 1480 - 2959 | `1480 / 8 = 185`          | **1** (More follow)      |
| **Frag 3** | 860 B      | 20 B        | 840 B     | 2960 - 3799 | `2960 / 8 = 370`          | **0** (This is the last) |

#### Final Answer

The 3820-byte datagram will be split into **3 fragments**:

- **Fragment 1:** 1500 bytes total, carrying 1480 bytes of data, with Offset=0 and MF=1.
- **Fragment 2:** 1500 bytes total, carrying 1480 bytes of data, with Offset=185 and MF=1.
- **Fragment 3:** 860 bytes total, carrying the final 840 bytes of data, with Offset=370 and MF=0.
