from player import Player
from ai_computer import AI_Computer
from human import Human

class Game():
    def __init__(self):
        self.player = Human('P1')
        self.rounds = 0
        self.player_2= Human('P2')
        self.computer = AI_Computer('computer')
        self.current_round = 0
        self.player_points = 0
        self.player_2_points = 0
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
        result = self.single_or_multiplayer()
        self.choose_rounds()
        while self.current_round < self.rounds:
            self.current_round += 1
            self.choose_gesture(result)
            round_winner = self.compare_gesture(result)
            self.determine_winner_round(round_winner)
        self.determine_game_won()
        self.display_winner()


    def choose_rounds(self):
        while self.rounds < 3:
            self.rounds = int(input('Enter the number of rounds, minimum three rounds: '))
        
    def single_or_multiplayer(self):
        players = input('Choose to play with human or computer: ')
        if players == 'computer':
            return self.computer
        if players == 'human':
            return self.player_2

    def choose_gesture(self, result):
        self.player.select()
        if result == self.computer:
            self.computer.random_selection()
        elif result == self.player_2:
            self.player_2.select()

    def compare_gesture(self, result):
        '''
        Comparison of gestures between principal player and player2 as human
        '''
        if result == self.player_2:
            if self.player.gesture == self.player_2.gesture:
                return None
            if self.player.gesture == "Rock" and self.player_2.gesture == "Scissors":
                return self.player
            elif self.player.gesture == "Scissors" and self.player_2.gesture == "Paper":
                return self.player
            elif self.player.gesture == "Paper" and self.player_2.gesture == "Rock":
                return self.player
            elif self.player.gesture == "Rock" and self.player_2.gesture == "Lizard":
                return self.player
            elif self.player.gesture == "Lizard" and self.player_2.gesture == "Spock":
                return self.player             
            elif self.player.gesture == "Spock" and self.player_2.gesture == "Scissors":
                return self.player
            elif self.player.gesture == "Scissors" and self.player_2.gesture == "Lizard":
                return self.player
            elif self.player.gesture == "Lizard" and self.player_2.gesture == "Paper":
                return self.player
            elif self.player.gesture == "Paper" and self.player_2.gesture == "Spock":
                return self.player
            elif self.player.gesture == "Spock" and self.player_2.gesture == "Rock":
                return self.player
            elif self.player_2.gesture == "Rock" and self.player.gesture == "Scissors":
                return self.player_2
            elif self.player_2.gesture == "Scissors" and self.player.gesture == "Paper":
                return self.player_2
            elif self.player_2.gesture == "Paper" and self.player.gesture == "Rock":
                return self.player_2
            elif self.player_2.gesture == "Rock" and self.player.gesture == "Lizard":
                return self.player_2
            elif self.player_2.gesture == "Lizard" and self.player.gesture == "Spock":
                return self.player_2             
            elif self.player_2.gesture == "Spock" and self.player.gesture == "Scissors":
                return self.player_2
            elif self.player_2.gesture == "Scissors" and self.player.gesture == "Lizard":
                return self.player_2
            elif self.player_2.gesture == "Lizard" and self.player.gesture == "Paper":
                return self.player_2
            elif self.player_2.gesture == "Paper" and self.player.gesture == "Spock":
                return self.player_2
            elif self.player_2.gesture == "Spock" and self.player.gesture == "Rock":
                return self.player_2
        '''
        Comparison of gestures between principal player and player2 as computer
        '''       
        if result == self.computer:
            if self.player.gesture == self.computer.gesture:
                return None
            if self.player.gesture == "Rock" and self.computer.gesture == "Scissors":
                return self.player
            elif self.player.gesture == "Scissors" and self.computer.gesture == "Paper":
                return self.player
            elif self.player.gesture == "Paper" and self.computer.gesture == "Rock":
                return self.player
            elif self.player.gesture == "Rock" and self.computer.gesture == "Lizard":
                return self.player
            elif self.player.gesture == "Lizard" and self.computer.gesture == "Spock":
                return self.player             
            elif self.player.gesture == "Spock" and self.computer.gesture == "Scissors":
                return self.player
            elif self.player.gesture == "Scissors" and self.computer.gesture == "Lizard":
                return self.player
            elif self.player.gesture == "Lizard" and self.computer.gesture == "Paper":
                return self.player
            elif self.player.gesture == "Paper" and self.computer.gesture == "Spock":
                return self.player
            elif self.player.gesture == "Spock" and self.computer.gesture == "Rock":
                return self.player
            elif self.computer.gesture == "Rock" and self.player.gesture == "Scissors":
                return self.player_2
            elif self.computer.gesture == "Scissors" and self.player.gesture == "Paper":
                return self.player_2
            elif self.computer.gesture == "Paper" and self.player.gesture == "Rock":
                return self.player_2
            elif self.computer.gesture == "Rock" and self.player.gesture == "Lizard":
                return self.player_2
            elif self.computer.gesture == "Lizard" and self.player.gesture == "Spock":
                return self.player_2             
            elif self.computer.gesture == "Spock" and self.player.gesture == "Scissors":
                return self.player_2
            elif self.computer.gesture == "Scissors" and self.player.gesture == "Lizard":
                return self.player_2
            elif self.computer.gesture == "Lizard" and self.player.gesture == "Paper":
                return self.player_2
            elif self.computer.gesture == "Paper" and self.player.gesture == "Spock":
                return self.player_2
            elif self.computer.gesture == "Spock" and self.player.gesture == "Rock":
                return self.player_2

    def determine_winner_round(self, round_winner):
        if round_winner == self.player:
            self.player_points += 1
            print(f'Winner of the round: {self.player.name}')
        elif round_winner == self.player_2:
            self.player_2_points += 1
            print(f'Winner of the round: {self.player_2.name}')
        else:
            print('Tied')

    def determine_game_won(self):
        half = self.rounds // 2
        if self.player_points > half:
            self.winner = self.player
        elif self.player_2_points > half:
            self.winner = self.player_2


    def display_winner(self):
        if self.winner == None:
            print('No winner')
        else:
            print(f'Winner of the game {self.winner.name}')