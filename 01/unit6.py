# coding=utf-8
# 计算一个列表中每个元素出现的次数
list = ['c','a','dfs','sde','a','a','c','dfs']
out_put = {}
times = 1
for i in list:
    if i in out_put.keys():
        out_put[i] = times + 1
    else:
        out_put[i] = times
print out_put
