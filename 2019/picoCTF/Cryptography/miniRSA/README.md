# miniRSA
## Points: 300
### Solved by: Vermillion
<br></br>
### Description

`Lets decrypt this: `[ciphertext](ciphertext)`? Something seems a bit small`

### Solve

Opening up the given file gives us the following:

```
N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872650082343781881947286623459260358458095368337105247516735006016223547924074432814737081052371203373104854490121754016011241903971190586239974732476290129461147622505210058893325312869 
```

If you don't understand what this means, see [this writeup](../rsa-pop-quiz/README.md) for an explanation on RSA.

At first glance, this may seem impossible. The modulus `N` is far too large to factor. However, there is a caveat. `c = pow(m,e,n)`. However, what if `m ^ e < n`? Then the modulus never comes into play, and `c = m ^ e`. Not only that, but `e` in this case is very small: 3. We can clearly see that `c` is much smaller than `n`, meaning that it might just be possible that `m ^ e < n`. If that is the case, we can just take the cube root of `c` to find `m` (`m ^ 3 = c` so `c = m ^ (1/3)`).

These numbers are very large, so we need to make sure that our cube root is precise enough to list every digit. To do this in python, you can use a binary search. I wrote this [program](/Useful-Scripts/Cryptography/invpow.py) that finds the nth root of a number and outputs the result in ASCII.

![](/Images/2019/picoCTF/minirsa.PNG)

### Flag:
`picoCTF{n33d_a_lArg3r_e_db48b19b}`
