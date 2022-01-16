import pygame
import os
import time
from PiecesClass import *
from BoardClass import *

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
                if (event.type == pygame.QUIT): #Quitting the gmae
                    run = False
                if (event.type == pygame.MOUSEBUTTONDOWN): #Click
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2] #Index 2 is for right click
                    self.Click(position, rightClick)
            self.grid()
            pygame.display.flip()
            if self.board.getWon(): #Win state
                print("You won! =D")
                vic = pygame.mixer.Sound("victory.wav") #Plays a sound of 8bit victory =D
                vic.set_volume(0.01)
                vic.play()
                time.sleep(3)
                run = False #Closes game
            elif self.board.getLose(): #Lose state
                boom = pygame.mixer.Sound("explosion.wav") #Plays a sound of 8bit explosion =D
                boom.set_volume(0.01) #I set it so low cause it jumpscared me when i tested it T_T
                boom.play()
                print("You Lost :(")
                time.sleep(4)
                run = False #Stops loop
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
        for fileName in os.listdir("images"):
            img = pygame.image.load(f"images/{fileName}")
            img = pygame.transform.scale(img, self.gridsize) #Scales the image
            self.imgs[fileName.split(".")[0]] = img #removes the png

    def getImg(self, piece): #Change the images based on actions
        string = ""
        if piece.getOpened():
            if piece.getBomb():
                string = "bombclicked" #If you click on a bomb
            else:
                string = str(piece.getNumAround()) #If you click on a number, it will get the images based on the number
        else:
            if piece.getFlagged():
                string = "flag" #This is for the flagged status
            else:
                string = "covered" #If its not opened, and not flagged, then yea its empty =D
        if self.board.getLose():
            if piece.getBomb():#If user lose, it will reveal all the bombs
                if not piece.getOpened():
                    string = "bomb"
                else:
                    string = "bombclicked"
        if self.board.getWon():
            if piece.getBomb(): #If user wins, it will auto flag the blocks that has not been flagged yet.
                if not piece.getOpened():
                    string = "flag"
                else:
                    string = "covered"
        return self.imgs[string] #Returns the image so it can be placed to each block

    def Click(self, position, rightClick):
        coords = position[1] // self.gridsize[1], position[0] // self.gridsize[0] #Getting the coordinate for the blocks
        piece = self.board.getPiece(coords) #Gets the piece based on the position (coordinates, in pygame top left is (0, 0))
        self.board.Click(piece, rightClick)
