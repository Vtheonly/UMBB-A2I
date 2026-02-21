
# 04 - WAN Links and Routing Protocols

## 📌 WAN Basics: Serial Connections
In the previous note, we used Ethernet cables (RJ45) to connect PCs to Routers. But to connect a Router to another Router over a long distance (like Campus Sud to Campus Nord), we often simulate a **Serial Link**.

### 🛠️ Hardware Setup (Packet Tracer)
Routers like the **2811** do not have Serial ports by default. You must add them:
1.  Click the Router > **Physical** tab.
2.  **Turn OFF** the router (click the power switch).
3.  Find the module **WIC-1T** or **WIC-2T** in the left list.
4.  Drag it into an empty slot on the router image.
5.  **Turn ON** the router.
6.  *Repeat for the second router.*

### 🔌 Cabling: DCE vs. DTE
When connecting two routers via Serial in a lab:
*   Use the **Red Serial Cable (with a clock icon)**.
*   One side is **DCE** (Data Circuit-terminating Equipment) - usually the ISP side.
*   The other is **DTE** (Data Terminal Equipment) - usually the Customer side.
*   **Crucial Rule:** The **DCE** side must set the `clock rate` (synchronization speed). Packet Tracer usually marks the DCE side with a small clock icon on the cable end.

### ⚙️ Configuring the Serial Interface
**Scenario:** Router0 (DCE) connects to Router1 (DTE).
**Network:** 10.10.10.0/30 (Use mask 255.255.255.252 for point-to-point).

**Router0 (DCE Side):**
```cisco
Router0(config)# interface serial 0/3/0
Router0(config-if)# ip address 10.10.10.1 255.255.255.252
Router0(config-if)# clock rate 64000     <-- ONLY ON DCE SIDE!
Router0(config-if)# bandwidth 2048       <-- Optional info for routing protocols
Router0(config-if)# no shutdown
```

**Router1 (DTE Side):**
```cisco
Router1(config)# interface serial 0/3/0
Router1(config-if)# ip address 10.10.10.2 255.255.255.252
Router1(config-if)# no shutdown
```

---

## 🗺️ Routing: How Routers "Learn"
By default, a router **only** knows about networks directly attached to its cables. It does NOT know about remote networks. We must teach it.

### Method 1: Static Routing (Manual)
You explicitly tell the router: *"To get to Network X, throw the packet to IP Y."*

**Syntax:** `ip route [Destination_Network] [Mask] [Next_Hop_IP]`

**Example (from TP3):**
*   **Router0** wants to reach **172.16.1.0** (which is behind Router1).
*   **Next Hop:** Router1's Serial IP (10.10.10.2).

```cisco
Router0(config)# ip route 172.16.1.0 255.255.255.0 10.10.10.2
```

**Pros:** Secure, low CPU usage.
**Cons:** If the link breaks, the router doesn't know. Tedious for big networks.

### Method 2: Dynamic Routing (RIP)
You tell the router: *"Here are the networks I own. Share this info with my neighbors."*

**Protocol:** RIP (Routing Information Protocol) v2.

**Router0 Configuration:**
```cisco
Router0(config)# router rip
Router0(config-router)# version 2
Router0(config-router)# network 192.168.1.0   <-- Advertise my LAN
Router0(config-router)# network 10.10.10.0    <-- Advertise the WAN link
Router0(config-router)# no auto-summary       <-- Good practice to prevent classful masking
```

**Router1 Configuration:**
```cisco
Router1(config)# router rip
Router1(config-router)# version 2
Router1(config-router)# network 172.16.1.0
Router1(config-router)# network 10.10.10.0
```

**Pros:** Automatic. If a link breaks, it finds a new path.
**Cons:** Uses bandwidth to send updates.

---

## 🔍 Verification
*   `show ip route`
    *   Look for **S** (Static route).
    *   Look for **R** (RIP route).
*   `ping` from PC in Network A to PC in Network B.