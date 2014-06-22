# !usr/bin/python
# coding:utf-8
import sys
import marshal

dump_file = open(sys.argv[2], "r")
mydict = marshal.load(dump_file)

for line in open(sys.argv[1]):
	if line.strip() not in mydict:
		print line.strip()
