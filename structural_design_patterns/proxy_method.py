"""
The Proxy design pattern is a structural design pattern that provides a surrogate or placeholder 
for another object to control access to it. It is often used to add an extra layer of control or 
functionality to an object, such as lazy loading, access control, logging, or caching.
"""

from abc import ABC, abstractmethod

# Subject interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject class
class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")

# Proxy class
class ProxyImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# Client code
if __name__ == "__main__":
    # Using the Proxy to load and display the image
    image_proxy = ProxyImage("high_resolution_image.jpg")

    # The image is not loaded until display() is called
    print("Image is loaded lazily:")
    image_proxy.display()

    # The image is already loaded, so it's just displayed again
    print("\nImage is displayed directly:")
    image_proxy.display()
