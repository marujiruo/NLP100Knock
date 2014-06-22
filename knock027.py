# !usr/bin/python
# coding:utf-8
import sys
from knock010 import *

wordlist=[]
for word in open(sys.argv[1]):
	wordlist.append(word)
print_freq(wordlist)
