#!usr/bin/python
#coding:utf-8
# http://php.o0o0.jp/article/php-split_address
import sys
import re
from collections import defaultdict

re_address = re.compile(u"((?![0-9])[0-9]{3}(?![0-9])-[0-9]{4}(?![0-9]))*[一-龠]{2,3}県.{2,10}(市|町|村)")
#re_address = re.compile("(東京都|北海道|(?:京都|大阪)府|.{6,9}県)((?:四日市|廿日市|野々市|かすみがうら|つくばみらい|いちき串木野)市|(?:杵島郡大町|余市郡余市|高市郡高取)町|.{3,12}市.{3,12}区|.{3,9}区|.{3,15}市(?=.*市)|.{3,15}市|.{6,27}町(?=.*町)|.{6,27}町|.{9,24}村(?=.*村)|.{9,24}村)(.*)")

for line in open(sys.argv[1]):
	result_match = re_address.search(line)
	if result_match is None:
		pass
	else:
		print result_match.group()
		