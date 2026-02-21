---
sources:
  - "[[1.1 Network Definitions and Elements]]"
  - "[[1.2 Network Classification]]"
  - "[[1.3 Transmission Modes]]"
  - "[[1.4 Protocols and Layered Models]]"
  - "[[1.5 MAC Addressing (Physical)]]"
  - "[[1.6 IP Addressing (Logical - IPv4)]]"
  - "[[1.7 Subnetting and Masks]]"
  - "[[1.8 Advanced Addressing: VLSM]]"
  - "[[1.9 Public vs Private Addressing]]"
  - "[[1.10 Network Address Translation (NAT)]]"
  - "[[1.11 The IPv4 Protocol]]"
  - "[[1.12 Address Resolution Protocol (ARP)]]"
---

> [!question] A Switch is considered a "dumb" device that blindly broadcasts data received on one port to all other ports.
>> [!success]- Answer
>> False

> [!question] In the OSI model, Decapsulation occurs as data moves down the stack from the Application layer to the Physical layer.
>> [!success]- Answer
>> False

> [!question] A MAC address is a hierarchical address similar to a postal address (Country -> City -> Street).
>> [!success]- Answer
>> False

> [!question] In a Star topology, the central node (Switch or Hub) represents a single point of failure.
>> [!success]- Answer
>> True

> [!question] The IPv4 Loopback address `127.0.0.1` sends traffic out to the network gateway to test connectivity.
>> [!success]- Answer
>> False

> [!question] When applying VLSM (Variable Length Subnet Mask), you should assign subnets starting from the largest requirement to the smallest.
>> [!success]- Answer
>> True

> [!question] An IP address starting with `169.254.x.x` indicates that the device successfully contacted a DHCP server.
>> [!success]- Answer
>> False

> [!question] Port Address Translation (PAT) allows multiple private IP addresses to map to a single public IP address using different source ports.
>> [!success]- Answer
>> True

> [!question] An ARP Request is sent as a Unicast message to a specific device.
>> [!success]- Answer
>> False

> [!question] In an IPv4 packet, if the TTL (Time To Live) value reaches 0, the router discards the packet to prevent infinite loops.
>> [!success]- Answer
>> True

> [!question] Match the Network Scope with its description.
>> [!example] Group A
>> a) PAN
>> b) LAN
>> c) WAN
>
>> [!example] Group B
>> n) Covers a country or globe; generally uses ISPs.
>> o) Range of a few meters; connects personal devices like headsets.
>> p) Limited geography like a building or campus; high speed.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Intermediary Device with its Layer/Function.
>> [!example] Group A
>> a) Hub
>> b) Switch
>> c) Router
>
>> [!example] Group B
>> n) Layer 2; filters/forwards based on MAC address.
>> o) Layer 3; uses IP addresses to determine best path.
>> p) Layer 1; broadcasts data to all ports blindly.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the PDU (Protocol Data Unit) to its OSI Layer.
>> [!example] Group A
>> a) Transport Layer
>> b) Network Layer
>> c) Data Link Layer
>
>> [!example] Group B
>> n) Frame
>> o) Segment
>> p) Packet
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Topology to its characteristic.
>> [!example] Group A
>> a) Bus
>> b) Ring
>> c) Mesh
>
>> [!example] Group B
>> n) Uses token passing; deterministic.
>> o) High redundancy; very expensive cabling.
>> p) Single central cable; high collision rate.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Transmission Mode with its definition.
>> [!example] Group A
>> a) Unicast
>> b) Multicast
>> c) Broadcast
>
>> [!example] Group B
>> n) 1-to-All communication.
>> o) 1-to-1 communication.
>> p) 1-to-Many (Specific Group) communication.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the IP Class with its First Octet Range.
>> [!example] Group A
>> a) Class A
>> b) Class B
>> c) Class C
>
>> [!example] Group B
>> n) 192 - 223
>> o) 1 - 126
>> p) 128 - 191
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Private IP Range (RFC 1918) to the Class.
>> [!example] Group A
>> a) 10.0.0.0/8
>> b) 172.16.0.0/12
>> c) 192.168.0.0/16
>
>> [!example] Group B
>> n) Class B Private Range
>> o) Class C Private Range
>> p) Class A Private Range
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the NAT Type with its description.
>> [!example] Group A
>> a) Static NAT
>> b) Dynamic NAT
>> c) PAT (Overload)
>
>> [!example] Group B
>> n) Mapping many private IPs to a single public IP using ports.
>> o) Mapping one private IP to one specific public IP.
>> p) Mapping private IPs to a pool of public IPs (First come, first served).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the IPv4 Header Field with its function.
>> [!example] Group A
>> a) TTL
>> b) Protocol
>> c) Fragment Offset
>
>> [!example] Group B
>> n) Indicates the position of data in the original packet.
>> o) Prevents infinite loops by decrementing at routers.
>> p) Identifies the content type (e.g., TCP=6, UDP=17).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Special Address Type with its Example.
>> [!example] Group A
>> a) Network Address
>> b) Broadcast Address
>> c) Loopback
>
>> [!example] Group B
>> n) 192.168.1.255 (All host bits 1)
>> o) 127.0.0.1
>> p) 192.168.1.0 (All host bits 0)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Which layer of the OSI model is responsible for End-to-end delivery, Reliability, and Flow Control?
> a) Network Layer
> b) Transport Layer
> c) Session Layer
> d) Data Link Layer
>> [!success]- Answer
> b) Transport Layer

