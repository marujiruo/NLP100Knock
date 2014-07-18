#!/usr/bin/python
#coding:utf-8
import sys
import pymongo
from pymongo import *

query = unicode(sys.argv[1], "utf-8")

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets

for data in col.find():
    if query in data["body"]:
        print "%s :\n%s" % (data["nickname"], data["body"])
