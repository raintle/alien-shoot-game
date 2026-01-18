

def sandwich_toppings(*toppings):
    """任意数量形参"""
    print('about u order toppings:')
    for topping in toppings:
        print('-', topping)
sandwich_toppings('asd', 'sad', 'dwas')

def user_profile(first_name, last_name, **kwargs):
    """形参加上任意数量形参"""
    a_user = {'first_name': first_name, 'last_name': last_name, **kwargs}
    print(f'\nmu name is {first_name} {last_name}')
    print('all of u message:', a_user)
user_profile(first_name='John', last_name='Smith', aaa='asd', san='dwd')

def make_car(manufacturer, model, **args):
    """形参加上任意数量关键字形参"""
    car_message = {'manufacturer': manufacturer, 'model': model, **args}
    return car_message
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print('\n', car)