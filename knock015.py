#!usr/bin/python
#coding:utf-8
import sys
import re
from collections import defaultdict

#アカウントを見つける正規表現
re_acount = re.compile("@[0-9a-zA-Z_]{1,15}")

for line in open(sys.argv[1]):
	result_match = re_acount.search(line)
	if result_match is None:
		print line+"<br>"
	else:
		print re_acount.sub(r"<a href=\"https://twitter.com/#!/"+result_match.group()+r"\">"+result_match.group()+"</a>", line)+"<br>"
