# CLASSES (ADVANCE)

class Car():
    """this is the class to create a general car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer = 0
    
    def description(self):
        print(f"Car info: make: {self.make}, model: {self.model}, year: {self.year}.")
    
    def get_odometer(self):
        print(f"your odometer shows: {self.__odometer}")

    def set_odometer(self, miles):
        if miles > self.__odometer:
            self.__odometer = miles
        else:
            print(f"You can not set the odometer to less that {self.__odometer}")


audi_a5 = Car('audi', 'A5', 2020)
audi_a5.description()
# print(f"odometer reading: {audi_a5.__odometer}")
# audi_a5.odometer = 5000 # we are assigning new value
print(f"odometer reading: {audi_a5.get_odometer()}")
audi_a5.set_odometer(5000)

# print(f"odometer reading after 5000miles: {audi_a5.__odometer}")
print(f"odometer reading after 5000miles: {audi_a5.get_odometer()}")
# audi_a5.odometer= 2000
audi_a5.set_odometer(2000)

# print(f"odometer reading after another 2000 : {audi_a5.__odometer}")
print(f"odometer reading after another 2000 : {audi_a5.get_odometer()}")
audi_a5.get_odometer()







