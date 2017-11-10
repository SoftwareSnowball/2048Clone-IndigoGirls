'''
    Created on September 20, 2017

    @Author: James Malloy

    Purpose of File:
        To implement the initalizeGame function

'''

# InitializeGame takes the messageDictionary from dispatch and uses the
# information to create a dictionary containing the initial game state.
#
# In the messageDictionary, the function specificaly checks for a user
# specified rowCount and columnCount. Both of these values are unverified.
#
#
# See initializeGameTest.py for comments related to the allowed inputs


import random
from IndigoGirls.placeTile import placeTile

def initializeGame(messageDictionary):

    #------------------------------------------
    #           HELPER FUNCTIONS
    # -----------------------------------------

    #Function is used to simplify the validity check for both rowCount and columnCount
    #TODO: refactor this out of this function
    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False

    #function used to generate the random values for the initial pieces
    def makeInitialPiece():
        value = random.randint(0,3)
        if (value == 3):
            return 2
        else:
            return 1

    # -----------------------------------------
    #       VALIDITY CHECK FOR INPUTS
    # -----------------------------------------

    # -----------------------------------------
    # Variables used in function that are needed during Validity check
    columnCount = 4
    rowCount = 4
    errorMessage = ''
    functionErrorFlag = False
    gameMessage = {}

    #TODO: rework this part to use areDimensionsValid and rework testcode to allow more general error responses
    # -----------------------------------------
    # Check columnCount validity
    if ('columnCount' in messageDictionary):
        columnCount = messageDictionary['columnCount']

        if isNotValidNumber(columnCount):
            functionErrorFlag = True
            errorMessage = errorMessage + 'columnCount is not a valid number. '

    # -----------------------------------------
    # Check the rowCount validity
    if ('rowCount' in messageDictionary):
        rowCount = messageDictionary['rowCount']

        if isNotValidNumber(rowCount):
            functionErrorFlag = True
            errorMessage = errorMessage + 'rowCount is not a valid number. '

    # -----------------------------------------
    # Function return if functionErrorFlag is set
    if (functionErrorFlag):
        errorMessage = "error:  " + errorMessage
        gameMessage['gameStatus'] = errorMessage
        return gameMessage




    # -----------------------------------------
    #         GAME INITIALIZATION CODE
    # -----------------------------------------

    # -----------------------------------------
    #remaining variables used for game initialization
    gridSize = columnCount * rowCount
    grid = [0] * (gridSize) #Python, your syntax is so weird
#    piecePlacement = [0,0]
#
#
#    # -----------------------------------------
#    # Determine where initial game pieces will go
#
#    piecePlacement[0] = random.randint(0, gridSize - 1)
#    piecePlacement[1] = random.randint(0, gridSize - 1)
#
#    # Account for possibility that both pieces could be placed on the same tile
#    while (piecePlacement[1] == piecePlacement[0]):
#        piecePlacement[1] = random.randint(0, gridSize - 1)
#
#
#    # -----------------------------------------
#    # Sets the pieces on the board with their initial values
#    grid[piecePlacement[0]] = makeInitialPiece()
#    grid[piecePlacement[1]] = makeInitialPiece()

    placeTile(grid)
    placeTile(grid)



    # -----------------------------------------
    # Prepare gameMessage with outgoing game data
    gameMessage['score'] = 0
    gameMessage['board'] = {'columnCount': columnCount, 'rowCount' : rowCount, 'grid' : grid }
    gameMessage['gameStatus'] = 'underway'



    return gameMessage;