from MineClass import *

size = (10, 10) #The size of the board, i usually play 20x20
prob = 0.99 #The probability of there being a bomb, in this case it is 99% out of 100 blocks, therefore only 1 block isnt a bomb (fun guessing game =D)
board = Board(size, prob) #To set up the board
SSize = (1000, 900) #The screen size
mine = Game(SSize , board)
mine.game() #The main run function