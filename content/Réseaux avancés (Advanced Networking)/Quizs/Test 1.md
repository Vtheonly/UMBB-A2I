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
> [!question] The MAC address `01-00-5E-AB-CD-EF` is a Unicast address.
>> [!success]- Answer
>> False

> [!question] Which of the following MAC addresses is a Unicast address?
> a) `01-00-5E-AB-CD-EF`
> b) `11-52-AB-9B-DC-12`
> c) `00-01-4B-B4-A2-EF`
> d) `FF-FF-FF-FF-FF-FF`
>> [!success]- Answer
>> c) `00-01-4B-B4-A2-EF`

> [!question] Match the first byte of a MAC address to its type.
>> [!example] Group A
>> a) `00`
>> b) `01`
>> c) `FF`
>
>> [!example] Group B
>> n) Broadcast
>> o) Unicast
>> p) Multicast
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] A Multicast MAC address can be used in the "source address" field of an Ethernet frame.
>> [!success]- Answer
>> False

> [!question] Machine M1 has the IP `192.175.60.3`. What is the broadcast address for its network (assuming a default classful mask)?
> a) `192.175.60.0`
> b) `192.175.60.255`
> c) `192.175.255.255`
> d) `255.255.255.255`
>> [!success]- Answer
>> b) `192.175.60.255`

> [!question] Match the IP address to its class.
>> [!example] Group A
>> a) `10.5.5.1`
>> b) `150.100.50.1`
>> c) `200.20.10.1`
>
>> [!example] Group B
>> n) Class C
>> o) Class A
>> p) Class B
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] The EtherType `0x0806` in an Ethernet frame indicates that the payload is an IPv4 packet.
>> [!success]- Answer
>> False

> [!question] What is the subnet address for the host `184.65.94.20` using the mask `255.255.240.0`?
> a) `184.65.94.0`
> b) `184.65.0.0`
> c) `184.65.80.0`
> d) `184.65.64.0`
>> [!success]- Answer
>> c) `184.65.80.0`

> [!question] Match the IP address to its special purpose.
>> [!example] Group A
>> a) `127.1.1.1`
>> b) `231.200.1.1`
>> c) `198.121.254.255`
>
>> [!example] Group B
>> n) Network Broadcast Address
>> o) Multicast Address (Class D)
>> p) Loopback Address
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] The IP address `127.0.0.1` is a valid and usable address for a standard host PC on a LAN.
>> [!success]- Answer
>> False

> [!question] A Class C network `198.63.24.0` needs to be divided into subnets that can each support at least 60 hosts. What is the minimum number of host bits (`h`) required?
> a) 5 bits
> b) 6 bits
> c) 7 bits
> d) 4 bits
>> [!success]- Answer
>> b) 6 bits

> [!question] Match the CIDR notation to its decimal equivalent.
>> [!example] Group A
>> a) `/27`
>> b) `/28`
>> c) `/30`
>
>> [!example] Group B
>> n) `255.255.255.240`
>> o) `255.255.255.252`
>> p) `255.255.255.224`
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] When subnetting a Class B network with the mask `255.255.240.0`, a total of 4 bits have been borrowed from the host portion.
>> [!success]- Answer
>> True

> [!question] In the IP header data `45 00 00 3C ...`, what does the hex value `3C` represent?
> a) The header is 60 bytes long
> b) The total packet length is 60 bytes
> c) The TTL is 60
> d) The protocol is number 60
>> [!success]- Answer
>> b) The total packet length is 60 bytes

> [!question] Match the hex value from the header `45 00 ... 38 01 c0 a8 01 01` to its meaning.
>> [!example] Group A
>> a) `4` (from `45`)
>> b) `01`
>> c) `c0 a8 01 01`
>
>> [!example] Group B
>> n) Protocol is ICMP
>> o) Source IP is 192.168.1.1
>> p) Version is IPv4
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] A host can use a default gateway that is located on a different subnet.
>> [!success]- Answer
>> False

> [!question] In an IPv4 header, a Don't Fragment (DF) bit set to 1 means:
> a) The packet is the last fragment in a series.
> b) The packet must be fragmented by routers.
> c) The packet cannot be fragmented and must be dropped if it exceeds the MTU.
> d) More fragments are following this one.
>> [!success]- Answer
>> c) The packet cannot be fragmented and must be dropped if it exceeds the MTU.

> [!question] Match the networking term to its description.
>> [!example] Group A
>> a) FLSM
>> b) VLSM
>> c) Aggregation
>
>> [!example] Group B
>> n) Creates subnets sized specifically for their host requirements to minimize waste.
>> o) Divides a network into multiple subnets of the exact same size.
>> p) Combines multiple contiguous routes into a single summary route.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] In VLSM, it is best practice to allocate the address blocks for the smallest subnets first to save space.
>> [!success]- Answer
>> False

> [!question] A fragment's data starts at byte 2960 of the original datagram. What is its Fragment Offset value in the IP header?
> a) 2960
> b) 1480
> c) 370
> d) 185
>> [!success]- Answer
>> c) 370

> [!question] Match the subnetting calculation to what it determines.
>> [!example] Group A
>> a) `2^n` (where n = borrowed bits)
>> b) `2^h - 2` (where h = host bits)
>> c) `IP Address AND Subnet Mask`
>
>> [!example] Group B
>> n) The network address of the subnet
>> o) The number of usable hosts per subnet
>> p) The total number of subnets created
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] An IHL value of `5` in an IPv4 header means the header is 5 bytes long.
>> [!success]- Answer
>> False

> [!question] For a VLSM plan, which subnet should be allocated first from the main address block?
> a) The one with the most hosts.
> b) The one with the fewest hosts.
> c) The one for the point-to-point WAN link.
> d) The allocation order does not matter.
>> [!success]- Answer
>> a) The one with the most hosts.

> [!question] Match the fragmentation field/flag to its function.
>> [!example] Group A
>> a) Identification
>> b) MF (More Fragments) Flag
>> c) Fragment Offset
>
>> [!example] Group B
>> n) A value shared by all fragments of the same original datagram.
>> o) Specifies the fragment's position in 8-byte blocks.
>> p) Set to 0 only on the final fragment of a sequence.
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] In IP fragmentation, the MF (More Fragments) flag is set to 0 on all fragments except the last one.
>> [!success]- Answer
>> False

> [!question] The IP address `248.5.10.156` belongs to which class?
> a) Class C
> b) Class D
> c) Class A
> d) Class E
>> [!success]- Answer
>> d) Class E

> [!question] Match the address type to the OSI model layer where it primarily operates.
>> [!example] Group A
>> a) MAC Address
>> b) IP Address
>> c) Port Number
>
>> [!example] Group B
>> n) Layer 4 (Transport)
>> o) Layer 3 (Network)
>> p) Layer 2 (Data Link)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] The broadcast MAC address is `00:00:00:00:00:00`.
>> [!success]- Answer
>> False

> [!question] In the Ethernet frame data `ffff ffff ffff 09ab 14d8 0548 0806 ...`, what does `0806` represent?
> a) The source MAC address
> b) The destination MAC address
> c) The EtherType for ARP
> d) The EtherType for IPv4
>> [!success]- Answer
>> c) The EtherType for ARP

> [!question] Match the number of required hosts to the minimum number of host bits (`h`) needed.
>> [!example] Group A
>> a) 14 hosts
>> b) 60 hosts
>> c) 500 hosts
>
>> [!example] Group B
>> n) 6 bits
>> o) 9 bits
>> p) 4 bits
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)