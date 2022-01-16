import time
import os
from MineClass import *
from BoardClass import *

print("Welcome to the classic minesweeper game!")
time.sleep(2)
print("Are you new to minesweeper? (y/n)")
tutor = input("")
if tutor.lower() == "yes" or tutor.lower() == "y":
    print("The objective of the game is to clear a rectangular board that contains hidden bomb without detonating them!")
    time.sleep(2)
    print("As long as you dont hit the bombs, numbers or empty blocks will appear!")
    time.sleep(2)
    print("Use those numbers to help you through this puzzle game!")
    time.sleep(2)
    print("The numbers represents the number of mines or bombs that are on the neighboring blocks!")
    time.sleep(2)
    print("Good Luck and Have Fun!")
    time.sleep(2)
elif tutor.lower() == "no" or tutor.lower() =="n":
    pass
#This is just a tutorial of the game =D
#To make sure everyone can play the game :)

print()
print("Make sure that you make a square, width and height has to be the same!")
time.sleep(2)
h = int(input("How many blocks (height) do you want to have in the board? (min. 5, max. 30): ")) #height of board
while h < 5 or h > 30:
    h = int(input("How many blocks (height) do you want to have in the board? (min. 5, max. 30): "))

w = int(input("How many blocks (width) do you want to have in the board? (min. 5, max. 30): ")) #width of baord
while w < 5 or h > 30:
    w = int(input("How many blocks (width) do you want to have in the board? (min. 5, max. 30): "))

while w != h:
    os.system("cls")
    print("Make sure that you make a square, width and height has to be the same!")
    time.sleep(2)
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
