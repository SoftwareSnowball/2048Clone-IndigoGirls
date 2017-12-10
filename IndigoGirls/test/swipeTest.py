'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Tests functionality of the swipe function

'''

from unittest import TestCase

from IndigoGirls.swipe.swipe import swipe


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


class swipeTest(TestCase):
    # Invalid input tests

    def test_swipe_ValidateDirection01(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = 3

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateDirection02(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = "north"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateRow01(self):
        columnCount = 2
        rowCount = 1
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateRow02(self):
        columnCount = 2
        rowCount = 101
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateColumn01(self):
        columnCount = 1
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateColumn02(self):
        columnCount = 101
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateColumn03(self):
        columnCount = "6"
        rowCount = 2
        grid = [0] * 2
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_ValidateGrid01(self):
        columnCount = 3
        rowCount = 2
        grid = [0] * (3 * 2 - 1)
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_invalid_grid01(self):
        columnCount = 3
        rowCount = 2
        grid = [0] * (3 * 2 + 50)
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_invalid_grid02(self):
        columnCount = 3
        rowCount = 2
        grid = [1,2,3,4,5,0,0,3,4,5,3,2]
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])

    def test_swipe_Unmovable01(self):
        columnCount = 2
        rowCount = 2
        grid = [1, 0, 4, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        self.assertIn("error", output["gameStatus"])


    def test_swipe_Normal01(self):
        columnCount = 2
        rowCount = 2
        grid = [0, 1, 0, 1]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        grid = output["board"]["grid"]

        self.assertEquals(grid[0], 1)
        self.assertEquals(grid[2], 1)
        self.assertEquals(output["score"], 0)
        self.assertTrue(grid[1] != 0 or grid[3] != 0)

    def test_swipe_Normal02(self):
        columnCount = 2
        rowCount = 2
        grid = [1, 0, 1, 0]
        direction = "right"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        grid = output["board"]["grid"]

        self.assertEquals(grid[1], 1)
        self.assertEquals(grid[3], 1)
        self.assertEquals(output["score"], 0)
        self.assertTrue(grid[0] != 0 or grid[2] != 0)


    def test_swipe_Normal03(self):
        columnCount = 2
        rowCount = 2
        grid = [0, 0, 1, 1]
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        grid = output["board"]["grid"]

        self.assertEquals(grid[1], 1)
        self.assertEquals(grid[0], 1)
        self.assertEquals(output["score"], 0)


    def test_swipe_Normal04(self):
        columnCount = 2
        rowCount = 2
        grid = [1, 1, 1, 1]
        direction = "down"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        grid = output["board"]["grid"]

        self.assertEquals(grid[3], 2)
        self.assertEquals(grid[2], 2)
        self.assertEquals(output["score"], 8)

    def test_swipe_Normal05(self):
        columnCount = 4
        rowCount = 2
        grid = [0, 1, 1, 1, 0, 0, 0, 0]
        direction = "left"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        input = {"board": board, "direction": direction}

        output = swipe(input)

        grid = output["board"]["grid"]

        self.assertEqual(grid[0], 2)
        self.assertEqual(grid[1], 1)
        self.assertEqual(output["score"], 4)