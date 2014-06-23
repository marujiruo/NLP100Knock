# !usr/bin/python
# coding:utf-8
import sys
import os
from knock053 import *

#ディレクトリ内のファイルリストを返す
def get_files(dirpath):
	flist =[]
	for root, dirs, files in os.walk(dirpath):
		for file in files:
			path = os.path.join(root, file)
			if os.path.isfile(os.path.join(path)):
				flist.append(path)
	return flist

# 名詞句\t名詞句が係る周辺単語\t名詞句に係る周辺単語\t...
if __name__ == '__main__':
	corpus_dir = sys.argv[1]
	target_dir = sys.argv[2]

	files = get_files(corpus_dir)
	for cfile_name in files:
		print cfile_name
		tfile = open(target_dir + cfile_name.split("/")[-1] +".n", "w")
		for sent in createChunksText(cfile_name):
			for chunk in sent:
				if chunk.getNP() is not None:
					# 名詞句
					np = "".join(morph.base for morph in chunk.getNP())
					# 係り先の周辺単語
					if chunk.dst == -1:
						dst = "None"
					elif sent[chunk.dst].morphs[sent[chunk.dst].head].isIndipendent():
						dst = sent[chunk.dst].morphs[sent[chunk.dst].head].base
					else:
						dst = "None"
					# 係り元の周辺単語
					srcs = [sent[src].morphs[sent[src].head].base for src in chunk.srcs if sent[src].morphs[sent[src].head].isIndipendent()]
					if len(srcs)==0:
						srcs.append("None")
					tfile.write(np + "\t" + dst + "\t" + "\t".join(srcs)+"\n")
		tfile.close()
