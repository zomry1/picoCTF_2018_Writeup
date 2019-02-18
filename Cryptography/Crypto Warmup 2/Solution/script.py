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
