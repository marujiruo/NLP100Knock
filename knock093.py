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
    # id っていう属性があった場合、id=1の<sentence>の中のノードを<token>のみで回す
    # その中にid属性があった場合 id=4のtokenのwordを取得する
    for selement in root.iter("sentence"):
        if "id" in selement.attrib:
            if selement.attrib["id"] == "1":
                for telement in selement.iter("token"):
                    if "id" in telement.attrib:
                        if telement.attrib["id"] == "4":
                            for element in telement:
                                if element.tag == "word":
                                    word = element.text

    # 1番目の文の係り受け関係をみる
    for selement in root.iter("sentence"):
        if "id" in selement.attrib:
            if selement.attrib["id"] == "1":
                for delement in selement.iter("dependencies"):
                    if "type" in delement.attrib:
                        if delement.attrib["type"] == "basic-dependencies":
                            for gdelement in delement.iter("governor"):
                                if gdelement.text == word:
                                    print [el.text for el in gdelement.getparent().iter("dependent")][0]


if __name__ == '__main__':
    args = getArgs()
    main()


