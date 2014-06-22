#!usr/bin/python
#coding:utf-8
import sys

count = 0;
for line in open(sys.argv[1]):
	if(count == int(sys.argv[2])):
		break
	count+=1;
	print line.strip()

