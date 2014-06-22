# !usr/bin/python
# coding:utf-8
import sys
import marshal
from optparse import OptionParser

parser = OptionParser(usage=u"%prog [-v] [--v2] [--sn] [--ab] [--nn] dumpfile")
parser.add_option('-v', '--v1',action='store_true', help=u"全ての動詞を抜き出す(42)")
parser.add_option('--v2',action='store_true', help=u"全ての動詞の原型を抜き出す(43)")
parser.add_option('--sn',action='store_true', help=u"全てのサ変名詞を抜き出す(44)")
parser.add_option('--ab',action='store_true', help=u"全ての「AのB」という表現を抜き出す(45)")
parser.add_option('--nn',action='store_true', help=u"全ての名詞の連接を抜き出す(46)")
parser.set_defaults(
        v1=False,
        v2=False,
        sn=False,
        ab=False,
        nn=False,
        )
options, args = parser.parse_args()
if len(args)>0:
	text = marshal.load(open(args[0]))

	if options.v1:
		# print "全ての動詞を抜き出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "動詞":
					print morph["surface"]
	if options.v2:
		# print "全ての動詞の原型を抜出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "動詞":
					print morph["surface"], morph["base"]
	if options.sn:
		# print "全てのサ変名詞を抜き出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "名詞" and morph["pos1"]=="サ変接続":
					print morph["surface"]
	if options.ab:
		# print "全ての「AのB」という表現を抜き出す"
		for sent in text:
			pre_morph = {"surface":"", "pos":"", "pos1":""}
			prepre_morph = {"pos":""}
			for morph in sent:
				if prepre_morph["pos"]=="名詞" and morph["pos"]=="名詞" \
					and pre_morph["surface"]=="の" and pre_morph["pos"]=="助詞" and pre_morph["pos1"]=="連体化":
					print prepre_morph["surface"]+""+pre_morph["surface"]+""+morph["surface"]
				prepre_morph = pre_morph
				pre_morph = morph
	if options.nn:
		# print "全ての名詞の連接を抜き出す"
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
