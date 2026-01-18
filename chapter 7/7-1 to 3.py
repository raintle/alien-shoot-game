print('what do u want to buy what car?')
car = input()
print('wait, let me find', car)
print('\n')
#input函数练习

print("how many people are there?")
people = int(input())
if people > 8:
    print('sorry,there are only 8 people')
else:
    print('welcome')
print('\n')
#添加判断条件

print('please input a number')
number = int(input())
if number % 10 == 0:
    print('this is a 10 number')
else:
    print('this is not a 10 number')
#判断余数是否为零，%求模的使用