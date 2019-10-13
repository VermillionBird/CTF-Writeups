#!/usr/bin/python
import argparse
import sys

def find_invpow(x,n):
	high = 1
	while high ** n < x:
		high *= 2
	low = high/2
	while low < high:
		mid = (low + high) // 2
		if low < mid and mid**n < x:
			low = mid
		elif high > mid and mid**n > x:
			high = mid
		else:
			return mid
	return mid + 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Find the integer component of the nth root of a number')
	parser.add_argument('n', help='The index for the root',metavar='index',type=int)
	parser.add_argument('Number', help='The number to find the nth root of',metavar='number',type=int)
	args = parser.parse_args()

	x = args.Number
	n = args.n
	
	res = find_invpow(x,n)

	print "\n\nThe calculated root is: " + str(res)

	reshex = hex(res).replace('0x','').replace('L','')
	ascii = reshex.decode('hex')

	print "\nASCII of the calculated root is:"
	print ascii
	
	sys.exit()
