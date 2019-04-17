# Is This The Real Life
### Cryptography: 90 points
#### Solved by: Vermillion

`Written by etherlyt`

`...is this just fantasy?` <a href="https://static.tjctf.org/d31e48552820b36aaa806153940e7de027fd8b3f8e6131a957c17edd08bb715f_pubkey.txt">public key</a> <a href="https://static.tjctf.org/e581e273b60f17d142fa21c7d86a40cddcdf5887d8f692d91ee95eaef005e6f0_rsa.sage">rsagen</a>

The source code (rsagen) looked like this:
```
nbits = 512
e = 65537
flag = REDACTED
nlist = []

block = 0

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
        
for x in range(8):
	n = 0
	phi = 1
	#RSA pubkey gen
	while True:
		p = random_prime(2^floor(nbits/2)-1,lbound=2^floor(nbits/2-1),proof=False)
		q = random_prime(2^floor(nbits/2)-1, lbound=2^floor(nbits/2-1), proof=False)
		n = p*q
		phi = (p-1)*(q-1)
		d = modinv(e, (p-1)*(q-1))
		block = (d*e) % phi
		if gcd(phi,e) == 1:
			shield = 108.0
			n = ((shield.nth_root(2)+10).nth_root(3)-(shield.nth_root(2)-10).nth_root(3))/2
			break
	phi = int(str(phi)[:4]+str(phi)[::-1][:4])**ceil(n)
	nlist.append(phi)
modulus = random_prime(2^floor(nbits/2)-1,lbound=2^floor(nbits/2-1),proof=False)
cipher = [0]*len(flag)
for c in range(len(flag)):
	nm = str(int(bin(int(flag[c].encode('hex'),16)).replace('0b', '')))
	for b in range(len(nm)):
		cipher[c] += int(nm[b])*nlist[b]
	cipher[c] = cipher[c]*int(nm)
	cipher[c] = cipher[c]%modulus
for x in range(len(cipher)):
	cipher[x] = cipher[x]*block

print nlist
print cipher
```
It appears to have two parts to it. First, it generates a list of "phi's" if you will. These phi's are the first 4 letters and the last 4 letters of a phi generated from random phi's. It then encrypts each letter of a flag using a modified Knapsack encryption algorihm. In this algorithm, it takes the binary of each character and uses Knapsack with nlist (the phi's) as the key. It then multiplies by the binary, treating the binary string as an integer (e.g pretending 111 is one hundred and eleven). Finally, it takes the resulting number, moduluses by a random prime, and then multiplies it by '`block`', which is `(d*e) % phi`.

It's a lot to take in, so try and understand the code yourself.

Moving on, we're given nlist and the cipher text in 'public key':

```
nlist = [42798447, 60070844, 64372735, 50740679, 96064802, 42258424, 44356317, 77336984]
ct = [292296909762800, 215653060477940, 208434519524352, 292296909762800, 265338299876870, 338411113077906, 217961079953287, 344375715089844, 205288667438400, 16912457697000, 11315622010000, 341537164927645, 314135413320574, 169124576970000, 32145056144756, 344375715089844, 15964193777715, 292296909762800, 344375715089844, 388451782884159, 16912457697000, 26533829987687, 344375715089844, 150925396356060, 281783803794437, 87154851154764, 398222847250224]
```
Therefore, we can ignore the first part of the code. Now, we just have to crack the latter half. I spend a long time trying to figure out how to get the modulus and the block, until I realized two things:
<ol>
  <li>block = (d*e) % phi, which is just 1 in RSA.</li>
  <li>The random prime that is modulus is much too large to have any affect on the cipher integer. (I tried it using an online interpreter)</li>
</ol>
From here, the script is easy:
```
import string
dic = {}
ct = [292296909762800, 215653060477940, 208434519524352, 292296909762800, 265338299876870, 338411113077906, 217961079953287, 344375715089844, 205288667438400, 16912457697000, 11315622010000, 341537164927645, 314135413320574, 169124576970000, 32145056144756, 344375715089844, 15964193777715, 292296909762800, 344375715089844, 388451782884159, 16912457697000, 26533829987687, 344375715089844, 150925396356060, 281783803794437, 87154851154764, 398222847250224]
nlist = [42798447, 60070844, 64372735, 50740679, 96064802, 42258424, 44356317, 77336984]

#generate a dictionary with the encoded values of all alphanumeric characters + braces and underscores
chars = string.ascii_letters+string.digits + '{_}'
cipher = [0]*len(chars)
#Does the encryption algorithm for every possible character
for c in range(len(chars)):
	nm = str(int(bin(int(chars[c].encode('hex'),16)).replace('0b', ''))) #Get the binary value of each character
	for b in range(len(nm)):
		cipher[c] += int(nm[b])*nlist[b] #Knapsackify it
	cipher[c] = cipher[c]*int(nm) #Multiply it by the binary
	dic[cipher[c]] = chars[c] #Adds it to the dictionary in the form cipher:char

print dic
flag = ''
for num in ct:
	flag += dic[num] #Add each matching character to the flag string
print flag
```

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568128948634910761/unknown.png'>

flag: `tjctf{i_T40ugh7_1t_w43_RsA}`

So did I, etherlyt, so did I.
