# Cable Selachimorpha
### Forensics: 40 points
#### Solved by: Vermillion
```
Written by jfrucht25

Although Omkar is the expert at web, I was still able to intercept his communications. Find out what password he used to login into his website so that we can gain access to it and see what Omkar is up to.
```
<a href="https://static.tjctf.org/d9a0cdb25486aaa8a72102fc4de1156f4d3a76f10ea24a7559dcca79a1ea2d3a_capture.pcap">capture.pcap</a>

Downlaoding it, we see that it is a .pcap file, so we open it in Wireshark. Knowing that we're looking for a login into a website, we filter by HTTP Protocol and look at the POST request:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567839097457213445/unknown.png'>

flag: `tjctf{b0mk4r_br0k3_b10n}`
