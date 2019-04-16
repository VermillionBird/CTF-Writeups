# Sight at Last
### Miscellaneous: 100 points
#### Solved by: Vermillion
```
Written by jfrucht25

nc p1.tjctf.org 8005
```
Netcatting into the service, we see:
```
To get the flag, solve a hundred captchas in 500 seconds!
Find the minimum distance between the centers of two circles to continue:
```
Followed by a huge string of base64 that I won't paste here.. It mentioned two circles, so I wondered if this was an image encoded in base64, so I found an <a href='https://codebeautify.org/base64-to-image-converter'>online converter</a> and it was. The image is randomly generated each time, so here's an example of the decoded image:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567815679550685185/unknown.png'>

Clearly, we have to be able to find the center of all the circles, and find a minimum distance between them all. And do that several times within 500 seconds. But first, we had to be able to pull the captcha, so I wrote a script to do so:
```
from pwn import *
from base64 import *
r = remote('p1.tjctf.org', 8005)

print r.recvuntil('\n')
print r.recvuntil('\n')
x = r.recvuntil('\n')
decoded = decodestring(x)                   #base64 function that decodes a base64 string
with open('decodedimage','wb') as fil:
	fil.write(decoded)
```
Testing it out, it worked, and we now had a file called decodedimage that contained our captcha. Next, I had to find a way to find the distances between the centers of circles. After a long time of searching and trying different things, I found this <a href='https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/'>website</a>, and took the following script. I added comments where I had to change some things due to changes in the OpenCV module since the article was published.
```
from pwn import *
from base64 import *
r = remote('p1.tjctf.org', 8005)

print r.recvuntil('\n')
print r.recvuntil('\n')
x = r.recvuntil('\n')
decoded = decodestring(x)
with open('decodedimage','wb') as fil:
	fil.write(decoded)

import cv2

# read image through command line
img = cv2.imread('decodedimage')                        #Changed to just automatically read the decodedimage file.
 
# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,0)
 
# find contours in the binary image
contours,a = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #It used to have 3 variables, but im2 was removed, and 'a' is a throwaway variable. All we really need are the contours
contours.pop(0)                           #Normally, the overall background is the first element in the list, so I popped it.
for c in contours:
  # calculate moments for each contour
  M = cv2.moments(c)
 
  # calculate x,y coordinate of center
  cX = int(M["m10"] / M["m00"])
  cY = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)                                                    #Changed color
  cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)   #Changed color
 
  # display the image
  cv2.imshow("Image", img)
  cv2.waitKey(0)
```
It now created the image from the base64, opened the file, and found all of the centers. It opened a new window where everytime you pressed a key a new center would label another circle's center. 

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567821379664085002/unknown.png'>

I changed the script to not open the image and instead just write all of the centers to a list, and then added a script to find the minimum distance:
```
from pwn import *
from base64 import *
r = remote('p1.tjctf.org', 8005)

print r.recvuntil('\n')
print r.recvuntil('\n')
x = r.recvuntil('\n')
decoded = decodestring(x)
with open('decodedimage','wb') as fil:
	fil.write(decoded)

import cv2

# read image through command line
img = cv2.imread(decodedimage)
 
# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,0)
 
# find contours in the binary image
contours,a = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
centers = []
contours.pop(0)
for c in contours:
  # calculate moments for each contour
  M = cv2.moments(c)
 
  # calculate x,y coordinate of center
  cX = int(M["m10"] / M["m00"])
  cY = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)
  cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
 
  # display the image
  cv2.imshow("Image", img)
  centers.append((cX,cY))

from math import sqrt
distances = []
for point in centers:
	for point2 in centers:
		d = sqrt((point[0]-point2[0])**2+(point[1]-point2[1])**2)
		if d != 0.0:
			distances.append(d)
print min(distances)
print str(int(round(min(distances))))
r.sendline(str(int(round(min(distances)))))
print r.recvuntil('\n')
```
Running the code, it succesfully passed the captcha and pulled the next one. Therefore, all I had to do was to wrap it in a loop:
```
from pwn import *
from base64 import *
r = remote('p1.tjctf.org', 8005)

for i in range(500):
	print r.recvuntil('\n')
	print r.recvuntil('\n')
	x = r.recvuntil('\n')
	decoded = decodestring(x)
	with open('decodedimage','wb') as fil:
		fil.write(decoded)

	import cv2
	# read image through command line
	img = cv2.imread('decodedimage')
	 
	# convert the image to grayscale
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	 
	# convert the grayscale image to binary image
	ret,thresh = cv2.threshold(gray_image,127,255,0)
	 
	# find contours in the binary imagesdf
	contours,a= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	centers = []
	contours.pop(0)
	for c in contours:
	   # calculate moments for each contour
	   M = cv2.moments(c)
	 
	   # calculate x,y coordinate of center
	   cX = int(M["m10"] / M["m00"])
	   cY = int(M["m01"] / M["m00"])
	   cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)
	   cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
	 
	   # display the image
	   cv2.imshow("Image", img)
	   centers.append((cX,cY))
	print centers
	from math import sqrt
	distances = []
	for point in centers:
		for point2 in centers:
			d = sqrt((point[0]-point2[0])**2+(point[1]-point2[1])**2)
			if d != 0.0:
				distances.append(d)
	print min(distances)
	print str(int(round(min(distances))))
	r.sendline(str(int(round(min(distances)))))
	print r.recvuntil('\n')
print r.recv()
print 'done'
```
I ran the script, and it usually worked. Sometimes, it would fail for seemingly no reason at random intervals, but I ran it multiple times, and eventually got lucky. The script took 7 seconds and returned the flag:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567820628015710209/unknown.png'>

flag: `tjctf{i5_th1s_c0mput3r_v1si0n?}`

Post competition: It appears as though the script occasionally fails to find some small circles near the edges for some reason. I don't know why.
