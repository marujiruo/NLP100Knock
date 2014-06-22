# !usr/bin/python
# coding:utf-8
import sys
from knock053 import *

text = createChunksText(sys.argv[1])

for sent in text:
	for src_chunk in sent:
		for dst_chunk in sent:
			# ↓は記号を含むchankを除いちゃったけど、記号のMorohだけ除くやつだった
			# if not src_chunk.inPos("記号") and not dst_chunk.inPos("記号") and src_chunk.dst==dst_chunk.ID:
			# 	print str(src_chunk)+"\t"+str(dst_chunk)
			if src_chunk.dst==dst_chunk.ID:
				print str(src_chunk.withoutPos("記号"))+"\t"+str(dst_chunk.withoutPos("記号"))
