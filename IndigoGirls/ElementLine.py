'''
    Created on October 17, 2017

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

    def __init__(self, board, direction, line_number):

        self._grid = board["grid"]
        self._length = board["columnCount"]

        if (direction == "right"):
            self._initialIndex = 0
            self._stride = 1

        if (direction == "left"):
            self._initialIndex = board["columnCount"] - 1
            self._stride = -1



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
        pass

    def getLength(self):
        return self._length


