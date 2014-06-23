#!/usr/bin/python
# coding:utf-8
import sys


def getDotProduct(v1, v2):
    dotpro = 0
    for v1_item in v1:
        v1_split = v1_item.split(":")
        v1_split = [":".join(v1_split[:-1]), float(v1_split[-1])]
        for v2_item in v2:
            v2_split = v2_item.split(":")
            v2_split = [":".join(v2_split[:-1]), float(v2_split[-1])]
            if v1_split[0] == v2_split[0]:
                dotpro += v1_split[1]*v2_split[1]
    return dotpro


if __name__ == '__main__':
    input_file = sys.argv[1]
    file_linenum = sum(1 for line in open(input_file))

    product_dict = {}
    for line1, index1 in zip(open(input_file), range(file_linenum)):
        split_line1 = line1.strip().split("\t")
        for line2, index2 in zip(open(input_file), range(file_linenum)):
            if index2 <= index1:
                continue
            split_line2 = line2.strip().split("\t")
            product_dict[split_line1[0]+"\t"+split_line2[0]] = getDotProduct(split_line1[1:], split_line2[1:])

    # output
    for text, product in sorted(product_dict.items(), key=lambda x:-x[1]):
        if product < 0.6:
            break
        print str(product)+"\t"+text
