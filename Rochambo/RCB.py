import Players
import Game
import random

if __name__ == '__main__':
    # player_name = input("Hello! What's your name? ")
    CPUName = ["Andy", "Brad", "Camelia", "Daniel", "Dan", "Davey", "Erik", "Jaimie" ,"Jessica", "Laura", "Merii", "n00bles", "Ren", "Sabrina", "Tim", "Will"] # A list of names to assign randomly to the CPU
    players = [Players.Player("Pleb"), Players.RandomPlayer(random.choice(CPUName)), Players.CyclePlayer(random.choice(CPUName), ""), Players.ReflectPlayer(random.choice(CPUName), "")] 
    # A list of CPU types, also assigns a random name to the CPU
    game = Game.Game(players) # Creates a game object and passes the players to it.
    game.play(CPUName) # Method that plays the game``