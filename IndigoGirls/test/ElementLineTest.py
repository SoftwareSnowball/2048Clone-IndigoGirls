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
        #       lineNumber - the column or row that is being abstracted from the grid
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




    def test_ElementLineInit_01(self):

        board = {"grid": [0,1,2,3,4], "rowCount": 1, "columnCount": 5}
        direction = "right"
        lineNumber = 1

        test_line = ElementLine(board, direction, lineNumber)

        self.assertEqual(test_line._grid, board["grid"])
        self.assertEqual(test_line._initialIndex, 0)
        self.assertEqual(test_line._stride, 1)
        self.assertEqual(test_line._length, 5)


    def test_ElementLineInit_02(self):

        board = {"grid": [0, 1, 2, 3, 4], "rowCount": 1, "columnCount": 5}
        direction = "left"
        lineNumber = 1

        test_line = ElementLine(board, direction, lineNumber)


        self.assertEqual(test_line._grid, board["grid"])
        self.assertEqual(test_line._initialIndex, board["columnCount"] - 1)
        self.assertEqual(test_line._stride, -1)
        self.assertEqual(test_line._length, 5)


    # Function getElement(self, board, direction, line_number)
    #
    # inputs:
    #       index - The location in the line of the desired element
    #
    # outputs:
    #       grid element at given location
    #
    #
    # affects:
    #       nothing

    def test_getElement_01(self):

        board = {"grid": [0, 1, 2, 3, 4], "rowCount": 1, "columnCount": 5}
        direction = "right"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine.getElement(4), 4)
        self.assertEqual(testLine.getElement(2), 2)