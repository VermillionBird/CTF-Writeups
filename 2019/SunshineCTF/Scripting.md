# Scripting Challenges
Writing code.
<br>
<br>
## 50 points: TimeWarp
```
Oh no! A t3mp0ral anoma1y has di5rup7ed the timeline! Y0u'll have to 4nswer the qu3stion5 before we ask them!

nc tw.sunshinectf.org 4101 (post competition: nc archive.sunshinectf.org 19004)

Author: Mesaj2000
```
I got this before they had to reduce the number of iterations. Nice.

Running the netcat command:

<img src="https://cdn.discordapp.com/attachments/532350033241309226/563521556282867729/unknown.png">

It appears as though we need to repeat back numbers, but we only get those numbers after we give an attempt. I wrote a bash script to do this, and after a bunch of research, got the following script:
```
for x in {0..100} #I tried 100 for a first guess, but it turned out to be around 400 or so, so I ran the script several times
do
t=$(echo "$(cat numbers) 2" | nc tw.sunshinectf.org 4101) #numbers was another file I had that started off empty, but eventually contained all of the numbers needed separated by spaces, change nc address post-competition to archive.sunshinectf.org 19004
l=1 #I set this for the while loop later, but this is the number of words I need to go back from the end of $t to get the number
i=$(echo $t | awk '{print $NF}') #This gets the last word, $NF is the last one.
echo $i #print the last word, which should hopefully be the flag. Originally, I printed the full $t to make sure the flag was the last word, so this code is more optimized.

while [ $l -gt 0 ] #As long as $i isn't the number I need to save to the file, then
do

if [[ $i =~ [^[:digit:]] ]] #Is $i not only digits?
then
j=$(echo $t | awk -v v=$l '{print $( NF-v )}') #This sets j to be the previous word, since the variable v is equal to $l
i=$j #set i to be j
l=$((l+1)) #add 1 to the value of $l, so the next iteration goes one word further back if necessary
else
l=0 #set it to be 0 to break the loop
fi #finish the if else clause
done #end the while loop
printf " %s" "$i" >> numbers #add the number to the end of numbers
done
```
Running my (messy) script gets me:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/563524749393920012/unknown.png'>

flag: `sun{derotser_enilemit_1001131519}`
<br>
<br>
<br>
## 250 points: Entry Exam
```
I heard the Hart Foundation is accepting applications, see if you have what it takes by completing their entry exam.
```
< a href='http://ee.sunshinectf.org'>http://ee.sunshinectf.org</a>
```
Author: dmaria
```
TBA
