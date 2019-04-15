# Broken Parrot
### Reversing: 40 points
#### Solved by: Vermillion
```
Written by evanyeyeye
```
`I found this annoying `<a href='https://static.tjctf.org/0f1a1fab0a0d186e591e138df30f96f25fbad7f3b6cd561d41ec43d5c90fa15d_parrot'>parrot</a>`. I wish I could just ignore it, but I've heard that it knows something special.`

Running the program, it appears to just take standard input and repeat it back to you. Knowing there must be more, I started analyzing it with gdb. I did the standard starting procedures that I use:
```
info functions
b main
r
disas
```

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567485522289754190/unknown.png'>

This specific section shows that after printing 'Say something to the parrot: ' and getting your response, it checks it to see if the length of your input, including the newline character, is 0x22 characters long, or 34 characters long. The newline and 'tjctf{}' take 8 characters, so there are 26 characters in between.

I set a breakpoint at this compare and ran the program with the payload 'tjctf{12345678901234567890123456}'. It passed the length check, so I continued stepping through the program. I noticed that the program compared my first letter t with a t from the stack:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567487220366180362/unknown.png'>

I set a breakpoint at this compare line (main+141), and continued through the function. Sure enough, it continued to check 'j', 'c', 't', 'f', and '{', but after that, continuing finished the echo.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567487825881071627/unknown.png'>

I then inputted the same payload, but after it compared '{', instead of continuing, I started stepping again. I noticed that at line main+113, it compares a location on the stack with 0x5. 'tjctf{' is 6 characters, so perhaps 0x5 refers to index 5, or '{', and if you finished comparing that, then it jumps. True to word, at main+117, it jumps. 

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567488893558063104/unknown.png'>

Continuing to step, I find another `cmp dl,al` line, and find that it expects the next character to be 3. I set a breakpoint at this line and remove the previous breakpoint for 'tjctf{'. I rerun the program, replacing the first character in my payload to become a 3 (tjctf{31234567890123456789012345}). I continue in this manner, slowly adding one character at a time. I then find that after "\_", it continues to echo.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567490014481481738/unknown.png'>

I once again step after the '\_', and find that it jumps once again (0x2 is 3 characters). Interestingly, I find that it compares the second character after '\_' next.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567490808241192980/unknown.png'>

Ignoring this, I change my payload to match the expected result, set the breakpoint, and continue until I get the string:
`tjctf{3d_?0n7_y0u_l34v3_m3_4l0n3}`

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567491458534342685/unknown.png'>

Maybe there's one final compare line that gets that missing character? Looking at the code, there indeed is:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567491865423642626/unknown.png'>

0x64 is the hex code for 'd', so that's the missing letter.

flag: `tjctf{3d_d0n7_y0u_l34v3_m3_4l0n3}`

Notes: There was a red herring flag as you stepped through the program or if you ran strings on it. The herring flag was: "tjctf{my_b3l0v3d_5qu4wk3r_w0n7_y0u_l34v3_m3_4l0n3}", and there are some similarities, taking the 3d from beloved, and from 0n7 on. And since d was compared using its hex code instead of a stack value, this program clearly compared your flag to some sections of this red herring, changing the w to a d.
