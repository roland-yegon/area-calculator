""" A script that calculates the Surface area of a cone """

# Imports
import models.radius as radius
import models.unit as unit

# Function that calculates
def cone():
    # Inputs
    print('\n')
    print('=' * 30)
    print('\tArea of a cone')
    print('=' * 30)
    
    coneoptions = ['1', '2']
    conetype = None

    print('''
What type of cone are you dealing with
    1.  Open
    2.  Closed
''')

    while conetype not in coneoptions:
        conetype = input('What is the type of cone(1/2): ')
    
    r = radius.radius()
    units = unit.unit()

    # Calculations
    pi = 3.141592653589793
    
    if conetype == '1':
        area = (1 / 3) * pi * r**2
    else:
        area = (1 / 3) * pi * r**2 + pi * r**2

    return print(f"\nThe area of the cone is: {area} {units}\u00b2\n")