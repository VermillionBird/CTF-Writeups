# MC Woes
### Forensics: 5 points
#### Solved by: Vermillion
`Written by boomo`

<a href='https://static.tjctf.org/b9bf0bf0d5572ba9ab95a2e13af6d44b362ed7613fa30bb939d71cb38c5f7833_my_world.zip'>My world</a>` won't launch anymore! I'm sure its something in the files...`

Downloading the zip file, I extracted it using `unzip b9bf0bf0d5572ba9ab95a2e13af6d44b362ed7613fa30bb939d71cb38c5f7833_my_world.zip -d my_world`. Entering the directory I created, I saw an overarching folder called `'my world'`, which meant I didn't need to specify the output directory, but oh well.

I looked through the files a little, and it seemed to legitimately be a Minecraft world file, which is horrible and boomo should feel bad. This was a low point value, so I decided to just give grepping a try. I used the recursive tag (`-r`) in order to search every directory. It was found in a binary file `worlddata/level.dat`, so I then included the `-a` tag to process binary files as normal text so I could get the flag:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567824697966854168/unknown.png'>

flag: `tjctf{_g3t_sn4ck5}`
