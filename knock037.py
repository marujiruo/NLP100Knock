# !usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict

bigram_dict = defaultdict(int)
for line in open(sys.argv[1]):
	bigram_dict[line.strip()]+=1

for key, value in bigram_dict.items():
	print str(value)+"\t"+key
