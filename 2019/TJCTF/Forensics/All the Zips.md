# All the Zips
### Forensics: 20 points
#### Solved by: Vermillion
```
Written by boomo

140 zips in the zip, all protected by a dictionary word.
```
<a href="https://static.tjctf.org/41f4419f4ba027561f22df9fabb56589205c4ec4bf47fa49d5e07cc3910d6d4f_all_the_zips.zip">All the zips</a>

I downloaded the zips and extracted the zip to a directory called all_the_zips. True to word, there were 140 zips inside the zip. Furthermore, each zip was password protected and had their own version of `flag.txt`.

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567829764082237450/unknown.png'>

`zip2john` allows you to find the john crackable hash of a zip. Using the command looks like this:

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567830949363187735/unknown.png'>

The first thing I did was to get the hashes of all the zips by writing the following script:
```
files=*.zip;
for file in $files; do
zip2john ${file} | cut -d ':' -f 2 > ${file}.hash #this only removes the hash from the zip2john output, the rest is ignored
done
```
I now had the directory populated with all of the hashes. The hashes were different as well, indicating different passwords for each, and some zip files did not output a hash (e.g. zip1.zip.hash).

<img src='https://cdn.discordapp.com/attachments/532350033241309226/567830328786550799/unknown.png'>

The next thing I did was to get John the Ripper to crack all of them using John's default dictionary:
```
files=*.zip.hash
for file in ${files}
do
echo ${file}
john ${file}
done
```
This cracked all of the zip hashes and stored them in the John directory. Some files did not have a dictionary password, so I skipped those, not wanting to spend time cracking them incrementally. However, you could have let John run and crack all of them. I wrote one last script to unzip all of the zip files and cat the flag.txt:
```
files=*.zip
for file in ${files}
do
pw=$(john --show ${file}.hash | grep ":" | cut -c 3-)
unzip  -o -P ${pw} ${file} #-o allows overwriting
cat flag.txt | grep "tjctf"
done
```
<img src='https://cdn.discordapp.com/attachments/532350033241309226/567833147304050836/unknown.png'>

flag: `tjctf{sl4m_1_d0wn_s0_that_it5_heard}`

Note: the last script will occasionally print an unzip help page; this occurs if you skip the cracking of the password for that file because its password isn't a word in the wordlist. Also, if you want to know, the password for zip85 was 'every'.
