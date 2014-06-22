#!usr/bin/python
#coding:utf-8
import sys
import re
from collections import defaultdict

# １つのツイート文字列,1つのアカウント
tweet = ""
acount = ""
# アカウントとツイートリストのMap
tweet_dict = defaultdict(list)
#第意の条件を満たす正規表現
re_jp = re.compile("([一-龠]+)\(([A-Z]+)\)")

for line in open(sys.argv[1]):
	result_match = re_jp.search(line)
	if result_match is None:
		pass
	else:
		print result_match.group(1)+'\t'+result_match.group(2)
