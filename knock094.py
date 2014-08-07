#!/usr/bin/python
#coding:utf-8
import xml.sax as sax
from xml.sax.handler import *
import argparse


class Node:
    def __init__(self, name, parent, attrs):
        self.name = name
        self.parent = parent
        self.attrs = attrs
        self.content = None
        self.children = list()


class MyHandler(ContentHandler):
    def __init__(self, root='root'):
        self.root = Node(root, None, dict())
        self.current_node = self.root

    def startElement(self, name, attrs):
        self.current_node = Node(name, self.current_node, attrs)
        self.current_node.parent.children.append(self.current_node)

    def endElement(self, name):
        self.current_node = self.current_node.parent

    def characters(self, content):
        self.current_node.content = content
        if self.current_node.name == "title":
            print content


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
    return mh.root


def print_children(parent):
    for child in parent.children:
        if child.children:
            print "<"+child.name+">"
            print_children(child)
        else:
            print "<%s> %s <%s>" % (child.name, child.content, child.name)


def print_content(tag, parent):
    for child in parent.children:
        if child.children:
            print_content(tag, child)
        elif child.name == tag:
            print child.content


def main():
    root = get_setupdata(args.xml_file)
    # print_content("title", root)
    # print_children(root)


if __name__ == '__main__':
    args = getArgs()
    main()
