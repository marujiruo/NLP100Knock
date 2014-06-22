# !usr/bin/python
# coding:utf-8
import sys
import matplotlib.pyplot as plt
 
#横軸の最大値
max = 100
# データを読み込み
y=[]
count = 0
for line in iter(sys.stdin.readline, ""):
	num = int(line.strip().split()[1])
	y.append(num)
	count+=1
	if count==max:
		break
x=range(count) 
width = .5

plt.bar(x, y)

# 表示
plt.show()
