# *Crypto Warmup 2*
## Information
| Points |Category  | Level|
|--|--|--|
| 75 | Cryptography |Easy |

## Challenge

> Cryptography doesn't have to be complicated, have you ever heard of something called rot13? `cvpbPGS{guvf_vf_pelcgb!}`

### Hint
> This can be solved online if you don't want to do it by hand!
## Solution
So rot13 encryption? after google it, I found that it's really simple encryption,  

    For each letter in the plaintext:
	    replace this letter with the 13th letter after it
***In order to decrypt the ciphertext, we need to replace each letter with the 13th letter before it.**  

So I wrote a python script for this:
```python
ciphertext = "cvpbPGS{guvf_vf_pelcgb!}"
plaintext = ""

#Foreach char in the ciphertext
for char in ciphertext:
	#If the char is not a letter
	#=> Add it has is
	if not char.isalpha():
		plaintext += char
		continue
	
	#Get the 13th before letter
	newLetter = ord(char) - 13

	#If the letter is uppercase
	if char.isupper():
		#If now we below A 
		if newLetter < ord("A"):
			#=> Add 26 to complete circle of letters
			newLetter += 26
	#Else it's a lowercase letter and below a
	elif newLetter < ord("a"):
		#=> Add 26 to complete circle of letters
		newLetter += 26

	#Add the new letter to the plaintext
	plaintext += chr(newLetter)

print plaintext
```
So the script return the flag!
## Flag
> `picoCTF{this_is_crypto!}
`


