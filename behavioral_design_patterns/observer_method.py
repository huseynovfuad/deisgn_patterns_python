"""
The Observer design pattern is a behavioral design pattern that defines a one-to-many dependency 
between objects, so that when one object changes state, all its dependents (observers) are notified 
and updated automatically. This pattern is commonly used in situations where you need 
to maintain consistency between related objects.
"""


from abc import ABC, abstractmethod

# Define the Subject interface (Observable)
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete implementation of the Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print("Setting temperature to", temperature)
        self._temperature = temperature
        self.notify()

# Define the Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete implementation of the Observer
class WeatherDisplay(Observer):
    def __init__(self):
        self._temperature = None

    def update(self, temperature):
        self._temperature = temperature
        self.display()

    def display(self):
        print("Weather Display: Current Temperature is {} degrees".format(self._temperature))

# Concrete implementation of another Observer
class Logger(Observer):
    def update(self, temperature):
        print("Logger: Temperature updated to {} degrees".format(temperature))

# Example usage
if __name__ == "__main__":
    weather_station = WeatherStation()

    display_observer = WeatherDisplay()
    logger_observer = Logger()

    weather_station.attach(display_observer)
    weather_station.attach(logger_observer)

    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    weather_station.detach(logger_observer)

    weather_station.set_temperature(28)
