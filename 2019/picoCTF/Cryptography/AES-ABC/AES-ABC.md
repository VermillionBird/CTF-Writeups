# AES-ABC
## Points: 400
### Solved by: Vermillion
<br></br>
### Description

`AES-ECB is bad, so I rolled my own cipher block chaining mechanism - Addition Block Chaining! You can find the source here: `[aes-abc.py](aes-abc.py)`. The AES-ABC flag is `[body.enc.ppm](body.enc.ppm)

### Solve
The flag appears to be an [image](body.enc.ppm) that was encrypted. You can see some disturbance in the middle, which is probably where our flag will lie.

![](/Images/2019/picoCTF/body.enc.ppm.PNG)

From the description, it appears to be a unique method of chaining together AES encrypted blocks. AES encryption is a block cipher encryption method, meaning that it splits the original file into blocks of fixed length, and applies the encryption algorithm on each block. Without anything else, this is the Electronic CodeBook (ECB) mode. However, ECB is bad, as stated in the description, because the same block will output the same encrypted block. This can leave artifacts in the resulting encryption, as seen in the commonly used Tux example:

|Original|ECB|Desired Result (Other Modes)|
|----|----|----|
|![](https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg)|![](https://upload.wikimedia.org/wikipedia/commons/f/f0/Tux_ecb.jpg)|![](https://upload.wikimedia.org/wikipedia/commons/a/a0/Tux_secure.jpg)|

Cipher block chaining is used to create pseudorandomness in the encrypted file, as shown in the image on the right. This uses the encryption of the previous block to encrypt the current block, meaning that the encryption also depends on all the blocks being encrypted. Therefore, Cipher Block Chaining is much more secure. **This is only true, however, if the method of chaining is also secure.**

Let's open up the python program we are given. I'll go over it part by part. **Our goal is to find a way to revert the chaining to output an AES-ECB encrypted image, in which we will hopefully still be able to see the flag due to the artifacts.**

```
#!/usr/bin/env python

from Crypto.Cipher import AES
from key import KEY
import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))
```

As expected, it uses AES encryption. We don't know the key, but that won't be a problem. We just need the AES-ECB encrypted image, not the original. UMAX appears to be the maximum size a block can be. This probably refers to the color palette of 255 being the max for a color channel in a pixel.

```
def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded
```

This function takes in a byte in the form of an integer, and converts it to its equivalent raw format. It then pads the raw using zero padding (adds the necessary number of null bytes). It returns this padded raw.

```
def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]
```

This function has a comment, telling us that it returns the header line and the rest of the file. This will probably be used to preserve the `ppm` header format, which delineates the size of the image, among other things.

```
def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
```

Here we see it being put to use. ppm files have a 3 line header, so this will return the 3 line header and the actual image data.

```
def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (chr(padding) * padding)
```

This pads its input text using the [standard padding method](https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS#5_and_PKCS#7).

```
def aes_abc_encrypt(pt):
    cipher = AES.new(KEY, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt))

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
    iv = os.urandom(16)
    blocks.insert(0, iv)
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i+1].encode('hex'), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)

    ct_abc = "".join(blocks)
 
    return iv, ct_abc, ct
```

Here we finally get to the meat of the code: the actual encryption method. It encrypts the padded plaintext using AES-ECB. It splits the text into a list of blocks of 16 characters, and then initializes a random IV and inserts it at the front. Then the block chaining begins. 

```
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i+1].encode('hex'), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)
```

Ah. Each final block is the sum of the current encrypted block and the previous encrypted block modulo the maximum size a block can be as an integer. That's vulnerable. Typically, block chaining chains together the previous encrypted block with the current **plaintext** block, but here it uses the current **encrypted** block. This means that we have access to everything used in the chaining mechanism, so we can just write a function that will unchain it.

```
def un_abc(ct):
	blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
	
	for i in range(1, len(blocks)):
		curr = int(blocks[len(blocks)-i].encode('hex'), 16)
		prev = int(blocks[len(blocks)-i-1].encode('hex'), 16)

		n_curr_blk = curr - prev
		while n_curr_blk < 0:
			curr += UMAX
			n_curr_blk = curr - prev


		blocks[len(blocks)-i] = to_bytes(n_curr_blk)
	iv = blocks[0]

	notabc = "".join(blocks[1:])
 
	return iv, notabc
```
  
This was my solve function. It split the ciphertext into blocks, and undid the addition. This might result in a negative number due to the maximum size of a block, so we add the maximum until it isn't negative. Finally, we output the original ECB encrypted image.

Combining this with the other functions gives us our [solve script](deabc.py). Running it gives us our [output](out.ppm):

![](/Images/2019/picoCTF/out.ppm.PNG)

### Flag:
`picoCTF{d0Nt_r0ll_yoUr_0wN_aES}`
