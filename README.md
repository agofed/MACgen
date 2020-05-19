# MACgen
MACgen creates a mac address by randomly generating it.

## MACADDRESS

MAC address is compost of six octet.

<img src="https://render.githubusercontent.com/render/math?math=XX_{1}:XX_{2}:XX_{3}:XX_{4}:XX_{5}:XX_{6}">

Every octet has an hexadecimal value that represents a value between 0 and 255.

<img src="https://render.githubusercontent.com/render/math?math=XX_{n} \in [0,255]">

*Example B8:0E:20:1D:7D:34*

As mentioned early, each octet represents a value between 0 and 255 in hexadecimal value.

<img src="https://render.githubusercontent.com/render/math?math=B8_{16} = 184_{10} = 1011 1000_{2}">

### Global or local and unicast or multicast

![MAC-48_Address.svg](https://upload.wikimedia.org/wikipedia/commons/9/94/MAC-48_Address.svg)

The two less significant bit of the first octet show if the MAC address is universal or local and if it is unicast or multicast. Since the value of the octet is represented as hexadecimal, the bit wich determine the type are the 4 less significant ones. Instead, the 4 more significant  bit can take every value and don't interfere with the hexadecimal value.

<img src="https://render.githubusercontent.com/render/math?math=xxx0_{2}"> unicast

<img src="https://render.githubusercontent.com/render/math?math=xxx1_{2}"> multicast

<img src="https://render.githubusercontent.com/render/math?math=xx0x_{2}"> global

<img src="https://render.githubusercontent.com/render/math?math=xx1x_{2}"> locally

| Binary | Decimal | Hex | Global or locally | Unicast or multicast |
|--------|---------|-----|-------------------|----------------------|
| 0000   | 0       | 0   | global            | unicast              |
| 0001   | 1       | 1   | global            | multicast            |
| 0010   | 2       | 2   | locally           | unicast              |
| 0011   | 3       | 3   | locally           | multicast            |
| 0100   | 4       | 4   | global            | unicast              |
| 0101   | 5       | 5   | global            | multicast            |
| 0110   | 6       | 7   | locally           | unicast              |
| 0111   | 7       | 7   | locally           | multicast            |
| 1000   | 8       | 8   | global            | unicast              |
| 1001   | 9       | 9   | global            | multicast            |
| 1010   | 10      | A   | locally           | unicast              |
| 1011   | 11      | B   | locally           | multicast            |
| 1100   | 12      | C   | global            | unicast              |
| 1101   | 13      | D   | global            | multicast            |
| 1110   | 14      | E   | locally           | unicast              |
| 1111   | 15      | F   | locally           | multicast            |
