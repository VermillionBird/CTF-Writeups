## One Bite
### 60 points, 523 solves

`Whenever I have friends over, I love to brag about things that I can eat in a single bite. Can you give `<a href='https://files.actf.co/697526f731d6484c6fc1066070b722e3a833bef6c3280fcbae1004083460e887/one_bite'>this program</a>` a tasty flag that fits the bill?`

`/problems/2019/one_bite`

`Author: SirIan`

Running the program, we see it asks for a flag, takes in your input, and outputs '`That didn't taste so good :(`' for an incorrect input. We open it in GDB and break at main, and look at the assembly. It has a strlen call, followed by a cmp, so `b *main+115` is a good start. It also actually calls strcmp, so I set a breakpoint there too: `b *main+147`:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572567734370697217/unknown.png'>

After the program reached the first strlen call, I began stepping. The post-comparison jump is '`jb`', which means that it jumps if rbx, which starts as 0, is less than rax, our string length. Of course, this jumps, and it jumps to a previous block of code it passed over the first time through: lines 74-98. This block seemed to encipher the first letter of my input.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572569492497104936/unknown.png'>

This enciphering process was actually a simple xor with 0x3c:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572571011355246592/unknown.png'>

It then hit the strlen function again, once again compared, and rbx was now 0x1. It jumped once again, and this time enciphered the second letter, and rbx became 0x2. This continued until every single character was enciphered, including the new line character. At the strcmp however, we see that it compares the enciphered string against a hard coded one, which is the correct flag.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572569997361283082/unknown.png'>

Since it was just a repeating single byte xor, it was easy to decode. I used <a href='https://cryptii.com'>this website</a>.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572571487773392907/unknown.png'>

flag: `actf{i_think_im_going_to_be_sick}`
