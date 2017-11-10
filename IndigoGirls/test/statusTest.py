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
#           GE 2 and LE 2**(rowCount * columnCount) REQ EDIT!
#           defaults to 2**round(rowCount * columnCount * 0.6875) REQ EDIT!
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

        output = status(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard1(self):
        input = {}
        input["board"] = "muffin"

        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard2(self):
        input = {}
        board = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard3(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2


        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard4(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = "salad"

        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = "2"
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard6(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 3
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])


    def test_badBoard7(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2,0,0,0,0,0]

        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard8(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2,"cake",0,0,0,0]

        input = {}
        input["board"] = board
        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_goodBoard1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        output = status(input)

        self.assertNotIn("error", output["gameStatus"])


    def test_badtile1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        input["tile"] = 1

        output = status(input)

        self.assertIn("error", output["gameStatus"])

    def test_badtile2(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        input["tile"] = 2 ** (board["rowCount"] * board["columnCount"]) + 1

        output = status(input)

        self.assertIn("error", output["gameStatus"])


    def test_goodtile1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        input["tile"] = 2

        output = status(input)

        self.assertNotIn("error", output["gameStatus"])



    def test_goodtile2(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        input["tile"] = 2 ** (board["rowCount"] * board["columnCount"])

        output = status(input)

        self.assertNotIn("error", output["gameStatus"])


    def test_win1(self):
        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [4, 0, 0, 0]

        input = {}
        input["board"] = board
        input["tile"] = 4

        output = status(input)

        self.assertIn("win", output["gameStatus"])
