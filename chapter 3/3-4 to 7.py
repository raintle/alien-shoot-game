name = ['A', 'B', 'C', 'D', 'E', 'F']
messages = "我将邀请的人有"
print(f"\n{messages}: {name[0]} {name[1]} {name[2]} {name[3]} {name[4]} {name[5]}")

print(f"\n{name[5]}无法赴约")
name[5] = "G"
print(f"\n{messages}: {name[0]} {name[1]} {name[2]} {name[3]} {name[4]} {name[5]}")

print("\n我找到了大地方")
name.insert(0, "A1")
name.insert(3, "C2")
name.append("G3")
#添加G3到末尾
print("\n")
print(name)
for a in name:
    print(f"欢迎参加，{a}")

print("aba,aba")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")
popped_name = name.pop()
messages = "sorry"
print(f"\n{messages}: {popped_name}")

messages = "nihaizai"
print(f"\n{messages}: {name[0]},{name[1]}")
del name[0]
del name[0]
print(name)