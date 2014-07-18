#!/usr/bin/python
#coding:utf-8
import sys
import pymongo
from pymongo import *

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets

for data in col.find():
    pre_char = "<s>"
    bigrams = list()
    for char in data["body"]:
        bigrams.append(pre_char+char)
        pre_char = char
    bigrams.append(pre_char+"</s>")
    data["bigram"] = bigrams
    col.save(data)
col.create_index([("bigram", ASCENDING)])
