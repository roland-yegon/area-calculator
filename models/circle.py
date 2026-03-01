""" A script containing functions for area operations of a circle """

# Import required functions
import models.unit as unit
import models.radius as radius

# Function for the area of a circle
def circle():
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a circle')
    print('=' * 30)
    
    r = radius.radius()
    units = unit.unit()

    # Area calculation
    pi = 3.141592653589793
    area = pi * r**2

    # Result output
    return print(f'\nThe area of the circle is: {area} {units}\u00b2\n')
