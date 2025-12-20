# 03 - Router Configuration & Gateways

## 📌 Concept: Why do we need Routers?

- **Switch:** Connects devices in the **same** network (e.g., 192.168.1.x).
- **Router:** Connects **different** networks (e.g., 192.168.1.x connects to 172.16.1.x).
- **Gateway:** The interface of the Router that faces your PC. It is the "door" out of your local room.

### The Default Gateway Rule

> 🛑 **CRITICAL REMINDER:** If a PC wants to talk to a different network (Internet), it **MUST** have the "Default Gateway" IP configured. This IP must match the Router's interface IP.

---

## 🛠️ Configuring Router Interfaces

Routers(1841) are "turned off" by default. You must enable the ports and give them IP addresses.

**Topology Example (from TP02):**

- **Network 1:** 192.168.1.0/24 (Left Side)
- **Network 2:** 172.16.1.0/24 (Right Side)
- **Router:** Center

### Step-by-Step Configuration

1.  **Access Router CLI** (Click Router > CLI > type 'no' to wizard).
2.  **Global Config:** `enable` -> `config t`.

#### Configure Left Interface (FastEthernet 0/0)

This acts as the Gateway for the 192.168.1.0 network.

```cisco
Router(config)# interface fastEthernet 0/0
Router(config-if)# ip address 192.168.1.100 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

> **Explanation:**
>
> - `ip address [IP] [MASK]`: Assigns the logical address.
> - `no shutdown`: Crucial! Router ports are "down" (Red) by default. This commands turns them "up" (Green).

#### Configure Right Interface (FastEthernet 0/1)

This acts as the Gateway for the 172.16.1.0 network.

```cisco
Router(config)# interface fastEthernet 0/1
Router(config-if)# ip address 172.16.1.100 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

---

## 🔌 Telnet Configuration (Remote Access)

Using a Console cable is annoying because you have to be physically next to the router. **Telnet** allows you to manage the router via the network (Virtual Teletype - VTY).

**Requirement:** The router must have an IP address and be reachable.

```cisco
Router(config)# line vty 0 4
Router(config-line)# password cisco
Router(config-line)# login
Router(config-line)# exit
```

- `line vty 0 4`: Configures 5 simultaneous connections (lines 0, 1, 2, 3, 4).
- **Security Note:** Telnet sends passwords in plain text. (SSH is better, but Telnet is used in this TP).

---

## 🧪 Verification & Troubleshooting

1.  **Check IPs:** `show ip interface brief`
    - Look for "Status: UP" and "Protocol: UP".
    - If "Admin Down": You forgot `no shutdown`.
    - If "Down/Down": Cable is disconnected.
2.  **Check Routing Table:** `show ip route`
    - Codes: `C` = Connected. You should see both networks listed.
3.  **PC Config:**
    - **PC0 (Left):** IP: 192.168.1.2 | Gateway: **192.168.1.100** (Router IP)
    - **PC1 (Right):** IP: 172.16.1.2 | Gateway: **172.16.1.100** (Router IP)
4.  **Ping:**
    - PC0 ping 192.168.1.100 (Gateway) -> Should work.
    - PC0 ping 172.16.1.100 (Remote Gateway) -> Should work.
    - PC0 ping 172.16.1.2 (Remote PC) -> Should work.

> 💡 **Trace Route:** Use `tracert 172.16.1.2` on the PC. It will show the path.
>
> 1. Hop 1: 192.168.1.100 (The Router)
> 2. Hop 2: 172.16.1.2 (The Destination)
