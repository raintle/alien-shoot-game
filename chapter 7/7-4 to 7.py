
pizza_program = False
movie_ticket_program = True
aaa = False
"""控制程序启用"""

pizza_toppings = []
while pizza_program:

    print('please choose a pizza topping')
    pizza_topping = input()
    pizza_toppings.append(pizza_topping)
    #将用户的输入添加到列表
    if pizza_topping == 'q':
        pizza_program = False
        continue
        #当输入为q时，终止程序
    print(f'we will add {pizza_topping} pizza topping')
    print('\n')

while movie_ticket_program:
    print('please enter u age')
    age = input()
    if age == 'q':
        break
    try:
        age = int(age)
    except ValueError:
        print('please enter a number')
        print('\n')
        continue
    #将用户输入变为int类型
    if age < 3:
        print("it's free for u")
    elif (age >= 3) and (age < 12):
        print("u should pay 10 $")
    elif (age >= 12) and (age < 120):
        print("u should pay 15 $")
    else:
        print("enter a other age")
    #判断用户输入age，并做相应输出

"""
7-6已完成
"""
a = 0

while aaa:
    a += 0
    print(a)
    """这是个没完没了的循环！！！"""