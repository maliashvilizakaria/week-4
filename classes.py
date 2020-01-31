# OBEJCT ORIENTED PROGRAMMING CONCEPTS (OOPs)

# Class - blueprint
# Object - is the instnace of the class

# creating a class - names with capital letter


class Dog():
    # state
    # constructor - default functions to be execute when you create an object
    def __init__(self, breed, color, name):
        self.breed = breed
        self.color = color
        self.name = name

    def describeDog(self):
        return f"your dog is {self.breed}."

    def run(self):
        return f"Your dog {self.name} is running ..."

    def bark(self):
        return f"{self.name} is barking - Wouf wouf wouf wouf!!!!"


# instantiating the class - creating object of the class
rex = Dog('german shepherd', 'brown', 'Rex')
sharik = Dog('husky', 'black', 'Sharik')


# access the class state and behavior
print(f"the breed of the rex is {rex.breed}")
print(f"the color of the rex is {rex.color}")
print(rex.describeDog())
print(rex.run())
print(rex.bark())
print("======================================")

print(f"the breed of the rex is {sharik.breed}")
print(f"the color of the rex is {sharik.color}")
print(sharik.describeDog())
print(sharik.run())
print(sharik.bark())
