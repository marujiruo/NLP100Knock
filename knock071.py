# !usr/bin/pyton
# coding:utf-8
import sys
import re
import os
from geniatagger import *


#ディレクトリ内のファイルリストを返す
def get_files(dirpath):
    flist = []
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(os.path.join(path)):
                flist.append(path)
    return flist

if __name__ == '__main__':
    re_sentence = re.compile(r"\. [A-Z]|\.\[[0-9]+\] [A-Z]")
    tagger = GeniaTagger('/Users/ryosuke/Downloads/geniatagger-3.0.1/geniatagger')
    corpus_dir = sys.argv[1]
    target_dir = sys.argv[2]

    files = get_files(corpus_dir)
    for file_name in files:
        print file_name
        f = open(target_dir + file_name.split("/")[-1] + ".genia", "w")
        for line in open(file_name):
            if line == "\n":
                continue
            temp = line
            result_search = re_sentence.search(temp)
            while(result_search is not None):
                for taggered in tagger.parse(temp[0:result_search.start()+1]):
                    f.write("\t".join(taggered)+"\n")
                f.write("\n")
                temp = temp[result_search.start()+len(result_search.group()[:-1]):]
                result_search = re_sentence.search(temp)
            for taggered in tagger.parse(temp.strip()):
                f.write("\t".join(taggered)+"\n")
            f.write("\n")
        f.close()
