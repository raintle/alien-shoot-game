foods = ('A', 'B', 'C', 'D', 'E',)
#创建元组
for food in foods:
    print(food)

'''
foods[0] = 'F'
错误代码，不能修改元组元素
'''

print("\n")

foods = ('A', 'G', 'F', 'D', 'E',)
#对元组重新赋值
for food in foods:
    print(food)