#!usr/bin/python
#-*-coding:utf-8-*-
import sys

for line in open(sys.argv[1]):
	print line.split('\t')[0]
