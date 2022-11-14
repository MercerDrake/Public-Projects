import random
import Game

class Player: #The default player class. Has no internal logic
    def __init__(self, name):
        self.name = name # Stores the Player instance's name
        self.wins = 0    # Stores the Player instance's number of won games

    def count(self): # Method designed to increment the number of wins for each instance
        self.wins += 1

    def choose(self):
        choice = "Rock"
        return choice

class RandomPlayer(Player): # A player that chooses it's move at complete random
    def choose(self, choices):
        choice = random.choice(choices) # Randomly selects one of the choices and assigns it to choice
        return choice # Returns choice

class HumanPlayer(Player): # Defines the human player class
    def move(self):
        choice = "" # Creates and defines the variable for the Player's choice.
        while True: # Loop to ask the player which move they'd like to select
            choice = input("Please select 'Rock', 'Paper', 'Scissors' or 'Quit' to end the game: ")
            if (choice.lower() != 'rock' and choice.lower() != 'paper' and choice.lower() != 'scissors' and choice.lower() != 'quit'): # Checks to make sure the input is valid
                Game.PausePrint()
                print("Sorry, that's not a valid input.")
                Game.PausePrint()
            if (choice.lower() == 'rock' or choice.lower() == 'paper' or choice.lower() == 'scissors' or choice.lower() == 'quit'): # If it's a valid input it breaks out of the loop.
                break
        return choice

class ReflectPlayer(Player): # A CPU type that will use the move the player used the last round
    def __init__ (self, name, choice2):
        self.reflect = choice2 # Stores the move the Player made last round
        self.name = name # Stores the name of the CPU
        self.turns = 0
        self.prevmoves = []
        super().__init__(name)

    def choose(self, choice2, choices): # Sets the CPU's choice to the move the Player used last round
        if self.turns == 0:
            self.prevmoves.append(random.choice(choices))
            self.reflect = choice2
            self.turns += 1
        elif self.turns < 0:
            self.prevmoves.append(choice2)
            self.reflect = self.prevmoves[self.turns]
        return self.reflect
    
class CyclePlayer(Player):   # A CPU type that will cycle through the list of choices
    def __init__ (self, name, choice1):
        self.cycle = choice1 # A variable that stores the move the CPU used last turn
        self.name = name
        self.i = 0 # An index variable for cycling through the possible moves
        super().__init__(name)

    def choose(self, choices, choice1): # The method which selects the CPU's move based on it's last move
        self.cycle = choice1
        if(self.cycle == choices[2]): # If the move cycle is at the end of the list it moves back to the beginning
            self.i = 0                
        else:                         # If the move cycle is not at the end of the list it moves to the next item in the list.
            self.i += 1
        return choices[self.i]