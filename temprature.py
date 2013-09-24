def convert_to_celsius(fahrenheit):
    '''(number)-> float

    Return the number of celsius degrees equivalent to fagrenheit degrees.
    >>>convert_to_celsius(32)
    0.0
    >>>convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5/9

def colder_temprature(temp1, temp2):
    '''(number, number)-> number
    Return the colder of the two tempratures, temp1(degree celsius) and temp2(degree fahrenheit), in degree celsius.
    '''

   temp2_celsius = convert_to_celsius(temp2)
   return min(temp1, temp2_celsius)

convert_to_celsius(usa_city_temprature("Seattle"))
