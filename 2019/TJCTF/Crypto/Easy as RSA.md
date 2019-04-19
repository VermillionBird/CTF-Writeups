# Easy as RSA
### Crypto: 20 points
#### Solved by: Vermillion

` Written by rj9`

`Decrypt this for a quick flag!`

<a href="https://static.tjctf.org/12013a6849ec48d718e87b22bdf836e2caa41494483bd276a45d21d13a3b945c_rsa.txt">rsa</a>

rsa:
```
n: 379557705825593928168388035830440307401877224401739990998883
e: 65537
c: 29031324384546867512310480993891916222287719490566042302485
```
In RSA, the plaintext is encrypted by raising it to the power of some prime `e` (the public key) under modulus `n`. To decrypt ciphertext, we raise the ciphertext to the power of some prime `d` (the private key) under modulus `n`.

We are given the modulus `n`, the public key `e`, and the ciphertext `c`, and we need to find the private key `d` to decrypt the plaintext. In RSA, the modulus `n` is the product of two primes, `p` and `q`. `d` is the modular inverse of `e` under modulus `r`, where `r` is `(p-1)*(q-1)`. Therefore, we first need to start by finding the factors of `n`. This <a href='https://www.numberempire.com/numberfactorizer.php'>site</a> gives us:

`564819669946735512444543556507*671998030559713968361666935769`

Next we have to find `d` and then decrypt the message. I wrote a python script:
```
p = 564819669946735512444543556507
q = 671998030559713968361666935769
c = 29031324384546867512310480993891916222287719490566042302485
n = p*q
r = (p-1)*(q-1)
e = 65537

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

d=modinv(65537,r)
m = pow(c,d,n)      #A built in function for calculating modular exponentiation quicker
Hex = hex(m)[2:-1]  #Remove the 0x and L from the string.
print Hex.decode('hex')
```
Running the code gives us our flag:

flag: `tjctf{RSA_2_3asy}`
