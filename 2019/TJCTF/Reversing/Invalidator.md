# Invalidator
### Reversing: 70 points
#### Solved by: Vermillion
```
Written by evanyeyeye
```
`Come one, come all! I offer to you unparalleled convenience in getting your flags `<a href='https://static.tjctf.org/a70301566b55ac9766935950a79fbd88a58f0bc38aafa3c281dd94c737a9686e_invalidator'>invalidated</a>`!`

I would advise you to look over <a href='https://github.com/VermillionBird/CTF-Writeups/blob/master/2019/TJCTF/Reversing/Broken%20Parrot.md'>my writeup for Broken Parrot</a>, since Invalidator is similar and I will be skimming over some sections.

Running the program:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567494227680952340/unknown.png'>

Using my normal procedures for gdb, I find nothing of interest in the main function, except for a fake flag. But it calls a strcmp function, so I set a breakpoint there.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567494846390992925/unknown.png'>

Stepping through the function, it appears that it takes one character from my argument at a time and XORs it with two values from the stack. It then compares this value with an expected value. Therefore, I set a breakpoint at each XOR line and at the CMP line so I could reverse the XOR using an <a href='xor.pw'>online calculator</a> and converting the hex to ascii using <a href='https://www.rapidtables.com/convert/number/hex-to-ascii.html'>this iste</a>.
  
XOR 1:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567495844681482418/unknown.png'>

XOR 2:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567496136986984479/unknown.png'>

CMP (this breakpoint is unnecessary as EAX is the compare, so I removed this breakpoint later):

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567496349566631963/unknown.png'>

I ran the program, each time taking the two XOR values and the expected result and using the online calculator to get the original character. For instance:
```
Get values from GDB:
Char^4e^57=71
Use online calculator and xor 57 with 71:
char^4e=26
Use online calculator and xor 26 with 4e:
char=68
68 from hex to ascii is 'h'
```
I then added this letter to my flag. I would always try to guess the next letter or word to speed things up. I finally got the flag.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567497840176136200/unknown.png'>

flag: `tjctf{7h4nk_y0u_51r_0r_m4d4m3_v3ry_c00l}`

This was kinda tedious...
