"""
    Created on October 17, 2017

    @Author: James Malloy

    This file contains unit tests pertaining to the ElementLine class
"""
from unittest import TestCase
from IndigoGirls.ElementLine import ElementLine

class ElementLineTest(TestCase):


#Function __init__(self, board, direction, line_number)
#
#inputs:
#       board - a dictionary containing the grid, number of columns, number of rows
#               already verified
#       direction - up, down, left, or right; verified
#       line_number - the column or row that is being abstracted from the grid
#
#outputs:
#       ElementLine object
#
#
#affects:
#       grid
#       initial_index
#       stride
#       length
#




    def test_ElementLineInit(self):

        board = {"grid": [0,1,2,3,4], "rowCount": 1, "columnCount": 5}
        direction = "right"
        line_number = 1

        test_line = ElementLine(board, direction, line_number)

        self.assertEqual(test_line._grid, board["grid"])
        self.assertEqual(test_line._initialIndex, 0)
        self.assertEqual(test_line._stride, 1)
        self.assertEqual(test_line._length, 5)





