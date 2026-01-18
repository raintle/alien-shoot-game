name = ['A', 'B', 'C', 'D', 'E', 'F']
messages1 = "first three"
messages2 = "middle"
messages3 = "last"

print(f"\n{messages1}: {name[0 : 3]}")\
#打印前三个
print(f"\n{messages2}: {name[2 : 5]}")
#打印中间三个
print(f"\n{messages3}: {name[-3 : ]}")
#打印末尾三个

pizzas = ['pizzaA', 'pizzaB', 'pizzaC']
my_pizzas = pizzas[:]
#我的披萨的切片列表
friend_pizzas = pizzas[:]
#朋友的披萨的切片列表

my_pizzas.append("pizzaD")
#添加一项披萨
friend_pizzas.append("pizzaE")
for pizza in my_pizzas:
    print("my favorite pizza", pizza)
for pizza in friend_pizzas:
    print("friend favorite pizza", pizza)

'''两个for循环，略'''