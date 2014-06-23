#!/usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict


def getClassSimilarity(c1, c2):
    """
    クラス間の類似度を返す
    @parm   c1  クラス1(list)
    @parm   c2  クラス2(list)
    @return クラス間の類似度
    """
    # クラスの要素間での類似度計算(総当り)
    # その全ての類似度をリストに格納後、後でminimumを返す(最長距離法のため)
    # 内積辞書はdefaultで1.0なのでそもそも内積が存在しない場合は1.0になる
    # (最長距離法なので、1.0はどうせ無視される)
    # もし全ての要素の類似度が1.0なら(min=1.0, 全パターンやってもひとつも内積が存在しないなら)クラス間類似度は0にする
    similar_list = []
    for c1_item in c1:
        for c2_item in c2:
            similar_list.append(product_dict[c1_item+"\t"+c2_item])
    return min(similar_list) if min(similar_list) != 1 else 0


if __name__ == '__main__':
    input_file = sys.argv[1]
    stop_number = int(sys.argv[2])

    product_dict = defaultdict(lambda: 1.0)

    # クラスのリスト,各クラスもリストになってるので、リストinリスト
    class_list = []
    # クラスの初期化、内積辞書の初期化
    # line = 内積\t名詞句1\t名詞句2
    for line in open(input_file):
        product = float(line.strip().split("\t")[0])
        noun1 = line.strip().split("\t")[1]
        noun2 = line.strip().split("\t")[2]
        class_list.append(noun1)
        class_list.append(noun2)
        # どっちの連結でも参照できるようにしておく
        product_dict[noun1+"\t"+noun2] = product
        product_dict[noun2+"\t"+noun1] = product
    class_list = [[noun] for noun in set(class_list)]

    # 最長距離法クラスタリング
    while len(class_list) > stop_number:
        best_similarrity = .0
        neighbor_class = ()
        # クラスを総当りで類似度を計算して。一番高いものをマージする
        # 計算量を下げるためにネストされてるループは開始位置を変えてる
        # O(n*n) -> O(n*logn)
        for class1, i in zip(class_list, range(len(class_list))):
            for class2 in class_list[i+1:]:
                new_similarrity = getClassSimilarity(class1, class2)
                if best_similarrity < new_similarrity:
                    neighbor_class = (class1, class2)
                    best_similarrity = new_similarrity
        # 総当りしても一番いい類似度が0ってことは、もう内積辞書での組み合わせがない
        if best_similarrity == 0:
            print "can not merge anymore!"
            break
        class_list.append(neighbor_class[0]+neighbor_class[1])
        class_list.remove(neighbor_class[0])
        class_list.remove(neighbor_class[1])

    for one_class, i in zip(class_list, range(len(class_list))):
        print "class :", i+1, ",".join(one_class)
