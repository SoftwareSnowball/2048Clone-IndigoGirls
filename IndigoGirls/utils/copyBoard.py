'''
    Created  on November 11, 2017


    @Author: James Malloy

    Purpose of File:
        To hold a function used to create a deep copy of a board

'''

def copyBoard(board):

    newBoard = {}

    newBoard["rowCount"] = board["rowCount"]
    newBoard["columnCount"] = board["columnCount"]
    newBoard["grid"] = list(board["grid"])


    return newBoard