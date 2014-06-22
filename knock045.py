# !usr/bin/python
# coding:utf-8
import sys
import marshal

text = marshal.load(open(sys.argv[1]))
for sent in text:
	pre_morph = {"surface":"", "pos":"", "pos1":""}
	prepre_morph = {"pos":""}
	for morph in sent:
		if prepre_morph["pos"]=="名詞" and morph["pos"]=="名詞" \
			and pre_morph["surface"]=="の" and pre_morph["pos"]=="助詞" and pre_morph["pos1"]=="連体化":
			print prepre_morph["surface"]+""+pre_morph["surface"]+""+morph["surface"]
		prepre_morph = pre_morph
		pre_morph = morph

