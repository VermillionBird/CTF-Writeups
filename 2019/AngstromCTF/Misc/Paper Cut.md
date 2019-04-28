## Paper Cut
### 190 points, 42 solves

`defund submitted a math paper to a research conference and received a few comments from the editors. Unfortunately, we only have a `<a href="https://files.actf.co/ab0ba68436262dd0989939f80ef3c37f980c2c43d8beaf169a07b123d37f7620/paper_cut.pdf">fragment</a>` of the returned paper.`

`Author: defund`

Downloading the pdf, we find that we cannot open it. I looked through the hex in ghex, but could not immediately see any errors, so I wanted to see if I could extract anything from the data. I knew that pdfs were divided into stream objects, where the actual data is in the streams. From here I noticed that there was no endstream, trailer, or anything after the stream data, so that's where the error laid.

Anyway, I used dd to extract the data starting from the highlighted character:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572122782511529985/unknown.png'>

Offset = 0x4E = 78

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572123319571316736/unknown.png'>

From ghex, we can see that it used FlateDecode to compress the data, so we can just use zlib to decompress it. However, my code didn't initially work, so I used this <a href='https://stackoverflow.com/questions/32367005/zlib-error-error-5-while-decompressing-data-incomplete-or-truncated-stream-in'>site</a> to debug my code.
```
import zlib
text = open('stream','rb').read()
zobj = zlib.decompressobj()
decoded = zobj.decompress(text)
print decoded
```

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572125092100964362/unknown.png'>

The output was a bunch of letters and floating points. Searching up the recurring string 'Tj ET BT' turns up this <a href='https://blog.idrsolutions.com/2010/11/grow-your-own-pdf-file-%E2%80%93-part-5-path-objects/'>site</a>, which shows that these are PDF commands to create a PDF File. I just used their header and footer to create a new pdf, replacing their stream with my stream:
```
import zlib
text = open('stream','rb').read()
zobj = zlib.decompressobj()
decoded = zobj.decompress(text)
print decoded

#their beginning section
part1 = '''%PDF-1.6
1 0 obj <</Type /Catalog /Pages 2 0 R>>
endobj
2 0 obj <</Type /Pages /Kids [3 0 R] /Count 1 /MediaBox [0 0 500 800]>>
endobj
3 0 obj<</Type /Page /Parent 2 0 R /Contents 4 0 R>>
endobj
4 0 obj
<</Length 10000>>
stream
'''

#their end section
part2 = '''
endstream
endobj
xref
0 5
0000000000 65535 f
0000000010 00000 n
0000000059 00000 n
0000000140 00000 n
0000000202 00000 n
trailer <</Size 5/Root 1 0 R>>
startxref
314
%%EOF'''
write = open('test.pdf', 'w')

write.write(part1 + decoded + part2)
```

I then opened the pdf I created:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/572126145743421460/unknown.png'>

flag: `actf{worthy_of_the_fields_medal}`
