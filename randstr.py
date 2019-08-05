#!/usr/bin/env python3
# coding=utf-8
#
# random string generator
#
# imports
import string
import random
import argparse
import sys


def genstr(L):
	"""
	Random string generator.
	"""
	s = ''.join(random.choices(string.ascii_letters + string.digits, k=L))
	return s+'\n'


# main
def main():
	parser = argparse.ArgumentParser(description='Random string generator')
	parser.add_argument('-l', '--length', help='Specify the length of random string',
						type=int, required=True)

	args = parser.parse_args()
	length = args.length
	if(length <= 0):
		sys.exit("[-] The length cannot be negative")
	ranstr = ""
	ranstr = genstr(length)

	sys.stdout.write(ranstr)


# run
if __name__ == '__main__':
	main()
