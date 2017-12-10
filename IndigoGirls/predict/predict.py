'''
    Created  on December 10, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the public interface for the predict functionality in IndigoGirls

'''

from IndigoGirls.utils.isBoardValid import isBoardValid
from IndigoGirls.predict.checkMoves import checkMoves


def predict(input):

    #Check that board is valid
    if "board" not in input:
        return {"gameStatus": "error: missing board"}

    boardValidity = isBoardValid(input["board"])

    if boardValidity["isInvalid"] == True:
        return {"gameStatus": "error: " + boardValidity["errorMessage"] }

    #Check that moves is valid
    moves = 1
    if "moves" in input:
        moves = input["moves"]
        movesValidity = checkMoves(moves)
        if movesValidity["isInvalid"] == True:
            return {"gameStatus": "error: "+ movesValidity["errorMessage"]}


    return {}