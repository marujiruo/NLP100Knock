# !usr/bin/python
# coding:utf-8
import sys
import matplotlib.pyplot as plt
 
# データを読み込み
data=[]
max = 0
for line in iter(sys.stdin.readline, ""):
	num = int(line.strip().split()[1])
	max =  num if max < num else max
	data.append(num)
 
# 横軸の最大値
max = 50
 
# binsはビンの数,
plt.hist(data, bins = max, range = (0, max))

plt.savefig(r"Data/result049.png")
 
# 表示
plt.show()
