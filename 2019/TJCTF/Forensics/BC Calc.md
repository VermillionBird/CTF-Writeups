# BC Calc
### Forensics: 80 points
```
Written by jfrucht25

This file was found in Evan Shi's 60 gb homework folder. What could he be up to? Figure out what the images mean in order to find out.
```
<a href='https://static.tjctf.org/00944da5e375c96c7aad39041063fe6d8186d18249bf90aedca0acddd6ee7c2a_logos.odt'>notAnime</a>
```
note: all letters in the flag are lowercase
```
Downloading the file, I noticed that it was an .odt file. A file with the .odt file extension is an OpenDocument Text Document file, where everything is formatted using an XML stylesheet. First thing I did was open the file normally, but because I was on a linux machine, I didn't have Microsoft Word, so I used Google Docs instead.

![](/Images/2019/TJCTF/tjctfbcalc.PNG)

The flag is right there. The blue circle is around the tiny right brace, which is where I got stuck looking for for a little while.

flag: `tjctf{knowurfiles}`

Really easy for an 80 point question. Apparently the intended solution was for you to analyze the xml file to figure out the order. You could've done this by unzipping the .odt file, but why do that when you can just let Google do it for you? ;)
