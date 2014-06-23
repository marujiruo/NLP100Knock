# !usr/bin/python
# coding:utf-8
import sys
import os
import math
from collections import defaultdict

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
	input_dir = sys.argv[1]
	files = get_files(input_dir)
	tf_dict = defaultdict(int)
	df_dict = defaultdict(list)
	idf_dict = {}
	fileNum = len(files)

	# calc tf
	for file_name in files:
		for line in open(file_name):
			tf_dict[line.strip().split("\t")[0]] += 1
	# calc df
	for file_name, num in zip(files, range(0, fileNum)):
		for line in open(file_name):
			df_dict[line.strip().split("\t")[0]].append(num)
	for noun in df_dict.keys():
		df_dict[noun] = len(set(df_dict[noun]))

	#calc idf
	for noun in tf_dict.keys():
		idf_dict[noun] = math.log(float(fileNum)/df_dict[noun] ,2)

	# output
	for noun in tf_dict.keys():
		print noun, "\t", tf_dict[noun]*idf_dict[noun], "\t", tf_dict[noun], "\t", df_dict[noun]
