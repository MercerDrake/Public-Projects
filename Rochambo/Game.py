import Players
import time
import random

# Defines the only choices in a game of rock paper scissors
choices = ['Rock', 'Paper', 'Scissors']


class Game:
    def __init__(self, players):
        self.players = players

    def print_intro():  # Prints out the intro explaining the rules
        print("\nWelcome to Crazy Davey's Rochambeau!")
        PausePrint()
        print("1 game is best out of five")
        PausePrint()
        print("Get ready to create your player!")
        print("--------------------------------\n")

    def play(self, CPUName):
        # creates and initializes the CPU's choice
        choice1 = random.choice(choices)
        # creates and initializes the Player's choice
        choice2 = random.choice(choices)
        # Randomly selects which CPU the Player will play against
        CPU1 = self.players[random.randint(0, 3)]

        Game.print_intro()
        PausePrint()
        playerName = input("What is your name? ")  # Creates & names the player
        if playerName == 'Davey':
            # Secret message
            print("\nThat's interesting, but I'm skeptical. Cool if true though.\n")
        if playerName in CPUName:
            print(f"\nYou are a dear friend and I love you.\n")

        Player = Players.HumanPlayer(playerName)

        # Main game loop, runs the game as long as neither score = 3 (Best out of 5)
        while CPU1.wins < 3 and Player.wins < 3:
            if (isinstance(CPU1, Players.RandomPlayer)):
                # Assign a move for the RandomPlayer AI
                choice1 = CPU1.choose(choices)
            elif (isinstance(CPU1, Players.ReflectPlayer)):
                # Assign a move for the ReflectPlayer AI
                choice1 = CPU1.choose(choice2)
            elif (isinstance(CPU1, Players.CyclePlayer)):
                # Assign a move for the CyclePlayer AI
                choice1 = CPU1.choose(choices, choice1)
            else:
                choice1 = "Rock"                        # Assign a move for the Pleb player

            choice2 = Player.move()  # Assigns a move for the human player
            if choice2.lower() == 'quit':  # Quits the game early if the player enters "quit" into 'Choice'
                break

            PausePrint()
            # Prints out Player & CPU names and their choices
            print(f"\n{CPU1.name} chooses {choice1}")
            PausePrint()
            print(f"{Player.name} chooses {choice2}")
            PausePrint()
            # Calls the beats method which examines the choices of Player & CPU
            Game.beats(choice1, choice2, CPU1, Player)

            # Prints number of wins for Player and CPU at the end of each round.
            print(f"{CPU1.name}: {CPU1.wins}")
            PausePrint()
            print(f"{Player.name}: {Player.wins}\n")
        PausePrint()
        # Prints a good-bye message at the end of the game
        print("\nThanks for playing!")
        PausePrint()
        # Prints out the final score of all the rounds
        print(f"\n  Final Score:")
        print(f"---------------")
        PausePrint()
        print(f"  {CPU1.name}: {CPU1.wins}")
        PausePrint()
        print(f"  {Player.name}: {Player.wins}")

        PausePrint()               # Prints a message that displays the overall winner
        if (CPU1.wins > Player.wins):
            print(f"\n{CPU1.name} Wins!")
        elif (CPU1.wins < Player.wins):
            print(f"\n{Player.name} Wins!")
        else:
            print("Strange... no one won... huh.")

    def beats(choice1, choice2, CPU1, Player):  # Calls a function based on which choice CPU made
        if choice1 == 'rock':
            Game.rock(choice2, CPU1, Player)
            PausePrint()
        elif choice1 == 'scissors':
            Game.scissors(choice2, CPU1, Player)
            PausePrint()
        elif choice1 == 'paper':
            Game.paper(choice2, CPU1, Player)
            PausePrint()
        else:
            print("Sorry, something has gone wrong.")

    def rock(choice2, CPU1, Player):  # The logic for what to do if CPU chooses Rock
        if 'scissors' in choice2.lower():  # If Player chooses Scissors
            print(f"\n{CPU1.name} wins!\n")  # Prints "'CPU' Wins!#
            CPU1.count()                  # Calls count method which increments CPU's number of wins
        elif 'paper' in choice2.lower():
            print(f"\n{Player.name} wins!\n")
            Player.count()
        elif 'rock' in choice2.lower():  # What to do in the event of a tie
            # Prints that there's a tie, no count method call.
            print(
                f"\nNeither {CPU1.name} nor {Player.name} win! It's a tie.\n")

    def scissors(choice2, CPU1, Player):  # The logic for what to do if CPU chooses Scissors
        if 'rock' in choice2.lower():        # If Player chooses Rock
            print(f"\n{Player.name} wins!\n")    # Prints "'Player' Wins!"
            # Calls count method which increments Player's number of wins
            Player.count()
        elif 'paper' in choice2.lower():
            print(f"\n{CPU1.name} wins!\n")
            CPU1.count()
        elif 'scissors' in choice2.lower():  # What to do in the event of a tie
            # Prints that there's a tie, no count method call.
            print(
                f"\nNeither {CPU1.name} nor {Player.name} win! It's a tie.\n")

    def paper(choice2, CPU1, Player):  # The logic for what to do if CPU chooses Paper
        if 'rock' in choice2.lower():     # If 'Player 2' chooses Rock
            print(f"\n{CPU1.name} wins!\n")  # Prints "'Player' 1 Wins!"
            CPU1.count()                  # Calls count method which increments CPU's number of wins
        elif 'scissors' in choice2.lower():
            print(f"\n{Player.name} wins!\n")
            Player.count()
        elif 'paper' in choice2.lower():  # What to do in the event of a tie
            # Prints that there's a tie, no count method call
            print(
                f"\nNeither {CPU1.name} nor {Player.name} win! It's a tie.\n")


def PausePrint():  # Function to take a pause between printing each method
    time.sleep(1)
