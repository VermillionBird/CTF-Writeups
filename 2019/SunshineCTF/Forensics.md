# Forensics Challenges
Oh boy, forensics. Look ma, I'm a real Sherlock Holmes.
<br>
<br>
## 100 points: Golly Gee Willikers
```
Someone sent me this weird file and I don't understand it. It's freaking me out, this isn't a game! Please help me figure out what's in this file.
```
<a href='http://files.sunshinectf.org/forensics/golly_gee_willikers.txt'>golly_gee_willikers.txt</a>
```
Author: hackucf_kcolley
```
I spent a while searching up Golly Gee Willikers, which of course didn't return anything. But searching something else certainly does; open the text file to see:
```
x = 0, y = 0, rule = B3/S23
3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob
3ob3ob3ob3ob3ob3ob3ob3ob3o$obobobobobobobobobobobobobobobobobobobobobo
bobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobo
bobobobobob3o$obobobobobobobobobobobobobobobobobobobobobobobobobobobob
obobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobob3o
$obobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobobo
bobobobobobobobobobobobobobobobobobobobobobobobobobobob3o$3ob3ob3ob3ob
3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob3ob
3ob3ob3ob3ob3o$$5bo2bobobobo2b2obo3b2o3bo4bobo3bobo19bo2b2o2bo2b2o2b2o
2bobob3o2b2ob3ob3ob3o11bo5bo3b3o$5bo2bobob3ob2o4bob2o3bo3bo3bo3bo3bo
16bobobob2o4bo3bobobobo3bo5bobobobobo2bo3bo3bo2b3o2bo4bo$5bo6bobo2b2o
2bo2b3o6bo3bo2bobob3o5b3o6bo2bobo2bo3bo3bo2b3ob2o2b3o2bo2b3ob3o9bo9bo
2bo$12b3ob2o2bo3bobo6bo3bo7bo3bo10bo3bobo2bo2bo5bo3bo3bobobobo3bobo3bo
2bo3bo3bo2b3o2bo$5bo6bobo2bo4bo2b2o7bobo11bo8bo2bo3b2o3bo2b3ob2o4bob2o
2b3obo3b3ob2o6bo5bo5bo4bo$$bo3bo2b2o3b2ob2o2b3ob3o2b2obobob3o3bobobobo
3bobobobo2bo2b2o3bo2b2o3b2ob3obobobobobobobobobobob3ob3o5b3o2bo$obobob
obobobo3bobobo3bo3bo3bobo2bo4bobobobo3b3ob3obobobobobobobobobo4bo2bobo
bobobobobobobobo3bobo3bo5bobobo$3ob3ob2o2bo3bobob3ob3ob3ob3o2bo4bob2o
2bo3b3ob3obobob2o2bobob3o2bo3bo2bobobobob3o2bo3bo3bo2bo4bo4bo$o3bobobo
bobo3bobobo3bo3bobobobo2bo2bobobobobo3bobob3obobobo3b3ob2o4bo2bo2bobo
2bo2b3obobo2bo2bo3bo5bo3bo$b2obobob2o3b2ob2o2b3obo4b2obobob3o2bo2bobob
3obobobobo2bo2bo4b2obobob2o3bo3b2o2bo2bobobobo2bo2b3ob3o5b3o5b3o$$o7bo
9bo7bo5bo4bo4bobo3b2o31bo27b2o2bo2b2o3b2ob3o$bo2b2o2b2o3b2o2b2o2b2o2bo
3b2ob2o10bobo2bo2b3ob2o3bo2b2o3b2o2b2o2b2ob3obobobobobobobobobobob3o2b
o3bo3bo2b2o2b3o$5b2obobobo3bobobobob3obobobobo2bo4bob2o3bo2b3obobobobo
bobobobobo3b2o3bo2bobobobob3o2bo2bobo2b2obo9bo5b3o$4bobobobobo3bobob2o
3bo2b3obobo2bo4bob2o3bo2b3obobobobobobobobobo4b2o2bo2bobob3ob3o2bo3b2o
b2o3bo3bo3bo6b3o$4b3ob2o3b2o2b2o2b2o2bo4bobobo2bo2bobobobob3obobobobo
2bo2b2o3b2obo3b2o3b2o2b2o2bo2b3obobo3bob3o2b2o2bo2b2o6b3o$29bo11bo22bo
5bo30bo!$$$$13b2o2bo2bo4bo15b2o6bo6b2o11bo2b2o$b2obobob2o3bo2b3ob2o2b2o
3b2o5bobobobob2o2b3o6bo2b2o3b2ob3o2bo$2o2bobobobobo4bo2bobo2bo2b2o6b3o
bobobobo2bo7bo3b2ob2o3bo4bo$b2obobobobo2bo3bo2bobo2bo3b2o5b3obobobobo
2bo7bo2bobo2b2o2bo3bo$2o3b2obobo2b2o2b2obobo2bo2b2o2b3ob3ob2o2bobo2b2o
b3ob3ob3ob2o3b2ob2o!
```
This isn't crypto, so its not encryption. I searched up the first line, since it seemed distinct. Google outputs a Wikipedia page on cellular automata, and states that B3/S23 is a rule for Conway's Game of Life. I've messed around with Conway's Game of Life before, but haven't seen this kind of text. I scanned through the article to find <a href='https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Notable_programs'>this</a>.

