MAGIC_NUMBER = 7

while input("Guessing Game: Type q to quit ") != 'q':
    
    guess = int(input("Guess a number: "))
    
    if guess != MAGIC_NUMBER:
        print("Sorry your answer did not match the magic number")
        continue
    else:
        print("YOU GUESSED IT")
        break
