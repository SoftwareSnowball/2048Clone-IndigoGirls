'''
    Created on November 16, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used recursively find the action that could lead to the highest score in n moves
'''

from IndigoGirls.utils.copyBoard import copyBoard
from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe

def searchSwipePathsWithScores(board, movesleft, direction):
    # perform swipe on board in direction
    # store score from swipe

    # if move is invalid return -1


    # if moves left > 0 and if swipe is valid then
    #   call search swipe paths for each direction with moves - 1, and a copy of board
    #   pick path with greatest score
    #   add greatest score to score

    # if greatest score is -1
    #   return -1
    # return score

    score = 1

    inputPackage = {}
    inputPackage["board"] = board
    inputPackage["direction"] = direction

    myResults = deterministicSwipe(inputPackage)

    if ("error" in myResults["gameStatus"]):
        return -1

    score = myResults["score"]

    if (movesleft == 0):
        return score

    directions = ["up", "down", "left", "right"]
    scores = [0] * 4

    for index in range(4):
        boardCopy = copyBoard(board)
        scores[index] = searchSwipePathsWithScores(boardCopy, movesleft - 1, directions[index])

    maxScore = max(scores)

    if (maxScore == -1):
        return -1

    score += maxScore
    return score