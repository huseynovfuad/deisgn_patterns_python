"""
The Iterator design pattern is a behavioral design pattern that provides a way to access 
the elements of an aggregate object (e.g., a list, collection, or container) sequentially 
without exposing the underlying representation of the object. It defines a common interface 
for iterating over different types of collections.
"""


# Define the Iterator interface
class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        pass

    def next(self):
        pass

# Concrete Iterator implementation for a list
class ListIterator(Iterator):
    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Define the Iterable interface
class Iterable:
    def create_iterator(self):
        pass

# Concrete Iterable implementation for a list
class ListIterable(Iterable):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self):
        return ListIterator(self.items)

# Client code
if __name__ == "__main__":
    my_list = ListIterable()
    my_list.add_item("Item 1")
    my_list.add_item("Item 2")
    my_list.add_item("Item 3")

    iterator = my_list.create_iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)
