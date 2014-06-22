#!usr/bin/python
#coding:utf-8
import sys
from collections import defaultdict

mydict = defaultdict(lambda:0)
for line in open(sys.argv[1]):
	mydict[line.split('\t')[0].strip()]

print len(mydict)