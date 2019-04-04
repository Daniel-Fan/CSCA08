def copy_me(input_list):
    '''(list) -> list
    give the function a list and return a copy of list with some changes
    REQ: input_list cannot be empty
    >>> copy_me([1, 2, 'ABcd', True])
    [2, 3, 'ABCD', False]
    >>> copy_me([5, 6, [1,2,3], False])
    [6, 7, 'List', True]
    '''
    # make a copy of input_list
    new_list = input_list[:]
    # loop every elements in the list
    for index in range(0, len(new_list)):
        # if the element is str
        if(type(new_list[index]) is str):
            # the letters in the str become upper-case
            new_list[index] = new_list[index].upper()
        # if the element is boolean
        elif(type(new_list[index]) is bool):
            # the boolean need to be negation
            new_list[index] = not new_list[index]
        # if the element is int or float
        elif((type(new_list[index]) is int) or
             (type(new_list[index]) is float)):
            # the value increase 1
            new_list[index] += 1
        # if the element is list
        elif(type(new_list[index]) is list):
            # the lists need be the str 'List'
            new_list[index] = 'List'
    # return the new_list
    return new_list


def mutate_me(input_list):
    '''(list) -> None
    return None but change the input_list
    REQ: input_list cannot be empty
    >>> mutate_me([1, 2, 'ABcd', True])
    '''
    # loop every elements in the list
    for index in range(0, len(input_list)):
        # if the element is str
        if(type(input_list[index]) is str):
            # the letters in the str become upper-case
            input_list[index] = input_list[index].upper()
        # if the element is boolean
        elif(type(input_list[index]) is bool):
            # the boolean need to be negation
            input_list[index] = not input_list[index]
        # if the element is int or float
        elif((type(input_list[index]) is int) or
             (type(input_list[index]) is float)):
            # the value increase 1
            input_list[index] += 1
        # if the element is list
        elif(type(input_list[index]) is list):
            # the lists need be the str 'List'
            input_list[index] = 'List'
    # return the None
    return None
