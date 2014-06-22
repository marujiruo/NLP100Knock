#!usr/bin/python
#coding:utf-8
import sys
import re

#仙台市っぽい住所を見つける正規表現
re_address = re.compile("仙台市.{2,10}(町|区).+[0-9]+-[0-9]+-[0-9]")

for line in open(sys.argv[1]):
	result_match = re_address.search(line)
	if result_match is None:
		pass
	else:
		print result_match.group()

