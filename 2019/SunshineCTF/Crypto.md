# Crypto
I don't know why, but crypto challenges are always fun for me.
<br>
<br>
## 50 points: WelcomeCrypto
```
~C8 =39 A?2V8 73J:C 8FG7 AF?JJC2ECP

DF?LHb=r_>b0%_0520<c8bPN

Author: Loavso
```
I'm pretty embarassed this took me as long as it did. I didn't recognize the cipher right away, but its just a ROT47. Use any <a href='https://www.dcode.fr/rot-47-cipher'>online decoder</a> you want. The one I used outputted:
```
Org lbh pna'g fbyir guvf punyyratr!

sun{w3lC0m3_T0_da_k4g3!}
```
Literally no clue what the first line was supposed to be, but the flag was valid.

flag: `sun{w3lC0m3_T0_da_k4g3!}`

*Edit*: The first line is a ROT13 after the ROT47: `Bet you can't solve this challenge!` Why they would make the flavor text another step, I have no idea.
<br>
<br>
<br>
## 50 points: CB1
```
We picked up a new numbers station that's been active in the shortwave bands. We need to figure out how to crack his code.

Here's an example file, crack the cipher and send us the plaintext message.

```
<a href='http://files.sunshinectf.org/crypto/CB1.wav'>CB1.wav</a>
```

NOTE: NON-Standard Flag Format

Author: leviathan
```
When I saw this, I thought it would be an audio steganography challenge. But let's give it a listen! I transcribed:
```
Code Number: 6
Begin Message
Hotel Kilo Charlie Golf Xray Kilo Zulu November Kilo Oscar Juliette Kilo Yankee Uniform Lima Sierra Golf Xray India November
```
It just repeated after that. The words immediately stood out to me as the NATO Phonetic Alphabet; it's just the first letter of each word.
```
6
HKCGXKZNKOJKYULSGXIN
```
6 seems to suggest a Caesar Cipher. I used this <a href='https://cryptii.com/pipes/caesar-cipher'>site</a> to decode it with a shift of 6, and got the flag. The flag was in a nonstandard format, as was said by the description.

flag: `bewaretheidesofmarch`
<br>
<br>
<br>
## 100 points: CB2
```
That numbers station is still active, they've just switched codes. We need you to crack it before they switch again.

Here's an example file, crack the cipher and send us the plaintext message.
```
<a href='http://files.sunshinectf.org/crypto/CB2.wav'>CB2.wav</a>
```
NOTE: NON-Standard Flag Format

Author: leviathan
```
Another audio file. Transcription (already using NATO to replace to letters):
```
Codeword: Clarinet
DBDAABEDDDDCDEACADBBDDADDEABBB
```
I got stuck on this one for a while. The key point to notice is that there are only 5 characters, A-E. So, searching 'Cipher 5 unique letters' <a href='http://practicalcryptography.com/cryptanalysis/text-characterisation/identifying-unknown-ciphers/'>this website</a> popped up. It suggested that it was a polybius square cipher. I used <a href='https://www.dcode.fr/polybius-cipher'>dcode</a> once again.

![](/Images/2019/SunshineCTF/CB2.PNG)

I entered in the key of CLARINET, chose the no 'j' alphabet for the rest of the deranged alphabet, and changed 1-5 to A-E. The website has an explanation for how Polybius works and its pretty simple. The website did its work and outputted the flag, albeit in uppercase.

flag: `polysquarerule`
