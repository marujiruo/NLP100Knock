# !/usr/bin/python
# coding:utf-8
import sys
import re
import marshal

input_file = sys.argv[1]
output_file = sys.argv[2]

tfidf_dict={}
tfidf_list=[]
re_num = re.compile("[0-9]")
for line in open(input_file):
	line_strip = line.strip().split("\t")
	tfidf_dict[line_strip[0].strip()] = (float(line_strip[1]), line_strip[2], line_strip[3])
count = 0
for key, value in sorted(tfidf_dict.items(), key=lambda x:-x[1][0]):
	if re_num.search(key) is None:
		tfidf_list.append(key)
		# print key, value, count
		count +=1
	if count == 100:
		break
marshal.dump(tfidf_list, open(output_file, "w"))
