## Exercise 09: Subnet Planning (VLSM)

> [!Note] A network `193.152.100.0` needs to be divided to support four groups (RL1-RL4) with the following host requirements:
>
> - RL1: 15 machines
> - RL2: 20 machines
> - RL3: 25 machines
> - RL4: 30 machines
>   Design a subnetting scheme.

### 1. Solution According to the Notes

The note for `Exo(09)` approaches this as a Variable Length Subnet Masking (VLSM) problem.

1.  **Subnet Bits:** It first calculates that 4 subnets require `2` bits (`2^2=4`).
2.  **Host Bits:** It then analyzes the host requirements for each group:
    - RL1 (15 machines): Needs `n` bits where `2^n - 2 >= 15`. `2^4-2=14` (too small), so `2^5-2=30`. Requires **5 host bits**.
    - RL2 (20 machines): Requires **5 host bits**.
    - RL3 (25 machines): Requires **5 host bits**.
    - RL4 (30 machines): Requires **5 host bits**.
3.  **Calculate Mask:** Since the largest requirement is 30 hosts (requiring 5 host bits), the note correctly determines that a single subnet mask can satisfy all groups.
    - The base network is Class C (`193...`), which has 8 default host bits.
    - If we leave 5 bits for hosts, we must borrow `8 - 5 = 3` bits for subnets.
    - The new mask length is `/24 + 3 = /27`.
    - A `/27` mask is `255.255.255.224`, which is the final answer in the notes.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge

**Variable Length Subnet Masking (VLSM)** is a technique for designing subnets that are sized appropriately for the number of hosts they need to support, which prevents wasting IP addresses. The general strategy is to tackle the largest host requirements first.

#### Step-by-Step Analysis

1.  **Analyze Host Requirements:** For each group, we need to find the minimum number of host bits (`h`) required to satisfy the need (`2^h - 2 >= hosts`).
    - RL4 (30 machines): `2^4-2=14` (not enough). `2^5-2=30`. We need **h=5 host bits**. This subnet provides 30 usable IPs.
    - RL3 (25 machines): `2^5-2=30`. Also needs **h=5 host bits**.
    - RL2 (20 machines): `2^5-2=30`. Also needs **h=5 host bits**.
    - RL1 (15 machines): `2^5-2=30`. Also needs **h=5 host bits**.

2.  **Design the Subnet Mask:**
    - Since all four groups have the same host bit requirement (h=5), we can use a single, fixed-size subnet mask for all of them. This is technically not VLSM, but a standard subnetting design.
    - The base network is `193.152.100.0`, a Class C with a default `/24` mask and 8 host bits.
    - To leave `h=5` bits for hosts, we must use `32 - 5 = 27` bits for the network/subnet mask.
    - The new mask is **`/27`**.
    - Let's convert `/27` to decimal:
      `11111111.11111111.11111111.11100000` -> `255.255.255.224`.

3.  **Map Out the Subnets:**
    - A `/27` mask has a block size of `256 - 224 = 32`. We can now assign a subnet to each group.
    - **Subnet for RL4:** `193.152.100.0/27` (Range: .1 to .30)
    - **Subnet for RL3:** `193.152.100.32/27` (Range: .33 to .62)
    - **Subnet for RL2:** `193.152.100.64/27` (Range: .65 to .94)
    - **Subnet for RL1:** `193.152.100.96/27` (Range: .97 to .126)

#### Final Answer

The most efficient subnet mask that can accommodate all four required groups is **`255.255.255.224`** (or `/27`). This creates subnets with 30 usable host addresses each, which satisfies all requirements.

---
