# !usr/bin/python
# coding:utf-8
import sys
import os
import CaboCha
import codecs

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
	corpus_dir = sys.argv[1]
	target_dir = sys.argv[2]

	files = get_files(corpus_dir)
	cabo_parser = CaboCha.Parser()
	for file_name in files:
		f = codecs.open(target_dir + file_name.split("/")[-1] + ".cabo", "w", "utf-8")
		for line in open(file_name):
			str = cabo_parser.parse(line.strip()).toString(CaboCha.FORMAT_LATTICE)
			f.write(str.decode("utf-8"))
		f.close()

