
# 09 - Exercise Solution: TP4 NAT & DHCP

## 📌 The Scenario (TP4 Part 1 & 2)
We have an Enterprise Network (`192.168.1.0/24`) and a Web Server (`172.16.100.5`).
We need to:
1.  Give the Enterprise internet access (Dynamic NAT).
2.  Make the Web Server visible to the world (Static NAT).
3.  **ISP Pool:** `206.150.15.0/29`.

---

## 🔍 Understanding the ISP Pool /29
*   **Network:** 206.150.15.0
*   **Mask:** 255.255.255.248 (/29 = 5 usable IPs roughly).
*   **Usable Range:** .1, .2, .3, .4, .5, .6.
*   **Strategy:**
    *   Use `.1` to `.5` for the **Dynamic NAT** (Employees).
    *   Use `.6` for the **Static NAT** (Web Server).

---

## 🚀 Configuration Guide

### Phase 1: DHCP (Automating IPs)
*Why?* So PCs get IP/Mask/Gateway automatically.

```cisco
Router0(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
Router0(config)# ip dhcp excluded-address 192.168.1.250 192.168.1.254
Router0(config)# ip dhcp pool EMPLOYEES
Router0(dhcp-config)# network 192.168.1.0 255.255.255.0
Router0(dhcp-config)# default-router 192.168.1.254
Router0(dhcp-config)# dns-server 172.16.100.5
```

### Phase 2: Defining Interfaces (The "Doors")
You must tell the router which door is "Inside" the house and which is "Outside".

```cisco
! The door facing the LAN
Router0(config)# interface fa0/0
Router0(config-if)# ip nat inside

! The door facing the Server LAN
Router0(config)# interface fa0/1
Router0(config-if)# ip nat inside

! The door facing the ISP (Internet)
Router0(config)# interface serial 0/0/0
Router0(config-if)# ip nat outside
```

### Phase 3: Dynamic NAT (For Employees)
Allow standard PCs to share the public IPs (.1 to .5).

1.  **Create the Pool:**
    ```cisco
    Router0(config)# ip nat pool PUBLIC_POOL 206.150.15.1 206.150.15.5 netmask 255.255.255.248
    ```
2.  **Define who is allowed (ACL):**
    ```cisco
    Router0(config)# access-list 1 permit 192.168.1.0 0.0.0.255
    ```
3.  **Link them:**
    ```cisco
    Router0(config)# ip nat inside source list 1 pool PUBLIC_POOL
    ```

### Phase 4: Static NAT (For Web Server)
Map the private server IP permanently to the last public IP (.6).

```cisco
Router0(config)# ip nat inside source static 172.16.100.5 206.150.15.6
```

---

## ❓ Troubleshooting NAT
**Problem:** "I can ping the ISP from the PC, but the command `show ip nat translations` is empty."
**Reason:** The translation only happens *during* traffic.
**Solution:**
1.  Go to Simulation Mode.
2.  Send a ping from PC to ISP.
3.  Click the packet at the Router.
4.  Look at **Outbound PDU**.
    *   **SRC IP:** Should change from `192.168.1.x` -> `206.150.15.1`.
    *   If it doesn't change, check your `ip nat inside/outside` commands on the interfaces.

**Problem:** "The Server cannot be reached from the outside."
**Reason:** Routing issue. Does the ISP router know where `206.150.15.0` is?
**Solution:** Ensure the ISP router (Router1) has a route back to your router.