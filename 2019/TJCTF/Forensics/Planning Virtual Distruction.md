# Planning Virtual Distruction
### Forensics: 120 points
#### Solved by: Vermillion

`Written by jfrucht25`

`In his quest for world domination, Omkar realized that he needed to conquer more than just land, so he turned to conquering the internet. His first target was becoming the king of youtube by overcoming Pewdiepie. As a result, he embodied his Indian culture, creating the channel TSeries. In a step to stop Omkar's world domination, we need to regain control of the internet. Perhaps you can uncover his plans hidden in `<a href="https://static.tjctf.org/b4260c304144e942c38edcb1f6d9641c4be1c0f0afee0046b2d50b5342895610_phase2plans.png">this image</a>` and make a DIFFERENCE before it is too late.`

Planning Virtual Distruction's initials make the acronym PVD, which refers to Pixel Value Differencing, a type of steganography. After quite a bit of research, I found the following things:
<ul>
  <li>In PVD, pixel values of grayscale images are changed to encode numbers in their absolute differences</li>
  <li>Pixels are read in a zig-zag pattern; the first row left to right, the second right to left, and so on.</li>
  <li>Pixel differences are split into ranges, typically:
    <ul>
      <li>0-7</li>
      <li>8-15</li>
      <li>16-31</li>
      <li>32-63</li>
      <li>64-127</li>
      <li>128-255</li>
    </ul>
  </li>
  <li>When decoding a difference, you find the encoded binary by subtracting the lower end of the range from the difference, and then padding the binary based on the size of the range; you take the base-2 logarithm of the size of the range to find the number of bit
    <ul>
      <li>For example, a difference of 37 would become 37-32=5=101, but 32-63's range size is 32, so the number of bits is 5. Therefore, the final binary is 00101</li>
    </ul>
  </li>
  <li>You only find the difference between pairs; no overlapping. First difference is Pixel[1]-Pixel[0], second is Pixel[3]-Pixel[2].
    <ul>
      <li>I forgot this, so I got stuck for a little before remembering.</li>
    </ul>
  </li>
</ul>
This <a href='https://thetraaaxx.org/pixel-value-differencing-pvd-explications'>site</a> was especially helpful, but in French, so unless you understand French, you should use Google Translate. Anyway, I wrote my python script to analyze the image:

```
from PIL import Image
import sys
from itertools import chain
img = Image.open("p2p.png").convert('L') #Convert img to a grayscale style image

WIDTH, HEIGHT = img.size
data = list(img.getdata()) #get list of all pixel values
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)] #Convert list into lists of pixel values by row
newdata = []
for i in range(len(data)):
	if i % 2 == 0:
		newdata.append(data[i]) #If it's an even valued row, it should be left to right
	elif i % 2 == 1:
		newdata.append(data[i][::-1]) #If it's an odd valued row, it should be right to left
data = list(chain.from_iterable(newdata)) #Combine the list of lists back into one list

diff = []
import math
for i in range(0, len(data)-1, 2): #goes by 2 in order to prevent overlap (part where I got stuck)
	diff.append(int(math.fabs(data[i+1]-data[i]))) #Makes a list of integer absolute differences
print diff

strin = '0b' #Starts a binary string
for d in diff:
	if 0 <= d <= 7: #Range 1
		b = d
		b = format(b, '03b') #Convert number into binary with padding for 3 bits
		strin += b #Adds binary to string
	elif 8 <= d <= 15:
		b = d-8
		b = format(b, '03b')#Convert number into binary with padding for 3 bits
		strin += b #Adds binary to string
	elif 16 <= d <= 31:
		b = d-16
		b = format(b, '04b')#Convert number into binary with padding for 4 bits
		strin += b #Adds binary to string
	elif 32 <= d <= 63:
		b = d-32
		b = format(b, '05b')#Convert number into binary with padding for 5 bits
		strin += b #Adds binary to string
	elif 64 <= d <= 127:
		b = d-64
		b = format(b, '06b')#Convert number into binary with padding for 6 bits
		strin += b #Adds binary to string
	elif 128 <= d <= 255:
		b = d-128
		b = format(b, '07b')#Convert number into binary with padding for 7 bits
		strin += b #Adds binary to string

print strin
strin = int(strin, 2) #converts binary into giant integer so I can
strin = hex(strin)[2:-1] #Convert it to hex (Removing the 0x at the beginning and the L at the end)
print strin.decode('hex') #Decode it to ASCII
```

You should know if the code works if decode() can successfully decode it (padding check) and if, well, the flag is in the decoded hex.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568099799484858368/unknown.png'>

flag: `tjctf{r1p_p3wd5_t53r1s_b4d}`

RIP pewds, for his kingdom has fallen.
