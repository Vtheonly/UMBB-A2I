---
sources:
  - "[[2.1 The IP Router]]"
  - "[[2.2 Routing Tables]]"
  - "[[2.3 Route Aggregation]]"
  - "[[2.4 Packet Forwarding Logic]]"
  - "[[2.5 Types of Routing]]"
---
> [!question] When a router de-encapsulates a frame, it strips the Layer 3 IP header to expose the Layer 2 Ethernet frame.
>> [!success]- Answer
>> False

> [!question] A router connects at least two different logical networks (subnets) and uses IP addresses to forward traffic.
>> [!success]- Answer
>> True

> [!question] If a router finds two routes with the exact same prefix length (subnet mask) for a destination, it uses Administrative Distance or Metrics as a tie-breaker.
>> [!success]- Answer
>> True

> [!question] Static routing consumes significant CPU resources and bandwidth because it constantly sends updates between routers.
>> [!success]- Answer
>> False

> [!question] The Administrative Distance (AD) for an internal EIGRP route is 90 by default.
>> [!success]- Answer
>> True

> [!question] Route Aggregation reduces the stability of the network because flapping links inside a summarized area cause updates to be sent to all external routers.
>> [!success]- Answer
>> False

> [!question] In the Routing Table, the code 'S*' represents a standard Static route that is not a default candidate.
>> [!success]- Answer
>> False

> [!question] The "Longest Prefix Match" rule states that the router prefers the route with the shortest subnet mask (e.g., /8 over /24).
>> [!success]- Answer
>> False

> [!question] For a directly connected route to appear in the routing table, the physical interface must be in an "Up/Up" state.
>> [!success]- Answer
>> True

> [!question] If a packet's TTL reaches 0, the router re-encapsulates it and sends it back to the source address.
>> [!success]- Answer
>> False

> [!question] Match the Routing Protocol with its default Administrative Distance.
>> [!example] Group A
>> a) Connected
>> b) EIGRP
>> c) OSPF
>> d) RIP
>
>> [!example] Group B
>> n) 90
>> o) 110
>> p) 0
>> q) 120
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)
>> d) -> q)

> [!question] Match the Routing Table Code with its meaning.
>> [!example] Group A
>> a) L
>> b) C
>> c) S
>> d) S*
>
>> [!example] Group B
>> n) Connected Network
>> o) Default Route (Route of Last Resort)
>> p) Local Interface IP (/32)
>> q) Static Route
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] Match the Packet Processing Step with the correct action.
>> [!example] Group A
>> a) Step 1
>> b) Step 3
>> c) Step 5
>
>> [!example] Group B
>> n) Encapsulation into new Layer 2 frame.
>> o) Decrement TTL by 1.
>> p) De-encapsulation of Layer 2 header.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the Route Aggregation Step with its description.
>> [!example] Group A
>> a) Binary Alignment
>> b) Count Matching Bits
>> c) Set Remaining Bits
>
>> [!example] Group B
>> n) Determines the new Prefix Length (CIDR).
>> o) Becomes the Summary Network Address (bits set to 0).
>> p) Write out networks in binary to find the pattern.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Routing Scenario to the correct Logic Selection (LPM).
>> [!example] Group A
>> a) Dest: 10.1.1.1 -> Route: 10.0.0.0/8
>> b) Dest: 10.1.1.1 -> Route: 10.1.1.0/24
>> c) Dest: 10.1.1.1 -> Route: 10.1.0.0/16
>
>> [!example] Group B
>> n) 3rd Priority Match (Shortest Prefix)
>> o) 2nd Priority Match
>> p) 1st Priority Match (Longest Prefix)
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] Match the Static Routing Pros/Cons to their description.
>> [!example] Group A
>> a) Pro: Secure
>> b) Pro: Resource Friendly
>> c) Con: Non-Adaptive
>> d) Con: High Maintenance
>
>> [!example] Group B
>> n) No CPU overhead or bandwidth for updates.
>> o) Topology is hidden; no advertisements sent.
>> p) Manual updates required for every router.
>> q) Traffic drops if a link breaks.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> q)
>> d) -> p)

