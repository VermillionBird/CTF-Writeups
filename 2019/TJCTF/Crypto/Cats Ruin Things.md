# Cats Ruin Things
### Forensics: 120 points
#### Solved by: Vermillion

`Written by etherlyt`

`My cat took over my computer and ruined everything. Or maybe, only half of everything?` <a href="https://static.tjctf.org/107853e7123432ac8e83abd6a39d326bbdbd1955dd3814fc9a27e33ee95184b2_rsa.py">source</a>

`nc p1.tjctf.org 8006`

Originally, the challenge did not come with a source, but I have no idea how you were supposed to solve it without the source. With the source though, it was pretty simple:
```
#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from os import urandom
import struct

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
def sign(m, key):
	p = key.p
	q = key.q
	e = key.e
	d = modinv(e, (p-1)*(q-1))
	dp = d%(p-1)
	dq = d%(q-1)+struct.unpack('i', urandom(4))[0]
	qInv = modinv(q, p)
	
	s1 = pow(m, dp, p)
	s2 = pow(m, dq, q)
	h = (qInv*(s1-s2))%p
	s = s2+h*q
	return [s, e, p*q, p, q]
	
	
f = open("flag.txt", 'r')
flag = f.read()

while True:
	press = int(raw_input("Pick an option \n [1] Sign a message [2] Verify your own signature [-1] Adios! \n"))
	key = RSA.generate(2048)
	h = SHA256.new()
	h.update(flag)
	fin = int(h.hexdigest(), 16)
	test = str(key.encrypt(fin, 'x')[0])
	if( press == -1 ):
		print("Hasta luego!")
		break
	elif( press == 1 or press == 2 ):
		mes = raw_input("Enter a message to be signed: ")
		h.update(mes)
		hashm = h.hexdigest()
		mes = int(hashm, 16)
		out = sign(mes, key)
		print("e: " + str(out[1]))
		print("N: " + str(out[2]))
		if( press == 2 ):
			print("p: " + str(out[3]))
			print("q: " + str(out[4]))
			print("hashed mes: " + str(hashm))
			insig = int(raw_input("What is your signature? "))
			if( int(insig) != out[0] ):
				print("Wrong!")
				continue
			else:
				print("Correct!")
				continue
		else:
			print("Here is your signature:")
			print(str(out[0]) + "\n\n" + "-^.^-_-^.^-_-^.^-_-^.^-_-^.^-_-^.^-_-^.^-_-^.^-_-^.^-_-^.^-" + "\n")
			#print(fin) #comment out
			check = raw_input("I heard you wanted to steal my treats. You aren't worthy unless you can decrypt " + test + ": ")
			if( int(fin) == int(check) ):
				print(flag)
			else:
				print("Better luck next time!")
			break
	print(" :( ")
	break
```
At first, it seems like an RSA challenge, but it's really not.

The things to notice are that when you decide a message, you append your message to the flag and encrypt it using SHA256. It then prints this hashed message if you choose the '2' option, so if you pass an empty string as your message, you get the hex digest of the SHA256 encrypted flag.

Keeping this in mind, you can see that in order to get the flag, you need to decrypt the variable '`test`', which is encrypted using RSA. However, test is '`fin`' encrypted, and '`fin`' is the hexdigest of the encrypted flag converted to an integer. And most importantly of all, when it checks your decryption, it checks your integer against '`fin`'. So it's really quite simple.

First, choose to '`Verify your own signature`' and enter an empty string as your message to be signed. Ignore all of the RSA stuff, and copy the '`hashed mes`'.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568120392565260317/unknown.png'>

Then, convert this hashed message to an integer from hex:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568120634287325203/unknown.png'>

Then send any integer back for '`What is your signature?`', select '`Sign a message`', enter anything as the message, and finally, paste the integer from the previous step into the decryption challenge:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568121419284873245/unknown.png'>

flag: `tjctf{cAts_4r3_d3vils_RSACRT}`
