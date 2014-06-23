#!usr/bin/python
#coding:utf-8
import sys

print "graph knock069 {"
for line in open(sys.argv[1]):
	line = line.replace('\"', r'\"') 
	print "\t\""+line.strip().split("\t")[1]+"\" -- \""+line.strip().split("\t")[2]+"\";"
print "}"
