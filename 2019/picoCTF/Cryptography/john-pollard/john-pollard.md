# john-pollard
## Points: 500
### Solved by: Vermillion
<br></br>
### Description

`Sometimes RSA `[certificates](cert)` are breakable`

### Solve

If you don't understand RSA, see [this writeup](../rsa-pop-quiz/rsa-pop-quiz.md) for an explanation.

We are told that the flag is in the form `picoCTF{p,q}` in the hints. That means we are trying to find the factors of the RSA modulus. Opening up the provided RSA Certificate, we see an RSA certificate in Privacy Enhanced Mail (PEM) format:

```
-----BEGIN CERTIFICATE-----
MIIB6zCB1AICMDkwDQYJKoZIhvcNAQECBQAwEjEQMA4GA1UEAxMHUGljb0NURjAe
Fw0xOTA3MDgwNzIxMThaFw0xOTA2MjYxNzM0MzhaMGcxEDAOBgNVBAsTB1BpY29D
VEYxEDAOBgNVBAoTB1BpY29DVEYxEDAOBgNVBAcTB1BpY29DVEYxEDAOBgNVBAgT
B1BpY29DVEYxCzAJBgNVBAYTAlVTMRAwDgYDVQQDEwdQaWNvQ1RGMCIwDQYJKoZI
hvcNAQEBBQADEQAwDgIHEaTUUhKxfwIDAQABMA0GCSqGSIb3DQEBAgUAA4IBAQAH
al1hMsGeBb3rd/Oq+7uDguueopOvDC864hrpdGubgtjv/hrIsph7FtxM2B4rkkyA
eIV708y31HIplCLruxFdspqvfGvLsCynkYfsY70i6I/dOA6l4Qq/NdmkPDx7edqO
T/zK4jhnRafebqJucXFH8Ak+G6ASNRWhKfFZJTWj5CoyTMIutLU9lDiTXng3rDU1
BhXg04ei1jvAf0UrtpeOA6jUyeCLaKDFRbrOm35xI79r28yO8ng1UAzTRclvkORt
b8LMxw7e+vdIntBGqf7T25PLn/MycGPPvNXyIsTzvvY/MXXJHnAqpI5DlqwzbRHz
q16/S1WLvzg4PsElmv1f
-----END CERTIFICATE-----
```

RSA certificates are sent from a web server to a client when data needs to be encrypted. If the client trusts the certificate and its issuer, then the modulus and public key provided in the certificate is used to encrypt data sent by the client using RSA, and a corresponding private key is used to decrypt the contents at the web server.

Let's [decode](https://redkestrel.co.uk/products/decoder/) this PEM certificate to a more readable format.

![](/Images/2019/picoCTF/johnpollardweak.PNG)

We can see that the modulus is extremely weak: only 53 bits. Generally, you want a 4096 bit key, which will change as cracking gets faster.

Scroll down to the detailed information, where you can see the modulus:

![](/Images/2019/picoCTF/johnpollarddecode.PNG)

The modulus is `4966306421059967`, which is absolutely tiny. Factor it using basically any factorizer on the internet to get its factorization as `67867967 * 73176001`. From here, there are only permutations to check as the flag. It turns out that `p = 73176001` and `q = 67867967`.

### Flag:
`picoCTF{73176001,67867967}`
