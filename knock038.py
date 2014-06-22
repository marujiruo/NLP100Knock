# !usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict

bigram_dict = {}
unigram_dict = defaultdict(int)
for line in open(sys.argv[1]):
	words = line.strip().split("\t")
	bigram_dict[words[1]+"\t"+words[2]] = words[0]
	unigram_dict[words[1]]+=int(words[0])

for key, value in bigram_dict.items():
	print str(float(value)/unigram_dict[key.split("\t")[0]])+"\t"+key
