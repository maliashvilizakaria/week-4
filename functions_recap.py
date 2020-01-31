# Functions recap

# ALL MY FUNCTIONS HERE


def add(a, b):
    return a+b


def add2(a, b=0):
    """ a and b is an int, b has defaul value 0"""
    return a+b


def car_description(model, year, features):
    """ model:str, year:int, features: list, This functions describes the car based on inputs."""
    print(f"The car's model is {model.upper()}.")
    print(f"It was manufactured in {year}.")
    print(f"it has following features: ")
    for feature in features:
        print(f"\t{feature.title()}.")


def cars_desc(car):
    print(add(5, 6))
    for field, values in car.items():
        for value in values:
            print(f"Your car's {field} is {value}.")


# DATA
car_tesla = {'model': ['Model X', 'Model Y'],
             'year': [2020, 2019],
             'owner': ['Zakaria', 'Oleh']}


# ALL MY EXECUTIONS ARE HERE

cars_desc(car_tesla)
result1 = add(23, 45)
result2 = add(11, 22)
# result3 = add(12)
result3 = add2(12, 65)
result4 = add2(12)
print(result1, result2, result3, result4)
print(add(46789, 12347))

car_description("Model Y", 2019, [
                'cool design', 'fancy doors', 'techy tires', 'ugly window'])
