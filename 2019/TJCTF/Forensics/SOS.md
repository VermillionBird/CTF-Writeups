# SOS
### Forensics: 70 points
#### Solved by: Vermillion
`Written by Alaska47`

`Help! I swiped `<a href="https://static.tjctf.org/038638fcb76d888fe4cbe5ee88a476b88a6014b92a106df7f4683e2942054eca_music.wav">this</a>` off some extraterrestrial musician's laptop, but I think I'm getting trolled. I tried to intercept their communications, but their frequency is just too high. There's something wrong, but I just can't put my ear on it...`

Downloading the .wav file, we instantly get Rick-Rolled. UGH. Anyway, I opened it in Audacity. Since the description mentioned that the frequency was way to high, I reduced the sampling rate to the lowest that Audacity could go: 8000 Hz. Looking at the spectrogram, you can clearly begin to see random spikes in the waveform. They generally conform to one of to widths, one longer, one shorter, which implies morse.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567845536254918656/unknown.png'>

I transcribed it to:

`.-- --- .-- -.-.--/.-- .... .- -/.-/- .-. --- .-.. .-.. --..--/.- --/../.-. .. --. .... - ..--../.-- . .-.. .-.. --..--/. -. --- ..- --. ..../--- ..-./- .... .- - --..--/.... . .-. . .----. .../- .... ./..-. .-.. .- --.  ---.../- .--- -.-. - ..-. .--.- -- -.-- ...- --- .. -.-. . .. ... --. .-. --- .-- .. -. --. -- --- .-. ... . .--.--`

And used this <a href='https://morsecode.scphillips.com/translator.html'>site</a> to get the flag.

flag: `tjctf{myvoiceisgrowingmorse}`
