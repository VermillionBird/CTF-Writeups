## Streams
### 70 points, 61 solves

`White noise is useful whether you are trying to sleep, relaxing, or concentrating on writing papers. Find some natural white noise `<a href='https://streams.2019.chall.actf.co/'>here</a>`.`

`Note: The flag is all lowercase and follows the standard format (e.g. actf{example_flag})`

`Author: ctfhaxor`

Opening the website, we see a video:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572128486500859914/unknown.png'>

Looking at the source code, we can see the original mp4:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572128574752948225/unknown.png'>
  
However, going to the mp4 shows us not an mp4 file, but some xml:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572128656659447882/unknown.png'>
  
It is a MPD manifest, which divides the data into sections, like video, subtitles, audio, etc. The browser can then display the correct parts by pulling the data from the URLs it gives. Here, we can see that there are 2 audio Adaptation Sets. The second one has a Representation ID of 2, which is used in the URLS to pull the data.

In this case, the audio starts with the data from the url "init-stream$RepresentationID$.m4s" and then adds audio chunks from URLs in the form "chunk-stream$RepresentationID$-$Number%05d$.m4s". In otherwords, it would first pull the file "https://streams.2019.chall.actf.co/video/init-stream2.m4s" then concatenate it with "https://streams.2019.chall.actf.co/video/chunk-stream2-00001.m4s", then "https://streams.2019.chall.actf.co/video/chunk-stream2-00002.m4s", etc. until all audio files are pulled. However, we aren't displayed this audio, we get the first adaptation set from our browser. So we want to get this data ourselves.

I wrote a bash script to pull the data for us:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572129319195770907/unknown.png'>
  
This pulled an extra m4s, so I just removed it. I then concatenated all of the files:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572129665632698383/unknown.png'>
  
I then converted the resulting m4s to a mp3 file:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572135472793649152/unknown.png'>
  
Listening to it, I heard morse code. I transcribed the following:
```
.- -.-. - ..-. -.--. ..-. .---- ....- ..... .... -....- .---- ..... -....- -.. ...-- ....- -.. -....- .---- ----- -. ----. -....- .---- .---- ...- ...-- -....- -- .--. ...-- ----. -....- -.. ....- ... .... -.--.-
```
Which <a href='https://morsecode.scphillips.com/translator.html'>translates</a> to:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572135819037376512/unknown.png'>

(\<KN\> has the same morse code as '(' )

Asking the challenge author for confirmation, I converted it to the correct format.

flag: `actf{f14sh_15_d34d_10n9_11v3_mp3g_d4sh}`
