import triangle

def area(sidelength):
    ''' (number) -> float
    Return the area of an equilateral triangle with sides of lenght sidelength.
    >>> area(5)
    10.825317547305483
    '''
    return triangle.area_hero(sidelength, sidelength, sidelength)
