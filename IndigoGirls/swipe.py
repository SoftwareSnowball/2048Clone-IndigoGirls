'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Holds swipe function which performs the swipe task in the game

'''

from IndigoGirls.ElementLine import ElementLine


def swipe(input):

    #Function is used to simplify the validity check for both rowCount and columnCount
    #This function is also declared in initializeGame.
    #TODO: refactor this into its own file
    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False

    #Moves all tiles as far as it can without merging
    #returns true if a tile was moved. False otherwise
    def sweep(elementLine):

        lastEmpty = -1
        index = elementLine.getLength() - 1

        #find last empty index
        while (index >= 0 and lastEmpty == -1) :
            if (elementLine.getElement(index) == 0 ):
                lastEmpty = index

            index -= 1

        #List is full and nothing can be swept
        if (lastEmpty == -1):
            return False

        didWeMovedSomething = False
        index = lastEmpty

        while (index >= 0 ):

            if (elementLine.getElement(index) != 0 ):
                elementLine.swap(index, lastEmpty)
                lastEmpty -= 1
                didWeMovedSomething = True

            index -= 1

        return didWeMovedSomething



    board = input["board"]
    direction = input["direction"]

    errorMessage = "Error: "
    error = False

    if (type(direction) is not str):
        errorMessage += "Direction must be string. "
        error = True

    if (direction is not "up" and direction is not "down" and direction is not "left" and direction is not "right"):
        errorMessage += "Direction not recognized. "
        error = True

    if (isNotValidNumber(board["rowCount"])):
        errorMessage += "rowCount is invalid. "
        error = True

    if (isNotValidNumber((board["columnCount"]))):
        errorMessage += "columnCount is invalid. "
        error = True

    if (error):
        return {"gameStatus": errorMessage}

    # I don't want this code to run if rowCount or columnCount is not valid because it could cause an exception
    if (len(board["grid"]) != board["rowCount"] * board["columnCount"]):
        errorMessage += "Grid size is invalid. "
        return {"gameStatus": errorMessage}

    # At this point everything should be valid.


    elementLines = []

    index = 0
    numberOfLines = board["rowCount"]
    while (index < numberOfLines):
        elementLines.append(ElementLine(board, direction, index))
        index += 1

    for elementLine in elementLines:
        sweep(elementLine)

    answer = {"board": board}

    return answer
