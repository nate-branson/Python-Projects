# basketballSim.py
# Nathan Branson


from random import random

def printIntro():

    print("This program simulates a pickup basketball game.")
    print("The game is to 21, win by 2.")
    print("2 pointers count as 1s and 3 pointers count as 2s.")
    print("You will give inputs of the team's name and the probabilities of each team scoring a 1, a 2, and getting the rebound.")
    print("Good luck to both teams!")
    print()

def getInputs():
    print("The first team gets the ball first.")
    teamA = input("What is the first team's name? ")
    teamB = input("What is the second team's name? ")

    teamA = teamA.capitalize()
    teamB = teamB.capitalize()

    print()

    probAS = float(input("What is the probablilty of the " + teamA + " shooting a 1 pointer? (i.e .7) "))
    probBS = float(input("What is the probablilty of the " + teamB + " shooting a 1 pointer? (i.e .7) "))

    print()


    probA1 = float(input("What is the probablilty of the " + teamA + " scoring a 1 pointer? (i.e .5) "))
    probB1 = float(input("What is the probablilty of the " + teamB + " scoring a 1 pointer? (i.e .5) "))

    print()

    probA2 = float(input("What is the probablilty of the " + teamA + " scoring a 2 pointer? (i.e .2) "))
    probB2 = float(input("What is the probablilty of the " + teamB + " scoring a 2 pointer? (i.e .2) "))

    print()

    probAR = float(input("What is the probablilty of the " + teamA + " to get the OFFENSIVE rebound? (i.e .2) "))
    probBR = float(input("What is the probablilty of the " + teamB + " to get the OFFENSIVE rebound? (i.e .2) "))

    return teamA, teamB, probA1, probB1, probA2, probB2, probAR, probBR, probAS, probBS


def gameOver(scoreA, scoreB):
    gameOver = False
    if scoreA >= 21 and scoreA - 1 > scoreB or scoreB >= 21 and scoreB - 1 > scoreA:
        gameOver = True

    return gameOver


def simGame(teamA, teamB, probA1, probB1, probA2, probB2, probAR, probBR, probAS, probBS):
    ball = "A"
    scoreA = 0
    scoreB = 0

    while not gameOver(scoreA, scoreB):
   
        if ball == "A":
            if random() < probAS: #team shoots a 1
                if random() < probA1: #team A scores a 1
                    scoreA = scoreA + 1
                elif random() < probAR: # team A gets rebound
                    ball = "A"
                else:
                    ball = "B"
            else:
                if random() < probA2: #team A scores a 2
                    scoreA = scoreA + 2
                elif random() < probAR: # team A gets rebound
                    ball = "A"
                else:
                    ball = "B"
        else:
            if random() < probBS: #team shoots a 1
                if random() < probB1: #team A scores a 1
                    scoreB = scoreB + 1
                elif random() < probBR: # team A gets rebound
                    ball = "B"
                else:
                    ball = "A"
            else:
                if random() < probB2: #team A scores a 2
                    scoreB = scoreB + 2
                elif random() < probBR: # team A gets rebound
                    ball = "B"
                else:
                    ball = "A"

        print((str(scoreA) + " : " + str(scoreB)).center(30))
        

    return scoreA, scoreB


def main():
    printIntro()
    teamA, teamB, probA1, probB1, probA2, probB2, probAR, probBR, probAS, probBS = getInputs()

    print()
    print((teamA + " vs. " + teamB).center(30))
    print("-" * 30)

    scoreA, scoreB = simGame(teamA, teamB, probA1, probB1, probA2, probB2, probAR, probBR, probAS, probBS)

    print()
    if scoreA > scoreB:
        print(("The " + teamA + " won " + str(scoreA) + " to " + str(scoreB)).center(30))
    else:
        print(("The " + teamB + " won " + str(scoreB) + " to " + str(scoreA)).center(30)) 
    

    play = input("Would you like to play again? (Y/N) ")
    if play == "Y":
        main()


main()

