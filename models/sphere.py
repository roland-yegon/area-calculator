""" A script that contains functions for area of a sphere """

# Imports
import models.lengthunit as lengthunit
import models.radius as radius

# Function for area of a sphere
def sphere():
    # Inputs
    r = radius.radius()
    units = lengthunit.length_unit()

    # Calculation
    pi = 3.141592653589793
    area = 4 * pi * r**2

    return print(f'The area of your sphere is: {area} {units}')
