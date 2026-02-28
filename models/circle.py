""" A script containing functions for area operations of a circle """

# Import required functions
import models.lengthunit as lengthunit
import models.radius as radius

# Function for the area of a circle
def circle():
    # Radius input
    r = radius.radius()

    # Units input
    units = lengthunit.length_unit()

    # Area calculation
    pi = 3.141592653589793
    area = pi * r**2

    # Result output
    return print(f'The area of the circle is: {area} {units}')
