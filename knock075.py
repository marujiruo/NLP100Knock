#!/usr/bin/python
#coding:utf-8
import sys
from knock072 import *

dir_path = sys.argv[1]

np_list = []
inFlag = False
for text in get_docs_list(dir_path):
    prev_tok = None
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
            prev_tok = tok

# 出力
for np in np_list:
    print "# "+" ".join([tok["w"] for tok in np])

    article = "NONE"
    wm1 = ""
    fw = ""
    fpos = ""
    w0 = ""
    fwfpos = ""
    hw = ""
    hwhpos = ""
    pos1 = ""
    hpos = ""
    posm1 = ""
    w1 = ""

    # article
    if np[0]["pos"] == "DT":
        if np[0]["lem"] == "a" or np[0]["lem"] == "an"\
           or np[0]["lem"] == "A" or np[0]["lem"] == "An":
            article = "A"
        elif np[0]["lem"] == "the" or np[0]["lem"] == "The":
            article = "THE"
    else:
        article = "NONE"
    # wm1 名詞句の1語前の単語
    if np[0]["prev"] is not None:
        wm1 = np[0]["prev"]["w"]

    # w1 名詞句の一語後の単語
    if np[-1]["next"] is not None:
        w1 = np[-1]["next"]["w"]

    # fw 先頭の単語
    if np[0]["pos"] == "DT" and len(np) > 1:
        fw = np[1]["w"]
    else:
        fw = np[0]["w"]

    # fpos 先頭の品詞
    if np[0]["pos"] == "DT" and len(np) > 1:
        fpos = np[1]["pos"]
    else:
        fpos = np[0]["pos"]

    # w0 名詞句の単語列
    if np[0]["pos"] == "DT" and len(np) > 1:
        w0 = " ".join(t["w"] for t in np[1:])
    else:
        w0 = " ".join(t["w"] for t in np)

    # fw|fpos 先頭の単語|先頭の品詞
    fwfpos = fw+"|"+fpos

    # hw 末尾の単語
    hw = np[-1]["w"]

    # hpos 末尾の品詞
    hpos = np[-1]["pos"]

    # hw|hpos 末尾の単語|末尾の品詞
    hwhpos = hw+"|"+hpos

    # posm1 名詞句の一語前の品詞
    if np[0]["prev"] is not None:
        posm1 = np[0]["prev"]["pos"]

    # pos1 名詞句の一語一語後の品詞
    if np[-1]["next"] is not None:
        pos1 = np[-1]["next"]["pos"]

    print "\t".join([article, wm1, fw, fpos, w0, fwfpos,
                    hw, hwhpos, pos1, hpos, posm1, w1])
