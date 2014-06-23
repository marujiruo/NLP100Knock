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
    input_str1 = sys.argv[2]
    input_str2 = sys.argv[3]

    str1_vector = []
    str2_vector = []
    for line in open(input_file):
        split_line = line.strip().split("\t")
        if split_line[0] == input_str1:
            str1_vector = split_line[1:]
            if str2_vector:
                break
        if split_line[0] == input_str2:
            str2_vector = split_line[1:]
            if str1_vector:
                break

    if not str1_vector:
        print "can't find", input_str1
    if not str2_vector:
        print "can't find", input_str2
    if str1_vector and str2_vector:
        print input_str1+"・"+input_str2, "=",\
            getDotProduct(str1_vector, str2_vector)
