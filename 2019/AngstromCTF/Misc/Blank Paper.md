## Blank Paper
### 30 points, 660 solves

`Someone scrubbed defund's `<a href='https://files.actf.co/26e1d969c6a7c21d973a64a67f74ea2695ee5b8743cd8f20d9ccde665bbfd368/blank_paper.pdf'>paper</a>` too hard, and a few of the bytes fell off.`

`Author: defund`

Interestingly enough, most browsers and my pdf viewer automatically fix the pdf, so when you open it, the flag is right there. 

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571727456076300328/unknown.png'>

But for those interested in how the challenge was supposed to be solved or if it doesn't work for you, you can read on.

From the challenge description, it appears that a few of the bytes were supposed to be 'scrubbed off', so the pdf was supposed to not open properly. So open it in your favorite hex editor:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571729610232823808/unknown.png'>

It appears that the file header is incorrect, starting with the hex 00 00 00 00. Looks like those bytes really did get scrubbed off.

Using this <a href='https://www.garykessler.net/library/file_sigs.html'>site</a>, we find that the correct PDF file header is starts with '%PDF', exactly the four bytes we're missing (-1.5 describes the version). Filling in those bytes with the correct hex (25 50 44 46), the pdf should be fixed.

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571730063612051487/unknown.png'>

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571730366474485810/unknown.png'>

flag: `actf{knot_very_interesting}`
