counts1 = []
#创建空列表
for count in range(1, 21):
    #赋值循环
    counts1.append(count)
    #加入到空列表counts1
print(counts1)


counts2 = list(range(1, 1_000_001))
#list() 列表转换，创建一百万数列表
'''
for count in counts2:
    print(count)

#可用，但不使用
'''

print(min(counts2))
#最小值
print(max(counts2))
#最大值
print(sum(counts2))
#总和

"""
counts3 = list(range(1, 21, 2))
#偶数列表
for count in counts3:
    print(count)

counts4 = list(range(3, 31, 3))
#3倍数列表
for count in counts4:
    print(count)
"""

counts4 = list(a**3 for a in range(1, 11))
#立方解析列表
for count in counts4:
    print(count)

counts5 = []
for count in range(1, 11):
    count = count ** 3
    counts5.append(count)
print(counts5)
"""
创建一个包含1-10立方数的列表
和上相同
"""