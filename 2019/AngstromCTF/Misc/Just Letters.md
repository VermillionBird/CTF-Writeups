## Just Letters
### 60 points, 206 solves

`Hope you’ve learned the `<a href='https://esolangs.org/wiki/AlphaBeta'>alphabet</a>`!`
```
nc 54.159.113.26 19600

Author: derekthesnake
```
Netcatting into the service shows that the service is an AlphaBeta interpreter and that the flag is at the beginning of the allocated memory.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571817431350247424/unknown.png'>

Using the link they gave us, I tried to print the very first byte of memory. It appears that there are 5 registers, and the fifth one deals with memory commands. Since it starts as a memory pointer, I don't need to switch. 

I first need to set the pointer to 0 to point at the beginning of memory, and then set register 1 or 2 to the value at that memory pointer since I can manipulate those. Finally, I move that value to register 3 so I can print it to the screen (only register 3 values can be printed). Therefore, to print the first letter, I should use '`YGCL`'

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571818854599229440/unknown.png'>

And it works! Now I want to print the next bit of memory, so I would add an S after Y to to print the next byte of memory ('`YSGCL`'). I would then have to add another S for each byte. I didn't want to have to type that whole string myself, so I wrote a python script to generate a continuous line of code, and directly send it to the service:
```
from pwn import *
payload=''
for x in range(100):
	s = "S" * x
	payload += "Y"+s+"GCL"
r = remote('misc.2019.chall.actf.co', 19600) #was that address before challenge ended, now is 54.159.113.26
r.recv()
r.sendline(payload)
print r.recv()
``
<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571824279088267285/unknown.png'>

flag: `actf{esolangs_sure_are_fun!}`
