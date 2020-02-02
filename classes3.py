# from cars.cars import Car, ElectricCar, Battery
from cars_package.cars_module import *
import random
import time
import datetime

print(datetime.date.today())
print(f"Random number generated: {random.randint(1, 30)}.")
time.sleep(20)
# instanciating classes
print('=============  ELECTRIC CAR  =====================')

my_tesla = ElectricCar('Tesla', 'Model S', 2020, 150)
my_tesla.get_odometer()
print(my_tesla.model)
my_tesla.description()
my_tesla.battery.get_range()
my_tesla.battery.get_battery_size()


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
