## Exercise 03: IP Address Classification

> [!Note] For the list of IP addresses in the large table, determine if each is valid and usable, and if so, find its class, network/host portions, network address, and broadcast address.

### 1. Solution According to the Notes

The notes contain a table that correctly categorizes each address. The logic applied is sound:

- **Validity:** Checks if octets are within the `0-255` range. `131.107.256.80` is correctly marked invalid.
- **Usability:** Correctly identifies special addresses:
  - `127.1.1.1` as Loopback.
  - `255.255.255.255` as Broadcast.
  - `198.121.254.255` as the broadcast for its specific network.
  - `126.1.0.0` as a network address.
  - Class D (`231...`) and E (`248...`) addresses as unusable for hosts.
- **Class/Network/Host Parts:** For usable addresses, the class is determined from the first octet, and the N/H split is applied correctly (e.g., Class B `191.48.54.100` has network part `191.48`).
- **Network/Broadcast Addresses:** These are derived perfectly by setting the host bits to all `0`s or all `1`s, respectively.

### 2. Formal, Detailed Solution

#### Essential Background Knowledge

**IP Address Classes (Classful Addressing):** This is a historical system for allocating IP addresses. The class is determined by the first octet and defines the default network mask.

| Class | First Octet Range | Default Mask        | Structure                    |
| :---: | :---------------- | :------------------ | :--------------------------- |
| **A** | 1 - 126           | 255.0.0.0 (/8)      | Network.Host.Host.Host       |
| **B** | 128 - 191         | 255.255.0.0 (/16)   | Network.Network.Host.Host    |
| **C** | 192 - 223         | 255.255.255.0 (/24) | Network.Network.Network.Host |
| **D** | 224 - 239         | N/A                 | Multicast                    |
| **E** | 240 - 255         | N/A                 | Experimental                 |

**Address Usability Rules:** An address cannot be assigned to a standard host (like a PC) if it is:

1.  **Invalid:** An octet is outside the 0-255 range.
2.  **Loopback:** The `127.0.0.0/8` block is reserved for self-testing.
3.  **A Network Address:** The first address in a range (all host bits are 0).
4.  **A Broadcast Address:** The last address in a range (all host bits are 1).
5.  **Multicast/Experimental:** Belongs to Class D or E.

#### Detailed Analysis Table

| IP Address        | Valid/Usable?         | Reasoning                                                      | Class | Network Part  | Host Part   | Network Address | Broadcast Address |
| :---------------- | :-------------------- | :------------------------------------------------------------- | :---- | :------------ | :---------- | :-------------- | :---------------- |
| `131.107.256.80`  | **Invalid**           | The third octet `256` is greater than 255.                     | -     | -             | -           | -               | -                 |
| `127.1.1.1`       | **Valid, Not Usable** | Reserved for Loopback. Used for a machine to ping itself.      | A     | `127`         | `1.1.1`     | `127.0.0.0`     | `127.255.255.255` |
| `255.255.255.255` | **Valid, Not Usable** | The "Limited Broadcast" address.                               | E     | -             | -           | -               | -                 |
| `214.0.0.4`       | **Valid & Usable**    | A standard host address.                                       | C     | `214.0.0`     | `4`         | `214.0.0.0`     | `214.0.0.255`     |
| `222.222.255.222` | **Valid & Usable**    | A standard host address.                                       | C     | `222.222.255` | `222`       | `222.222.255.0` | `222.222.255.255` |
| `198.121.254.255` | **Valid, Not Usable** | This is the broadcast address for the `198.121.254.0` network. | C     | `198.121.254` | `255`       | `198.121.254.0` | `198.121.254.255` |
| `132.4.0.5`       | **Valid & Usable**    | A standard host address.                                       | B     | `132.4`       | `0.5`       | `132.4.0.0`     | `132.4.255.255`   |
| `248.5.10.156`    | **Valid, Not Usable** | Belongs to Class E (Experimental). Reserved for future use.    | E     | -             | -           | -               | -                 |
| `231.200.1.1`     | **Valid, Not Usable** | Belongs to Class D (Multicast). Used to address groups.        | D     | -             | -           | -               | -                 |
| `10.4.200.200`    | **Valid & Usable**    | A standard host address.                                       | A     | `10`          | `4.200.200` | `10.0.0.0`      | `10.255.255.255`  |
| `126.1.0.0`       | **Valid, Not Usable** | This is the network address for the `126.0.0.0` network.       | A     | `126`         | `1.0.0`     | `126.0.0.0`     | `126.255.255.255` |
| `191.48.54.100`   | **Valid & Usable**    | A standard host address.                                       | B     | `191.48`      | `54.100`    | `191.48.0.0`    | `191.48.255.255`  |

---
