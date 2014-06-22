# !usr/bin/python
# coding:utf-8
import sys
import marshal

text = marshal.load(open(sys.argv[1]))
for sent in text:
	for morph in sent:
		if morph["pos"] == "動詞":
			print morph["surface"]

