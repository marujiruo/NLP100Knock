#!/usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict


def getClassSimilarity(c1, c2):
    similar_list = []
    for c1_item in c1:
        for c2_item in c2:
            similar_list.append(product_dict[c1_item+"\t"+c2_item])
    return min(similar_list) if min(similar_list) != 1 else 0


if __name__ == '__main__':
    input_file = sys.argv[1]
    stop_number = int(sys.argv[2])

    product_dict = defaultdict(lambda: 1.0)
    class_list = []
    # クラスの初期化, 内積辞書の初期化
    for line in open(input_file):
        product = float(line.strip().split("\t")[0])
        noun1 = line.strip().split("\t")[1]
        noun2 = line.strip().split("\t")[2]
        class_list.append(noun1)
        class_list.append(noun2)
        product_dict[noun1+"\t"+noun2] = product
        product_dict[noun2+"\t"+noun1] = product
    class_list = [[noun] for noun in set(class_list)]

    # furthest neighbor method
    while len(class_list) > stop_number:
        best_similarrity = .0
        neighbor_class = ()
        # O(n*n) -> O(n*logn)
        for class1, i in zip(class_list, range(len(class_list))):
            for class2 in class_list[i+1:]:
                new_similarrity = getClassSimilarity(class1, class2)
                if best_similarrity < new_similarrity:
                    neighbor_class = (class1, class2)
                    best_similarrity = new_similarrity
        if best_similarrity == 0:
            print "can not merge anymore!"
            break
        class_list.append(neighbor_class[0]+neighbor_class[1])
        class_list.remove(neighbor_class[0])
        class_list.remove(neighbor_class[1])

    for one_class, i in zip(class_list, range(len(class_list))):
        print "class :", i+1, ",".join(one_class)
