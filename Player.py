import random
from Bunker import Bunker

class Player():
    name = str
    surname = str
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