def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from L
    concatenated together, starting with indices 0 and 1, 2 and 3,
    and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list

def even_sum(s):

    i = 524
    total = 0
    while i <= 10508:
        total = total + sum(i)
        i = i + 2

    return total

def sum_even(a, b):
    count = 0
    for i in range(a, b, 1):
        if i % 2 == 0:
            count = count + i

    return count
