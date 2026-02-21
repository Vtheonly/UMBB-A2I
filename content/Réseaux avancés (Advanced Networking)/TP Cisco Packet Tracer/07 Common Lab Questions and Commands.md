# 07 - Common Lab Questions & Commands

## ❓ From TP02: "Why can't I ping?"

**Question:** You connected two PCs to a router but they can't ping each other.
**Answer:**

1.  **Gateway Missing:** Did you configure the "Default Gateway" on the PC? The PC doesn't know where to send the packet destined for a foreign network.
2.  **No Shutdown:** Did you turn on the router interface? (`no shutdown`).
3.  **Wrong IP Subnet:** Is the PC IP matching the Router Interface subnet?

## ❓ From TP02: "Secure the Switch"

**Task:** Secure access to console and enable.
**Command Summary:**

- `line console 0` -> `password X` -> `login` (Secures physical plug-in).
- `enable secret X` (Secures the `enable` command).
- `service password-encryption` (Hides passwords in the config file).

## ❓ From TP2 (Interconnection): "ARP -a"

**Exercise:** Run `arp -a` on the PC.
**Explanation:**

- **ARP (Address Resolution Protocol)** maps an IP address to a MAC address.
- When you ping a local IP, your PC asks "Who has IP X?". The owner replies "I have it, my MAC is Y".
- `arp -a` displays this cache.
- **Important:** When pinging a _remote_ network, the PC does NOT ARP for the remote PC. It ARPs for the **Default Gateway** (The Router).

## ❓ From TP4 (NAT): "Can I surf the web?"

**Question:** If I only configure the Router interfaces, can I access the web server from the internet?
**Answer:** **No.** The web server uses a private IP (172.16...). Private IPs are dropped by Internet routers. You **must** configure **Static NAT** to map the private IP to a valid Public IP so the outside world can address it.
