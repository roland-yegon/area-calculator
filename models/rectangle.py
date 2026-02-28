""" A Script that Calculates the area of a rectangle """

# Imports
import models.length as length
import models.width as width
import models.unit as unit

#Main function
def rectangle():    
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a rectangle')
    print('=' * 30)

    l = length.length()
    w = width.width()

    print('\n')
    print('We\'ll assume both length and width have the same unit')
    units = unit.unit()

    # Calculations
    area = l * w

    return print(f'\nThe area of the rectangle is: {area} {units}\n')