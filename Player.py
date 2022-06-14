import random
import time
from Bunker import Bunker

class Player():
    name = str
    surname = str
    health = int
    hunger = int
    thirst = int
    level = int
    bunker = object()

    def __init__(self):
        with open("data/names.txt", "r") as f:
            self.name = random.choice(f.readlines())
            self.name = self.name.replace("\n", "")
        with open("data/surnames.txt", "r") as f:
            self.surname = random.choice(f.readlines())
            self.surname = self.surname.replace("\n", "")

        self.bunker = Bunker() 
        self.bunker.owner = self # The Player is the owner of the created bunker
        self.level = 0
        self.health = 100
        self.hunger = 100
        self.thirst = 100

        


