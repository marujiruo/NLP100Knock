# !usr/bin/python
# coding:utf-8
import sys

preword = ""
for line in open(sys.argv[1]):
	if preword is "" or line.strip() is "":
		preword = line.strip()
		continue
	print preword+"\t"+line.strip()
	preword = line.strip()
