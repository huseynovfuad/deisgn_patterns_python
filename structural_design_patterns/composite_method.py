"""
The Composite design pattern is a structural design pattern that allows you to compose objects 
into tree structures to represent part-whole hierarchies. It lets clients treat individual objects 
and compositions of objects uniformly.
"""


from abc import ABC, abstractmethod

# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf class
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite class
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

# Client code
if __name__ == "__main__":
    root = Directory("Root")
    folder1 = Directory("Folder 1")
    folder2 = Directory("Folder 2")
    file1 = File("File 1")
    file2 = File("File 2")
    file3 = File("File 3")

    root.add(folder1)
    root.add(folder2)
    folder1.add(file1)
    folder2.add(file2)
    folder2.add(file3)

    print("Displaying the file system hierarchy:")
    root.display()
