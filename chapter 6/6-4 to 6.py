"""
略过，在6-3已有解答
"""

river = {
    "china": "huang he",
    "via": "mei gong he",
    "egypt": "nile"
}

for k, v in river.items():
    print(f"{v} in {k}")
print("\n")
for value in river.values():
    print(value)
for key in river.keys():
    print(key)
print("\n")
#遍历字典键值对并打印

numbers1 = {
    "1st": "1",
    "2nd": "2",
    "3rd": "3",
    "4th": "4",
    "5th": "5"
}
numbers2 = {
    "1st": "1",
    "2nd": "2",
    "34th": "34",
    "37th": "37",
    "49th": "49"
}
for key in numbers1.keys():
    if key in numbers2.keys():
        continue
    else:
        print(f"{key} not in numbers2")
#遍历并对比两字典键的不同、