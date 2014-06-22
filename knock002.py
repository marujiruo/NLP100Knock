#!/usr/bin/python
#-*- coding:utf8 -*-
import sys

for line in open(sys.argv[1]):
	print line.strip().replace('\t', ' ')
