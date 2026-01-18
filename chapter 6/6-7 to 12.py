people1 = {'first_name': 'qw', 'last_name': 'er', 'age': 25, 'city': 'shanghai'}
people2 = {'first_name': 'sd', 'last_name': 'fg', 'age': 23, 'city': 'sahnggao'}
people3 = {'first_name': 'zx', 'last_name': 'xc', 'age': 13, 'city': 'hanghai'}
people = [people1, people2, people3]
for person in people:
    print(f"{person['first_name']} {person['last_name']} , he age is {person['age']}, and city is {person['city']}")
print('\n')
#创建三个字典并加入到列表中

pet1 = {'name': 'xiaohua', 'specie': 'dog', 'master': 'qw er'}
pet2 = {'name': 'xiaohuang', 'specie': 'cat', 'master': 'qw ui'}
pet3 = {'name': 'xiaoli', 'specie': 'dog', 'master': 'sd fg'}
pet4 = {'name': 'xiaoxin', 'specie': 'mouse', 'master': 'zx xc'}
pets = [pet1, pet2, pet3, pet4]
for pet in pets:
    print(f"this pet name is {pet['name']}")
    print(f"this pet species is {pet['specie']}")
    print(f"this pet master is {pet['master']}")
    print("\n")
#同上

favorite_place ={
    "lihua": ['jiangxi', 'nanchang', 'shanghai'],
    "liuzi": ['beijing'],
    "zhangsan": ['nanjing', 'shangrao']
}
for person, places in favorite_place.items():
    for place in places:
        print(f"{person} love {place}")
    print("\n")
#在字典中创建列表，并打印

favorite_number = {'a': [2, 5], 'b': [32, 43], 'c': [123, 234, 4], 'd': [21, 11], 'e': [12,3], 'f': [1]}
for k, v in favorite_number.items():
    for v2 in v:
        print(f"{k} favorite number is", v2)
    print("\n")
#同上

cities = {
    "california": {"country": 'USA', 'population': 20000, 'fact': 'dead man'},
    "shanghai": {"country": 'CN', 'population': 200000, 'fact': 'have money'},
    'london': {'country': 'UK', 'population': 10000, 'fact': 'have a famous building'}
}
for city, message in cities.items():
    print('about', city)
    print("it's country is", message['country'])
    print("it's population is", message['population'])
    print("it's fact is", message['fact'])
    print("\n")
#在字典中嵌套字典