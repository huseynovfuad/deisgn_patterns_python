"""
The Mediator design pattern is a behavioral design pattern that promotes loose coupling 
between objects by centralizing their communication through a mediator object. 
This pattern is useful when a set of objects need to interact with each other, 
but you want to avoid direct dependencies between them. Instead, they communicate through the mediator, 
which helps manage and coordinate their interactions.
"""


from abc import ABC, abstractmethod

# Mediator interface
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, user, message):
        pass

# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive_message(message)

# Colleague interface
class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass

# Concrete Colleague
class ChatUser(User):
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = ChatUser("Alice", chat_room)
    user2 = ChatUser("Bob", chat_room)
    user3 = ChatUser("Charlie", chat_room)

    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    user1.send("Hello, everyone!")
    user2.send("Hi, Alice!")
    user3.send("Hey, Bob!")

# Output:
# Alice sends: Hello, everyone!
# Bob receives: Hello, everyone!
# Charlie receives: Hello, everyone!
# Bob sends: Hi, Alice!
# Alice receives: Hi, Alice!
# Charlie receives: Hi, Alice!
# Charlie sends: Hey, Bob!
# Alice receives: Hey, Bob!
# Bob receives: Hey, Bob!
