# !/usr/bin/python
# coding:utf-8
import sys
import marshal
import os

#ディレクトリ内のファイルリストを返す
def get_files(dirpath):
	flist =[]
	for root, dirs, files in os.walk(dirpath):
		for file in files:
			path = os.path.join(root, file)
			if os.path.isfile(os.path.join(path)):
				flist.append(path)
	return flist

if __name__ == '__main__':
	dump_file = sys.argv[1]
	input_dir = sys.argv[2]

	files = get_files(input_dir)
	tfidf_list = marshal.load(open(dump_file))

	for file_name in files:
		for line in open(file_name):
			line_split = line.strip().split("\t")
			if line_split[0] in tfidf_list:
				print line_split[0], "\t->", line_split[1] 
				if len(line_split)>2:
					for src in line_split[2:]:
						print line_split[0], "\t<-", src



