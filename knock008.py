#!usr/bin/python
#coding:utf-8
import sys

list = []
for line in open(sys.argv[1]):
	list.append((line.split('\t')[0].strip(), line.split('\t')[1].strip()))

for line1, line2 in sorted(list, key = lambda x : x[1]):
	print line1 + '\t' + line2
