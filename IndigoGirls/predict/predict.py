'''
    Created  on December 10, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the public interface for the predict functionality in IndigoGirls

'''

from IndigoGirls.utils.isBoardValid import isBoardValid
from IndigoGirls.predict.isMovesValid import isMovesValid
from IndigoGirls.utils.isDirectionValid import isDirectionValid

def predict(input):

    #Check that board is valid
    if "board" not in input:
        return {"gameStatus": "error: missing board"}

    board = input["board"]
    boardValidity = isBoardValid(board)

    if boardValidity["isInvalid"] == True:
        return {"gameStatus": "error: " + boardValidity["errorMessage"] }

    #Check that moves is valid
    moves = 1
    if "moves" in input:
        moves = input["moves"]
        movesValidity = isMovesValid(moves)
        if movesValidity["isInvalid"] == True:
            return {"gameStatus": "error: "+ movesValidity["errorMessage"]}

    #Check that direction is valid
    if "direction" not in input:
        return {"gameStatus": "error: missing direction"}

    direction = input["direction"]
    directionValidity = isDirectionValid(direction)


    return {"gameStatus": "test"}