from ai_computer import AI_Computer
from human import Human


class Game():
    def __init__(self):
        self.player1 = Human('P1')
        self.player2 = Human('P2')
        self.rounds = 0
        self.current_round = 0
        self.player1_points = 0
        self.player2_points = 0
        self.winner = None
    
    def display_welcome(self):
        print('''Welcome to RPSLS. This are the game rules:
                    Rock crushes Scissors
                    Scissors cuts Paper
                    Paper covers Rock
                    Rock crushes Lizard
                    Lizard poisons Spock
                    Spock smashes Scissors
                    Scissors decapitates Lizard
                    Lizard eats Paper
                    Paper disproves Spock
                    Spock vaporizes Rock''')

    def run_game(self):
        self.display_welcome()
        self.single_or_multiplayer()
        self.choose_rounds()
        while self.current_round < self.rounds:
            self.current_round += 1
            self.choose_gesture()
            round_winner = self.compare_gesture()
            self.determine_winner_round(round_winner)
        self.determine_game_won()
        self.display_winner()


    def choose_rounds(self):
        while self.rounds < 3:
            self.rounds = int(input('Enter the number of rounds, minimum three rounds: '))
        
    def single_or_multiplayer(self):
        players = input('Choose to play with human or computer: ')
        if players == 'computer':
            self.player2 = AI_Computer('computer')

    def choose_gesture(self):
        self.player1.add_names()
        self.player1.select()
        if self.player2 == Human('P2'):
            self.player2.add_names
        self.player2.select()

    def compare_gesture(self):
        if self.player1.gesture.gesture_name == self.player2.gesture.gesture_name:
            return None
            
        if self.player1.gesture.gesture_name == 'Rock':
            loses = self.player2.gesture.gesture_name in self.player1.gesture.loses_to
            if loses == True:
                return self.player2
            elif loses == False:
                return self.player1

        elif self.player1.gesture.gesture_name == 'Paper':
            loses = self.player2.gesture.gesture_name in self.player1.gesture.loses_to
            if loses == True:
                return self.player2
            elif loses == False:
                return self.player1
        
        elif self.player1.gesture.gesture_name == 'Scissors':
            loses = self.player2.gesture.gesture_name in self.player1.gesture.loses_to
            if loses == True:
                return self.player2
            elif loses == False:
                return self.player1

        elif self.player1.gesture.gesture_name == 'Lizard':
            loses = self.player2.gesture.gesture_name in self.player1.gesture.loses_to
            if loses == True:
                return self.player2
            elif loses == False:
                return self.player1

        elif self.player1.gesture.gesture_name == 'Spock':
            loses = self.player2.gesture.gesture_name in self.player1.gesture.loses_to
            if loses == True:
                return self.player2
            elif loses == False:
                return self.player1
      
        # if self.player1.gesture == self.player2.gesture:
        #     return None
        # if self.player1.gesture == "Rock" and self.player2.gesture == "Scissors":
        #     return self.player1
        # elif self.player1.gesture == "Scissors" and self.player2.gesture == "Paper":
        #     return self.player1
        # elif self.player1.gesture == "Paper" and self.player2.gesture == "Rock":
        #     return self.player1
        # elif self.player1.gesture == "Rock" and self.player2.gesture == "Lizard":
        #     return self.player1
        # elif self.player1.gesture == "Lizard" and self.player2.gesture == "Spock":
        #     return self.player1             
        # elif self.player1.gesture == "Spock" and self.player2.gesture == "Scissors":
        #     return self.player1
        # elif self.player1.gesture == "Scissors" and self.player2.gesture == "Lizard":
        #     return self.player1
        # elif self.player1.gesture == "Lizard" and self.player2.gesture == "Paper":
        #     return self.player1
        # elif self.player1.gesture == "Paper" and self.player2.gesture == "Spock":
        #     return self.player1
        # elif self.player1.gesture == "Spock" and self.player2.gesture == "Rock":
        #     return self.player1
        # elif self.player2.gesture == "Rock" and self.player1.gesture == "Scissors":
        #     return self.player2
        # elif self.player2.gesture == "Scissors" and self.player1.gesture == "Paper":
        #     return self.player2
        # elif self.player2.gesture == "Paper" and self.player1.gesture == "Rock":
        #     return self.player2
        # elif self.player2.gesture == "Rock" and self.player1.gesture == "Lizard":
        #     return self.player2
        # elif self.player2.gesture == "Lizard" and self.player1.gesture == "Spock":
        #     return self.player2             
        # elif self.player2.gesture == "Spock" and self.player1.gesture == "Scissors":
        #     return self.player2
        # elif self.player2.gesture == "Scissors" and self.player1.gesture == "Lizard":
        #     return self.player2
        # elif self.player2.gesture == "Lizard" and self.player1.gesture == "Paper":
        #     return self.player2
        # elif self.player2.gesture == "Paper" and self.player1.gesture == "Spock":
        #     return self.player2
        # elif self.player2.gesture == "Spock" and self.player1.gesture == "Rock":
        #     return self.player2
    
    def determine_winner_round(self, round_winner):
        if round_winner == self.player1:
            self.player1_points += 1
            print(f'Winner of the round: {self.player1.name}')
        elif round_winner == self.player2:
            self.player2_points += 1
            print(f'Winner of the round: {self.player2.name}')
        else:
            print('Tied')

    def determine_game_won(self):
        half = self.rounds // 2
        if self.player1_points > half:
            self.winner = self.player1
        elif self.player2_points > half:
            self.winner = self.player2


    def display_winner(self):
        if self.winner == None:
            print('No winner')
        else:
            print(f'Winner of the game {self.winner.name}')