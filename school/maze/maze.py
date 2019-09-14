# maze.py
# Nathan Branson and Thao Truong

from random import *

def readMaze():
    filename = input("What is the name of the file with your maze? ")
    f = open(filename)
    s = f.read()
    f.close()

    maze = []

    for line in s.split("\n"):
        if (len(line) > 0) and line[0] == "X":
            maze.append([])

        for c in line:
            maze[-1].append(c)

    return maze, filename
    

def readRules(filename):
    f = open(filename)
    s = f.read()
    f.close()

    rules = {}

    for line in s.split("\n"):
        if (len(line) > 0) and (not line[0] in "X "):
            line = line.replace(" ", "")
            m = line.split(":")
            k = m[0]
            rules[k] = []

            for i in m[1].split(","):
                rules[k].append(i)

    return rules

def gameOverFunc(rules, inventory):
    gameOver = False

    for i in range(len(inventory)):
        if inventory[i] == "C":
            gameOver = True
        
    return gameOver

def playerPosi(maze):
    posis = "X"
    posir = 0
    posic = 0

    r = randrange(0, len(maze))
    c = randrange(0, len(maze))

    posis = maze[r][c]

    while posis == "X":
        r = randrange(0, len(maze))
        c = randrange(0, len(maze))
        posis = maze[r][c]
        posir = r
        posic = c

    return posir, posic

def inputs(posr, posc, maze, inventory, rules):
        inputs = input("What would you like to do? (MOVE (m), LOOK (l), TAKE (t), INVENTORY (i)) ")
        inputs = inputs.lower()
        
        if inputs == "m":
            posr, posc = move(posr, posc, maze)
        if inputs == "l":
            look(posr, posc, maze)
        if inputs == "t":
            inventory = take(posr, posc, maze, inventory, rules)
        if inputs == "i":
            print("Inventory: ")
            for i in inventory:
                print(i)

        return posr, posc, inventory



def move(posr, posc, maze):
    posS = maze[posr][posc]
    move = input("How would you like to move? (UP (u), DOWN (d), LEFT (l), RIGHT(r)) ")
    move = move.lower()

    if move == "u":
        posr = posr - 1  # has to move negative because up is negative in the maze
    if move == "d":
        posr = posr + 1
    if move == "r":
        posc = posc + 1
    if move == "l":
        posc = posc - 1

    posS = maze[posr][posc]
    print(posr, posc)

    if posS == "X":
        print("You can't move there.")
        
        if move == "u":
            posr = posr + 1
        if move == "d":
            posr = posr - 1
        if move == "r":
            posc = posc - 1
        if move == "l":
            posc = posc + 1
        print(posr, posc)

    return posr, posc
        

def look(posr, posc, maze):
    posS = maze[posr][posc]
    
    if posS == " ":
        print("There is nothing here.")
    elif posS == "A":
        print("There is an A.")
    elif posS == "B":
        print("There is an B.")
    elif posS == "C":
        print("There is an C.")


def take(posr, posc, maze, inventory, rules):

    posS = maze[posr][posc]

    if posS == "A":
        inventory.append("A")
        maze[posr][posc] = " "
    elif posS == "B":
        inventory.append("B")
        maze[posr][posc] = " "

    if posS == "C":
        if "C" in rules:
            for item in rules["C"]:
                if not (item in inventory):
                    print("You can't pick the 'C' up yet. You need an 'A' and a 'B'!")
                else:
                    inventory.append("C")
                    maze[posr][posc] = " "
                    print("You won!")
                    break
    else:
        print("There is nothing here.")


    return inventory


def main():
    maze, filename = readMaze()
    rules = readRules(filename)
    posr, posc = playerPosi(maze) # makes player's initial position

    inventory = []

    gameOver = False

    while gameOver == False:
        posr, posc, inventory = inputs(posr, posc, maze, inventory, rules)
        gameOver = gameOverFunc(rules, inventory)
  
    


if __name__ == "__main__":
    main()
