# Moar Horse 2
### Forensics: 70 points
#### Solved by: Vermillion
```
Written by okulkarni
```
`Moar Horse is back and better than ever before! Check out this `<a href='https://moar_horse_2.tjctf.org/4b043a01-a4b7-4141-8a99-fc94fe7e3778.html'>site</a>` and see if you can find the flag. It shouldn't be that hard, right?`

Going to the site, we see a page with two buttons:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567453846503424020/unknown.png'>

When you click a button, you go to another identical page, except the url is different. I clicked through for a little while, and did not find anything. I decided to write a script that would pull all of the possible links using Python and BeautifulSoup:
```
import re
import mechanicalsoup
addresses=['/4b043a01-a4b7-4141-8a99-fc94fe7e3778.html']
browser = mechanicalsoup.StatefulBrowser()
i = 0
while i >= 0:
	try:
		page=addresses[i]
		browser.open("https://moar_horse_2.tjctf.org"+page)
		for link in browser.links():
			target = link.attrs['href']
			if target not in addresses:
				addresses.append(target)
		if len(addresses) == 10000:
			print 'oof'
		if len(addresses) == 32767: #32767 was the number I eventually reached as the maximum
			break
		i+=1
		print len(addresses),
	except:
		i = -1
print addresses
print len(addresses)
with open('address.txt', 'wb') as fil:
	for address in addresses:
		fil.write(address+'\n')
```
I then used bash to curl every single address in the `address.txt` that I wrote to:
```
for a in $(cat address.txt)
do
curl -s "https://moar_horse_2.tjctf.org${a}" #This line is unnecessary and will clutter up the output, but I kept it for debugging
curl -s "https://moar_horse_2.tjctf.org${a}" | grep "tjctf"
done
```
After a while of running, I eventually got the flag:

![](/Images/2019/TJCTF/moar.PNG)

flag: `tjctf{s0rry_n0_h0rs3s_anym0ar}`

This definitely was not the most efficient way to do this; if I had thought more I would have noticed that the pages formed a binary tree. I had noticed that when you cycled through enough pages, it looped back to the beginning, so the leaf of the binary tree loops back to the node. Knowing this, I could have made a search algorithm that was a lot more efficient.
