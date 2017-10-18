'''
    Created  on October 17, 2017
    Modified on October 18, 2017

    @Author: James Malloy

    Purpose of File:
        To implement the ElementLine class. This will be an abstraction
        used to make the swipe operations easier

'''


class ElementLine:

    #Grid will hold reference to a matrix
    _grid = []
    #The starting element of the line. Every other line member will be accessed relative to this index.
    _initialIndex = 0
    #stride will be the distance traveledbto reach the next element in the line
    _stride = 0
    #Number of elements in the Element Line
    _length = 0

    def __init__(self, board, direction, lineNumber):
    #decision: The lineNumber will go from 0 to columnCount - 1 or rowCount - 1
        self._grid = board["grid"]

        columns = board["columnCount"]
        rows = board["rowCount"]

        if (direction == "right"):
            self._initialIndex = columns * lineNumber
            self._stride = 1
            self._length = columns

        if (direction == "left"):
            self._initialIndex = (columns * lineNumber) + (columns - 1)
            self._stride = -1
            self._length = columns

        if (direction == "down"):
            self._initialIndex = lineNumber
            self._stride = columns
            self._length = rows

        if (direction == "up"):
            self._initialIndex = lineNumber + columns * (rows - 1)
            self._stride = -columns
            self._length = rows

    def _transform(self, index):
        realIndex = self._initialIndex
        realIndex += self._stride * index

        return realIndex


    def getElement(self, index):

        if (index >= self._length or index < 0):
            return "Error: Index out of bounds"

        realIndex = self._transform(index)
        element = self._grid[realIndex]

        return element


    def setElement(self, index, element):

        realIndex = self._transform(index)

        realIndex = self._transform(index)
        self._grid[realIndex] = element


    def getLength(self):
        return self._length


