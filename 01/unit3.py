# coding=utf-8
# 存10000元，年利率是3.25%，求多少年后存款可以翻倍


money = 10000
rate = 0.0325
year = 0
while money <= 20000:
    money = money + money*rate
    year += 1
    print "第 %s 年，你的存款是 %s" % (year, money)
print "存款在 %s 年后翻倍了，是 %s" % (year, money)
