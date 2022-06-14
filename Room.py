class Room():
    maxPeople = 2
    size = "small" 
    peopleContention = []
    type = str # waterpump, cafeteria, sleeping room, storage room, power generator
    powerConsumption = int # per minutes
    
    neighbours={
    "north": None,
    "south": None,
    "west": None,
    "east": None,
        }


    