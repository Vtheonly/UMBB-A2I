---
sources:
  - "[[2.1 The IP Router]]"
  - "[[2.2 Routing Tables]]"
  - "[[2.3 Route Aggregation]]"
  - "[[2.4 Packet Forwarding Logic]]"
  - "[[2.5 Types of Routing]]"
---
> [!question] An IP Router operates at Layer 2 (Data Link Layer) and uses MAC addresses to forward packets between networks.
>> [!success]- Answer
>> False

> [!question] When a router receives a packet, it decrements the Time To Live (TTL) value by 1; if the value reaches 0, the packet is dropped.
>> [!success]- Answer
>> True

> [!question] In a routing table, a "Local" route (Code L) represents the specific /32 IP address assigned to the router's interface.
>> [!success]- Answer
>> True

> [!question] Administrative Distance is used to select the best path *before* the router checks for the Longest Prefix Match (LPM).
>> [!success]- Answer
>> False

> [!question] Route Aggregation (Summarization) increases the size of routing tables and increases bandwidth usage for updates.
>> [!success]- Answer
>> False

> [!question] For a "Connected" route to appear in the routing table, the interface must only be configured with an IP address; the link status does not matter.
>> [!success]- Answer
>> False

> [!question] Static routing is considered more secure than dynamic routing because it does not broadcast network topology advertisements.
>> [!success]- Answer
>> True

> [!question] If a router finds two routes to a destination, one with a /16 mask and one with a /24 mask, it will choose the /16 route because it covers more addresses.
>> [!success]- Answer
>> False

> [!question] A router acts as a Default Gateway, allowing hosts on a LAN to communicate with devices on different networks.
>> [!success]- Answer
>> True

> [!question] Dynamic routing protocols automatically detect link failures and recalculate paths, a process known as convergence.
>> [!success]- Answer
>> True

> [!question] Match the Routing Protocol Code with its source.
>> [!example] Group A
>> a) C
>> b) S
>> c) O
>> d) D
>
>> [!example] Group B
>> n) EIGRP
>> o) Connected
>> p) Static
>> q) OSPF
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> q)
>> d) -> n)

> [!question] Match the Router Action with its description in the packet processing flow.
>> [!example] Group A
>> a) De-encapsulation
>> b) Decision Making
>> c) Encapsulation
>
>> [!example] Group B
>> n) Strips the Layer 2 header to expose the packet.
>> o) Wraps the IP packet into a new Layer 2 frame.
>> p) Consults the Routing Table using Destination IP.
>
>> [!success]- Answer
>> a) -> n)
>> b) -> p)
>> c) -> o)

> [!question] Match the Administrative Distance (AD) to the Route Type.
>> [!example] Group A
>> a) Connected
>> b) Static
>> c) OSPF
>> d) RIP
>
>> [!example] Group B
>> n) 1
>> o) 120
>> p) 0
>> q) 110
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] Match the Route Aggregation concept with its benefit.
>> [!example] Group A
>> a) Efficiency
>> b) Stability
>> c) Traffic Reduction
>
>> [!example] Group B
>> n) Flapping links inside a summarized area do not affect external routers.
>> o) Fewer routing updates are sent between routers.
>> p) Smaller routing tables result in faster lookups.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Routing Logic step to its priority order (1 being first).
>> [!example] Group A
>> a) Check Longest Prefix Match (LPM)
>> b) Check Administrative Distance / Metric
>> c) Filter entries where network portion matches
>
>> [!example] Group B
>> n) Step 2 (Highest Priority Rule)
>> o) Step 3 (Tie-breaker only)
>> p) Step 1 (Initial Filter)
>
>> [!success]- Answer
>> a) -> n)
>> b) -> o)
>> c) -> p)

> [!question] Match the Static Routing characteristic to its classification (Pro or Con).
>> [!example] Group A
>> a) Non-Adaptive
>> b) Secure
>> c) High Maintenance
>> d) Resource Friendly
>
>> [!example] Group B
>> n) Pro (Advantage)
>> o) Con (Disadvantage)
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> o)
>> d) -> n)

