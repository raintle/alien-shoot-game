people1 = {'first_name': 'qw', 'last_name': 'er', 'age': 25, 'city': 'shanghai'}
for value in people1.values():
    print(value)
print('\n')
#遍历打印，值

favorite_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for k, v in favorite_number.items():
    print(k, "favorite number is", v)
print('\n')
favorite_number['g'] = 7
#添加键值对
#遍历打印键值对

words = {
    'print': "打印",
    'for': "对列表循环",
    'if': "条件判断",
    'else': "不执行条件时输出该语法",
    'end': "结束",
}
for k, v in words.items():
    print(k, v)

"""
该练习在编写方程时用的是接下来一节的遍历方法
"""