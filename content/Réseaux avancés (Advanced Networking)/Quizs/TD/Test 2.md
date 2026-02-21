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
> [!question] The MAC address `FF:FF:FF:FF:FF:FF` is a type of multicast address.
>> [!success]- Answer
>> False

> [!question] Which of the following IP addresses is invalid due to an out-of-range octet?
> a) `10.255.255.1`
> b) `192.168.1.256`
> c) `128.0.0.1`
> d) `224.0.0.5`
>> [!success]- Answer
>> b) `192.168.1.256`

> [!question] Match the first octet range to the corresponding IP Address Class.
>> [!example] Group A
>> a) 1-126
>> b) 128-191
>> c) 192-223
>
>> [!example] Group B
>> n) Class B
>> o) Class C
>> p) Class A
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] To create 1000 subnets from a Class A network, you must borrow at least 10 bits.
>> [!success]- Answer
>> True

> [!question] A Class B network is subnetted with a `/20` mask. How many bits were borrowed from the default host portion?
> a) 2
> b) 4
> c) 8
> d) 16
>> [!success]- Answer
>> b) 4

> [!question] Match the number of required hosts to the most efficient CIDR mask.
>> [!example] Group A
>> a) 2 hosts (point-to-point)
>> b) 14 hosts
>> c) 200 hosts
>
>> [|example] Group B
>> n) /28
>> o) /24
>> p) /30
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] The TTL field in an IPv4 header is increased by one at each router hop.
>> [!success]- Answer
>> False

> [!question] In the IPv4 header data starting with `45 00...`, what is the length of the header itself?
> a) 4 bytes
> b) 5 bytes
> c) 20 bytes
> d) 45 bytes
>> [!success]- Answer
>> c) 20 bytes

> [!question] Match the required number of subnets to the number of bits (`n`) that must be borrowed.
>> [!example] Group A
>> a) 2 subnets
>> b) 60 subnets
>> c) 550 subnets
>
>> [!example] Group B
>> n) 10 bits
>> o) 1 bit
>> p) 6 bits
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] The Fragment Offset value in an IPv4 header is measured directly in bytes.
>> [!success]- Answer
>> False

> [!question] Aggregating the routes `172.17.24.0/22` and `172.17.28.0/22` results in what summary route?
> a) `172.17.24.0/21`
> b) `172.17.24.0/23`
> c) `172.17.0.0/19`
> d) `172.17.32.0/21`
>> [!success]- Answer
>> a) `172.17.24.0/21`

> [!question] Match the field from an IPv4 header to its byte position (starting from 0).
>> [!example] Group A
>> a) Protocol
>> b) Time To Live (TTL)
>> c) Source IP Address
>
>> [!example] Group B
>> n) Byte 8
>> o) Bytes 12-15
>> p) Byte 9
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Two devices with the same subnet mask are on the same subnet if their IP addresses produce the same result after a bitwise AND operation with the mask.
>> [!success]- Answer
>> True

> [!question] A subnet requires 25 host addresses. What is the most efficient subnet mask to use?
> a) /26 (provides 62 hosts)
> b) /27 (provides 30 hosts)
> c) /28 (provides 14 hosts)
> d) /25 (provides 126 hosts)
>> [!success]- Answer
>> b) /27 (provides 30 hosts)

> [!question] An IP datagram is split into 3 fragments. Match the fragment to its correct MF (More Fragments) flag setting.
>> [!example] Group A
>> a) Fragment 1
>> b) Fragment 2
>> c) Fragment 3 (the last one)
>
>> [!example] Group B
>> n) MF = 1
>> o) MF = 0
>> p) MF = 1
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] FLSM (Fixed Length Subnet Masking) is generally more efficient in address allocation than VLSM.
>> [!success]- Answer
>> False

