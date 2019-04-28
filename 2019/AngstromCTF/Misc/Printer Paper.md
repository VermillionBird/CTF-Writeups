## Printer Paper
### 150 points, 60 solves

`We need to collect more of defund's math papers to gather evidence against him. See if you can find anything in the `<a href='https://files.actf.co/1c24f3f479ccb20bb2c0169497a7e59e6e9962b03aa5e25ca4a054cd1f4e114b/printer_paper.pcapng'>data packets</a>` we've intercepted from his printer.`

`Author: defund`

Opening the file with Wireshark, we see several USB packets, showing that defund printed a paper from a USB. Most of the packets contain printer commands, which did not turn out to be important. However, there were 7 very large packets that contained the actual data to be printed:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572117456072736769/unknown.png'>

In USB protocols, the data is contained in Leftover Capture Data. The highlighted packet starts with '`,XQX`' which looks like a file header. I haven't seen it before, so I looked it up. It turned out to be XQX, which is a method of converting documents to a printer stream. 

I used <a href='http://foo2xqx.rkkda.com/'>foo2xqx</a>, which contained a tool to decode xqx streams to readable text. So first, I copied all of the raw data from the large packets, and concatenated them. I then used XQXdecode to decode the bytes into a .pbm file:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572120386536341624/unknown.png'>

And then opened the pbm file:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572120751713419304/unknown.png'>

flag: `actf{daniel_zhu_approves}`
