## Paper Bin
### 40 points, 373 solves

`defund accidentally deleted all of his math papers! Help recover them from his computer's `<a href='https://files.actf.co/ac4e8f7e16fb244613ffe42741046f98839e477e7a511d583dcc1bb291486029/paper_bin.dat'>raw data</a>`.`

`Author: defund`

Downloading the file, we can see the several pdf's file headers and trailers within the raw data (you can just cat the file to see this, or open it in a text editor). You could use dd to individually remove each pdf using the file headers and trailers, but it's a lot easier to use a tool. 

I used '`foremost -i paper_bin.dat -o paperbinoutput`' to do it; foremost is a tool that automatically tries to recover files from raw data. Looking at the audit, we successfully extracted 20 pdfs from the data. 

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571732448791232536/unknown.png'>

Now just enter the pdf folder, and look through each pdf. '`00011880.pdf`' was the pdf with the flag:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571733530376142869/unknown.png'>

flag: `actf{proof_by_triviality}`
