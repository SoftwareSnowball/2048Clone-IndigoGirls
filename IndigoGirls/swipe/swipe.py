'''
    Created  on October 19, 2017
    Modified on November 9, 2017

    @Author: James Malloy

    Purpose of File:
        Holds swipe function. This is the public interface called from dispatch which allows
        the swipe operation to be performed

'''

from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe
from IndigoGirls.utils.isBoardValid import isBoardValid
from IndigoGirls.utils.placeTile import placeTile


#TODO refactor validation tests from deterministicSwipe into swipe

def swipe(input):

    #-----------------------------------------------------#
    #HELPER FUNCTIONS

    #Function checks for invalid inputs and returns a dictionary with keys "isError" and "errorMessage"
    def isInputValid(input):

        resultPackage = {}
        errorMessage = "error: "
        resultPackage["errorMessage"] = errorMessage
        resultPackage["isError"] = False

        #Check that everything is in the dictionary

        if ("direction" not in input):
            resultPackage["isError"] = True
            errorMessage += "direction not given. "

        if ("board" not in input):
            resultPackage["isError"] = True
            errorMessage += "board not in dictionary. "

        if (resultPackage["isError"]):
            return resultPackage




        #check that everything within the dictionary is valid

        direction = input["direction"]

        if (type(direction) is unicode):
            direction = direction.encode('ascii', 'ignore')


        if (type(direction) is not str):
            errorMessage += "Direction must be string. "
            resultPackage["isError"] = True
            return resultPackage


        direction = direction.lower()
        input["direction"] = direction


        if (direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right'):
            errorMessage += "Direction not recognized. "
            resultPackage["isError"] = True


        board = input["board"]

        boardValidity = isBoardValid(board)

        if (boardValidity["isInvalid"]):
            resultPackage["isError"] = True
            errorMessage += resultPackage["errorMessage"]


        return resultPackage

    #END HELPER FUNCTIONS
    #-----------------------------------------------------#

    validationResults = isInputValid(input)
    if (validationResults["isError"] == True):
        return {"gameStatus": validationResults["errorMessage"]}

    results = deterministicSwipe(input)
    if ("error" in results["gameStatus"]):
        return results


    operationSuccess  = placeTile(input["board"]["grid"])
    if (operationSuccess == False):
        return {"gameStatus": "error A new tile could not be placed after swiping."}

    return results