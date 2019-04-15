# Checker
### Reversing: 30 points
#### Solved by: Vermillion
```
 Written by rj9

Found a flag checker program that looked pretty sketchy. Take a look at it.
```
<a href='https://static.tjctf.org/2e328993c4d64ddf9ff69b2f8929e5d4a494e480da0e56f8373062b212a97258_Checker.java'>file</a>

Ok, they actually changed the challenge after I solved it because they were missing a crucial function that made it NOT horrible. My file looked like this:
```
import java.util.*;
public class Checker{
    public static String wow(String b, int s){
        String r = "";
        for(int x=s; x<b.length()+s; x++){
            r+=b.charAt(x%b.length());
        }
        return r;
    }
    public static String woah(String b){
        String r = "";
        for(int x=0; x<b.length(); x++){
            if(b.charAt(x)=='0')
                r+='1';
            else
                r+='0';
        }
        return r;
    }
    public static String encode(String plain){
        String b = "";
        Stack<Integer> t = new Stack<Integer>();
        for(int x=0; x<plain.length(); x++){
            int i = (int)plain.charAt(x);
            t.push(i);
        }
        for(int x=0; x<plain.length(); x++){
            b+=Integer.toBinaryString(t.pop());
        }
        b = woah(b);
        b = wow(b,9);
        System.out.println(b);
        return b;
    }
    public static boolean check(String flag, String encoded){
        if(encode(flag).equals(encoded))
            return true;
        return false;
    }
    public static void main(String[] args){
        String flag = "redacted";
        String encoded = "1100001110000111000011000010100001110000111000010100001110000010000110010001011001110000101010001011000001000";
        System.out.println(check(flag,encoded));
    }
}
```

I copied it into <a href='https://www.jdoodle.com/online-java-compiler'>JDoodle</a>. Looking at the code, I figured out what it was doing. It took the flag string and encoded it by:
<ol>
  <li>Converting each character to its ASCII number</li>
  <li>Reversing the order of the numbers</li>
  <li>Converting each number in the reversed order into binary WITHOUT PADDING and concatenating them</li>
  <li>Taking each bit in the string and performing a logical NOT operation on it</li>
  <li>And performing a LEFT-CIRC of 9 on the string</li>
</ol>
It then compared it to its expected output: 

```
1100001110000111000011000010100001110000111000010100001110000010000110010001011001110000101010001011000001000
```

Knowing this, I began to figure out the flag. I first moved the last 9 bits to the front, and then performed a logical NOT on the string. Since there was no padding, I knew that each letter was only encoded by 7 bits, but at the same time, I noticed that the string was NOT divisible by 7, but rather was missing 3 bits. Therefore, there had to be 3 0s somewhere in the string.
```
1111101110011110001111000111100111101011110001111000111101011110001111101111001101110100110001111010101110100
```
Since the string was reversed, I first pulled the '} from the front of the string ('1111101') and '{ftcjt' from the end ('01111101 01100110 01110100 01100011 01101010 01110100') to get the string:
```
110011110001111000111100111101011110001111000111101011110001
```
I now had to figure out where to add more 0s. After a long, painstaking trial and error process using this <a href='http://www.unit-conversion.info/texttools/convert-text-to-binary/'>website</a> and adding 0s until it made sense, I got the padded string:
```
00110011
01100011
00110001
01110011
01101011
01100011
00110001
01110101
01110001
```
Which translated into 3c1skc1uq, or in the correct order: `qu1cks1c3`.

flag: `tjctf{qu1cks1c3}`

After I solved it, I mentioned it to the author, and they added a padding function, making the challenge a LOT easier. Like, a LOT easier.
