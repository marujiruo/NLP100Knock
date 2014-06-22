# !usr/bin/python
# coding:utf-8
import sys
import marshal

dump_file = open(sys.argv[2], "r")
mydict = marshal.load(dump_file)

for line in open(sys.argv[1]):
	if line.strip() in mydict:
		for tpl in mydict[line.strip()]:
			print "\t".join([line.strip(), tpl[0], tpl[1], tpl[2]])

