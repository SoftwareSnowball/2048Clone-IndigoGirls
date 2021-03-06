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
from IndigoGirls.utils.copyBoard import copyBoard

class RecommendTest(TestCase):

    def test_noBoard01(self):

        input = {}

        output = recommend(input)

        self.assertIn("gameStatus", output)
        self.assertIn("error", output["gameStatus"])

    def test_noBoard02(self):

        input = {}
        input["tile"] = 4
        input["moves"] = 1

        output = recommend(input)
        #error from assignment 7 could not be replicated
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

    def test_badBoard5_1(self):
        board = {}
        board["rowCount"] = 3
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_2(self):
        board = {}
        board["columnCount"] = 2
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_3(self):
        board = {}
        board["columnCount"] = 2
        board["rowCount"] = None
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_4(self):
        board = {}
        board["columnCount"] = None
        board["rowCount"] = 3
        board["grid"] = [2,2,2,2,2,0]

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_5(self):
        board = {}
        board["columnCount"] = 101
        board["rowCount"] = 3
        board["grid"] = [0] * (3*101)
        board["grid"][0] = 1
        board["grid"][1] = 2

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_6(self):
        board = {}
        board["columnCount"] = 3
        board["rowCount"] = 101
        board["grid"] = [0] * (3*101)
        board["grid"][0] = 1
        board["grid"][1] = 2

        input = {}
        input["board"] = board
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_badBoard5_7(self):
        board = {}
        board["columnCount"] = 3
        board["rowCount"] = 12
        board["grid"] = [0] * (3*12)
        board["grid"][0] = 1
        board["grid"][1] = 2
        board["grid"][1] = -1


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

    def test_badmoves3(self): #no moves
        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [2] * (3 * 2)

        input = {}
        input["board"] = board
        input["moves"] = "nan"
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

    def test_0depthRecommend1(self):

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
        grid = output["board"]["grid"]

        self.assertTrue(grid[0] == 3 or grid[1] == 3)

    def test_0depthRecommend2(self):
        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [2, 5, 1, 3]

        moves = 0

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertIn("error", output["gameStatus"])

    def test_0depthRecommend3(self):
        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [2, 3, 0, 0]

        moves = 0

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        boardOut = output["board"]



        self.assertNotIn("error", output["gameStatus"])
        self.assertEqual(boardOut["grid"][2], 2)
        self.assertEqual(boardOut["grid"][3], 3)


    def test_0depthRecommend4(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        grid = [2,2,1,3]
        board["grid"] = list(grid)

        moves = 0
        leftMoves = 0
        rightMoves = 0

        input = {}
        input["board"] = board
        input["moves"] = moves

        trials = 1000
        i = 0

        while (i < trials):
            i += 1
            output = recommend(input)

            self.assertNotIn("error", output["gameStatus"])
            grid = output["board"]["grid"]

            if (grid[0] == 3):
                leftMoves += 1
            else:
                rightMoves += 1



        percentMoves = float(leftMoves) / float(trials)
        self.assertEqual(leftMoves + rightMoves, trials)
        self.assertAlmostEqual(percentMoves, 0.5, 1)

    def test_0depthRecommend5(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        grid = [3, 3, 3, 0]
        board["grid"] = list(grid)

        moves = 0
        leftMoves = 0
        rightMoves = 0
        upMoves = 0
        downMoves = 0

        input = {}
        input["moves"] = moves

        trials = 1000
        i = 0

        while (i < trials):
            i += 1
            input["board"] = copyBoard(board)
            output = recommend(input)


            self.assertNotIn("error", output["gameStatus"])
            grid = output["board"]["grid"]

            if (grid[0] == 4 and grid[2] == 3):
                leftMoves += 1
            elif (grid[1] == 4 and grid[3] == 3):
                rightMoves += 1
            elif (grid[2] == 4 and grid[3] == 3):
                downMoves += 1
            else:
                upMoves += 1

        percentMoves = float(upMoves) / float(trials)
        self.assertEqual(leftMoves + rightMoves + downMoves + upMoves, trials)
        self.assertAlmostEqual(percentMoves, 0.25, 1)


    def test_1depthRecommend1(self):

        board = {}
        board["rowCount"] = 3
        board["columnCount"] = 2
        board["grid"] = [1,1,2,3,2,2]

        moves = 1

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)


        self.assertEqual(output["score"], 12)

    def test_1depthRecommend2(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [2,2,1,3]

        moves = 1

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)

        self.assertNotIn("error", output["gameStatus"])
        grid = output["board"]["grid"]

        self.assertTrue(grid[0] == 3 or grid[1] == 3)

    def test_1depthRecommend3(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 2
        board["grid"] = [1,1,2,0]

        moves = 1

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)


        self.assertEqual(output["score"], 2**2)
        self.assertTrue(output["board"]["grid"][0] == 2 or output["board"]["grid"][1] == 2)

    def test_2depthRecommend1(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 3
        board["grid"] = [3, 1, 4, 3, 0, 3]

        moves = 2

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)
        outputGrid = output["board"]["grid"]


        self.assertEqual(output["score"], 16)
        self.assertEqual(outputGrid[0], 3)
        self.assertEqual(outputGrid[1], 1)
        self.assertEqual(outputGrid[2], 4)
        self.assertEqual(outputGrid[5], 4)


    def test_3depthRecommend1(self):

        board = {}
        board["rowCount"] = 2
        board["columnCount"] = 3
        board["grid"] = [3, 5, 4, 3, 0, 3]

        moves = 3

        input = {}
        input["board"] = board
        input["moves"] = moves
        output = recommend(input)
        outputGrid = output["board"]["grid"]

        print outputGrid


        self.assertEqual(output["score"], 16)
        self.assertEqual(outputGrid[0], 3)
        self.assertEqual(outputGrid[1], 5)
        self.assertEqual(outputGrid[2], 4)
        self.assertEqual(outputGrid[5], 4)
