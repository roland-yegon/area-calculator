""" A script that contains all known problems """

#A function for all problems
def available_problems():

    # Displaying that can be solved
    print("""
Available shapes to calculate area:
    1.  Circle
    2.  Semi-circle
    3.  Surface Area of a Sphere
    4.  Surface Area of a Cone
    5.  Triangle
    6.  Rectangle
    7.  Square      
    8.  Rhombus 
    9.  Parralelogram
    10. Trapezium
""")

    problems_options = range(1,11)
    problems_choice = None

    while problems_choice not in problems_options:
        problems_choice = int(input('Choose one above(1-10): '))

    return problems_choice