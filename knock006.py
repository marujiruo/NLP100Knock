#!usr/bin/python
#coding:utf-8
import sys

list = []
for line in open(sys.argv[1]):
	list.append(line.strip())

for n in range(len(list)-int(sys.argv[2]), len(list)):
	print list[n]
