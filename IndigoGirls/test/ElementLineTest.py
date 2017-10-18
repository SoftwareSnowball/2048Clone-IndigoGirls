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
        #                    CAUTION: IT WAS DECIDED THAT THE NUMBERING WILL START FROM 0
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
        lineNumber = 0

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine._grid, board["grid"])
        self.assertEqual(testLine._initialIndex, 0)
        self.assertEqual(testLine._stride, 1)
        self.assertEqual(testLine._length, 5)


    def test_ElementLineInit_02(self):

        board = {"grid": [0, 1, 2, 3, 4], "rowCount": 1, "columnCount": 5}
        direction = "left"
        lineNumber = 0

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine._grid, board["grid"])
        self.assertEqual(testLine._initialIndex, board["columnCount"] - 1)
        self.assertEqual(testLine._stride, -1)
        self.assertEqual(testLine._length, 5)


    def test_ElementLineInit_03(self):


        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "left"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine._grid, board["grid"])
        self.assertEqual(testLine._initialIndex, 7)
        self.assertEqual(testLine._stride, -1)
        self.assertEqual(testLine._length, 4)


    def test_ElementLineInit_04(self):


        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "down"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine._grid, board["grid"])
        self.assertEqual(testLine._initialIndex, 1)
        self.assertEqual(testLine._stride, 4)
        self.assertEqual(testLine._length, 2)


    def test_ElementLineInit_05(self):
        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "up"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine._grid, board["grid"])
        self.assertEqual(testLine._initialIndex, 1 + 4)
        self.assertEqual(testLine._stride, -4)
        self.assertEqual(testLine._length, 2)


    # Function getElement(self, index)
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
        lineNumber = 0

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine.getElement(4), 4)
        self.assertEqual(testLine.getElement(2), 2)
        self.assertEqual(testLine.getElement(5), "Error: Index out of bounds")


    def test_getElement_02(self):

        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "right"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine.getElement(0), 4)
        self.assertEqual(testLine.getElement(3), 7)
        self.assertEqual(testLine.getElement(5), "Error: Index out of bounds")

    def test_getElement_03(self):

        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "left"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine.getElement(0), 7)
        self.assertEqual(testLine.getElement(3), 4)
        self.assertEqual(testLine.getElement(4), "Error: Index out of bounds")


    def test_getElement_04(self):

        board = {"grid": [0, 1, 2, 3, 4], "rowCount": 1, "columnCount": 5}
        direction = "left"
        lineNumber = 0

        testLine = ElementLine(board, direction, lineNumber)

        self.assertEqual(testLine.getElement(4), 0)
        self.assertEqual(testLine.getElement(2), 2)
        self.assertEqual(testLine.getElement(5), "Error: Index out of bounds")


    def test_getElement_05(self):

        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "down"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)


        self.assertEqual(testLine.getElement(0), 1)
        self.assertEqual(testLine.getElement(1), 5)
        self.assertEqual(testLine.getElement(3), "Error: Index out of bounds")

    def test_getElement_06(self):

        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "up"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)


        self.assertEqual(testLine.getElement(0), 5)
        self.assertEqual(testLine.getElement(1), 1)
        self.assertEqual(testLine.getElement(3), "Error: Index out of bounds")



    # Function setElement(self, index, element)
    #
    # inputs:
    #       index - The location in the line of the desired element
    #       element - The value that should be written to the location at the index
    #
    # outputs:
    #       nothing
    #
    #
    # affects:
    #       grid

    def test_setElement_01(self):

        board = {"grid": [0, 1, 2, 3, 4, 5, 6, 7], "rowCount": 2, "columnCount": 4}
        direction = "up"
        lineNumber = 1

        testLine = ElementLine(board, direction, lineNumber)
        testLine.setElement(0, 10)

        self.assertEqual(board["grid"][5], 10)