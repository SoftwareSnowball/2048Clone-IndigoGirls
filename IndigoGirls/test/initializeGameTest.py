"""
    Created on September 20, 2017

    @Author: James Malloy

    This file contains unit test pertaining to the initializeGame function
"""

from unittest import TestCase
from IndigoGirls.initializeGame import initializeGame


#----------------------------------
#Acceptance Tests:
#
#
#Inputs:
#       op, paired with 'initializeGame'. This is checked by dispatch and does not need to be considered.
#       rowCount, should be paired with an integer from 2 to 100, optional assumed as 4, not verified
#       columnCount, should be paired with an integer from 2 to 100, optional assumed as 4, not verified
#
#Outputs:
#       In design case the function returns a dictionary containing:
#       score, contains 0 as an integer value
#       board, a dictionary containing:
#           columnCount, pairs with an integer representing the number of columns the board has
#           rowCount, pairs with an integer representing the number of rows the board has
#           grid, pairs with a list representing each cell in the grid. Numbers are 0 for empty cell or the power of 2 contained in the cell
#       Gamestatus, should pair with 'underway'
#
#       In the event of an error, the function returns a dictionary containing:
#        gameStatus, paired with an appropriate error message
#

class InitializeGameTest(TestCase):


#These tests check for basic functionality and ensure the function is returning the correct dictionary fields

    def test_checkPassDictionaryKeys(self):

        message = {'op' : 'initializeGame'}
        answer = initializeGame(message)

        assert('score' in message)
        assert('board' in message)
        assert('gameStatus' in message)


    def test_checkBoardKeys(self):

        message = {'op': 'initializeGame'}
        answer = initializeGame(message)
        board = answer.get('board')

        assert('columnCount' in board)
        assert('rowCount' in board)
        assert('grid' in board)

    def test_checkFailedDictionaryKeys(self):

        message = {'op': 'initializeGame'}
        answer = initializeGame(message)

        assert('score' not in answer)
        assert('board' not in answer)
        assert('gameStatus' in answer)


