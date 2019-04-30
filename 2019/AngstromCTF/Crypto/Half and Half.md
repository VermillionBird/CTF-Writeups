## Half and Half.md
### 

`Mm, coffee. Best served with `<a href='https://files.actf.co/9cefffa835c5a46d2e0daa1bec961ceb8574e35d37b966bc8b63e51a59509467/half_and_half.py'>half and half</a>`!`

`Author: defund`

The code:

```
from secret import flag

def xor(x, y):
	o = ''
	for i in range(len(x)):
		o += chr(ord(x[i])^ord(y[i]))
	return o

assert len(flag) % 2 == 0

half = len(flag)//2
milk = flag[:half]
cream = flag[half:]

assert xor(milk, cream) == '\x15\x02\x07\x12\x1e\x100\x01\t\n\x01"'
```

So we xor the first half of the flag with the second half of the flag, and we are given the result. The full hex of the result is `\x15\x02\x07\x12\x1e\x10\x30\x01\x09\x0a\x01\x22`

I used cyberchef to begin decrypting the xor. I first started the key as 'actf{' knowing that that is what the flag should start with. I then added underscores until the last character didn't change. My final key was 'actf{_______'

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572584464111239206/unknown.png'>

I tried the key 'tastes_____}' guessing that was the next letter. It gave me 'actf{co^VU^_', which if you notice, has the exact number of characters for 'actf{coffee_', and because of the description, that's what I guessed it would be.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572584935018332172/unknown.png'>

flag: `actf{coffee_tastes_good}`
