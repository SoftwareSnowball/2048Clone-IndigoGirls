'''
    Created on November 9, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used to check the validity of a given board
'''

from IndigoGirls.areDimensionsValid import areDimensionsValid

def isBoardValid(board):

    resultPackage = {}
    resultPackage["isError"] = False
    errorMessage = ""
    resultPackage["errorMessage"] = errorMessage


    if (type(board) is not dict):
        resultPackage["isError"] = True
        errorMessage += "board is not a dictionary. "
        return resultPackage

    if ("grid" not in board):
        resultPackage["isError"] = True
        errorMessage += "grid missing from board. "

    if ("rowCount" not in board):
        resultPackage["isError"] = True
        errorMessage += "rowCount is missing from board. "

    if ("columnCount" not in board):
        resultPackage["isError"] = True
        errorMessage += "columnCount is missing from board. "

    if (resultPackage["isError"]):
        return resultPackage

    dimensionValidity = areDimensionsValid(board["rowCount"], board["columnCount"])

    if (dimensionValidity["isError"]):
        resultPackage["isError"] = True
        errorMessage += dimensionValidity["errorMessage"]
        return resultPackage

    # I don't want this code to run if rowCount or columnCount is not valid because it could cause an exception
    if (len(board["grid"]) != board["rowCount"] * board["columnCount"]):
        errorMessage += "Grid size is invalid. "
        resultPackage["isError"] = True


    return resultPackage