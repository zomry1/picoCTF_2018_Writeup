from base64 import b64encode, b64decode

cookie = 'Sj1vwoe8gNvq/I7UdyXTms8/T2+yPPiy4xuZQ33nktu/5eb+8Xl2pvLb9QKyIrnfaIhmGZmW3U5iq5M0LA7Fkg=='
#decrypt the 64base code
Dcookie =  b64decode(cookie)

#In order to work with the 10th char, make it a list (because string in python is immutable)
listCookie = list(Dcookie)

#ord - cast from char to number
#chr - cast from char to ascii
#Set the 10th char to be the XOR of him with "0" and XOR that with "1"
listCookie[10] = chr(ord(Dcookie[10])^ord("0")^ord("1"))

#join again the list to a string
Dcookie = "".join(listCookie)

#encode the string again as a 64base code
print b64encode(Dcookie)
