---
sources:
  - "[[Exercise 1]]"
  - "[[Exercise 2]]"
  - "[[Exercise 3]]"
  - "[[Exercise 4]]"
  - "[[Exercise 5]]"
  - "[[Exercise 6]]"
  - "[[Exercise 7]]"
  - "[[Exercise 8]]"
  - "[[Exercise 9]]"
  - "[[Exercise 10]]"
  - "[[Exercise 11]]"
  - "[[Exercise 1 (1)]]"
  - "[[Exercise 2 (1)]]"
  - "[[Exercise 3 (1)]]"
  - "[[Exercise 4 (1)]]"
---
> [!question] The IP address `191.200.10.5` belongs to IP Class B.
>> [!success]- Answer
>> True

> [!question] How many usable host addresses are available in a subnet with a `/26` mask?
> a) 64
> b) 62
> c) 32
> d) 30
>> [!success]- Answer
>> b) 62

> [!question] Match the term to the OSI Model Layer where it is primarily defined.
>> [!example] Group A
>> a) IP Address
>> b) MAC Address
>> c) TCP/UDP Port
>
>> [!example] Group B
>> n) Layer 4 (Transport)
>> o) Layer 2 (Data Link)
>> p) Layer 3 (Network)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] An IP packet with a Total Length of 60 bytes and an IHL of 5 contains exactly 40 bytes of payload data.
>> [!success]- Answer
>> True

> [!question] The process of combining `193.152.100.0/27` and `193.152.100.32/27` into a single `193.152.100.0/26` route is called:
> a) Fragmentation
> b) Subnetting
> c) Aggregation (Supernetting)
> d) Encapsulation
>> [!success]- Answer
>> c) Aggregation (Supernetting)

> [!question] Match the default classful IP address to its corresponding network address.
>> [!example] Group A
>> a) `10.50.25.10`
>> b) `192.168.1.1`
>> c) `172.16.32.64`
>
>> [!example] Group B
>> n) `172.16.0.0`
>> o) `10.0.0.0`
>> p) `192.168.1.0`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] A `/30` subnet mask provides 4 usable host IP addresses.
>> [!success]- Answer
>> False

> [!question] In an Ethernet II frame, which field is used to identify the protocol of the data payload (e.g., IPv4, ARP)?
> a) Source Address
> b) Preamble
> c) EtherType
> d) Frame Check Sequence (FCS)
>> [!success]- Answer
>> c) EtherType

> [!question] Match the VLSM host requirement to the correct "block size" of the allocated subnet.
>> [!example] Group A
>> a) Requires 2 hosts
>> b) Requires 14 hosts
>> c) Requires 28 hosts
>
>> [!example] Group B
>> n) Block size of 16 addresses (/28)
>> o) Block size of 4 addresses (/30)
>> p) Block size of 32 addresses (/27)
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] The network address of a subnet is always the first IP address in its range.
>> [!success]- Answer
>> True

> [!question] A network administrator needs to create 5 subnets from the network `172.17.0.0/19`. How many bits must be borrowed to achieve this with FLSM?
> a) 2 bits (creates 4 subnets)
> b) 3 bits (creates 8 subnets)
> c) 4 bits (creates 16 subnets)
> d) 5 bits (creates 32 subnets)
>> [!success]- Answer
>> b) 3 bits (creates 8 subnets)

> [!question] Match the subnet mask to the number of usable hosts it provides.
>> [!example] Group A
>> a) `/25`
>> b) `/29`
>> c) `/27`
>
>> [example] Group B
>> n) 6 hosts
>> o) 126 hosts
>> p) 30 hosts
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] An EtherType field of `0x0800` signifies that the payload is an ARP packet.
>> [!success]- Answer
>> False

> [!question] A MAC address starts with the hex byte `B4`. What type of address is it?
> a) Broadcast, because it starts with 'B'
> b) Multicast, because 'B' is an odd number
> c) Unicast, because the last hex digit '4' is an even number
> d) Invalid address type
>> [!success]- Answer
>> c) Unicast, because the last hex digit '4' is an even number

