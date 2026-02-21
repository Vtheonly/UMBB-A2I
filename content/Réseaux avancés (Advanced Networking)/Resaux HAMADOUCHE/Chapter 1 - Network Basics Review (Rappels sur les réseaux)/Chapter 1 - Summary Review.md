# Chapter 1: Network Basics Review - Comprehensive Summary

This note provides a detailed overview of the core concepts covered in the Network Basics Review chapter, including network classifications, topologies, architectures, and the fundamental principles of IPv4 addressing and subnetting.

## 1. Network Classifications

Networks are categorized based on their geographic scope:

- **PAN (Personal Area Network):** Short-range connections (e.g., Bluetooth) within a few meters.
- **LAN (Local Area Network):** High-speed private networks within a building or campus.
- **MAN (Metropolitan Area Network):** City-wide networks interconnecting LANs.
- **WAN (Wide Area Network):** Global or country-wide networks involving ISPs.

## 2. Topologies and Architectures

### Topologies (Physical vs. Logical)

- **Bus:** Single central cable; vulnerable to a single point of failure.
- **Star:** Devices connect to a central hub/switch; most common in modern networks.
- **Ring:** Closed loop using token passing; deterministic.
- **Mesh:** High redundancy; every device connects to several others.
- **Tree:** Hierarchical connection of switches (extended star).

### Architectures

- **Client/Server:** Centralized management, dedicated servers providing services to clients.
- **Peer-to-Peer (P2P):** Decentralized; every node acts as both client and server.

## 3. The OSI and TCP/IP Models

The layered models standardize communication:

- **OSI Model (7 Layers):** Physical, Data Link, Network, Transport, Session, Presentation, Application.
- **TCP/IP Model (4/5 Layers):** Network Access, Internet, Transport, Application.
- **PDUs (Protocol Data Units):**
  - Layer 4: Segment
  - Layer 3: Packet
  - Layer 2: Frame
  - Layer 1: Bit

## 4. MAC and IP Addressing

### MAC Address (Physical)

- 48-bit hexadecimal address burned into the NIC.
- First 24 bits: OUI (Manufacturer ID).
- Last 24 bits: Unique Serial Number.

### IPv4 Address (Logical)

- 32-bit address expressed in four decimal octets.
- **Classful Addressing:**
  - Class A: 1-126 (/8)
  - Class B: 128-191 (/16)
  - Class C: 192-223 (/24)
  - Class D: Multicast (224-239)
  - Class E: Experimental (240-255)
- **Special Addresses:**
  - `127.0.0.1`: Loopback (Localhost).
  - Network Address: All Host bits = 0.
  - Broadcast Address: All Host bits = 1.

## 5. ARP (Address Resolution Protocol)

ARP bridges the gap between Layer 3 and Layer 2.

- **ARP Request:** Broadcast (FF:FF:FF:FF:FF:FF) message asking "Who has this IP?".
- **ARP Reply:** Unicast response with the MAC address.
- **ARP Cache:** RAM table storing IP/MAC pairings for reuse.

## 6. Subnetting and VLSM

### Subnetting

Breaking large networks into smaller subnets by "borrowing" bits from the host portion.

- **Subnets:** $2^b$ (b = borrowed bits).
- **Usable Hosts:** $2^h - 2$ (h = remaining host bits).
- **Subnet Mask:** Defines which part is Network and which is Host.

### VLSM (Variable Length Subnet Mask)

Allows different masks for different subnets to minimize waste.

- **Rule:** Always allocate the largest requirements first.
- **Requirement:** Routing protocols like OSPF or RIPv2 must be used.

### Private Addressing (RFC 1918)

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16
- APIPA: 169.254.x.x (Self-assigned on DHCP failure).
