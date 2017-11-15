'''
    Created  on November 11, 2017


    @Author: James Malloy

    Purpose of File:
        To hold the tests related to the recommend functionality in IndigoGirls

'''

# Function swipe
#
# Inputs:
#   moves, unvalidated, optional
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
#       general behavior induced sadness
#           if no tiles can be moved during the process
#
#



from unittest import TestCase
from IndigoGirls.recommend.recommend import recommend

class RecommendTest(TestCase):

    def test_noBoard(self):

        input = {}

        output = recommend(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_badBoard1(self):
        input = {}
        input["board"] = "muffin"

        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard2(self):
        input = {}
        board = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard3(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2


        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard4(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = "salad"

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = "2"
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard6(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 3
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])


    def test_badBoard7(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2,0,0,0,0,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard8(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2,"cake",0,0,0,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_goodBoard1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertNotIn("error", output["gameStatus"])


    def test_badmoves1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3*2)

        moves = "cat"

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badmoves2(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3 * 2)

        moves = -1

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_goodmoves1(self):
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3 * 2)

        moves = 0

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertNotIn("error", output["gameStatus"])

    def test_0depthrecommend1(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [2,2,1,3]

        moves = 0

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertNotIn("error", output["gameStatus"])
        self.assertIn("grid", output)
        grid = output["grid"]

        self.assertTrue(grid[0] == 3 or grid[1] == 3)
