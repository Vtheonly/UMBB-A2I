
# 05 - Network Services: DHCP & NAT

## 📦 Service 1: DHCP (Dynamic Host Configuration Protocol)
Instead of manually typing IPs on every PC, the Router can assign them automatically.

### Configuration (Router0)
**Goal:** Assign IPs from 192.168.1.0/24, excluding the first 10 addresses.

1.  **Exclude Addresses** (Reserved for servers/routers):
    ```cisco
    Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
    ```
2.  **Create the Pool:**
    ```cisco
    Router(config)# ip dhcp pool LAN_POOL
    Router(dhcp-config)# network 192.168.1.0 255.255.255.0
    Router(dhcp-config)# default-router 192.168.1.1       <-- The Gateway
    Router(dhcp-config)# dns-server 8.8.8.8
    Router(dhcp-config)# exit
    ```
3.  **On the PC:**
    *   Go to Desktop > IP Configuration.
    *   Click **DHCP**.
    *   Wait for "DHCP Request Successful."

---

## 🌍 Service 2: NAT (Network Address Translation)
Private IPs (192.168.x.x) cannot be used on the Internet. **NAT** translates them to a Public IP provided by the ISP.

### Terminology (from TP4)
*   **Inside Local:** Your private PC IP (192.168.1.5).
*   **Inside Global:** The Public IP the world sees (200.1.1.1).
*   **Outside Interface:** The Serial port connected to ISP.
*   **Inside Interface:** The Ethernet port connected to LAN.

### Type A: NAT Dynamic (Pool) - "The Company Connection"
Allowing multiple employees to browse the web using a group of public IPs.

1.  **Define Interfaces:**
    ```cisco
    Router(config)# int fa0/0
    Router(config-if)# ip nat inside
    Router(config)# int s0/0/0
    Router(config-if)# ip nat outside
    ```
2.  **Create Access List (Who is allowed?):**
    ```cisco
    Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
    ```
3.  **Create Pool of Public IPs (Given by ISP):**
    ```cisco
    Router(config)# ip nat pool PUBLIC_POOL 206.150.15.1 206.150.15.5 netmask 255.255.255.248
    ```
4.  **Bind them together:**
    ```cisco
    Router(config)# ip nat inside source list 1 pool PUBLIC_POOL
    ```

### Type B: Static NAT - "The Web Server"
We want the Web Server (172.16.100.5) to always have a fixed Public IP (206.150.15.6) so people outside can find it.

```cisco
Router(config)# ip nat inside source static 172.16.100.5 206.150.15.6
```

### 🔍 Verification
*   `show ip nat translations`: Shows the table linking Private IPs <-> Public IPs.
*   Ping from the PC to the ISP Router (simulating the internet).
