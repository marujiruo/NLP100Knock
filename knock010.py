#!usr/bin/python
#coding:utf-8
import sys
from collections import defaultdict

def print_freq(wordlist):
	mydict = defaultdict(lambda:0)
	for line in wordlist:
		mydict[line.strip()] += 1

	for key, value in sorted(mydict.items(), key=lambda x:x[1], reverse = True):
		print key + "\t頻度:"+str(value)

if __name__ == '__main__':
	print_freq(sys.argv[1])
	