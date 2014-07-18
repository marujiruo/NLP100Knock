#!/usr/bin/python
#coding:utf-8
import sys
import pymongo
from pymongo import *

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets

for data in col.find({"$query":{"user":"170626372"}, "$orderby":{"freq_rted":1}}).limit(10):
    print data
