'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Holds swipe function. This is the public interface called from dispatch which allows
        the swipe operation to be performed

'''

from IndigoGirls.deterministicSwipe import deterministicSwipe
from IndigoGirls.placeTile import placeTile

#TODO refactor validation tests from deterministicSwipe into swipe

def swipe(input):

    #-----------------------------------------------------#
    #HELPER FUNCTIONS

    #Function is used to simplify the validity check for both rowCount and columnCount
    #This function is also declared in initializeGame.
    #TODO: refactor this into its during OO rework
    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False

    #Function checks for invalid inputs and returns a dictionary with keys "isError" and "errorMessage"
    def isInputValid(input):
        errorMessage = "error: "
        error = False
        direction = input["direction"]
        board = input["board"]

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

        # I don't want this code to run if rowCount or columnCount is not valid because it could cause an exception
        if ((error == False) and (len(board["grid"]) != board["rowCount"] * board["columnCount"])):
            errorMessage += "Grid size is invalid. "
            error = True


        return {"errorMessage": errorMessage, "isError": error}

    #END HELPER FUNCTIONS
    #-----------------------------------------------------#

    validationResults = isInputValid(input)
    if (validationResults["isError"] == True):
        return {"gameStatus": validationResults["errorMessage"]}

    results = deterministicSwipe(input)
    if ("error" in results["gameStatus"]):
        return results


    operationSuccess  = placeTile(input["board"])
    if (operationSuccess == False):
        return {"gameStatus": "error A new tile could not be placed after swiping."}

    return results