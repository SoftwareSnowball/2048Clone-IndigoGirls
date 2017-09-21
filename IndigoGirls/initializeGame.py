'''
    Created on September 20, 2017

    @Author: James Malloy

    Purpose of File:
        To implement the initalizeGame function

    todo: finish description

'''

import random


def initializeGame(messageDictionary):


    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False


    columnCount = 4
    rowCount = 4
    errorMessage = ''
    functionError = False


    if ('columnCount' in messageDictionary):
        columnCount = messageDictionary['columnCount']

        if isNotValidNumber(columnCount):
            functionError = True
            errorMessage = errorMessage + 'columnCount is not a valid number. '

    if ('rowCount' in messageDictionary):
        rowCount = messageDictionary['rowCount']

        if isNotValidNumber(rowCount):
            functionError = True
            errorMessage = errorMessage + 'rowCount is not a valid number. '



    gameMessage = {}


    #This is where the function should end if the input is invalid
    if (functionError):
        errorMessage = "error:  " + errorMessage
        gameMessage['gameStatus'] = errorMessage
        return gameMessage

    #Remaining code sets the board and returns all the data associated with a
    #properly initialized game.


    gridSize = columnCount * rowCount
    grid = [0] * (gridSize) #Python, your syntax is so weird


    piecePlacement = [0,0]



    piecePlacement[0] = random.randint(0, gridSize - 1)
    piecePlacement[1] = random.randint(0, gridSize - 1)


    #Account for possibility that both pieces could be placed on same tile
    while (piecePlacement[1] == piecePlacement[0]):
        piecePlacement[1] = random.randint(0, gridSize - 1)


    #function to generate the random values for the initial pieces
    def makeInitialPiece():
        value = random.randint(0,3)
        if (value == 3):
            return 2
        else:
            return 1

    #Sets the pieces on the board with their initial values
    grid[piecePlacement[0]] = makeInitialPiece()
    grid[piecePlacement[1]] = makeInitialPiece()


    gameMessage['score'] = 0
    gameMessage['board'] = {'columnCount': columnCount, 'rowCount' : rowCount, 'grid' : grid }
    gameMessage['gameStatus'] = 'underway'

    return gameMessage;