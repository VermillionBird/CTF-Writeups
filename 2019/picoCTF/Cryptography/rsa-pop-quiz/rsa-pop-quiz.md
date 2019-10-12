# rsa-pop-quiz
## Points: 200
### Solved by: Vermillion
<br></br>
### Description

`Class, take your seats! It's PRIME-time for a quiz...` `nc 2019shell1.picoctf.com 53028` ` `

### Solve

Connecting to the service using the provided netcat command, we see an introduction. It seems that we will have to answer questions about the RSA (Rivest-Shamir-Adleman) public-key cryptosystem, similar to the RSA pop quiz from 2018:

![](/Images/2019/picoCTF/rsapopquizintro.PNG)

All answers are given in decimal. I will give a brief overview of RSA and go over how I got the answer for each question, but you might want to read up [how RSA works](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation) elsewhere as well.

#### How does RSA work?

RSA is a public key cryptosystem, meaning that messages are encrypted with a public key that is known to everyone and decrypted using a private key known only to the receiver. This private key and public key are generated ahead of time. The generation uses primes, since the time needed to factorize a large number into its prime factors is infeasibly high for large numbers and large primes.

First, two different large primes are chosen, `p` and `q`. These are kept secret.

Then, compute `n = p * q`, the modulus that will be used during encryption/decryption. This is public.

Then `totient(n)` is calculated. `totient(n)` is either Carmichael's totient function: `lcm(p - 1, q - 1)` or the Euler totient function. Most CTFs use the Euler totient function, `totient(n) = (p - 1) * (q - 1)`. This is secret.

Pick an `e` between 1 and `totient(n)` so that `totient(n)` and `e` share no common factors. `e` is often `65537` due to its efficiency. This, in combination with `n`, is the public key.

Find `d` so that `e * d ≡ 1 (mod totient(n))`. In other words, find the modular multiplicative inverse of `e` modulo `totient(n)`. `d`, in combination with `n`, is the private key.

In order to encrypt a message m, find `pow(m,e,n)`, or `m` raised to the `e` modulo `n`.

To decrypt a message c, find `pow(c,d,n)`.

Now that we're done, let's get started. I used python to calculate all values I needed.

#### Question 1:
![](/Images/2019/picoCTF/rsapopquizq1.PNG)

Here we are given `p` and `q` and are asked to find `n`. As stated above, `n` is just `p * q`. Simple enough. Therefore, this is feasible and I gave the correct answer.

#### Question 2:
![](/Images/2019/picoCTF/rsapopquizq2.PNG)

Here we are given `p` and `n` and are asked to find `q`. `p * q = n`, so `q = n / p`. Feasible.

#### Question 3:
![](/Images/2019/picoCTF/rsapopquizq3.PNG)

Here is the first question where the answer is actually infeasible. We are given `e` and `n` and asked to find `p` and `q`. This is basically asking you to find the factors of `n`. When `n` is sufficiently large, finding the factors becomes extremely time consuming, such that it would take many lifetimes to factor. So while it is *technically* possible, it isn't feasible. The difficulty of factoring large numbers is the entire premise behind most cryptosystems today.

#### Question 4:
![](/Images/2019/picoCTF/rsapopquizq4.PNG)

We are given `p` and `q` and asked to find `totient(n)`. As stated above, RSA origianlly used the Euler totient function, so we use that here. `totient(n) = (p - 1) * (q - 1)`. Feasible.

#### Question 5:
![](/Images/2019/picoCTF/rsapopquizq5.PNG)

Here we are given the plaintext `m` and the public key `(e, n)`. We are expected to find the encrypted message. This is just `pow(m,e,n)`. Use Python's built-in function `pow()` for calculating modular exponentiation to get the answer. Feasible.

#### Question 6:
![](/Images/2019/picoCTF/rsapopquizq6.PNG)

Here we are given the ciphertext `c` and the public key `(e, n)`. We are expected to find the plaintext message. Notice that we are not given the private key used for decrytion, `(d, n)`, but rather the public key for encryption. In order to find `d`, we would need `totient(n)` and `e`. To get `totient(n)` we would need `p` and `q`, so this once again becomes a matter of the feasibility of factoring large `n`. This is infeasible.

#### Question 7:
![](/Images/2019/picoCTF/rsapopquizq7.PNG)

Here we are given `q`, `p`, and `e`. We need to find the private exponent `d`. This is done during generation of the cryptosystem, so it is obviously feasible. The fastest way to find the modular multiplicative inverse of a number is using the Extended Euclidean algorithm. I coded it up [here](modinv.py).

Find `d = modinv(e, totient)`, where `totient = (p - 1) * (q - 1)`. Feasible.

#### Question 8:
![](/Images/2019/picoCTF/rsapopquizq8.PNG)

Here we are given `p`, `c`, `e`, and `n` and asked to find `m`. This is essentially the complete decryption using RSA.

Find `q` as `n / p`. Then find `totient(n)` as `(p - 1) * (q - 1)`. Find the private exponent `d` as `modinv(e, totient)`. Find m as `pow(c,d,n)`. Feasible. 

Note that if we weren't given `p`, this would be infeasible, which is what makes RSA secure. Someone who intercepts communication on a website (Man in the Middle Attack) would only see `c`, `e`, and `n`, so he would not be able to decrypt the message.

### Conclusion:

![](/Images/2019/picoCTF/rsapopquizconclusion.PNG)

It appears that the flag is the message we just decrypted.

Getting the flag:

![](/Images/2019/picoCTF/rsapopquizflag.PNG)

### Flag:
picoCTF{wA8_th4t$_ill3aGal..of4878474}
