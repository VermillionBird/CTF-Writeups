# Reversing
Ooh boy, my worst area
<br>
<br>
## 50 points: Patches Punches
```
That moment when you go for a body slam and you realize you jump too far. Adjust your aim, and you'll crush this challenge!
```
<a href='http://files.sunshinectf.org/pwn/patches'>patches</a>
```
Author: soaspro
```
I first downloaded and ran it. Since this is reversing, I then used gdb to analyze the program. I saw that `main` was indeed a function, so I set a breakpoint at main.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/563506217654419476/unknown.png'>

Disassembling main gives us its machine code:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563506442116530176/unknown.png">

Looking at it I noticed these lines:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563506896674357261/unknown.png">

No matter what happens, it will always jump because `0x0` is never equal to `0x1`. Running the file and the description mentions jumping past the flag/too far, so perhaps this jump, which jumps us to near the end of the program, is the problem. Therefore, I set a breakpoint at this line, so that before it was called, the program stopped. Then, I jumped to `main+41` to skip over that line, and continued running from there.

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563507417371901972/unknown.png">

flag: `sun{To0HotToHanDleTo0C0ldToH0ld!}`
