#!usr/bin/python
#coding:utf-8
import sys

list = []
for line in open(sys.argv[1]):
	list.append(line.split('\t')[1].strip() + '\t' + line.split('\t')[0].strip())

for line in sorted(list, reverse = True):
	print line.split('\t')[1].strip() + '\t' + line.split(',')[0].strip()
