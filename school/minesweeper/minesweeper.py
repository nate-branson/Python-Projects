# minesweeper.py
# by Nathan Branson and Bailey Rhodes 

# graphics.py is needed in the same folder to run this program

from graphics import *
from random import *

def sizeWindow():

    w = GraphWin("Minesweeper", 400, 150)
    w.setCoords(-4, -2, 4, 2)
    w.setBackground("white")
    instructions = Text(Point(0, 0.6), "Pick a grid size")
    instructions.draw(w)

    ten = Rectangle(Point(-2, -0.75), Point(-0.5, 0))
    ten.setFill("silver")
    ten.draw(w)
    t = Text(Point(-1.25, -0.45), "10 x 10")
    t.draw(w)
    
    twenty = Rectangle(Point(0.5, 0), Point(2, -0.75))
    twenty.setFill("silver")
    tw = Text(Point(1.25, -0.45), "20 x 20")
    twenty.draw(w)
    tw.draw(w)


    click = w.getMouse()
    x = click.getX()
    y = click.getY()

    close = False

    while close == False:
        
        if (-2 <= x <= -0.5) and (-0.75 <= y <= 0):
            r = 10
            w.close()
            close = True
        
        if (0.5 <= x <= 2) and (-0.75 <= y <= 0):
            r = 20
            w.close()
            close = True
    
    return r

def rectOut(i, n):
    global w
    ll = Point(i, n)
    ul = Point(i + 1, n + 1)
    
    r = Rectangle(ll, ul)
    r.setOutline("black")
    r.draw(w)


def rectFillG(i, n):
    global w
    ll = Point(i, n)
    ul = Point(i + 1, n + 1)
    
    r = Rectangle(ll, ul)
    r.setFill("grey")
    r.draw(w)


def rectFillW(i, n):
    global w
    ll = Point(i, n)
    ul = Point(i + 1, n + 1)
    
    r = Rectangle(ll, ul)
    r.setFill("white")
    r.draw(w)

def rectFillB(i, n):
    global w
    ll = Point(i, n)
    ul = Point(i + 1, n + 1)
    
    r = Rectangle(ll, ul)
    r.setFill("blue")
    r.draw(w)


def mines(r):
    global w

    listC = []
    listD = []

    b = r ** 2

    num = randrange(0.04 * b, 0.2 * b)
    
    for i in range(num):
        t = randrange(0, r)
        n = randrange(0, r)
        ll = Point(t + .5, n + .5)

        c = Circle(ll, .5)
        c.draw(w)
        c.setFill("red")
        listC.append(t)
        listD.append(n)

    return listC, listD, num



def gameOverFunc(listC, listD, x, y, r, numNotMine):
    global w
    gameOver = False

    for l in range(len(listC)):
        if int(x) == listC[l] and int(y) == listD[l]:
            gameOver = True
            lostFunc(r, listC, listD)
            
    if numNotMine == 0:
        gameOver = True
        winFunc(r, listC, listD)
        
    return gameOver

def winFunc(r, listC, listD):
    
    for i in range(0, r):
        for n in range(0, r):
            for l in range(len(listC)):
                if i == listC[l] and n == listD[l]:
                    c = Circle(Point(listC[l] + .5, listD[l] + .5), .5)
                    c.draw(w)
                    c.setFill("red")

    t = Text(Point(r / 2, r / 2), "You won!")
    t.setStyle("bold")
    t.setSize(30)
    t.draw(w)
    w.getMouse()
    w.close()



def lostFunc(r, listC, listD):

    for i in range(0, r):
        for n in range(0, r):
            for l in range(len(listC)):
                if i == listC[l] and n == listD[l]:
                    c = Circle(Point(listC[l] + .5, listD[l] + .5), .5)
                    c.draw(w)
                    c.setFill("red")

    t = Text(Point(r / 2, r / 2), "You lost.")
    t.setStyle("bold")
    t.setSize(30)
    t.draw(w)
    w.getMouse()
    w.close()

    

def clickFunc():
    click = w.getMouse()

    x = click.getX()
    y = click.getY()

    return x, y



def click(listC, listD, r, num):

    gameOver = False

    numNotMine = r * r - num

    listx = []
    listy = []

    x, y = clickFunc()
    listx.append(int(x))
    listy.append(int(y))

    while gameOver == False:
     
        x, y = clickFunc()
        if int(x) in listx and int(y) in listy:
            if listx.index(int(x)) == listy.index(int(y)) and int(x) == listx[listx.index(int(x))] and int(y) == listy[listy.index(int(y))]:
                numNotMine = numNotMine
            else:
                numNotMine = numNotMine - 1
        else:
            numNotMine = numNotMine - 1

        for i in range(0, r):
            for n in range(0, r):
                if int(x) == i and int(y) == n:
                    rectFillW(i, n)
                    rectOut(i, n)
                    notMine(listC, listD, x, y, i, n)
                    for l in range(len(listC)):
                        if int(x) == listC[l] and int(y) == listD[l]:
                            c = Circle(Point(listC[l] + .5, listD[l] + .5), .5)
                            c.draw(w)
                            c.setFill("red")

        gameOver = gameOverFunc(listC, listD, x, y, r, numNotMine)
          
    return x, y, num


def notMine(listC, listD, x, y, i, n):
    
    for e in range(len(listC)):
        if int(x) != listC[e] and int(y) != listD[e]:
            for l in range(len(listC)):
                if int(x) == listC[l] - 1 and int(y) == listD[l] or int(x) == listC[l] + 1 and int(y) == listD[l] or int(x) == listC[l] and int(y) == listD[l] + 1 or int(x) == listC[l] and int(y) == listD[l] - 1:
                    rectFillB(i, n)


def main():
    global w
    global m

    r = sizeWindow()
    
    w = GraphWin("Minesweeper", 30 * r, 30 * r)
    w.setBackground("white")
    w.setCoords(0, 0, r, r)

    listC, listD, num = mines(r)

    for i in range(0, r):
        for n in range(0, r):
            rectFillG(i, n)
            rectOut(i, n)

    
    click(listC, listD, r, num)
        
    

if __name__ == "__main__":
    main()
