
run_sandwich = False
run_sell = False
run_survey = True
"""程序启用"""

sandwich_ordes = ['A_sandwich', 'B_sandwich', 'C_sandwich', 'D_sandwich', 'E_sandwich', 'F_sandwich', 'G_sandwich', 'G_sandwich', 'G_sandwich']
finished_sandwich = []
#列表创建
while run_sandwich:
    for sandwich in sandwich_ordes:
        if sandwich not in finished_sandwich:
            print(f"i will make {sandwich}")
        finished_sandwich.append(sandwich)
        #向列表中添加新元素
        if finished_sandwich == sandwich_ordes:
            #列表相等时停止程序
            run_sandwich = False
    print(f"finished sandwich: {', '.join(finished_sandwich)}")
    #join，列出元素，并以‘，’为分割号，去除方括号
print('\n')

while run_sell:
    for sandwich in sandwich_ordes:
        if sandwich == 'G_sandwich':
            sandwich_ordes.remove(sandwich)
            #检测并移除G_sandwich
        if 'G_sandwich' not in sandwich_ordes:
            print(f"sandwich ordes: ", ', '.join(sandwich_ordes))
            run_sell = False
            #不存在G_sandwich时停止程序
print('\n')

users = {}
#创建空字典
while run_survey:
    print("what's your name?,and where are you want to go? when u want to leave")
    user = input('name?')
    users[user] = input("where?")
    #向空字典中加入新的键值对
    check =True
    choice = ''
    #开始检测输入
    while check:
        print("continue? 1 leave 0 continue")
        choice = input()
        if choice in ['1', '0']:
            check = False
        else:
            print("please enter 1 or 0")
            continue
        #检测输入
    if choice == '1':
        run_survey = False

for user, place in users.items():
    print(f"{user} like place: {place}")
    #打印字典