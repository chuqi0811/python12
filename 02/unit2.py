# 主要就是数组的稳固
# 冒泡排序熟悉与练习,熟悉数据结构，然后慢慢接触算法，这个是必经之路。
arr = range(10,0,-1)
count = 0
for j in range(len(arr)-1):
    for i in range(len(arr)-1-j):
        count += 1
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print arr
print arr
print count
  
