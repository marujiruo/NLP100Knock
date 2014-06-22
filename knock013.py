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
#アカウントを見つける正規表現
re_acount = re.compile("([0-9a-zA-Z_]{1,15}) : ")
# RTを見つける正規表現
re_RT = re.compile("RT @[0-9a-zA-Z_]{1,15}: ")

# アカウントとマッチしたらツイートをMapに保存
# マッチしなかったらツイート末尾に文字列を追加
for line in open(sys.argv[1]):
	result_match = re_acount.match(line)
	if result_match is None:
		tweet = tweet + line
	else:
		if acount == "":
			pass
		else:
			tweet = tweet[:-1]
			tweet_dict[acount].append(tweet)
		acount = result_match.group(1)
		tweet = line[len(result_match.group()):]

for key, value in tweet_dict.items():
	for tweet in value:
		if re_RT.match(tweet) is None:
			result_match = re_RT.search(tweet)
			if result_match is None:
				pass
			else:
				print "@"+key+" :\n"+tweet,
				print "コメント部分のみ :\n"+tweet[:result_match.start()]
		else:
			pass