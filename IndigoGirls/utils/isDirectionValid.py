'''
    Created on December 10, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used to check the validity of a given direction
'''

def isDirectionValid(direction):

    errorMessage = ""
    resultPackage = {}
    resultPackage["errorMessage"] = errorMessage
    resultPackage["isInvalid"] = False

    if (type(direction) is unicode):
        direction = direction.encode('ascii', 'ignore')

    if (type(direction) is not str):
        errorMessage += "Direction must be string. "
        resultPackage["isInvalid"] = True
        return resultPackage

    direction = direction.lower()
    input["direction"] = direction

    if (direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right'):
        errorMessage += "Direction not recognized. "
        resultPackage["isInvalid"] = True

    return resultPackage