from MineClass import *
from BoardClass import *

h = int(input("How many blocks (height) do you want to have in the board? (min. 5, max. 30): ")) #height of board
while h < 5 or h > 30:
    h = int(input("How many blocks (height) do you want to have in the board? (min. 5, max. 30): "))

w = int(input("How many blocks (width) do you want to have in the board? (min. 5, max. 30): ")) #width of baord
while w < 5 or h > 30:
    w = int(input("How many blocks (width) do you want to have in the board? (min. 5, max. 30): "))

size = (h, w) #The size of the board, i usually play 20x20

prob = float(input("Whats the bomb probability u want to have? (in decimal, (i.e. 0.1 is 10%)) (min 0.1, max 0.9): ")) #The probability of there being a bomb
while prob < 0.1 or prob > 0.9:
    prob = float(input("Whats the bomb probability u want to have? (in decimal, (i.e. 0.1 is 10%)) (min 0.1, max 0.9): "))

board = Board(size, prob) #To set up the board
SSize = (1000, 1000) #The screen size
mine = Game(SSize , board)
mine.game() #The main run function
