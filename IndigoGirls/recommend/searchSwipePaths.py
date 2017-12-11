'''
    Created on November 16, 2017

    @Author: James Malloy

    Purpose of File:
        Holds a function used recursively find the action that could lead to the highest score in n moves
'''

from IndigoGirls.utils.copyBoard import copyBoard
from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe

def searchSwipePaths(board, movesleft, direction):

    #perform swipe on board in direction
    #store score from swipe

    #if move is invalid return -1


    #if moves left > 0 and if swipe is valid then
    #   call search swipe paths for each direction with moves - 1, and a copy of board
    #   pick path with greatest score
    #   add greatest score to score

    #if greatest score is -1
    #   return -1
    #return score

    errorMessage = ""

    outputPackage = {}
    outputPackage["isInvalid"] = False
    outputPackage["errorMessage"] = errorMessage
    outputPackage["maxScore"] = -1
    outputPackage["minScore"] = -1
    outputPackage["avgScore"] = -1
    outputPackage["scoreWeight"] = 1

    inputPackage = {}
    inputPackage["board"] = board
    inputPackage["direction"] = direction

    myResults = deterministicSwipe(inputPackage)

    if ("error" in myResults["gameStatus"]):
        outputPackage["isInvalid"] = True
        errorMessage = " swipe could not be performed"
        return outputPackage

    myScore = myResults["score"]

    outputPackage["maxScore"] = myScore
    outputPackage["minScore"] = myScore
    outputPackage["avgScore"] = myScore

    if (movesleft == 0):
        return outputPackage

    directions = ["up", "down", "left", "right"]

    maxScores = []
    minScores = []
    avgScores = []
    avgScoreWeights = []


    for index in range(4):
        boardCopy = copyBoard(board)
        directionalSearchResult = searchSwipePaths(boardCopy, movesleft - 1, directions[index])

        if directionalSearchResult["isInvalid"] == False:
            maxScores.append(directionalSearchResult["maxScore"])
            minScores.append(directionalSearchResult["minScore"])
            avgScores.append(directionalSearchResult["avgScore"])
            avgScoreWeights.append(directionalSearchResult["scoreWeight"])

    if (len(maxScores) == 0):
        outputPackage["isInvalid"] = True
        return outputPackage


    outputPackage["maxScore"] += max(maxScores)
    outputPackage["minScore"] += min(minScores)

    average = 0.0
    for index in range(len(avgScores)):
        average += float(avgScores[index]) * float(avgScoreWeights[index])

    average /= float(sum(avgScoreWeights))

    outputPackage["avgScore"] += average




    return outputPackage