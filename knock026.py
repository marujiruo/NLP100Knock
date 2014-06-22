# !usr/bin/python
# coding:utf-8
import sys
import re

re_nessly = re.compile("(ness|ly)$")
for line in open(sys.argv[1]):
	if re_nessly.search(line) is not None:
		print line.strip()
		