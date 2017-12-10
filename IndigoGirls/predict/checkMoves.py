'''
    Created  on December 10, 2017


    @Author: James Malloy

    Purpose of File:
        To hold a simple function that checks if moves are valid

'''


def checkMoves(moves):

    resultPackage = {}
    resultPackage["isInvalid"] = False
    errorMessage = ""
    resultPackage["errorMessage"] = errorMessage

    if type(moves) is not int:
        errorMessage = "moves must be integer value"
        resultPackage["isInvalid"] = True
        return resultPackage

    if (moves < 1):
        errorMessage = "moves must be greater than or equal to 1"
        resultPackage["isInvalid"] = True
        return resultPackage

    return resultPackage