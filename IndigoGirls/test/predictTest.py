"""
    Created on December 10, 2017

    @Author: James Malloy

    This file contains unit tests pertaining to the predict function
"""

from unittest import TestCase
from IndigoGirls.predict.predict import predict


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

    def test_goodBoard01(self):
        input = {}

        board = {}
        board["grid"] = [0,1,2,0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertNotIn("error", output["gameStatus"])


    def test_badMoves01(self):
        input = {}

        board = {}
        board["grid"] = [1,2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "right"
        input["moves"] = 0

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badMoves02(self):
        input = {}

        board = {}
        board["grid"] = [1, 2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "right"
        input["moves"] = "1"

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badDirection01(self):
        input = {}

        board = {}
        board["grid"] = [1, 2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "north"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badDirection02(self):
        input = {}

        board = {}
        board["grid"] = [1, 2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = None
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badDirection03(self):
        input = {}

        board = {}
        board["grid"] = [1, 2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = 3
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_MissingDirection01(self):
        input = {}

        board = {}
        board["grid"] = [1, 2, 2, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        #input["direction"] = "up"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])


    def test_unicodeDirection(self):
        input = {}

        board = {}
        board["grid"] = [1, 1, 0, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = u"right"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 4)
        self.assertEqual(lowScore, 4)
        self.assertEqual(averageScore, 4)

    def test_capitalDirection(self):
        input = {}

        board = {}
        board["grid"] = [1, 1, 0, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "lEFt"
        input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 4)
        self.assertEqual(lowScore, 4)
        self.assertEqual(averageScore, 4)

    def test_predictWithNoSpecifiedMoves01(self):
        input = {}

        board = {}
        board["grid"] = [1, 1, 0, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "left"
        #input["moves"] = 1

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 4)
        self.assertEqual(lowScore, 4)
        self.assertEqual(averageScore, 4)

    def test_predictDepth2_01(self):
        input = {}

        board = {}
        board["grid"] = [1, 1, 0, 0]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "down"
        input["moves"] = 2

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 4)
        self.assertEqual(lowScore, 0)
        self.assertEqual(averageScore, 3)

    def test_predictDepth2_02(self):
        input = {}

        board = {}
        board["grid"] = [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]
        board["rowCount"] = 4
        board["columnCount"] = 4

        input["board"] = board
        input["direction"] = "left"
        input["moves"] = 2

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 20)
        self.assertEqual(lowScore, 16)
        self.assertEqual(averageScore, 19)

    def test_predictDepth3_02(self):
        input = {}

        board = {}
        board["grid"] = [1, 1, 3, 2]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "right"
        input["moves"] = 3

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("underway", output["gameStatus"])
        self.assertIn("highScore", output)
        self.assertIn("lowScore", output)
        self.assertIn("averageScore", output)

        highScore = output["highScore"]
        lowScore = output["lowScore"]
        averageScore = output["averageScore"]

        self.assertEqual(highScore, 28)
        self.assertEqual(lowScore, 4)
        self.assertEqual(averageScore, 16)


    def test_predictNoValidMove_03(self):
        input = {}

        board = {}
        board["grid"] = [1,2,3,4]
        board["rowCount"] = 2
        board["columnCount"] = 2

        input["board"] = board
        input["direction"] = "down"
        input["moves"] = 2

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_predictManyMoves_01(self):
        input = {}

        board = {}
        board["grid"] = [0] * (100*100)
        board["rowCount"] = 100
        board["columnCount"] = 100

        board["grid"][3] = 4
        board["grid"][2] = 5
        board["grid"][23] = 2

        input["board"] = board
        input["direction"] = "down"
        input["moves"] = 1000000

        output = predict(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])