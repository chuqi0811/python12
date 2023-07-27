# coding=utf-8
# 用户输入数字。判断是不是闰年；如果是100的倍数，要能被400整除，其他的都是4整除；如果不是闰年，继续输入，直到闰年结束；

#
# while True:
#     year = raw_input("Enter a year:\n")
#     if int(year) % 100 == 0:
#         if int(year) % 400 == 0: # 这个是冗余代码，因为能被400整除一定能被100整除，写代码不思考
#             print "%s 年是闰年！" % year
#             break
#         else:
#             print "%s 年不是闰年！" % year
#     else:
#         if int(year) % 4 == 0:
#             print "%s 年是闰年！" % year
#             break
#         else:
#             print "%s 年不是闰年！" % year

# 尝试优化以及简化代码
string = "%s 是一个润年"
while True:
    x = int(raw_input("Enter a year:\n"))
    if x % 400 == 0:
        print string % x
        break
    elif x % 100 > 0 and x % 4 == 0:
        print string % x
        break
    else:
        print "not"
# 注意最优化自己的代码，减少没用的逻辑，精简代码