> [!question] Match the Routing Entry Component to its description.
>> [!example] Group A
>> a) Next Hop (Remote)
>> b) Next Hop (Direct)
>> c) Net_ID
>
>> [!example] Group B
>> n) The exit interface (e.g., GigabitEthernet0/0).
>> o) The IP address of the next router.
>> p) The destination network address.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] Match the Dynamic Protocol with its type (as per the notes).
>> [!example] Group A
>> a) RIP
>> b) OSPF
>> c) EIGRP
>
>> [!example] Group B
>> n) Dynamic Protocol (AD 110)
>> o) Dynamic Protocol (AD 90)
>> p) Dynamic Protocol (AD 120)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Packet Drop Reason with the cause.
>> [!example] Group A
>> a) TTL = 0
>> b) No Route in Table
>> c) FCS Error
>
>> [!example] Group B
>> n) Packet corrupted at Layer 2.
>> o) Destination Unknown / ICMP Unreachable.
>> p) Loop prevention / ICMP Time Exceeded.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the Binary value to the Summary logic.
>> [!example] Group A
>> a) High Order Bits
>> b) Remaining Bits
>
>> [!example] Group B
>> n) Set to 0 to form the address.
>> o) Determine the common pattern (Mask).
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Which OSI Layer does an IP Router primarily operate at?
> a) Layer 1 (Physical)
> b) Layer 2 (Data Link)
> c) Layer 3 (Network)
> d) Layer 4 (Transport)
>> [!success]- Answer
>> c) Layer 3 (Network)

> [!question] What happens immediately after the router decrements the TTL?
> a) It checks if the TTL is greater than 0.
> b) It recalculates the header checksum.
> c) It consults the routing table.
> d) It encapsulates the packet.
>> [!success]- Answer
>> a) It checks if the TTL is greater than 0.

> [!question] Which route type has an Administrative Distance of 1?
> a) Connected
> b) Static
> c) EIGRP
> d) OSPF
>> [!success]- Answer
>> b) Static

> [!question] In the example of summarizing 10.2.1.0/24 through 10.2.4.0/24, what is the resulting subnet mask in dotted decimal format?
> a) 255.255.255.0
> b) 255.255.248.0
> c) 255.255.240.0
> d) 255.0.0.0
>> [!success]- Answer
>> b) 255.255.248.0

> [!question] What is the "Golden Rule" of Packet Forwarding Logic?
> a) Lowest Metric Match
> b) Longest Prefix Match
> c) Lowest Administrative Distance
> d) Highest Bandwidth Path
>> [!success]- Answer
>> b) Longest Prefix Match

> [!question] Which of the following is a specific advantage of Static Routing?
> a) It scales easily to large networks.
> b) It automatically reroutes traffic if a link fails.
> c) It is predictable and strictly follows the administrator's path.
> d) It requires less configuration time than dynamic routing.
>> [!success]- Answer
>> c) It is predictable and strictly follows the administrator's path.

> [!question] If a router receives a packet with Destination IP `192.168.1.57` and has routes for `192.168.1.0/24` and `192.168.1.48/28`, which route is chosen?
> a) 192.168.1.0/24 because it is a standard Class C.
> b) 192.168.1.0/24 because it has a lower metric.
> c) 192.168.1.48/28 because it has a longer prefix match.
> d) Neither, the packet is dropped.
>> [!success]- Answer
>> c) 192.168.1.48/28 because it has a longer prefix match.

> [!question] What does the command `show ip route` display?
> a) The current configuration of the router interfaces.
> b) The contents of the Routing Table in RAM.
> c) The ARP table mapping IP to MAC addresses.
> d) The status of the physical hardware.
>> [!success]- Answer
>> b) The contents of the Routing Table in RAM.

> [!question] What is the result of Route Aggregation on CPU processing?
> a) It increases CPU load due to complex calculations.
> b) It decreases CPU processing time due to faster lookups.
> c) It has no effect on CPU processing.
> d) It stops the CPU from processing routing updates entirely.
>> [!success]- Answer
>> b) It decreases CPU processing time due to faster lookups.

> [!question] If a destination IP does not match any specific route in the table, and there is no Default Route configured, what does the router do?
> a) Broadcasts the packet to all interfaces.
> b) Sends the packet to the ISP.
> c) Drops the packet and usually sends an ICMP Unreachable message.
> d) Holds the packet in a buffer until a route appears.
>> [!success]- Answer
>> c) Drops the packet and usually sends an ICMP Unreachable message.