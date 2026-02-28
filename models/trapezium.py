""" A script that calculates the area of a trapezium """

# Imports
import models.base as base
import models.top as top
import models.height as height
import models.unit as unit

# Main function
def trapezium():
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a trapezium')
    print('=' * 30)

    b = base.base()
    t = top.top()
    h = height.height()

    print('\n')
    print('We\'ll assume the base, top and height all have the same unit')
    units = unit.unit()

    # Calculation
    area = 0.5 * h * (b + t)

    return print(f'\nThe area of the trapezium is: {area} {units}')
