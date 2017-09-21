'''
    Created on September 20, 2017

    @Author: James Malloy

    Purpose of File:
        To implement the initalizeGame function

    todo: finish description

'''


def initializeGame(messageDictionary):


    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False


    columnCount = 4
    rowCount = 4
    errorMessage = ''
    functionError = False


    if ('columnCount' in messageDictionary):
        columnCount = messageDictionary['columnCount']

        if isNotValidNumber(columnCount):
            functionError = True
            errorMessage = errorMessage + 'columnCount is not a valid number. '

    if ('rowCount' in messageDictionary):
        rowCount = messageDictionary['rowCount']

        if isNotValidNumber(columnCount):
            functionError = True
            errorMessage = errorMessage + 'rowCount is not a valid number. '



    gameMessage = {}

    if (functionError):
        errorMessage = "error:  " + errorMessage
        gameMessage['gameStatus'] = errorMessage
        return gameMessage



    grid = [0] * (columnCount * rowCount) #Python, your syntax is so weird



    gameMessage['score'] = 0
    gameMessage['board'] = {'columnCount': columnCount, 'rowCount' : rowCount, 'grid' : grid }
    gameMessage['gameStatus'] = 'underway'

    return gameMessage;