#!usr/bin/python
#coding:utf-8
# http://mitukiii.hatenablog.com/entry/2013/05/31/023156 
import sys
import re
from collections import defaultdict

text          = '[0-9A-Za-zぁ-ヶ一-龠]';
non_text      = '[^0-9A-Za-zぁ-ヶ一-龠]';
allow_text    = '[ovっつ゜ニノ三二]';
hw_kana       = '[ｦ-ﾟ]';
open_branket  = '[\(∩꒰（]';
close_branket = '[\)∩꒱）]';
arround_face  = '(?:' + non_text + '|' + allow_text + ')*';
face          = '(?!(?:' + text + '|' + hw_kana + '){3,}).{3,}';

re_face = re.compile(arround_face + open_branket + face + close_branket + arround_face)

for line in open(sys.argv[1]):
	result_match = re_face.search(line)
	if result_match is None:
		pass
	else:
		print result_match.group()
		