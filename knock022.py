# !usr/bin/pyton
# coding:utf-8
import sys
import re

re_sentence = re.compile(r"\. [A-Z]")
for line in open(sys.argv[1]):
	temp = line
	result_search = re_sentence.search(temp)
	while(result_search is not None):
		print temp[0:result_search.start()+1]
		temp = temp[result_search.start()+2:]
		result_search = re_sentence.search(temp)
	print temp.strip()