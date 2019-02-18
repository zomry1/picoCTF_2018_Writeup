
# *Caesar cipher 1*
## Information
| Points |Category  | Level|
|--|--|--|
| 150 | Cryptography |Easy |

## Challenge

> This is one of the older ciphers in the books, can you decrypt the [message](https://2018shell.picoctf.com/static/8b8d9e1fd4c9cd66facc3794d9c69175/ciphertext)? You can find the ciphertext in /problems/caesar-cipher-1_2_73ab1c3e92ea50396ad143ca48039b86 on the shell server

### Hint
> caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)
## Solution
So the ciphertext we got is:  

    picoCTF{payzgmuujurjigkygxiovnkxlcgihubb}  

we need to decrypt this, and all we know that the encryption is **Caesar cipher**.  
So after searching it in google I found that ROT13 we [discuss earlier](https://github.com/zomry1/picoCTF_2018_Writeup/tree/master/Cryptography/Crypto%20Warmup%202)  
it's a private case of Caesar cipher when the key is 13.  
  
In Caesar cipher the key can be between 0 to 25 and for each letter we   replace each letter with the key'th letter after it.    
In more formal representation the encryption is:  
![Encryption](https://wikimedia.org/api/rest_v1/media/math/render/svg/77b59c7a676a99610ddee4ffc305aa7f9cda3b1a)

  **x**  - the letter we want to encrypt
**n** - the key
**En(x)** - the ciphertext for n and x

And the decryption is just the reverse of this operation:  
![Decryption](https://wikimedia.org/api/rest_v1/media/math/render/svg/8ed607e0202ff8d35aa41559f846cac9d358a362)    
So I wrote a python script to try each valid key value for the ciphertext we got:  
```python

#For comments on this function look at "Crypto Warmup 2" challenge
def decryptor(key, ciphertext):
	plaintext = ""
	for c in ciphertext:
		newChar = ord(c)-key
		if newChar < ord("a"):
			newChar = newChar + 26
		plaintext += chr(newChar)
	return plaintext


ciphertext = "payzgmuujurjigkygxiovnkxlcgihubb"
#For each valid key value
for i in range(1,26):
	plaintext = decryptor(i,ciphertext)
	print "key is: ", i ,"text is: ", plaintext
	
```

*The results:*   
>key is:  1 text is:  ozxyflttitqihfjxfwhnumjwkbfhgtaa  
>key is:  2 text is:  nywxeksshsphgeiwevgmtlivjaegfszz  
>key is:  3 text is:  mxvwdjrrgrogfdhvduflskhuizdferyy  
>key is:  4 text is:  lwuvciqqfqnfecguctekrjgthycedqxx  
>key is:  5 text is:  kvtubhppepmedbftbsdjqifsgxbdcpww  
>**key is:  6 text is:  justagoodoldcaesarcipherfwacbovv**  
>key is:  7 text is:  itrszfnncnkcbzdrzqbhogdqevzbanuu  
>key is:  8 text is:  hsqryemmbmjbaycqypagnfcpduyazmtt  
>key is:  9 text is:  grpqxdllaliazxbpxozfmeboctxzylss  
>key is:  10 text is:  fqopwckkzkhzywaownyeldanbswyxkrr  
>key is:  11 text is:  epnovbjjyjgyxvznvmxdkczmarvxwjqq  
>key is:  12 text is:  domnuaiixifxwuymulwcjbylzquwvipp  
>key is:  13 text is:  cnlmtzhhwhewvtxltkvbiaxkyptvuhoo  
>key is:  14 text is:  bmklsyggvgdvuswksjuahzwjxosutgnn  
>key is:  15 text is:  aljkrxffufcutrvjritzgyviwnrtsfmm  
>key is:  16 text is:  zkijqweetebtsquiqhsyfxuhvmqsrell  
>key is:  17 text is:  yjhipvddsdasrpthpgrxewtgulprqdkk  
>key is:  18 text is:  xighouccrczrqosgofqwdvsftkoqpcjj  
>key is:  19 text is:  whfgntbbqbyqpnrfnepvcuresjnpobii  
>key is:  20 text is:  vgefmsaapaxpomqemdoubtqdrimonahh  
>key is:  21 text is:  ufdelrzzozwonlpdlcntaspcqhlnmzgg  
>key is:  22 text is:  tecdkqyynyvnmkockbmszrobpgkmlyff  
>key is:  23 text is:  sdbcjpxxmxumljnbjalryqnaofjlkxee  
>key is:  24 text is:  rcabiowwlwtlkimaizkqxpmzneikjwdd   
>key is:  25 text is:  qbzahnvvkvskjhlzhyjpwolymdhjivcc 

And as we can see, only the key 6 has a meaning so it's the flag
## Flag
> `picoCTF{justagoodoldcaesarcipherfwacbovv}
`


