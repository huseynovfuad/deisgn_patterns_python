"""
The Factory Design Pattern is a creational design pattern that provides an interface 
for creating objects but allows subclasses to alter the type of objects that will be 
created. In Python, you can implement the Factory Design Pattern using classes and methods
"""

# Define the Pizza base class
class Pizza:
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass

# Concrete pizza classes
class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")

    def bake(self):
        print("Baking Margherita Pizza")

    def cut(self):
        print("Cutting Margherita Pizza")

    def box(self):
        print("Boxing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

    def cut(self):
        print("Cutting Pepperoni Pizza")

    def box(self):
        print("Boxing Pepperoni Pizza")

# PizzaFactory to create different types of pizzas
class PizzaFactory:
    pizzas = {
        "Margherita": MargheritaPizza,
        "Pepperoni": PepperoniPizza,
    }


    def create_pizza(self, pizza_type):
        if not pizza_type in self.pizzas:
            raise ValueError("Invalid pizza type")
        
        return self.pizzas[pizza_type]()


# Client code
pizza_factory = PizzaFactory()

pizza1 = pizza_factory.create_pizza("Margherita")
pizza1.prepare()
pizza1.bake()
pizza1.cut()
pizza1.box()

pizza2 = pizza_factory.create_pizza("Pepperoni")
pizza2.prepare()
pizza2.bake()
pizza2.cut()
pizza2.box()
