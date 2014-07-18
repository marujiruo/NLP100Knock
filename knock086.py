#!/usr/bin/python
#coding:utf-8
import sys
import pymongo
from pymongo import *

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets

for data in col.find({"url": "http://twitter.com/mirepiyo_berry/status/485830086889701376"}):
    print data
