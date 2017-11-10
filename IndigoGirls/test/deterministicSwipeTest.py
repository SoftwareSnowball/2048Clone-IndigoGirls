'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Tests functionality of the deterministicSwipe function

'''

from unittest import TestCase

from IndigoGirls.swipe.deterministicSwipe import deterministicSwipe


# Function swipe
#
# Inputs:
#   direction, validated
#   board, validated
#       rowCount
#       columnCount
#       grid
#
#
#



class deterministicSwipeTest(TestCase):

    #Functionality Tests

    def test_swipe_FunctionalTest01(self):
        columnCount = 2
        rowCount = 2
        grid = [1, 0, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([0,1,0,0], output["board"]["grid"])

    def test_swipe_FunctionalTest02(self):
        columnCount = 2
        rowCount = 2
        grid = [0, 1, 0, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        grid = output["board"]["grid"]

        self.assertEqual(1, grid[0])


    def test_swipe_FunctionalTest03(self):
        columnCount = 2
        rowCount = 4
        grid = [0, 1, 1, 0, 1, 0, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([0, 1, 0, 1, 0, 1, 0, 0], output["board"]["grid"])

    def test_swipe_FunctionalTest04(self):
        columnCount = 4
        rowCount = 2
        grid = [1, 2, 3, 0, 1, 2, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([0, 1, 2, 3, 0, 0, 1, 2], output["board"]["grid"])


    def test_swipe_FunctionalTest05(self):
        columnCount = 2
        rowCount = 4
        grid = [1, 4, 3, 0, 1, 2, 0, 0]
        direction = "down"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([0, 0, 1, 0, 3, 4, 1, 2], output["board"]["grid"])


    def test_swipe_FunctionalTest06(self):
        columnCount = 4
        rowCount = 2
        grid = [0, 1, 0, 0, 0, 0, 0, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([1, 0, 0, 0, 0, 0, 0, 0], output["board"]["grid"])


    def test_swipe_FunctionalTest07(self):
        columnCount = 4
        rowCount = 2
        grid = [0, 1, 1, 1, 0, 0, 0, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([2, 1, 0, 0, 0, 0, 0, 0], output["board"]["grid"])


    def test_swipe_FunctionalTest08(self):
        columnCount = 4
        rowCount = 2
        grid = [0, 1, 1, 1, 1, 1, 0, 0]
        direction = "down"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual([0, 0, 0, 0, 1, 2, 1, 1], output["board"]["grid"])


    def test_swipe_Score01(self):
        columnCount = 4
        rowCount = 2
        grid = [0, 1, 1, 1, 1, 1, 0, 0]
        direction = "down"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual(4, output["score"])


    def test_swipe_Score02(self):
        columnCount = 4
        rowCount = 2
        grid = [1, 3, 3, 0, 2, 2, 0, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = deterministicSwipe(input)

        self.assertEqual(2**4 + 2**3, output["score"])


