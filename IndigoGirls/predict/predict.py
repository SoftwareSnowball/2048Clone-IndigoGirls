'''
    Created  on December 10, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the public interface for the predict functionality in IndigoGirls

'''

from IndigoGirls.utils.isBoardValid import isBoardValid
from IndigoGirls.predict.isMovesValid import isMovesValid
from IndigoGirls.utils.isDirectionValid import isDirectionValid
from IndigoGirls.recommend.searchSwipePaths import searchSwipePaths

import signal
import multiprocessing
import time

def predict(input):


    #Check that board is valid
    if "board" not in input:
        return {"gameStatus": "error: missing board"}

    board = input["board"]
    boardValidity = isBoardValid(board)

    if boardValidity["isInvalid"]:
        return {"gameStatus": "error: " + boardValidity["errorMessage"] }

    #Check that moves is valid
    moves = 1
    if "moves" in input:
        moves = input["moves"]
        movesValidity = isMovesValid(moves)
        if movesValidity["isInvalid"]:
            return {"gameStatus": "error: "+ movesValidity["errorMessage"]}

    #Check that direction is valid
    if "direction" not in input:
        return {"gameStatus": "error: missing direction"}

    direction = input["direction"]
    directionValidity = isDirectionValid(direction)

    if directionValidity["isInvalid"]:
        return {"gameStatus": "error: " + directionValidity["errorMessage"]}

    #Force direction to comply with desired format
    if (type(direction) is unicode):
        direction = direction.encode('ascii', 'ignore')
    direction = direction.lower()


    try:
        searchResults = searchSwipePaths(board, moves - 1, direction, time.clock())
    except RuntimeError:
        return { "gameStatus": "error: runtime error detected" }

    if (searchResults["isInvalid"]):
        return {"gameStatus": "error: " + searchResults["errorMessage"]}


    resultPackage = {}
    resultPackage["gameStatus"] = "underway"
    resultPackage["highScore"] = searchResults["maxScore"]
    resultPackage["lowScore"] = searchResults["minScore"]
    resultPackage["averageScore"] = round(searchResults["avgScore"],0)


    return resultPackage