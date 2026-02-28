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
    pi = 22 / 7
    area = 4 * pi * r**2

    print(f'The area of your sphere is: {area} {units}')

    return area