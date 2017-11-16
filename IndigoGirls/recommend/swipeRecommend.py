'''
    Created on November 16, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function to find the best swipe direction and return the results of a swipe in that direction
'''
from IndigoGirls.recommend.searchSwipePaths import searchSwipePaths
from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe
from IndigoGirls.utils.placeTile import placeTile
from IndigoGirls.utils.copyBoard import copyBoard

import random

def swipeRecommend(board, moves):


    directions = ["up", "down", "left", "right"]
    boardCopy = {}
    scores = [0] * 4

    for index in range(4):

        boardCopy = copyBoard(board)
        scores[index] = searchSwipePaths(boardCopy, moves - 1, directions[index])

    highestScore = max(scores)

    bestDirections = []

    for index in range(4):
        if (scores[index] == highestScore):
            bestDirections.append(directions[index])


    if (len(bestDirections) == 0):
        return {"gameStatus": "error: Cannot swipe in any direction. "}


    bestDirection = random.choice(bestDirections)

    generatedInput = {}
    generatedInput["board"] = copyBoard(board)
    generatedInput["direction"] = bestDirection
    output = deterministicSwipe(generatedInput)


    return output