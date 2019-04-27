## Lithp
### 60 points, 147 solves
`My friend gave me this `<a href='https://files.actf.co/b7bb1a50e52ba3f9ff93f4d08691a7eef81457410192f769b076a3052ff21b21/lithp.lisp'>program</a>` but I couldn't understand what he was saying - what was he trying to tell me?`

`Author: fireholder`

Opening the program, we see:
```
;LITHP

(defparameter *encrypted* '(8930 15006 8930 10302 11772 13806 13340 11556 12432 13340 10712 10100 11556 12432 9312 10712 10100 10100 8930 10920 8930 5256 9312 9702 8930 10712 15500 9312))
(defparameter *flag* '(redacted))
(defparameter *reorder* '(19 4 14 3 10 17 24 22 8 2 5 11 7 26 0 25 18 6 21 23 9 13 16 1 12 15 27 20))

(defun enc (plain)
    (setf uwuth (multh plain))
    (setf uwuth (owo uwuth))
    (setf out nil)
    (dotimes (ind (length plain) out)
        (setq out (append out (list (/ (nth ind uwuth) -1))))))
    
(defun multh (plain)
    (cond
        ((null plain) nil)
        (t (cons (whats-this (- 1 (car plain)) (car plain)) (multh (cdr plain))))))

(defun owo (inpth)
    (setf out nil)
    (do ((redth *reorder* (cdr redth)))
        ((null redth) out)
        (setq out (append out (list (nth (car redth) inpth))))))

(defun whats-this (x y)
    (cond
        ((equal y 0) 0)
        (t (+ (whats-this x (- y 1)) x))))

;flag was encrypted with (enc *flag*) to give *encrypted*
```
This is a lisp program, but every time there is an 's', it's replaced with 'th' as a joke (lisp). After a lot of researching lisp functions, methods, and syntax, I managed to understand the program. Lisp basically uses infix for everything. I rewrote the program in python:

```
encrypted = [8930, 15006, 8930, 10302, 11772, 13806, 13340, 11556, 12432, 13340, 10712, 10100, 11556, 12432, 9312, 10712, 10100, 10100, 8930, 10920, 8930, 5256, 9312, 9702, 8930, 10712, 15500, 9312]
flag = 'REDACTED'
reorder = [19, 4, 14, 3, 10, 17, 24, 22, 8, 2, 5, 11, 7, 26, 0, 25, 18, 6, 21, 23, 9, 13, 16, 1, 12, 15, 27, 20]

def whats_this(x, y):                     #just multplies its inputs
  return x*y

def muls(plain):                          #returns a list where every number n is replaced by n(n-1)
	lis = []
	for item in plain:
		lis.append(whats_this(1-item, item))  #As a reminder, whats_this is just multiplication
	return lis

def owo(inps):                            #uses the list reorder to reorder inps
	out = []
	for x in range(len(reorder)):
		out.append([inps[reorder[x]]])
  return out

def enc(plain):                           #Encrypts a list of numbers
	uwus = muls(plain)
	uwus = owo(uwus)
	out = []
	for x in range(len(plain)):
		out.append([uwus[x]/-1])              #Divides each number in the new list by -1 to make it positive
  return out

#flag was encrypted to give encrypted.
```
From here, I wrote a python program to reverse the encryption:
```
from math import sqrt

encrypted = [8930, 15006, 8930, 10302, 11772, 13806, 13340, 11556, 12432, 13340, 10712, 10100, 11556, 12432, 9312, 10712, 10100, 10100, 8930, 10920, 8930, 5256, 9312, 9702, 8930, 10712, 15500, 9312]
reorder = [19, 4, 14, 3, 10, 17, 24, 22, 8, 2, 5, 11, 7, 26, 0, 25, 18, 6, 21, 23, 9, 13, 16, 1, 12, 15, 27, 20]

decrypted = []
for i in range(len(encrypted)):
  char = encrypted[i]
  char *=-1                         #undos the negative one from the original script
  #-n^2+n - char = 0
  n = int((-1-sqrt(1-4*char))/-2)   #minus in the quadratic formula to get positive result
  decrypted.append(n)               #list of decrypted chars but is out of order

dic = {}
for x in range(len(reorder)):       #create a dictionary of (correct position, decrypted) pairs
  dic[reorder[x]] = decrypted[x]

decrypted = []
for x in range(len(dic)):           #correctly order the list
  decrypted.append(dic[x])

string = ''
for item in decrypted:              #create string
  string += chr(item)
  
print string
```
<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571816027768225842/unknown.png'>

flag: `actf{help_me_I_have_a_lithp}`
