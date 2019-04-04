# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 25
exam_weight = 40
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of Ex2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    value_of_percentage = (raw_mark / max_mark) * 100
    return value_of_percentage


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    # return the number of marks it contributes to the final course mark.
    result = raw_mark / max_mark * weight
    return result


def term_work_mark(a0, a1, a2, exercises, quizzes, term_test_marks):
    '''(float, float, float, float, float, float) -> float
    Given the marks of each term which the student earned.
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= term_test_mark <= 50
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    60.0
    '''
    # calculate a0's contribution to our final marks.
    a0 = contribution(a0, a0_max_mark, a0_weight)
    # calculate a1's contribution to our final marks.
    a1 = contribution(a1, a1_max_mark, a1_weight)
    # calculate a2's contribution to our final marks.
    a2 = contribution(a2, a2_max_mark, a2_weight)
    # calculate exercises's contribution to our final marks.
    exercises = contribution(exercises, exercises_max_mark, exercises_weight)
    # calculate quizzes's contribution to our final marks.
    quizzes = contribution(quizzes, quizzes_max_mark, quizzes_weight)
    # calculate term_test_marks's contribution to our final marks.
    term_test_marks = contribution(term_test_marks, term_tests_max_mark,
                                   term_tests_weight)
    # calculate the sum of contribution.
    value = a0 + a1 + a2 + exercises + quizzes + term_test_marks
    # return the sum of each term work's contribution
    return value


def final_mark(a0, a1, a2, exercises, quizzes, term_test_marks, final_exam):
    '''(float, float, float, float, float, float, float) -> float
    Given the every mark of terms
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= term_test_mark <= 50
    REQ: 0 <= final_exam <= 100
    >>> final_mark(25, 50, 100, 10, 5, 50,100)
    100.0
    >>> final_mark(20, 45, 70, 8, 4, 40, 73)
    77.1
    '''
    # calculate final_exam's contribution to our final marks.
    final_exam = contribution(final_exam, exam_max_mark, exam_weight)
    # calculate final marks.
    final_grades = (term_work_mark(a0, a1, a2, exercises, quizzes,
                                   term_test_marks) + final_exam)
    # return final_grades
    return final_grades


def is_pass(a0, a1, a2, exercises, quizzes, term_test_marks, final_exam):
    '''(float, float, float, float, float, float, float) -> bool
    Given the each mark of the term_work and fianl exam.
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= term_test_mark <= 50
    REQ: 0 <= final_exam <= 100
    >>> is_pass(20, 45, 70, 8, 4, 40, 41)
    True
    >>> is_pass(20, 45, 70, 8, 4, 40, 39)
    False
    >>> is_pass(10, 21, 12, 2, 1, 15, 23)
    False
    '''
    # We need to test the marks of final_mark and final_exam.
    # if you want to pass the course.
    # you must get a final overall mark at or above 50.
    # as well as an exam mark at or above 40.
    if_Pass = (final_mark(a0, a1, a2, exercises, quizzes, term_test_marks,
                          final_exam) >= overall_pass_mark and
               final_exam >= exam_pass_mark)
    return if_Pass
