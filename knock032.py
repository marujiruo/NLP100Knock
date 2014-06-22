# !usr/bin/python
# coding:utf-8
import sys
import marshal

mydict = {}
for line in open(sys.argv[1]):
	keyword = line.strip().split("|")
	if keyword[0] not in mydict:
		mydict[keyword[0]] = [(keyword[1], keyword[3], keyword[6])]
	else:
		mydict[keyword[0]].append((keyword[1], keyword[3], keyword[6]))

dump_file = open(sys.argv[2], "w")
marshal.dump(mydict, dump_file)
