---
sources:
  - "[[Chapter 1 - Summary Review]]"
---

> [!question] The OSI model has 7 layers, while the TCP/IP model has 4 or 5 layers.
>
> > [!success]- Answer
> > True

> [!question] MAC addresses are logical addresses that change when a computer moves to a new network.
>
> > [!success]- Answer
> > False

> [!question] ARP is used to find an IP address when only the MAC address is known.
>
> > [!success]- Answer
> > False

> [!question] An ARP Request is sent as a Broadcast (FF:FF:FF:FF:FF:FF).
>
> > [!success]- Answer
> > True

> [!question] The Network Layer in the OSI model is responsible for routing and logical addressing.
>
> > [!success]- Answer
> > True

> [!question] A MAC address consists of 48 bits, usually represented in Hexadecimal.
>
> > [!success]- Answer
> > True

> [!question] Routers reassemble fragmented IP packets before forwarding them to the next hop.
>
> > [!success]- Answer
> > False

> [!question] The ARP Cache is a table stored in RAM to avoid repeating ARP requests.
>
> > [!success]- Answer
> > True

> [!question] Layer 2 (Data Link) units are called "Packets".
>
> > [!success]- Answer
> > False

> [!question] ARP Spoofing is a security risk where an attacker provides false MAC-to-IP pairings.
>
> > [!success]- Answer
> > True

> [!question] Which OSI layer is responsible for end-to-end communication and error recovery (e.g., TCP)?
> a) Network
> b) Data Link
> c) Transport
> d) Session
>
> > [!success]- Answer
> > c) Transport

> [!question] What is the first half (first 3 bytes) of a MAC address called?
> a) NIC
> b) OUI (Organizationally Unique Identifier)
> c) serial number
> d) IP prefix
>
> > [!success]- Answer
> > b) OUI (Organizationally Unique Identifier)

> [!question] When communicating with a remote server, what is the destination MAC address for the outgoing frame?
> a) The Server's MAC address
> b) The Default Gateway's (Router) MAC address
> c) A broadcast address
> d) The source's own MAC address
>
> > [!success]- Answer
> > b) The Default Gateway's (Router) MAC address

> [!question] Which protocol bridges the gap between Layer 3 (IP) and Layer 2 (MAC)?
> a) DNS
> b) DHCP
> c) ARP
> d) HTTP
>
> > [!success]- Answer
> > c) ARP

> [!question] What is the Data Unit for Layer 3 (Network)?
> a) Frame
> b) Segment
> c) Packet
> d) Bit
>
> > [!success]- Answer
> > c) Packet

> [!question] Which layer handles physical cabling and bit-level transmission?
> a) Layer 1 (Physical)
> b) Layer 2 (Data Link)
> c) Layer 3 (Network)
> d) Layer 4 (Transport)
>
> > [!success]- Answer
> > a) Layer 1 (Physical)

> [!question] What command can be used to view the ARP Cache on a Windows/Linux machine?
> a) ipconfig
> b) ping -a
> c) arp -a
> d) traceroute
>
> > [!success]- Answer
> > c) arp -a

> [!question] Which part of the MAC address is unique to the specific manufacturer's card?
> a) The first 24 bits
> b) The last 24 bits
> c) The middle 8 bits
> d) None, it's random
>
> > [!success]- Answer
> > b) The last 24 bits

> [!question] How does a destination host know how to reassemble fragmented packets?
> a) By the Source IP
> b) By the TTL value
> c) By the Identification and Fragment Offset fields
> d) By the MAC address
>
> > [!success]- Answer
> > c) By the Identification and Fragment Offset fields

> [!question] Which layer is responsible for "framing" data?
> a) Physical
> b) Data Link
> c) Network
> d) Transport
>
> > [!success]- Answer
> > b) Data Link

> [!question] Match the OSI Layer with its Data Unit (PDU).
>
> > [!example] Group A
> > a) Layer 4 (Transport)
> > b) Layer 3 (Network)
> > c) Layer 2 (Data Link)
>
> > [!example] Group B
> > n) Packet
> > o) Frame
> > p) Segment
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the Address type with its Layer.
>
> > [!example] Group A
> > a) MAC Address
> > b) IP Address
> > c) Port Number
>
> > [!example] Group B
> > n) Layer 3
> > o) Layer 4
> > p) Layer 2
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the ARP step with its description.
>
> > [!example] Group A
> > a) ARP Request
> > b) ARP Reply
> > c) ARP Cache Update
>
> > [!example] Group B
> > n) Unicast response containing the MAC.
> > o) Saving the IP/MAC pair in RAM.
> > p) Broadcast asking "Who has this IP?".
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the MAC Address component with its length.
>
> > [!example] Group A
> > a) Total MAC address
> > b) OUI (Vendor)
> > c) Serial Number (NIC)
>
> > [!example] Group B
> > n) 24 bits (3 bytes)
> > o) 24 bits (3 bytes)
> > p) 48 bits (6 bytes)
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the OSI layer with its primary function.
>
> > [!example] Group A
> > a) Physical
> > b) Presentation
> > c) Session
>
> > [!example] Group B
> > n) Compression, Encryption, Formatting.
> > o) Managing logical dialogues.
> > p) Transmission of raw bits.
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the Network device with its primary OSI Layer.
>
> > [!example] Group A
> > a) Hub
> > b) Switch
> > c) Router
>
> > [!example] Group B
> > n) Layer 2
> > o) Layer 3
> > p) Layer 1
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the IP header field for fragmentation.
>
> > [!example] Group A
> > a) Identification
> > b) Fragment Offset
> > c) More Fragments (MF) flag
>
> > [!example] Group B
> > n) Indicates if more pieces are coming.
> > o) Unique ID for a group of fragments.
> > p) The position of data in the original packet.
>
> > [!success]- Answer
> > a) -> o)
> > b) -> p)
> > c) -> n)

> [!question] Match the TCP/IP Layer with its OSI Equivalent.
>
> > [!example] Group A
> > a) Application (TCP/IP)
> > b) Internet (TCP/IP)
> > c) Network Access (TCP/IP)
>
> > [!example] Group B
> > n) Network Layer
> > o) Layers 1 & 2
> > p) Layers 5, 6, & 7
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the ARP behavior with the Destination type.
>
> > [!example] Group A
> > a) Local destination
> > b) Remote destination
> > c) ARP Cache hit
>
> > [!example] Group B
> > n) ARP for Default Gateway's MAC.
> > o) No ARP request sent (uses RAM).
> > p) ARP for specific Host's MAC.
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the MAC addressing mode with its address.
>
> > [!example] Group A
> > a) Unicast MAC
> > b) Broadcast MAC
> > c) Multicast MAC (Standard prefix)
>
> > [!example] Group B
> > n) FF:FF:FF:FF:FF:FF
> > o) 01:00:5E...
> > p) Single specific NIC address
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)
