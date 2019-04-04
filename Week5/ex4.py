def insert(objectA, objectB, index):
    '''(obj, obj, int) -> obj
    return a copy of objectA with the elements of objectB inserted at the index
    REQ: index < len(objectA)
    REQ: need to be both list or string
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # add the first part of objectA to a new object
    new_object = objectA[0:index]
    # add the objectB to new_list
    new_object += objectB
    # add the remaining of objectA
    new_object += objectA[index:]
    # return the new_object
    return new_object


def up_to_first(objectA, objectB):
    '''(obj, obj) -> obj
    returns the objectA up to the first objectB
    REQ: objectA need to be a string or list
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first('abcdef', 'd')
    'abc'
    '''
    # loop the objectA
    for element in objectA:
        # find the objectB in objectA
        if(element == objectB):
            # assign the objectA up to the first objectB to new_object
            new_object = objectA[:objectA.index(element)]
            # return the new_object
            return new_object
        # there is no objectB in objectA
        new_object = objectA
    return new_object


def cut_list(objectA, index):
    '''(obj, int) -> obj
    The function swap the items before and after the index item
    REQ: objectA needs to be string or list
    REQ: index < len(objectA)
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # get the items after the index item
    first_object = objectA[index+1:]
    # get the items before the index item
    second_object = objectA[:index]
    # the object is list
    if(type(objectA) == list):
        # put the index item to the end of first_object
        first_object.append(objectA[index])
    # the object is string
    elif(type(objectA) == str):
        # put the index item to the end of first_object
        first_object += objectA[index]
    # combine two objects
    new_object = first_object + second_object
    # return the new_object
    return new_object
