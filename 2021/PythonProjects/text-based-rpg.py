#Imports

import random

#Generating the map and events

squareType = ["Swamp", "Grassland", "Hill"]
squareEvents = ["No enemies in site", "A monster sits before you"]
squareLocation = [0, 0]

#Variables

exitCode = False
xLocation = squareLocation[0]
yLocation = squareLocation[1]

#Main loop

while exitCode != True:
    
    Type = random.choices(squareType, weights=(10, 20, 10), k=1)
    Event = random.choices(squareEvents, weights=(50, 20), k=1)

    Question = input("Which way would you like to go? (UP, DOWN, LEFT, RIGHT): ")

    if Question == "UP":
        yLocation += 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(squareLocation)
        continue
    elif Question == "DOWN":
        yLocation -= 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(squareLocation)
        continue
    elif Question == "LEFT":
        xLocation
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(squareLocation)
        continue
    elif Question == "RIGHT":
        xLocation += 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(squareLocation)
        continue
    else:
        continue

    