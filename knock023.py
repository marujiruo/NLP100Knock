# !usr/bin/python
# coding:utf-8
import sys

for line in open(sys.argv[1]):
	for word in line.split(" "):
		print word
