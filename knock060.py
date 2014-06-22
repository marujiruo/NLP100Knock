#!usr/bin/python
#coding:utf-8
import sys

print "digraph knock060 {"
for line in open(sys.argv[1]):
	line = line.replace('\"', r'\"') 
	print "\t\""+line.strip().split("\t")[0]+"\" -> \""+line.strip().split("\t")[1]+"\";"
print "}"
