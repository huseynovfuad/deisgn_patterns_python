"""
The Facade design pattern is a structural design pattern that provides a simplified interface 
to a complex system of classes, functions, or objects. It helps hide the complexity of the system and 
provides a unified interface for the client code to interact with.
"""


# Subsystem components
class DVDPlayer:
    def turn_on(self):
        print("DVD Player is on")

    def play_movie(self, movie):
        print(f"Playing movie: {movie}")

    def turn_off(self):
        print("DVD Player is off")


class AudioSystem:
    def turn_on(self):
        print("Audio System is on")

    def set_volume(self, volume):
        print(f"Setting volume to {volume}")

    def turn_off(self):
        print("Audio System is off")


class Projector:
    def turn_on(self):
        print("Projector is on")

    def display_movie(self, movie):
        print(f"Displaying {movie} on the screen")

    def turn_off(self):
        print("Projector is off")


# Facade for the home theater system
class HomeTheaterFacade:
    def __init__(self):
        self.dvd_player = DVDPlayer()
        self.audio_system = AudioSystem()
        self.projector = Projector()

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.dvd_player.turn_on()
        self.dvd_player.play_movie(movie)
        self.audio_system.turn_on()
        self.audio_system.set_volume(10)
        self.projector.turn_on()
        self.projector.display_movie(movie)

    def end_movie(self):
        print("Shutting down the home theater...")
        self.dvd_player.turn_off()
        self.audio_system.turn_off()
        self.projector.turn_off()


# Client code
if __name__ == "__main__":
    theater = HomeTheaterFacade()
    movie_name = "The Avengers"

    theater.watch_movie(movie_name)
    print("\nMovie is over...")
    theater.end_movie()
