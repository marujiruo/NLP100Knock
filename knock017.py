#!usr/bin/python
#coding:utf-8
import sys
import re
from collections import defaultdict

#人名っぽいを見つける正規表現
re_name = re.compile(u".{2,6}(さん|ちゃん|氏|くん)")

for line in open(sys.argv[1]):
	result_match = re_name.search(line.decode("utf-8"))
	if result_match is None:
		pass
	else:
		print result_match.group()
