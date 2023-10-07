"""
The Visitor design pattern is a behavioral design pattern that allows you to separate an algorithm 
from an object structure on which it operates. It enables you to add new operations 
to the object structure without modifying the classes of the objects. 
In Python, you can implement the Visitor pattern using classes and method overriding.
"""


# Define the Visitor interface
class ShoppingCartVisitor:
    def visit_book(self, book):
        pass

    def visit_electronics(self, electronics):
        pass

    def visit_clothes(self, clothes):
        pass

# Concrete Visitor implementation for calculating total cost with tax
class ShoppingCartTotalVisitor(ShoppingCartVisitor):
    def visit_book(self, book):
        return book.price + (book.price * 0.05)  # 5% tax

    def visit_electronics(self, electronics):
        return electronics.price + (electronics.price * 0.10)  # 10% tax

    def visit_clothes(self, clothes):
        return clothes.price + (clothes.price * 0.08)  # 8% tax

# Define the elements (items) in the object structure
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)

class Electronics:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit_electronics(self)

class Clothes:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def accept(self, visitor):
        return visitor.visit_clothes(self)

# Create a shopping cart
cart = [Book("Python Programming", 50.0), Electronics("Laptop", 800.0), Clothes("T-shirt", 20.0)]

# Calculate the total cost with tax using the Visitor pattern
total_cost_visitor = ShoppingCartTotalVisitor()
total_cost = sum(item.accept(total_cost_visitor) for item in cart)

print(f"Total cost with tax: ${total_cost:.2f}")
