# CLASSES (ADVANCE)

class Car():
    """this is the class to create a general gas car"""

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

class ElectricCar(Car):
    """ Model to represent the electric cars"""
     
    def __init__(self, make, model, year, battery_size=100):
         super().__init__(make, model, year)
         self.battery_size = battery_size

    # METHOD/FUNCTION OVERRIDING
    def description(self):
        msg = f"Car info: make: {self.make} "
        msg = msg + f"model: {self.model} "
        msg += f"year: {self.year} "
        msg += f"battery capacity {self.battery_size}-kWh."
        print(msg)


# instanciating classes
print('=============  ELECTRIC CAR  =====================')

my_tesla = ElectricCar('Tesla', 'Model S', 2020, 150)
my_tesla.get_odometer()
print(my_tesla.model)
my_tesla.description()


print('===============  GAS CAR ===================')
audi_a5 = Car('audi', 'A5', 2020)
audi_a5.description()
# print(f"odometer reading: {audi_a5.__odometer}")
# audi_a5.odometer = 5000 # we are assigning new value
print(f"odometer reading: {audi_a5.get_odometer()}")
audi_a5.set_odometer(5000)

print('================ GAS CAR ==================')
# print(f"odometer reading after 5000miles: {audi_a5.__odometer}")
print(f"odometer reading after 5000miles: {audi_a5.get_odometer()}")
# audi_a5.odometer= 2000
audi_a5.set_odometer(2000)

# print(f"odometer reading after another 2000 : {audi_a5.__odometer}")
print(f"odometer reading after another 2000 : {audi_a5.get_odometer()}")
audi_a5.get_odometer()







