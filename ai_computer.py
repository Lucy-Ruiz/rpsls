from player import Player
import random
class AI_Computer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def random_selection(self):
        self.gesture = random.choice(self.gesture_options)
        print(self.gesture)

