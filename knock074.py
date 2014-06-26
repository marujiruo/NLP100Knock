#!/usr/bin/python
#coding:utf-8
import sys
from knock072 import *

dir_path = sys.argv[1]

np_list = []
inFlag = False
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
    if np[0]["pos"] == "DT":
        if np[0]["lem"] == "a" or np[0]["lem"] == "an"\
           or np[0]["lem"] == "A" or np[0]["lem"] == "An":
            print "A"
        elif np[0]["lem"] == "the" or np[0]["lem"] == "The":
            print "THE"
        # else:
        #     print "!!!!!!!!!!"+np[0]["lem"]
    else:
        print "NONE"
