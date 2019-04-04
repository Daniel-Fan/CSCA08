def create_dict(input_file):
    '''(io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    read a file that each line will have a username, first name, last name,
    age, gender and an e-mail address, all separated by spaces.
    The function will insert each person's information into a dictionary
    with their username as the key, and the value being a list of
    [last name, first name, e-mail, age, gender]. return the dictionary
    REQ: input_file need to be like the provided ex7 data.txt
    '''
    # creat a empty dictionnary
    result_dictionary = {}
    # username as Key_word postion
    Key_word_index = 0
    # read every line in input_file
    for next_line in input_file:
        # split every string to list
        next_line = next_line.split()
        # the username is key and rest of list is the value
        result_dictionary[next_line[Key_word_index]] = next_line[
            Key_word_index + 1:]
    # return the dictionary
    return result_dictionary


def position_of_name(field_name):
    '''(dict) -> int
    return the position of field in a list according to the field_name
    REQ: name of a field (One of: 'LAST', 'FIRST', 'E-MAIL', 'AGE' or 'GENDER')
    >>> position_of_name('LAST')
    0
    '''
    # 'LAST' in the list[0]
    if(field_name == 'LAST'):
        position = 0
    # 'FIRST' in the list[1]
    elif(field_name == 'FIRST'):
        position = 1
    # 'E-MAIL' in the list[2]
    elif(field_name == 'E-MAIL'):
        position = 2
    # 'AGE' in the list[3]
    elif(field_name == 'AGE'):
        position = 3
    # 'GENDER' in the list[4]
    elif(field_name == 'GENDER'):
        position = 4
    return position


def update_field(created_dictionary, username, field_name, replace_value):
    '''(dict, str, str, obj) -> None
    let a new value to replace the current value of the specified field.
    REQ: A dictionary in the format created by the previous function
    REQ: a username
    REQ: name of a field (One of: 'LAST', 'FIRST', 'E-MAIL', 'AGE' or 'GENDER')
    >>> my_dict = {'sclause':['Clause', 'Santa', 'san@christ.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause': ['Clause', 'Santa', 'san@christ.np', 999, 'M']}
    True
    '''
    # find the postion of field_name in the list
    position_in_list = position_of_name(field_name)
    # change the value of specified field
    created_dictionary[username][position_in_list] = replace_value
    return None


def select(my_dict, field_selected, field_checked, checked_value):
    '''(dict, str, str, str) -> set
    return a set of all the data elements from the selected fields of people
    whose checked fields were equal to the checked value
    REQ: A dictionary in the format created by the previous function
    REQ: name of a field (One of: 'LAST', 'FIRST', 'E-MAIL', 'AGE' or 'GENDER')
    '''
    # the set have not been created
    exists_set = False
    # find the position of selected field
    pos_of_selected = position_of_name(field_selected)
    # find the position of checked field
    pos_of_checked = position_of_name(field_checked)
    # loop every key in the dict
    for key in my_dict:
        # the first time to find selected fields of people
        # whose checked fields were equal to the checked value
        if(my_dict[key][pos_of_checked] == checked_value and
           exists_set is False):
            # create a set to store the select field and exist a set
            selected_set = {my_dict[key][pos_of_selected]}
            exists_set = True
        # there exist a set for the selected field
        elif(my_dict[key][pos_of_checked] == checked_value and
             exists_set is True):
            # add the select field to the set
            selected_set.add(my_dict[key][pos_of_selected])
    # return the set
    return selected_set
