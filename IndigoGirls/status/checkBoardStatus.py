'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        The actual code of that checks what state the board is in
        All inputs should be prevalidated by the time they reach this function

'''

from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe

def checkBoardStatus(tile, board):

    def prepareInputPackage(direction):
        inputPackage = {}
        inputPackage["direction"] = direction
        inputPackage["board"] = dict(board)
        inputPackage["board"]["grid"] = list(board["grid"])
        return inputPackage


    output = ""

    for element in board["grid"]:
        if (element >= tile):
            output = "win"
            return output

    swipeResults = [0]*4

    upInput = prepareInputPackage("up")
    swipeResults[0] = deterministicSwipe(upInput)
    downInput = prepareInputPackage("down")
    swipeResults[1] = deterministicSwipe(downInput)
    leftInput = prepareInputPackage("left")
    swipeResults[2] = deterministicSwipe(leftInput)
    rightInput = prepareInputPackage("right")
    swipeResults[3] = deterministicSwipe(rightInput)

    for result in swipeResults:

        if ("error" not in result["gameStatus"]):
            return "underway"


    return "lose"


    return output