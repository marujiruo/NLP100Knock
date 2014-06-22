# !usr/bin/python
# coding:utf-8
import sys
from knock010 import *

bigramlist=[]
preword = ""
for word in open(sys.argv[1]):
	word = word.strip()
	if preword is "" or word is "":
		preword = word
	else:
		bigramlist.append(preword+" "+word)
		preword = word
print_freq(bigramlist)
