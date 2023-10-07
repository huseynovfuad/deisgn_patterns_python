"""
The State design pattern is a behavioral design pattern that allows an object to alter its behavior 
when its internal state changes. The pattern achieves this by representing different states 
as separate classes and delegating the state-specific behavior to these classes. 
This can make the code more maintainable and flexible when dealing with complex objects 
that exhibit different behaviors based on their internal state.
"""


# Define the VendingMachineContext class, which maintains the current state.
class VendingMachineContext:
    def __init__(self):
        self.state = NoCoinState()

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def select_item(self):
        self.state.select_item()

    def change_state(self, state):
        self.state = state


# Define the base State class.
class State:
    def insert_coin(self):
        pass

    def eject_coin(self):
        pass

    def select_item(self):
        pass


# Define concrete state classes.
class NoCoinState(State):
    def insert_coin(self):
        print("Coin inserted. You can now select an item.")
        return HasCoinState()


class HasCoinState(State):
    def eject_coin(self):
        print("Coin ejected.")
        return NoCoinState()

    def select_item(self):
        print("Item selected. Dispensing the item.")
        return SoldState()


class SoldState(State):
    def select_item(self):
        print("Please wait, dispensing your item.")
        return NoCoinState()


# Usage example
if __name__ == "__main__":
    vending_machine = VendingMachineContext()

    vending_machine.insert_coin()
    vending_machine.select_item()

    vending_machine.insert_coin()
    vending_machine.eject_coin()

    vending_machine.insert_coin()
    vending_machine.select_item()