> [!question] Match the component of an Ethernet frame to its standard size in bytes.
>> [!example] Group A
>> a) Destination MAC Address
>> b) Source MAC Address
>> c) EtherType
>
>> [!example] Group B
>> n) 2 Bytes
>> o) 6 Bytes
>> p) 6 Bytes
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] In route aggregation, the resulting CIDR prefix length is always smaller (a lower number) than the prefixes of the networks being aggregated.
>> [!success]- Answer
>> True

> [!question] A Class C network `209.206.202.0` needs to be divided into 60 subnets. What is the correct new subnet mask?
> a) `255.255.255.192` (/26)
> b) `255.255.255.240` (/28)
> c) `255.255.255.252` (/30)
> d) `255.255.255.224` (/27)
>> [!success]- Answer
>> c) `255.255.255.252` (/30)

> [!question] Match the Fragment Offset value to the starting byte of the data in the original datagram.
>> [!example] Group A
>> a) Offset = 0
>> b) Offset = 185
>> c) Offset = 370
>
>> [!example] Group B
>> n) Starts at byte 1480
>> o) Starts at byte 0
>> p) Starts at byte 2960
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] A MAC address with the first byte `1E` is a multicast address.
>> [!success]- Answer
>> False

> [!question] What is the primary motivation for using VLSM (Variable Length Subnet Masking)?
> a) To simplify router configuration
> b) To increase network speed
> c) To improve address space efficiency and reduce wasted IPs
> d) To make all subnets the same size for easier management
>> [!success]- Answer
>> c) To improve address space efficiency and reduce wasted IPs

> [!question] Match the number of borrowed bits (`n`) from a Class C network to the resulting CIDR mask.
>> [!example] Group A
>> a) n = 2 bits
>> b) n = 3 bits
>> c) n = 4 bits
>
>> [!example] Group B
>> n) /27
>> o) /28
>> p) /26
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] A host machine's default gateway must be on a different subnet for routing to work correctly.
>> [!success]- Answer
>> False

> [!question] An IP datagram must be fragmented. Which header field is used to reassemble the fragments in the correct order?
> a) Identification
> b) Fragment Offset
> c) Total Length
> d) Header Checksum
>> [!success]- Answer
>> b) Fragment Offset

> [!question] Match the IP address to its specific classification.
>> [!example] Group A
>> a) `239.255.255.250`
>> b) `240.0.0.10`
>> c) `127.0.0.1`
>
>> [!example] Group B
>> n) Loopback
>> o) Experimental (Class E)
>> p) Multicast (Class D)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] The bitwise AND operation between a host IP and its subnet mask reveals the broadcast address.
>> [!success]- Answer
>> False

> [!question] A subnet needs to support 2000 hosts. What is the smallest CIDR mask that can be used?
> a) /20
> b) /21
> c) /22
> d) /23
>> [!success]- Answer
>> b) /21

> [!question] Match the IPv4 header hex value from the packet `45 00 ... 38 01 ...` to its meaning.
>> [!example] Group A
>> a) `5` (from `45`)
>> b) `38`
>> c) `01`
>
>> [!example] Group B
>> n) Protocol is ICMP
>> o) Time To Live is 56
>> p) IHL (Header length is 20 bytes)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] The source MAC address field in an Ethernet frame can contain a broadcast address.
>> [!success]- Answer
>> False

> [!question] A network plan using a single `/27` mask for all subnets, regardless of their individual size requirements, is an example of:
> a) VLSM
> b) FLSM
> c) Supernetting
> d) NAT
>> [!success]- Answer
>> b) FLSM

> [!question] Match the IP address `172.17.X.Y` to the subnet it belongs to, given the FLSM plan with mask `/22`.
>> [!example] Group A
>> a) `172.17.6.210`
>> b) `172.17.12.25`
>> c) `172.17.18.1`
>
>> [!example] Group B
>> n) Subnet `172.17.16.0/22`
>> o) Subnet `172.17.4.0/22`
>> p) Subnet `172.17.12.0/22`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)