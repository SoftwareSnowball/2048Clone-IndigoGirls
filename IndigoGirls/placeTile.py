'''
    Created on September 20, 2017

    @Author: James Malloy

    Purpose of File:
        Function places random tile on grid
        Input is board
        Assumes board is valid

'''


import random


def placeTile(grid):

    #Check that board has empty spot
    index = 0
    hasEmpty = False

    while (hasEmpty == False and index < len(grid)):
        if (grid[index] == 0):
            hasEmpty = True

        index += 1

    if (hasEmpty != True):
        return False

    #TODO: Refactor - This code is very similar to code in initializeGame
    piecePlacement = random.randint(0, len(grid) - 1)

    while (grid[piecePlacement] != 0):
        piecePlacement = random.randint(0, len(grid) - 1)

    value = random.randint(0, 3)
    if (value == 3):
        grid[piecePlacement] = 2
    else:
        grid[piecePlacement] = 1

    return True