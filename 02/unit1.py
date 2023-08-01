#coding=utf-8
#利用列表的特性，打印99乘法表


for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print ("%s*%s=%s " % (j, i, i*j)),
    print ""
#看一下这个，如何写成一句话代码：
# 大神都用一句话代码写,这个属于是总结除了i和j的基本关系，就剩了不少事，不用if直接遍历的话可以用一句话操作：
print('\n'.join([' '.join(['%s*%s=%s' % (j, i, i*j) for j in range(1, i+1)])for i in range(1, 10)]))
