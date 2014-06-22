# !usr/bin/python
# coding:utf-8
import sys
import marshal

text = marshal.load(open(sys.argv[1]))
for sent in text:
	for morph in sent:
		if morph["pos"] == "名詞" and morph["pos1"]=="サ変接続":
			print morph["surface"]

