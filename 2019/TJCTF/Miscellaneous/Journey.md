# Journey
### Forensics: 20 points
#### Solved by: Vermillion
```
Written by boomo

Every journey starts on step one

nc p1.tjctf.org 8009
```
I netcatted into the service:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567499203522330626/unknown.png'>

Pretty simple, we just have to return the last word back. Of course, this is a scripting challenge, similar to the one from SunshineCTF2019. I wrote up my script in python to do it for me, using pwntools:
```
from pwn import *
r = remote('p1.tjctf.org',8009)
for x in range(10000): #lots just in case, I can force quit Ctrl-C if necessary.
	data = r.recvuntil('\n') #receive until the newline character, only getting the first line (Encountered 'word')
	print data
	list = data.split()
	word = list[len(list)-1] #get the word
	word = word[1:-1] #remove quotation marks
	
	r.sendline(word)
```
After an OK runtime (Could have not printed unless it contained 'tjctf'), I got the flag:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567500416942866472/unknown.png'>

flag: `tjctf{an_38720_step_journey}`

Looks like it was only 38720 times. Also, the 'an' bothers me it should be 'a'.
