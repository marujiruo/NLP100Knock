# !usr/bin/python
# coding:utf-8
import sys
import MeCab
import marshal

me = MeCab.Tagger("mecabrc")
text = []

for line in open(sys.argv[1]):
	result = me.parse(line.strip())
	sent = []
	for morph in result.split("\n"):
		if morph == "EOS":
			break
		d={}
		d["surface"]=morph.split("\t")[0]
		d["base"]=morph.split("\t")[1].split(",")[6]
		d["pos"]=morph.split("\t")[1].split(",")[0]
		d["pos1"]=morph.split("\t")[1].split(",")[1]
		sent.append(d)
	text.append(sent)
marshal.dump(text, open(sys.argv[2], "w"))
