# coding=utf-8
# 让用户一直输入数字，如果没输入任何值，终止程序，打印所有输入数字的平均值

num = 0
i = 1
while True:
    x = raw_input("Enter a num:\n")
    if x:
        num = num + int(x)
        avg = float(num)/i
        print "you have %s num(s),the avg is %s!" % (i, avg)
        i = i + 1
    else:
        break

#print avg
# 原本我想添加后面的这句，发现正常执行也没有问题，但是pycharm会有提示，发现了，如果上来就是0那么这个变量就是未定义的，所以一定要逻辑通顺
# 程序当时没出问题不代表没问题！
