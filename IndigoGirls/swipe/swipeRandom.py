'''
    Created  on November 15, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the swipe random function related to the recommend function

'''

from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe
from IndigoGirls.utils.placeTile import placeTile
from IndigoGirls.utils.copyBoard import copyBoard
import random

def swipeRandom(board):

    directions = ["up", "down", "left", "right"]
    generatedInput = {}
    validResults = []


    for direction in directions:
        boardCopy = copyBoard(board)
        generatedInput["board"] = boardCopy
        generatedInput["direction"] = direction

        swipeResult = deterministicSwipe(generatedInput)

        if ("error" not in swipeResult["gameStatus"]):
            validResults.append(swipeResult)

    numberValidResults = len(validResults)

    if (numberValidResults == 0):
        return {'gameStatus':"error: Cannot swipe in any direction"}


    #pickIndex = random.randint(1, numberValidResults) - 1
    result = random.choice(validResults)

    operationSuccess = placeTile(result["board"]["grid"])

    if (not operationSuccess):
        raise RuntimeError("There was no empty space to put a new tile. This exception should never occur.")


    return result




