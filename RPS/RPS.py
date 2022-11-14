# Version 3.0
# Dave Kelly

import Game
import Players
import random

# -------------------------Play Area--------------------------------
if __name__ == '__main__':

    # A list of names to assign randomly to the CPU. 
    CPUName = ["Andy", "Brad", "Camelia", "Daniel", "Dan", "Davey",
               "Erik", "Jaimie" ,"Jessica", "Laura", "Merii", "n00bles",
               "Ren", "Sabrina", "Tim", "Will"]

    # A list of potential players of the various AI types.
    players = [Players.Player("Pleb"), 
               Players.RandomPlayer(random.choice(CPUName)),
               Players.ReflectPlayer(random.choice(CPUName), ""),
               Players.CyclePlayer(random.choice(CPUName))]
    game = Game.Game() 
    rounds = game.print_intro()

    # Sets up game by creating players and processing # of rounds
    game.setup_game(players, rounds)
