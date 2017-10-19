'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Tests functionality of the swipe function

'''

from unittest import TestCase
from IndigoGirls.swipe import swipe


# Function swipe
#
# Inputs:
#   direction, unvalidated
#   board, unvalidated
#       rowCount
#       columnCount
#       grid
#
#   Acceptable inputs:
#       direction
#           string value, must be "left", "right", "up", or "down"
#       grid:
#           grid must contain all integers GE than 0
#           grid size must equal rowCount * columnCount
#       columnCount
#           integer from 2 to 100 inclusive
#       rowCount
#           integer from 2 to 100 inclusive
#
#



class SwipeTest(TestCase):

    def test_swipeValidate01(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = 3

        board = {"columnCount": columnCount, "rowCount" :rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual(output["gamestatus"], "Error: Direction must be string")



