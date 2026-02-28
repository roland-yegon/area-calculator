""" A script that calculate are of a semicircle """

# Import
import models.radius as radius
import models.unit as unit

# Function for semi circle area
def semi_circle():
    # Inputs
    r = radius.radius()
    units = unit.unit()

    # Calculations
    pi = 3.141592653589793
    area = 0.5 * pi * r**2

    return print(f"The area of the semicircle is: {area} {units}")
