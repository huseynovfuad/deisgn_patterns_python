"""
The Template Design Pattern is a behavioral design pattern that defines the skeleton of an algorithm 
in the superclass but lets subclasses override specific steps of the algorithm without changing 
its structure. It's often used when you have a series of steps in an algorithm, and you want to allow 
subclasses to implement or customize some of those steps.
"""

from abc import ABC, abstractmethod

# Abstract class defining the template for making a beverage
class Beverage(ABC):

    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
    
    @abstractmethod
    def brew(self):
        pass
    
    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

# Concrete class for making Coffee
class Coffee(Beverage):

    def brew(self):
        print("Brewing coffee grounds")

    def add_condiments(self):
        print("Adding sugar and milk")

# Concrete class for making Tea
class Tea(Beverage):

    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

if __name__ == "__main__":
    print("Making Coffee:")
    coffee = Coffee()
    coffee.prepare()

    print("\nMaking Tea:")
    tea = Tea()
    tea.prepare()
