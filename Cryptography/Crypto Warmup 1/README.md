


# *Crypto Warmup 1*

## Information
| Points |Category  | Level|
|--|--|--|
| 75 | Cryptography |Easy |

## Challenge

> Crpyto can often be done by hand, here's a message you got from a friend, `llkjmlmpadkkc` with the key of `thisisalilkey`. Can you use this [table](https://2018shell.picoctf.com/static/7e80900bd1afae76845553d895e271e1/table.txt) to solve it?.

### Hint
> -   Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
>-   Please use all caps for the message.
## Solution
So what we have here?
the ciphertext (encoded text) is:
`llkjmlmpadkkc`
the key is:
`thisisalilkey`
And we got this table:
![Table](https://i.imgur.com/xhQEzqN.png)

the legnth of each key and ciphertext is eqaul so probably for each char in the    plaintext (the original text) we use the char in the same index in our key and this gives us the ciphertext.
After some searching in google I found an encryption with the name **"[Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)"**  and the description of it look the same encryption we use here, and in this encryption they use the same table called "**[Vigenère square](https://en.wikipedia.org/wiki/Tabula_recta)**".

So for being lazy I just used [this site](https://www.dcode.fr/vigenere-cipher) in order to decrypt the ciphertext, and got the flag.

## Flag
> `picoCTF{secretmessage}`


