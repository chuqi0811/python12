# coding=utf-8
# 求一个列表中的最大值

list = [111111111111,22222222222222222,123,432,12,34,56,78,89807,324523,123124,45346,55856]
a = list[0]
for i in list:
    if i > a:
        a = i
print a