> [!question] Match the binary values to the correct decimal subnet mask.
>> [!example] Group A
>> a) /24
>> b) /21
>> c) /16
>
>> [!example] Group B
>> n) 255.255.0.0
>> o) 255.255.255.0
>> p) 255.255.248.0
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the component of a Routing Entry to its definition.
>> [!example] Group A
>> a) Destination Network
>> b) Subnet Mask
>> c) Next Hop
>
>> [!example] Group B
>> n) Defines the size of the destination network.
>> o) The IP address of the next router in the path.
>> p) The network address (Net_ID) you want to reach.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] Match the Packet Outcome with the TTL Scenario.
>> [!example] Group A
>> a) TTL > 0
>> b) TTL reaches 0
>
>> [!example] Group B
>> n) Packet is dropped and ICMP "Time Exceeded" is sent.
>> o) Header checksum is recalculated and packet is forwarded.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the Routing Type with its primary mechanism.
>> [!example] Group A
>> a) Static Routing
>> b) Dynamic Routing
>> c) Default Route
>
>> [!example] Group B
>> n) Software protocols exchange network info.
>> o) Route of Last Resort (0.0.0.0/0).
>> p) Administrator manually types in routes.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] What is the primary function of an IP Router?
> a) To connect devices within the same network using MAC addresses.
> b) To forward packets between different logical networks (subnets).
> c) To assign IP addresses to hosts automatically.
> d) To encrypt all data passing through the network.
>> [!success]- Answer
>> b) To forward packets between different logical networks (subnets).

> [!question] Which command on Cisco devices displays the routing table?
> a) show ip interface brief
> b) show running-config
> c) show ip route
> d) ip route status
>> [!success]- Answer
>> c) show ip route

> [!question] When a router performs Route Aggregation, what happens to the bits remaining after the common pattern (Prefix Length) is determined?
> a) They are set to 1.
> b) They are set to 0.
> c) They remain unchanged.
> d) They are converted to hexadecimal.
>> [!success]- Answer
>> b) They are set to 0.

> [!question] According to the Packet Forwarding Logic, which route will be selected for destination IP `192.168.1.57`?
> a) 192.168.0.0 /16
> b) 192.168.1.0 /24
> c) 192.168.1.48 /28
> d) 0.0.0.0 /0
>> [!success]- Answer
>> c) 192.168.1.48 /28

> [!question] Why must the header checksum be recalculated by the router before forwarding?
> a) Because the Destination IP has changed.
> b) Because the Layer 2 header was stripped.
> c) Because the TTL value in the header was modified.
> d) Because the payload data was compressed.
>> [!success]- Answer
>> c) Because the TTL value in the header was modified.

> [!question] What is the "Route of Last Resort" formally known as?
> a) Static Route
> b) Dynamic Route
> c) Default Route (0.0.0.0/0)
> d) Connected Route
>> [!success]- Answer
>> c) Default Route (0.0.0.0/0)

> [!question] Which of the following is a disadvantage of Dynamic Routing?
> a) It is non-adaptive to link failures.
> b) It consumes CPU, RAM, and Bandwidth overhead.
> c) It requires manual updates for every new subnet.
> d) It cannot handle large networks.
>> [!success]- Answer
>> b) It consumes CPU, RAM, and Bandwidth overhead.

> [!question] In the context of Route Aggregation, what is the summarized route for `10.2.1.0/24`, `10.2.2.0/24`, `10.2.3.0/24`, and `10.2.4.0/24`?
> a) 10.2.0.0 /22
> b) 10.2.0.0 /21
> c) 10.2.0.0 /24
> d) 10.0.0.0 /8
>> [!success]- Answer
>> b) 10.2.0.0 /21

> [!question] What specific condition allows the router to break the "Longest Prefix Match" rule?
> a) When a static route has a lower metric.
> b) When the packet is encrypted.
> c) Never; Longest Prefix Match is the golden rule.
> d) When the destination is directly connected.
>> [!success]- Answer
>> c) Never; Longest Prefix Match is the golden rule.

> [!question] If a PC does not have a Default Gateway configured, what is the result?
> a) It cannot communicate with devices on its local LAN.
> b) It cannot communicate with devices on different networks.
> c) It will broadcast all traffic to the internet.
> d) It will automatically act as a router.
>> [!success]- Answer
>> b) It cannot communicate with devices on different networks.