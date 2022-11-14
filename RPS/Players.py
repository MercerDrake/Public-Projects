import random
import Game

# -------------------------Player Classes---------------------------
# The default Player class, has no internal logic always picks rock.
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
    
    # A Method which increments the number of wins for each instance.
    def count(self):
        self.wins += 1

    # A method which chooses the CPU move.  For the default class it's always rock.
    def choose(self):
        return "Rock"

# A child class of Player.  Chooses it's move at random.
class RandomPlayer(Player):
    def choose(self, choices):
        choice = random.choice(choices)
        return choice

# A child class of Player.  The user-playable classes.  Lets the user
# Select their own move to play against the CPU.
class HumanPlayer(Player):
    def move(self):
        choice = ""
        while True:
            choice = input("Please select 'Rock', 'Paper', or 'Scissors': ")
            if (choice.lower() != 'rock' and choice.lower() != 'paper' and choice.lower() != 'scissors'):
                Game.PausePrint()
                print("Sorry, that's not a valid input.")
                Game.PausePrint()
            if (choice.lower() == 'rock' or choice.lower() == 'paper' or choice.lower() == 'scissors'):
                break
        return choice

# A child class of Player.  The ReflectPlayer uses the move the player used in the last round.
class ReflectPlayer(Player):
    def __init__ (self, name, choice2):
        self.reflect = choice2
        self.name = name
        self.turns = 0
        self.prevmoves = []
        super().__init__(name)

    # A method that chooses the move of the ReflectPlayer class.  It starts the game by selecting
    # A random move.  It then appends the move the player used that turn in a list.  All rounds following
    # It will select the most recent move stored in the list.
    def choose(self, choice2, choices):
        if self.turns == 0:
            self.prevmoves.append(random.choice(choices))
            self.reflect = choice2
            self.turns += 1
        else:
            self.prevmoves.append(self.reflect)
            self.reflect = choice2
            self.turns += 1
        return self.prevmoves[self.turns - 1]

# A child class of Player.  The CyclePlayer will cycle through the list of RPS moves.
# It starts a game by choosing rock and then every round after that it will use the next
# Move in the list.  If it gets to the end of the move list it will wrap around to the 
# Beginning of the list.
class CyclePlayer(Player):
    def __init__ (self, name):
        self.name = name
        self.turns = 0
        self.i = 0
        super().__init__(name)

    # A method to select the move of the CyclePlayer.  It uses the modulus operator
    # To cycle through the 3 moves of Rock Paper Scissors.
    def choose(self, choices):
        self.i = self.i % 3
        choice1 = choices[self.i]
        self.i += 1
        return choice1