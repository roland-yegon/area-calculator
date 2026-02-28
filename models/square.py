""" A script that calculates the area of a square """

# Imports
import models.length as length
import models.unit as unit

# Main Function
def square():
    # Input
    print('\n')
    print('=' * 30)
    print('\tThe area of a Square')
    print('=' * 30)

    l = length.length()
    units = unit.unit()

    # Calculations
    area = l**2

    return print(f'\nThe area of the square is: {area} {units}\n')
