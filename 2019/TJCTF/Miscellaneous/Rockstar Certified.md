# Rockstar Certified
### Miscellaneous: 50 points
#### Solved by: Vermillion

`Written by boomo`

`Tommy is a Certified Rockstar Developer! That means he can code in the `<a href='https://github.com/dylanbeattie/rockstar/blob/master/spec.md'>rockstar</a>` programming language.`

`I've known him for years but last week I saw him dealing with some shady, cultist-y people, exchanging numbers and dates. Just last night, I saw him working on some program called `<a href='https://static.tjctf.org/b58e1fb8016943a7d3d980340ee707b201985a37d4b96dff5b511ab481658613_ritual.rock'>ritual.rock</a>`. He typed in a number I couldn't see, then the number 1337. The program gave the output 'November 18.' The thing is, November 18th is my favorite day and 1337 is my second favorite number. If the first number he put in is my favorite, I think Tommy here might be a bit of a stalker. And I don't want a cowboy from ram ranch following me around.`

`Note: the flag is in the format tjctf{[first_number]}`


ritual.rock:

```
Void takes Something
Everything is a disposable, invariable, unoriginal expression
Nothingness is nothing
While Something is not Nothingness and Nothingness is less than Everything
Build Nothingness up

Give back Nothingness

The Earth takes Life and Death
Until Death is stronger than Life
Put Life without Death into Life

Give back Life

His Reincarnation takes my soul and your blood
His Life is nothing
While my soul is as high as your blood
Put my soul without your blood into my soul
Build His Life up

Give back His Life

Listen to your whispers
Put Void taking them into Ice
Listen to your screams
Put Void taking them into Fire
Energy is ki
Put Energy without Energy into Ashes
Put Energy over Energy into Potential
While Ice is stronger than nothing or Fire is stronger than nothing
Put The Earth taking Ice and Energy into Wind
Put The Earth taking Fire and Energy into Earth
Put His Reincarnation taking Ice and Energy into Ice
Put His Reincarnation taking Fire and Energy into Fire
if Wind is stronger than Earth or Earth is stronger than Wind
Put Ashes with Potential into Ashes

Put Potential of Energy into Potential

His Heart was 'n us
Put His Reincarnation taking Ashes and His Heart into Space
Put The Earth taking Ashes and His Heart into Flow
Put "Mysterious " into Time
if Flow is 1
Put "January " into Time

if Flow is 2
Put "February " into Time

if Flow is 3
Put "March " into Time

if Flow is 4
Put "April " into Time

if Flow is 5
Put "May " into Time

if Flow is 6
Put "June " into Time

if Flow is 7
Put "July " into Time

if Flow is 8
Put "August " into Time

if Flow is 9
Put "September " into Time

if Flow is 10
Put "October " into Time

if Flow is 11
Put "November " into Time

if Flow is 12
Put "December " into Time

Whisper Time with Space
```
Going to the first link, I start to be able to understand what the code is doing. With some extra research, I found that:
<ul>
  <li>Void, Earth, and Reincarnation are functions, where 'takes' denotes arguments and 'Put' calls it</li>
  <li>Variables can be preceded by a proper noun; they don't affect anything</li>
  <li>Certain strings have a numerical value, so if a variable is set to text it actually is a number (e.g 'ki' is 2)</li>
  <li>Loops, if clauses, and functions are ended with new lines; so the empty newlines are important</li>
  <li>Other english terms denotes arithmetic (without is minus), so the entire thing seems like lyrics</li>
  <li>Rockstar is kinda cool</li>
  <li>Online interpreters don't work, probably because of some missed formatting</li>
  <li>It's kinda hard to just understand it straight up</li>
</ul>
My native language is Python, so I wanted to see if I could find a way to convert it for me before rewriting it manually in python. I searched 'rockstar to python' and found two python libraries. The first one appeared to be a joke; I'm not sure but I didn't look into it. <a href='https://pypi.org/project/rockstar-py/'>The second one</a> seemed like a hit.

