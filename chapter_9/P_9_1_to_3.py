class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆基本信息"""
        print(f"{self.restaurant_name} is {self.cuisine_type} style")

    def open_restaurant(self):
        """表示正在营业"""
        print(f"{self.restaurant_name} is open")

    def all_print(self):
        self.describe_restaurant()
        self.open_restaurant()

old_people_chicken = Restaurant("Chicken", "north")
#创建实例
old_people_chicken.all_print()
#使用方法

anther_old_people_chicken = Restaurant("Chicken", "west")
anther_old_people_chicken.describe_restaurant()

anther_1_old_people_chicken = Restaurant("Chicken", "south")
anther_1_old_people_chicken.describe_restaurant()

anther_2_old_people_chicken = Restaurant("Chicken", "east")
anther_2_old_people_chicken.describe_restaurant()
print('\n')

class User:
    """user的类"""
    def __init__(self, first_name, last_name, age, email):
        """初始化user信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def greet_user(self):
        """向user打招呼"""
        print(f"hello! {self.first_name} {self.last_name}.")

    def describe_user(self):
        """描述user"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print('ur email is', self.email)

user_1 = User("Chicken", "Chicken", "17", "<EMAIL1>")
#创建实例
user_1.greet_user()
user_1.describe_user()
#使用方法