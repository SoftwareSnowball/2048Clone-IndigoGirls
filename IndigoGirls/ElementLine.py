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
        pass


    def getElement(self, index):
        pass


    def setElement(self, index, element):
        pass

    def getLength(self):
        return self._length


