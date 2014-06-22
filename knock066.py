# !/usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict
import math

def norm_vector(vector):
	sum = 0
	for value in vector.values():
		sum += value*value
	return math.sqrt(sum)



if __name__ == '__main__':

	input_file = sys.argv[1]
	context_vector = defaultdict(lambda: defaultdict(int))

	# 文脈ベクトルの作成
	for line in open(input_file):
		line_split = line.strip().split("\t")
		context_vector[line_split[0].strip()][line_split[1].strip()]+=1

	# ベクトルの正規化
	for np, context_dict in context_vector.items():
		norm = norm_vector(context_vector[np])
		for context in context_dict.keys():
			context_vector[np][context]=float(context_vector[np][context])/norm

	# 出力
	for np, context_dict in context_vector.items():
		print np,
		for context, value in context_dict.items():
			print "\t"+context+":"+str(value),
		print ""
