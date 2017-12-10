'''
    Created  on December 10, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the public interface for the predict functionality in IndigoGirls

'''

from IndigoGirls.utils.isBoardValid import isBoardValid


def predict(input):

    if "board" not in input:
        return {"gameStatus": "error: missing board"}

    boardValidity = isBoardValid(input["board"])

    if boardValidity["isInvalid"] == True:
        return {"gameStatus": "error: " + boardValidity["errorMessage"] }

    return 0