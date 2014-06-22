# !usr/bin/python
# coding:utf-8
import sys
from stemming.porter2 import stem

for line in open(sys.argv[1]):
	line = line.strip()
	if line is not "":
		print line+"\t"+stem(line.split("\t")[1])
