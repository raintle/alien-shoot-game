n = ['s', 'q', 'r', 't', 'u']
print(n)
print(sorted(n))
print(n)
n.reverse()
print(n)
n.reverse()
print(n)
n.sort()
print(n)
n.sort(reverse=True)

name = ['A', 'B', 'C', 'D', 'E', 'F']
print(len(name))
#输出长度

pp = ['2', '4', '2', '3', '5', '6', '7']
print(sorted(pp))
#临时整理
print(sorted(pp, reverse=True))#reverse 反转
pp.sort()
#永久整理
print(pp)
print(len(pp))

print(pp[6])
print(pp[-1])
#倒数第一个输出
print(pp[-2])
#倒数第二个输出