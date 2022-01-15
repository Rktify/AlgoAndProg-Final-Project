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

    def toggleFlag(self): #toggling the rightClick flag
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
