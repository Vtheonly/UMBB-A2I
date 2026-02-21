
# 10 - Ultimate IOS Command Cheat Sheet

## 🔑 Mode Navigation & Saving

| Action                | Command                              | Context         |
| :-------------------- | :----------------------------------- | :-------------- |
| Enter Privileged Mode | `enable`                             | `Router>`       |
| Enter Global Config   | `config terminal`                    | `Router#`       |
| Go back one level     | `exit`                               | Any config mode |
| Go back to start      | `end` (or `Ctrl+Z`)                  | Any config mode |
| **SAVE CONFIG**       | `copy running-config startup-config` | `Router#`       |
| View Active Config    | `show running-config`                | `Router#`       |

---

## 🛠️ Interface Configuration (Routers)

_Replace `fa0/0` with your actual interface name._

| Action          | Command                                |
| :-------------- | :------------------------------------- |
| Enter Interface | `interface fastEthernet 0/0`           |
| Assign IP (LAN) | `ip address 192.168.1.1 255.255.255.0` |
| Turn On Port    | `no shutdown`                          |
| Add Description | `description Link_to_LAN_A`            |
| Check Status    | `do show ip interface brief`           |

**For Serial Interfaces (WAN):**

| Action | Command |
| :--- | :--- |
| Enter Interface | `interface serial 0/0/0` |
| Set Speed (DCE Side) | `clock rate 64000` |
| Set Bandwidth | `bandwidth 2048` |

---

## 🚦 Routing Protocols

**Static Routing:**
`ip route [Dest_Network] [Mask] [Next_Hop_IP]`
Example: `ip route 172.16.1.0 255.255.255.0 10.10.10.2`

**RIPv2 (Dynamic):**

```cisco
router rip
version 2
no auto-summary
network [Network_ID_1]
network [Network_ID_2]
```


---

## 🛡️ Security & Management

**Console Password:**

```cisco
line console 0
password [your_pass]
login
```

**Enable Password:**

```cisco
enable secret [your_pass]
```

**Telnet (VTY):**

```cisco
line vty 0 4
password [your_pass]
login
```

**Encrypt All Passwords:**
`service password-encryption`

---

## 🌍 NAT & DHCP (The Advanced Stuff)

**DHCP Server Setup:**

```cisco
ip dhcp excluded-address [Start_IP] [End_IP]
ip dhcp pool [POOL_NAME]
network [Net_ID] [Mask]
default-router [Gateway_IP]
dns-server [DNS_IP]
```

**NAT Configuration:**

1.  **Inside Interface:** `ip nat inside`
2.  **Outside Interface:** `ip nat outside`
3.  **Dynamic NAT:** `ip nat inside source list 1 pool [POOL_NAME]`
4.  **Static NAT:** `ip nat inside source static [Private_IP] [Public_IP]`

