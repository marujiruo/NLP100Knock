# !usr/bin/python
# coding:utf-8
import sys
from knock053 import *

text = createChunksText(sys.argv[1])

for sent in text:
	for dst_chunk in sent:
		if len(dst_chunk.srcs)>1:
			print "\n係り先 :",dst_chunk, "\n係り元 :"
			for src_chunk in sent:
				if src_chunk.ID in dst_chunk.srcs: print "\t",src_chunk
