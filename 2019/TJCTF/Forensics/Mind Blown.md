# Mind Blown
### Forensics: 30 points
#### Solved by: Vermillion
```
Written by rj9

One of my friends keeps sending me weird memes from his favorite subreddit but I don't quite understand this one...
```
<a href="https://static.tjctf.org/694003b3deecf2382b3aa510e5f3e5f5153bb9c062e4f20878c0d343bc297767_meme.jpg">meme</a>

Opening the image, we see the first image of the template for the Expanding Brain meme. Clearly, there's more, so it's probably a hidden file steganography type challenge. I first run binwalk on the file:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567836539095220224/unknown.png'>

It looks like there are 3 JPEGs hidden in the file, not just the one we see. Using `dd` to extract them:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567837320842313729/unknown.png'>

And looking at both the images we see:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567837721100288011/unknown.png'>

flag: `tjctf{kn0w_y0ur_m3tad4ta}`
