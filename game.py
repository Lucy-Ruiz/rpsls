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
        self.player1.select()
        self.player2.select()

    def compare_gesture(self):
        if self.player1.gesture.gesture_name == self.player2.gesture.gesture_name:
            return None
        elif self.player1.gesture.gesture_name in self.player2.gesture.loses_to:
            return self.player1
        else:
            return self.player2

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