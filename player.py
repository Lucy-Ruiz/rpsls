from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = None
        self.gesture_options = [Rock('Rock'), Paper('Paper'), Scissors('Scissors'), Lizard('Lizard'), Spock('Spock')]
    
    def display_gesture_options(self):
        for gesture in self.gesture_options:
            print(gesture.gesture_name)

    def select(self):
        pass
        