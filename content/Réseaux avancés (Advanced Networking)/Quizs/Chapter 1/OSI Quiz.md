---
sources:
---
---
sources:
  - "[[Networking Protocols and Models]]"
---
> [!question] The primary problem that protocols solve in networking is the heterogeneity of hardware and software from different vendors.
>> [!success]- Answer
>> True

> [!question] A protocol is a strict set of rules that defines Format, Order, and Meaning of communication.
>> [!success]- Answer
>> True

> [!question] Which component of a protocol definition determines "what the data looks like" (headers, footers)?
> a) Format
> b) Order
> c) Meaning
> d) Timing
>> [!success]- Answer
>> a) Format

> [!question] Which component of a protocol definition determines "how to interpret the signals"?
> a) Format
> b) Order
> c) Meaning
> d) Syntax
>> [!success]- Answer
>> c) Meaning

> [!question] Match the Protocol definition component to its description.
>> [!example] Group A
>> a) Format
>> b) Order
>> c) Meaning
>
>> [!example] Group B
>> n) Who speaks first, initiation, and termination.
>> o) How to interpret the signals.
>> p) What the data looks like (headers/footers).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)

> [!question] The OSI model stands for "Open Systems Interconnection" and consists of 5 layers.
>> [!success]- Answer
>> False

> [!question] The OSI model is a theoretical reference model, while TCP/IP is the practical model used in the Internet.
>> [!success]- Answer
>> True

> [!question] Which mnemonic is used to remember the OSI layers from Bottom-Up?
> a) All People Seem To Need Data Processing
> b) Please Do Not Throw Sausage Pizza Away
> c) Please Do Not Touch Steve's Pet Alligator
> d) All Protocols Should Take Network Data
>> [!success]- Answer
>> b) Please Do Not Throw Sausage Pizza Away

> [!question] Match the OSI Layer Number to its Name.
>> [!example] Group A
>> a) Layer 7
>> b) Layer 4
>> c) Layer 3
>> d) Layer 1
>
>> [!example] Group B
>> n) Network
>> o) Physical
>> p) Application
>> q) Transport
>
>> [!success]- Answer
>> a) -> p)
>> b) -> q)
>> c) -> n)
>> d) -> o)

> [!question] Which OSI layer is responsible for logical addressing (IP) and routing?
> a) Data Link
> b) Network
> c) Transport
> d) Session
>> [!success]- Answer
>> b) Network

> [!question] Which OSI layer handles physical addressing (MAC) and error detection?
> a) Physical
> b) Network
> c) Data Link
> d) Presentation
>> [!success]- Answer
>> c) Data Link

> [!question] The Physical layer deals with the transmission of raw bits using voltages or light.
>> [!success]- Answer
>> True

> [!question] Match the OSI Layer to its specific function.
>> [!example] Group A
>> a) Presentation
>> b) Session
>> c) Transport
>> d) Application
>
>> [!example] Group B
>> n) Managing sessions (Start, Stop, Keep-alive).
>> o) Interface for the user.
>> p) Formatting, Encryption, Compression.
>> q) End-to-end delivery, Reliability, Flow Control.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] Which OSI layer provides services such as Encryption and Compression (JPEG, ASCII)?
> a) Application
> b) Presentation
> c) Session
> d) Transport
>> [!success]- Answer
>> b) Presentation

> [!question] The "PDU" for the Transport layer is called a Packet.
>> [!success]- Answer
>> False

> [!question] Match the OSI Layer to its Protocol Data Unit (PDU).
>> [!example] Group A
>> a) Transport
>> b) Network
>> c) Data Link
>> d) Physical
>
>> [!example] Group B
>> n) Packet
>> o) Bits
>> p) Segment
>> q) Frame
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] In the OSI model, what is the PDU at the Application, Presentation, and Session layers generally called?
> a) Segment
> b) Packet
> c) Data
> d) Stream
>> [!success]- Answer
>> c) Data

> [!question] The TCP/IP model condenses the OSI model into how many layers?
> a) 3
> b) 4
> c) 5
> d) 7
>> [!success]- Answer
>> b) 4

> [!question] Which three OSI layers are combined into the single TCP/IP "Application" layer?
> a) Application, Presentation, Session
> b) Application, Transport, Network
> c) Session, Transport, Network
> d) Presentation, Session, Transport
>> [!success]- Answer
>> a) Application, Presentation, Session

