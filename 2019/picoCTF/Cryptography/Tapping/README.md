# Tapping
## Points: 200
### Solved by: Vermillion
<br></br>
### Description

`Theres tapping coming in from the wires. What's it saying` `nc 2019shell1.picoctf.com 37911` `.`

### Solve

Connect to the service using netcat:

![](/Images/2019/picoCTF/tappingnetcat.PNG)

You get what's clearly Morse Code:
```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- ..--- -.... ..... ----. ...-- --... -.... -.... ...-- }
```

I used [this site](https://www.dcode.fr/morse-code) to decode the Morse Code.

![](/Images/2019/picoCTF/tappingdecode.PNG)

Replace the ? with the appropriate braces to get the flag. Note that the flag is in all uppercase.

### Flag:
`PICOCTF{M0RS3C0D31SFUN2265937663}`
