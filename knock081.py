#!/usr/bin/python
#coding:utf-8
import sys
import json
from pymongo import Connection

# jsonの取得
json_file = sys.argv[1]
tweet_data = json.load(open(json_file))

# コネクション作成
con = Connection('fomalhaut', 27017)
db = con.nlp100_miyazaki
col = db.tweets


for one_tw in tweet_data:
    tw = {}
    tw["url"] = "http://twitter.com/%s/status/%s" % (one_tw["user"]["screen_name"], one_tw["id_str"])
    tw["date"] = one_tw["created_at"]
    tw["user"] = one_tw["user"]["id_str"]
    tw["nickname"] = one_tw["user"]["name"]
    tw["body"] = one_tw["text"]
    tw["rt_url"] = None
    if "retweeted_status" in one_tw:
        tw["rt_url"] = "http://twitter.com/"+one_tw["retweeted_status"]["user"]["screen_name"]+"/status/"+one_tw["retweeted_status"]["id_str"]
    tw["reply_url"] = None
    if one_tw["in_reply_to_screen_name"] is not None:
        tw["reply_url"] = "http://twitter.com/"+one_tw["in_reply_to_screen_name"]+"/status/"+one_tw["in_reply_to_status_id_str"]
    tw["freq_rted"] = one_tw["retweet_count"]
    # tw["qt_url"]
    # tw["freq_replied"]
    # tw["freq_qted"]
    col.insert(tw)

