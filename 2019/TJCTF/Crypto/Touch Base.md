# Touch Base
### Crypto: 5 points
#### Solved by: wowie
```
Written by rj9
Decode this string for an easy flag!`

Encoded: dGpjdGZ7ajJzdF9zMG0zX2I0c2U2NH0=
```

The name of the challenge is "Touch Base" so we can assume that the flag is encoded into some base. We notice the equals sign at the end and it reminds us of base 64, so if we go to this <a href='https://www.base64decode.org/'>site</a>, we paste the encoded string in and decode and voila!

flag: `tjctf{j2st_s0m3_b4se64}`
