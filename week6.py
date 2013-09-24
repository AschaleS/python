def count_adjacent_repeats(s):
    ''' (str) -> int
    Return the number of occurences of a character and an adjacent
    character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0
    for i in range (len(s) - 1):
        if s[i] == s[i+1]:
            repeats = repeats + 1

    return repeats


def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left and shift the
    first item to the last position.

    Precondition: len(L) >= 1
    '''

    first_item = L(0)

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

def sum_items(list1, list2):
    '''(list of numbers, list of numbers) -> list of numbers

    Return a new list in which each item is the sum of the list
    of the corresponding position of list1 and list2.

    precondition: len(list1) == len(list2)

    >>> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''

    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contain the same
    character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)
    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''

    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches

def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return  the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)

def averages(grades):
    '''
    (list of list of numbers)-> list of float
    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position of
    grades.
    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []
    for grade_list in grades:
        # Calculate the average of grade_list and append it
        # to average.

        total = 0
        for mark in grade_list:
            total = total + mark
        averages.append(total / len(grade_list))
    return averages

def mystery(lst):
    
    for sublist in lst:
        total = 0
        for num in sublist:
            total = total + num
            
    return total
    
