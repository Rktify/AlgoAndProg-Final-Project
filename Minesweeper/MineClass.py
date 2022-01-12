import pygame
import os
from random import random

class Game:
    def __init__(self, SSize, board): #Initializer
        self.board = board
        self.SSize = SSize
        self.gridsize = self.SSize[0] // self.board.getSize()[1], self.SSize[1] // self.board.getSize()[0] #Getting the size of the ratio of blocks and screensize
        self.Limg()

    def game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.SSize)
        pygame.display.set_caption("Classic Minesweeper") #just a caption (Top left window name)
        run = True
        while run: #basically while game is running
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    run = False
                if (event.type == pygame.MOUSEBUTTONDOWN): #Click
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.Click(position, rightClick)
            self.grid()
            pygame.display.flip()
            if self.board.getWon(): #Win state
                print("You won! =D")
                run = False #Closes game
            elif self.board.getLose(): #Lose state
                print("You Lost :(")
                run = False
        pygame.quit()

    def grid(self): #Draw the board
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col)) #Getting the peice
                image = self.getImg(piece)#Get image based on piece
                self.screen.blit(image, topLeft) #Placing images in the correct places
                topLeft = topLeft[0] + self.gridsize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.gridsize[1]

    def Limg(self): #Load Images
        self.imgs = {}
        for fileName in os.listdir("Minesweeper/images"):
            img = pygame.image.load(f"Minesweeper/images/{fileName}")
            img = pygame.transform.scale(img, self.gridsize) #Scales the image
            self.imgs[fileName.split(".")[0]] = img #removes the png


    def getImg(self, piece): #Change the images based on actions
        string = None
        if piece.getOpened():
            if piece.getBomb():
                string = "bombclicked" #If you click on a bomb
            else:
                string = str(piece.getNumAround()) #If you click on a number, it will get the images based on the number
        else:
            if piece.getFlagged():
                string = "flag" #This is for the flagged status
            else:
                string = "empty"
        # if piece.getBomb():
        #     string = "bomb"
        # else:
        #     string = str(piece.getNumAround())
        return self.imgs[string]

    def Click(self, position, rightClick):
        coords = position[1] // self.gridsize[1], position[0] // self.gridsize[0] #Getting the coordinate for the blocks
        piece = self.board.getPiece(coords) #Gets the piece based on the position (coordinates, in pygame top left is (0, 0))
        self.board.Click(piece, rightClick)



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
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                Bomb = random() < self.prob #Bombs
                if not Bomb:
                    self.numNotBombs += 1 #Every block that isnt a bomb, numNotBombs + 1
                piece = Pieces(Bomb) #pushes the bomb to piece
                row.append(piece)
            self.board.append(row)
        self.setNumbers()

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
                outOfBounds = row < 0 or col < 0 or row >= self.size[0]  or col >= self.size[1]
                if outOfBounds:
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
        piece.click()
        if piece.getBomb():
            self.lose = True #if block has bomb we lose
            return
        self.numOpened += 1
        if piece.getNumAround() != 0: #Checks if a neighboring block is a 0 or not, to continue to the function below
            return
        for i in piece.getNumbers(): #If the block is 0 , itll keep opening until it reaches a block that isnt a bomb or an opened block
            if not i.getBomb() and not i.getOpened():
                self.Click(i, False)

class Pieces:
    def __init__(self, Bomb): #Initializer
        self.Bomb = Bomb
        self.opened = False
        self.flagged = False

    def getBomb(self): #Self explanatory get funcs
        return self.Bomb

    def getOpened(self):
        return self.opened

    def getFlagged(self):
        return self.flagged

    def getNumbers(self):
        return self.numbers

    def getNumAround(self):
        return self.numAround

    def toggleFlag(self): #toggleing the rightClick flag
        self.flagged = not self.flagged

    def click(self): #Handle click
        self.opened = True

    def setNumbers(self, numbers):
        self.numbers = numbers
        self.setNumAround()

    def setNumAround(self): #setting the number according the amount of bombs it has around it
        self.numAround = 0
        for i in self.numbers:
            if i.getBomb():
                self.numAround += 1 #If it has a bomb, the number will rise to the amount of bombs it has around it
