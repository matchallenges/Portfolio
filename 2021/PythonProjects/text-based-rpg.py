#Imports

import random

#Generating the map and events

squareType = ["Swamp", "Grassland", "Hill"]
squareEvents = ["No enemies in site", "A monster sits before you"]
fighting = ["Dead", "Alive"]
fighting_result = ["Dead"]
monster_ecounter = ["A monster sits before you"]
x = 0
y = 0

#Main loop

while True:

    Type = random.choices(squareType, weights=(10, 20, 10), k=1)
    Event = random.choices(squareEvents, weights=(50, 20), k=1)
    Monst =  random.choices(monster_ecounter, k=1)
    Question = input("Which way would you like to go? (UP, DOWN, LEFT, RIGHT): ")
    
    if Question == "UP":
        y += 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(x, y)
        if Event == Monst:
            print("You are fighting curageously")
            die = random.choices(fighting, weights=(10, 10), k=1)
            die1 = random.choices(fighting_result,  k=1)
            if die == die1:
                print("You died in the process")
                exit()
            else:
                continue

    elif Question == "DOWN":
        y -= 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(x, y)
        if Event == Monst:
            print("You are fighting curageously")
            die = random.choices(fighting, weights=(10, 10), k=1)
            die1 = random.choices(fighting_result,  k=1)
            if die == die1:
                print("You died in the process")
                exit()
            else:
                continue

    elif Question == "LEFT":
        x -= 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(x, y)
        if Event == Monst:
            print("You are fighting curageously")
            die = random.choices(fighting, weights=(10, 10), k=1)
            die1 = random.choices(fighting_result,  k=1)
            if die == die1:
                print("You died in the process")
                exit()
            else:
                continue

    elif Question == "RIGHT":
        x += 1
        print("Scenery: ")
        print(*Type)
        print("Event: ")
        print(*Event)
        print("Location: ")
        print(x, y)
        if Event == Monst:
            print("You are fighting curageously")
            die = random.choices(fighting, weights=(10, 10), k=1)
            die1 = random.choices(fighting_result,  k=1)
            if die == die1:
                print("You died in the process")
                exit()
            else:
                continue

    

    