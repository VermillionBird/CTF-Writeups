## Classy Cipher
### 20 points, 720 solves

`Every CTF starts off with a Caesar cipher, but we're more `<a href='https://files.actf.co/2e1940179916e0501fbba0de705a668e42646c916276d7a51ad6a2d2cc381720/classy_cipher.py'>classy</a>`.`

`Author: defund`

Code:

```
from secret import flag, shift

def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'
```

It's a ROT cipher with the full ascii character set. You could write a python program to find the shift amount, or you could use <a href='https://www.dcode.fr/rot-cipher'>this website</a> like I did.

The shift amount was 216 for the full ascii table, and the flag was found.

flag: `actf{so_charming}`
