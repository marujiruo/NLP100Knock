# !usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict

mydict = defaultdict(list)
for line in open(sys.argv[1]):
	keyword = line.strip().split("|")
	mydict[keyword[0]].append((keyword[1], keyword[3], keyword[6]))

print "pleas in put text"
while True:
	text = raw_input()
	if text is "":
		print "exit"
		break;
	if text in mydict:
		print mydict[text]
	else:
		print "not found"
