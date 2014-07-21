#!/usr/bin/python
#coding:utf-8
from lxml import etree
import argparse


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


def main():
    root = etree.parse(args.xml_file)

    # rootの子ノードを<sentence>タグのみで回す
    # id っていう属性があった場合、id=2の<sentence>の中のノードを<token>のみで回す
    # その中にid属性があった場合 id=5のtokenのwordを表示する
    for selement in root.iter("sentence"):
        if "id" in selement.attrib:
            if selement.attrib["id"] == "2":
                for telement in selement.iter("token"):
                    if "id" in telement.attrib:
                        if telement.attrib["id"] == "5":
                            for word in telement.iter("word"):
                                print word.text

if __name__ == '__main__':
    args = getArgs()
    main()


