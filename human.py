from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
   
    def select(self):
        self.gesture = input(f"Please type any of the next options: {self.gesture_options} ")