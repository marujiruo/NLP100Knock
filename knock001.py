#!/usr/bin/python
#-*- coding:utf8 -*-
import sys

lineCount = 0
for line in open(sys.argv[1]):
    lineCount+=1
print lineCount
