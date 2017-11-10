'''
    Created on November 9, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used to check the validity of rowCount and columnCount
'''


def areDimensionsValid(rowCount, columnCount):

    #Function is used to simplify the validity check for both rowCount and columnCount
    #This function is also declared in initializeGame.
    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False


    resultPackage = {}
    resultPackage["isError"] = False
    errorMessage = ""
    resultPackage["errorMessage"] = errorMessage

    if (isNotValidNumber(rowCount)):
        errorMessage += "rowCount is invalid. "
        resultPackage["isError"] = True

    if (isNotValidNumber(columnCount)):
        errorMessage += "columnCount is invalid. "
        resultPackage["isError"] = True


    return resultPackage