# Guess My Hashword
### Cryptography: 10 points
#### Solved by: Vermillion
```
Written by boomo

I bet you'll never guess my password!

I hashed tjctf{[word]} - my word has a captial letter, two lowercase letters, a digit, and an underscore. ex: hash('tjctf{o_0Bo}') or hash('tjctf{Aaa0_}')

Here's the md5 hash: 31f40dc5308fa2a311d2e2ba8955df6c
```
Originally, the challenge was written in such a way as to imply that only the word was hashed, and they updated it after I flagged. That's why I got stuck for a little, but after realizing they hashed the whole flag, it was pretty simple:
```
from itertools import *
import string
import md5
goal = '31f40dc5308fa2a311d2e2ba8955df6c'
for combo in product(string.ascii_lowercase,repeat= 2):
	lc = ''.join(combo)
	for char in string.ascii_uppercase:
		for num in string.digits:
			st = lc+char+num+'_'
			for perm in permutations(st):
				x= md5.new('tjctf{'+''.join(perm)+'}')
				if x.hexdigest() == goal:
					print ''.join(perm)
```

<img src='https://cdn.discordapp.com/attachments/532350033241309226/568117773465813012/unknown.png'>

flag: `tjctf{w0w_E}`
