# !usr/bin/python
# coding:utf-8
import sys
import CaboCha

cabo_parser = CaboCha.Parser()
for line in open(sys.argv[1]):
	print cabo_parser.parse(line.strip()).toString(CaboCha.FORMAT_LATTICE),
