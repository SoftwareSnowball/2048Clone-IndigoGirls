'''
    Created on November 9, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used to check the validity of a given tile value
'''

def isVictoryTileValid(tile, rowCount, columnCount):

    resultPackage = {}
    errorMessage = ""
    resultPackage["errorMessage"] = errorMessage
    resultPackage["isInvalid"] = False

    if (type(tile) is not int):
        resultPackage["isInvalid"] = True
        errorMessage = "tile type is not int. "
        return resultPackage

    if (tile < 2):
        resultPackage["isInvalid"] = True
        errorMessage = "tile is too small. "
    elif (tile > 2 ** (rowCount * columnCount)):
        resultPackage["isInvalid"] = True
        errorMessage = "tile is too small. "

    return resultPackage