> [!question] Match the OSI Layer to the corresponding TCP/IP Layer.
>> [!example] Group A
>> a) Network
>> b) Data Link & Physical
>> c) Transport
>
>> [!example] Group B
>> n) Transport
>> o) Internet
>> p) Network Access
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Which of the following is a protocol found in the TCP/IP Internet layer?
> a) HTTP
> b) TCP
> c) IP
> d) Ethernet
>> [!success]- Answer
>> c) IP

> [!question] HTTP, DNS, and DHCP are protocols found in the Transport layer of the TCP/IP model.
>> [!success]- Answer
>> False

> [!question] Which layer in the TCP/IP model corresponds to the OSI Data Link and Physical layers?
> a) Internet
> b) Network Access
> c) Transport
> d) Hardware
>> [!success]- Answer
>> b) Network Access

> [!question] Encapsulation is the process of adding headers as data moves **down** the stack (from Application to Physical).
>> [!success]- Answer
>> True

> [!question] Decapsulation occurs at the Sender's side before transmission.
>> [!success]- Answer
>> False

> [!question] During Encapsulation, what happens at Layer 3 (Network Layer)?
> a) A MAC header is added to create a Frame.
> b) An IP header is added to create a Packet.
> c) The data is converted to bits.
> d) A TCP header is added to create a Segment.
>> [!success]- Answer
>> b) An IP header is added to create a Packet.

> [!question] Vertical Interaction means Layer N provides services to Layer N-1.
>> [!success]- Answer
>> False

> [!question] Horizontal Interaction describes how Layer N on the sender communicates logically with Layer N on the receiver.
>> [!success]- Answer
>> True

> [!question] Which process involves reading a header and removing it as data moves up the stack?
> a) Encapsulation
> b) Decapsulation
> c) Segmentation
> d) Fragmentation
>> [!success]- Answer
>> b) Decapsulation

> [!question] Match the Protocol to its standard Layer (TCP/IP or OSI equivalent).
>> [!example] Group A
>> a) SMTP
>> b) UDP
>> c) OSPF
>> d) Wi-Fi
>
>> [!example] Group B
>> n) Internet / Network
>> o) Network Access / Data Link
>> p) Application
>> q) Transport
>
>> [!success]- Answer
>> a) -> p)
>> b) -> q)
>> c) -> n)
>> d) -> o)

> [!question] In the OSI model, Layer 6 is the Session layer.
>> [!success]- Answer
>> False

> [!question] Which layer is responsible for flow control and reliability (TCP/UDP)?
> a) Network
> b) Transport
> c) Session
> d) Data Link
>> [!success]- Answer
>> b) Transport

> [!question] Routers primarily operate at which layer of the OSI model?
> a) Layer 2 (Data Link)
> b) Layer 3 (Network)
> c) Layer 4 (Transport)
> d) Layer 1 (Physical)
>> [!success]- Answer
>> b) Layer 3 (Network)

> [!question] Switches (that use MAC addresses) primarily operate at which layer of the OSI model?
> a) Layer 2 (Data Link)
> b) Layer 3 (Network)
> c) Layer 4 (Transport)
> d) Layer 5 (Session)
>> [!success]- Answer
>> a) Layer 2 (Data Link)

> [!question] The mnemonic "All People Seem To Need Data Processing" is used to remember the layers in Top-Down order.
>> [!success]- Answer
>> True

> [!question] Match the Data Unit to the Encapsulation Step (Sender side).
>> [!example] Group A
>> a) User Data + Layer 4 Header
>> b) Segment + Layer 3 Header
>> c) Packet + Layer 2 Header
>> d) Frame + Binary Encoding
>
>> [!example] Group B
>> n) Bits
>> o) Segment
>> p) Frame
>> q) Packet
>
>> [!success]- Answer
>> a) -> o)
>> b) -> q)
>> c) -> p)
>> d) -> n)

> [!question] Which attribute is NOT part of a protocol's definition?
> a) Manufacturer
> b) Format
> c) Order
> d) Meaning
>> [!success]- Answer
>> a) Manufacturer

> [!question] The Internet Layer in TCP/IP handles protocols like ICMP and ARP.
>> [!success]- Answer
>> True

> [!question] Which OSI layer manages the dialogue between computers (start/stop/keep-alive)?
> a) Transport
> b) Session
> c) Presentation
> d) Application
>> [!success]- Answer
>> b) Session

> [!question] In the context of Encapsulation, a "header" can be thought of as:
> a) The raw binary data.
> b) An envelope containing specific info for that layer.
> c) The physical cable connecting devices.
> d) The user interface.
>> [!success]- Answer
>> b) An envelope containing specific info for that layer.