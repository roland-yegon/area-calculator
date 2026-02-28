""" A script that contains functions for area of a sphere """

# Imports
import models.unit as unit
import models.radius as radius

# Function for area of a sphere
def sphere():
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a sphere')
    print('=' * 30)

    r = radius.radius()
    units = unit.unit()

    # Calculation
    pi = 3.141592653589793
    area = 4 * pi * r**2

    print('\n')
    return print(f'\nThe area of your sphere is: {area} {units}\n')
