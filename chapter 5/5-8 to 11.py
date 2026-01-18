users = ['admin', 'alice', 'beer', 'duck', 'maxwell']
for user in users:
    if user == 'admin':
        print(f"welcome {user}")
    else:
        print(f"hello {user}")
print('\n')
#列表循环打印

users2 = []
if users2:
    for user in users2:
        if user == 'admin':
            print(f"welcome {user}")
        else:
            print(f"hello {user}")
else:
    print("we need some users!")
print('\n')
#判断条件后，对列表进行空列表判断

current_users = ['admin', 'alice', 'beer', 'duck', 'maxwell']
new_users = ['Admin', 'alice', 'mike', 'susan', 'lucy']
for user in new_users:
    user = user.lower()
    if user in current_users:
        print("is be used")
    else:
        print("is not be used")
print('\n')
#新列表对已有列表测定

numbers = range(1, 10)
for number in numbers:
    if number == 1:
        print(number, "st")
    elif number == 2:
        print(number, "nd")
    elif number == 3:
        print(number, "rd")
    else:
        print(number, "th")
#数字循环