I followed the installation instructions, and ran `rockstar-py --output=ritual.py ritual.rock`. Opening ritual.py, it seemed that it didn't quite manage to format everything properly in terms of indents. Everything else seemed right. So I went through and deleted a lot of indents, keeping in mind that an empty newline should close the parent if, function, or loop. The correct code should become:
```
def Void(Something):
    Everything = 10000                                              #'a disposable, invariable, unoriginal expression' is 10000
    Nothingness = False
    while Something != Nothingness and Nothingness < Everything:
        Nothingness += 1
                                                                    #empty line here ends the while loop
    return Nothingness
                                                                    #empty line here ends the Void definition
def the_earth(Life, Death):
    while not Death > Life:
        Life = Life - Death
                                                                    #empty line here ends the while loop
    return Life
                
def his_reincarnation(my_soul, your_blood):
    his_life = False
    while my_soul >= your_blood:
        my_soul = my_soul - your_blood
        his_life += 1
                                                                    #empty line here ends the while loop
    return his_life
                                                                    #empty line here ends the his_reincarnation definition                     
your_whispers = input()
Ice = Void(your_whispers)
your_screams = input()
Fire = Void(your_screams)
Energy = 2
Ashes = Energy - Energy
Potential = Energy / Energy
while Ice > False or Fire > False:
    Wind = the_earth(Ice, Energy)
    Earth = the_earth(Fire, Energy)
    Ice = his_reincarnation(Ice, Energy)
    Fire = his_reincarnation(Fire, Energy)
    if Wind > Earth or Earth > Wind:
    	Ashes = Ashes + Potential
                                                                    #empty line here ends the if clause    
    Potential = Potential * Energy
                                                                    #empty line here ends the while loop    
his_heart = 12
Space = his_reincarnation(Ashes, his_heart)
Flow = the_earth(Ashes, his_heart)
Time = "Mysterious "
if Flow == 1:
	Time = "January "
                                                                    #empty line here ends the if clause
if Flow == 2:
	Time = "February "
                                                                    #empty line here ends the if clause
if Flow == 3:
	Time = "March "
                                                                    #empty line here ends the if clause
if Flow == 4:
	Time = "April "
                                                                    #empty line here ends the if clause
if Flow == 5:
	Time = "May "
                                                                    #empty line here ends the if clause
if Flow == 6:
	Time = "June "
                                                                    #empty line here ends the if clause
if Flow == 7:
	Time = "July "
                                                                    #empty line here ends the if clause
if Flow == 8:
	Time = "August "
                                                                    #empty line here ends the if clause
if Flow == 9:
	Time = "September "
                                                                    #empty line here ends the if clause
if Flow == 10:
	Time = "October "
                                                                    #empty line here ends the if clause
if Flow == 11:
	Time = "November "
                                                                    #empty line here ends the if clause
if Flow == 12:
	Time = "December "
```
Which is about what I expected from my own understanding. Now that I have the correct code, I just added a loop around the main portion of the code to test a bunch of numbers for the first input, and set the second input to 1337. Final code:
```
def Void(Something):
    Everything = 10000
    Nothingness = False
    while Something != Nothingness and Nothingness < Everything:
        Nothingness += 1
        
    return Nothingness
        
def the_earth(Life, Death):
    while not Death > Life:
        Life = Life - Death
        
    return Life
                
def his_reincarnation(my_soul, your_blood):
    his_life = False
    while my_soul >= your_blood:
        my_soul = my_soul - your_blood
        his_life += 1
        
    return his_life
for num in range(10000):                        
	your_whispers = num
	Ice = Void(your_whispers)
	your_screams = 1337
	Fire = Void(your_screams)
	Energy = 2
	Ashes = Energy - Energy
	Potential = Energy / Energy
	while Ice > False or Fire > False:
	    Wind = the_earth(Ice, Energy)
	    Earth = the_earth(Fire, Energy)
	    Ice = his_reincarnation(Ice, Energy)
	    Fire = his_reincarnation(Fire, Energy)
	    if Wind > Earth or Earth > Wind:
	    	Ashes = Ashes + Potential
	    
	    Potential = Potential * Energy
	    
	his_heart = 12
	Space = his_reincarnation(Ashes, his_heart)
	Flow = the_earth(Ashes, his_heart)
	Time = "Mysterious "
	if Flow == 1:
		Time = "January "

	if Flow == 2:
		Time = "February "

	if Flow == 3:
		Time = "March "

	if Flow == 4:
		Time = "April "

	if Flow == 5:
		Time = "May "

	if Flow == 6:
		Time = "June "

	if Flow == 7:
		Time = "July "

	if Flow == 8:
		Time = "August "

	if Flow == 9:
		Time = "September "

	if Flow == 10:
		Time = "October "

	if Flow == 11:
		Time = "November "

	if Flow == 12:
		Time = "December "

	if str(Time) + str(Space) == "November 18":  #Test to see if number is correct
		print num
		break
```
Running the code, it returns 1498. The description states that the flag is `tjctf{[first number]}`, so our flag is found.

flag: `tjctf{1498}`

Man I'm such a ROCKSTAR programmer.
