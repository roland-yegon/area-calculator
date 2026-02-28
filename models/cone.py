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
    
    coneoptions = ['open', 'closed']
    conetype = None

    while conetype not in coneoptions:
        conetype = input('What is the type of cone(closed/open): ').lower()
    
    r = radius.radius()
    units = unit.unit()

    # Calculations
    pi = 3.141592653589793
    
    if conetype != 'closed':
        area = (1 / 3) * pi * r**2
    else:
        area = (1 / 3) * pi * r**2 + pi * r**2

    print('\n')
    return print(f"The area of the cone is: {area} {units}")