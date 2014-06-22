# !usr/bin/python
# coding:utf-8
import sys

for line in open(sys.argv[1]):
	if line != "\n":
		print line.strip()+"\t"+line.strip().lower()
	else:
		print ""
		