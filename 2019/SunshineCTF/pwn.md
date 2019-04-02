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
