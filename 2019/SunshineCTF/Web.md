# Web Challenge
Lots of wrestlers. nice.
<br>
<br>
## 100 points: WrestlerBook
```
WrestlerBook is the social network for wrestlers, by wrestlers. WrestlerBook is exclusively for wrestlers, so if you didn't get an invite don't even bother trying to view our profiles.
```
<a href="http://archive.sunshinectf.org:19006">http://archive.sunshinectf.org:19006</a>
```
Author: dmaria
```
Opening the website:

![](/Images/2019/SunshineCTF/WrestlerBook.PNG)

It's a simple login screen, and being a basic web challenge, it's probably SQLi (SQL injection). First thing I do is try to login using '`' or '1'='1`' as both the username and the password. It works, but all you get is this:

![](/Images/2019/SunshineCTF/hulkhogie.PNG)

Looks like its going to be a bit more work than I thought. However, looking at the user info, there appears to be a flag section that's just empty for this user. Perhaps '`flag`' is a column in the database. I used the LIKE operator to test for an entry that contains '`sun`'. My payload therefore becomes:

username: `' or flag LIKE '%sun%' or '1'='2`

password: `' or '1'='2`

The `'1'='2` part of each section allows me to incorporate the ending quote while not afecting the query. My payload worked:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563510097884741642/unknown.png">

flag: `sun{ju57_4n07h3r_5ql1_ch4ll}`
<br>
<br>
<br>
## 150 points: Wrestler Name Generator
```
Even better than the Wu-Tang name generator, legend has it that Hulk Hogan used this app to get his name.
```
<a href='http://archive.sunshinectf.org:19007'>http://archive.sunshinectf.org:19007</a>
```
Author: dmaria
```
TBA
<br>
<br>
<br>
## 150 points: Portfolio
```
Check out my development portfolio! I'm just getting started, so don't be too mean :(
```
<a href='http://archive.sunshinectf.org:19009'>http://archive.sunshinectf.org:19009</a>
```
Author: dmaria
```
TBA
<br>
<br>
<br>
## 300 points: Enter the Polygon 1
```
These photos are The Best There Is, The Best There Was and The Best There Ever Will Be. Give me your photos I'll EXAMINE if they meet the bar.
```
<a href='http://img.sunshinectf.org'>http://img.sunshinectf.org</a>
```
Author: Astor
```
TBA
<br>
<br>
<br>
## 300 points: Enter the Polygon 2
TBA
