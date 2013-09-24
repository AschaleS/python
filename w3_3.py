def same_abs(num1, num2):
    ''' (number, number) -> bool
    Return True if and only if num1 and num2 have the same
    absolute value.
    >>> same_abs(12.5, -12.5)
    True
    >>> same_abs(3, 4.5)
    False
    '''
    return abs(num1) == abs(num2)
##    if abs(num1) == abs(num2):
##        return True
##    else:
##        return False

def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temprature in degrees celsius
    is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    >>> inhospitable_weather(-21.5)
    True
    '''
    return temp > 28 or temp < 12
       
##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
