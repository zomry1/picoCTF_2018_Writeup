# *net cat*

## Information
| Points |Category  | Level|
|--|--|--|
| 75 | General Skills |Easy |

## Challenge
> Using netcat (nc) will be a necessity throughout your adventure. Can you connect to `2018shell.picoctf.com` at port `22847` to get the flag?
### Hint

> nc [tutorial](https://linux.die.net/man/1/nc)
## Solution

> **netcat -** computer networking utility for reading from and writing to network
> connections using [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol") or [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol).

Let's connect thought netcat -
Open terminal -> nc 2018shell.picoctf.com 22847
* nc - stands for netcat 
	* command syntax:
		>   nc ADDRESS PORT
## Flag
> `picoCTF{NEtcat_iS_a_NEcESSiTy_69222dcc}`


