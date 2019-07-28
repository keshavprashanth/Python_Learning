import random
import sys
import os


class Animal:
    __name = None   # None Signifies lack of a value
    __height = 0    # two underscores signify that the variable is private, we need getters and setter to access them
    __weight = 0
    __sound = 0

# Constructors - are used to initialize an object
# In this case we are demanding name, height, weight and sound to be passed when the Animal class is called
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

# Defining getters and setters to access private variables from a class.
    def set_name(self, name):  # Self allows an object to refer to itself inside of a class
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}.".format(self.get_name(),
                                                                       self.get_height(),
                                                                       self.get_weight(),
                                                                       self.get_sound())
# Creating an object cat using Animal class and using the method / function from Animal class.
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.get_type())
print(cat.toString())

# Inheritance - When we inheritance from another class, we automatically get all the variables, functions,
# Methods etc from the class we are inheriting from


class Dog(Animal):   # We created Dog class and inherited from Animal class.
    __owner = ""     # Every dog will have additional variable owner. This is not in Animal class.

# Constructor for Dog Class
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
# we want the Animal superclass to handle variables that are coming from Animal super class into Dog class
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):   # Method overriding
        print("Dog")

    def toString(self):   # Method overriding
        return "{} is {} cm tall and {} kilograms and says {} and his owner is {}".format(self.get_name(),
                                                                                          self.get_height(),
                                                                                          self.get_weight(),
                                                                                          self.get_sound(),
                                                                                          self.get_owner())

# Method Overloading - we will be able to perform different tasks based on attributes that are sent in
    def multiple_sounds(self, howMany = None):
        if howMany is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * howMany)

spot = Dog('Spot', 53, 25, 'Ruff', 'Derek')
print(spot.toString())

spot.multiple_sounds(4)
spot.multiple_sounds()

# Polymorphism -
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

