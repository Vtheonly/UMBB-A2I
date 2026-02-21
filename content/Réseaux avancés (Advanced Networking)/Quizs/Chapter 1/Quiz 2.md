---
sources:
  - "[[Chapter 1 - Summary Review]]"
---

> [!question] Subnetting is used to break a single large network ID into smaller, manageable pieces.
>
> > [!success]- Answer
> > True

> [!question] In a subnet mask, the '0' bits represent the Network portion.
>
> > [!success]- Answer
> > False

> [!question] CIDR notation `/24` is equivalent to the decimal mask `255.255.255.0`.
>
> > [!success]- Answer
> > True

> [!question] To calculate the number of usable hosts per subnet, you use the formula $2^h$ (where $h$ is host bits).
>
> > [!success]- Answer
> > False

> [!question] RIPv1 is a routing protocol that supports VLSM (Variable Length Subnet Mask).
>
> > [!success]- Answer
> > False

> [!question] Private IP addresses are routable on the global Internet backbone.
>
> > [!success]- Answer
> > False

> [!question] VLSM requires sorting host requirements from smallest to largest.
>
> > [!success]- Answer
> > False

> [!question] The IP range `10.0.0.0/8` is a Class A private addressing range.
>
> > [!success]- Answer
> > True

> [!question] APIPA addresses start with `169.254.x.x` and indicate a failure to reach a DHCP server.
>
> > [!success]- Answer
> > True

> [!question] The "Magic Number" or increment in subnetting is the value of the lowest borrowed bit.
>
> > [!success]- Answer
> > True

> [!question] Which operation does a router perform between an IP and a mask to find the Network Address?
> a) OR
> b) XOR
> c) AND
> d) NOT
>
> > [!success]- Answer
> > c) AND

> [!question] How many host bits are remaining in a `/19` subnet mask?
> a) 19
> b) 13
> c) 8
> d) 5
>
> > [!success]- Answer
> > b) 13

> [!question] Which private range is typically used for home routers and small offices?
> a) 10.0.0.0/8
> b) 172.16.0.0/12
> c) 192.168.0.0/16
> d) 127.0.0.0/8
>
> > [!success]- Answer
> > c) 192.168.0.0/16

> [!question] What is the "Golden Rule" of VLSM?
> a) Smallest subnet first
> b) Largest subnet first
> c) WAN links first
> d) Random assignment
>
> > [!success]- Answer
> > b) Largest subnet first

> [!question] Which CIDR notation corresponds to the mask `255.255.224.0`?
> a) /18
> b) /19
> c) /20
> d) /21
>
> > [!success]- Answer
> > b) /19

> [!question] Why is "2" subtracted when calculating usable hosts?
> a) For the Router and Switch
> b) For Network ID and Broadcast Address
> c) For Gateway and Gateway redundacy
> d) For loopback and multicast
>
> > [!success]- Answer
> > b) For Network ID and Broadcast Address

> [!question] Which of the following is a VALID private IP address?
> a) 11.0.0.1
> b) 172.32.0.1
> c) 192.168.50.25
> d) 8.8.8.8
>
> > [!success]- Answer
> > c) 192.168.50.25

> [!question] What is a primary goal of VLSM?
> a) Increase routing speed
> b) Minimize IP address wastage
> c) Simplify network documentation
> d) Replace IPv6
>
> > [!success]- Answer
> > b) Minimize IP address wastage

> [!question] If you borrow 3 bits from a Class C network, how many subnets are created?
> a) 3
> b) 6
> c) 8
> d) 16
>
> > [!success]- Answer
> > c) 8

> [!question] What does it mean if a host has an IP of `169.254.10.5`?
> a) It is a large enterprise server
> b) It failed to get a DHCP address
> c) It is a multicast source
> d) It is the default gateway
>
> > [!success]- Answer
> > b) It failed to get a DHCP address

> [!question] Match the Subnet Mask with its CIDR prefix.
>
> > [!example] Group A
> > a) 255.0.0.0
> > b) 255.255.0.0
> > c) 255.255.255.0
>
> > [!example] Group B
> > n) /16
> > o) /24
> > p) /8
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the RFC 1918 Private Range with its Class.
>
> > [!example] Group A
> > a) 10.0.0.0/8
> > b) 172.16.0.0/12
> > c) 192.168.0.0/16
>
> > [!example] Group B
> > n) Class B
> > o) Class C
> > p) Class A
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the masking logic with its bit value.
>
> > [!example] Group A
> > a) 1s (Ones)
> > b) 0s (Zeros)
> > c) Subnetting
>
> > [!example] Group B
> > n) Borrowing bits from Host to Network.
> > o) Represent the Network portion.
> > p) Represent the Host portion.
>
> > [!success]- Answer
> > a) -> o)
> > b) -> p)
> > c) -> n)

> [!question] Match the VLSM requirement with the Host count.
>
> > [!example] Group A
> > a) 100 hosts
> > b) 57 hosts
> > c) 25 hosts
>
> > [!example] Group B
> > n) /26 mask
> > o) /27 mask
> > p) /25 mask
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the addressing type with its scope.
>
> > [!example] Group A
> > a) Public IP
> > b) Private IP
> > c) APIPA
>
> > [!example] Group B
> > n) Local LAN only, not routable.
> > o) Global Internet, routable.
> > p) Link-local, failed DHCP.
>
> > [!success]- Answer
> > a) -> o)
> > b) -> n)
> > c) -> p)

> [!question] Match the Subnetting formula component with its definition.
>
> > [!example] Group A
> > a) $2^b$
> > b) $2^h - 2$
> > c) Increment
>
> > [!example] Group B
> > n) Number of usable hosts.
> > o) Number of subnets created.
> > p) Distance between network addresses.
>
> > [!success]- Answer
> > a) -> o)
> > b) -> n)
> > c) -> p)

> [!question] Match the network mask octet to its binary value.
>
> > [!example] Group A
> > a) 128
> > b) 192
> > c) 224
>
> > [!example] Group B
> > n) 11000000
> > o) 11100000
> > p) 10000000
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the addressing feature with the IP type.
>
> > [!example] Group A
> > a) Unique worldwide
> > b) Assigned by Admin/DHCP freely
> > c) Starts with 127
>
> > [!example] Group B
> > n) Private IP
> > o) Loopback IP
> > p) Public IP
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the VLSM protocol with its capability.
>
> > [!example] Group A
> > a) RIPv1
> > b) RIPv2
> > c) OSPF
>
> > [!example] Group B
> > n) Supports VLSM
> > o) Supports VLSM
> > p) Classful ONLY (No VLSM)
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)

> [!question] Match the Subnet mask to its slash notation.
>
> > [!example] Group A
> > a) 255.255.255.240
> > b) 255.255.255.248
> > c) 255.255.255.252
>
> > [!example] Group B
> > n) /29
> > o) /30
> > p) /28
>
> > [!success]- Answer
> > a) -> p)
> > b) -> n)
> > c) -> o)
