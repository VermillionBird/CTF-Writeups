## I Like It
### 40 points, 611 solves

`Now I like dollars, I like diamonds, I like ints, I like strings. Make Cardi `<a href='https://files.actf.co/ced231db51437ed22dd7b244042135184436148b97cd16236bf0bc12f6139d5e/i_like_it'>like it</a>` please.`

`/problems/2019/i_like_it`

`Author: SirIan`

I downloaded the program and ran began analyzing it using gdb. I set a breakpoint at main, ran the program, and then viewed the assembly code. There appeared to be 2 inputs using fgets; I set a breakpoint at both of them (`b *main+59` and `b *main+165`). I continued the program at the first input, sending an input of test. I stepped through the function until I reached a function call to strcmp, a builtin c function. Luckily, the function was directly called using the expected string:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572208616740749382/unknown.png'>

So the first input should be 'okrrrrrrr'.

It then wants two integers, separated by a space at the next fgets. I inputted 1 and 2 for the time being.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572209065149595658/unknown.png'>

On lines 200 and 203 it moved my inputs to the registers RDX and RAX respectively, and then on line 206 it added the two and stored it in RAX. It then compares RAX with the expected 0x88, or 136. Therefore, our two numbers should add up to 136. 

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572210078703419402/unknown.png'>

I then re-ran it, passing in the two integers 36 and 100. After checking the sum, it reset RDX and RAX, then multiplied them together and checked it with 0xec7, or 3783. 

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572211153430904843/unknown.png'>

Therefore, we need to find two integers that add to 136 and multiply to 3783. The 2 numbers are 36 and 97, so that is what we should pass in. But in what order? The next few lines of code expect the first number to be less than the second:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572211354119962635/unknown.png'>

So our 2 numbers are 39 and 97. Running it normally nets us our flag:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572211768500289536/unknown.png'>

flag: `actf{okrrrrrrr_39_97}`
