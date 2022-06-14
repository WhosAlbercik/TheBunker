import random
from Building import Building
from Room import Room

class Bunker(Building):
    owner = object()
  
    # self.rooms is inherited from Building()

    def __init__(self):
        super().__init__()
        self.type = "Bunker"

        vaultDoor = Room()
        vaultDoor.powerConsumption = 0
        vaultDoor.type = "Vault Door"
        self.rooms.append(vaultDoor) 
        
        powerRoom = Room()
        powerRoom.powerConsumption = 0
        powerRoom.type = "Power Generator"
        self.rooms.append(powerRoom)

        cafeteriaRoom = Room()
        cafeteriaRoom.powerConsumption = 2
        cafeteriaRoom.type = "Cafeteria"
        self.rooms.append(cafeteriaRoom)

        waterRoom = Room()
        waterRoom.powerConsumption = 2
        waterRoom.type = "Water Pump"
        self.rooms.append(waterRoom)

        unBuiltRooms = self.rooms
        unBuiltRooms.remove(vaultDoor)
        sides = ['north', 'south', 'west', 'east']

        while unBuiltRooms != []: # 'builds' the rooms to a random side of the vault room
            roomSide = random.choice(sides)


            if roomSide == 'north':
                room = random.choice(unBuiltRooms)
                vaultDoor.neighbours['north'] = room
                unBuiltRooms.remove(room)
                sides.remove('north')

            elif roomSide == 'south':
                room = random.choice(unBuiltRooms)
                vaultDoor.neighbours['south'] = room
                unBuiltRooms.remove(room)
                sides.remove('south')

            elif roomSide == 'west':
                room = random.choice(unBuiltRooms)
                vaultDoor.neighbours['west'] = room
                unBuiltRooms.remove(room)
                sides.remove('west')

            elif roomSide == 'east':
                room = random.choice(unBuiltRooms)
                vaultDoor.neighbours['east'] = room
                unBuiltRooms.remove(room)
                sides.remove('east')