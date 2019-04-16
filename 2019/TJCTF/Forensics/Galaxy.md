# Galaxy
### Forensics: 20 points
#### Solved by: Vermillion
```
Written by rj9

I found this interesting picture in my astronomy textbook but I don't know whats special about it. Maybe a reverse image search will help.
```
<a href="https://static.tjctf.org/41862e5c8dd075d112756d754285a5e6218b6f270054a09a23735431b80de9fd_galaxy.png">galaxy</a>

Downloading the image and using <a href='https://tineye.com/'>TinEye</a> to reverse image search it as the description suggests returns a wikipedia page on Low Surface Brightness galaxies. The acronym for Low Surface Brightness is LSB, which is also the acronym for Least Significant Bit steganography. LSB involves changing the very last bit of each byte in an image to encode a message, since changing the very last bit has very little effect on the image.

Using <a href='https://github.com/zardus/ctf-tools/blob/master/stegsolve/install'>StegSolve</a>, I extracted the LSB to find the flag:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567835313045504030/unknown.png'>

flag: `tjctf{last_but_n0t_l3ast}`
