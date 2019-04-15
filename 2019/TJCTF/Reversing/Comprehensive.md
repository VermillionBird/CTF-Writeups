# Comprehensive
### Reversing: 50 points
#### Solved by: Vermillion
```
Written by boomo

Please teach me how to be a comprehension master, all my friends are counting on me!
```
<a href='https://static.tjctf.org/89499ec336d112481a0aa44de40c5aa52b62d3557f1791356fc775877c945545_comprehensive.py'>comprehensive.py</a>
```
Original output: 225, 228, 219, 223, 220, 231, 205, 217, 224, 231, 228, 210, 208, 227, 220, 234, 236, 222, 232, 235, 227, 217, 223, 234, 2613

Note: m and k were 24 and 8 characters long originally and english characters.
```
The program looked like this:
```
m = 'tjctf{?????????????????}'.lower()
k = '????????'.lower()

f = [[ord(k[a]) ^ ord(m[a+b]) for a in range(len(k))] for b in range(0, len(m), len(k))]
g = [a for b in f for a in b]
h = [[g[a] for a in range(b, len(g), len(f[0]))] for b in range(len(f[0]))]
i = [[h[b][a] ^ ord(k[a]) for a in range(len(h[0]))] for b in range(len(h))]
print(str([a + ord(k[0]) for b in i for a in b])[1:-1] + ',', sum([ord(a) for a in m]))
```
I began analyzing the program. It's a lot easier if you print between each step, so I did. I found that f is a list of three lists, each list containing 8 numbers that are the result of XOR-ing 8 characters (ascii number) from the flag (m) with the 8 character key (k) at a time:
```
[[75, 85, 92, 75, 89, 68, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 66]]
```
g just combines the lists into one.
```
[75, 85, 92, 75, 89, 68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66]
```
h turns the list into 8 lists of 3 numbers. The first such list takes the first, ninth, and seventeenth numbers from g. The second such list takes the second, tenth, and eighteenth numbers from g, and so on.
```
[[75, 0, 0], [85, 0, 0], [92, 0, 0], [75, 0, 0], [89, 0, 0], [68, 0, 0], [0, 0, 0], [0, 0, 66]]
```
i takes each list and XORs with the first 3 characters from the key:
```
[[116, 63, 63], [106, 63, 63], [99, 63, 63], [116, 63, 63], [102, 63, 63], [123, 63, 63], [63, 63, 63], [63, 63, 125]]
```
And finally, it combines them into one tuple, adding the ascii number of the first letter from the key to each number and a final number that's the sum of the ascii numbers for all of the characters in the orginal flag.
```
('179, 126, 126, 169, 126, 126, 162, 126, 126, 179, 126, 126, 165, 126, 126, 186, 126, 126, 126, 126, 126, 126, 126, 188,', 1858)
```
We want this final output to be equal to the given one by finding the letters. Luckily, this is definitely possible. We know that m starts with 'tjctf{' and ends with '}', so we can use this to get most of the key. First, I got the first letter of the key, since its ord is added at the end. I used python to bash out all possible characters until I got the correct value.
```
import string, itertools
print "first"
for char in string.ascii_lowercase:
	x = ((ord('t')^ord(char))^ord(char))+ord(char)
	if x == 225:
		print char
```
Output: `m`

Key: m???????


I then found the next 5 letters, since all of those letters get moved to the beginning of their own list in step h, so therefore all get XOR-ed with 'm' during step i. I rememberd to compare against the correct final number, since they got shifted out of order in step h.

```
print "second"
for char in string.ascii_lowercase:
	x = ((ord('j')^ord(char))^ord('m'))+ord('m')
	if x == 223:
		print char

print 'third'
for char in string.ascii_lowercase:
	x = ((ord('c')^ord(char))^ord('m'))+ord('m')
	if x == 205:
		print char

print 'fourth'
for char in string.ascii_lowercase:
	x = ((ord('t')^ord(char))^ord('m'))+ord('m')
	if x == 231:
		print char

print 'fifth'
for char in string.ascii_lowercase:
	x = ((ord('f')^ord(char))^ord('m'))+ord('m')
	if x == 208:
		print char

print 'sixth'
for char in string.ascii_lowercase:
	x = ((ord('{')^ord(char))^ord('m'))+ord('m')
	if x == 234:
		print char
```
output:
```
second
u
third
n
fourth
c
fifth
h
sixth
k
```
key: munchk??

Unfortunately, we cannot get the next letter, since that would require another known letter. But we can get the final letter of the key, using the character '}':
```
print 'last'
for char in string.ascii_lowercase:
	x = ((ord('}')^ord(char))^ord('n'))+ord('m')
	if x == 234:
		print char
```
Key: munchk?n
Finally, I ran the following script that would generate a dictionary with all possible 7th characters in the format flag:key:
```
p = '225, 228, 219, 223, 220, 231, 205, 217, 224, 231, 228, 210, 208, 227, 220, 234, 236, 222, 232, 235, 227, 217, 223, 234'
lis = p.split(', ')
keys={}
for c in string.ascii_lowercase:
	strin = ''
	k = 'munchk' + c + 'n'
	for i in range(len(m)):
		for char in string.ascii_lowercase+'{}':
			if i < 8:
				x = ((ord(char) ^ ord(k[i])) ^ ord('m')) + ord('m')
				if x == int(lis[3*i]):
					strin+=char
			elif i <16:
				x = ((ord(char) ^ ord(k[i%8])) ^ ord('u')) + ord('m')
				if x == int(lis[3*(i-8)+1]):
					strin+=char
			else:
				x = ((ord(char) ^ ord(k[i%8])) ^ ord('n')) + ord('m')
				if x == int(lis[3*(i-16)+2]):
					strin+=char
	keys[strin]=k
print keys
```
<img src='https://cdn.discordapp.com/attachments/532350033241309226/567479795101728769/unknown.png'>

Notice that some of the flags don't have 24 characters because the key resulted in a non-alphanumeric character. Therefore, I ran all of these flag:key pairs back through the original algorithm to find the one that resulted in the desired output:
```
for flag in keys:
	m = flag
	k = keys[flag]
	print m, k
	try:
		f = [[ord(k[a]) ^ ord(m[a+b]) for a in range(len(k))] for b in range(0, len(m), len(k))]
		g = [a for b in f for a in b]
		h = [[g[a] for a in range(b, len(g), len(f[0]))] for b in range(len(f[0]))]
		i = [[h[b][a] ^ ord(k[a]) for a in range(len(h[0]))] for b in range(len(h))]
		print(str([a + ord(k[0]) for b in i for a in b])[1:-1] + ',', sum([ord(a) for a in m]))
	except:
		pass
```
<img src='https://cdn.discordapp.com/attachments/532350033241309226/567480786945572885/unknown.png'>

I finally found the key and the flag.

flag: `tjctf{oooowakarimashita}`
