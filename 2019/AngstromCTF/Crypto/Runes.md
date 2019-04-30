## Runes
### 70 points, 240 solves

`The year is 20XX. ångstromCTF only has pwn challenges, and the winner is solely determined by who can establish a socket connection first. In the data remnants of an ancient hard disk, we've recovered a `<a href="https://files.actf.co/8a7dd6bb04a759a4b061636b90ddb2e82830a8fd7bdc0879f25cbba1441ab2fa/runes.txt">string of letters and digits</a>`. The only clue is the etching on the disk's surface: Paillier.`

`Author: defund`

The file has:
```
n: 99157116611790833573985267443453374677300242114595736901854871276546481648883
g: 99157116611790833573985267443453374677300242114595736901854871276546481648884
c: 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
```
Searching up Paillier gives us the <a href='https://en.wikipedia.org/wiki/Paillier_cryptosystem'>Wikipedia page</a> for the Paillier Cryptosystem. First, I needed to factor n into its two prime factors. I used <a href='https://www.alpertron.com.ar/ECM.HTM'>this site</a> to get p and q:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572586104763580474/unknown.png'>

I then used <a href='https://www.wolframalpha.com/input/?source=frontpage-immediate-access&i=LCM%5B310013024566643256138761337388255591612,319848228152346890121384041219876391790%5D'>Wolfram-Alpha</a> to find lambda (LCM[p-1,q-1]):

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572586591005048832/unknown.png'>

I then wrote my python script:
```
p = 310013024566643256138761337388255591613
q = 319848228152346890121384041219876391791
lamda = 49578558305895416786992633721726687338335190430938373377797362948969174832740
n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def L(x):
	return (x-1)/n

inv = modinv(L(pow(g,lamda,n**2)),n)                        #The modular inverse in Paillier
print inv

plain = L(pow(c,lamda,n**2))*inv%n                          #Decrypt in Paillier
print plain
print hex(plain)[2:-1].decode('hex')
```

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572587374840905748/unknown.png'>

flag: `actf{crypto_lives}`
