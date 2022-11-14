import Players
import random
import time

# Defines the only choices in a game of rock paper scissors.
choices = ['Rock', 'Paper', 'Scissors'] 

# -------------------------Testing Tools----------------------------

# -------------------------Game Class-------------------------------
# The default Game class.  This contains all the method for running a game of RPS.
class Game:
    
    # Method to print out the game intro, get the number of rounds from the User
    # And checks that it is valid.
    def print_intro(self):
        print("\nWelcome to Crazy Davey's Rochambeau!", flush = True)
        PausePrint()
        
        # Asks the User for the number of rounds and verifies that the number is valid.
        while True:
            rounds = input("How many rounds should we play? ")
            try:
                if int(rounds) > 0:
                    break
                else:
                    print(f"\nSorry, that's not a valid number of rounds.", flush = True)
            except ValueError:
                print(f"\nSorry, that's not a valid number of rounds.", flush = True)
            PausePrint()
        
        # Checks number of rounds and reads it back to the User.
        if int(rounds) == 1:
            print(f"Excellent! {rounds} round!", flush = True)
            PausePrint()
        else:
            print(f"Excellent! {rounds} rounds!", flush = True)
            PausePrint()
        print(f"\nGet ready to create your User!", flush = True)
        print(f"--------------------------------\n", flush = True)
        PausePrint()
        return rounds

    # The method that creates the User, CPU, and selects number of rounds
    def setup_game(self, Users, rounds):
        CPU = Users[random.randint(0, 2)]

        # Asks the User for their name and creates a Player of that name.
        name = input("What is your name? ")
        Player = Players.HumanPlayer(name)
        if int(rounds) == 1:
            Game.one_round(choices, CPU, Player)
        else:
            Game.multi_round(choices, CPU, Player, rounds)
        Game.overall_outcome(CPU, Player)
    
    # Plays 1 round of the game.  Gets choices from User and CPU, prints choices.
    # Calls several functions which make up a round of play.
    def one_round(choices, CPU, Player):
        choice2 = Player.move()
        choice1 = Game.check_CPU_type(CPU, choice2)
        Game.print_choices(CPU, Player, choice1, choice2)
        Game.beats(choice1, choice2, CPU, Player)
        PausePrint()
        Game.print_outcome(CPU, Player)

    # Plays multiple rounds of the game (the number defined by the User).
    def multi_round(choices, CPU, Player, rounds):
        i = 0
        while i < int(rounds):
            Game.one_round(choices, CPU, Player)
            i += 1

    # A Method that checks to see which class the CPU is and calls the 
    # Proper .choose method and assigns to the choice1 variable.
    def check_CPU_type(CPU, choice2):
        if(isinstance(CPU, Players.RandomPlayer)):
            choice1 = CPU.choose(choices)
        elif(isinstance(CPU, Players.ReflectPlayer)):
            choice1 = CPU.choose(choice2, choices)
        elif(isinstance(CPU, Players.CyclePlayer)):
            choice1 = CPU.choose(choices)
        else:
            choice1 = "Rock"
        return choice1             

    # Prints out Player & CPU names and their respective choices.
    def print_choices(CPU, Player, choice1, choice2):
        PausePrint()
        print(f"\n{CPU.name} chooses {choice1}", flush = True) 
        PausePrint()
        print(f"{Player.name} chooses {choice2}", flush = True)
        PausePrint()

    # Prints the number of wins for the Player and CPU at the end of each round.
    def print_outcome(CPU, Player):
        print(f"{CPU.name}: {CPU.wins}", flush = True) 
        PausePrint()
        print(f"{Player.name}: {Player.wins}\n", flush = True)   

    # Calls a method based on which choice the CPU made. 
    def beats(choice1, choice2, CPU, Player):
        if choice1.lower() == 'rock':
            Game.rock(choice2, CPU, Player)
        elif choice1.lower() == 'scissors':
            Game.scissors(choice2, CPU, Player)
        elif choice1.lower() == 'paper':
            Game.paper(choice2, CPU, Player)
        else:
            print("Sorry, something has gone wrong.") # Exception handler

    # A method that runs if CPU chooses rock.  It compares the Player's move
    # Against rock and then prints who wins and increases the .wins variable
    # Or prints out that there's no winner in the case of a tie.
    def rock(choice2, CPU, Player):
        if 'scissors' in choice2.lower():
            print(f"\n{CPU.name} wins!\n", flush = True)
            CPU.count()
        elif 'paper' in choice2.lower():
            print(f"\n{Player.name} wins!\n", flush = True)
            Player.count()
        elif 'rock' in choice2.lower():
            print(f"\nNeither {CPU.name} nor {Player.name} win! It's a tie.\n", flush = True)

    # A method that runs if CPU chooses scissors.  It compares the Player's move
    # Against scissors and then prints who wins and increases the .wins variable
    # Or prints out that there's no winner in the case of a tie.
    def scissors(choice2, CPU, Player):
        if 'rock' in choice2.lower():
            print(f"\n{Player.name} wins!\n", flush = True)
            Player.count()
        elif 'paper' in choice2.lower():
            print(f"\n{CPU.name} wins!\n", flush = True)
            CPU.count()
        elif 'scissors' in choice2.lower():
            print(f"\nNeither {CPU.name} nor {Player.name} win! It's a tie.\n", flush = True) 

    # A method that runs if CPU chooses paper.  It compares the Player's move
    # Against paper and then prints who wins and increases the .wins variable
    # Or prints out that there's no winner in the case of a tie.
    def paper(choice2, CPU, Player):
        if 'rock' in choice2.lower():
            print(f"\n{CPU.name} wins!\n", flush = True)
            CPU.count()
        elif 'scissors' in choice2.lower():
            print(f"\n{Player.name} wins!\n", flush = True)
            Player.count()
        elif 'paper' in choice2.lower():
            print(f"\nNeither {CPU.name} nor {Player.name} win! It's a tie.\n", flush = True) 
    
    # A method that prints out a message at the end of the game.
    # Prints out a goodbye message and the final score of all the rounds.
    # Prints out a congratulations message to the winner.  Or a message
    # If no one won
    def overall_outcome(CPU, Player):
        PausePrint()
        print("\nThanks for playing!", flush = True)
        PausePrint()
        print(f"\n  Final Score:", flush = True)
        print(f"---------------")
        PausePrint()
        print(f"  {CPU.name}: {CPU.wins}", flush = True)
        PausePrint()
        print(f"  {Player.name}: {Player.wins}", flush = True)
        PausePrint()
        if CPU.wins > Player.wins:
            print(f"\nCongratulations, {CPU.name}", flush = True)
        elif CPU.wins < Player.wins:
            print(f"\nCongratulations, {Player.name}", flush = True)
        else:
            print(f"\nNo winners this time, try again!", flush = True)

# --------------------------Housekeeping Functions---------------------
# Method that creates a 1 second pause
def PausePrint():
    time.sleep(1)