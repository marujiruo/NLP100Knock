#!/usr/bin/python
#coding:utf-8
import sys
import pymongo
from pymongo import *

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets

# for data in col.find():
#     for bigram in data["bigram"]:
#         if bigram == u"神田":
#             print "%s :\n%s" % (data["nickname"], data["body"])
for data in col.find({"bigram": u"神田"}):
    print "%s :\n%s" % (data["nickname"], data["body"])
