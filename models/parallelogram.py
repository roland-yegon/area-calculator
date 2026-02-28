""" A script that calculates the area of a parallelogram """

# Imports
import models.base as base
import models.height as height
import models.diagonal as diagonal
import models.unit as unit

# Main function
def parallelogram():
    #Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a parallelogram')
    print('=' * 30)

    areaoptions = ['1', '2']
    areachoice = None

    print('''
The available options for area of parallelogram:
    1.  Through diagonals
    2.  Through base and height          
''')

    while areachoice not in areaoptions:
        areachoice = input('Enter the method type(1/2): ')

    if areachoice == '1':
        d1 = diagonal.diagonal()
        print('Now enter the second digonal')
        d2 = diagonal.diagonal()

        print('\n')
        print('We\'ll assume both diagonals have the same unit')
        units = unit.unit()

        area = 0.5 * d1 * d2

    else:
        b = base.base()
        h = height.height()

        print('\n')
        print('We\'ll assume both base and height have the same unit')
        units = unit.unit()

        area = b * h

    return print(f'The area of the parallelogram is: {area} {units}')
