'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Implement the status function

'''

from IndigoGirls.status.checkBoardStatus import checkBoardStatus
from IndigoGirls.status.isVictoryTileValid import isVictoryTileValid
from IndigoGirls.utils.isBoardValid import isBoardValid


def status(input):

    output = {}
    output["gameStatus"] = ""
    errorMessage = "error "
    isError = False

    if ("board" not in input):
        errorMessage += "missing board in input. "
        isError = True
        output["gameStatus"] = errorMessage
        return output

    board = input["board"]
    boardValidity = isBoardValid(board)

    if (boardValidity["isInvalid"]):
        isError = True
        errorMessage += boardValidity["errorMessage"]
        output["gameStatus"] = errorMessage
        return output

    tile = 2 ** round(board["rowCount"] * board["columnCount"] * 0.6875)


    if ("tile" in input):
        tile = input["tile"]
        tileValidity = isVictoryTileValid(tile, board["rowCount"], board["columnCount"])

        if (tileValidity["isInvalid"]):
            isError = True
            errorMessage += boardValidity["errorMessage"]
            output["gameStatus"] = errorMessage
            return output


    if (isError):
        output["gameStatus"] = errorMessage
        return output

    boardStatus = checkBoardStatus(tile, board)

    output["gameStatus"] = boardStatus

    return output