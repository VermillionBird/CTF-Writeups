# whats-the-difference
## Points: 200
### Solved by: Vermillion
<br></br>
### Description

`Can you spot the difference? `[kitters](kitters.jpg)` `[cattos](cattos.jpg)`. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server`

### Solve

Download both the images and open them up:

|[kitters.jpg](kitters.jpg)|[cattos.jpg](cattos.jpg)|
|----|----|
|![](kitters.jpg)|![](cattos.jpg)|

There's obviously something in `cattos.jpg` that is making it look like that. Since the prompt is to find the difference, I'm going to use the following bash one-liner that will find the bytes that are different between the two and output it as pretty hexadecimal. The first hexadecimal is the offset of that byte (location), the second is the byte in `kitters.jpg` as hex, and the third is the byte in `cattos.jpg` as hex.

`cmp -l kitters.jpg cattos.jpg | gawk '{printf "%08X %02X %02X\n", $1, strtonum(0$2), strtonum(0$3)}'`

![](/Images/2019/picoCTF/diffbash.PNG)

The right side, or the bytes in `cattos.jpg` seem promising as ASCII values (`'picoCTF' = '70 69 63 6f 43 54 46'`), so let's get only that side:

`cmp -l kitters.jpg cattos.jpg | gawk '{printf "%02X\n", strtonum(0$3)}'`

![](/Images/2019/picoCTF/diffascii.PNG)

Copy that to a python script to output the flag:

![](/Images/2019/picoCTF/diffflag.PNG)

### Flag:
picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
