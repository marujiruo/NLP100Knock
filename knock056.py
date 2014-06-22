# !usr/bin/python
# coding:utf-8
import sys
from knock053 import *

text = createChunksText(sys.argv[1])

for sent in text:
	for src_chunk in sent:
		for dst_chunk in sent:
			if src_chunk.dst==dst_chunk.ID and src_chunk.inPos("名詞") and dst_chunk.inPos("動詞"):
				print str(src_chunk)+"\t"+str(dst_chunk)