Golly turns out to be a program for running Conway's Game of Life. I downloaded <a href='http://golly.sourceforge.net/'>Golly</a>, but you don't have to. There's actually a <a href='copy.sh/life'>website</a> for it. I pasted the entire text into Golly, and it turned out to just be a bunch of characters. I ran the simulation, and nothing seemed to come out of it. So there has to be more than that.

At this point, I had learned that the text was a Run Length Encoded file for Golly/Game of Life. So I decided to search up the way that Game of Life files are encoded using RLE. I found this <a href='http://www.conwaylife.com/wiki/Run_Length_Encoded'>website</a>, which helped me understand what each character did in the text. Most notably, the website says:

`The last <run_count><tag> item is followed by a ! character.` and `Anything after the final ! is ignored.`

If you notice, there's two exclamation points at the end of the text: `5bo30bo!$$$$13b...b2ob2o!`. Copypaste the code after the first '`!`', making sure to keep the first line '`x = 0, y = 0, rule = B3/S23`', and you'll get the flag:

![](/Images/2019/SunshineCTF/Golly.PNG)

flag: sun{th1s_w0nt_last}
<br>
<br>
<br>
## 150 points: Castles
```
The flag might be in another castle.
```
<a href='http://files.sunshinectf.org/forensics/Castles.001'>http://files.sunshinectf.org/forensics/Castles.001</a>
```
Note: The flag is in flag{} format
```
Solved this one prehint too. Yay me.

I first downloaded the file. Mounting it gives you four jpeg images. Nothing interesting there.
TBC
<br>
<br>
<br>
## 250 points: Sonar
```
We think a wrestler called Sonar wants to rebrand and go to a competitor. We have to reason to believe that he was sending them his new wrestling name, lucky that our next-gen firewall was capturing the traffic during the time where he sent that info out. Unfortunately our staff cannot make heads or tails of it. Mind looking at it for us?
```
<a href='http://files.sunshinectf.org/forensics/sonar.pcapng.gz'>sonar.pcapng.gz</a>
```
Author: aleccoder
```
Darn. I didn't get this one during the challenge perse, but I definitely could've. Download the pcapng and open it in Wireshark. You don't need to unzip it.

![](/Images/2019/SunshineCTF/wireshark.PNG)

It's a pretty big file, so I decided to look at the protocols:

![](/Images/2019/SunshineCTF/prothier.PNG)

I got fixated on the Internet Group Management Protocol, since it had the least packets sent. I even confirmed this with an admin, so I looked through the IGMP files, but didn't find anything at all. So I gave up there. But guess what? When I asked the admin, I shortened it to IGMP, and the admin thought I meant ICMP. After the competition, I found that out real fast.

![](/Images/2019/SunshineCTF/darn.PNG)

RIP. To be fair, ICMP also had one of the lower number of packets. So uh, maybe I shouldn't have given up. Continuing on, filtering by ICMP gives us:

![](/Images/2019/SunshineCTF/icmp.PNG)

Notice something? The data is just random characters. Why would that be? Unless, it has something to do with the data length...

In the image above, the packet I've highlighted has a data length of 115 bytes and a total length of 165 bytes. The next unique data length, since there are groups of consecutive packets with the same data length, is 117 with a total length of 167 bytes. Then it was 110 bytes/160 bytes, followed by 123bytes/173 bytes. 

`115 117 110 123`...Why that's the ascii codes for `sun{`! I recognized that immediately, and since the total length is just the data length plus 50, I started recording down all the ascii codes:
`115, 117, 110, 123, 055, 085, 099, 072, 097, 095, 076, 049, 066, 114, 051, 125`.
Using this <a href='http://www.unit-conversion.info/texttools/ascii/'>website</a>, I converted it to text and got:

flag: `sun{7UcHa_L1Br3}`

Darn, could've gotten 250 more points.
<br>
<br>
<br>
## 250 points: We Will We Will
```
Hey we found this SD card in one of wrestlers' Rubix™ cubes but we can't make heads or tails of it. Maybe you can figure out what's in it...
```
<a href='http://files.sunshinectf.org/forensics/WeWill.img'>WeWill.img</a>
```
Author: Aleccoder
```
Okay, so I'm really mad about this one. You'll see why in time, but just know that I deserved 250 more points.

Download the image, and try to mount it. You'll find that it's password protected. Looks like its a hashcat bashing problem. To be honest, I didn't know all too much about hashcat, so I followed this handy little <a href='https://articles.forensicfocus.com/2018/02/22/bruteforcing-linux-full-disk-encryption-luks-with-hashcat/'>tutorial</a>, specifically the 4th part where it mentions hashcat. Luckily, all my information was the same as theirs. Following it gets me:

<img src='https://media.discordapp.net/attachments/561665413918883840/562063531764350986/unknown.png?width=681&height=755'>

Oops. Something's wrong. Luckily, I found the answer pretty quickly; I just added a `--force` option to the end, and it started running. But uh...I'm running on a VM so this happened:

<img src='https://media.discordapp.net/attachments/555118456593317910/562087763378438146/unknown.png'>

That was 3 minutes after the competition ended. And it still took another 8 hours or so. Darn.

<img src='https://media.discordapp.net/attachments/555118456593317910/562223026851020800/unknown.png'>

The morning after the competition ended, I got the password: `filosofia`. And opening the file with that password gets you:

![](/Images/2019/SunshineCTF/darnit.PNG)

flag: `SUN{wrasslin}`

Yeah, so you can tell I'm mad.
<br>
<br>
<br>
