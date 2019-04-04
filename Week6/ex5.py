def function_names(input_file):
    '''(io.TextIOWrapper) -> list of str
    The function return all of the function name in the input_file
    REQ: input_file needs to be a file open for reading
    '''
    # creat a blank list
    function_name_list = []
    # loop through each line in the file
    for next_line in input_file:
        # remove the \n in string
        next_line = next_line.strip('\n')
        # the line is start with 'def'
        if(next_line.startswith('def') is True):
            # there is a space after 'def'
            if(next_line[3] == ' ' and next_line[4] != ' '):
                # fine the index of ()
                index_left_bracket = next_line.find('(')
                index_right_bracket = next_line.find(')')
                # there exists the ()
                if(index_left_bracket != -1 and index_right_bracket != -1):
                    # there is no space before the (
                    if(next_line[index_left_bracket - 1] != ' '):
                        # the last characteristic is :
                        if(next_line[-1] == ':'):
                            # get the function name
                            function_name = next_line[4:index_left_bracket]
                            # add the function name to the list
                            function_name_list.append(function_name)
    return function_name_list


def justified(input_file):
    '''(io.TextIOWrapper) -> bool
    The function return whether every line in file is left_justified
    REQ: input_file needs to be a file open for reading
    '''
    # creat a blank bool list
    every_line_check = []
    # loop evert line in input file
    for next_line in input_file:
        # it is not the blank line
        if(next_line != ''):
            # the line starts with something other than a space
            if(next_line.startswith(' ') is False):
                # this line is left_justified
                every_line_check.append(True)
            # the line starts with a space
            else:
                every_line_check.append(False)
        else:
            every_line_check.append(True)
    # not every line in the file is left_justified
    if(False in every_line_check):
        result = False
    # every line in the file is left_justified
    else:
        result = True
    return result


def section_average(input_file, section_code):
    '''(io.TextIOWrapper, str) -> int
    The function return the average midterm mark in that section or None
    REQ: input_file needs to be a file open for reading
    '''
    # the number of stuent in this section
    number_of_student = 0
    # creat a total mark
    total_mark = 0
    # creat a line list
    each_line_list = []
    # loop each lines
    for next_line in input_file:
        # split each line
        each_line_list = next_line.split()
        # the student in this line is in the specific section
        if(section_code in each_line_list):
            # add the student mark to total marks
            total_mark += float(each_line_list[len(each_line_list) - 1])
            # get the number of student in this section
            number_of_student += 1
    # there is no student in this section
    if(number_of_student == 0):
        average_mark = None
    # get the average mark
    else:
        average_mark = total_mark / number_of_student
    return average_mark
