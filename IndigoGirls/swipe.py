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

    elementLines.append(ElementLine(board, direction, 0))
    elementLines.append(ElementLine(board, direction, 1))

    elementLine = elementLines[0]
    elementLine.setElement(0, 0)
    elementLine.setElement(1, 1)

    answer = {"board": board}

    return answer
