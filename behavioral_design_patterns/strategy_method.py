"""
The Strategy design pattern is a behavioral design pattern that defines a family of algorithms, 
encapsulates each one, and makes them interchangeable. It allows the client to choose an algorithm 
from a family of algorithms at runtime, without altering the code that uses the algorithm. 
This pattern is useful when you want to decouple the client code from 
the specific implementation of an algorithm.
"""


# Define the Item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Define the PaymentStrategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete PaymentStrategy implementations
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        print(f"Paid ${amount} with Credit Card: {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount} with PayPal: {self.email}")

# Context class that uses the PaymentStrategy
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.cart)

    def checkout(self, payment_strategy):
        total_amount = self.calculate_total()
        payment_strategy.pay(total_amount)

# Client code
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(Item("Item 1", 10.0))
    cart.add_item(Item("Item 2", 20.0))
    cart.add_item(Item("Item 3", 30.0))

    # Choose a payment strategy at runtime
    payment_strategy = CreditCardPayment("1234-5678-9012-3456", "John Doe")
    # payment_strategy = PayPalPayment("john@example.com")

    cart.checkout(payment_strategy)
