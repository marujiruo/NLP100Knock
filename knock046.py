# !usr/bin/python
# coding:utf-8
import sys
import marshal

text = marshal.load(open(sys.argv[1]))
for sent in text:
	pre_morph = {"pos":""}
	mylist=[]
	pre_id = 0
	for morph in sent:
		if pre_morph["pos"]=="名詞" and morph["pos"]=="名詞":
			if pre_id == id(pre_morph):
				mylist.append(morph["surface"])
			else:
				print "  ".join(mylist)
				mylist=[]
				mylist.append(pre_morph["surface"])
				mylist.append(morph["surface"])
			pre_id = id(morph)
		pre_morph = morph
