'''
    Created on November 9, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used to check the validity of a given board
'''

from IndigoGirls.utils.areDimensionsValid import areDimensionsValid


def isBoardValid(board):

    resultPackage = {}
    resultPackage["isInvalid"] = False
    errorMessage = ""
    resultPackage["errorMessage"] = errorMessage


    if (type(board) is not dict):
        resultPackage["isInvalid"] = True
        errorMessage += "board is not a dictionary. "
        return resultPackage

    if ("grid" not in board):
        resultPackage["isInvalid"] = True
        errorMessage += "grid missing from board. "
        return resultPackage

    if ("rowCount" not in board):
        resultPackage["isInvalid"] = True
        errorMessage += "rowCount is missing from board. "
        return resultPackage

    if ("columnCount" not in board):
        resultPackage["isInvalid"] = True
        errorMessage += "columnCount is missing from board. "
        return resultPackage

    if (type(board["grid"]) is not list):
        resultPackage["isInvalid"] = True
        errorMessage += "grid must be a list. "
        return resultPackage

    dimensionValidity = areDimensionsValid(board["rowCount"], board["columnCount"])

    if (dimensionValidity["isInvalid"]):
        resultPackage["isInvalid"] = True
        errorMessage += dimensionValidity["errorMessage"]
        return resultPackage

    # I don't want this code to run if rowCount or columnCount is not valid because it could cause an exception
    if (len(board["grid"]) != board["rowCount"] * board["columnCount"]):
        errorMessage += "Grid size is invalid. "
        resultPackage["isInvalid"] = True
        return resultPackage


    #Check that at least two members are non zero
    nonIntFound = False
    nonZerosFound = 0
    negativesFound = 0
    for element in board["grid"]:

        if type(element) is int: #because I really really don't trust python (and my distrust proved warranted)
            if element is not 0:
                nonZerosFound += 1
            if element < 0:
                negativesFound += 1
                break
        else:
            nonIntFound = True

    if (nonIntFound):
        errorMessage += "grid contains non integer element. "
        resultPackage["isInvalid"] = True
        return resultPackage

    if (negativesFound > 0):
        errorMessage += "grid must not contain negative numbers. "
        resultPackage["isInvalid"] = True
        return resultPackage


    if (nonZerosFound < 2):
        errorMessage += "grid must contain at least 2 non empty tiles. "
        resultPackage["isInvalid"] = True
        return resultPackage



    return resultPackage