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


class Battery():
    def __init__(self,  battery_size):
        self.__battery_size = battery_size

    def get_range(self):
        if self.__battery_size > 100:
            msg = f"This car has range of 320 miles with full charge."
        elif self.__battery_size < 80:
            msg = f"This car has range of 250 miles with full charge."
        else:
            msg = f"This car has range of around 290 miles with full charge"
        print(msg)
    
    def get_battery_size(self):
        return self.__battery_size


class ElectricCar(Car):
    """ Model to represent the electric cars"""
     
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)
        #  self.battery_size = battery_size

    # METHOD/FUNCTION OVERRIDING
    def description(self):
        msg = f"Car info: make: {self.make} "
        msg = msg + f"model: {self.model} "
        msg += f"year: {self.year} "
        msg += f"battery capacity {self.battery.get_battery_size()}-kWh."
        print(msg)
