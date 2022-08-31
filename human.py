from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
   
    def add_names(self):
       for object in self.gesture_options:
           print(object.gesture_name)


    def select(self):
        self.gesture = None
        while self.gesture not in self.gesture_options: 
            self.display_gesture_options()
            human_input = input(f"Please type any of the options above: ")
            if human_input == 'Rock':
                self.gesture = self.gesture_options[0]
            elif human_input == "Paper":
                self.gesture = self.gesture_options[1]
            elif human_input == 'Scissors':
                self.gesture = self.gesture_options[2]
            elif human_input == 'Lizard':
                self.gesture = self.gesture_options[3]
            elif human_input == "Spock":
                self.gesture = self.gesture_options[4]
            else:
                print("Not a valid option!")