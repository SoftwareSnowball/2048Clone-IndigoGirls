"""
    Created on October 19, 2017

    @Author: James Malloy

    This file contains tests to insure that dispatch is properly calling
    any new modules that I add to the program.

    So far it only tests swipe
"""



from unittest import TestCase
from IndigoGirls.dispatch import dispatch

import json

class IntegrationTests(TestCase):

    def test_swipeIntegration01(self):
        columnCount = 2
        rowCount = 2
        grid = [0] * 4
        direction = 3

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        message = {"board": board, "direction": direction, "op": "swipe"}

        jInput = json.dumps(message)


        joutput = dispatch(jInput)

        output = json.loads(joutput)

        self.assertTrue("error" in output["gameStatus"])

    def test_swipeIntegration02(self):
        columnCount = 2
        rowCount = 2
        grid = [0,0,1,1]
        direction = "up"

        board = {"columnCount": columnCount, "rowCount": rowCount, "grid": grid}
        message = {"board": board, "direction": direction, "op": "swipe"}

        jInput = json.dumps(message, ensure_ascii=True)

        joutput = dispatch(jInput)

        print(joutput)

        output = json.loads(joutput)

        grid = output["board"]["grid"]

        self.assertEquals(grid[0], 1)
        self.assertEquals(grid[1], 1)
