'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Holds swipe function which performs the swipe task in the game

'''

import random
from IndigoGirls.deterministicSwipe import deterministicSwipe

#TODO refactor validation tests from deterministicSwipe into swipe

def swipe(input):

    results = deterministicSwipe(input)

    #Check that board has empty spot
    grid = results["board"]["grid"]
    index = 0
    hasEmpty = False

    while (hasEmpty == False and index < len(grid)):
        if (grid[index] == 0):
            hasEmpty = True

        index += 1

    if (hasEmpty != True):
        return {"gameStatus": "Error. Grid has no empty tile. (This error should never occur)"}


    #TODO: Refactor - This code is very similar to code in initializeGame
    piecePlacement = random.randint(0, len(grid) - 1)

    while (grid[piecePlacement] != 0):
        piecePlacement = random.randint(0, len(grid) - 1)

    value = random.randint(0, 3)
    if (value == 3):
        grid[piecePlacement] = 2
    else:
        grid[piecePlacement] = 1


    return results