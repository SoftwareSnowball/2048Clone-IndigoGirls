'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Tests functionality of the status function

'''

# Function swipe
#
# Inputs:
#   tile, unvalidated, optional
#   board, unvalidated
#       rowCount
#       columnCount
#       grid
#
#   Acceptable inputs:
#       tile:
#           specifies winning tile val.
#           GE 2 and LE 2**(rowCount * colCount)
#       grid:
#           grid must contain all integers GE than 0
#           grid size must equal rowCount * columnCount
#       columnCount
#           integer from 2 to 100 inclusive
#       rowCount
#           integer from 2 to 100 inclusive
#
#   Sad paths
#       tile:
#           doesn't exits
#           out of range
#           not int
#       board:
#           doesn't exist
#           board not dictionary
#       grid:
#           doesn't exist
#           not array of ints
#           less than 2 elements are nonzero
#           wrong size
#       rowCount:
#           doesn't exits
#           not int
#           not in range
#       colCount:
#           same as rowCount
#
#   Happy path

from unittest import TestCase
from IndigoGirls.status import status


class statusTest(TestCase):


    def test_noBoard(self):

        input = {}
        input["tile"] = 3

        output = status(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])
