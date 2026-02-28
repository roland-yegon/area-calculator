""" A script that calculates the area of a triangle """

# Imports
import models.base as base
import models.height as height
import models.unit as unit

# Main function
def triangle():
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a triangle')
    print('=' * 30)

    b = base.base()
    h = height.height()

    print('\n')
    print('We\'ll assume both base and height are in the same unit')
    units = unit.unit()

    # Calculations
    area = 0.5 * b * h

    print('\n')
    return print(f"The area of the triangle is: {area} {units}")
