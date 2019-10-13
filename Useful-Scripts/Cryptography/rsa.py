#!/usr/bin/python
import sys
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
		print 'The modular inverse does not exist'
		sys.exit(1)
	else:
		return x % m

def decrypte(n,e,c,p = None,q = None, od = None, r = None):
	print '\n\n'
	if not r:
		r = (p - 1) * (q - 1)
	if p and q:
		if r != (p - 1) * (q - 1):
			r = (p - 1) * (q - 1)
			print "The provided Euler Totient is not equal to the calculated one.\n"
			print "Continuing with calculated Totient. Omit -p and -q and run again to use provided exponent..."
	d = modinv(e,r)
	if od != None:
		if d != od:
			print "The provided private exponent is not equal to the calculated one.\n"
			print "Continuing with calculated exponent. Omit -e and run again to use provided exponent..."
	print "Calculated Private Exponent: " + str(d) + "\n"
	m = pow(c,d,n)
	hexm = hex(m)
	hexm = hexm.replace('0x','').replace('L','')
	if len(hexm) % 2 != 0:
		hexm = '0' + hexm
	dec = hexm.decode('hex')
	print "Decrypted message:\n\n" + dec

def decryptd(c,d,n):
	print '\n\n'
	m = pow(c,d,n)
	hexm = hex(m)
	hexm = hexm.replace('0x','').replace('L','')
	if len(hexm) % 2 != 0:
		hexm = '0' + hexm
	dec = hexm.decode('hex')
	print "Decrypted message:\n\n" + dec
	
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Decrypt RSA. All provided values must be in decimal.\n',usage='%(prog)s -c CIPHERTEXT [OPTION]\nUse rsa.py -h for more details.')
	parser.add_argument('-c', required = True, help = 'Ciphertext in decimal. Must be provided', metavar = 'Ciphertext', type = int)
	parser.add_argument('-n', help = 'The Modulus', metavar = 'Modulus', type = int)
	parser.add_argument('-e', help = 'Public Encryption Exponent. This or -d must be provided.', metavar = 'Public Exponent', type = int)
	parser.add_argument('-d', help = 'Private Decryption Exponent. This or -e must be provided.', metavar = 'Private Exponent', type = int)
	parser.add_argument('-p', help = 'One of the Prime Factors', metavar = 'Factor1', type = int)
	parser.add_argument('-q', help = 'One of the Prime Factors', metavar = 'Factor2', type = int)
	parser.add_argument('-r', help = "Euler's Totient", metavar = 'Totient', type = int)
	

	args = parser.parse_args()
	c = args.c

	if args.e:
		e = args.e
		given = [args.p,args.q,args.n]
		if given.count(None) > 1:
			if args.r and args.n:
				n = args.n
				print "Calculating...\n"
				decrypte(n,e,c,None,None,r = args.r)
				sys.exit(0)
			else:
				parser.error("When e is provided, at least two out of -n, -p, and -q must be provided. You can also use the -r flag instead of -p and -q.")
		
		elif given.count(None) == 0:
			p = args.p
			q = args.q
			n = args.n
			if n != p * q:
				parser.error("The provided modulus -n was not equal to the product of the provided factors -p and -q.")

		elif args.p == None:
			q = args.q
			n = args.n
			if n % q == 0:
				p = n / q
			else:
				parser.error("q is not a factor of n")

		elif args.q == None:
			p = args.p
			n = args.n
			if n % p == 0:
				q = n / p
			else:
				parser.error("p is not a factor of n")

		else:
			p = args.p
			q = args.q
			n = p * q

		print "Calculating...\n"
		decrypte(n,e,c,p,q,od = args.d, r = args.r)

			
	elif args.d:
		d = args.d
		if not args.p or not args.q:
			if args.n:
				n = args.n
			else:
				parser.error("If the modulus -n is not provided, both -p and -q must be provided.")
		else:
			p = args.p
			q = args.q
			if args.n:
				n = args.n
				if n != p * q:
					parser.error("The provided modulus -n was not equal to the product of the provided factors -p and -q.")
			else:
				n = p * q

		print "Calculating...\n"
		decryptd(c,d,n)
	else:
		parser.error("Either -e or -d must be provided.")


