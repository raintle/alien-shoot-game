def make_shirts(size, word= "i love python"):
    """后形参为默认值的使用"""
    print(f"this shirt will be mede with {size} and will print {word}")
make_shirts(size="3", word="shirt")
#关键字实参
make_shirts('3', 'good')
#位置实参
make_shirts('23')
make_shirts('23')
#使用默认值
make_shirts('12', 'aaa')

def describe_city(city='Reykjavik', country='Iceland'):
    """双形参为默认值的练习"""
    print(f"{city} is in {country}")
describe_city()
#使用默认值
describe_city(city='aaa')
#country形参使用默认值
describe_city(city='beijing', country='CN')