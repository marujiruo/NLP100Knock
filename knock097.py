#!/usr/bin/python
#coding:utf-8
import xml.sax as sax
from xml.sax.handler import *
import argparse
import re

#英語版を見つける正規表現
re_link = re.compile("\{\{Commonscat\|(.*)\}\}")

class MyHandler(ContentHandler):
    def __init__(self):
        self.title_flag = False
        self.title = ""
        self.text_flag = False
        self.link = ""

    def startElement(self, name, attrs):
        if name == "title":
            self.title_flag = True
        if name == "text":
            self.text_flag = True

    def endElement(self, name):
        if name == "title":
            self.title_flag = False
        if name == "text":
            self.text_flag = False
            if self.link:
                print "Title: %s\tEnLink: http://en.wikipedia.org/wiki/%s" % (self.title, self.link)
                self.link = ""

    def characters(self, content):
        if self.title_flag:
            self.title = content
        if self.text_flag:
            r_result = re_link.search(content)
            if r_result:
                self.link = "_".join(r_result.group(1).split("|")[0].split(" "))


def getArgs():
    # パーサーの生成
    parser = argparse.ArgumentParser(description="xmlのパース")
    
    # オプション引数の追加
    parser.add_argument(
        "-f", "--file",
        dest="xml_file",
        required=True,
        help="XML形式の入力ファイル"
    )
    
    return parser.parse_args()


def get_setupdata(path):
    parser = sax.make_parser()
    parser.setFeature(sax.handler.feature_namespaces, 0)
    mh = MyHandler()
    parser.setContentHandler(mh)
    file = open(path, 'r')
    try:
        parser.parse(file)
    finally:
        file.close()


def main():
    get_setupdata(args.xml_file)


if __name__ == '__main__':
    args = getArgs()
    main()
