alien_color1 = 'red'
alien_color2 = 'yellow'
alien_color3 = 'green'
#外星人颜色

if alien_color1 == 'red':
    print("you get 15 points")
if alien_color2 == 'yellow':
    print("you get 10 points")
if alien_color3 == 'green':
    print("you get 5 points")
if alien_color1 == 'yellow':
    print("you get 10 points")
#颜色判断
print('\n')

if alien_color1 == 'red':
    print("you get 15 points")
else:
    print("you get 10 points")
if alien_color1 == 'yellow':
    print("you get 10 points")
else:
    print("you get 15 points")
#esle进行判断
print('\n')

alien_colors = [alien_color1, alien_color2, alien_color3]
for alien_color in alien_colors:
    if alien_color == 'green':
        print("u kill a green alien")
        print("you get 5 points")
    elif alien_color == 'yellow':
        print("u kill a yellow alien")
        print("you get 10 points")
    elif alien_color == 'red':
        print("u kill a red alien")
        print("you get 15 points")
#使用列表进行for循环判定
    print('\n')

ages = [1, 49, 23, 80, 14, 3]
for age in ages:
    print('u age is', age)
    if age < 2:
        print("he is a baby")
    elif (age < 4) and (age >= 2):
        print("he is a kid")
    elif (age >= 4) and (age < 13):
        print("he is a kid2")
    elif (age >= 13) and (age < 20):
        print("he is a teenager")
    elif (age >= 20) and (age < 65):
        print("he is a man")
    elif age >= 65:
        print("he is a old")
    print('\n')
#判断大小，使用for循环列表

favorite_fruits = ['apple', 'banana', 'orange']
for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print("fruit is", fruit,"u really like it")
print('\n')
#同颜色差不多,进行列表判断