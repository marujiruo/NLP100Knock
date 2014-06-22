# !usr/bin/python
# coding:utf-8
import sys
from collections import defaultdict

d=defaultdict(int)
for line in iter(sys.stdin.readline, ""):
    d[line.strip()]+=1

for key, value in sorted(d.items(), key=lambda x:-x[1]):
	print key, value
