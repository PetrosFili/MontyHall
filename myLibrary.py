import random

#return array of length 3 with 2 entries being 0 (goats) and 1 entry being 1 (car)
def generateDoors():
    doors = [0, 0, 0]
    prize_index = random.randint(0,2)
    doors[prize_index] = 1
    return doors

#return random guess of the 3 doors
def generateGuess():
    return random.randint(0,2)

#return new door array with one of the 0's removed (aka turned to -1)
def getNewDoors(doors, guess):
    for i in range(len(doors)):
        if (i != guess) & (doors[i] != 1):
            doors[i] = -1 #signifies door is out of question
            break
    return doors

#randomly generate whether or not player switches their guess
#def doesPlayerSwitch():
#    #return 0 if player doesn't switch, return 1 if they do
#    return random.randint(0,1)

#returns new guess. Aka the player switches guess after goat door has been revealed
def generateNewGuess(doors, guess):
    for i in range(len(doors)):
        if (i != guess) & (doors[i] != -1):
            return i

#simulate Monty Hall problem n times trying both strategies
#returns correct guess percentage
def simulate(n):
    num_correct_gut = 0
    num_correct_switch = 0
    for i in range(n):
        #3 doors
        #doors[0] = 1st door, doors[1] = 2nd door, doors[2] = 3rd door
        doors = generateDoors()
        #get door guess
        gut_guess = generateGuess()
        #get new doors after host 'removes' a goat door (not the one the user guessed if they guessed one)
        newDoors = getNewDoors(doors,gut_guess)
        switch_guess = generateNewGuess(newDoors,gut_guess)
        #if guess is correct, add to sum
        if newDoors[gut_guess] == 1:
            num_correct_gut += 1
        elif newDoors[switch_guess] == 1:
            num_correct_switch += 1

    guess_percentage_gut = (num_correct_gut / n) * 100
    guess_percentage_switch = (num_correct_switch / n) * 100

    return [round(guess_percentage_gut,2),round(guess_percentage_switch,2)] #round percents to 2 decimals
    