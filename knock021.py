# !usr/bin/python
# coding:utf-8
import sys

for line in open(sys.argv[1]):
	for sentence in line.split("."):
		print sentence.strip()+"."

