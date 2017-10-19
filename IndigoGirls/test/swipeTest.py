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



    #Invalid input tests

    def test_swipe_ValidateDirection01(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = 3

        board = {"columnCount": columnCount, "rowCount" :rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("Direction must be string" in output["gameStatus"])



    def test_swipe_ValidateDirection02(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = "north"

        board = {"columnCount": columnCount, "rowCount" :rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("Direction not recognized" in output["gameStatus"])


    def test_swipe_ValidateRow01(self):
        columnCount = 2
        rowCount = 1
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount" :rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("rowCount is invalid" in output["gameStatus"])

    def test_swipe_ValidateRow02(self):
        columnCount = 2
        rowCount = 101
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("rowCount is invalid" in output["gameStatus"])


    def test_swipe_ValidateColumn01(self):
        columnCount = 1
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("columnCount is invalid" in output["gameStatus"])

    def test_swipe_ValidateColumn02(self):
        columnCount = 101
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("columnCount is invalid" in output["gameStatus"])

    def test_swipe_ValidateColumn03(self):
        columnCount = "5"
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("columnCount is invalid" in output["gameStatus"])


    def test_swipe_ValidateGrid01(self):
        columnCount = 3
        rowCount = 2
        grid = [0] * (3*2 - 1)
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertTrue("Grid size is invalid" in output["gameStatus"])


    #Functionality Tests

    def test_swipe_FunctionalTest01(self):
        columnCount = 2
        rowCount = 2
        grid = [1, 0, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual([0,1,0,0], output["board"]["grid"])

    def test_swipe_FunctionalTest02(self):
        columnCount = 2
        rowCount = 2
        grid = [0, 1, 0, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual([1,0,0,0], output["board"]["grid"])


    def test_swipe_FunctionalTest02(self):
        columnCount = 2
        rowCount = 4
        grid = [0, 1, 1, 0, 1, 0, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual([0, 1, 0, 1, 0, 1, 0, 0], output["board"]["grid"])

    def test_swipe_FunctionalTest03(self):
        columnCount = 4
        rowCount = 2
        grid = [1, 2, 3, 0, 1, 2, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual([0, 1, 2, 3, 0, 0, 1, 2], output["board"]["grid"])


    def test_swipe_FunctionalTest03(self):
        columnCount = 2
        rowCount = 4
        grid = [1, 4, 3, 0, 1, 2, 0, 0]
        direction = "down"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertEqual([0, 0, 1, 0, 3, 4, 1, 2], output["board"]["grid"])