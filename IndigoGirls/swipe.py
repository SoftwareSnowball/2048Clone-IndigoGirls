'''
    Created  on October 19, 2017


    @Author: James Malloy

    Purpose of File:
        Holds swipe function which performs the swipe task in the game

'''

from IndigoGirls.ElementLine import ElementLine


def swipe(input):

    #------------------------------------------------------------#
    #HELPER FUNCTIONS

    #Function is used to simplify the validity check for both rowCount and columnCount
    #This function is also declared in initializeGame.
    #TODO: refactor this into its own file
    def isNotValidNumber(x):
        if (type(x) is not int):
            return True

        if ((x <= 1) or (x > 100)):
            return True

        return False




    #Moves all tiles as far right as it can without merging
    #returns true if a tile was moved. False otherwise
    def sweep(elementLine):

        lastEmpty = -1
        index = elementLine.getLength() - 1

        #find last empty index
        while (index >= 0 and lastEmpty == -1) :
            if (elementLine.getElement(index) == 0 ):
                lastEmpty = index

            index -= 1

        #List is full and nothing can be swept
        if (lastEmpty == -1):
            return False

        didBoardChange = False
        index = lastEmpty

        while (index >= 0 ):

            if (elementLine.getElement(index) != 0 ):
                elementLine.swap(index, lastEmpty)
                lastEmpty -= 1
                didBoardChange = True

            index -= 1

        return didBoardChange

    #Merges tiles to the right of the array.
    #Returns a dictionary containing "score" and "didBoardChange"
    #As a precondition there must be no empty spaces to the right of any tile
    #Algorithm:
    #   index = next to last index
    #
    #   while there is an element at index and index GE 0
    #
    #       if can merge with next element then merge
    #       decrement index
    #
    #   sweep the element line
    #
    #   return
    #
    #This should never merge anything twice since after a merge the next index will contain 0
    #
    #
    #
    #
    def merge(elementLine):

        index = elementLine.getLength() - 2
        result = {"didBoardChange": 0, "score": 0}
        #TODO: add score system

        while (index >= 0 and elementLine.getElement(index) != 0):

            prev = elementLine.getElement(index + 1)
            current = elementLine.getElement(index)

            if (prev == current):

                elementLine.setElement(index + 1, current + 1)
                elementLine.setElement(index, 0)
                result["didBoardChange"] = True

            index -= 1

        #TODO: refactor
        #TODO: move sweep the end sweep outside the function or move the initial sweep to the start of the function
        sweep(elementLine)

        return result

    #END OF HELPER FUNCTION CODE
    # ------------------------------------------------------------#


    board = input["board"]
    direction = input["direction"]

    errorMessage = "Error: "
    error = False

    if (type(direction) is not str):
        errorMessage += "Direction must be string. "
        error = True

    if (direction is not "up" and direction is not "down" and direction is not "left" and direction is not "right"):
        errorMessage += "Direction not recognized. "
        error = True

    if (isNotValidNumber(board["rowCount"])):
        errorMessage += "rowCount is invalid. "
        error = True

    if (isNotValidNumber((board["columnCount"]))):
        errorMessage += "columnCount is invalid. "
        error = True

    if (error):
        return {"gameStatus": errorMessage}

    # I don't want this code to run if rowCount or columnCount is not valid because it could cause an exception
    if (len(board["grid"]) != board["rowCount"] * board["columnCount"]):
        errorMessage += "Grid size is invalid. "
        return {"gameStatus": errorMessage}

    # At this point everything should be valid.


    elementLines = []
    index = 0
    didBoardChange = False

    if (direction == "left" or direction == "right"):
        numberOfLines = board["rowCount"]
    else:
        numberOfLines = board["columnCount"]

    while (index < numberOfLines):
        elementLines.append(ElementLine(board, direction, index))
        index += 1

    for elementLine in elementLines:
        didBoardChange |= sweep(elementLine)
        mergeResults = merge(elementLine)
        didBoardChange |= mergeResults["didBoardChange"]

    answer = {"board": board}

    return answer
