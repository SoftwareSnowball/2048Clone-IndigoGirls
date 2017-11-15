'''
    Created  on November 11, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the public interface for the recommend functionality in IndigoGirls

'''


from IndigoGirls.utils.isBoardValid import isBoardValid

def recommend(input):
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

    moves = 0

    if ("moves" in input):
        moves = input["moves"]

        if (type(moves) is not int or moves < 0):
            errorMessage += "moves is invalid. "
            isError = True
            output["gameStatus"] = errorMessage
            return output






    return output