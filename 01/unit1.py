# coding=utf-8
# 让用户一直输入数字，如果输入的是0，终止程序；否则的话一直打印所有数字之和
# 注意格式转换

num = 0
while True:
    x = raw_input("Enter a number:\n")
    # if x == 0，这样会一直不等于的
    if int(x) == 0:
        break
    else:
        num = num + int(x)
        print num
print num
