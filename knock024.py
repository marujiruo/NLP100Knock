# !usr/bin/python
# coding:utf-8
import sys
import re

re_dotcomma = re.compile(r"(\.|,)$")
for line in open(sys.argv[1]):
	for word in line.strip().split(" "):
		if re_dotcomma.search(word) is not None:
			print word[:-1]
			print word[-1]
		else:
			print word
	print ""
	