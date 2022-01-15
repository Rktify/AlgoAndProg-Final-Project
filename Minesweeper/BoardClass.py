from random import random
from PiecesClass import *

class Board: #This is the Board class, mostly for stuff around the board
    def __init__(self, size, prob): #THis is the Initializer of the code
        self.size = size #The size of the game (blocks)
        self.prob = prob #The probability of the block being a bomb
        self.lose = False #Lose obviously false in the beginning or else already GG we lose =D
        self.numOpened = 0 #The number of opened Blocks
        self.setBoard()


    def setBoard(self): #Setting up the board
        self.numNotBombs = 0 #The number of blocks that does not have a bomb in them
        self.board = []
        for row in range(self.size[0]): #Row is size index 0
            row = []
            for col in range(self.size[1]): #column is size index 1
                Bomb = random() < self.prob #Bombs
                if not Bomb:
                    self.numNotBombs += 1 #Every block that isnt a bomb, numNotBombs + 1
                piece = Pieces(Bomb) #pushes the bomb to piece
                row.append(piece) #appends the piece for each block
            self.board.append(row) #appends an entire row to the board
        self.setNumbers() #then it will set the numbers based on the piece

    def setNumbers(self): #setting the numbers
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col)) #getting the pieces for each coods
                numbers = self.getNumList((row, col)) #getting the numbers for each coods
                piece.setNumbers(numbers) #Setting each piece's numbers based on the list of numbers that it got from getNumList

    def getNumList(self, coords): #Getting the numbers for the adjacent blocks
        numbers = []
        for row in range(coords[0] - 1, coords[0] + 2):
            for col in range(coords[1] - 1, coords[1] + 2):
                if row < 0 or col < 0 or row >= self.size[0]  or col >= self.size[1]:
                    continue
                numbers.append(self.getPiece((row, col)))
        return numbers

    def getSize(self): #Self explanatory get funcs
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def getLose(self):
        return self.lose

    def getWon(self):
        return  self.numNotBombs == self.numOpened #If the number of blocks that doesnt have a bomb in them = the number of blocks that are opened, we win

    def Click(self, piece, flag):
        if piece.getOpened() or (not flag and piece.getFlagged()): #If the piece is opened and not flagged, we cna click
            return
        elif flag:
            piece.toggleFlag() #if we right clicked we flag the block
            return
        piece.click() #opens the block
        if piece.getBomb():
            self.lose = True #if block has bomb we lose
            return
        self.numOpened += 1
        if piece.getNumAround() != 0: #Checks if a neighboring block is a 0 or not, to continue to the function below
            return
        for i in piece.getNumbers(): #If the block is 0 , itll keep opening until it reaches a block that isnt a bomb or an opened block
            if not i.getBomb() and not i.getOpened():
                self.Click(i, False)
