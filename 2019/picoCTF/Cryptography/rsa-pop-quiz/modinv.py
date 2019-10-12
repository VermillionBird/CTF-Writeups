#!/usr/bin/python
import argparse, sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('The modular inverse does not exist')
    else:
        return x % m
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Find the modular multiplicative inverse of a number.')
    parser.add_argument('Number', help = 'The number to find the inverse of', metavar = 'a',type = int)
    parser.add_argument('Modulus', help = 'The modulus', metavar = 'm', type = int)
    args = parser.parse_args()

    a = args.Number
    m = args.Modulus

    try:
        print "The modular inverse of " + str(a) + " modulus " + str(m) + " is: " + str(modinv(a,m))
        sys.exit()
    except Exception:
        sys.exit("The modular inverse does not exist.")
