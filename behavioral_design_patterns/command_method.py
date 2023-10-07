"""
The Command design pattern is a behavioral design pattern that encapsulates a request as an object, 
thereby allowing for parameterization of clients with queues, requests, and operations. 
It also allows you to support undoable operations. This pattern promotes loose coupling 
between the sender and receiver of a request.
"""


# Receiver classes
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


class Stereo:
    def turn_on(self):
        print("Stereo is ON")

    def turn_off(self):
        print("Stereo is OFF")


class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


# Command interface
class Command:
    def execute(self):
        pass


# Concrete Command classes
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()


class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()


# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def add_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()
        else:
            print("Invalid slot")


# Client code
if __name__ == "__main__":
    # Create instances of devices
    tv = TV()
    stereo = Stereo()
    light = Light()

    # Create commands
    tv_on = TurnOnCommand(tv)
    tv_off = TurnOffCommand(tv)
    stereo_on = TurnOnCommand(stereo)
    stereo_off = TurnOffCommand(stereo)
    light_on = TurnOnCommand(light)
    light_off = TurnOffCommand(light)

    # Create the remote control
    remote = RemoteControl()

    # Assign commands to slots on the remote
    remote.add_command(0, tv_on)
    remote.add_command(1, tv_off)
    remote.add_command(2, stereo_on)
    remote.add_command(3, stereo_off)
    remote.add_command(4, light_on)
    remote.add_command(5, light_off)

    # Press buttons on the remote to execute commands
    remote.press_button(0)  # Turns TV on
    remote.press_button(3)  # Turns Stereo off
    remote.press_button(5)  # Turns Light off
    remote.press_button(7)  # Invalid slot