> [!question] User A is on the subnet `143.27.64.0/18`. Which of the following default gateways can User A legally use?
> a) `143.27.128.1`
> b) `143.27.63.254`
> c) `143.27.105.1`
> d) `143.28.0.1`
>> [!success]- Answer
>> c) `143.27.105.1`

> [!question] Match the IP address with the subnet it belongs to, using the mask `255.255.255.224` (`/27`) on the base network `204.15.5.0`.
>> [!example] Group A
>> a) `204.15.5.31`
>> b) `204.15.5.33`
>> c) `204.15.5.95`
>
>> [!example] Group B
>> n) Is the broadcast address for subnet `204.15.5.64`
>> o) Is the broadcast address for subnet `204.15.5.0`
>> p) Is a usable host address on subnet `204.15.5.32`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Route aggregation (supernetting) is used to break down a large network into smaller ones.
>> [!success]- Answer
>> False

> [!question] What is the defining characteristic of a Multicast MAC address?
> a) The first byte is `FF`.
> b) The Least Significant Bit (LSB) of the first byte is `0`.
> c) All bits in the address are set to `1`.
> d) The Least Significant Bit (LSB) of the first byte is `1`.
>> [!success]- Answer
>> d) The Least Significant Bit (LSB) of the first byte is `1`.

> [!question] Match the LAN size requirement to the necessary CIDR mask.
>> [!example] Group A
>> a) 1500 hosts
>> b) 500 hosts
>> c) 100 hosts
>
>> [!example] Group B
>> n) /23
>> o) /25
>> p) /21
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] To support a subnet with exactly 2 hosts (a point-to-point link), you need a mask of `/29`.
>> [!success]- Answer
>> False

> [!question] A network `172.16.0.0/20` is further divided using a `/22` mask. What is the increment or "block size" between the new, smaller subnets?
> a) An increment of 2 in the 4th octet
> b) An increment of 4 in the 3rd octet
> c) An increment of 8 in the 3rd octet
> d) An increment of 16 in the 4th octet
>> [!success]- Answer
>> b) An increment of 4 in the 3rd octet

> [!question] Match the IP header field to its description.
>> [!example] Group A
>> a) IHL (Internet Header Length)
>> b) Total Length
>> c) Flags
>
>> [!example] Group B
>> n) Contains bits like DF (Don't Fragment) and MF (More Fragments).
>> o) Specifies the length of the header in 4-byte words.
>> p) Specifies the length of the entire packet (header + data) in bytes.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] An IP address with the first octet of `241` is a Class D (Multicast) address.
>> [!success]- Answer
>> False

> [!question] A 4000-byte IP packet (including a 20-byte header) must be sent over a link with a 1500-byte MTU. What is the maximum data payload of the first fragment?
> a) 1500 bytes
> b) 1480 bytes
> c) 4000 bytes
> d) 3980 bytes
>> [!success]- Answer
>> b) 1480 bytes

> [!question] Match the IP address to its usability status.
>> [!example] Group A
>> a) `126.1.0.0`
>> b) `214.0.0.4`
>> c) `131.107.256.80`
>
>> [!example] Group B
>> n) Invalid (octet > 255)
>> o) Valid and Usable
>> p) Valid, but Not Usable (Network Address)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] The Protocol field value of `0x06` in an IPv4 header indicates the payload is UDP.
>> [!success]- Answer
>> False

> [!question] In an FLSM plan, a subnet requires 7 hosts but is allocated a `/27` block (30 usable IPs). What is the address utilization rate for this specific subnet?
> a) 23.3%
> b) 93.3%
> c) 100%
> d) 6.7%
>> [!success]- Answer
>> a) 23.3%

> [!question] Match the MAC address prefix (first byte) to its type using the hexadecimal shortcut.
>> [!example] Group A
>> a) `1A`
>> b) `0F`
>> c) `00`
>
>> [!example] Group B
>> n) Multicast (last hex digit is odd)
>> o) Unicast (last hex digit is even)
>> p) Unicast (last hex digit is even)
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)