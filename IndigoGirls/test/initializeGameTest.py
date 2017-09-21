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

        assert('score' in answer)
        assert('board' in answer)
        assert('gameStatus' in answer)


    def test_checkBoardKeys(self):

        message = {'op': 'initializeGame'}
        answer = initializeGame(message)
        board = answer.get('board')

        assert('columnCount' in board)
        assert('rowCount' in board)
        assert('grid' in board)

    def test_checkFailedDictionaryKeys(self):

        message = {'op': 'initializeGame', 'columnCount': '3'}
        answer = initializeGame(message)

        assert(answer['gameStatus'] == 'error:  columnCount is not a valid number. ')

        assert('score' not in answer)
        assert('board' not in answer)
        assert('gameStatus' in answer)


#Checking boundaries for row and column count

    def test_checkUpperBoundColumnCount(self):

        message = {'op': 'initializeGame', 'columnCount' : 100}
        answer = initializeGame(message)

        assert(answer['gameStatus'] == 'underway')
        assert(answer['board']['columnCount'] == 100)

        message = {'op': 'initializeGame', 'columnCount' : 101}
        answer = initializeGame(message)

        assert (answer['gameStatus'] == 'error:  columnCount is not a valid number. ')

    def test_checkLowerBoundColumnCount(self):

        message = {'op': 'initializeGame', 'columnCount' : 2}
        answer = initializeGame(message)

        assert(answer['gameStatus'] == 'underway')
        assert(answer['board']['columnCount'] == 2)

        message = {'op': 'initializeGame', 'columnCount' : 1}
        answer = initializeGame(message)

        assert (answer['gameStatus'] == 'error:  columnCount is not a valid number. ')

    def test_checkUpperBoundRowCount(self):

        message = {'op': 'initializeGame', 'columnCount' : 100}
        answer = initializeGame(message)

        assert(answer['gameStatus'] == 'underway')
        assert(answer['board']['columnCount'] == 100)

        message = {'op': 'initializeGame', 'columnCount' : 101}
        answer = initializeGame(message)

    def test_checkLowerBoundRowCount(self):

        message = {'op': 'initializeGame', 'columnCount' : 2}
        answer = initializeGame(message)

        assert(answer['gameStatus'] == 'underway')
        assert(answer['board']['columnCount'] == 2)

        message = {'op': 'initializeGame', 'columnCount' : 1}
        answer = initializeGame(message)


#Checking that function in returning valid grid sizes

    def test_GridSize1(self):

        message = {'op': 'initializeGame'}
        answer = initializeGame(message)

        grid = answer['board']['grid']

        assert(len(grid) == 16)
        assert(answer['board']['columnCount'] == 4)
        assert(answer['board']['rowCount'] == 4)



    def test_GridSize2(self):

        message = {'op': 'initializeGame', 'columnCount' : 5}
        answer = initializeGame(message)

        grid = answer['board']['grid']

        assert(len(grid) == (4*5))
        assert(answer['board']['columnCount'] == 5)
        assert(answer['board']['rowCount'] == 4)


    def test_GridSize3(self):

        message = {'op': 'initializeGame', 'rowCount' : 7}
        answer = initializeGame(message)

        grid = answer['board']['grid']

        assert(len(grid) == (4*7))
        assert(answer['board']['columnCount'] == 4)
        assert(answer['board']['rowCount'] == 7)

    def test_GridSize3(self):

        message = {'op': 'initializeGame', 'columnCount': 2, 'rowCount' : 7}
        answer = initializeGame(message)

        grid = answer['board']['grid']

        assert(len(grid) == (2*7))
        assert(answer['board']['columnCount'] == 2)
        assert(answer['board']['rowCount'] == 7)