> [!question] What is the correct formula to calculate the number of usable hosts per subnet?
> a) $2^b$
> b) $2^b - 2$
> c) $2^h$
> d) $2^h - 2$
>> [!success]- Answer
>> d) $2^h - 2$

> [!question] Which part of the MAC address `00:0B:DB:16:E7:8A` represents the OUI (Organizationally Unique Identifier)?
> a) The first 24 bits (`00:0B:DB`)
> b) The last 24 bits (`16:E7:8A`)
> c) The entire address
> d) The first byte only (`00`)
>> [!success]- Answer
>> a) The first 24 bits (`00:0B:DB`)

> [!question] You need to subnet a network to create 5 subnets. How many bits must you borrow ($b$) according to the formula $2^b \ge 5$?
> a) 2 bits
> b) 3 bits
> c) 4 bits
> d) 5 bits
>> [!success]- Answer
>> b) 3 bits

> [!question] In the IPv4 header, which flag is set to `0` only for the very last fragment of a packet?
> a) DF (Don't Fragment)
> b) TTL (Time To Live)
> c) MF (More Fragments)
> d) ToS (Type of Service)
>> [!success]- Answer
>> c) MF (More Fragments)

> [!question] If Host A (192.168.1.10) wants to send a packet to Google (8.8.8.8), what IP address is placed in the ARP Request?
> a) Google's IP (8.8.8.8)
> b) The Default Gateway's (Router) IP
> c) The Broadcast IP (255.255.255.255)
> d) Host A's own IP
>> [!success]- Answer
>> b) The Default Gateway's (Router) IP

> [!question] Which medium type uses "Electrical Impulses" for signal encoding?
> a) Fiber Optic
> b) Copper (Coaxial/Twisted Pair)
> c) Wireless (Radio Waves)
> d) Microwave
>> [!success]- Answer
>> b) Copper (Coaxial/Twisted Pair)

> [!question] What is the default subnet mask for a Class C network?
> a) 255.0.0.0
> b) 255.255.0.0
> c) 255.255.255.0
> d) 255.255.255.255
>> [!success]- Answer
>> c) 255.255.255.0

> [!question] Which topology is characterized by "Full Mesh" where every device connects to every other device?
> a) Star
> b) Ring
> c) Bus
> d) Mesh
>> [!success]- Answer
>> d) Mesh

> [!question] Which of the following is an advantage of Peer-to-Peer (P2P) architecture?
> a) Centralized security and management
> b) Easy to back up data centrally
> c) Easy to set up and inexpensive
> d) Scalable performance with more users
>> [!success]- Answer
>> c) Easy to set up and inexpensive