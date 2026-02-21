---
sources:
  - "[[MAC Addressing and Ethernet]]"
---
> [!question] A MAC address is a hierarchical address, similar to how a postal address works (Country -> City -> Street).
>> [!success]- Answer
>> False

> [!question] The Media Access Control (MAC) address is 48 bits in length.
>> [!success]- Answer
>> True

> [!question] The "Preamble" field in an Ethernet frame is used for error checking.
>> [!success]- Answer
>> False

> [!question] A MAC address with the value `01-00-5E-AB-CD-EF` can validly be used as a "Source Address" in an Ethernet frame.
>> [!success]- Answer
>> False

> [!question] If the data payload in an Ethernet frame is less than 46 bytes, padding is added to meet the minimum size requirement.
>> [!success]- Answer
>> True

> [!question] The Broadcast MAC address is represented as `FF-FF-FF-FF-FF-FF`.
>> [!success]- Answer
>> True

> [!question] In the OUI of a MAC address, if the "I/G Bit" is set to `1`, the address is a Unicast address.
>> [!success]- Answer
>> False

> [!question] The Ethernet Type field value `0x0806` indicates that the payload is an ARP packet.
>> [!success]- Answer
>> True

> [!question] The FCS (Frame Check Sequence) is located at the beginning of an Ethernet frame to alert the card that data is coming.
>> [!success]- Answer
>> False

> [!question] A "Universally unique" MAC address (burned-in) has the U/L bit set to `0`.
>> [!success]- Answer
>> True

> [!question] What is the length of the Organizationally Unique Identifier (OUI) portion of a MAC address?
> a) 12 bits
> b) 24 bits
> c) 32 bits
> d) 48 bits
>> [!success]- Answer
>> b) 24 bits

> [!question] Which field in the Ethernet frame is responsible for synchronization?
> a) SFD
> b) Preamble
> c) Type
> d) FCS
>> [!success]- Answer
>> b) Preamble

> [!question] How many hexadecimal digits make up a standard MAC address?
> a) 8
> b) 10
> c) 12
> d) 16
>> [!success]- Answer
>> c) 12

> [!question] Which bit in the first byte of a MAC address determines if it is Unicast or Multicast?
> a) The Most Significant Bit (MSB)
> b) The Least Significant Bit (LSB)
> c) The U/L Bit
> d) The Parity Bit
>> [!success]- Answer
>> b) The Least Significant Bit (LSB)

> [!question] Which of the following MAC addresses represents a Multicast address?
> a) `00-00-25-47-EF-CD`
> b) `00-01-4B-B4-A2-EF`
> c) `01-00-5E-AB-CD-EF`
> d) `FF-FF-FF-FF-FF-FF`
>> [!success]- Answer
>> c) `01-00-5E-AB-CD-EF`

> [!question] What is the function of the FCS field in an Ethernet frame?
> a) Defines the Layer 3 protocol
> b) Synchronizes the transmission
> c) Identifies the manufacturer
> d) Error checking (CRC)
>> [!success]- Answer
>> d) Error checking (CRC)

> [!question] What corresponds to the Ethernet Type `0x0800`?
> a) ARP
> b) IPv4
> c) IPv6
> d) RARP
>> [!success]- Answer
>> b) IPv4

> [!question] Which part of the MAC address is assigned by the IEEE?
> a) The NIC Controller
> b) The Padding
> c) The OUI
> d) The CRC
>> [!success]- Answer
>> c) The OUI

> [!question] What is the maximum size of the Data payload in a standard Ethernet frame (MTU)?
> a) 46 Bytes
> b) 1000 Bytes
> c) 1500 Bytes
> d) 65535 Bytes
>> [!success]- Answer
>> c) 1500 Bytes

> [!question] Why can't a Multicast address be used as a Source MAC address?
> a) Because Multicast addresses are 64 bits long.
> b) Because a source must always identify a specific, single device.
> c) Because Multicast addresses are reserved for the router only.
> d) Because they do not have an OUI.
>> [!success]- Answer
>> b) Because a source must always identify a specific, single device.

