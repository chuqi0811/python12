# coding=utf-8
# 计算一个数字组成列表的最大的两个值
list = [1,2,3,34,454,6547,234,567,654,345,234,678,897,12,34,23,54,35,64,57]
num = 0
num_1 = 0
for i in list:
    if i > num:
        num = i
for j in list:
    if num_1 < j < num:
        num_1 = j
print "列表最大的两个值为 %s %s" % (num ,num_1)
# 这个需要遍历两次列表，不知道是否有更加便捷的方式，后续探索
