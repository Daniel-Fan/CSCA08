import math


class Parallelogram():
    '''this is the class representing Parallelogram'''
    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> NoneType
        make an object by initializing the instance variables
        REQ: the theta cannot be greater than 90
        '''
        self._base = base
        self._side = side
        self._theta = theta
        # calculate the area by base * side * sin(theta)
        self._area =\
            self._base * self._side * math.sin(math.radians(self._theta))

    def __str__(self):
        '''(Parallelogram) -> str
        return a sentence with shape and area
        '''
        # set a name of shape
        self._name = 'Parallelogram'
        return 'I am a ' + self._name + ' with area ' + str(self._area)

    def area(self):
        ''' (Parallelogram) -> float
        returns the area of the shape
        '''
        return self._area

    def bst(self):
        '''(Parallelogram) -> list
        return a list that contains three floats [base, side, theta]
        '''
        # set a empty list and add the element to a list
        result_list =\
            [float(self._base), float(self._side), float(self._theta)]
        return result_list


class Rectangle(Parallelogram):
    '''this is the class representing Rectangle'''
    def __init__(self, base, side):
        '''(Rectangle, float, float) -> Nonetype
        make an object by initializing the instance variables
        '''
        # the theta of rectangle is 90 degrees
        theta = 90
        # initialize the shared variables
        super().__init__(base, side, theta)

    def __str__(self):
        '''(Rectangle) -> str
        return a sentence with shape and area
        '''
        # set a name of shape
        self._name = 'Rectangle'
        return 'I am a ' + self._name + ' with area ' + str(self._area)


class Rhombus(Parallelogram):
    '''this is the class representing Rhombus'''
    def __init__(self, base, theta):
        '''(Rectangle, float, float) -> Nonetype
        make an object by initializing the instance variables
        '''
        # the side and base of Rhombus is same
        side = base
        # initialize the shared variables
        super().__init__(base, side, theta)

    def __str__(self):
        '''(Rhombus) -> str
        return a sentence with shape and area
        '''
        # set a name of shape
        self._name = 'Rhombus'
        return 'I am a ' + self._name + ' with area ' + str(self._area)


class Square(Rhombus, Rectangle):
    '''this is the class representing Square'''
    def __init__(self, base):
        '''(Rectangle, float) -> Nonetype
        make an object by initializing the instance variables
        '''
        # initialize the shared variables
        Rectangle.__init__(self, base, base)

    def __str__(self):
        '''(Square) -> str
        return a sentence with shape and area
        '''
        # set a name of shape
        self._name = 'Square'
        return 'I am a ' + self._name + ' with area ' + str(self._area)
