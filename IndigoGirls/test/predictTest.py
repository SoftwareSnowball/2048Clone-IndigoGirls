"""
    Created on December 10, 2017

    @Author: James Malloy

    This file contains unit tests pertaining to the predict function
"""

from unittest import TestCase
from IndigoGirls.predict import predict


#----------------------------------
#Acceptance Tests:
#
#
# Inputs:
#   moves, unvalidated, optional
#   direction, unvalidated
#   board, unvalidated
#       rowCount
#       columnCount
#       grid
#
#   Acceptable inputs:
#       moves
#           int GE 0
#       grid:
#           grid must contain all integers GE than 0
#           grid size must equal rowCount * columnCount
#       columnCount
#           integer from 2 to 100 inclusive
#       rowCount
#           integer from 2 to 100 inclusive
#
#   Sad paths
#       board:
#           doesn't exist
#           board not dictionary
#       grid:
#           doesn't exist
#           not array of ints
#           less than 2 elements are nonzero
#           contains negatives
#           wrong size
#           none type
#       rowCount:
#           doesn't exits
#           not int
#           not in range
#           none type
#       colCount:
#           same as rowCount
#
#       general behavior induced sadness
#           if no tiles can be moved during the process
#
#


class PredictTest(TestCase):

    def test_noBoard01(self):

        input = {}
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard01(self):

        input = {}
        input["board"] = None
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard02(self):

        input = {}

        board = {}
        #no grid
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard03(self):
        input = {}

        board = {}
        board["grid"] = 5
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard04(self):
        input = {}

        board = {}
        board["grid"] = None
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard05(self):
        input = {}

        board = {}
        board["grid"] = [1,2,"pi",8]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard06(self):
        input = {}

        board = {}
        board["grid"] = [1,2,2.7,8]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard07(self):
        input = {}

        board = {}
        board["grid"] = [1,2,-1,8]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard08(self):
        input = {}

        board = {}
        board["grid"] = [1,2,-1,8, 4, 5, 6, 7, 4, 0, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])