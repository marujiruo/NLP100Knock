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
    tree = etree.parse(args.xml_file)

    # treeの子ノードを<sentence>タグのみで回す
    # id っていう属性があった場合、id=1の<sentence>の中のノードを<token>のみで回す
    # <token>のなかの<lemma>で回してテキストを出力
    for selement in tree.iter("sentence"):
        if "id" in selement.attrib:
            if selement.attrib["id"] == "1":
                for telement in selement.iter("token"):
                    for lemma in telement.iter("lemma"):
                        print lemma.text

if __name__ == '__main__':
    args = getArgs()
    main()


