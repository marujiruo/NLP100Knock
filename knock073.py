#!/usr/bin/python
#coding:utf-8
import sys
from knock072 import *

dir_path = sys.argv[1]

np_list = []
for text in get_docs_list(dir_path):
    for sent in text:
        np = []
        inFlag = False
        for tok in sent:
            if tok["chunk"] == "B-NP" and not inFlag:
                np.append(tok)
                inFlag = True
            elif tok["chunk"] == "B-NP" and inFlag:
                np_list.append(np)
                np = []
                np.append(tok)
            elif tok["chunk"] == "I-NP" and inFlag:
                np.append(tok)
            else:
                if len(np) != 0:
                    np_list.append(np)
                    np = []
                inFlag = False

# 出力
for np in np_list:
    print "# "+" ".join([tok["w"] for tok in np])
