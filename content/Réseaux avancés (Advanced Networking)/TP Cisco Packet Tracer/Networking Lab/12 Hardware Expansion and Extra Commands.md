# 12 - Hardware Expansion & Extra Commands

## 🛠️ Hardware Modules (From TP3 Part I)

In **TP3 Part I**, you are asked to connect **5 Departments** to one central router.

- **The Problem:** A standard Router (like the 2811) only has **2** FastEthernet ports (Fa0/0 and Fa0/1). You need **5**.
- **The Solution:** You must buy and install extra Network Interface Cards (NICs).

### How to do this in Packet Tracer:

1.  Click the **Router (2811)**.
2.  Go to the **Physical** tab.
3.  **Turn OFF** the power switch (Green light goes off).
4.  Look for the module **NM-2FE2W** (2 FastEthernet + 2 WAN) or **WIC-1ENET** (1 Ethernet).
    - _Note:_ In newer Packet Tracer versions, you might use **HWIC-4ESW** (4 switching ports), but for a pure routing lab, try to find Ethernet interfaces.
5.  Drag the module into the empty big slot on the left.
6.  **Turn ON** the power.
7.  **Verify:** Go to CLI and type `show ip interface brief`. You should now see new interfaces (e.g., `FastEthernet 0/1/0`).

---

## 💻 The "Undo" Command (From TP02)

We talked about saving (`copy run start`), but TP02 also lists the command to **cancel** changes.

**Command:** `copy startup-config running-config`

- **What it does:** It overwrites your _current_ mistakes with the _last saved_ good configuration.
- **Use case:** You messed up the router config so badly you want to go back to how it was 10 minutes ago (assuming you saved 10 minutes ago).

---

## 🔍 Additional "Show" Commands (From TP02 Table)

TP02 lists a few specific information commands that are good for exams:

| Command          | Explanation                                                                                                                        |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `show version`   | Displays the hardware info, RAM amount, and the **IOS Image file name**. Useful if the teacher asks "What version of IOS is this?" |
| `show protocols` | Shows which protocols (like RIP, TCP/IP) are active and the IP addresses of interfaces. A quick summary.                           |
| `show history`   | (Not in PDF but useful) Shows the last 10 commands you typed.                                                                      |

---

## 🧪 TP5: Wireshark vs. Packet Tracer Simulation

**TP5** mentions "Lancer Wireshark".

- **In Real Life:** You install Wireshark on a PC, plug it into the switch, and capture traffic.
- **In Packet Tracer:** You cannot run real Wireshark. Instead, Packet Tracer has a built-in "Sniffer" device, but most students just use **Simulation Mode** (The Play/Stop button) which acts exactly like Wireshark.
  - _Exam Tip:_ If the question asks "Observe the Ethernet Frame content", use the **Simulation Mode**, click the colored envelope, and look at the **Inbound PDU Details**.
  