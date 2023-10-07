"""
The Decorator design pattern is a structural design pattern that allows you to dynamically 
add behavior or responsibilities to objects without altering their code. 
It's commonly used in Python to extend the functionality of classes or objects by wrapping them 
with one or more decorator classes.
"""


# Component interface
class Coffee:
    def cost(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost of a simple coffee

# Decorator abstract class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Add the cost of milk

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Add the cost of sugar

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Add the cost of vanilla flavor

if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"Cost of simple coffee: ${coffee.cost()}")

    milk_coffee = MilkDecorator(coffee)
    print(f"Cost of coffee with milk: ${milk_coffee.cost()}")

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(f"Cost of coffee with sugar and milk: ${sugar_milk_coffee.cost()}")

    vanilla_sugar_milk_coffee = VanillaDecorator(sugar_milk_coffee)
    print(f"Cost of coffee with vanilla, sugar, and milk: ${vanilla_sugar_milk_coffee.cost()}")