> [!question] Match the Ethernet Frame Field to its correct size in Bytes.
>> [!example] Group A
>> a) Dest MAC
>> b) Type/Len
>> c) FCS (CRC)
>> d) Preamble
>
>> [!example] Group B
>> n) 7 Bytes
>> o) 4 Bytes
>> p) 6 Bytes
>> q) 2 Bytes
>
>> [!success]- Answer
>> a) -> p)
>> b) -> q)
>> c) -> o)
>> d) -> n)

> [!question] Match the MAC Address concept to its definition.
>> [!example] Group A
>> a) MAC Address
>> b) OUI
>> c) NIC Controller
>
>> [!example] Group B
>> n) The last 24 bits, assigned by the vendor.
>> o) Unique identifier burned into the NIC.
>> p) The first 24 bits, identifying the Manufacturer.
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Special Bit in the OUI to its function.
>> [!example] Group A
>> a) I/G Bit = 0
>> b) I/G Bit = 1
>> c) U/L Bit = 0
>> d) U/L Bit = 1
>
>> [!example] Group B
>> n) Multicast/Broadcast
>> o) Locally administered
>> p) Unicast
>> q) Universally unique (Burned-in)
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> q)
>> d) -> o)

> [!question] Match the Address Type to the example provided.
>> [!example] Group A
>> a) Unicast
>> b) Broadcast
>> c) Multicast
>
>> [!example] Group B
>> n) `01-00-5E-xx-xx-xx`
>> o) `00-50-56-C0-00-08`
>> p) `FF-FF-FF-FF-FF-FF`
>
>> [!success]- Answer
>> a) -> o)
>> b) -> p)
>> c) -> n)

> [!question] Match the Ethernet Frame Field to its primary function.
>> [!example] Group A
>> a) Preamble
>> b) SFD
>> c) Type
>> d) Data
>
>> [!example] Group B
>> n) Start Frame Delimiter.
>> o) Indicates the Layer 3 protocol.
>> p) Synchronization.
>> q) The Payload (IP Packet).
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)
>> d) -> q)

> [!question] Match the binary value of the First Byte to the resulting Address Type (based on the LSB).
>> [!example] Group A
>> a) `0000 0001` (Hex 01)
>> b) `0000 0000` (Hex 00)
>> c) `0000 0011` (Hex 03)
>
>> [!example] Group B
>> n) Unicast
>> o) Multicast
>> p) Multicast
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)
>> c) -> p)

> [!question] Match the Ethernet Type Field (Hex) to the Protocol.
>> [!example] Group A
>> a) 0x0800
>> b) 0x0806
>
>> [!example] Group B
>> n) ARP
>> o) IPv4
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the Addressing Style to the Model.
>> [!example] Group A
>> a) Flat Addressing
>> b) Hierarchical Addressing
>
>> [!example] Group B
>> n) IP Address (Country -> City -> Street)
>> o) MAC Address (Social Security Number style)
>
>> [!success]- Answer
>> a) -> o)
>> b) -> n)

> [!question] Match the Frame Component to its location in the structure.
>> [!example] Group A
>> a) Preamble
>> b) FCS
>> c) Type
>
>> [!example] Group B
>> n) Located between Source MAC and Data.
>> o) Located at the very end of the frame.
>> p) Located at the very beginning of the frame.
>
>> [!success]- Answer
>> a) -> p)
>> b) -> o)
>> c) -> n)

> [!question] Match the specific Byte counts to the MAC address sections.
>> [!example] Group A
>> a) Total MAC Length
>> b) OUI Length
>> c) NIC Controller Length
>
>> [!example] Group B
>> n) 3 Bytes
>> o) 3 Bytes
>> p) 6 Bytes
>
>> [!success]- Answer
>> a) -> p)
>> b) -> n)
>> c) -> o)